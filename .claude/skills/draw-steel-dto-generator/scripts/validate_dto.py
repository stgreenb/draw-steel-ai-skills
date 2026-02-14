#!/usr/bin/env python3
"""
DTO Validation Script for Draw Steel Dynamic Terrain Objectives

This script validates generated DTO stat blocks against Draw Steel patterns
and checks for common D&D terminology errors.
"""

import re
import sys
from pathlib import Path
from typing import Optional

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

VALID_CONDITIONS = {
    "bleeding",
    "dazed",
    "frightened",
    "grabbed",
    "prone",
    "restrained",
    "slowed",
    "taunted",
    "weakened",
}

VALID_ABILITY_KEYWORDS = {
    "area",
    "melee",
    "ranged",
    "strike",
    "weapon",
    "magic",
}

VALID_DTO_CATEGORIES = {
    "environmental-hazard",
    "fieldwork",
    "mechanism",
    "siege-engine",
    "power-fixture",
    "supernatural-object",
    "hazard",
    "trap",
    "trigger",
    "fortification",
    "relic",
}

VALID_DTO_ROLES = {
    "defender",
    "hexer",
    "ambusher",
    "artillery",
    "support",
    "controller",
}

EV_RANGES = {
    "environmental-hazard": {1: (1, 1), 2: (2, 3), 3: (3, 4)},
    "hazard": {1: (1, 1), 2: (2, 3), 3: (3, 4), 5: (7, 14)},
    "fieldwork": {1: (1, 2), 2: (3, 3)},
    "trap": {1: (1, 2), 2: (3, 3)},
    "mechanism": {1: (1, 2), 2: (3, 3), 3: (3, 4)},
    "trigger": {1: (2, 2)},
    "fortification": {2: (3, 4), 3: (3, 4)},
    "siege-engine": {2: (8, 8), 3: (10, 10), 4: (12, 12)},
    "power-fixture": {5: (7, 14)},
    "relic": {3: (20, 20), 4: (24, 24), 5: (7, 14)},
    "supernatural-object": {3: (20, 20), 4: (24, 24)},
}

STAMINA_RANGES = {
    "environmental-hazard": (3, 12),
    "fieldwork": (1, 9),
    "mechanism": (3, 9),
    "siege-engine": (25, 60),
    "power-fixture": (35, 60),
    "supernatural-object": (80, 140),
}

DAMAGE_BY_LEVEL = {
    1: {"tier1": (1, 4), "tier2": (3, 5), "tier3": (5, 6)},
    2: {"tier1": (3, 5), "tier2": (6, 9), "tier3": (9, 11)},
    3: {"tier1": (3, 5), "tier2": (6, 9), "tier3": (9, 12)},
    4: {"tier1": (6, 6), "tier2": (10, 10), "tier3": (13, 13)},
    5: {"tier1": (6, 6), "tier2": (11, 11), "tier3": (14, 14)},
}

DND_PATTERNS = [
    (r"\bDC\s*\d+", "DC notation (use potency checks like 'M < 2')"),
    (r"\bsaving throw\b", "'saving throw' (use 'save' or 'save ends')"),
    (r"\b[Dd]exterity\s+save", "Dexterity save (use 'Agility test' or 'A < X')"),
    (r"\b[Cc]onstitution\s+save", "Constitution save (use 'Might test' or 'M < X')"),
    (r"\b[Ww]isdom\s+save", "Wisdom save (use 'Intuition test' or 'I < X')"),
    (r"\b[Cc]harisma\s+save", "Charisma save (use 'Presence test' or 'P < X')"),
    (r"\b[Ss]trength\s+save", "Strength save (use 'Might test' or 'M < X')"),
    (
        r"\d+d(4|8|12|20)(?:\s*\+\s*\d+)?\s+(?:damage|fire|cold|poison|acid)",
        "dice notation with d4/d8/d12/d20 (Draw Steel uses d3/d6/d10 only)",
    ),
    (r"\bhalf\s+damage\b", "'half damage' (not used in Draw Steel)"),
    (r"\bon\s+a\s+failed\s+save\b", "'on a failed save' (use potency checks)"),
    (r"\bsuccessful\s+save\b", "'successful save' (use potency checks)"),
]


class ValidationResult:
    def __init__(self):
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.passed: bool = True

    def add_error(self, message: str) -> None:
        self.errors.append(message)
        self.passed = False

    def add_warning(self, message: str) -> None:
        self.warnings.append(message)

    def is_valid(self) -> bool:
        return self.passed

    def print_report(self, filename: str) -> None:
        print(f"\n{'=' * 60}")
        print(f"DTO Validation Report: {filename}")
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


class DTONValidator:
    """Validator for Draw Steel Dynamic Terrain Objectives."""

    def __init__(self):
        self.result = ValidationResult()

    def validate_header(self, content: str) -> Optional[dict]:
        """Validate DTO header line and extract metadata."""
        header_pattern = r"#+\s*(.+?)\s*\(Level\s*(\d+)\s+([^)]+)\)"
        match = re.search(header_pattern, content)

        if not match:
            self.result.add_error(
                "Missing or invalid header. Expected: '###### Name (Level X Category Role)'"
            )
            return None

        name = match.group(1).strip()
        level = int(match.group(2))
        category_role = match.group(3).strip()

        parts = category_role.split()
        role = ""
        category = ""

        for i, part in enumerate(parts):
            part_lower = part.lower()
            if part_lower in VALID_DTO_ROLES:
                role = part_lower
                category = " ".join(parts[:i]).lower()
                break
        else:
            category = category_role.lower()

        category_normalized = category.replace(" ", "-")

        if (
            category_normalized not in VALID_DTO_CATEGORIES
            and category not in VALID_DTO_CATEGORIES
        ):
            self.result.add_warning(
                f"Unusual category '{category}'. Typical: Environmental Hazard, Fieldwork, Mechanism, Siege Engine, Power Fixture, Supernatural Object"
            )

        if role and role not in VALID_DTO_ROLES:
            self.result.add_warning(
                f"Unusual role '{role}'. Typical: Defender, Hexer, Ambusher, Artillery, Support, Controller"
            )

        return {
            "name": name,
            "level": level,
            "category": category_normalized,
            "role": role,
        }

    def validate_ev(self, content: str, metadata: Optional[dict]) -> None:
        """Validate EV value and format."""
        ev_pattern = r"\*\*EV:\*\*\s*(.+?)(?:\n|$)"
        match = re.search(ev_pattern, content)

        if not match:
            self.result.add_error(
                "Missing EV field. Required format: '- **EV:** [value]'"
            )
            return

        ev_text = match.group(1).strip()

        if re.search(r"per\s+\d+\s*x\s*\d+", ev_text, re.IGNORECASE):
            pass
        elif ev_text == "-":
            self.result.add_warning("DTO has EV: - (should typically have an EV value)")
        else:
            try:
                ev_value = int(ev_text)
                if metadata and metadata["category"] in EV_RANGES:
                    level = metadata["level"]
                    cat_ranges = EV_RANGES[metadata["category"]]
                    if level in cat_ranges:
                        min_ev, max_ev = cat_ranges[level]
                        if not (min_ev <= ev_value <= max_ev):
                            self.result.add_warning(
                                f"EV {ev_value} outside typical range ({min_ev}-{max_ev}) for {metadata['category']} level {level}"
                            )
            except ValueError:
                self.result.add_warning(f"Non-integer EV value: '{ev_text}'")

    def validate_stamina(self, content: str, metadata: Optional[dict]) -> None:
        """Validate Stamina value."""
        stamina_pattern = r"\*\*Stamina:\*\*\s*(.+?)(?:\n|$)"
        match = re.search(stamina_pattern, content)

        if not match:
            self.result.add_error(
                "Missing Stamina field. Required format: '- **Stamina:** [value or -]'"
            )
            return

        stamina_text = match.group(1).strip()

        if stamina_text == "-":
            return

        if "per square" in stamina_text.lower():
            stamina_match = re.search(
                r"(\d+)\s*per\s*square", stamina_text, re.IGNORECASE
            )
            if stamina_match:
                stamina_value = int(stamina_match.group(1))
            else:
                self.result.add_warning(
                    f"Could not parse per-square Stamina: '{stamina_text}'"
                )
                return
        else:
            try:
                stamina_value = int(stamina_text)
            except ValueError:
                self.result.add_warning(f"Non-integer Stamina value: '{stamina_text}'")
                return

        if metadata and metadata["category"] in STAMINA_RANGES:
            min_sta, max_sta = STAMINA_RANGES[metadata["category"]]
            if not (min_sta <= stamina_value <= max_sta * 3):
                self.result.add_warning(
                    f"Stamina {stamina_value} outside typical range ({min_sta}-{max_sta}) for {metadata['category']}"
                )

    def validate_size(self, content: str) -> None:
        """Validate Size field."""
        size_pattern = r"\*\*Size:\*\*\s*(.+?)(?:\n|$)"
        match = re.search(size_pattern, content)

        if not match:
            self.result.add_error(
                "Missing Size field. Required format: '- **Size:** [value]'"
            )
            return

        size_text = match.group(1).strip()
        valid_sizes = ["1S", "1M", "1L", "1", "2", "3", "4", "5"]

        if not any(size_text.startswith(s) for s in valid_sizes):
            if not re.search(r"\d+\s*(square|squares|x)", size_text, re.IGNORECASE):
                self.result.add_warning(
                    f"Unusual Size value: '{size_text}'. Typical: 1S, 1M, 1L, 2, 3, or 'X squares'"
                )

    def validate_deactivate(self, content: str) -> None:
        """Validate Deactivate section."""
        if "🌀 **Deactivate**" not in content and "> 🌀 **Deactivate**" not in content:
            self.result.add_error(
                "Missing Deactivate section. Every DTO needs a Deactivate section (even if 'must be destroyed')."
            )

    def validate_activate(self, content: str, metadata: Optional[dict]) -> None:
        """Validate Activate section."""
        has_activate = "❕ **Activate**" in content or "> ❕ **Activate**" in content

        if metadata and metadata["category"] in [
            "siege-engine",
            "power-fixture",
            "relic",
        ]:
            return

        if not has_activate:
            self.result.add_warning(
                "Missing Activate section. Most DTOs should have an Activate section with trigger condition."
            )

    def validate_power_roll(self, content: str) -> None:
        """Validate power roll structure."""
        power_roll_pattern = r"Power Roll\s*\+\s*(\d+):"
        matches = list(re.finditer(power_roll_pattern, content))

        for match in matches:
            modifier = int(match.group(1))
            if modifier < 0 or modifier > 5:
                self.result.add_warning(
                    f"Unusual power roll modifier: +{modifier}. Typical range is +0 to +5."
                )

        tier_pattern = r"[-*]\s*\*\*?(≤11|12-16|17\+)"
        for roll_match in matches:
            start = roll_match.end()
            end = start + 500
            roll_section = content[start:end]

            tiers_found = re.findall(tier_pattern, roll_section)
            if len(tiers_found) < 3:
                self.result.add_error(
                    f"Power Roll missing tier outcomes. Required: ≤11, 12-16, 17+"
                )

    def validate_damage_type(self, content: str) -> None:
        """Validate that damage has a type specified for elemental hazards."""
        has_elemental_keywords = any(
            keyword in content.lower()
            for keyword in [
                "fire",
                "cold",
                "acid",
                "poison",
                "lightning",
                "corruption",
                "psychic",
                "holy",
                "sonic",
            ]
        )

        if has_elemental_keywords:
            damage_pattern = r"(\d+)\s+damage(?!\s+(?:fire|cold|acid|poison|lightning|holy|psychic|corruption|sonic))"
            matches = re.findall(damage_pattern, content, re.IGNORECASE)

            if matches and len(matches) > 2:
                self.result.add_warning(
                    f"Found {len(matches)} damage value(s) without damage type. Elemental hazards should specify type (fire, cold, acid, poison, etc.). Physical traps can use 'damage' without type."
                )

    def validate_conditions(self, content: str) -> None:
        """Validate condition format and duration."""
        potency_pattern = r"([MARI])\s*<\s*(-?\d+)\s+(\w+)"
        matches = re.findall(potency_pattern, content)

        for char, value, condition in matches:
            condition_lower = condition.lower()
            if condition_lower in ["the", "a", "an", "takes", "push", "is"]:
                continue
            if condition_lower not in VALID_CONDITIONS:
                if condition_lower not in ["burning"]:
                    self.result.add_warning(
                        f"Potency check uses unusual condition '{condition}'. Valid: {', '.join(sorted(VALID_CONDITIONS))}"
                    )

        condition_no_duration = r"([MARI])\s*<\s*(-?\d+)\s+(slowed|dazed|weakened|frightened|restrained|taunted)(?!\s*\()"
        matches = re.findall(condition_no_duration, content, re.IGNORECASE)
        for char, value, condition in matches:
            self.result.add_warning(
                f"Condition '{condition}' has no duration. Consider '(save ends)' or '(EoT)'."
            )

    def validate_no_dnd_terminology(self, content: str) -> None:
        """Check for D&D terminology that should be avoided."""
        for pattern, description in DND_PATTERNS:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                self.result.add_error(
                    f"Found D&D terminology: '{matches[0]}' ({description}). Use Draw Steel terminology instead."
                )

    def validate_keywords(self, content: str) -> None:
        """Validate ability keywords."""
        keyword_pattern = r"\*\*([^|*]+)\*\*\s*\|\s*\*\*[^|]+\*\*\s*\|\s*\n\s*\|"
        matches = re.findall(keyword_pattern, content)

        for keywords_str in matches:
            keywords_str = keywords_str.strip()
            if keywords_str.startswith("-"):
                keywords_str = keywords_str[1:].strip()
            keywords = [k.strip().lower() for k in keywords_str.split(",")]
            for keyword in keywords:
                if keyword and keyword not in VALID_ABILITY_KEYWORDS and keyword != "-":
                    if keyword not in [
                        "free triggered action",
                        "main action (adjacent creature)",
                    ]:
                        self.result.add_warning(
                            f"Unusual ability keyword '{keyword}'. Valid: {', '.join(sorted(VALID_ABILITY_KEYWORDS))}"
                        )

    def validate_siege_engine(self, content: str, metadata: Optional[dict]) -> None:
        """Validate Siege Engine specific structure."""
        if not metadata or metadata["category"] not in ["siege-engine"]:
            return

        if "Main action (Adjacent creature)" not in content:
            self.result.add_error(
                "Siege Engine abilities must include 'Main action (Adjacent creature)' label."
            )

        if "Reload" not in content and "reload" not in content.lower():
            self.result.add_warning(
                "Siege Engine should have a Reload ability for its primary attack."
            )

    def validate_hidden(self, content: str) -> None:
        """Validate Hidden property format."""
        if "Hidden" in content or "hidden" in content:
            if "⭐️ **Hidden**" not in content and "> ⭐️ **Hidden**" not in content:
                self.result.add_warning(
                    "Hidden property should use format: '> ⭐️ **Hidden**'"
                )

    def validate_link(self, content: str) -> None:
        """Validate Link field for trigger mechanisms."""
        if "Link:" in content:
            link_pattern = r"Link:\s*(.+?)(?:\n|$)"
            match = re.search(link_pattern, content)
            if match and "linked to another mechanism" not in match.group(1).lower():
                self.result.add_warning(
                    "Link field should describe connection to linked mechanism."
                )

    def validate(self, content: str) -> ValidationResult:
        """Run all validations on DTO content."""
        metadata = self.validate_header(content)

        self.validate_ev(content, metadata)
        self.validate_stamina(content, metadata)
        self.validate_size(content)
        self.validate_deactivate(content)
        self.validate_activate(content, metadata)
        self.validate_power_roll(content)
        self.validate_damage_type(content)
        self.validate_conditions(content)
        self.validate_no_dnd_terminology(content)
        self.validate_keywords(content)
        self.validate_siege_engine(content, metadata)
        self.validate_hidden(content)
        self.validate_link(content)

        return self.result


def validate_dto_file(filepath: str) -> ValidationResult:
    """Validate a single DTO file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        result = ValidationResult()
        result.add_error(f"File not found: {filepath}")
        return result

    validator = DTONValidator()
    return validator.validate(content)


def validate_directory(directory: str) -> tuple:
    """Validate all markdown files in a directory."""
    passed = 0
    failed = 0
    total = 0

    path = Path(directory)
    if not path.exists():
        print(f"Error: Directory not found: {directory}")
        return 0, 0, 0

    md_files = list(path.glob("**/*.md"))

    for md_file in md_files:
        total += 1
        result = validate_dto_file(str(md_file))
        result.print_report(md_file.name)

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

    parser = argparse.ArgumentParser(description="Validate Draw Steel DTO stat blocks")
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to markdown file or directory to validate (default: current directory)",
    )
    parser.add_argument(
        "--strict", action="store_true", help="Treat warnings as errors"
    )

    args = parser.parse_args()

    path = Path(args.path)

    if path.is_file() and path.suffix == ".md":
        result = validate_dto_file(str(path))
        result.print_report(path.name)

        if args.strict and result.warnings:
            result.passed = False
            result.errors.extend(result.warnings)
            result.warnings.clear()

        sys.exit(0 if result.passed else 1)

    elif path.is_dir():
        passed, failed, total = validate_directory(str(path))
        sys.exit(0 if failed == 0 else 1)

    else:
        print(f"Error: Path not found: {args.path}")
        sys.exit(1)


if __name__ == "__main__":
    main()
