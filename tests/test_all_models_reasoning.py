#!/usr/bin/env python3
"""
Test reasoning support for different models.
Tests each model to see if it returns reasoning content.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "webapp"))

from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "webapp", ".env"))

from llm_client import LLMClient, MODEL_CONFIG


def test_model_reasoning(client, model_name, model_config):
    """Test if a model returns reasoning content."""
    print(f"\n{'=' * 60}")
    print(f"Testing: {model_name}")
    print("=" * 60)
    print(f"Base URL: {model_config.get('base_url', 'N/A')}")
    print(f"Supports Reasoning: {model_config.get('supports_reasoning', False)}")
    print(f"Reasoning Type: {model_config.get('reasoning_type', 'N/A')}")

    # Test prompt
    system_prompt = "You are a monster designer for Draw Steel TTRPG."
    user_prompt = "Create a Level 2 Gremlin, Minion Harrier"

    try:
        response = client.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            model=model_name,
            reasoning_effort="medium"
            if model_config.get("reasoning_type") == "standard"
            else None,
        )

        if not response["success"]:
            print(f"\n✗ Generation failed: {response['error']}")
            return False

        print(f"\n✓ Generation successful")
        print(f"  Tokens used: {response['tokens']['total']}")

        # Check for reasoning
        reasoning = response.get("reasoning")
        if reasoning:
            print(f"\n✓ Reasoning content found!")
            print(f"  Length: {len(reasoning)} characters")
            print(f"\n  Preview (first 500 chars):")
            print("-" * 60)
            print(reasoning[:500])
            print("-" * 60)
            return True
        else:
            print(f"\n✗ No reasoning content returned")
            print(f"  Available response keys: {list(response.keys())}")

            # Check message structure
            if "raw_response" in response:
                print(f"  Raw response available")

            return False

    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback

        traceback.print_exc()
        return False


def main():
    """Run reasoning tests for all configured models."""
    print("=" * 60)
    print("Model Reasoning Support Test")
    print("=" * 60)

    client = LLMClient()

    results = {}

    for model_name, model_config in MODEL_CONFIG.items():
        # Skip models without API key
        if not model_config.get("api_key"):
            print(f"\n{'=' * 60}")
            print(f"Skipping: {model_name} (no API key)")
            print("=" * 60)
            continue

        # Test the model
        supports_reasoning = test_model_reasoning(client, model_name, model_config)
        results[model_name] = {
            "config_supports": model_config.get("supports_reasoning", False),
            "actual_supports": supports_reasoning,
            "match": model_config.get("supports_reasoning", False)
            == supports_reasoning,
        }

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    for model_name, result in results.items():
        config_status = "✓" if result["config_supports"] else "✗"
        actual_status = "✓" if result["actual_supports"] else "✗"
        match_status = "✓" if result["match"] else "✗ MISMATCH"

        print(f"\n{model_name}:")
        print(f"  Config: {config_status} | Actual: {actual_status} | {match_status}")

    # Check for mismatches
    mismatches = [m for m, r in results.items() if not r["match"]]
    if mismatches:
        print(f"\n⚠️  Configuration mismatches found for: {', '.join(mismatches)}")
    else:
        print(f"\n✓ All model configurations match actual behavior")


if __name__ == "__main__":
    main()
