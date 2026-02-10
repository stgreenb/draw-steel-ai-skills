"""Test prompt builder for Markdown output"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "webapp"))

from prompt_builder import PromptBuilder

print("Testing Prompt Builder...")
builder = PromptBuilder()

# Test 1: Create prompt with simple idea
print("\n=== Test 1: Simple Create Prompt ===")
idea = "Level 3 Red Dragon, Solo Brute"
prompt = builder.build_create_prompt(idea)
print(f"Idea: {idea}")
print(f"Prompt length: {len(prompt)} chars")
assert "Create a Draw Steel monster" in prompt
assert "Red Dragon" in prompt
assert "Markdown" in prompt
print("✓ Create prompt generated correctly")

# Test 2: Create prompt with complex idea
print("\n=== Test 2: Complex Create Prompt ===")
idea = "Level 5 Shadowy Assassin, Platoon Harrier with poison abilities"
prompt = builder.build_create_prompt(idea)
print(f"Idea: {idea}")
print(f"Prompt length: {len(prompt)} chars")
assert "Shadowy Assassin" in prompt
assert "Platoon" in prompt
assert "Harrier" in prompt
assert "poison" in prompt
print("✓ Complex create prompt generated correctly")

# Test 3: Convert prompt with D&D 5e stat block
print("\n=== Test 3: D&D 5e Convert Prompt ===")
stat_block = """Goblin
Small humanoid (goblinoid), neutral evil
Armor Class 15 (leather armor, shield)
Hit Points 7 (2d6)
Speed 30 ft.

STR 8 (-1) DEX 14 (+2) CON 10 (+0) INT 10 (+0) WIS 8 (-1) CHA 8 (-1)"""
prompt = builder.build_convert_prompt(stat_block)
print(f"Stat block length: {len(stat_block)} chars")
print(f"Prompt length: {len(prompt)} chars")
assert "Convert this monster to Draw Steel format" in prompt
assert "Goblin" in prompt
assert "Markdown" in prompt
print("✓ D&D 5e convert prompt generated correctly")

# Test 4: Convert prompt with Pathfinder stat block
print("\n=== Test 4: Pathfinder Convert Prompt ===")
stat_block = """Goblin Warrior CR 1/3
XP 135
NE Small humanoid (goblinoid)
Init +2; Senses darkvision 60 ft.; Perception +1
DEFENSE
AC 15, touch 12, flat-footed 13 (+3 armor, +2 Dex)
hp 6 (1d8+2)
Fort +2, Ref +4, Will +0"""
prompt = builder.build_convert_prompt(stat_block)
print(f"Stat block length: {len(stat_block)} chars")
print(f"Prompt length: {len(prompt)} chars")
assert "Convert this monster to Draw Steel format" in prompt
assert "Goblin Warrior" in prompt
print("✓ Pathfinder convert prompt generated correctly")

# Test 5: System prompt
print("\n=== Test 5: System Prompt ===")
system_prompt = builder.get_system_prompt()
print(f"System prompt length: {len(system_prompt)} chars")
assert "expert monster designer" in system_prompt
assert "Draw Steel" in system_prompt
assert "Markdown" in system_prompt
print("✓ System prompt generated correctly")

# Test 6: Verify critical validation requirements in system prompt
print("\n=== Test 6: Critical Validation Requirements ===")
system_prompt = builder.get_system_prompt()
critical_requirements = [
    "ancestry:",
    "level:",
    "ev:",
    "stamina:",
    "roles:",
    "size:",
    "speed:",
    "might:",
    "agility:",
    "reason:",
    "intuition:",
    "presence:",
    "free_strike:",
]
for req in critical_requirements:
    assert req in system_prompt, f"Missing critical requirement: {req}"
    print(f"✓ Found: {req}")

# Test 7: Verify Draw Steel formulas in system prompt
print("\n=== Test 7: Draw Steel Formulas ===")
system_prompt = builder.get_system_prompt()
formulas = [
    "EV = ceil(((2 × Level) + 4)",
    "Stamina = ceil(((10 × Level)",
    "Damage = ceil((4 + Level",
]
for formula in formulas:
    assert formula in system_prompt, f"Missing formula: {formula}"
    print(f"✓ Found formula: {formula}")

# Test 8: Verify NO Foundry-specific requirements
print("\n=== Test 8: Verify NO Foundry-specific Requirements ===")
system_prompt = builder.get_system_prompt()
foundry_requirements = [
    '"type": "npc"',
    '_id" fields must match pattern',
    'system.power.roll.formula" must be "@chr"',
]
for req in foundry_requirements:
    assert req not in system_prompt, f"Foundry requirement should not be present: {req}"
    print(f"✓ Not found (correct): {req[:50]}...")

print("\n" + "=" * 50)
print("✓ All prompt builder tests passed!")
print("=" * 50)
