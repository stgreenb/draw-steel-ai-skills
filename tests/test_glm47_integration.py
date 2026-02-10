"""Test GLM 4.7 integration in webapp"""

import sys
import os

# Add webapp to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "webapp"))

# Load environment
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "webapp", ".env"))

from llm_client import LLMClient
from prompt_builder import PromptBuilder


def test_glm47_integration():
    """Test GLM 4.7 model configuration."""
    print("Testing GLM 4.7 Integration...")
    print("=" * 60)

    # Initialize client
    client = LLMClient()

    # Check model configuration
    print("\n1. Model Configuration:")
    print(f"   Default model: {client.model}")
    print(f"   Available models: {list(client.get_model_config.__code__.co_consts[1])}")

    # Check GLM 4.7 config
    glm47_config = client.get_model_config("z-ai/glm4.7")
    print(f"\n2. GLM 4.7 Configuration:")
    print(f"   Base URL: {glm47_config['base_url']}")
    print(
        f"   API Key: {'***' + glm47_config['api_key'][-4:] if glm47_config['api_key'] else 'NOT SET'}"
    )
    print(f"   Timeout: {glm47_config['timeout']}s")
    print(f"   Max Tokens: {glm47_config['max_tokens']}")

    # Check discovery
    print(f"\n3. Model Discovery:")
    models = client.fetch_models()
    print(f"   Total models: {len(models)}")
    for model in models:
        print(f"   - {model['id']} (provider: {model['provider']})")

    # Check working models
    print(f"\n4. Working Models:")
    working = client.get_working_models()
    print(f"   Working models: {len(working)}")
    for model in working:
        print(f"   - {model['id']}")

    # Check health report
    print(f"\n5. Health Report:")
    health = client.get_health_report()
    for model_id, status in health.items():
        print(f"   - {model_id}: {status['status']} (provider: {status['provider']})")

    print("\n" + "=" * 60)
    print("✓ GLM 4.7 Integration Test Complete!")
    print("=" * 60)

    return True


if __name__ == "__main__":
    try:
        test_glm47_integration()
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)
