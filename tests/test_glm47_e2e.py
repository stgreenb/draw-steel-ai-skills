"""Test GLM 4.7 end-to-end generation"""

import sys
import os
import json

# Add webapp to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "webapp"))

# Load environment
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "webapp", ".env"))

from llm_client import LLMClient
from prompt_builder import PromptBuilder
from response_parser import ResponseParser
from ds_validator import DrawSteelValidator


def test_glm47_generation():
    """Test GLM 4.7 monster generation."""
    print("Testing GLM 4.7 End-to-End Generation...")
    print("=" * 60)

    # Initialize components
    client = LLMClient()
    builder = PromptBuilder()
    parser = ResponseParser()
    validator = DrawSteelValidator()

    # Test parameters
    model = "z-ai/glm4.7"
    concept = "Level 1 goblin, minion organization, skirmisher role"

    print(f"\n1. Test Configuration:")
    print(f"   Model: {model}")
    print(f"   Concept: {concept}")

    # Build prompts
    system_prompt = builder.get_system_prompt()
    user_prompt = builder.build_create_prompt(concept)

    print(f"\n2. Generating monster...")
    print(f"   This will take ~30 seconds...")

    # Generate
    result = client.generate(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        model=model,
    )

    if not result["success"]:
        print(f"\n❌ Generation failed: {result['error']}")
        return False

    print(f"\n✓ Generation successful!")
    print(f"   Time: {result.get('attempts', 1)} attempt(s)")
    print(f"   Model used: {result.get('model_used', 'unknown')}")
    print(
        f"   Tokens: {result['tokens']['total']} (prompt: {result['tokens']['prompt']}, completion: {result['tokens']['completion']})"
    )

    # Parse JSON
    print(f"\n3. Parsing JSON...")
    parsed = parser.parse(result["output"], "json")

    if not parsed["json_data"]:
        print(f"   ❌ Failed to parse JSON")
        print(f"   Output preview: {result['output'][:200]}...")
        return False

    print(f"✓ JSON parsed successfully")

    # Validate
    print(f"\n4. Validating against Draw Steel schema...")
    validation = validator.validate(parsed["json_data"])

    if validation["success"]:
        print(f"✓ Validation passed!")
    else:
        print(f"❌ Validation failed:")
        for error in validation["errors"]:
            print(f"   - {error}")

    # Display monster info
    if parsed["json_data"]:
        monster = parsed["json_data"]
        print(f"\n5. Monster Details:")
        print(f"   Name: {monster.get('name', 'Unknown')}")
        print(f"   Level: {monster.get('system', {}).get('level', 'Unknown')}")
        print(
            f"   Organization: {monster.get('system', {}).get('monster', {}).get('organization', 'Unknown')}"
        )
        print(
            f"   Role: {monster.get('system', {}).get('monster', {}).get('role', 'Unknown')}"
        )
        print(
            f"   Keywords: {monster.get('system', {}).get('monster', {}).get('keywords', [])}"
        )
        print(f"   Abilities: {len(monster.get('abilities', []))}")

    # Save output
    output_file = os.path.join(
        os.path.dirname(__file__), f"glm47_test_output_{os.getpid()}.json"
    )
    with open(output_file, "w") as f:
        json.dump(parsed["json_data"], f, indent=2)
    print(f"\n6. Output saved to: {output_file}")

    print("\n" + "=" * 60)
    if validation["success"]:
        print("✓ GLM 4.7 End-to-End Test PASSED!")
    else:
        print("⚠ GLM 4.7 End-to-End Test COMPLETED (with validation errors)")
    print("=" * 60)

    return validation["success"]


if __name__ == "__main__":
    try:
        success = test_glm47_generation()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)
