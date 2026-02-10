## ADDED Requirements

### Requirement: ID Generator Script

The skill SHALL provide a simple Python script to generate unique 16-character alphanumeric IDs for Foundry VTT JSON.

#### Scenario: Generate single ID
- **WHEN** the script is run without arguments
- **THEN** it SHALL output one 16-character alphanumeric ID to stdout
- **AND** the ID SHALL match the regex `^[a-zA-Z0-9]{16}$`
- **AND** the ID SHALL be generated using cryptographically secure random selection

#### Scenario: Generate multiple IDs
- **WHEN** the script is run with `--count N` or `-c N` argument
- **THEN** it SHALL output N unique 16-character alphanumeric IDs to stdout
- **AND** each ID SHALL be on a separate line
- **AND** all IDs SHALL match the regex `^[a-zA-Z0-9]{16}$`

#### Scenario: Script usage in SKILL.md instructions
- **WHEN** the SKILL.md instructions reference ID generation
- **THEN** it SHALL instruct LLMs to use the script instead of manual generation
- **AND** it SHALL provide clear examples: `python scripts/generate_foundry_ids.py --count 5`
- **AND** it SHALL explain that manual generation is error-prone

#### Scenario: Script dependencies
- **WHEN** the script is executed
- **THEN** it SHALL use only Python standard library modules
- **AND** it SHALL require no external dependencies
- **AND** it SHALL work with Python 3.6+

## MODIFIED Requirements

### Requirement: Self-Validation Checklist

The skill SHALL include a self-validation checklist that the LLM completes BEFORE outputting Foundry JSON.

#### Scenario: Pre-generation validation (updated)
- **WHEN** the skill generates JSON with `--format foundry` or `--format both`
- **THEN** the LLM SHALL verify:
  - Actor `type` is `"npc"`
  - All `_id` fields are exactly 16 characters (alphanumeric only)
  - All `_id` fields were generated using `scripts/generate_foundry_ids.py`
  - No duplicate `_id` values within the same monster
  - All items have valid `type` (`"ability"` or `"feature"`)
  - All abilities have valid `system.type` (main, maneuver, freeManeuver, triggered, freeTriggered, move, none, villain)
  - All abilities have valid `system.category` (heroic, freeStrike, signature, villain, or empty for features)
  - `system.monster.role` is valid (ambusher, artillery, brute, controller, defender, harrier, hexer, mount, support, solo)
  - `system.monster.organization` is valid (minion, horde, platoon, elite, leader, solo)
  - `system.monster.keywords` are all valid monster keywords
  - All ability `system.keywords` are valid ability keywords
  - Formula is `"@chr"` not characteristic name
  - Keywords are lowercase
  - For generated abilities (heroic, signature, villain), power effects is empty `{}`
  - No HTML entities in effect text
  - Required actor fields are present (stamina, characteristics, combat, monster stats)
  - Token configuration is valid (prototypeToken.bar1.attribute = "stamina")

#### Scenario: Validation before output
- **WHEN** validation fails
- **THEN** the LLM SHALL correct the errors before outputting JSON
- **AND** re-run validation until all checks pass

## ADDED Requirements

### Requirement: Duplicate ID Detection

The validation script SHALL detect duplicate `_id` values within the same Foundry VTT JSON file.

#### Scenario: Detect duplicate IDs
- **WHEN** the validation script runs on a JSON file
- **THEN** it SHALL check all `_id` fields for duplicates
- **AND** report an error if any duplicate `_id` values are found
- **AND** list all duplicate `_id` values in the error message

#### Scenario: No duplicate IDs
- **WHEN** the validation script runs on a JSON file with unique IDs
- **THEN** it SHALL NOT report any duplicate ID errors
- **AND** the validation for ID format and uniqueness SHALL pass