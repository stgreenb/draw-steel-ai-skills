# foundry-export Specification

## Purpose
TBD - created by archiving change add-foundry-json-validation. Update Purpose after archive.
## Requirements
### Requirement: Foundry JSON Validation Script
The generator SHALL provide a standalone validation script that checks Foundry VTT JSON output for common errors before import.

#### Scenario: Validate ID format
- **WHEN** the validation script runs on a JSON file
- **THEN** it SHALL check that all `_id` fields contain exactly 16 alphanumeric characters (a-z, A-Z, 0-9)
- **AND** report an error for any ID that is too short, too long, or contains invalid characters
- **AND** report an error for UUID format (dashes like `a1b2c3d4-e5f6-7890-abcd-ef1234567890`)
- **AND** report an error for placeholder text like `monster-uuid`

#### Scenario: Validate actor type
- **WHEN** the validation script runs on a JSON file
- **THEN** it SHALL verify that the root `type` field equals `"npc"` for monster actors
- **AND** report an error for `"hero"` or other actor types

#### Scenario: Validate item types
- **WHEN** the validation script runs on a JSON file
- **THEN** it SHALL verify that all items in the `items` array have `type` of `"ability"` or `"feature"`
- **AND** report an error for other item types like `"class"`, `"ancestry"`, `"treasure"`, etc.

#### Scenario: Validate ability type (action type)
- **WHEN** the validation script runs on a JSON file
- **THEN** it SHALL verify that all abilities have a valid `system.type`:
  - `"main"` - Main Action
  - `"maneuver"` - Maneuver
  - `"freeManeuver"` - Free Maneuver
  - `"triggered"` - Triggered Action
  - `"freeTriggered"` - Free Triggered Action
  - `"move"` - Move Action
  - `"none"` - No Action Type
  - `"villain"` - Villain Action
- **AND** report an error for invalid types

#### Scenario: Validate ability category
- **WHEN** the validation script runs on a JSON file
- **THEN** it SHALL verify that all abilities have a valid `system.category`:
  - `"heroic"` - Heroic Action
  - `"freeStrike"` - Free Strike
  - `"signature"` - Signature Attack
  - `"villain"` - Villain Action
- **AND** report an error for invalid categories

#### Scenario: Validate monster role
- **WHEN** the validation script runs on a JSON file
- **THEN** it SHALL verify that `system.monster.role` is a valid role:
  - `"ambusher"` - Ambusher
  - `"artillery"` - Artillery
  - `"brute"` - Brute
  - `"controller"` - Controller
  - `"defender"` - Defender
  - `"harrier"` - Harrier
  - `"hexer"` - Hexer
  - `"mount"` - Mount
  - `"support"` - Support
- **AND** report an error for invalid roles

#### Scenario: Validate monster organization
- **WHEN** the validation script runs on a JSON file
- **THEN** it SHALL verify that `system.monster.organization` is a valid organization:
  - `"minion"` - Minion
  - `"horde"` - Horde
  - `"platoon"` - Platoon
  - `"elite"` - Elite
  - `"leader"` - Leader
  - `"solo"` - Solo
- **AND** report an error for invalid organizations

#### Scenario: Validate monster keywords
- **WHEN** the validation script runs on a JSON file
- **THEN** it SHALL verify that `system.monster.keywords` only contains valid monster keywords:
  - `"abyssal"`, `"accursed"`, `"animal"`, `"beast"`, `"construct"`, `"dragon"`, `"elemental"`, `"fey"`, `"giant"`, `"horror"`, `"humanoid"`, `"infernal"`, `"plant"`, `"soulless"`, `"swarm"`, `"undead"`
- **AND** report an error for invalid monster keywords

#### Scenario: Validate ability keywords
- **WHEN** the validation script runs on a JSON file
- **THEN** it SHALL verify that all ability `system.keywords` only contains valid ability keywords:
  - `"animal"`, `"animapathy"`, `"area"`, `"charge"`, `"chronopathy"`, `"cryokinesis"`, `"earth"`, `"fire"`, `"green"`, `"magic"`, `"melee"`, `"metamorphosis"`, `"psionic"`, `"pyrokinesis"`, `"ranged"`, `"resopathy"`, `"rot"`, `"performance"`, `"strike"`, `"telekinesis"`, `"telepathy"`, `"void"`, `"weapon"`
- **AND** report an error for invalid ability keywords

#### Scenario: Validate formula syntax
- **WHEN** the validation script runs on a JSON file
- **THEN** it SHALL verify that all `system.power.roll.formula` fields equal `"@chr"`
- **AND** report an error for any formula using characteristic names like `"@might"`, `"@agility"`, `"@reason"`, `"@presence"`, or `"@intuition"`

#### Scenario: Validate keywords format
- **WHEN** the validation script runs on a JSON file
- **THEN** it SHALL verify all keywords are lowercase strings
- **AND** report an error for capitalized keywords like `"Melee"`, `"Weapon"`, `"Fey"`, `"Humanoid"`

#### Scenario: Validate power effects structure
- **WHEN** the validation script runs on a JSON file
- **THEN** for generated abilities (abilities with `system.category` of `"heroic"`, `"signature"`, or `"villain"`), it SHALL verify that `system.power.effects` is empty `{}`
- **AND** for abilities with `system.category` of `"freeStrike"` or no category, `system.power.effects` may contain data
- **AND** report a warning for non-empty effects on generated abilities, as the AI cannot correctly generate the complex power roll effect structure
- **NOTE**: Official Draw Steel compendium monsters CAN have populated `power.effects` - this rule is specifically for AI-generated content to prevent malformed power roll structures

#### Scenario: Detect HTML entities in effect text
- **WHEN** the validation script runs on a JSON file
- **THEN** it SHALL scan `system.effect.before` and `system.effect.after` fields for HTML entities
- **AND** report a warning for `&lt;`, `&gt;`, `&amp;` and suggest using raw `<`, `>`, `&` instead

#### Scenario: Validate required actor fields
- **WHEN** the validation script runs on a JSON file
- **THEN** it SHALL verify the actor has all required NPC fields:
  - `system.stamina.value` and `system.stamina.max` (positive integers)
  - `system.characteristics` with might, agility, reason, intuition, presence
  - `system.combat.save.threshold` (positive integer)
  - `system.combat.size.value` (positive integer)
  - `system.monster.level` (positive integer)
  - `system.monster.ev` (positive integer)
- **AND** report an error for missing or invalid required fields

#### Scenario: Validate token configuration
- **WHEN** the validation script runs on a JSON file
- **THEN** it SHALL verify `prototypeToken` configuration:
  - `prototypeToken.bar1.attribute` equals `"stamina"`
  - `prototypeToken.width` and `prototypeToken.height` are positive integers
  - `prototypeToken.disposition` is -1, 0, or 1
- **AND** report a warning for missing or invalid token configuration

### Requirement: Test Coverage with Real Draw Steel Monsters
The validation script SHALL be tested against official Draw Steel monster compendium files to ensure it correctly validates real monsters.

#### Test Scenario: Validate Ajax the Invincible (Solo Boss)
- **GIVEN** the monster file at `src/packs/monsters/Ajax_the_Invincible_1duzR7U5imjJBje4/npc_Ajax_the_Invincible_DZKCzrvXRPBUjUJf.json`
- **WHEN** the validation script runs
- **THEN** it SHALL pass all validation rules:
  - Actor `type` is `"npc"` ✓
  - All `_id` fields are exactly 16 alphanumeric characters ✓
  - Items have valid `type` (`"ability"` or `"feature"`) ✓
  - Abilities have valid `system.type` values (main, maneuver, triggered, villain, none) ✓
  - Abilities have valid `system.category` values (signature, heroic, villain, or empty) ✓
  - Monster `system.monster.role` is `"solo"` ✓
  - Monster `system.monster.organization` is `"solo"` ✓
  - Monster keywords are valid and lowercase (`["humanoid"]`) ✓
  - Formulas are `"@chr"` ✓
  - Keywords are lowercase ✓

#### Test Scenario: Validate Minotaur Brute (Standard Monster)
- **GIVEN** a minotaur brute monster file from `src/packs/monsters`
- **WHEN** the validation script runs
- **THEN** it SHALL pass all validation rules:
  - Actor `type` is `"npc"` ✓
  - All `_id` fields are exactly 16 alphanumeric characters ✓
  - Monster `system.monster.role` is `"brute"` ✓
  - Monster `system.monster.organization` is `"platoon"` or similar ✓
  - Monster keywords include valid keywords like `"humanoid"`, `"giant"` ✓

#### Test Scenario: Validate Goblin Ambusher (Small Monster)
- **GIVEN** a goblin ambusher monster file from `src/packs/monsters`
- **WHEN** the validation script runs
- **THEN** it SHALL pass all validation rules:
  - Actor `type` is `"npc"` ✓
  - Monster `system.monster.role` is `"ambusher"` ✓
  - Monster `system.monster.organization` is `"horde"` ✓
  - Monster keywords include `"humanoid"` ✓

#### Test Scenario: Validate Dragon (Solo Elite Monster)
- **GIVEN** a dragon monster file from `src/packs/monsters/Dragons_1xAB7dzxBYqdc7qX`
- **WHEN** the validation script runs
- **THEN** it SHALL pass all validation rules:
  - Actor `type` is `"npc"` ✓
  - Monster `system.monster.role` is `"solo"` ✓
  - Monster keywords include `"dragon"` ✓
  - All `_id` fields are exactly 16 characters ✓

#### Test Scenario: Validate Undead Monster (e.g., Lich)
- **GIVEN** a lich or other undead monster file from `src/packs/monsters/Undead_Awroz7YqtpURNlF5`
- **WHEN** the validation script runs
- **THEN** it SHALL pass all validation rules:
  - Actor `type` is `"npc"` ✓
  - Monster keywords include `"undead"` ✓
  - Monster `system.monster.role` is valid ✓

#### Test Scenario: Validate Swarm Monster
- **GIVEN** a swarm monster file from `src/packs/monsters`
- **WHEN** the validation script runs
- **THEN** it SHALL pass all validation rules:
  - Actor `type` is `"npc"` ✓
  - Monster keywords include `"swarm"` ✓
  - `system.combat.size.value` reflects swarm size ✓

#### Test Scenario: Validate Elemental Monster
- **GIVEN** an elemental monster file from `src/packs/monsters/Elementals_hatSTUdV3EGvlnvE`
- **WHEN** the validation script runs
- **THEN** it SHALL pass all validation rules:
  - Actor `type` is `"npc"` ✓
  - Monster keywords include `"elemental"` ✓
  - All `_id` fields are exactly 16 characters ✓

### Requirement: Self-Validation Checklist
The skill SHALL include a self-validation checklist that the LLM completes BEFORE outputting Foundry JSON.

#### Scenario: Pre-generation validation
- **WHEN** the skill generates JSON with `--format foundry` or `--format both`
- **THEN** the LLM SHALL verify:
  - Actor `type` is `"npc"`
  - All `_id` fields are exactly 16 characters (alphanumeric only)
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

### Requirement: Mandatory Validation Script Execution
The skill SHALL run the validation script `scripts/validate_foundry_json.py` on all generated Foundry JSON files BEFORE completing the task.

#### Scenario: Run validation script after generation
- **WHEN** the skill generates JSON with `--format foundry` or `--format both`
- **THEN** the skill SHALL execute: `python scripts/validate_foundry_json.py <output_file>`
- **AND** the skill SHALL NOT report success until validation passes
- **AND** the skill SHALL fix any validation errors and re-run validation

#### Scenario: Validation script execution required
- **GIVEN** a request for `--format foundry` or `--format both`
- **WHEN** the skill generates output
- **THEN** it SHALL run the validation script as a mandatory step
- **AND** it SHALL include the validation output in the response
- **AND** it SHALL report any errors or warnings found
- **AND** it SHALL fix errors and re-validate until passing

#### Scenario: Validation failure handling
- **WHEN** the validation script reports errors
- **THEN** the skill SHALL identify the specific errors from the validation output
- **AND** the skill SHALL correct the JSON to fix all errors
- **AND** the skill SHALL re-run validation after corrections
- **AND** the skill SHALL repeat until validation passes with no errors

#### Example validation workflow
```
1. Working directory: ds-monster-generator project root
2. Generate JSON file: output/fungal-morlock-ambusher.json
3. Run validation: python scripts/validate_foundry_json.py output/fungal-morlock-ambusher.json
4. Review output:
   - If errors: Fix JSON, go to step 3
   - If warnings only: Acceptable for official content, proceed
   - If passed: Validation complete
5. Report validation status to user
```

