"""Test Draw Steel Markdown validation"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "webapp"))

from ds_validator import DrawSteelValidator

# Sample valid Markdown (simplified format)
valid_markdown = """```yaml
name: Test Goblin
level: 1
ev: 3
stamina: 12
characteristics: 0
role: brute
organization: minion
keywords: [humanoid]

combat:
  defense: 12
  save: 6
  damage: 8
  free_strike: 8

abilities:
  - name: Sword Strike
    type: main
    category: signature
    keywords: [melee, strike, weapon]
    distance: melee
    roll: @chr
    damage: 8
    effects: |
      Test effect description.
```"""

# Sample invalid Markdown (missing required fields)
invalid_markdown = """```yaml
name: Test Goblin
keywords: [humanoid]

abilities:
  - name: Sword Strike
    type: main
    keywords: [melee]
    effects: |
      Test effect.
```"""

print("Testing Draw Steel Markdown Validator...")
validator = DrawSteelValidator()

# Test valid Markdown
print("\n--- Testing Valid Markdown ---")
validation = validator.validate(valid_markdown)
print(f"Validation Success: {validation['success']}")
if validation["errors"]:
    print(f"Errors ({len(validation['errors'])}):")
    for err in validation["errors"]:
        print(f"  - {err}")
if validation["warnings"]:
    print(f"Warnings ({len(validation['warnings'])}):")
    for warn in validation["warnings"]:
        print(f"  - {warn}")

# Test invalid Markdown
print("\n--- Testing Invalid Markdown ---")
validation2 = validator.validate(invalid_markdown)
print(f"Validation Success: {validation2['success']}")
if validation2["errors"]:
    print(f"Errors ({len(validation2['errors'])}):")
    for err in validation2["errors"]:
        print(f"  - {err}")
if validation2["warnings"]:
    print(f"Warnings ({len(validation2['warnings'])}):")
    for warn in validation2["warnings"]:
        print(f"  - {warn}")

# Test Draw Steel formula validation
print("\n--- Testing Draw Steel Formula Validation ---")
# This should trigger warnings about incorrect EV/Stamina/Damage
incorrect_formulas = """```yaml
name: Test Dragon
level: 5
ev: 100
stamina: 500
characteristics: 3
role: solo
organization: solo
keywords: [dragon]

combat:
  defense: 20
  save: 12
  damage: 50
  free_strike: 25

abilities:
  - name: Fire Breath
    type: main
    category: signature
    keywords: [fire, area]
    distance: burst 3
    roll: @chr
    damage: 20
    effects: |
      Deals fire damage to all creatures in burst.
```"""

validation3 = validator.validate(incorrect_formulas)
print(f"Validation Success: {validation3['success']}")
if validation3["errors"]:
    print(f"Errors ({len(validation3['errors'])}):")
    for err in validation3["errors"]:
        print(f"  - {err}")
if validation3["warnings"]:
    print(f"Warnings ({len(validation3['warnings'])}):")
    for warn in validation3["warnings"]:
        print(f"  - {warn}")

print("\n" + "=" * 50)
print("✓ Validation tests completed!")
print("=" * 50)
