"""Test LLM client with actual proxy"""

import sys
import os

# Add webapp to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "webapp"))

# Load environment
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "webapp", ".env"))

from llm_client import LLMClient
from prompt_builder import PromptBuilder
from response_parser import ResponseParser


def test_llm_connection():
    """Test LLM proxy connection."""
    print("Testing LLM Proxy Connection...")
    print(f"Proxy URL: {os.getenv('LLM_PROXY_URL')}")
    print(f"Model: {os.getenv('OPENAI_MODEL', 'llama3.1:8b')}")
    print()

    client = LLMClient()
    builder = PromptBuilder()
    parser = ResponseParser()

    # Test 1: Simple prompt
    print("Test 1: Simple generation...")
    system_prompt = builder.get_system_prompt()
    user_prompt = builder.build_create_prompt(
        "Level 1 Goblin, Minion Skirmisher", "markdown"
    )

    response = client.generate(system_prompt, user_prompt)

    if response["success"]:
        print("✓ LLM response received")
        print(
            f"  Tokens: {response['tokens']['total']} (prompt: {response['tokens']['prompt']}, completion: {response['tokens']['completion']})"
        )
        print(f"  Model: {response['model']}")
        print(f"\n  Output preview (first 200 chars):")
        print(f"  {response['output'][:200]}...")

        # Parse and validate
        parsed = parser.parse(response["output"], "markdown")
        print(
            f"\n  Validation: {'✓ Passed' if parsed['validation']['success'] else '✗ Failed'}"
        )
        if parsed["validation"]["errors"]:
            print(f"  Errors: {parsed['validation']['errors']}")
    else:
        print(f"✗ LLM request failed: {response['error']}")
        return False

    print()

    # Test 2: JSON format
    print("Test 2: JSON format generation...")
    user_prompt = builder.build_create_prompt(
        "Level 2 Skeleton, Minion Soldier", "json"
    )

    response = client.generate(system_prompt, user_prompt)

    if response["success"]:
        print("✓ LLM response received")
        parsed = parser.parse(response["output"], "json")
        print(f"  JSON parsed: {'✓ Yes' if parsed['json_data'] else '✗ No'}")
        print(
            f"  Validation: {'✓ Passed' if parsed['validation']['success'] else '✗ Failed (expected for partial JSON)'}"
        )
        if parsed["json_data"]:
            print(f"  Monster name: {parsed['json_data'].get('name', 'N/A')}")
    else:
        print(f"✗ LLM request failed: {response['error']}")

    print()
    print("=" * 50)
    print("LLM Integration Test Complete!")
    print("=" * 50)
    return True


if __name__ == "__main__":
    try:
        success = test_llm_connection()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)
