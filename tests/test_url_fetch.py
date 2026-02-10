#!/usr/bin/env python3
"""
Test URL fetching with improved headers and retry logic.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "webapp"))

from url_fetcher import URLFetcher


def test_url_fetch():
    """Test URL fetching."""
    print("=" * 60)
    print("Testing URL Fetching")
    print("=" * 60)

    fetcher = URLFetcher()

    # Test URLs
    test_urls = [
        "https://example.com",
        "https://pf2easy.com/api/creature/badger",
        "https://5e.tools/bestiary.html#giant%20badger_xmm",
    ]

    for url in test_urls:
        print(f"\n{'=' * 60}")
        print(f"Testing: {url}")
        print("=" * 60)

        result = fetcher.fetch(url)

        if result["success"]:
            print(f"✓ Success!")
            print(f"  Content type: {result.get('content_type', 'unknown')}")
            print(f"  Content length: {len(result.get('content', ''))} characters")
            print(f"  Content preview (first 200 chars):")
            print("-" * 60)
            print(result.get("content", "")[:200])
            print("-" * 60)
        else:
            print(f"✗ Failed: {result.get('error', 'Unknown error')}")


def main():
    """Run URL fetch tests."""
    try:
        test_url_fetch()
        return 0
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback

        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
