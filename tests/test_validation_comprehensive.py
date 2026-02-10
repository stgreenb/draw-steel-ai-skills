"""Comprehensive Draw Steel validation tests"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "webapp"))

from ds_validator import DrawSteelValidator

print("Testing Draw Steel Validator with various test cases...")
validator = DrawSteelValidator()

# Test 1: Valid monster should pass
print("\n=== Test 1: Valid Monster ===")
valid_json = {
    "name": "Test Goblin",
    "type": "npc",
    "_id": "OzCzCqQLFnjssE2Z",
    "system": {
        "stamina": {"value": 10, "max": 10},
        "characteristics": {
            "might": {"value": 0},
            "agility": {"value": 1},
            "reason": {"value": -1},
            "intuition": {"value": 0},
            "presence": {"value": -1},
        },
        "combat": {
            "save": {"threshold": 6, "bonus": ""},
            "size": {"value": 1, "letter": "S"},
            "stability": 0,
            "turns": 1,
        },
        "movement": {"value": 5},
        "damage": {"immunities": {"all": 0, "poison": 0}, "weaknesses": {"all": 0}},
        "monster": {
            "level": 1,
            "ev": 8,
            "role": "brute",
            "organization": "minion",
            "keywords": ["humanoid"],
            "freeStrike": 5,
        },
    },
    "prototypeToken": {"name": "Test Goblin", "disposition": -1},
    "items": [
        {
            "name": "Sword Strike",
            "type": "ability",
            "_id": "dhexTaOhHZ6EUqfY",
            "system": {
                "type": "main",
                "category": "signature",
                "keywords": ["melee", "strike", "weapon"],
                "distance": {"type": "melee", "primary": 1},
                "target": {"type": "creatureObject", "value": 1},
                "damageDisplay": "melee",
                "power": {
                    "roll": {"formula": "@chr", "characteristics": ["might"]},
                    "effects": {
                        "dAmAgE1234567890ab": {
                            "_id": "dAmAgE1234567890ab",
                            "type": "damage",
                            "damage": {
                                "tier1": {
                                    "value": "5",
                                    "types": [],
                                    "properties": [],
                                    "potency": {
                                        "value": "@potency.weak",
                                        "characteristic": "none",
                                    },
                                },
                                "tier2": {
                                    "value": "7",
                                    "types": [],
                                    "properties": [],
                                    "potency": {
                                        "value": "@potency.average",
                                        "characteristic": "",
                                    },
                                },
                                "tier3": {
                                    "value": "9",
                                    "types": [],
                                    "properties": [],
                                    "potency": {
                                        "value": "@potency.strong",
                                        "characteristic": "",
                                    },
                                },
                            },
                        }
                    },
                },
                "effect": {"before": "", "after": "<p>Test effect.</p>"},
                "spend": {"text": "", "value": None},
            },
            "effects": [],
        }
    ],
    "_stats": {"systemId": "draw-steel"},
    "effects": [
        {"_id": "r5OCyITqPdjB7C3n", "flags": {"abilityModifier": "withCaptain"}}
    ],
}
validation = validator.validate(valid_json)
print(f"Validation Success: {validation['success']}")
assert validation["success"], "Valid monster should pass validation"
print("✓ Valid monster passed")

# Test 2: Invalid actor type
print("\n=== Test 2: Invalid Actor Type ===")
invalid_json = {**valid_json, "type": "hero"}
validation = validator.validate(invalid_json)
print(f"Validation Success: {validation['success']}")
assert not validation["success"], "Invalid actor type should fail"
assert any("Invalid actor type" in err for err in validation["errors"])
print("✓ Invalid actor type detected")

# Test 3: Invalid _id format
print("\n=== Test 3: Invalid _id Format ===")
invalid_json = {**valid_json, "_id": "abc-123-def-456"}
validation = validator.validate(invalid_json)
print(f"Validation Success: {validation['success']}")
assert not validation["success"], "Invalid _id should fail"
assert any("Invalid actor _id" in err for err in validation["errors"])
print("✓ Invalid _id format detected")

# Test 4: Missing required fields
print("\n=== Test 4: Missing Required Fields ===")
invalid_json = {"name": "Test", "type": "npc", "_id": "OzCzCqQLFnjssE2Z", "system": {}}
validation = validator.validate(invalid_json)
print(f"Validation Success: {validation['success']}")
assert not validation["success"], "Missing fields should fail"
assert any("Missing required field" in err for err in validation["errors"])
print("✓ Missing required fields detected")

# Test 5: Invalid monster role
print("\n=== Test 5: Invalid Monster Role ===")
invalid_json = {
    **valid_json,
    "system": {
        **valid_json["system"],
        "monster": {**valid_json["system"]["monster"], "role": "skirmisher"},
    },
}
validation = validator.validate(invalid_json)
print(f"Validation Success: {validation['success']}")
assert not validation["success"], "Invalid role should fail"
assert any("Invalid monster role" in err for err in validation["errors"])
print("✓ Invalid monster role detected")

# Test 6: Invalid monster organization
print("\n=== Test 6: Invalid Monster Organization ===")
invalid_json = {
    **valid_json,
    "system": {
        **valid_json["system"],
        "monster": {**valid_json["system"]["monster"], "organization": "squad"},
    },
}
validation = validator.validate(invalid_json)
print(f"Validation Success: {validation['success']}")
assert not validation["success"], "Invalid organization should fail"
assert any("Invalid monster organization" in err for err in validation["errors"])
print("✓ Invalid monster organization detected")

# Test 7: Invalid monster keyword
print("\n=== Test 7: Invalid Monster Keyword ===")
invalid_json = {
    **valid_json,
    "system": {
        **valid_json["system"],
        "monster": {
            **valid_json["system"]["monster"],
            "keywords": ["humanoid", "invalid"],
        },
    },
}
validation = validator.validate(invalid_json)
print(f"Validation Success: {validation['success']}")
assert not validation["success"], "Invalid keyword should fail"
assert any("Invalid monster keyword" in err for err in validation["errors"])
print("✓ Invalid monster keyword detected")

# Test 8: Minion without With Captain trait (warning)
print("\n=== Test 8: Minion Without With Captain ===")
invalid_json = {
    **valid_json,
    "effects": [],
    "system": {
        **valid_json["system"],
        "monster": {**valid_json["system"]["monster"], "organization": "minion"},
    },
}
validation = validator.validate(invalid_json)
print(f"Validation Success: {validation['success']}")
assert validation["success"], "Minion without With Captain is valid (warning only)"
assert any("With Captain" in warn for warn in validation["warnings"])
print("✓ Minion without With Captain warning detected")

# Test 9: No signature ability
print("\n=== Test 9: No Signature Ability ===")
invalid_json = {
    **valid_json,
    "items": [
        {
            **valid_json["items"][0],
            "system": {**valid_json["items"][0]["system"], "category": "freeStrike"},
        }
    ],
}
validation = validator.validate(invalid_json)
print(f"Validation Success: {validation['success']}")
assert not validation["success"], "No signature ability should fail"
assert any("exactly 1 signature ability" in err for err in validation["errors"])
print("✓ Missing signature ability detected")

# Test 10: Multiple signature abilities
print("\n=== Test 10: Multiple Signature Abilities ===")
invalid_json = {
    **valid_json,
    "items": [
        {
            **valid_json["items"][0],
            "_id": "dhexTaOhHZ6EUqfY",
            "system": {**valid_json["items"][0]["system"], "category": "signature"},
        },
        {
            **valid_json["items"][0],
            "_id": "AbCdEfGhIjKlMnOpQ",
            "name": "Second Strike",
            "system": {**valid_json["items"][0]["system"], "category": "signature"},
        },
    ],
}
validation = validator.validate(invalid_json)
print(f"Validation Success: {validation['success']}")
assert not validation["success"], "Multiple signature abilities should fail"
assert any("exactly 1 signature ability" in err for err in validation["errors"])
print("✓ Multiple signature abilities detected")

# Test 11: Invalid item type
print("\n=== Test 11: Invalid Item Type ===")
invalid_json = {**valid_json, "items": [{**valid_json["items"][0], "type": "action"}]}
validation = validator.validate(invalid_json)
print(f"Validation Success: {validation['success']}")
assert not validation["success"], "Invalid item type should fail"
assert any('Invalid type "action"' in err for err in validation["errors"])
print("✓ Invalid item type detected")

# Test 12: Uppercase keyword
print("\n=== Test 12: Uppercase Keyword ===")
invalid_json = {
    **valid_json,
    "items": [
        {
            **valid_json["items"][0],
            "system": {
                **valid_json["items"][0]["system"],
                "keywords": ["Melee", "strike"],
            },
        }
    ],
}
validation = validator.validate(invalid_json)
print(f"Validation Success: {validation['success']}")
assert not validation["success"], "Uppercase keyword should fail"
assert any("must be lowercase" in err for err in validation["errors"])
print("✓ Uppercase keyword detected")

# Test 13: Invalid formula
print("\n=== Test 13: Invalid Formula ===")
invalid_json = {
    **valid_json,
    "items": [
        {
            **valid_json["items"][0],
            "system": {
                **valid_json["items"][0]["system"],
                "power": {
                    **valid_json["items"][0]["system"]["power"],
                    "roll": {"formula": "@might"},
                },
            },
        }
    ],
}
validation = validator.validate(invalid_json)
print(f"Validation Success: {validation['success']}")
assert not validation["success"], "Invalid formula should fail"
assert any('must be "@chr"' in err for err in validation["errors"])
print("✓ Invalid formula detected")

# Test 14: Signature ability without power effects
print("\n=== Test 14: Signature Without Power Effects ===")
invalid_json = {
    **valid_json,
    "items": [
        {
            **valid_json["items"][0],
            "system": {
                **valid_json["items"][0]["system"],
                "power": {**valid_json["items"][0]["system"]["power"], "effects": {}},
            },
        }
    ],
}
validation = validator.validate(invalid_json)
print(f"Validation Success: {validation['success']}")
assert not validation["success"], "Signature without effects should fail"
assert any("must have power.effects" in err for err in validation["errors"])
print("✓ Missing power effects detected")

# Test 15: Invalid damage type
print("\n=== Test 15: Invalid Damage Type ===")
invalid_json = {
    **valid_json,
    "system": {
        **valid_json["system"],
        "damage": {
            "immunities": {"slashing": 1, "poison": 0},
            "weaknesses": {"all": 0},
        },
    },
}
validation = validator.validate(invalid_json)
print(f"Validation Success: {validation['success']}")
assert not validation["success"], "Invalid damage type should fail"
assert any("Invalid damage immunity type" in err for err in validation["errors"])
print("✓ Invalid damage type detected")

# Test 16: HTML entities in effect text
print("\n=== Test 16: HTML Entities in Effect ===")
invalid_json = {
    **valid_json,
    "items": [
        {
            **valid_json["items"][0],
            "system": {
                **valid_json["items"][0]["system"],
                "effect": {"before": "", "after": "<p>Test &lt;effect&gt;.</p>"},
            },
        }
    ],
}
validation = validator.validate(invalid_json)
print(f"Validation Success: {validation['success']}")
assert not validation["success"], "HTML entities should fail"
assert any("HTML entity" in err for err in validation["errors"])
print("✓ HTML entities detected")

# Test 17: Invalid distance type
print("\n=== Test 17: Invalid Distance Type ===")
invalid_json = {
    **valid_json,
    "items": [
        {
            **valid_json["items"][0],
            "system": {
                **valid_json["items"][0]["system"],
                "distance": {"type": "reach", "primary": 1},
            },
        }
    ],
}
validation = validator.validate(invalid_json)
print(f"Validation Success: {validation['success']}")
assert not validation["success"], "Invalid distance type should fail"
assert any("Invalid distance type" in err for err in validation["errors"])
print("✓ Invalid distance type detected")

# Test 18: Missing spend field
print("\n=== Test 18: Missing Spend Field ===")
invalid_json = {
    **valid_json,
    "items": [
        {
            **valid_json["items"][0],
            "system": {
                k: v
                for k, v in valid_json["items"][0]["system"].items()
                if k != "spend"
            },
        }
    ],
}
validation = validator.validate(invalid_json)
print(f"Validation Success: {validation['success']}")
assert not validation["success"], "Missing spend field should fail"
assert any("Must have 'spend' field" in err for err in validation["errors"])
print("✓ Missing spend field detected")

print("\n" + "=" * 50)
print("✓ All validation tests passed!")
print("=" * 50)
