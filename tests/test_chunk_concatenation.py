#!/usr/bin/env python3
"""
Test that streaming chunks are concatenated correctly without extra spaces.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "webapp"))

from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "webapp", ".env"))

from llm_client import LLMClient


def test_chunk_concatenation():
    """Test that chunks concatenate correctly."""
    print("=" * 60)
    print("Testing Chunk Concatenation")
    print("=" * 60)

    client = LLMClient()
    model = "z-ai/glm4.7"

    print(f"\nModel: {model}")
    print("Prompt: What is 2+2?")
    print("\nAccumulated reasoning:")
    print("-" * 60)

    accumulated = ""
    chunk_count = 0

    try:
        for chunk in client.generate_stream(
            system_prompt="You are a helpful assistant.",
            user_prompt="What is 2+2?",
            model=model,
        ):
            chunk_type = chunk.get("type")

            if chunk_type == "reasoning":
                reasoning_text = chunk.get("content", "")
                accumulated += reasoning_text
                chunk_count += 1

                # Show what we're adding
                print(f"[Chunk {chunk_count}] Adding: '{reasoning_text}'")
                print(f"  Current accumulated: '{accumulated[-50:]}'...")

            elif chunk_type == "done":
                print(f"\n{'=' * 60}")
                print(f"Total chunks: {chunk_count}")
                print(f"Total length: {len(accumulated)} characters")
                print(f"\nFull reasoning:")
                print("-" * 60)
                print(accumulated)
                print("-" * 60)

                # Check for weird spacing patterns
                print("\nChecking for spacing issues...")
                issues = []

                # Check for spaces in the middle of words
                words = accumulated.split()
                for word in words:
                    if " " in word:
                        issues.append(f"Space in word: '{word}'")

                # Check for multiple consecutive spaces
                if "  " in accumulated:
                    issues.append(f"Multiple consecutive spaces found")

                # Check for spaces before punctuation
                import re

                if re.search(r"\s+[.,!?;:]", accumulated):
                    issues.append("Spaces before punctuation")

                if issues:
                    print("\n⚠️  Issues found:")
                    for issue in issues[:10]:  # Show first 10
                        print(f"  - {issue}")
                else:
                    print("\n✓ No spacing issues detected!")

                return len(issues) == 0

            elif chunk_type == "error":
                print(f"\n✗ Error: {chunk.get('error')}")
                return False

    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback

        traceback.print_exc()
        return False


def main():
    """Run chunk concatenation test."""
    try:
        success = test_chunk_concatenation()

        print("\n" + "=" * 60)
        if success:
            print("✓ Chunk concatenation test PASSED")
        else:
            print("✗ Chunk concatenation test FAILED")
        print("=" * 60)

        return 0 if success else 1
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user")
        return 1


if __name__ == "__main__":
    sys.exit(main())
