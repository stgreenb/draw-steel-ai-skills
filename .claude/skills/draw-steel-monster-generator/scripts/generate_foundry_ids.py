#!/usr/bin/env python3
"""
Generate unique 16-character alphanumeric IDs for Foundry VTT JSON.

Usage:
    python scripts/generate_foundry_ids.py                    # Generate 1 ID (default)
    python scripts/generate_foundry_ids.py --count 5         # Generate 5 IDs
    python scripts/generate_foundry_ids.py -c 10             # Generate 10 IDs

Output:
    IDs are printed to stdout, one per line.
    Each ID is exactly 16 alphanumeric characters (a-z, A-Z, 0-9).
"""

import argparse
import secrets
import sys


def generate_id() -> str:
    """Generate a single 16-character alphanumeric ID using cryptographically secure random selection."""
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join(secrets.choice(characters) for _ in range(16))


def main():
    parser = argparse.ArgumentParser(
        description="Generate unique 16-character alphanumeric IDs for Foundry VTT JSON.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  %(prog)s                    # Generate 1 ID
  %(prog)s --count 5         # Generate 5 IDs
  %(prog)s -c 10             # Generate 10 IDs""",
    )
    parser.add_argument(
        "-c",
        "--count",
        type=int,
        default=1,
        help="Number of IDs to generate (default: 1)",
    )

    args = parser.parse_args()

    if args.count < 1:
        print("Error: count must be at least 1", file=sys.stderr)
        sys.exit(1)

    for _ in range(args.count):
        print(generate_id())


if __name__ == "__main__":
    main()
