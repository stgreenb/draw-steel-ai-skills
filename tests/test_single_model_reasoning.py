#!/usr/bin/env python3
"""
Quick test for a single model to check reasoning support.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "webapp"))

from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "webapp", ".env"))

from llm_client import LLMClient


def main():
    if len(sys.argv) < 2:
        print("Usage: python test_single_model_reasoning.py <model-name>")
        print("\nAvailable models from MODEL_CONFIG:")
        from llm_client import MODEL_CONFIG

        for model in MODEL_CONFIG.keys():
            print(f"  - {model}")
        sys.exit(1)

    model_name = sys.argv[1]
    client = LLMClient()

    print(f"Testing: {model_name}")
    print("=" * 60)

    response = client.generate(
        system_prompt="You are a helpful assistant.",
        user_prompt="What is 2+2? Explain your reasoning.",
        model=model_name,
        reasoning_effort="medium",
    )

    if not response["success"]:
        print(f"✗ Generation failed: {response['error']}")
        sys.exit(1)

    print(f"✓ Generation successful")
    print(f"Tokens: {response['tokens']['total']}")

    reasoning = response.get("reasoning")
    if reasoning:
        print(f"\n✓ Reasoning found ({len(reasoning)} chars):")
        print("-" * 60)
        print(reasoning)
        print("-" * 60)
    else:
        print(f"\n✗ No reasoning found")
        print(f"Response keys: {list(response.keys())}")

        # Try to show message structure
        if "raw_response" in response:
            print(f"Raw response available")


if __name__ == "__main__":
    main()
