#!/usr/bin/env python3
"""
Foundry VTT JSON Validation Script for Draw Steel Reward Generator

This script validates generated reward JSON files (treasures and titles)
against common errors that cause import failures in Foundry VTT.
"""

import json
import re
import sys
from pathlib import Path

# Valid treasure categories
VALID_TREASURE_CATEGORIES = {"consumable", "trinket", "leveled", "artifact"}

# Valid treasure creation keywords (every treasure must have one or both)
VALID_CREATION_KEYWORDS = {"magic", "psionic"}

# Valid body keywords (for wearable treasures)
VALID_BODY_KEYWORDS = {
    "arms",
    "feet",
    "hands",
    "head",
    "neck",
    "waist",
    "ring",
}

# Valid equipment keywords (for leveled treasures)
VALID_EQUIPMENT_KEYWORDS = {
    # Weapon categories
    "light weapon",
    "medium weapon",
    "heavy weapon",
    "bow",
    "polearm",
    "spear",
    # Armor categories
    "light armor",
    "medium armor",
    "heavy armor",
    "shield",
    # Implement types
    "implement",
    "orb",
    "wand",
}

# Valid project sources (regions)
VALID_PROJECT_SOURCES = {
    "caelian",
    "anjali",
    "zaliac",
    "khelt",
    "yllyric",
    "variac",
    "hyrallic",
    "ullorvic",
    "high kuric",
    "first language",
    "proto-ctholl",
    "voll",
    "szetch",
    "kalliak",
    "khemharic",
}

# Valid project roll characteristics
VALID_CHARACTERISTICS = {"reason", "intuition", "agility", "might", "presence"}

# Valid damage types (for effects)
VALID_DAMAGE_TYPES = {
    "acid",
    "cold",
    "corruption",
    "fire",
    "holy",
    "lightning",
    "poison",
    "psychic",
    "sonic",
}


class ValidationResult:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.passed = True

    def add_error(self, message):
        self.errors.append(message)
        self.passed = False

    def add_warning(self, message):
        self.warnings.append(message)

    def is_valid(self):
        return self.passed

    def print_report(self, filename: str):
        """Print a validation report for the given file."""
        print(f"\n{'=' * 60}")
        print(f"Validation Report: {filename}")
        print(f"{'=' * 60}")

        if self.passed and not self.warnings:
            print("✓ PASSED - No errors or warnings found")
            return

        if self.errors:
            print(f"\n❌ ERRORS ({len(self.errors)}):")
            for i, error in enumerate(self.errors, 1):
                print(f"  {i}. {error}")

        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
            for i, warning in enumerate(self.warnings, 1):
                print(f"  {i}. {warning}")

        print(f"\nStatus: {'✓ PASSED' if self.passed else '❌ FAILED'}")


def is_valid_16_char_id(value: str) -> bool:
    """Check if value matches pattern ^[a-zA-Z0-9]{16}$ (16 alphanumeric chars)."""
    if not isinstance(value, str):
        return False
    return bool(re.match(r"^[a-zA-Z0-9]{16}$", value))


def validate_item_type(data: dict, result: ValidationResult) -> None:
    """Validate that item type is valid ('treasure' or 'title')."""
    item_type = data.get("type")
    if item_type not in ("treasure", "title"):
        result.add_error(f"Item type must be 'treasure' or 'title', got '{item_type}'")


def validate_treasure_category(data: dict, result: ValidationResult) -> None:
    """Validate treasure category."""
    if data.get("type") != "treasure":
        return

    system = data.get("system", {})
    category = system.get("category")

    if category and category not in VALID_TREASURE_CATEGORIES:
        result.add_error(
            f"Invalid treasure category '{category}'. "
            f"Must be one of: {', '.join(sorted(VALID_TREASURE_CATEGORIES))}"
        )


def validate_echelon(data: dict, result: ValidationResult) -> None:
    """Validate echelon value (1-4)."""
    system = data.get("system", {})
    echelon = system.get("echelon")

    if echelon is not None and (
        not isinstance(echelon, int) or echelon < 1 or echelon > 4
    ):
        result.add_error(
            f"Invalid echelon '{echelon}'. Must be an integer between 1 and 4."
        )


def validate_keywords_lowercase(data: dict, result: ValidationResult) -> None:
    """Validate that all keywords are lowercase strings."""
    system = data.get("system", {})
    keywords = system.get("keywords", [])

    for keyword in keywords:
        if not keyword.islower():
            result.add_error(
                f"Keyword '{keyword}' is capitalized. All keywords must be lowercase."
            )


def validate_creation_keywords(data: dict, result: ValidationResult) -> None:
    """
    Validate that treasures have at least one creation keyword (Magic or Psionic).

    Every treasure must have Magic, Psionic, or both keywords.
    These indicate creation method, not usage restrictions.
    """
    if data.get("type") != "treasure":
        return

    system = data.get("system", {})
    keywords = set(k.lower() for k in system.get("keywords", []))

    # Check if treasure has at least one creation keyword
    has_creation_keyword = bool(keywords & VALID_CREATION_KEYWORDS)

    if not has_creation_keyword:
        result.add_error(
            f"Treasure must have at least one creation keyword (Magic or Psionic). "
            f"Found keywords: {', '.join(keys) if keys else 'none'}. "
            f"Every treasure indicates how it was created (Magic, Psionic, or both)."
        )


def validate_body_keyword(data: dict, result: ValidationResult) -> None:
    """
    Validate that trinkets and leveled treasures have a body keyword.

    Wearable treasures should have body keywords (Arms, Feet, Hands, Head, Neck, Waist, Ring).
    """
    if data.get("type") != "treasure":
        return

    system = data.get("system", {})
    category = system.get("category")
    keywords = set(k.lower() for k in system.get("keywords", []))

    # Only check trinkets and leveled treasures
    if category not in ("trinket", "leveled"):
        return

    # Check if treasure has at least one body keyword
    has_body_keyword = bool(keywords & VALID_BODY_KEYWORDS)

    if not has_body_keyword:
        result.add_error(
            f"{category.capitalize()} treasure must have at least one body keyword. "
            f"Valid body keywords: {', '.join(sorted(VALID_BODY_KEYWORDS))}. "
            f"Found keywords: {', '.join(sorted(keywords)) if keywords else 'none'}."
        )


def validate_equipment_keyword(data: dict, result: ValidationResult) -> None:
    """
    Validate that leveled treasures have an equipment keyword.

    Leveled treasures should have equipment keywords (weapon categories, armor categories, implement types).
    """
    if data.get("type") != "treasure":
        return

    system = data.get("system", {})
    category = system.get("category")
    keywords = set(k.lower() for k in system.get("keywords", []))

    # Only check leveled treasures
    if category != "leveled":
        return

    # Check if treasure has at least one equipment keyword
    has_equipment_keyword = bool(keywords & VALID_EQUIPMENT_KEYWORDS)

    if not has_equipment_keyword:
        result.add_warning(
            f"Leveled treasure should have an equipment keyword. "
            f"Valid equipment keywords: {', '.join(sorted(VALID_EQUIPMENT_KEYWORDS))}. "
            f"Found keywords: {', '.join(sorted(keywords)) if keywords else 'none'}."
        )


def validate_project_goal(data: dict, result: ValidationResult) -> None:
    """Validate project goal against echelon and treasure type patterns."""
    if data.get("type") != "treasure":
        return

    system = data.get("system", {})
    category = system.get("category")
    echelon = system.get("echelon", 1)
    project = system.get("project", {})
    goal = project.get("goal")

    if goal is None:
        return

    # Project goal patterns by treasure type and echelon
    if category == "consumable":
        valid_goals = {
            1: {30, 45},
            2: {90},
            3: {120, 180},
            4: {360},
        }
        expected = valid_goals.get(echelon, set())
        if goal not in expected:
            result.add_warning(
                f"Project goal {goal} for {echelon}st/nd/rd/th echelon consumable may not match pattern. "
                f"Expected values: {', '.join(map(str, sorted(expected)))}."
            )

    elif category == "trinket":
        expected = 150 * echelon
        if goal != expected:
            result.add_error(
                f"Project goal {goal} for {echelon}st/nd/rd/th echelon trinket is incorrect. "
                f"Expected: {expected} (150 × echelon)."
            )

    elif category == "leveled":
        if goal != 450:
            result.add_error(
                f"Project goal {goal} for leveled treasure is incorrect. "
                f"All leveled treasures have project goal 450."
            )

    elif category == "artifact":
        # Artifacts have higher goals, but patterns need further analysis
        minimum = 600
        if goal < minimum:
            result.add_warning(
                f"Project goal {goal} for artifact seems low. "
                f"Artifacts typically have project goals {minimum}+. "
                f"Patterns need further analysis."
            )


def validate_project_source(data: dict, result: ValidationResult) -> None:
    """Validate project source is a valid region."""
    if data.get("type") != "treasure":
        return

    system = data.get("system", {})
    project = system.get("project", {})
    source = project.get("source", "").lower()

    if not source:
        return

    # Check if source contains a valid region name
    has_valid_source = any(region in source for region in VALID_PROJECT_SOURCES)

    if not has_valid_source:
        result.add_warning(
            f"Project source '{source}' may not be a valid region. "
            f"Valid regions: {', '.join(sorted(VALID_PROJECT_SOURCES))}."
        )


def validate_roll_characteristics(data: dict, result: ValidationResult) -> None:
    """Validate project roll characteristic values."""
    if data.get("type") != "treasure":
        return

    system = data.get("system", {})
    project = system.get("project", {})
    roll_char = project.get("rollCharacteristic")

    if roll_char is None:
        return

    # Normalize to list
    if isinstance(roll_char, str):
        characteristics = [roll_char.lower()]
    elif isinstance(roll_char, list):
        characteristics = [c.lower() for c in roll_char]
    else:
        result.add_error(
            f"Project roll characteristic must be a string or array of strings, got {type(roll_char).__name__}."
        )
        return

    # Validate each characteristic
    invalid_chars = [c for c in characteristics if c not in VALID_CHARACTERISTICS]
    if invalid_chars:
        result.add_error(
            f"Invalid project roll characteristics: {', '.join(invalid_chars)}. "
            f"Valid characteristics: {', '.join(sorted(VALID_CHARACTERISTICS))}."
        )


def validate_yield_structure(data: dict, result: ValidationResult) -> None:
    """Validate yield structure for consumables."""
    if data.get("type") != "treasure":
        return

    system = data.get("system", {})
    category = system.get("category")
    project = system.get("project", {})
    yield_data = project.get("yield")

    # Only check consumables (they commonly have yield)
    if category != "consumable":
        return

    if yield_data is None:
        return

    # Check structure
    if not isinstance(yield_data, dict):
        result.add_error(f"Yield must be an object, got {type(yield_data).__name__}.")
        return

    # Check required keys
    if "amount" not in yield_data:
        result.add_error("Yield missing 'amount' key.")
    elif not isinstance(yield_data["amount"], str):
        result.add_error(
            f"Yield amount must be a string, got {type(yield_data['amount']).__name__}."
        )

    if "display" not in yield_data:
        result.add_error("Yield missing 'display' key.")
    elif yield_data["display"] != "":
        result.add_warning(
            f"Yield display should be empty string, got '{yield_data['display']}'."
        )


def validate_id_format(data: dict, result: ValidationResult, path: str = "") -> None:
    """Validate that all _id fields match pattern ^[a-zA-Z0-9]{16}$."""
    if isinstance(data, dict):
        for key, value in data.items():
            new_path = f"{path}.{key}" if path else key
            if key == "_id":
                if not is_valid_16_char_id(value):
                    if isinstance(value, str) and "-" in value:
                        result.add_error(
                            f"{new_path} contains UUID format (has dashes). "
                            f"Must match pattern ^[a-zA-Z0-9]{{16}}$, got: {value}"
                        )
                    elif isinstance(value, str) and len(value) != 16:
                        result.add_error(
                            f"{new_path} has invalid length (must be 16). "
                            f"Must match pattern ^[a-zA-Z0-9]{{16}}$, got {len(value)} chars: {value}"
                        )
                    else:
                        result.add_error(
                            f"{new_path} contains invalid characters. "
                            f"Must match pattern ^[a-zA-Z0-9]{{16}}$, got: {value}"
                        )
            else:
                validate_id_format(value, result, new_path)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            validate_id_format(item, result, f"{path}[{i}]")


def validate_duplicate_ids(data: dict, result: ValidationResult) -> None:
    """Validate that all _id fields within the same JSON file are unique."""
    if isinstance(data, dict):
        # Collect all _id values recursively
        ids = []
        path_to_id = {}

        def collect_ids(obj, path=""):
            if isinstance(obj, dict):
                for key, value in obj.items():
                    new_path = f"{path}.{key}" if path else key
                    if key == "_id":
                        if isinstance(value, str):
                            ids.append(value)
                            if value not in path_to_id:
                                path_to_id[value] = []
                            path_to_id[value].append(new_path)
                    else:
                        collect_ids(value, new_path)
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    collect_ids(item, f"{path}[{i}]")

        collect_ids(data)

        # Check for duplicates
        seen = set()
        duplicates = set()
        for id_value in ids:
            if id_value in seen:
                duplicates.add(id_value)
            seen.add(id_value)

        if duplicates:
            for dup_id in duplicates:
                paths = path_to_id.get(dup_id, [])
                result.add_error(
                    f"Duplicate _id value found: '{dup_id}' appears {len(paths)} times at: {', '.join(paths)}. "
                    f"All IDs must be unique within the same reward."
                )


def validate_leveled_scaling(data: dict, result: ValidationResult) -> None:
    """Validate leveled treasure scaling patterns (1st, 5th, 9th level)."""
    if data.get("type") != "treasure":
        return

    system = data.get("system", {})
    category = system.get("category")

    # Only check leveled treasures
    if category != "leveled":
        return

    effects = data.get("effects", [])
    keywords = set(k.lower() for k in system.get("keywords", []))

    # Check for equipment type
    is_weapon = any(
        kw in keywords
        for kw in [
            "light weapon",
            "medium weapon",
            "heavy weapon",
            "bow",
            "polearm",
            "spear",
        ]
    )
    is_armor = any(
        kw in keywords for kw in ["light armor", "medium armor", "heavy armor"]
    )
    is_shield = "shield" in keywords
    is_implement = "implement" in keywords

    # Collect damage and stamina values by level
    damage_by_level = {}
    stamina_by_level = {}

    for effect in effects:
        effect_name = effect.get("name", "")
        effect_type = effect.get("type")
        changes = effect.get("changes", [])

        # Parse level from effect name
        level_match = re.search(
            r"\((\d+)(?:st|nd|rd|th) level\)", effect_name, re.IGNORECASE
        )
        if not level_match:
            continue

        level = int(level_match.group(1))

        # Check for damage bonuses (weapons/implements)
        if is_weapon or is_implement:
            for change in changes:
                key = change.get("key", "")
                value = change.get("value", "")
                if "damage.tier" in key and effect_type == "abilityModifier":
                    damage_by_level[level] = value

        # Check for stamina bonuses (armor/shields)
        if is_armor or is_shield:
            for change in changes:
                key = change.get("key", "")
                value = change.get("value", "")
                if "stamina" in key.lower() and effect_type == "abilityModifier":
                    stamina_by_level[level] = value

    # Validate damage scaling (weapons/implements)
    if is_weapon or is_implement:
        expected_damage = {1: "1", 5: "2", 9: "3"}
        for level, expected in expected_damage.items():
            actual = damage_by_level.get(level)
            if actual is None:
                result.add_warning(
                    f"Leveled treasure missing {level}st/nd/rd/th level damage effect."
                )
            elif actual != expected:
                result.add_warning(
                    f"Leveled treasure damage at {level}st/nd/rd/th level is {actual}, expected {expected}. "
                    f"Standard scaling: +1/+2/+3."
                )

    # Validate stamina scaling (armor)
    if is_armor:
        expected_stamina = {1: "6", 5: "12", 9: "21"}
        for level, expected in expected_stamina.items():
            actual = stamina_by_level.get(level)
            if actual is None:
                result.add_warning(
                    f"Leveled treasure missing {level}st/nd/rd/th level stamina effect."
                )
            elif actual != expected:
                result.add_warning(
                    f"Leveled treasure stamina at {level}st/nd/rd/th level is {actual}, expected {expected}. "
                    f"Standard armor scaling: +6/+12/+21."
                )


def validate_title_advancements(data: dict, result: ValidationResult) -> None:
    """Validate title advancements structure."""
    if data.get("type") != "title":
        return

    system = data.get("system", {})
    advancements = system.get("advancements", {})

    if not advancements:
        result.add_error("Title must have advancements structure.")
        return

    # Check each advancement
    for adv_id, advancement in advancements.items():
        adv_type = advancement.get("type")

        if adv_type != "itemGrant":
            result.add_error(
                f"Advancement '{adv_id}' has invalid type '{adv_type}'. "
                f"Must be 'itemGrant' for title benefits."
            )
            continue

        # Check pool
        pool = advancement.get("pool", [])
        if not isinstance(pool, list):
            result.add_error(
                f"Advancement '{adv_id}' pool must be an array, got {type(pool).__name__}."
            )
        elif len(pool) < 1:
            result.add_error(
                f"Advancement '{adv_id}' pool must have at least one UUID."
            )

        # Check chooseN
        choose_n = advancement.get("chooseN")
        if not isinstance(choose_n, int) or choose_n < 1:
            result.add_error(
                f"Advancement '{adv_id}' chooseN must be a positive integer, got {choose_n}."
            )


def validate_title_prerequisites(data: dict, result: ValidationResult) -> None:
    """Validate title prerequisites field."""
    if data.get("type") != "title":
        return

    system = data.get("system", {})
    prerequisites = system.get("prerequisites", {})

    if not prerequisites:
        result.add_warning("Title missing prerequisites field.")
        return

    # Check for value field
    value = prerequisites.get("value")
    if not value or not isinstance(value, str):
        result.add_error(
            f"Title prerequisites must have a 'value' string field describing the accomplishment."
        )


def validate_title_story(data: dict, result: ValidationResult) -> None:
    """Validate title story field."""
    if data.get("type") != "title":
        return

    system = data.get("system", {})
    story = system.get("story")

    if not story or not isinstance(story, str):
        result.add_warning(
            "Title missing story field (should be 1-2 flavorful sentences)."
        )
    elif len(story) > 200:
        result.add_warning(
            "Title story is too long (should be 1-2 sentences, ~50-100 chars)."
        )


def validate_dsid_format(data: dict, result: ValidationResult) -> None:
    """Validate _dsid field is kebab-case."""
    system = data.get("system", {})
    dsid = system.get("_dsid")

    if not dsid:
        return

    # Check if kebab-case (lowercase with hyphens, no spaces)
    if not re.match(r"^[a-z0-9-]+$", dsid):
        result.add_error(
            f"_dsid '{dsid}' must be kebab-case (lowercase with hyphens, no spaces)."
        )


def validate_effects_structure(data: dict, result: ValidationResult) -> None:
    """Validate effects array structure."""
    effects = data.get("effects", [])

    if not isinstance(effects, list):
        result.add_error(f"Effects must be an array, got {type(effects).__name__}.")
        return

    for effect in effects:
        # Check required fields
        if "name" not in effect:
            result.add_error("Effect missing 'name' field.")
        if "type" not in effect:
            result.add_error("Effect missing 'type' field.")
        if "_id" not in effect:
            result.add_error("Effect missing '_id' field.")

        # Check type is valid
        effect_type = effect.get("type")
        valid_effect_types = {"abilityModifier", "base"}
        if effect_type and effect_type not in valid_effect_types:
            result.add_error(
                f"Effect type '{effect_type}' is invalid. "
                f"Valid types: {', '.join(sorted(valid_effect_types))}."
            )

        # Check changes structure
        changes = effect.get("changes", [])
        if not isinstance(changes, list):
            result.add_error(
                f"Effect changes must be an array, got {type(changes).__name__}."
            )
            continue

        for change in changes:
            if "key" not in change:
                result.add_error("Effect change missing 'key' field.")
            if "mode" not in change:
                result.add_error("Effect change missing 'mode' field.")
            if "value" not in change:
                result.add_error("Effect change missing 'value' field.")

            # Validate mode
            mode = change.get("mode")
            valid_modes = {1, 2, 3, 4, 5}  # Foundry mode values
            if mode not in valid_modes:
                result.add_warning(
                    f"Effect change mode {mode} may not be valid. "
                    f"Common modes: 2 (additive), 4 (override)."
                )


def validate_damage_types_in_effects(data: dict, result: ValidationResult) -> None:
    """Validate damage types in effects."""
    effects = data.get("effects", [])

    for effect in effects:
        changes = effect.get("changes", [])

        for change in changes:
            key = change.get("key", "")

            # Check for damage immunity/weakness keys
            if "immunities." in key or "weaknesses." in key:
                damage_type = key.split(".")[-1]
                if damage_type and damage_type not in VALID_DAMAGE_TYPES:
                    result.add_error(
                        f"Invalid damage type '{damage_type}' in effect change key '{key}'. "
                        f"Valid types: {', '.join(sorted(VALID_DAMAGE_TYPES))}."
                    )


def validate_dice_notation(data: dict, result: ValidationResult) -> None:
    """
    Validate that reward descriptions do not contain D&D-style dice notation (d4, d8, d12, d20).

    Draw Steel uses fixed damage values, not dice notation. D&D-style dice
    (d4, d8, d12, d20) are not valid and indicate D&D/PF2e influence.
    """
    # D&D dice types to flag (not valid in Draw Steel)
    invalid_dice = {"d4", "d8", "d12", "d20"}

    system = data.get("system", {})
    description = system.get("description", {}).get("value", "")
    reward_name = data.get("name", "Unknown")

    # Find all dice notation patterns
    # Matches: 1d4, 2d8, 1d12, 3d20, etc. (case-insensitive)
    dice_matches = re.findall(r"\d+d\d+", description, re.IGNORECASE)

    for dice in dice_matches:
        dice_lower = dice.lower()

        # Check if it's D&D-style dice (d4, d8, d12, d20)
        for invalid_die in invalid_dice:
            if invalid_die in dice_lower:
                result.add_error(
                    f"Reward '{reward_name}' contains D&D-style dice notation '{dice}' "
                    f"in description. Draw Steel uses fixed damage values, not {invalid_die}. "
                    f"Use fixed values like '6' instead of '1d6', or '11' instead of '2d6'."
                )
                break


def validate_characteristic_bonuses(data: dict, result: ValidationResult) -> None:
    """
    Validate that consumables do not use direct characteristic bonuses (+X to [characteristic]).

    Draw Steel consumables use EDGE bonuses, not direct characteristic increases.
    Direct characteristic bonuses are VERY rare and reserved for leveled treasures only.
    """
    system = data.get("system", {})
    category = system.get("category")
    description = system.get("description", {}).get("value", "")
    reward_name = data.get("name", "Unknown")

    # Only check consumables (leveled treasures might have direct bonuses in rare cases)
    if category != "consumable":
        return

    # Patterns for direct characteristic bonuses
    # Matches: "+2 to Intuition", "gain +3 to Might", "+1 to Agility", etc.
    characteristic_bonus_patterns = [
        r"\+\d+\s+to\s+(?:might|agility|reason|intuition|presence)",
        r"gain\s+\+\d+\s+(?:might|agility|reason|intuition|presence)",
        r"characteristic\s+bonus\s+\+\d+",
        r"\+\d+\s+(?:might|agility|reason|intuition|presence)\s+bonus",
    ]

    for pattern in characteristic_bonus_patterns:
        matches = re.findall(pattern, description, re.IGNORECASE)
        if matches:
            result.add_error(
                f"Reward '{reward_name}' contains direct characteristic bonus '{matches[0]}'. "
                f"Draw Steel consumables should use EDGE bonuses instead. "
                f"Use 'edge on [characteristic] tests' not '+X to [characteristic]'."
            )


def validate_json_file(filepath: str) -> ValidationResult:
    """
    Validate a single JSON file and return a ValidationResult.
    """
    result = ValidationResult()

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        result.add_error(f"Invalid JSON: {e}")
        return result
    except FileNotFoundError:
        result.add_error(f"File not found: {filepath}")
        return result

    # Run all validations
    validate_item_type(data, result)
    validate_treasure_category(data, result)
    validate_echelon(data, result)
    validate_keywords_lowercase(data, result)
    validate_creation_keywords(data, result)
    validate_body_keyword(data, result)
    validate_equipment_keyword(data, result)
    validate_project_goal(data, result)
    validate_project_source(data, result)
    validate_roll_characteristics(data, result)
    validate_yield_structure(data, result)
    validate_id_format(data, result)
    validate_duplicate_ids(data, result)
    validate_leveled_scaling(data, result)
    validate_title_advancements(data, result)
    validate_title_prerequisites(data, result)
    validate_title_story(data, result)
    validate_dsid_format(data, result)
    validate_effects_structure(data, result)
    validate_damage_types_in_effects(data, result)
    validate_dice_notation(data, result)
    validate_characteristic_bonuses(data, result)

    return result


def validate_directory(directory: str) -> tuple:
    """
    Validate all JSON files in a directory.
    Returns (passed_count, failed_count, total_count).
    """
    passed = 0
    failed = 0
    total = 0

    path = Path(directory)
    if not path.exists():
        print(f"Error: Directory not found: {directory}")
        return 0, 0, 0

    json_files = list(path.glob("**/*.json"))

    for json_file in json_files:
        total += 1
        result = validate_json_file(str(json_file))
        result.print_report(json_file.name)

        if result.is_valid():
            passed += 1
        else:
            failed += 1

    print(f"\n{'=' * 60}")
    print(f"Summary: {passed}/{total} files passed validation")
    print(f"{'=' * 60}")

    return passed, failed, total


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Validate Draw Steel reward JSON files for Foundry VTT import"
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to JSON file or directory to validate (default: current directory)",
    )
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    parser.add_argument(
        "--strict", action="store_true", help="Treat warnings as errors"
    )

    args = parser.parse_args()

    path = Path(args.path)

    if path.is_file() and path.suffix == ".json":
        result = validate_json_file(str(path))
        result.print_report(path.name)

        if args.strict and result.warnings:
            result.passed = False
            result.errors.extend(result.warnings)
            result.warnings.clear()

        if args.json:
            output = {
                "file": path.name,
                "passed": result.passed,
                "errors": result.errors,
                "warnings": result.warnings,
            }
            print(json.dumps(output, indent=2))

        sys.exit(0 if result.passed else 1)

    elif path.is_dir():
        passed, failed, total = validate_directory(str(path))

        if args.json:
            output = {
                "directory": str(path),
                "passed": passed,
                "failed": failed,
                "total": total,
            }
            print(json.dumps(output, indent=2))

        sys.exit(0 if failed == 0 else 1)

    else:
        print(f"Error: Path not found or not a JSON file: {args.path}")
        sys.exit(1)


if __name__ == "__main__":
    main()
