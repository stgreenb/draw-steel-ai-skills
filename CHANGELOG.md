# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.6.0] - 2026-02-21

### Added
- **Free Strike Calculation:** Documented official rule: free strike equals tier 1 damage from signature ability
- **Immunity Numeric Values:** Explained damage reduction pattern (value = reduction, 1000 = total immunity)
- **Immunity Patterns by Creature Type:** Added patterns for undead, demons, devils, dragons
- **Feature Items:** Documented `type: "feature"` for passive traits
- **Prior Malice Features Pattern:** Added compendium reference pattern for undead and typed monsters
- **Summoning Abilities:** Documented malice costs and minion pattern for summons
- **Solo Turns Field:** Explained `turns: 2` gives two initiative slots
- **Compendium UUID References:** Added examples for cross-referencing in Foundry VTT
- **Potency Notation Mapping:** Added markdown-to-JSON conversion table

### Changed
- **Repository Renamed:** `draw-steel-monster-generator` → `draw-steel-ai-skills`
- **README.md:** Updated title to "Draw Steel AI Skills", added Retainer Generator to skills list
- **project.md:** Updated purpose to reflect multi-skill collection
- **Characteristic Distribution:** Clarified echelon value is guideline for highest characteristic

## [1.5.0] - 2026-02-05

### Added
- **Markdown Output Format:** Enhanced Markdown generation with YAML front matter for Draw Steel monsters
- **Markdown Validator:** New `ds_validator.py` validates Markdown stat blocks against Draw Steel rules

### Changed
- **Simplified Validation:** Validation now focuses on Draw Steel formulas (EV, Stamina, Damage, Free Strike) instead of Foundry-specific requirements for Markdown output
- **Enhanced Prompts:** Updated prompts for Markdown output with YAML structure
- **Improved Testing:** Test suite validates Markdown output alongside Foundry JSON

### Removed
- **json_to_markdown.py:** Removed unused JSON-to-Markdown converter (integrated into main workflow)

### Fixed
- **Success Rates:** Improved success rates through simplified validation workflow
- **Token Usage:** Reduced token consumption by optimizing prompt structure

### Notes
- **Skill Focus:** The Claude skill remains fully functional with Foundry JSON export via `--format foundry` and Markdown output as default

## [1.5.1] - 2026-02-10

### Removed
- **Webapp Version:** Removed webapp interface to focus solely on the skill version
- **Webapp Dependencies:** Removed all webapp-related code, Docker configurations, and dependencies

### Changed
- **Project Focus:** Simplified to skill-only implementation for better reliability and maintainability

### Notes
- **Migration:** Users should use the skill via Claude Code, OpenCode, or other compatible AI coding tools

## [1.4.0] - 2026-02-01

### Added
- **ID Generator Script:** Added `scripts/generate_foundry_ids.py` to generate unique 16-character alphanumeric IDs for Foundry VTT JSON
- **Duplicate ID Detection:** Enhanced validation script to detect duplicate `_id` values within the same JSON file
- **ID Generation Workflow:** Updated SKILL.md with instructions to use the ID generator script instead of manual generation
- **Self-Validation Checklist:** Updated to require use of ID generator script and check for duplicate IDs

### Changed
- **ID Format Instructions:** Replaced manual ID generation examples with script usage examples
- **Validation Error Messages:** Added guidance to use ID generator script when duplicate IDs are detected

### Fixed
- **ID Generation Errors:** Eliminated common LLM errors (wrong length, dashes, placeholders, duplicates) by providing automated ID generation

## [1.3.0] - 2026-01-30

### Added
- **Ability Type Examples:** Added examples for maneuver, freeTriggered, and none type abilities
- **Charge Attack Example:** Added example with "charge" keyword (optional)
- **Breath Weapon Example:** Added example with correct `["area", "magic"]` keywords
- **Ability Type Variety Section:** Added documentation covering all ability types and their purposes
- **Villain Action Usage Rules:** Added 3 usage rules (once per encounter, one per round, end of turn)
- **Inspiration Guidance:** Added explicit guidance that examples should inspire unique creations, not be copied verbatim
- **Custom Field Examples:** Added examples showing "custom" field in area targets for clarity

### Changed
- **Strike Keywords:** All strike examples now include "weapon" keyword
- **Target Types:** All strike examples now use "creatureObject" instead of "creature"
- **Breath/Spew Keywords:** Updated to use `["area", "magic"]` pattern instead of damage types
- **DO/DON'T Table:** Added 5 new rules for strike keywords, target types, breath keywords, custom fields, and inspiration usage
- **Villain Action Guidance:** Enhanced with specific usage rules from Monster Basics.md
- **Output Formats:** Added "Using Examples as Inspiration" section to prevent verbatim copying

### Fixed
- **LLM Compliance:** Updated examples to match official Draw Steel patterns
- **Foundry VTT Crashes:** Corrected patterns that cause crashes (invalid damage types, missing "weapon" keyword)
- **Example Copying:** Added guidance to prevent LLMs from copying examples verbatim instead of creating unique abilities

## [1.2.2] - 2026-01-30

### Added
- **Spend Field Validation:** Added validator to check all abilities have required `spend` field
- **Damage Type Validation:** Added validator to check for invalid D&D damage types (piercing, slashing, bludgeoning, etc.)
- **Spend Field Documentation:** Added section documenting spend field requirement
- **Spend Field Example:** Added spend field to main JSON example

### Changed
- **Valid Damage Types:** Updated keywords.json to only include Foundry-valid types (acid, cold, corruption, fire, holy, lightning, poison, psychic, sonic)
- **Removed D&D Damage Types:** Removed physical, slashing, bludgeoning, piercing from valid damage types

### Fixed
- **Foundry Crash Fix:** Missing `spend` field causes Foundry VTT to crash with "Cannot read properties of undefined (reading 'label')" error
- **Foundry Crash Fix:** Invalid damage types (piercing, slashing, bludgeoning, etc.) cause Foundry VTT to crash when trying to display damage
- **Self-Validation Checklist:** Added checks for spend field and valid damage types

## [1.2.1] - 2026-01-30

### Changed
- **ID Format Documentation:** Changed from "16 alphanumeric characters" to regex pattern `^[a-zA-Z0-9]{16}$`
- **Validation Error Messages:** Updated to include regex pattern in error messages
- **DO/DON'T Table:** Updated ID requirement to show regex pattern

### Fixed
- **LLM ID Format Compliance:** Regex pattern is easier for LLMs to parse correctly than numeric character count description

## [1.2.0] - 2026-01-30

### Added
- **Comprehensive Power Effects Documentation:** Added 170+ line section on power.roll.effects structure with official examples
- **Effect Type Reference:** Added table for damage/applied/forced/other effect types with use cases
- **Power Effects Rules:** Added documentation on when power.effects can be empty vs required
- **Official Examples:** Added 3 complete examples from Basilisk, Goblin, and Griffon monsters

### Changed
- **SKILL.md:** Updated Foundry VTT JSON example to use structured power.effects (was incorrect HTML format)
- **DO/DON'T Table:** Updated to show structured power.effects requirement, not empty effects
- **Self-Validation Checklist:** Added checks for power.effects structure and effect.before content

### Fixed
- **Validator Logic:** Fixed validate_power_effects() to only require structured effects for main action abilities
- **False Positives:** Triggered/freeTriggered/maneuver/type:none abilities now correctly allowed to have empty power.effects
- **Official Monster Validation:** Basilisk, Goblin Warrior, and Griffon now pass validation

## [1.1.0] - 2026-01-18

### Added (OpenSpec: add-monster-features)
- **Strike Bonus:** Added rule for adding highest characteristic to strike damage
- **Echelon-based Characteristics:** Highest characteristic = 1 + echelon (Level 1=+1, 2-4=+2, 5-7=+3, 8-10=+4)
- **Leader/Solo Bonuses:** +1 to highest characteristic (max +5), +1 to all potencies
- **Official Potency Formula:** Potency = Highest Characteristic − (3 − Tier)
- **Target Count Rules:** Normal=1 target, Elite/Leader/Solo=2 targets
- **Target Damage Scaling:** 0.8x for +1 target, 0.5x for +2+ targets, 1.2x for -1 target
- **Villain Actions:** Templates for Leaders/Solos (Opener, Crowd Control, Ultimate)
- **Solo Turn Rules:** Documentation for multiple turns per round
- **Minion "With Captain" trait:** Bonuses when led by a captain
- **Malice Features:** Templates for group-wide malice abilities
- **2 New Examples:** Level 5 Solo Brute (Hill Giant), Level 4 Elite Controller (Shadow Elf)

### Changed (OpenSpec: add-monster-features)
- Potency formula updated to official Monster Basics.md rules
- Characteristic tables now use echelon-based scaling
- Critical Rules expanded with 19 rules (was 15)
- Self-Validation Checklist updated with new verification items

## [1.0.0] - 2026-01-18

### Added
- SKILL.md for OpenCode native skill discovery
- scripts/calculate_stats.py with official Draw Steel formulas
- formulas.md with complete formula reference
- templates.md with ability patterns for all 9 roles
- examples.md with 5 complete creature stat blocks
- keywords.json with all valid keywords, conditions, and damage types
- pytest test suite with 90%+ coverage
- pyproject.toml for Poetry dependency management
- .flake8 and .pre-commit-config.yaml for code quality
- .github/workflows/test.yml for CI/CD
- .github/workflows/release.yml for automated releases

### Changed
- Updated all formulas to match official Monster Basics.md
- Changed tier multipliers from 1.0/1.5/2.0 to 0.6/1.1/1.4
- Updated organization modifiers (Solo is 6.0, Elite is 2.0)
- Updated role modifiers (Harrier is +20/+0, Brute is +30/+1)
- Free Strike now equals Tier 1 damage (was 2 + Level/2)
- All calculations now use ceil() rounding

### Fixed
- Removed all D&D terminology (no "vs. AC", "HP", "d20", "DC")
- Fixed Power Roll format to 2d10 + characteristic
- Fixed tier outcome ranges (≤11, 12-16, 17+)

### Removed
- D&D-based formulas and references
- Incorrect tier multipliers (1.0/1.5/2.0)
- Free Strike formula using 2 + Level/2

### Known Limitations
- Performance targets (30s generation, 3K tokens) are aspirational
- OpenCode integration not yet validated with production
- Claude Code/Web compatibility via SKILL.md is untested
