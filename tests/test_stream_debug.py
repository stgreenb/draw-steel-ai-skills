#!/usr/bin/env python
"""Test script to debug the streaming issue"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "webapp"))

from llm_client import LLMClient

client = LLMClient()

print("Testing streaming generation...")
print("Model:", client.model)
print()

system_prompt = "You are a helpful assistant."
user_prompt = "Say hello in one word."

print("Starting stream...")
for i, chunk in enumerate(
    client.generate_stream(
        system_prompt=system_prompt, user_prompt=user_prompt, model=client.model
    )
):
    print(f"Chunk {i}: {chunk}")
    if chunk.get("type") == "done":
        print("Got done chunk, breaking")
        break
