#!/usr/bin/env python3
"""
Foundry VTT Object Actor JSON Validation Script for Draw Steel DTO Generator

This script validates generated Object actor JSON files against common errors
that cause import failures in Foundry VTT for the Draw Steel system.
"""

import json
import re
import sys
from pathlib import Path

VALID_OBJECT_CATEGORIES = {
    "hazard",
    "trap",
    "trigger",
    "siegeEngine",
    "relic",
    "fortification",
}

VALID_OBJECT_ROLES = {
    "ambusher",
    "artillery",
    "brute",
    "controller",
    "defender",
    "harrier",
    "hexer",
    "mount",
    "support",
    "",
}

VALID_ABILITY_KEYWORDS = {
    "animal",
    "animapathy",
    "area",
    "charge",
    "chronopathy",
    "cryokinesis",
    "earth",
    "fire",
    "green",
    "magic",
    "melee",
    "metamorphosis",
    "psionic",
    "pyrokinesis",
    "ranged",
    "resopathy",
    "rot",
    "performance",
    "strike",
    "telekinesis",
    "telepathy",
    "void",
    "weapon",
}

VALID_ABILITY_TYPES = {
    "main",
    "maneuver",
    "freeManeuver",
    "triggered",
    "freeTriggered",
    "move",
    "none",
    "villain",
}

VALID_ABILITY_CATEGORIES = {"heroic", "freeStrike", "signature", "villain"}

VALID_ITEM_TYPES = {"ability", "feature"}

VALID_ABILITY_DISTANCES = {
    "melee",
    "ranged",
    "meleeRanged",
    "aura",
    "burst",
    "cube",
    "line",
    "wall",
    "special",
    "self",
}

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
        print(f"\n{'=' * 60}")
        print(f"Object Actor Validation Report: {filename}")
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
    if not isinstance(value, str):
        return False
    return bool(re.match(r"^[a-zA-Z0-9]{16}$", value))


def validate_actor_type(data: dict, result: ValidationResult) -> None:
    actor_type = data.get("type")
    if actor_type != "object":
        result.add_error(f"Actor type must be 'object' for DTOs, got '{actor_type}'")


def validate_object_category(data: dict, result: ValidationResult) -> None:
    system = data.get("system", {})
    obj = system.get("object", {})
    category = obj.get("category")
    if category and category not in VALID_OBJECT_CATEGORIES:
        result.add_error(
            f"Invalid object category '{category}'. "
            f"Must be one of: {', '.join(sorted(VALID_OBJECT_CATEGORIES))}"
        )


def validate_object_role(data: dict, result: ValidationResult) -> None:
    system = data.get("system", {})
    obj = system.get("object", {})
    role = obj.get("role")
    if role is not None and role not in VALID_OBJECT_ROLES:
        result.add_error(
            f"Invalid object role '{role}'. "
            f"Must be one of: {', '.join(sorted(VALID_OBJECT_ROLES))}"
        )


def validate_object_level(data: dict, result: ValidationResult) -> None:
    system = data.get("system", {})
    obj = system.get("object", {})
    level = obj.get("level")
    if level is None:
        result.add_error("Missing system.object.level")
    elif not isinstance(level, int) or level < 0:
        result.add_error(
            f"Invalid system.object.level (must be non-negative integer), got: {level}"
        )


def validate_stamina(data: dict, result: ValidationResult) -> None:
    system = data.get("system", {})
    stamina = system.get("stamina", {})

    if not isinstance(stamina.get("value"), int) or stamina.get("value", 0) < 0:
        result.add_error(
            "Missing or invalid system.stamina.value (must be non-negative integer)"
        )
    if not isinstance(stamina.get("max"), int) or stamina.get("max", 0) < 0:
        result.add_error(
            "Missing or invalid system.stamina.max (must be non-negative integer)"
        )


def validate_characteristics(data: dict, result: ValidationResult) -> None:
    system = data.get("system", {})
    characteristics = system.get("characteristics", {})
    required_chars = ["might", "agility", "reason", "intuition", "presence"]

    for char in required_chars:
        if char not in characteristics:
            result.add_error(f"Missing system.characteristics.{char}")
        else:
            char_value = characteristics[char]
            if isinstance(char_value, dict):
                if not isinstance(char_value.get("value"), int):
                    result.add_error(f"Invalid system.characteristics.{char}.value")
                if "banes" in char_value and not isinstance(
                    char_value.get("banes"), int
                ):
                    result.add_error(
                        f"Invalid system.characteristics.{char}.banes (must be integer)"
                    )
                if "edges" in char_value and not isinstance(
                    char_value.get("edges"), int
                ):
                    result.add_error(
                        f"Invalid system.characteristics.{char}.edges (must be integer)"
                    )
            elif isinstance(char_value, int):
                pass
            else:
                result.add_error(f"Invalid system.characteristics.{char}")


def validate_movement(data: dict, result: ValidationResult) -> None:
    system = data.get("system", {})
    movement = system.get("movement")

    if movement is not None:
        if not isinstance(movement, dict):
            result.add_error(
                f"system.movement must be null (static) or an object, got: {type(movement).__name__}"
            )
        else:
            if "value" in movement and not isinstance(
                movement.get("value"), (int, type(None))
            ):
                result.add_error(
                    "Invalid system.movement.value (must be integer or null)"
                )


def validate_id_format(data: dict, result: ValidationResult, path: str = "") -> None:
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
                            f"Got {len(value)} chars: {value}"
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
                f"Duplicate _id value found: '{dup_id}' appears {len(paths)} times at: {', '.join(paths)}"
            )


def validate_item_types(data: dict, result: ValidationResult) -> None:
    items = data.get("items", [])
    for item in items:
        item_type = item.get("type")
        if item_type not in VALID_ITEM_TYPES:
            result.add_error(
                f"Item '{item.get('name', 'Unknown')}' has invalid type '{item_type}'. "
                f"Must be one of: {', '.join(sorted(VALID_ITEM_TYPES))}"
            )


def validate_ability_keywords(data: dict, result: ValidationResult) -> None:
    items = data.get("items", [])
    for item in items:
        if item.get("type") == "ability":
            system = item.get("system", {})
            keywords = system.get("keywords", [])

            for keyword in keywords:
                if keyword not in VALID_ABILITY_KEYWORDS:
                    result.add_error(
                        f"Ability '{item.get('name', 'Unknown')}' has invalid keyword '{keyword}'. "
                        f"Must be one of: {', '.join(sorted(VALID_ABILITY_KEYWORDS))}"
                    )


def validate_ability_distance(data: dict, result: ValidationResult) -> None:
    items = data.get("items", [])

    for item in items:
        if item.get("type") == "ability":
            system = item.get("system", {})
            distance = system.get("distance", {})
            distance_type = distance.get("type", "")

            if distance_type and distance_type not in VALID_ABILITY_DISTANCES:
                result.add_error(
                    f"Ability '{item.get('name', 'Unknown')}' has invalid distance type '{distance_type}'. "
                    f"Must be one of: {', '.join(sorted(VALID_ABILITY_DISTANCES))}."
                )


def validate_damage_types(data: dict, result: ValidationResult) -> None:
    items = data.get("items", [])
    for item in items:
        if item.get("type") == "ability":
            system = item.get("system", {})
            power = system.get("power", {})
            effects = power.get("effects", {})

            for effect_id, effect in effects.items():
                if effect.get("type") == "damage":
                    damage = effect.get("damage", {})
                    for tier_name in ["tier1", "tier2", "tier3"]:
                        tier = damage.get(tier_name, {})
                        types = tier.get("types", [])

                        if not isinstance(types, list):
                            continue

                        for damage_type in types:
                            if damage_type and damage_type not in VALID_DAMAGE_TYPES:
                                result.add_error(
                                    f"Ability '{item.get('name', 'Unknown')}' uses invalid damage type "
                                    f"'{damage_type}'. Valid types: {', '.join(sorted(VALID_DAMAGE_TYPES))}."
                                )


def validate_square_stamina(data: dict, result: ValidationResult) -> None:
    system = data.get("system", {})
    obj = system.get("object", {})
    stamina = system.get("stamina", {})

    square_stamina = obj.get("squareStamina", False)
    area = obj.get("area")

    if square_stamina and area is None:
        result.add_warning(
            "Object has squareStamina=true but no area specified. "
            "Per-square stamina DTOs should have area defined."
        )


def validate_system_version(data: dict, result: ValidationResult) -> None:
    stats = data.get("_stats", {})
    version = stats.get("systemVersion", "")

    if not version:
        result.add_warning("Missing _stats.systemVersion")
    elif version not in ["0.10.0", "0.9.0"]:
        result.add_warning(
            f"Unexpected systemVersion '{version}'. Expected '0.10.0' for v0.10.0 features."
        )


def validate_can_flank(data: dict, result: ValidationResult) -> None:
    system = data.get("system", {})
    statuses = system.get("statuses", {})

    if "canFlank" in statuses:
        if not isinstance(statuses.get("canFlank"), bool):
            result.add_error(
                f"Invalid system.statuses.canFlank (must be boolean), got: {type(statuses.get('canFlank')).__name__}"
            )


def validate_json_file(filepath: str) -> ValidationResult:
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

    validate_actor_type(data, result)
    validate_object_category(data, result)
    validate_object_role(data, result)
    validate_object_level(data, result)
    validate_stamina(data, result)
    validate_characteristics(data, result)
    validate_movement(data, result)
    validate_can_flank(data, result)
    validate_square_stamina(data, result)
    validate_id_format(data, result)
    validate_duplicate_ids(data, result)
    validate_item_types(data, result)
    validate_ability_keywords(data, result)
    validate_ability_distance(data, result)
    validate_damage_types(data, result)
    validate_system_version(data, result)

    return result


def validate_directory(directory: str) -> tuple:
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
    import argparse

    parser = argparse.ArgumentParser(
        description="Validate Draw Steel Object actor JSON files for Foundry VTT import"
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
