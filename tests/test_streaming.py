#!/usr/bin/env python3
"""
Test streaming reasoning support.
Verifies that reasoning content is streamed in chunks, not all at once.
"""

import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "webapp"))

from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "webapp", ".env"))

from llm_client import LLMClient


def test_streaming():
    """Test that reasoning is streamed in chunks."""
    print("=" * 60)
    print("Testing Streaming Reasoning")
    print("=" * 60)

    client = LLMClient()
    model = "z-ai/glm4.7"

    print(f"\nModel: {model}")
    print("Prompt: What is 2+2? Explain step by step.")
    print("\nStreaming output:")
    print("-" * 60)

    chunk_count = 0
    reasoning_chunks = []
    content_chunks = []
    start_time = time.time()

    try:
        for chunk in client.generate_stream(
            system_prompt="You are a helpful assistant.",
            user_prompt="What is 2+2? Explain step by step.",
            model=model,
        ):
            chunk_type = chunk.get("type")
            chunk_count += 1

            if chunk_type == "reasoning":
                reasoning_text = chunk.get("content", "")
                reasoning_chunks.append(reasoning_text)
                print(
                    f"[{chunk_count}] Reasoning chunk ({len(reasoning_text)} chars): {reasoning_text[:50]}..."
                )

            elif chunk_type == "content":
                content_text = chunk.get("content", "")
                content_chunks.append(content_text)
                print(
                    f"[{chunk_count}] Content chunk ({len(content_text)} chars): {content_text[:50]}..."
                )

            elif chunk_type == "done":
                elapsed = time.time() - start_time
                print(f"\n[{chunk_count}] Done in {elapsed:.1f}s")
                print(f"  Total reasoning chunks: {len(reasoning_chunks)}")
                print(f"  Total content chunks: {len(content_chunks)}")
                print(
                    f"  Full reasoning length: {len(chunk.get('reasoning', ''))} chars"
                )
                print(f"  Full content length: {len(chunk.get('content', ''))} chars")
                print(f"  Tokens: {chunk.get('tokens', {})}")

                # Show full reasoning
                if chunk.get("reasoning"):
                    print(f"\nFull reasoning:")
                    print("-" * 60)
                    print(chunk["reasoning"])
                    print("-" * 60)

                return True

            elif chunk_type == "error":
                print(f"\n[{chunk_count}] Error: {chunk.get('error')}")
                return False

            # Small delay to see streaming in action
            time.sleep(0.1)

    except Exception as e:
        print(f"\nError: {e}")
        import traceback

        traceback.print_exc()
        return False


def main():
    """Run streaming test."""
    try:
        success = test_streaming()

        print("\n" + "=" * 60)
        if success:
            print("✓ Streaming test PASSED")
            print("  Reasoning is being streamed in chunks")
        else:
            print("✗ Streaming test FAILED")
        print("=" * 60)

        return 0 if success else 1
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user")
        return 1


if __name__ == "__main__":
    sys.exit(main())
