# draw-steel-monster-generator Specification

## Purpose
TBD - created by archiving change add-force-movement-status-rules. Update Purpose after archive.
## Requirements
### Requirement: Level-Scaled Force Movement
The generator SHALL provide force movement values (push, pull, slide) that scale with monster level and echelon.

#### Scenario: Level 1 monster uses pull
- **WHEN** creating a Level 1 (Echelon 0) monster with a pull effect
- **THEN** the pull values SHALL be 1/2/2 for T1/T2/T3
- **AND** the format SHALL be "pull [N]"

#### Scenario: Level 5 monster uses pull
- **WHEN** creating a Level 5 (Echelon 2) monster with a pull effect
- **THEN** the pull values SHALL be 3/4/5 for T1/T2/T3
- **AND** the format SHALL be "pull [N]"

#### Scenario: Level 9 monster uses slide
- **WHEN** creating a Level 9 (Echelon 3) monster with a slide effect
- **THEN** the slide values SHALL be 4/5/6 for T1/T2/T3
- **AND** the format SHALL be "slide [N]"

### Requirement: Role-Appropriate Force Movement Selection
The generator SHALL select force movement type based on monster role archetype.

#### Scenario: Harrier monster uses pull
- **WHEN** creating a Harrier monster with force movement
- **THEN** the generator SHALL prefer pull effects
- **AND** pull values SHALL follow level-scaled tables

#### Scenario: Brute monster uses push
- **WHEN** creating a Brute monster with force movement
- **THEN** the generator SHALL prefer push effects
- **AND** push values SHALL follow level-scaled tables

#### Scenario: Controller monster uses slide
- **WHEN** creating a Controller monster with force movement
- **THEN** the generator SHALL prefer slide effects
- **AND** slide values SHALL follow level-scaled tables

### Requirement: Condition Application Format
The generator SHALL apply conditions using the official Draw Steel format.

#### Scenario: Condition with potency and save ends
- **WHEN** an ability applies a condition that can be saved against
- **THEN** the format SHALL be "[potency], [condition] (save ends)"
- **EXAMPLE**: "M < 2, prone (save ends)", "A < 1, slowed (save ends)"

#### Scenario: Condition without potency
- **WHEN** an ability applies a condition without potency
- **THEN** the format SHALL be "[condition]"
- **EXAMPLE**: "prone", "grabbed"

#### Scenario: Multiple conditions at tier 3
- **WHEN** a tier 3 ability applies multiple conditions
- **THEN** the format SHALL list all conditions
- **EXAMPLE**: "prone and bleeding (save ends)"

### Requirement: Condition Persistence Rules
The generator SHALL understand that conditions are inherently persistent or conditional.

#### Scenario: Persistent conditions
- **WHEN** applying conditions like prone, slowed, weakened, dazed
- **THEN** these conditions are PERSISTENT by default
- **AND** they last until explicitly removed by an ability, maneuver, or save
- **EXAMPLES**: "prone" (ends by standing), "slowed" (ends by healing)

#### Scenario: Conditional conditions
- **WHEN** applying conditions like grabbed, frightened
- **THEN** these conditions are CONDITIONAL
- **AND** they end when the triggering condition is met
- **EXAMPLES**: "grabbed (until escape)" or adjacency breaks, "frightened" (ends when source changes)

#### Scenario: Damage-over-time conditions
- **WHEN** applying conditions like bleeding
- **THEN** these conditions cause ongoing effects
- **AND** they have no duration but trigger on action use
- **EXAMPLE**: "bleeding" (deals damage when target uses actions)

### Requirement: Tier-Based Effect Duration
The generator SHALL apply appropriate duration patterns based on tier.

#### Scenario: Tier 1 instant or brief effects
- **WHEN** a tier 1 ability applies a condition
- **THEN** the condition MAY be instant with no duration
- **OR** MAY have brief duration like "(EoT)" for minor effects

#### Scenario: Tier 2 persistent conditions
- **WHEN** a tier 2 ability applies a condition
- **THEN** the condition SHALL be "(save ends)" for persistent effects
- **AND** the target can save to end the condition

#### Scenario: Tier 3 enhanced conditions
- **WHEN** a tier 3 ability applies a condition
- **THEN** the condition SHALL be "(save ends)" or enhanced
- **AND** MAY include multiple conditions or additional effects

### Requirement: Official Condition Definitions
The generator SHALL use only official Draw Steel condition definitions.

#### Scenario: Applying prone condition
- **WHEN** a monster ability applies the prone condition
- **THEN** the condition follows the official definition: "While a creature is prone, they are flat on the ground, any strike they make takes a bane, and melee abilities used against them gain an edge."
- **AND** the format SHALL be "prone" or "prone (save ends)" if save-able

#### Scenario: Applying grabbed condition
- **WHEN** a monster ability applies the grabbed condition
- **THEN** the condition follows the official definition: "A creature who is grabbed has speed 0, can't be force moved except by the grabber, and takes a bane on abilities that don't target the grabber."
- **AND** the format SHALL be "grabbed" or "grabbed (until escape)"

#### Scenario: Applying bleeding condition
- **WHEN** a monster ability applies the bleeding condition
- **THEN** the condition follows the official definition: "While bleeding, whenever they use a main action, triggered action, or make a power roll using Might or Agility, they lose Stamina."
- **AND** the format SHALL be "bleeding" (no duration - persists until healed)

