# monster-generation Specification

## Purpose
TBD - created by archiving change add-cross-system-conversion. Update Purpose after archive.
## Requirements
### Requirement: Conversion Input Format
The generator SHALL accept cross-system monster conversion requests with flexible input.

#### Scenario: Basic conversion with optional source mention
- **WHEN** user provides input matching "Convert [Name] [options]"
- **OR** user provides input matching "Convert [Name] from [System] [options]"
- **THEN** the skill SHALL parse the conversion request
- **AND** extract creature name and any source system mentioned
- **AND** apply Draw Steel formulas to calculate all stats

#### Scenario: Conversion with pasted stat block
- **WHEN** user provides input matching "Convert [Name]: [pasted stat block content] [options]"
- **THEN** the skill SHALL parse the pasted content as source inspiration
- **AND** extract thematic elements (creature type, abilities, damage types, conditions)
- **AND** use these elements to inspire keyword and ability design
- **AND** apply Draw Steel formulas for all numerical stats

#### Scenario: Minimal conversion request
- **WHEN** user provides minimal input "Convert [Name] [options]"
- **THEN** the skill SHALL generate a Draw Steel monster with the given name
- **AND** use keywords and role to determine thematic elements
- **AND** apply Draw Steel formulas for all stats

### Requirement: Draw Steel Math Only
The generator SHALL use Draw Steel formulas exclusively for all calculations.

#### Scenario: Ignore source HP
- **WHEN** converting a monster with 150 HP from another system
- **THEN** the generator SHALL calculate Draw Steel Stamina using Draw Steel formulas
- **AND** SHALL NOT use 150 or any derivative of it

#### Scenario: Ignore source damage
- **WHEN** converting a monster that deals 8d6 fire damage in another system
- **THEN** the generator SHALL calculate Draw Steel damage using Draw Steel formulas
- **AND** SHALL NOT use 8d6 or calculate equivalent

#### Scenario: Ignore source attack bonus
- **WHEN** converting a monster with +7 to hit from another system
- **THEN** the generator SHALL calculate characteristics using Draw Steel echelon rules
- **AND** SHALL NOT use +7 or any derivative

#### Scenario: Use only creature name and options
- **WHEN** converting "Ancient Red Dragon" from D&D 5e
- **THEN** the generator SHALL use the creature name and any specified organization/role
- **AND** SHALL apply Draw Steel formulas for all numerical stats
- **AND** SHALL NOT use CR, HP, damage, or any numerical values from source

### Requirement: Inspiration-Based Design
The generator SHALL use source monsters for creative inspiration only.

#### Scenario: Extract thematic elements
- **WHEN** converting "Red Dragon" from D&D 5e
- **THEN** the generator SHALL use theme: "fire-breathing dragon"
- **AND** use keywords: "dragon", "fire"
- **AND** create fire-themed abilities

#### Scenario: Preserve creature identity
- **WHEN** converting "Lich" from another system
- **THEN** the generator SHALL preserve undead nature
- **AND** use "undead" keyword
- **AND** create abilities inspired by lich themes (magic, death, souls)

#### Scenario: Adapt ability concepts
- **WHEN** source monster has "Fire Breath" ability
- **THEN** the generator SHALL create an original ability inspired by fire breath
- **AND** use Draw Steel damage formulas for the ability
- **AND** NOT copy exact mechanics or damage amounts

### Requirement: Conversion Output
The generator SHALL produce standard Draw Steel output.

#### Scenario: Markdown conversion output
- **WHEN** converting a monster
- **THEN** output SHALL be a standard Draw Steel stat block
- **AND** include "Converted from [System]" in the source field

#### Scenario: Foundry VTT conversion output
- **WHEN** converting with `--format foundry`
- **THEN** output SHALL be standard Foundry VTT JSON
- **AND** include converted monster in appropriate organization structure

### Requirement: Strike Bonus for Strike Abilities
Monsters SHALL add their highest characteristic to damage when using abilities with the Strike keyword.

#### Scenario: Level 3 Brute uses strike ability
- **WHEN** creating a Level 3 Brute (Might +2) with a Strike ability at Tier 2
- **THEN** base damage = 8, strike bonus = +2, final damage = 10
- **AND** the format SHALL be "[Damage] [type]; M < [potency]"

#### Scenario: Level 5 Solo Dragon uses strike
- **WHEN** creating a Level 5 Solo Dragon (highest characteristic +4) with a Strike ability
- **THEN** strike bonus = +4 added to all strike damage
- **AND** Free Strike = Tier 1 damage + strike bonus

### Requirement: Echelon-Based Characteristic Scaling
A monster's highest characteristic and power roll bonus SHALL equal 1 + their echelon.

#### Scenario: Level 1 monster (Echelon 0)
- **WHEN** creating a Level 1 monster
- **THEN** highest characteristic = +1
- **AND** power roll bonus = +1

#### Scenario: Level 3 monster (Echelon 1)
- **WHEN** creating a Level 3 monster (Level 2-4 range)
- **THEN** highest characteristic = +2
- **AND** power roll bonus = +2

#### Scenario: Level 5 monster (Echelon 2)
- **WHEN** creating a Level 5 monster (Level 5-7 range)
- **THEN** highest characteristic = +3
- **AND** power roll bonus = +3

#### Scenario: Level 8 monster (Echelon 3)
- **WHEN** creating a Level 8 monster (Level 8-10 range)
- **THEN** highest characteristic = +4
- **AND** power roll bonus = +4

### Requirement: Leader/Solo Bonuses
Leader and Solo monsters SHALL receive +1 to highest characteristic and +1 to all potencies.

#### Scenario: Level 5 Solo Brute
- **WHEN** creating a Level 5 Solo Brute
- **THEN** base characteristic = +3 (1 + echelon 2)
- **AND** Solo bonus = +1
- **AND** final highest characteristic = +4 (max +5)

#### Scenario: Level 4 Leader Controller
- **WHEN** creating a Level 4 Leader Controller
- **THEN** base characteristic = +2 (1 + echelon 1)
- **AND** Leader bonus = +1
- **AND** final highest characteristic = +3

#### Scenario: Solo potency bonus
- **WHEN** creating a Solo monster with highest characteristic +4
- **THEN** Tier 3 potency = +4
- **AND** Tier 2 potency = +3
- **AND** Tier 1 potency = +2
- **AND** all potencies gain +1 bonus (max 6)

### Requirement: Official Potency Formula
Monsters SHALL use the official potency formula: Potency = Highest Characteristic - (3 - Tier).

#### Scenario: Characteristic +3 potency calculation
- **WHEN** monster has highest characteristic +3
- **THEN** Tier 3 potency = +3 (3 - 0)
- **AND** Tier 2 potency = +2 (3 - 1)
- **AND** Tier 1 potency = +1 (3 - 2)

#### Scenario: Characteristic +5 potency calculation
- **WHEN** monster has highest characteristic +5
- **THEN** Tier 3 potency = +5
- **AND** Tier 2 potency = +4
- **AND** Tier 1 potency = +3

#### Scenario: Writing potencies in stat blocks
- **WHEN** writing abilities for monster with Agility +2
- **THEN** Tier 1 format = "A < 0"
- **AND** Tier 2 format = "A < 1"
- **AND** Tier 3 format = "A < 2"

### Requirement: Target Count Rules
Monsters SHALL target a specific number of creatures based on organization.

#### Scenario: Normal organization targets
- **WHEN** creating Minion, Horde, or Platoon monster
- **THEN** normal targets = 1

#### Scenario: Elite/Leader/Solo targets
- **WHEN** creating Elite, Leader, or Solo monster
- **THEN** normal targets = 2

### Requirement: Target Damage Scaling
Damage SHALL scale based on number of targets relative to normal.

#### Scenario: One fewer target
- **WHEN** monster targets 0 creatures instead of normal 1
- **THEN** damage multiplier = 1.2x

#### Scenario: Normal targets
- **WHEN** monster targets normal number of creatures
- **THEN** damage multiplier = 1.0x

#### Scenario: One additional target
- **WHEN** monster targets +1 creature than normal
- **THEN** damage multiplier = 0.8x

#### Scenario: Two or more additional targets
- **WHEN** monster targets 2+ creatures than normal
- **THEN** damage multiplier = 0.5x

#### Scenario: Elite Controller targeting 2 creatures
- **WHEN** Elite Controller (normal 2) targets exactly 2 creatures
- **THEN** damage multiplier = 1.0x (no change)

### Requirement: Extra Stamina for Non-Minions
Non-minion monsters SHALL receive extra stamina based on level.

#### Scenario: Non-minion extra stamina
- **WHEN** creating non-minion monster at level L
- **THEN** extra stamina = ceil((3 × L) + 3)
- **EXAMPLE**: Level 5 = ceil(18) = 18 extra stamina

#### Scenario: Minion extra stamina
- **WHEN** creating Minion monster
- **THEN** no extra stamina formula applied

### Requirement: Villain Actions for Leaders/Solos
Leader and Solo monsters SHALL have access to Villain Actions (experimental feature).

#### Scenario: Villain Action types
- **WHEN** creating Leader or Solo monster
- **THEN** monster MAY have up to 3 Villain Actions
- **AND** Opener: Relocation, minor damage, summons, buffs, or debuffs
- **AND** Crowd Control: Debuffing, area management, regaining upper hand
- **AND** Ultimate: High-damage finisher, dramatic finish

#### Scenario: Villain Action usage
- **WHEN** using Villain Action
- **THEN** can be used at end of any creature's turn
- **AND** only once per encounter
- **AND** no more than one per round

#### Scenario: Villain Action template format
- **WHEN** documenting Villain Action
- **THEN** format SHALL include: Type, Trigger, Effect, Usage
- **AND** format SHALL use ☠️ icon prefix

### Requirement: Solo Turn Rules
Solo creatures SHALL take multiple turns per round.

#### Scenario: Standard Solo turns
- **WHEN** creating Standard Solo creature
- **THEN** creature takes 2 turns per round
- **AND** turns occur at start and middle, or middle and end

#### Scenario: Boss Solo turns
- **WHEN** creating Boss Solo creature
- **THEN** creature takes 3 turns per round
- **AND** turns occur at start, middle, and end

#### Scenario: Mini-Boss turns
- **WHEN** creating Mini-Boss creature
- **THEN** creature takes 2 turns per round
- **AND** turns occur at start and end

### Requirement: Minion "With Captain" Trait
Minions SHALL have bonuses when led by a captain.

#### Scenario: Minion With Captain damage bonus
- **WHEN** minion has "With Captain" trait for damage
- **THEN** format = "+1 bonus to damage"

#### Scenario: Minion With Captain speed bonus
- **WHEN** minion has "With Captain" trait for speed
- **THEN** format = "+2 speed"

#### Scenario: Minion With Captain in stat block
- **WHEN** minion has With Captain trait
- **THEN** it SHALL be listed in the stat block table
- **AND** format = "[+N bonus to type]<br/> With Captain"

### Requirement: Malice Features
All monsters SHALL have access to group-wide Malice features.

#### Scenario: Brutal Effectiveness feature
- **WHEN** monster spends 3 Malice
- **THEN** next ability's potency increased by 1

#### Scenario: Malicious Strike feature
- **WHEN** monster spends 5+ Malice
- **THEN** next strike deals extra damage equal to highest characteristic
- **AND** +1 damage per additional Malice spent (max 3x)

#### Scenario: Malice Features template
- **WHEN** documenting Malice Features
- **THEN** format SHALL include: Cost, Feature Name, Effect
- **AND** format SHALL use 💀 icon prefix

### Requirement: Basic Malice Features
The generator SHALL provide universal malice features available to all monster types.

#### Scenario: Brutal Effectiveness (3 Malice)
- **WHEN** generating malice features
- **THEN** include "Brutal Effectiveness" as a universal option
- **AND** it SHALL increase potency by 1 on the next ability with potency

#### Scenario: Malicious Strike (5+ Malice)
- **WHEN** generating malice features
- **THEN** include "Malicious Strike" as a universal option
- **AND** it SHALL deal extra damage equal to the monster's highest characteristic
- **AND** extra damage increases by 1 for each additional Malice spent (max 3× highest characteristic)
- **AND** note that this feature can't be used two rounds in a row

### Requirement: Malice Feature Icon Classification
The generator SHALL use icons to indicate malice feature type and scope.

#### Scenario: Trait features (⭐️)
- **WHEN** generating a trait malice feature
- **THEN** use the ⭐️ icon
- **AND** the feature SHALL be always in effect or self-targeted
- **AND** examples include team buffs, self-healing, or permanent bonuses

#### Scenario: Area features (🔳)
- **WHEN** generating a cube, line, or wall area malice feature
- **THEN** use the 🔳 icon
- **AND** specify the area dimensions (e.g., "4 cube within 10")

#### Scenario: Aura/Burst features (❇️)
- **WHEN** generating an aura or burst area malice feature
- **THEN** use the ❇️ icon
- **AND** the feature SHALL affect creatures within a radius

#### Scenario: Special features (🌀)
- **WHEN** generating a special malice feature with unique distance
- **THEN** use the 🌀 icon
- **AND** features MAY affect the entire encounter map

#### Scenario: Solo/Leader features (☠️)
- **WHEN** generating malice features for solo or leader monsters
- **THEN** use the ☠️ icon for villain actions
- **AND** villain actions have different trigger timing (end of other creature's turn)
- **AND** villain actions can be used only once per encounter
- **AND** no more than one villain action per round

### Requirement: Level-Based Malice Tiers
The generator SHALL assign malice features to appropriate level tiers.

#### Scenario: Level 1+ malice features
- **WHEN** generating a Level 1-3 monster
- **THEN** generate malice features with costs 3-7 Malice
- **AND** features SHALL include basic attacks, buffs, or minor environmental effects

#### Scenario: Level 4+ malice features
- **WHEN** generating a Level 4-6 monster
- **THEN** generate one new malice feature at Level 4+
- **AND** the monster SHALL have access to all Level 1+ malice features

#### Scenario: Level 7+ malice features
- **WHEN** generating a Level 7-9 monster
- **THEN** generate one new malice feature at Level 7+
- **AND** features MAY include encounter-wide effects
- **AND** the monster SHALL have access to all lower level malice features

#### Scenario: Level 10+ malice features
- **WHEN** generating a Level 10+ monster
- **THEN** generate one ultimate malice feature at Level 10+
- **AND** the monster SHALL have access to all malice features from all tiers

### Requirement: Triggered Action Malice Features
The generator SHALL support malice features that activate as triggered actions.

#### Scenario: Triggered action activation
- **WHEN** generating malice features that use triggered actions
- **THEN** describe activation as "At the start of [monster]'s turn or when an action's trigger occurs"
- **AND** specify the trigger condition clearly

#### Scenario: Reactive malice features
- **WHEN** generating reactive malice features
- **THEN** features MAY be activated when targeted by an ability
- **AND** features MAY swap targets or counter-attack

### Requirement: Prior Malice Features Pattern
The generator SHALL provide access to lower level malice features for higher level monsters.

#### Scenario: Prior feature access
- **WHEN** generating malice features for Level 4+ monsters
- **THEN** include "Prior Malice Features" as an option
- **AND** describe as "The [monster] activates a Malice feature available to [monster type] of level [X] or lower"

### Requirement: Villain Actions for Leaders and Solo Creatures
The generator SHALL create villain actions for leader and solo monsters as special abilities distinct from regular malice features.

#### Scenario: Villain action availability
- **WHEN** monster organization is "leader" or "solo"
- **THEN** generate exactly 3 villain actions
- **AND** villain actions CANNOT be used by other organization types

#### Scenario: Villain action usage limits
- **WHEN** describing villain actions
- **THEN** each villain action CAN be used only once per encounter
- **AND** no more than one villain action can be used per round
- **AND** this limit applies even if multiple villain action creatures are in the encounter

#### Scenario: Villain action trigger timing
- **WHEN** describing villain action activation
- **THEN** villain actions are used at the end of any other creature's turn during combat
- **AND** this differs from regular malice features which activate at the start of the monster's turn

#### Scenario: Villain action numbering
- **WHEN** generating villain actions
- **THEN** number actions as Villain Action 1, Villain Action 2, Villain Action 3
- **AND** actions are intended to be used in order but CAN be used in any order

#### Scenario: Villain Action 1 (Opener)
- **WHEN** generating Villain Action 1
- **THEN** the action SHALL be an "opener" that shows heroes they're not battling a typical creature
- **AND** options include: dealing damage, summoning lackeys, buffing the leader, debuffing heroes, or moving into advantageous position

#### Scenario: Villain Action 2 (Crowd Control)
- **WHEN** generating Villain Action 2
- **THEN** the action SHALL provide crowd control after heroes have had a chance to respond
- **AND** the action SHALL help the villain regain the upper hand
- **AND** the action SHALL be more powerful than Villain Action 1

#### Scenario: Villain Action 3 (Ultimate)
- **WHEN** generating Villain Action 3
- **THEN** the action SHALL be an "ultimate" or "showstopper"
- **AND** the action SHALL deal a devastating blow to the heroes
- **AND** the action is designed to be used before the end of the battle

#### Scenario: Villain action icon
- **WHEN** describing villain actions
- **THEN** use the ☠️ icon for all villain actions
- **AND** format as "☠️ **[Name] (Villain Action [X])" where X is 1, 2, or 3

### Requirement: Malice Feature Trigger
The generator SHALL ensure all malice features activate at the start of the monster's turn.

#### Scenario: Activation timing
- **WHEN** describing malice features
- **THEN** all features SHALL specify "At the start of any [monster name]'s turn, you can spend Malice to activate one of the following features:"
- **AND** features cannot be activated mid-turn

### Requirement: Malice Resource Configuration
The generator SHALL configure malice resource in NPC system.

#### Scenario: Malice features as feature items
- **WHEN** generating Foundry VTT JSON
- **THEN** malice features SHALL be items with `"type": "feature"`
- **AND** the feature description SHALL include malice cost and activation text

#### Scenario: Prior Malice Features feature
- **WHEN** generating Level 4+ monsters with malice features
- **THEN** include a feature named "Prior Malice Features"
- **AND** the feature SHALL have `_dsid: "prior-malice-features"`
- **AND** the description SHALL list available lower-level malice features
- **AND** features MAY use UUID references to compendium items: `@UUID[Compendium.draw-steel.monster-features.Item.{id}]{Feature Name}`

#### Scenario: Malice text in Markdown
- **WHEN** generating Markdown stat block
- **THEN** the output SHALL include a "Malice" section listing available abilities
- **AND** each malice ability SHALL show cost and effect

### Requirement: Villain Actions in Foundry VTT
The generator SHALL create villain actions as ability items with special type.

#### Scenario: Villain action item structure
- **WHEN** generating villain actions for Foundry VTT JSON
- **THEN** each villain action SHALL be an item with `"type": "ability"`
- **AND** the system SHALL have `"type": "villain"` and `"category": "villain"`
- **AND** villain actions SHALL NOT have a resource cost
- **AND** villain actions SHALL have `"trigger": ""` (empty string)

#### Scenario: Villain action names
- **WHEN** generating villain actions
- **THEN** name them as "Villain Action 1", "Villain Action 2", "Villain Action 3"
- **AND** include the villain action number in the name

#### Scenario: Villain action trigger timing
- **WHEN** describing villain action activation in Foundry JSON
- **THEN** the trigger field SHALL be empty
- **AND** the effect description SHALL indicate "Used at the end of any other creature's turn"
- **AND** each villain action CAN be used only once per encounter

### Requirement: Organization-Based Malice Selection
The generator SHALL select malice features based on organization.

#### Scenario: Solo organization
- **WHEN** monster organization is "solo"
- **THEN** generate 3 malice features
- **AND** features SHALL include Solo Action (5 Malice)
- **AND** include one 10-malice ultimate ability
- **AND** generate 3 villain actions with ☠️ icon

#### Scenario: Elite/Leader organization
- **WHEN** monster organization is "elite" or "leader"
- **THEN** generate 2 malice features
- **AND** include team-buff effects
- **AND** if organization is "leader", generate 3 villain actions with ☠️ icon

#### Scenario: Platoon organization
- **WHEN** monster organization is "platoon"
- **THEN** generate 2 malice features
- **AND** include ally-benefit effects

#### Scenario: Minion/Horde organization
- **WHEN** monster organization is "minion" or "horde"
- **THEN** generate 2 malice features
- **AND** features SHALL benefit the swarm/horde
- **AND** minions CANNOT use malice features individually (squad uses shared malice)

### Requirement: Monster Stat Calculation
The system SHALL provide deterministic formulas for calculating Draw Steel TTRPG monster statistics including Encounter Value (EV), Stamina, Free Strike bonus, and damage per tier.

#### Official Formulas (from Monster Basics.md)

**Encounter Value (EV):**
```
EV = ceil(((2 × Level) + 4) × Organization_Modifier)
```

**Stamina:**
```
Stamina = ceil(((10 × Level) + Role_Stamina_Modifier) × Organization_Modifier)
```

**Damage:**
```
Damage = ceil((4 + Level + Damage_Modifier) × Tier_Modifier)
```
For Horde and Minion monsters: `Damage = ceil(Damage ÷ 2)`

**Free Strike:**
```
Free Strike = ceil((4 + Level + Damage_Modifier) × 0.6)
```
For Horde and Minion: `Free Strike = ceil(ceil((4 + Level + Damage_Modifier) × 0.6) ÷ 2)`

**Extra Stamina (Non-Minions Only):**
```
Extra_Stamina = ceil((3 × Level) + 3)
```

#### Organization Modifiers (Official from Monster Basics.md)

| Organization | EV Modifier | Stamina Modifier | Damage Modifier | Notes |
|--------------|-------------|------------------|-----------------|-------|
| Minion (stamina only) | 0.5 | 0.125 | ÷2 | EV uses 0.5 |
| Minion | 0.5 | 0.5 | ÷2 | Standard minion |
| Horde | 0.5 | 0.5 | ÷2 | Divide damage by 2 |
| Platoon | 1.0 | 1.0 | 1.0 | No change |
| Elite | 2.0 | 2.0 | 2.0 | Double multipliers |
| Leader | 2.0 | 2.0 | 2.0 | Double multipliers |
| Solo (stamina only) | 6.0 | 5.0 | 6.0 | EV uses 6.0 |
| Solo | 6.0 | 6.0 | 6.0 | Full solo stats |

#### Role Modifiers (Official from Monster Basics.md)

| Role | Stamina Modifier | Damage Modifier |
|------|------------------|-----------------|
| Ambusher | +20 | +1 |
| Artillery | +10 | +1 |
| Brute | +30 | +1 |
| Controller | +10 | +0 |
| Defender | +30 | +0 |
| Harrier | +20 | +0 |
| Hexer | +10 | +0 |
| Mount | +20 | +0 |
| Support | +20 | +0 |
| Elite* | +0 | +1 (stacks) |
| Leader | +30 | +1 |
| Solo | +30 | +2 |

*Elite can be used with a role that has +1 damage modifier, for total +2.

#### Tier Multipliers (Official from Monster Basics.md)

| Tier | Roll Range | Multiplier |
|------|------------|------------|
| Tier 1 | ≤11 | 0.6 |
| Tier 2 | 12-16 | 1.1 |
| Tier 3 | 17+ | 1.4 |

#### Scenario: Calculate EV for Level 3 Platoon Harrier
- **WHEN** user requests monster with level=3, organization="Platoon", role="Harrier"
- **THEN** EV = ceil(((2 × 3) + 4) × 1.0) = ceil(10) = 10

#### Scenario: Calculate Stamina for Level 5 Solo Brute
- **WHEN** user requests monster with level=5, organization="Solo", role="Brute"
- **THEN** Stamina = ceil(((10 × 5) + 30) × 6.0) = ceil(80 × 6) = 480

#### Scenario: Calculate Free Strike for Level 7 Harrier
- **WHEN** user requests monster with level=7, role="Harrier", organization="Platoon"
- **THEN** Free Strike = ceil((4 + 7 + 0) × 0.6) = ceil(6.6) = 7

#### Scenario: Calculate Damage Tiers for Level 4 Elite Controller
- **WHEN** user requests monster with level=4, organization="Elite", role="Controller"
- **THEN** Damage T1 = ceil((4 + 4 + 0) × 0.6) = ceil(4.8) = 5
- **THEN** Damage T2 = ceil((4 + 4 + 0) × 1.1) = ceil(8.8) = 9
- **THEN** Damage T3 = ceil((4 + 4 + 0) × 1.4) = ceil(11.2) = 12

#### Scenario: Calculate Damage for Horde Monster
- **WHEN** user requests monster with level=3, organization="Horde", role="Controller"
- **THEN** Damage T1 = ceil((4 + 3 + 0) × 0.6) ÷ 2 = ceil(4.2) ÷ 2 = 5 ÷ 2 = 3

#### Scenario: Validate Level Bounds
- **WHEN** user requests calculation with level < 1 or level > 10
- **THEN** system SHALL raise ValueError with descriptive error message
- **THEN** error message SHALL list valid levels (1-10)

### Requirement: Python Calculation Engine
The system SHALL provide a Python module (`calculate_stats.py`) that supports both CLI invocation and importable function calls for stat calculation.

#### Scenario: CLI Invocation with Valid Inputs
- **WHEN** user runs `python3 scripts/calculate_stats.py --level 3 --organization Horde --role Harrier`
- **THEN** system SHALL output JSON with all calculated stats
- **THEN** output SHALL include: level, organization, role, ev, stamina, free_strike, damage_t1, damage_t2, damage_t3, error=null

#### Scenario: CLI Invocation with Invalid Organization
- **WHEN** user runs `python3 scripts/calculate_stats.py --level 3 --organization Unknown --role Harrier`
- **THEN** system SHALL exit with error code 1
- **THEN** output SHALL include error message
- **THEN** output SHALL list valid_organizations array

#### Scenario: Module Import and Function Call
- **WHEN** Python code imports `from scripts.calculate_stats import calculate_all_stats`
- **AND** calls `calculate_all_stats(3, "Horde", "Harrier")`
- **THEN** function SHALL return dictionary with all calculated stats
- **THEN** return value SHALL be identical to CLI output for same inputs

#### Scenario: Text Format Output
- **WHEN** user runs CLI with `--format text`
- **THEN** system SHALL output key-value pairs (one per line)
- **THEN** format SHALL be: "key: value"

### Requirement: OpenCode Skill Discovery
The system SHALL be auto-discoverable by OpenCode CLI and web IDE via SKILL.md frontmatter metadata.

#### Scenario: Global Path Discovery
- **WHEN** skill folder exists at `~/.config/opencode/skills/draw-steel-monsters/`
- **AND** user runs `opencode skill list`
- **THEN** "draw-steel-monster-generator" SHALL appear in skill list
- **THEN** description SHALL match SKILL.md frontmatter

#### Scenario: Project-Local Path Discovery
- **WHEN** skill folder exists at `.opencode/skills/draw-steel-monsters/`
- **AND** user runs `opencode skill list`
- **THEN** "draw-steel-monster-generator" SHALL appear in skill list
- **THEN** both global and local paths SHALL be supported simultaneously

#### Scenario: Compatibility Field
- **WHEN** SKILL.md contains `compatibility: ["opencode-agent", "claude-code", "claude-web"]`
- **THEN** OpenCode SHALL recognize skill via "opencode-agent" entry
- **THEN** Claude Code SHALL recognize skill via "claude-code" entry
- **THEN** no breaking changes between platforms

### Requirement: Natural Language Monster Generation
The system SHALL generate complete Draw Steel monster stat blocks from natural language input containing creature name, level, organization, and role.

#### Scenario: Simple Input
- **WHEN** user provides "Create a Level 3 Pegasus, Horde, Harrier"
- **THEN** system SHALL generate complete stat block
- **THEN** output SHALL include: Name, Level, Organization, Role, EV, Stamina, Free Strike, Keywords, Damage Types, Signature Ability, Secondary Abilities, Malice Feature, Notes

#### Scenario: Input with Clarifications
- **WHEN** user provides partial input (missing level or role)
- **THEN** system SHALL ask for clarification
- **THEN** system SHALL specify required format: "creature, level (1-10), organization, role"

#### Scenario: Harrier Role Ability Pattern
- **WHEN** user requests Harrier role monster
- **THEN** Signature Ability SHALL emphasize mobility + strikes
- **THEN** Secondary Ability SHALL include repositioning effects
- **THEN** Damage SHALL use calculated T1/T2/T3 values exactly

#### Scenario: Brute Role Ability Pattern
- **WHEN** user requests Brute role monster
- **THEN** Signature Ability SHALL emphasize high damage + area effects
- **THEN** Secondary Ability SHALL include crowd control
- **THEN** Conditions SHALL include Prone, Restrained, Slowed

#### Scenario: Output Format
- **WHEN** system generates monster
- **THEN** output SHALL be YAML + Markdown format
- **THEN** output SHALL match SKILL.md example template
- **THEN** all calculated stats SHALL be verified before output

### Requirement: Formula Compliance Validation
The system SHALL validate all generated monsters against Draw Steel formulas before output, with a mandatory 8-point checklist.

#### Scenario: EV Validation
- **WHEN** system generates monster with level=3, organization=Platoon
- **THEN** validation SHALL confirm EV = ceil(((2 × 3) + 4) × 1.0) = ceil(10) = 10
- **THEN** if validation fails, system SHALL NOT output monster

#### Scenario: Stamina Validation
- **WHEN** system generates monster with level=3, role=Harrier, organization=Platoon
- **THEN** validation SHALL confirm Stamina = ceil(((10 × 3) + 20) × 1.0) = ceil(50) = 50
- **THEN** if validation fails, system SHALL NOT output monster

#### Scenario: Damage Validation
- **WHEN** system generates monster with level=3, role=Harrier, organization=Platoon
- **THEN** validation SHALL confirm Damage T1 = ceil((4 + 3 + 0) × 0.6) = ceil(4.2) = 5
- **THEN** validation SHALL confirm Damage T2 = ceil((4 + 3 + 0) × 1.1) = ceil(7.7) = 8
- **THEN** validation SHALL confirm Damage T3 = ceil((4 + 3 + 0) × 1.4) = ceil(9.8) = 10
- **THEN** if any validation fails, system SHALL NOT output monster

#### Scenario: Free Strike Validation
- **WHEN** system generates monster with level=3, role=Harrier, organization=Platoon
- **THEN** validation SHALL confirm Free Strike = ceil((4 + 3 + 0) × 0.6) = 5 (equals T1 damage)
- **THEN** if validation fails, system SHALL NOT output monster

#### Scenario: Keyword Validation
- **WHEN** system generates monster with keywords
- **THEN** validation SHALL confirm all creature keywords from fixed list
- **THEN** validation SHALL confirm all ability keywords from fixed list
- **THEN** validation SHALL confirm all damage types from fixed list
- **THEN** validation SHALL confirm all conditions from fixed list
- **THEN** if any invalid keyword, system SHALL NOT output monster

#### Scenario: Complete Checklist Execution
- **WHEN** system generates monster
- **THEN** validation SHALL run all 9 checks: EV, Stamina, Free Strike, Damage T1/T2/T3, Damage Types, Conditions, Keywords, Format match
- **THEN** only when ALL 9 checks pass shall system output monster

### Requirement: Fixed Reference Data
The system SHALL provide authoritative lists of valid keywords, damage types, conditions, organizations, and roles to prevent hallucination.

#### Scenario: Creature Keywords Lookup
- **WHEN** AI generates monster keywords
- **THEN** system SHALL limit choices to: Abyssal, Accursed, Animal, Beast, Construct, Dragon, Elemental, Fey, Giant, Horror, Humanoid, Infernal, Ooze, Plant, Soulless, Swarm, Undead
- **THEN** AI SHALL NOT invent new creature keywords

#### Scenario: Ability Keywords Lookup
- **WHEN** AI generates ability keywords
- **THEN** system SHALL limit choices to: Strike, Magic, Weapon, Psionic, Area
- **THEN** AI SHALL NOT invent new ability keywords

#### Scenario: Damage Types Lookup
- **WHEN** AI selects damage types for abilities
- **THEN** system SHALL limit choices to: acid, cold, corruption, fire, holy, lightning, poison, psychic, sonic
- **THEN** AI SHALL NOT invent new damage types

#### Scenario: Conditions Lookup
- **WHEN** AI applies conditions to abilities
- **THEN** system SHALL limit choices to: Bleeding, Dazed, Frightened, Grabbed, Prone, Restrained, Slowed, Taunted, Weakened
- **THEN** AI SHALL NOT invent new conditions

#### Scenario: Organizations Lookup
- **WHEN** AI parses organization input
- **THEN** system SHALL validate against: Minion, Horde, Platoon, Elite, Leader, Solo
- **THEN** if invalid organization, system SHALL prompt for correction

#### Scenario: Roles Lookup
- **WHEN** AI parses role input
- **THEN** system SHALL validate against: Ambusher, Artillery, Brute, Controller, Defender, Harrier, Hexer, Mount, Support
- **THEN** if invalid role, system SHALL prompt for correction

### Requirement: Documentation Coverage
The system SHALL provide comprehensive documentation covering formulas, ability templates, examples, keywords, and installation instructions.

#### Scenario: Formulas Reference
- **WHEN** user reads `formulas.md`
- **THEN** document SHALL include all formula expressions
- **THEN** document SHALL include complete lookup tables for Organization offsets, Role bonuses, Tier multipliers
- **THEN** document SHALL include example calculations with step-by-step breakdown

#### Scenario: Ability Templates Reference
- **WHEN** user reads `templates.md`
- **THEN** document SHALL include patterns for all 9 roles
- **THEN** each role SHALL include archetype description, signature ability pattern, secondary ability pattern
- **THEN** document SHALL include example ability names

#### Scenario: Complete Examples Reference
- **WHEN** user reads `examples.md`
- **THEN** document SHALL include 5 complete creature stat blocks
- **THEN** each example SHALL include: stat block, validation checklist, thematic notes, generation commentary
- **THEN** examples SHALL cover diverse levels (1, 2, 3, 4, 5), organizations, and roles

#### Scenario: Installation Instructions
- **WHEN** user reads `README.md`
- **THEN** document SHALL include OpenCode installation steps
- **THEN** document SHALL include usage examples
- **THEN** document SHALL include troubleshooting section with common errors and fixes

### Requirement: Testing Coverage
The system SHALL provide comprehensive pytest suite with 90%+ code coverage for calculation functions.

#### Scenario: EV Calculation Tests
- **WHEN** pytest runs test suite
- **THEN** suite SHALL include test for each Organization EV offset (6 tests)
- **THEN** suite SHALL include boundary tests for level=1 and level=10 (2 tests)
- **THEN** suite SHALL include invalid level tests (level=0, level=11) (2 tests)

#### Scenario: Stamina Calculation Tests
- **WHEN** pytest runs test suite
- **THEN** suite SHALL include test for each Role stamina bonus (9 tests)
- **THEN** suite SHALL include tests for each Organization multiplier (6 tests)
- **THEN** combined tests SHALL verify formula: (10 × L + bonus) × multiplier

#### Scenario: Damage Calculation Tests
- **WHEN** pytest runs test suite
- **THEN** suite SHALL include tests for all three tiers (3 tests per combo)
- **THEN** suite SHALL include tests for all Role damage modifiers (9 tests)
- **THEN** suite SHALL include tests for all Organization multipliers (6 tests)
- **THEN** combined tests SHALL verify formula: (4 + L + mod) × tier × org_mult

#### Scenario: Integration Tests
- **WHEN** pytest runs test suite
- **THEN** suite SHALL include `calculate_all_stats()` function tests (4+ tests)
- **THEN** tests SHALL cover valid input scenarios
- **THEN** tests SHALL cover invalid input scenarios (level, organization, role)

#### Scenario: Coverage Threshold
- **WHEN** pytest runs with `--cov=scripts` flag
- **THEN** coverage SHALL be ≥90%
- **THEN** uncovered lines SHALL be documented as acceptable (e.g., error paths only)

### Requirement: Development Tooling
The system SHALL provide Poetry-based environment with code quality tools (black, flake8, mypy) and pre-commit hooks.

#### Scenario: Poetry Installation
- **WHEN** developer runs `poetry install`
- **THEN** system SHALL install Python 3.8+ dependencies
- **THEN** system SHALL install dev dependencies (pytest, black, flake8, mypy, pytest-cov)
- **THEN** virtual environment SHALL be created automatically

#### Scenario: Code Formatting
- **WHEN** developer runs `poetry run black scripts/`
- **THEN** system SHALL format all Python files to 100 character line length
- **THEN** system SHALL target Python 3.8+ syntax
- **THEN** formatting SHALL be PEP 8 compliant

#### Scenario: Linting
- **WHEN** developer runs `poetry run flake8 scripts/`
- **THEN** system SHALL check code style violations
- **THEN** system SHALL exclude .git, __pycache__, venv directories
- **THEN** system SHALL report line length violations (>100 chars)

#### Scenario: Type Checking
- **WHEN** developer runs `poetry run mypy scripts/`
- **THEN** system SHALL verify type hints on all functions
- **THEN** system SHALL warn on `Any` return types
- **THEN** system SHALL warn on unused configurations

#### Scenario: Pre-commit Hooks
- **WHEN** developer runs `pre-commit install`
- **THEN** system SHALL install git hooks for black, flake8, end-of-file-fixer, trailing-whitespace
- **THEN** hooks SHALL run automatically on `git commit`
- **THEN** hooks SHALL prevent commits if checks fail

### Requirement: CI/CD Automation
The system SHALL provide GitHub Actions workflows for automated testing across Python 3.8-3.11 and release automation.

#### Scenario: Test Workflow
- **WHEN** developer pushes code to GitHub
- **THEN** GitHub Actions SHALL run workflow on Python 3.8, 3.9, 3.10, 3.11
- **THEN** workflow SHALL install dependencies, run linting, type checking, and tests
- **THEN** workflow SHALL upload coverage report to Codecov
- **THEN** workflow SHALL fail if any check fails

#### Scenario: Release Workflow
- **WHEN** developer pushes version tag (e.g., v1.0.0)
- **THEN** GitHub Actions SHALL create GitHub release
- **THEN** release body SHALL be populated from CHANGELOG.md
- **THEN** release SHALL be marked draft for beta tags
- **THEN** release SHALL be marked prerelease for alpha/beta tags

### Requirement: Performance Targets
The system SHALL generate monsters in <30 seconds with <3K token usage and Python calculations in <5 seconds.

#### Scenario: Generation Time
- **WHEN** user requests monster generation
- **THEN** complete stat block SHALL be generated in <30 seconds
- **THEN** time SHALL include formula calculation + AI generation

#### Scenario: Token Usage
- **WHEN** AI generates monster from SKILL.md
- **THEN** token consumption SHALL be <3K tokens
- **THEN** token usage SHALL be 40-60% below raw prompt generation

#### Scenario: Python Calculation Latency
- **WHEN** Python script calculates stats via CLI or module import
- **THEN** calculation SHALL complete in <5 seconds
- **THEN** latency SHALL include all formula computations and validation

### Requirement: License and Open Source
The system SHALL be released under MIT license and be fully open source on GitHub.

#### Scenario: License File
- **WHEN** user reviews LICENSE file
- **THEN** license SHALL be MIT
- **THEN** license SHALL permit commercial use, modification, distribution, private use
- **THEN** repository SHALL be public on GitHub

#### Scenario: Repository Structure
- **WHEN** user clones repository
- **THEN** structure SHALL include SKILL.md, scripts/, docs/, tests/, .github/, README.md, LICENSE
- **THEN** repository SHALL be ready for immediate use without additional setup

### Requirement: Claude Code Compatibility
The system SHALL maintain compatibility with Claude Code and Claude Web via SKILL.md metadata (secondary target in Phase 1).

#### Scenario: SKILL.md Format
- **WHEN** Claude Code reads SKILL.md
- **THEN** frontmatter SHALL include standard fields (name, description, context, agent)
- **THEN** frontmatter SHALL include compatibility field with "claude-code" entry
- **THEN** Claude Code SHALL recognize and load skill

#### Scenario: Claude Web Upload
- **WHEN** user uploads SKILL.md to Claude Web UI
- **THEN** Claude Web SHALL recognize skill format
- **THEN** skill SHALL work without Python execution (web limitation)
- **THEN** AI SHALL use embedded lookup tables instead of Python module

