#!/usr/bin/env python3
"""
Test script to verify reasoning content is returned from GLM4.7.
"""

import sys
import os
import json

# Add webapp directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "webapp"))

from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "webapp", ".env"))

from llm_client import LLMClient
from prompt_builder import PromptBuilder


def test_reasoning_content():
    """Test that GLM4.7 returns reasoning content."""
    print("=" * 60)
    print("Testing GLM4.7 Reasoning Content")
    print("=" * 60)

    # Initialize components
    llm_client = LLMClient()
    prompt_builder = PromptBuilder()

    # Test parameters
    model = "z-ai/glm4.7"
    monster_concept = "Level 2 Gremlin, Minion Harrier"

    print(f"\n1. Testing with model: {model}")
    print(f"2. Monster concept: {monster_concept}")

    # Build prompt
    print("\n3. Building prompt...")
    system_prompt = prompt_builder.get_system_prompt()
    user_prompt = prompt_builder.build_create_prompt(monster_concept)

    # Generate monster
    print("\n4. Generating monster with GLM4.7...")
    print("   (This may take 20-30 seconds...)")

    llm_response = llm_client.generate(
        system_prompt=system_prompt, user_prompt=user_prompt, model=model
    )

    if not llm_response["success"]:
        print(f"\n✗ Generation failed: {llm_response['error']}")
        return False

    print(f"   ✓ Generation completed")
    print(f"   Tokens used: {llm_response['tokens']['total']}")

    # Check for reasoning content
    print("\n5. Checking for reasoning content...")
    reasoning = llm_response.get("reasoning")

    if reasoning:
        print(f"   ✓ Reasoning content found!")
        print(f"   Reasoning length: {len(reasoning)} characters")
        print(f"   Reasoning preview (first 500 chars):")
        print("-" * 60)
        print(reasoning[:500])
        print("-" * 60)

        # Save reasoning to file
        with open("test_glm47_reasoning.txt", "w") as f:
            f.write(reasoning)
        print(f"\n   Full reasoning saved to: test_glm47_reasoning.txt")
    else:
        print(f"   ✗ No reasoning content found")
        print(f"   Response keys: {llm_response.keys()}")
        return False

    # Check output content
    print("\n6. Checking output content...")
    output = llm_response.get("output", "")
    print(f"   Output length: {len(output)} characters")
    print(f"   Output preview (first 200 chars):")
    print("-" * 60)
    print(output[:200])
    print("-" * 60)

    print("\n" + "=" * 60)
    print("✓ GLM4.7 Reasoning Content Test PASSED!")
    print("=" * 60)
    return True


def main():
    """Run the test."""
    try:
        success = test_reasoning_content()
        return 0 if success else 1
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user")
        return 1
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        import traceback

        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
