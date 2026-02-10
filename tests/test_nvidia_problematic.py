"""Test problematic NVIDIA models"""

import sys
import os
import json
import time
from datetime import datetime
from typing import Dict, Any, List
from dataclasses import dataclass

# Add webapp to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "webapp"))

# Load environment
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

from prompt_builder import PromptBuilder
from response_parser import ResponseParser
from ds_validator import DrawSteelValidator

# Test configurations
NVIDIA_BASE_URL = "https://integrate.api.nvidia.com/v1"
PROBLEMATIC_MODELS = [
    {"model_id": "moonshotai/kimi-k2.5", "name": "Kimi K2.5"},
    {"model_id": "deepseek-ai/deepseek-v3.2", "name": "DeepSeek V3.2"},
    {"model_id": "stepfun-ai/step-3.5-flash", "name": "Step 3.5 Flash"},
]

# Rate limiting for NVIDIA (conservative to avoid rate limits)
NVIDIA_RATE_LIMIT_DELAY = 10.0  # seconds between requests (very conservative)

TEST_MONSTER_CONCEPTS = [
    {
        "id": "fire_dragon",
        "name": "Level 5 Fire Dragon",
        "concept": "Level 5 fire dragon, solo organization, brute role",
    },
]


@dataclass
class NvidiaTestResult:
    """Result of a single NVIDIA model test."""

    model: str
    model_name: str
    success: bool = False
    total_time: float = 0.0
    tokens_prompt: int = 0
    tokens_completion: int = 0
    validation_passed: bool = False
    validation_errors: List[str] = None
    quality_score: int = 0
    thinking_content: str = ""
    output_json: str = ""
    error: str = ""

    def __post_init__(self):
        if self.validation_errors is None:
            self.validation_errors = []


def test_nvidia_model(
    model_id: str,
    model_name: str,
    system_prompt: str,
    user_prompt: str,
    api_key: str,
    test_id: str = None,
) -> NvidiaTestResult:
    """Test a single NVIDIA model with a prompt."""
    import requests

    result = NvidiaTestResult(model=model_id, model_name=model_name)

    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": model_id,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": 0.7,
            "max_tokens": 4096,
            "stream": False,
        }

        start_time = time.time()

        response = requests.post(
            f"{NVIDIA_BASE_URL}/chat/completions",
            json=payload,
            headers=headers,
            timeout=240,  # Increased from 180 to 240 seconds
        )

        response.raise_for_status()

        total_time = time.time() - start_time

        data = response.json()
        choice = data["choices"][0]
        raw_output = choice["message"].get("content", "")

        if not raw_output:
            result.error = "No content in response"
            result.success = False
            return result

        result.output_json = raw_output

        # Extract token usage
        if "usage" in data:
            result.tokens_prompt = data["usage"].get("prompt_tokens", 0)
            result.tokens_completion = data["usage"].get("completion_tokens", 0)

        result.total_time = total_time * 1000  # Convert to ms

        # Try to parse JSON and validate
        parser = ResponseParser()
        parsed = parser.parse(result.output_json, "json")

        # If standard parsing failed, try to extract JSON from the end of the output
        # (NVIDIA models often output thinking content before the JSON)
        if not parsed["json_data"]:
            # Try to find JSON by looking for the last complete JSON object
            json_data = extract_json_from_end(raw_output)
            if json_data:
                parsed["json_data"] = json_data

        # Save raw output for debugging if parsing failed
        if not parsed["json_data"] and test_id:
            debug_file = os.path.join(os.path.dirname(__file__), f"debug_{test_id}.txt")
            with open(debug_file, "w", encoding="utf-8") as f:
                f.write(f"Model: {model_id}\n")
                f.write(f"Test ID: {test_id}\n")
                f.write(f"Raw output:\n{raw_output}\n")
            print(f"    Raw output saved to {debug_file}")

        if parsed["json_data"]:
            validator = DrawSteelValidator()
            validation = validator.validate(parsed["json_data"])
            result.validation_passed = validation["success"]
            result.validation_errors = validation["errors"]
            result.output_json = json.dumps(parsed["json_data"])
        else:
            result.validation_passed = False
            result.validation_errors = ["Failed to parse JSON response"]

        result.success = result.validation_passed
        result.quality_score = calculate_quality_score(result)

    except Exception as e:
        result.error = str(e)
        result.success = False

    return result


def extract_json_from_end(text: str) -> dict:
    """Try to extract JSON from the end of text (handles thinking content)."""
    import re

    # Try to find the last complete JSON object
    # Look for the last occurrence of a pattern that looks like the start of a JSON object
    # and try to parse from there

    # Find all potential JSON start positions
    json_starts = []
    for match in re.finditer(r'\{"_id"', text):
        json_starts.append(match.start())

    # Try parsing from each start position (working backwards)
    for start_pos in reversed(json_starts):
        try:
            json_text = text[start_pos:]
            # Try to balance braces
            brace_count = 0
            in_string = False
            escape_next = False
            end_pos = 0

            for i, char in enumerate(json_text):
                if escape_next:
                    escape_next = False
                    continue
                if char == "\\":
                    escape_next = True
                    continue
                if char == '"' and not escape_next:
                    in_string = not in_string
                    continue
                if not in_string:
                    if char == "{":
                        brace_count += 1
                    elif char == "}":
                        brace_count -= 1
                        if brace_count == 0:
                            end_pos = i + 1
                            break

            if end_pos > 0:
                json_candidate = json_text[:end_pos]
                data = json.loads(json_candidate)
                return data
        except (json.JSONDecodeError, Exception):
            continue

    return None


def calculate_quality_score(result: NvidiaTestResult) -> int:
    """Calculate automated quality score (1-5)."""
    score = 0

    if result.validation_passed:
        score += 2

    if result.validation_errors:
        score -= len(result.validation_errors) * 0.5

    if result.total_time > 0:
        if result.total_time < 5000:
            score += 1
        elif result.total_time < 10000:
            score += 0.5

    if result.tokens_completion > 500:
        score += 0.5
    elif result.tokens_completion < 200:
        score -= 0.5

    if not result.error:
        score += 1

    return max(1, min(5, int(score)))


def run_nvidia_tests(
    models: List[Dict[str, str]],
    concepts: List[Dict[str, str]],
    api_key: str,
    output_file: str = None,
) -> Dict[str, Any]:
    """Run NVIDIA tests on multiple models with multiple concepts."""
    builder = PromptBuilder()
    all_results = []

    print("=" * 60)
    print("NVIDIA API Model Testing (Problematic Models)")
    print("=" * 60)
    print(f"API Base URL: {NVIDIA_BASE_URL}")
    print(f"Models to test: {len(models)}")
    print(f"Concepts to test: {len(concepts)}")
    print(f"Rate limit delay: {NVIDIA_RATE_LIMIT_DELAY}s")
    print("=" * 60)
    print()

    for concept in concepts:
        print(f"\nTesting concept: {concept['name']}")
        print("-" * 60)

        system_prompt = builder.get_system_prompt()
        user_prompt = builder.build_create_prompt(concept["concept"])

        # Add more explicit instructions for NVIDIA models
        user_prompt += '\n\nYour response must be a valid JSON object with this structure:\n{\n  "_id": "16 alphanumeric chars",\n  "type": "npc",\n  "name": "Monster Name",\n  "img": "path/to/image.png",\n  "system": {\n    "level": 5,\n    "ev": 56,\n    "stamina": {"value": 280, "max": 280},\n    ...\n  },\n  "abilities": [...]\n}\n\nDo not include any text, explanations, or markdown formatting - ONLY the JSON object.'

        for model in models:
            print(f"\n  Model: {model['name']} ({model['model_id']})")

            # Rate limiting delay
            if len(all_results) > 0:
                print(f"    Rate limiting: waiting {NVIDIA_RATE_LIMIT_DELAY}s...")
                time.sleep(NVIDIA_RATE_LIMIT_DELAY)

            test_id = f"{concept['id']}_{model['model_id'].replace('/', '_')}"
            result = test_nvidia_model(
                model["model_id"],
                model["name"],
                system_prompt,
                user_prompt,
                api_key,
                test_id,
            )

            # Add concept info to result
            result_dict = {
                "concept_id": concept["id"],
                "concept_name": concept["name"],
                "concept": concept["concept"],
                **{k: v for k, v in result.__dict__.items() if not k.startswith("_")},
            }

            all_results.append(result_dict)

            # Print results
            status = "PASS" if result.validation_passed else "FAIL"
            print(f"    Status: {status}")
            print(f"    Time: {result.total_time:.0f}ms")
            print(
                f"    Tokens: {result.tokens_prompt} prompt, {result.tokens_completion} completion"
            )
            print(f"    Quality: {result.quality_score}/5")

            if result.validation_errors:
                print(f"    Errors: {len(result.validation_errors)}")
                for error in result.validation_errors[:3]:  # Show first 3 errors
                    print(f"      - {error}")

            if result.error:
                print(f"    Error: {result.error}")

    # Compile output data
    output_data = {
        "timestamp": datetime.now().isoformat(),
        "test_config": {
            "api_base_url": NVIDIA_BASE_URL,
            "models": models,
            "concepts": concepts,
            "rate_limit_delay": NVIDIA_RATE_LIMIT_DELAY,
        },
        "results": all_results,
        "summary": {
            "total_tests": len(all_results),
            "passed": sum(1 for r in all_results if r["validation_passed"]),
            "failed": sum(1 for r in all_results if not r["validation_passed"]),
            "avg_time_ms": sum(r["total_time"] for r in all_results) / len(all_results)
            if all_results
            else 0,
            "avg_quality": sum(r["quality_score"] for r in all_results)
            / len(all_results)
            if all_results
            else 0,
        },
    }

    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"Total tests: {output_data['summary']['total_tests']}")
    print(f"Passed: {output_data['summary']['passed']}")
    print(f"Failed: {output_data['summary']['failed']}")
    print(f"Avg time: {output_data['summary']['avg_time_ms']:.0f}ms")
    print(f"Avg quality: {output_data['summary']['avg_quality']:.1f}/5")
    print("=" * 60)

    # Save results to file
    if output_file:
        with open(output_file, "w") as f:
            json.dump(output_data, f, indent=2)
        print(f"\nResults saved to {output_file}")

    return output_data


def main():
    """Main entry point."""
    api_key = os.getenv("NVIDIA_API_KEY")

    if not api_key:
        print("ERROR: NVIDIA_API_KEY not found in environment")
        print("Please add NVIDIA_API_KEY to your .env file")
        sys.exit(1)

    # Generate output filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(
        os.path.dirname(__file__), f"nvidia_problematic_models_{timestamp}.json"
    )

    results = run_nvidia_tests(
        models=PROBLEMATIC_MODELS,
        concepts=TEST_MONSTER_CONCEPTS,
        api_key=api_key,
        output_file=output_file,
    )

    # Exit with error if all tests failed
    if results["summary"]["failed"] == results["summary"]["total_tests"]:
        print("\n❌ All tests failed")
        sys.exit(1)
    else:
        print("\n✓ Tests completed")
        sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)
