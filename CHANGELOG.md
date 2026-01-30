# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
