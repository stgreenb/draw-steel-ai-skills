## ADDED Requirements

### Requirement: Strike Ability Keywords

Strike abilities MUST include the "weapon" keyword in addition to "melee" and "strike" keywords.

#### Scenario: Basic strike ability
- **WHEN** generating a signature strike ability
- **THEN** keywords array includes `["melee", "strike", "weapon"]`
- **AND** "weapon" keyword is present

#### Scenario: Charge strike ability
- **WHEN** generating a charge-based strike ability
- **THEN** keywords array includes `["charge", "melee", "strike", "weapon"]`
- **AND** includes both "charge" and "weapon" keywords

#### Scenario: Non-charge strike ability
- **WHEN** generating a regular strike without charge
- **THEN** keywords array includes `["melee", "strike", "weapon"]`
- **AND** does NOT include "charge" keyword

### Requirement: Target Type for Strike Abilities

Strike abilities targeting creatures MUST use "creatureObject" type instead of "creature" to match official Draw Steel patterns.

#### Scenario: Single target strike
- **WHEN** generating a strike ability targeting one creature
- **THEN** target.type MUST be "creatureObject"
- **AND** target.value MUST be 1

#### Scenario: Multi-target strike
- **WHEN** generating a strike ability targeting multiple creatures
- **THEN** target.type MUST be "creatureObject"
- **AND** target.value MUST equal the number of targets

### Requirement: Breath and Spew Ability Keywords

Breath weapon and projectile spew abilities MUST use area/magic keywords, not damage type keywords.

#### Scenario: Poison breath weapon
- **WHEN** generating a poison breath weapon ability
- **THEN** keywords array includes `["area", "magic"]`
- **AND** does NOT include "poison" keyword in keywords
- **AND** damage types are specified in power.effects, not keywords

#### Scenario: Acid spew ability
- **WHEN** generating an acid projectile spew ability
- **THEN** keywords array includes `["area", "magic"]` or `["ranged"]`
- **AND** does NOT include "acid" keyword in keywords
- **AND** damage types are specified in power.effects, not keywords

#### Scenario: Fire breath weapon
- **WHEN** generating a fire breath weapon ability
- **THEN** keywords array includes `["area", "magic"]`
- **AND** does NOT include "fire" keyword in keywords
- **AND** damage types are specified in power.effects, not keywords

### Requirement: Custom Field in Area Targets

Area abilities MUST include a "custom" field in the target object for clarity to match official Draw Steel patterns.

#### Scenario: Area burst with custom text
- **WHEN** generating an area burst ability
- **THEN** target.custom field MUST contain descriptive text like "Each enemy in the area"
- **AND** target.type MUST be "enemy" or "creatureObject"

#### Scenario: Cone-like area with custom text
- **WHEN** generating a cone-like area ability (using cube type)
- **THEN** target.custom field MUST contain descriptive text like "Each creature and object in the area"
- **AND** target.type MUST be "creatureObject"

### Requirement: Ability Type Variety

Skill documentation MUST include examples of different ability types beyond just "main" to encourage variety in generated monsters.

#### Scenario: Maneuver type example
- **WHEN** providing ability examples in documentation
- **THEN** includes at least one ability with type "maneuver"
- **AND** example shows appropriate keywords like `["area", "ranged"]`

#### Scenario: FreeTriggered type example
- **WHEN** providing ability examples in documentation
- **THEN** includes at least one ability with type "freeTriggered"
- **AND** example shows trigger field populated

#### Scenario: None type example
- **WHEN** providing ability examples for custom abilities
- **THEN** includes at least one ability with type "none"
- **AND** example shows special target type

### Requirement: Villain Action Guidance Enhancement

SKILL.md already contains villain action guidance. The existing guidance MUST be enhanced with the specific rules from Monster Basics.md about villain action usage.

#### Scenario: Existing villain action guidance
- **WHEN** reviewing current SKILL.md villain action guidance
- **THEN** guidance already exists at lines 1808-1917
- **AND** includes template structure with Villain Action 1, 2, 3
- **AND** specifies only Solo/Leader organizations get villain actions
- **AND** specifies Malice cost ranges (5-7 for level 1-3, 5-10 for level 4+)

#### Scenario: Add usage rules to existing guidance
- **WHEN** enhancing villain action guidance
- **THEN** adds rule: each villain action can be used only once per encounter
- **AND** adds rule: no more than one villain action per round
- **AND** adds rule: villain actions are used at end of any creature's turn
- **AND** adds rule: Villain Action 1 is opener, Action 2 is crowd control, Action 3 is ult
- **AND** keeps guidance concise to avoid bloating instructions

### Requirement: Examples as Inspiration

SKILL.md MUST include clear guidance that LLMs should use example abilities and features as inspiration, not copy them verbatim.

#### Scenario: Example abilities as inspiration
- **WHEN** generating abilities based on examples
- **THEN** LLM creates unique ability names appropriate to the creature
- **AND** LLM adapts mechanics to fit the creature's theme (not just copying)
- **AND** LLM varies damage types, conditions, and effects from examples

#### Scenario: Example features as inspiration
- **WHEN** generating features based on examples
- **THEN** LLM creates unique feature names like "Draconic Frenzy" or "Shadow Step"
- **AND** LLM does NOT copy "Brutal Effectiveness" verbatim unless it's specifically needed
- **AND** LLM considers the creature's theme when selecting features

#### Scenario: Creative adaptation
- **WHEN** a generated monster is similar to an example monster
- **THEN** LLM still creates unique abilities and features
- **AND** LLM may adapt patterns but changes names, damage types, and effects
- **AND** LLM ensures each generated monster is distinct from examples

## MODIFIED Requirements

### Requirement: Foundry VTT JSON Structure

The skill SHALL generate Foundry VTT JSON that matches the official Draw Steel system schema.

#### Scenario: Valid strike ability structure
- **WHEN** generating a strike ability
- **THEN** keywords include "weapon"
- **AND** target.type is "creatureObject"
- **AND** power.effects contains structured damage objects

#### Scenario: Valid breath weapon structure
- **WHEN** generating a breath weapon ability
- **THEN** keywords include `["area", "magic"]`
- **AND** target.custom field contains descriptive text
- **AND** damage types are in power.effects, not keywords

#### Scenario: Valid ability type variety
- **WHEN** generating multiple abilities for a monster
- **THEN** includes different ability types (main, maneuver, freeTriggered, none)
- **AND** each ability type has appropriate structure

## REMOVED Requirements

None

## RENAMED Requirements

None