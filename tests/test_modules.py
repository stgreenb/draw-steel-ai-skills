"""Test script for webapp modules"""

import sys
import os

# Add webapp to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "webapp"))


def test_url_fetcher():
    """Test URL fetcher module."""
    print("Testing URL Fetcher...")
    from url_fetcher import URLFetcher

    fetcher = URLFetcher()

    # Test with invalid URL
    result = fetcher.fetch("not-a-url")
    assert not result["success"], "Invalid URL should fail"
    print("✓ Invalid URL test passed")

    # Test with timeout (using a slow URL)
    # result = fetcher.fetch("http://httpbin.org/delay/20")
    # assert not result['success'], "Timeout should fail"
    # print("✓ Timeout test passed")

    print("✓ URL Fetcher tests passed\n")


def test_llm_client():
    """Test LLM client module."""
    print("Testing LLM Client...")
    from llm_client import LLMClient

    client = LLMClient()

    # Check initialization
    assert client.base_url, "Base URL should be set"
    assert client.model, "Model should be set"
    print("✓ LLM Client initialization passed")

    # Note: Can't test actual API calls without a running LLM proxy
    print("✓ LLM Client tests passed (API call tests skipped)\n")


def test_prompt_builder():
    """Test prompt builder module."""
    print("Testing Prompt Builder...")
    from prompt_builder import PromptBuilder

    builder = PromptBuilder()

    # Test system prompt
    system_prompt = builder.get_system_prompt()
    assert system_prompt, "System prompt should not be empty"
    print("✓ System prompt test passed")

    # Test create prompt
    create_prompt = builder.build_create_prompt("Level 5 Fire Dragon", "markdown")
    assert "Level 5 Fire Dragon" in create_prompt, "Prompt should contain input"
    assert "markdown" in create_prompt.lower(), "Prompt should mention format"
    print("✓ Create prompt test passed")

    # Test convert prompt
    convert_prompt = builder.build_convert_prompt("Some stat block", "json")
    assert "stat block" in convert_prompt.lower(), "Prompt should mention stat block"
    assert "json" in convert_prompt.lower(), "Prompt should mention format"
    print("✓ Convert prompt test passed")

    print("✓ Prompt Builder tests passed\n")


def test_response_parser():
    """Test response parser module."""
    print("Testing Response Parser...")
    from response_parser import ResponseParser

    parser = ResponseParser()

    # Test markdown parsing
    markdown_text = "# Test Monster\n\n**Level 5**"
    result = parser.parse(markdown_text, "markdown")
    assert result["output"] == markdown_text, "Output should match input"
    print("✓ Markdown parsing test passed")

    # Test JSON parsing
    json_text = '{"name": "Test Monster", "level": 5}'
    result = parser.parse(json_text, "json")
    assert result["json_data"]["name"] == "Test Monster", "Should parse JSON"
    print("✓ JSON parsing test passed")

    # Test JSON validation
    result = parser.parse('{"name": "Test"}', "json")
    assert not result["validation"]["success"], (
        "Missing required fields should fail validation"
    )
    assert "level" in str(result["validation"]["errors"]), "Should report missing level"
    print("✓ JSON validation test passed")

    # Test both format
    both_text = '{"name": "Test"}\n\n# Test Monster'
    result = parser.parse(both_text, "both")
    assert result["json_data"]["name"] == "Test", "Should extract JSON"
    print("✓ Both format parsing test passed")

    print("✓ Response Parser tests passed\n")


if __name__ == "__main__":
    print("=" * 50)
    print("Webapp Module Tests")
    print("=" * 50)
    print()

    try:
        test_url_fetcher()
        test_llm_client()
        test_prompt_builder()
        test_response_parser()

        print("=" * 50)
        print("All tests passed! ✓")
        print("=" * 50)
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)
