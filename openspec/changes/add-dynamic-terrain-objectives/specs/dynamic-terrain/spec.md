## ADDED Requirements

### Requirement: DTO Mechanics and Outcomes

The system SHALL generate DTOs using Draw Steel's unique mechanics for applying conditions and resolving outcomes, NOT the saving throw system used in other game systems.

#### Scenario: Use Potency Checks Instead of Saves

**WHEN** a DTO applies a condition (slowed, prone, grabbed, etc.)

**THEN** the condition SHALL be applied via potency checks, NOT saves:
- **CORRECT:** "M < 1 slowed (save ends)" or "A < 2 prone"
- **INCORRECT:** "Target makes a Dexterity save or become slowed"
- **INCORRECT:** "DC 15 Constitution save or take poison damage"

**Potency check format:** `[Characteristic] < [Value] [condition]`
- M = Might, A = Agility, R = Reason, I = Intuition, P = Presence
- Value = potency threshold (typically -1, 0, 1, 2, 3 based on tier)
- Condition = the condition applied (may include "(save ends)" for ongoing effects)

**Example:** "A < 1 slowed (save ends)" means "If the target's Agility is less than 1, they are slowed (save ends)"

#### Scenario: Active DTO Outcomes (Power Roll)

**WHEN** a DTO makes an active check (DTO rolls power roll)

**THEN** the DTO SHALL use a 3-tiered power roll outcome:
- **Tier 1 (≤11):** Weakest effect
- **Tier 2 (12-16):** Average effect
- **Tier 3 (17+):** Strongest effect

**Example power roll structure:**
```
Power Roll + 2:
- ≤11: 3 damage; push 1
- 12-16: 6 damage; push 2; M < 1 slowed (save ends)
- 17+: 9 damage; push 3; M < 2 restrained (save ends)
```

#### Scenario: Passive DTO Outcomes (Player Test)

**WHEN** a player makes a test against a DTO (deactivate, avoid, etc.)

**THEN** the DTO SHALL use a 3-tiered test outcome:
- **Tier 1 (≤11):** Worst outcome for player (triggered, damaged, etc.)
- **Tier 2 (12-16):** Average outcome (partial success, slowed, etc.)
- **Tier 3 (17+):** Best outcome (deactivated, avoided, etc.)

**Example test structure (deactivate):**
```
As a maneuver, a creature adjacent to a bear trap can make an Agility test.
- ≤11: The creature triggers the trap and is affected as if in its space.
- 12-16: The trap is deactivated but the creature is slowed (EoT).
- 17+: The trap is deactivated and doesn't trigger.
```

#### Scenario: Mixed Active and Passive Outcomes

**WHEN** a DTO has both active power rolls and player tests

**THEN** the DTO SHALL clearly distinguish between:
- **Active:** DTO power roll (e.g., "Power Roll + 2" in Effect section)
- **Passive:** Player test (e.g., "Agility test" in Deactivate section)

**Example:** Bear Trap has both:
- Passive: Player makes Agility test to deactivate
- Active: DTO makes power roll when triggered

#### Scenario: Include Save Ends for Ongoing Conditions

**WHEN** a DTO applies an ongoing condition

**THEN** the condition SHALL include "(save ends)" unless it's permanent:
- **CORRECT:** "M < 1 slowed (save ends)" or "M < 2 grabbed"
- **PERMANENT:** "M < 2 restrained" (no save ends = permanent until condition ends naturally)

**Note:** Some conditions like grabbed don't have "(save ends)" because they end when the target breaks free, not via save.

#### Scenario: Avoid D&D-Style Saving Throws

**WHEN** generating DTO effects

**THEN** the system SHALL NOT use:
- "DC X [ability] save"
- "On a failed save, [effect]"
- "Save vs. [condition]"
- "Make a Constitution/Dexterity/Wisdom save"

**INSTEAD use:**
- Power roll tiers (≤11, 12-16, 17+)
- Potency checks (M/A/R/I/P < value)
- Player test tiers (≤11, 12-16, 17+)

#### Scenario: Apply Potency Based on DTO Tier

**WHEN** a DTO's power roll applies conditions with potency checks

**THEN** potency values SHALL scale with tier outcomes:
- **Tier 1 (≤11):** Potency = Characteristic - 2 (e.g., M < 0 for +2 Might)
- **Tier 2 (12-16):** Potency = Characteristic - 1 (e.g., M < 1 for +2 Might)
- **Tier 3 (17+):** Potency = Characteristic (e.g., M < 2 for +2 Might)

**Example DTO with +2 Might:**
```
Power Roll + 2:
- ≤11: 5 damage; M < 0 slowed (save ends)
- 12-16: 8 damage; M < 1 slowed (save ends)
- 17+: 11 damage; M < 2 slowed (save ends)
```

#### Scenario: Potency Check Evaluation

**WHEN** evaluating a potency check like "A < 1 prone"

**THEN** the condition applies if:
- Target's Agility score is LESS THAN the potency value (1)
- Target with Agility 0 or negative: becomes prone
- Target with Agility 1 or higher: resists, no condition applied

**Key difference from saves:**
- **Saves:** Target rolls to avoid effect (active resistance)
- **Potency:** Target's characteristic is compared to threshold (passive resistance)

#### Scenario: Distinguish Three Draw Steel Mechanics

**WHEN** converting or generating DTOs from other game systems

**THEN** the system SHALL use the correct Draw Steel mechanic based on purpose:

| Original D&D Concept | Draw Steel Conversion | Purpose/Use Case |
|---------------------|----------------------|------------------|
| **DC vs. Saving Throw** (to apply a condition) | **Potency** (Option A) | Used in DTO abilities (strikes/areas) to apply standard conditions based on target's characteristic score compared to potency value |
| **DC vs. Characteristic/Skill Check** (to interact/resist) | **Characteristic Test** (Option B) | Used for utilities, deactivating DTOs, resisting environment effects, or when actively challenging the effect |
| **Saving Throw** (to end a persistent effect) | **Saving Throw (d10 roll)** | Used ONLY to end an existing effect or condition marked as `(save ends)` (roll 6+ on d10) |

**Examples in DTOs:**
- **Option A (Potency):** "M < 2 slowed (save ends)" in DTO's power roll effect
- **Option B (Characteristic Test):** "Agility test to deactivate" in DTO's Deactivate section
- **Option C (Saving Throw):** The "save ends" in Option A requires a d10 roll to end the slowed condition

#### Scenario: Use Characteristic Tests for DTO Deactivation

**WHEN** a DTO has a Deactivate section

**THEN** the deactivation SHALL use characteristic tests (Option B), not saves:
- **CORRECT:** "As a maneuver, a creature adjacent to a dart trap can make an Agility test."
- **INCORRECT:** "DC 15 Dexterity save to deactivate the trap."

**Test outcomes use 3 tiers:**
- **≤11:** Worst outcome (triggered, damaged, failed to deactivate)
- **12-16:** Partial success (deactivated but slowed, etc.)
- **17+:** Best outcome (deactivated safely, no penalties)

**Examples from published DTOs:**
- **Bear Trap:** "Agility test - ≤11: triggers trap; 12-16: deactivated but slowed (EoT); 17+: deactivated safely"
- **Flammable Oil:** "Agility test - ≤11: ignites oil; 12-16: takes 3 fire damage and burning (save ends); 17+: rendered safe"
- **Hidey-Hole:** "Might test - ≤11: restrained (save ends); 12-16: collapses but slowed (save ends); 17+: collapsed, can't be used"
- **Dart Trap:** "Agility test - ≤11: triggers trap; 12-16: deactivated but slowed (EoT); 17+: deactivated safely"

**Note:** Some DTOs have no deactivation test (e.g., "can't be deactivated", "must be completely destroyed"). These are valid alternatives.

#### Scenario: Use Various Characteristics for Tests

**WHEN** generating DTO characteristic tests

**THEN** the system SHALL use the appropriate characteristic based on the task:

**Characteristic usage in published DTOs:**
- **Agility tests:** Most common for deactivating traps and mechanisms (Bear Trap, Dart Trap, Flammable Oil, Snare Trap, Spike Trap, Pressure Plate, Pulley, Ram, Switch, Arrow Launcher, Boiling Oil Cauldron, Catapult, Exploding Mill Wheel, Field Ballista, Iron Dragon)
- **Might tests:** Physical strength tasks (Hidey-Hole collapse, Pavise Shield control)
- **Reason tests:** Intellectual or magical tasks (Black Obelisk deactivation, Exploding Mill Wheel piloting)
- **Intuition tests:** Perception and awareness (Column of Blades Allied Awareness, Hidey-Hole network discovery)
- **Presence tests:** Social or supernatural tasks (Throne of A'An deactivation)

**Guideline:** Choose the characteristic that best fits the task:
- Agility = dexterity, nimbleness, traps
- Might = strength, physical force
- Reason = intellect, logic, magic
- Intuition = perception, awareness
- Presence = personality, willpower, supernatural

#### Scenario: Use Saving Throws Only for "Save Ends"

**WHEN** a DTO applies a condition with "(save ends)"

**THEN** the save ends mechanism refers to a d10 roll to end the condition:
- **Mechanic:** Target rolls d10 at start of their turn
- **Success:** 6+ on d10 = condition ends
- **Failure:** 1-5 on d10 = condition persists

**Examples:**
- "M < 1 slowed (save ends)" = slowed condition can be ended with d10 roll
- "M < 2 grabbed" = grabbed condition has NO save ends (must break free)

**IMPORTANT:** This d10 saving throw is ONLY for ending existing conditions, NOT for avoiding effects initially.

#### Scenario: DTOs Without Power Rolls

**WHEN** a DTO's effect doesn't use a power roll

**THEN** the DTO SHALL use simple damage or effect descriptions:

**Examples from published DTOs:**
- **Angry Beehive:** No power roll - "Any creature who starts their turn in the swarm's space takes 3 poison damage"
- **Brambles:** No power roll - "A creature takes 1 damage per square of brambles they enter"
- **Corrosive Pool:** No power roll for main effect - "Takes 3 acid damage if they start their turn in the pool, and takes 3 acid damage for each square of the pool they enter"
- **Flammable Oil:** No power roll - "Takes 3 fire damage and is burning (save ends)"
- **Psionic Pulse:** No power roll - "Each ally in the encounter is dazed until the end of their next turn"

**When to use power rolls vs. simple effects:**
- **Use power roll:** When effects have tiered outcomes (damage + conditions, force movement, etc.)
- **Use simple effects:** When effects are flat damage or straightforward conditions without tiers

### Requirement: Dynamic Terrain Objectives Generation

The system SHALL provide the capability to generate Draw Steel Dynamic Terrain Objectives (DTOs) including Environmental Hazards, Fieldworks, Mechanisms, Siege Engines, Power Fixtures, and Supernatural Objects.

#### Scenario: Generate Environmental Hazard

**WHEN** a user requests "Create a Level 2 Environmental Hazard [Name]" or "Create a Level 2 Hazard Hexer [Name]"

**THEN** the system SHALL generate a DTO stat block with:
- EV value appropriate for level 2 hazard (typically 2-4 EV)
- Stamina value (fixed or per-square)
- Size (standard size or squares of terrain)
- Deactivate section (if applicable)
- Activate section with trigger condition
- Effect section with power roll or ability
- Optional Upgrades with EV costs

#### Scenario: Generate Fieldwork

**WHEN** a user requests "Create a Level 1 Fieldwork [Name]" or "Create a Level 1 Fortification Defender [Name]"

**THEN** the system SHALL generate a DTO stat block with:
- EV value appropriate for level 1 fieldwork (typically 1-3 EV)
- Stamina value (often per-square for larger objects)
- Size (standard or squares of terrain)
- Direction field (if applicable, e.g., archer's stakes)
- Deactivate section
- Activate section with trigger condition
- Effect section
- Optional Upgrades with EV costs
- Optional Allied Awareness section

#### Scenario: Generate Mechanism

**WHEN** a user requests "Create a Level 3 Mechanism [Name]" or "Create a Level 3 Fortification Defender [Name]"

**THEN** the system SHALL generate a DTO stat block with:
- EV value appropriate for level 3 mechanism (typically 3-4 EV)
- Stamina value
- Size (standard or squares)
- Direction field (if applicable)
- Deactivate section
- Activate section with trigger condition
- Effect section with power roll
- Optional Upgrades with EV costs
- Optional Allied Awareness section

#### Scenario: Generate Siege Engine

**WHEN** a user requests "Create a Level 3 Siege Engine [Name]" or "Create a Level 3 Siege Engine Artillery [Name]"

**THEN** the system SHALL generate a DTO stat block with:
- EV value appropriate for level 3 siege engine (typically 8-12 EV)
- Stamina value (typically 30-60 for level 2-4)
- Size (standard: 1L, 2, or 3)
- Deactivate section
- Main action abilities (e.g., Arrow Storm, Boiling Oil)
- Reload, Spot, and Move actions (if applicable)
- Upgrades with EV costs

#### Scenario: Generate Power Fixture

**WHEN** a user requests "Create a Level 5 Power Fixture [Name]" or "Create a Level 5 Relic Support [Name]"

**THEN** the system SHALL generate a DTO stat block with:
- EV value appropriate for level 5 power fixture (typically 7-14 EV)
- Stamina value (typically 35-60)
- Size (standard: 2 or 3)
- Deactivate section
- Special abilities (e.g., Empowered Will, Psionic Barrier)
- Triggered abilities (if applicable)

#### Scenario: Generate Supernatural Object

**WHEN** a user requests "Create a Level 3 Supernatural Object [Name]" or "Create a Level 3 Relic Controller [Name]"

**THEN** the system SHALL generate a DTO stat block with:
- EV value appropriate for level 3 supernatural object (typically 20 EV)
- Stamina value (typically 80-140)
- Size (standard: 1M or 2)
- Deactivate section (often with special requirements)
- Activate section with trigger condition
- Effect section with power roll
- Special abilities (e.g., Dimensional Flicker, Light of the Northern Sun)

### Requirement: DTO EV Estimation

The system SHALL estimate Encounter Value (EV) for DTOs based on category, level, and complexity, using patterns derived from published examples.

#### Scenario: Calculate EV for Environmental Hazard

**WHEN** generating an Environmental Hazard at level 1-3

**THEN** EV SHALL be calculated as:
- Level 1 hazard: 1 EV (e.g., Brambles: 1 EV, Frozen Pond: 1 EV)
- Level 2 hazard: 2-3 EV (e.g., Angry Beehive: 2 EV, Corrosive Pool: 3 EV, Toxic Plants: 2 EV)
- Level 3 hazard: 3-4 EV (e.g., Lava: 4 EV, Quicksand: 3 EV)
- Per-square hazards: EV × 1 per 10×10 area

#### Scenario: Calculate EV for Fieldwork

**WHEN** generating a Fieldwork at level 1-2

**THEN** EV SHALL be calculated as:
- Level 1 fieldwork: 1-2 EV (e.g., Archer's Stakes: 2 EV, Bear Trap: 2 EV, Hidey-Hole: 1 EV, Pavise Shield: 1 EV)
- Level 2 fieldwork: 3 EV (e.g., Spike Trap: 3 EV, Pillar: 3 EV, Ram: 3 EV)
- Note: Dart Trap is Level 1 Trap (1 EV) with upgrades up to +4 EV for total 5 EV
- Complex traps with upgrades: base EV + upgrade EV costs

#### Scenario: Calculate EV for Mechanism

**WHEN** generating a Mechanism at level 1-3

**THEN** EV SHALL be calculated as:
- Level 1 mechanism: 1-2 EV (e.g., Dart Trap: 1 EV, Switch: 1 EV, Pressure Plate: 2 EV, Pulley: 1 EV)
- Level 2 mechanism: 3 EV (e.g., Pillar: 3 EV, Ram: 3 EV)
- Level 3 mechanism: 3-4 EV (e.g., Column of Blades: 3 EV, Portcullis: 4 EV)
- Complex mechanisms with upgrades: base EV + upgrade EV costs (e.g., Column of Blades can be +5 EV with upgrades)

#### Scenario: Calculate EV for Siege Engine

**WHEN** generating a Siege Engine at level 2-4

**THEN** EV SHALL be calculated as:
- Level 2 siege engine: 8 EV (e.g., Arrow Launcher: 8 EV, Field Ballista: 8 EV)
- Level 3 siege engine: 10 EV (e.g., Catapult: 10 EV, Boiling Oil Cauldron: 10 EV, Exploding Mill Wheel: 10 EV)
- Level 4 siege engine: 12 EV (e.g., Iron Dragon: 12 EV)
- Watchtower: 8 EV (special case, level 2 fortification)

#### Scenario: Calculate EV for Power Fixture

**WHEN** generating a Power Fixture at level 5

**THEN** EV SHALL be calculated as:
- Level 5 power fixture: 7-14 EV (e.g., Holy Idol: 7 EV, Psionic Shard: 7 EV, Tree of Might: 14 EV)
- Higher EV for more powerful effects (e.g., Tree of Might has ongoing damage and buffs)

#### Scenario: Calculate EV for Supernatural Object

**WHEN** generating a Supernatural Object at level 3-4

**THEN** EV SHALL be calculated as:
- Level 3 supernatural object: 20 EV (e.g., Black Obelisk: 20 EV, Chronal Hypercube: 20 EV)
- Level 4 supernatural object: 24 EV (e.g., Throne of A'An: 24 EV)
- Higher EV reflects unique, powerful, and complex abilities

### Requirement: DTO Stamina Calculation

The system SHALL calculate Stamina for DTOs based on category, level, and size, using patterns derived from published examples.

#### Scenario: Calculate Stamina for Environmental Hazard

**WHEN** generating an Environmental Hazard

**THEN** Stamina SHALL be calculated as:
- Small hazards: 3-12 Stamina (e.g., Angry Beehive: 3, Brambles: 3 per square)
- Medium hazards: 3-12 Stamina (e.g., Corrosive Pool: 12 per square, Frozen Pond: 3 per square)
- Large hazards: 12 Stamina per square (e.g., Lava: 12 per square)
- Some hazards have no Stamina (e.g., Quicksand: -)

#### Scenario: Calculate Stamina for Fieldwork

**WHEN** generating a Fieldwork

**THEN** Stamina SHALL be calculated as:
- Traps: 1-9 Stamina (e.g., Bear Trap: 6, Snare Trap: 1, Spike Trap: 6)
- Fortifications: 3-9 Stamina per square (e.g., Archer's Stakes: 3 per square, Pavise Shield: 9)
- Some fieldworks have no Stamina (e.g., Hidey-Hole: -, Flammable Oil: -)

#### Scenario: Calculate Stamina for Mechanism

**WHEN** generating a Mechanism

**THEN** Stamina SHALL be calculated as:
- Small mechanisms: 3-6 Stamina (e.g., Dart Trap: 3, Switch: 3)
- Medium mechanisms: 5-9 Stamina (e.g., Column of Blades: 5, Pillar: 6)
- Large mechanisms: 3-9 Stamina per square (e.g., Portcullis: 9 per square, Ram: 3 per square)
- Some mechanisms have no Stamina (e.g., Pressure Plate: -)

#### Scenario: Calculate Stamina for Siege Engine

**WHEN** generating a Siege Engine

**THEN** Stamina SHALL be calculated as:
- Level 2 siege engines: 30-50 Stamina (e.g., Arrow Launcher: 30, Field Ballista: 40, Watchtower: 50)
- Level 3 siege engines: 25-60 Stamina (e.g., Exploding Mill Wheel: 25, Catapult: 50, Boiling Oil Cauldron: 50)
- Level 4 siege engines: 60 Stamina (e.g., Iron Dragon: 60)

#### Scenario: Calculate Stamina for Power Fixture

**WHEN** generating a Power Fixture

**THEN** Stamina SHALL be calculated as:
- Level 5 power fixtures: 35-60 Stamina (e.g., Holy Idol: 35, Psionic Shard: 40, Tree of Might: 60)
- Higher Stamina for more durable objects

#### Scenario: Calculate Stamina for Supernatural Object

**WHEN** generating a Supernatural Object

**THEN** Stamina SHALL be calculated as:
- Level 3 supernatural objects: 80-100 Stamina (e.g., Chronal Hypercube: 80, Black Obelisk: 100)
- Level 4 supernatural objects: 140 Stamina (e.g., Throne of A'An: 140)
- Higher Stamina reflects powerful magical construction

### Requirement: DTO Power Roll Damage

The system SHALL generate power roll damage values for DTOs that match published patterns by level and tier.

#### Scenario: Calculate Damage for Level 1 DTO

**WHEN** generating a Level 1 DTO with power roll

**THEN** damage SHALL be:
- Tier 1 (≤11): 1-4 damage (e.g., Dart Trap: 2, Bear Trap: 1-3, Spike Trap: 3)
- Tier 2 (12-16): 3-5 damage (e.g., Dart Trap: 4, Bear Trap: 3, Spike Trap: 4)
- Tier 3 (17+): 5-6 damage (e.g., Dart Trap: 5, Bear Trap: 5, Spike Trap: 6)
- Note: Some Level 1 DTOs have no damage (force movement only, conditions only)

#### Scenario: Calculate Damage for Level 2 DTO

**WHEN** generating a Level 2 DTO with power roll

**THEN** damage SHALL be:
- Tier 1 (≤11): 3-4 damage (e.g., Arrow Launcher: 5, Field Ballista: 5, Pillar: 4)
- Tier 2 (12-16): 6-9 damage (e.g., Arrow Launcher: 8, Field Ballista: 8, Pillar: 6)
- Tier 3 (17+): 9-11 damage (e.g., Arrow Launcher: 11, Field Ballista: 11, Pillar: 9)
- Note: Some Level 2 DTOs have higher damage (e.g., Corrosive Pool Explosive Reaction: 3-9 fire damage)

#### Scenario: Calculate Damage for Level 3 DTO

**WHEN** generating a Level 3 DTO with power roll

**THEN** damage SHALL be:
- Tier 1 (≤11): 3-5 damage (e.g., Lava: 5, Column of Blades: 4, Portcullis: 3)
- Tier 2 (12-16): 6-9 damage (e.g., Lava: 9, Column of Blades: 6, Portcullis: 7)
- Tier 3 (17+): 9-12 damage (e.g., Lava: 12, Column of Blades: 9, Portcullis: 10)
- Siege engines at this level: Catapult 5/9/12, Boiling Oil Cauldron 5/9/12, Exploding Mill Wheel 5/9/12

#### Scenario: Calculate Damage for Level 4 DTO

**WHEN** generating a Level 4 DTO with power roll

**THEN** damage SHALL be:
- Tier 1 (≤11): 6 damage (e.g., Iron Dragon: 6 fire damage)
- Tier 2 (12-16): 10 damage (e.g., Iron Dragon: 10 fire damage)
- Tier 3 (17+): 13 damage (e.g., Iron Dragon: 13 fire damage)
- Note: Level 4 supernatural objects (Throne of A'An) use 6/11/14 damage pattern

#### Scenario: Calculate Damage for Level 5 DTO

**WHEN** generating a Level 5 DTO with power roll

**THEN** damage SHALL be:
- Tier 1 (≤11): 6 damage (e.g., Throne of A'An Primordial Flare: 6 fire damage)
- Tier 2 (12-16): 11 damage (e.g., Throne of A'An Primordial Flare: 11 fire damage)
- Tier 3 (17+): 14 damage (e.g., Throne of A'An Primordial Flare: 14 fire damage, Nova: 14 fire damage)
- Note: Some Level 5 DTOs have no damage (Tree of Might deals 10 corruption damage via special ability, not power roll)

### Requirement: DTO Stat Block Format

The system SHALL generate DTO stat blocks in the official Draw Steel format with all required sections.

#### Scenario: Generate Complete DTO Stat Block

**WHEN** generating any DTO

**THEN** the stat block SHALL include:
- Name and level/category/role
- EV value
- Stamina value
- Size value
- Optional fields: Immunity, Direction, Typical Space, Link
- Deactivate section (if applicable)
- Activate section (if applicable)
- Effect section with power roll or ability description
- Optional Upgrades section with EV costs
- Optional Allied Awareness section
- Optional Hidden trait

#### Scenario: Format Power Roll Section

**WHEN** a DTO has a power roll

**THEN** the power roll section SHALL include:
- Ability keywords (e.g., Melee, Strike, Weapon; Area, Magic)
- Distance (e.g., Melee 1, Ranged 5, 3 burst, 5 cube within 20)
- Target (e.g., One creature, Each creature in the area)
- Power Roll formula (typically +2 modifier)
- Tier outcomes with damage and effects
- Potency checks (e.g., M < 1 slowed, A < 2 prone)
- Effect description

#### Scenario: Format Upgrades Section

**WHEN** a DTO has upgrades

**THEN** each upgrade SHALL include:
- Upgrade name
- EV cost (e.g., +1 EV, +2 EV, +4 EV)
- Description of upgrade effects
- If upgrades replace abilities, indicate replacement clearly

### Requirement: DTO Type Guidance

The system SHALL provide guidance for generating different DTO types with appropriate themes and mechanics.

#### Scenario: Generate Environmental Hazard

**WHEN** generating an Environmental Hazard

**THEN** the DTO SHALL:
- Represent natural elements (fire, ice, poison, etc.)
- Have themes like: "angry beehive", "corrosive pool", "frozen pond", "lava", "quicksand", "toxic plants"
- Often be difficult terrain
- Activate when creatures enter or start turn in area
- Deal damage or apply conditions based on power roll

#### Scenario: Generate Fieldwork

**WHEN** generating a Fieldwork

**THEN** the DTO SHALL:
- Represent military fortifications or traps
- Have themes like: "archer's stakes", "bear trap", "snare trap", "spike trap", "pavise shield"
- Often be calibrate to trigger on specific creature sizes
- Include Allied Awareness for defenders
- Have upgrades for poison, concealment, etc.

#### Scenario: Generate Mechanism

**WHEN** generating a Mechanism

**THEN** the DTO SHALL:
- Represent intricate devices linked to triggers
- Have themes like: "column of blades", "dart trap", "pillar", "portcullis", "pressure plate", "ram"
- Often be linked to switches or pressure plates
- Have upgrades for materials (stone, metal) or concealment
- Include Allied Awareness for allies familiar with the mechanism

#### Scenario: Generate Siege Engine

**WHEN** generating a Siege Engine

**THEN** the DTO SHALL:
- Represent large weapons requiring creatures to operate
- Have themes like: "arrow launcher", "boiling oil cauldron", "catapult", "field ballista", "iron dragon"
- Require adjacent creatures to use main actions to activate
- Have Reload, Spot, and Move actions
- Have upgrades for ammunition, materials, or special capabilities

#### Scenario: Generate Power Fixture

**WHEN** generating a Power Fixture

**THEN** the DTO SHALL:
- Represent powerful fortifications for solo creatures
- Have themes like: "holy idol", "psionic shard", "tree of might"
- Provide ongoing benefits or effects at start of round
- Have high Stamina and EV
- Have unique, powerful abilities

#### Scenario: Generate Supernatural Object

**WHEN** generating a Supernatural Object

**THEN** the DTO SHALL:
- Represent magical or psionic objects
- Have themes like: "black obelisk", "chronal hypercube", "throne of A'An"
- Have effects that target enemies and allies
- Have very high EV (20+)
- Have unique, complex abilities
- Often require special conditions to deactivate