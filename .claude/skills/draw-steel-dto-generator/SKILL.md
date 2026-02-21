---
name: draw-steel-dto-generator
description: Generates Draw Steel TTRPG Dynamic Terrain Objectives (DTOs) with pattern-compliant stat blocks. Use when creating traps, hazards, fieldworks, mechanisms, siege engines, power fixtures, or supernatural objects for the Draw Steel tabletop roleplaying game.
license: MIT
compatibility: Designed for Claude Code, Cursor, Gemini CLI, and Antigravity Google following the Agent Skills specification.
metadata:
  author: stgreenb
  version: "1.0"
---

# Draw Steel Dynamic Terrain Objective Generator

Generate Draw Steel TTRPG Dynamic Terrain Objectives (DTOs) that strictly conform to official MCDM format from the Dynamic Terrain chapter.

## Quick Start

**Input Format:** `"Create a Level [X] [Category] [Name]"` or `"Create a Level [X] [Category] ([Role]) [Name]"`

**Examples:**
- `"Create a Level 2 Environmental Hazard Acidic Bog"`
- `"Create a Level 1 Fieldwork (Ambusher) Snap Trap"`
- `"Create a Level 3 Siege Engine Scorpion Ballista"`
- `"Create a Level 5 Power Fixture Crystal Shrine --format foundry"`
- `"Create a Level 1 Trap Bear Trap --format both"`

**Categories:** Environmental Hazard, Fieldwork, Mechanism, Siege Engine, Power Fixture, Supernatural Object

**Output Formats:** `--format markdown` (default), `--format foundry`, `--format both`

**Roles (secondary tags indicating mechanical pattern):**
- **Defender:** High Stamina, protects allies (Brambles, Column of Blades)
- **Hexer:** Applies conditions (Angry Beehive, Lava, Toxic Plants)
- **Ambusher:** Triggered sudden damage (Bear Trap, Dart Trap, Snare Trap)
- **Artillery:** Long-range area attacks (Arrow Launcher, Catapult)
- **Support:** Grants resources or mobility (Pressure Plate, Pulley, Holy Idol)
- **Controller:** Complex battlefield control (Black Obelisk, Throne of A'An)

## Critical: Draw Steel Mechanics (NOT D&D)

**CRITICAL:** There is NO concept of Difficulty Class (DC) in Draw Steel. DTOs use Draw Steel's unique mechanics, NOT D&D-style saving throws.

### Converting D&D Mechanics to Draw Steel

When converting traps/hazards from D&D or other systems:

| Original D&D Concept | Draw Steel Method | When to Use |
|---------------------|-------------------|-------------|
| **DC vs. Saving Throw** (to apply a condition) | **Potency Check** | In DTO abilities to apply conditions based on target's characteristic |
| **DC vs. Skill Check** (to interact/resist) | **Characteristic Test** | For deactivating DTOs, resisting effects, or actively challenging the effect |
| **Saving Throw** (to end a persistent effect) | **Saving Throw (d10)** | ONLY for conditions marked "(save ends)" |

### Three Draw Steel Mechanics

| Purpose | Mechanic | When to Use |
|---------|----------|-------------|
| **Apply a condition** | **Potency Check** | In DTO abilities to apply conditions based on target's characteristic |
| **Interact/resist** | **Characteristic Test** | For deactivating DTOs, resisting environment effects |
| **End a condition** | **Saving Throw (d10)** | ONLY for conditions marked "(save ends)" |

### Potency Check Format

`[Characteristic] < [Value] [condition]`

- M = Might, A = Agility, R = Reason, I = Intuition, P = Presence
- Value = potency threshold (typically -1, 0, 1, 2, 3 based on tier)
- Condition = the condition applied (may include "(save ends)")

**Example:** `A < 1 slowed (save ends)` means "If target's Agility is less than 1, they are slowed (save ends)"

### D&D Terms → Draw Steel Terms

| D&D Term (NEVER USE) | Draw Steel Term |
|---------------------|-----------------|
| "DC 15" | "A < 2" or "Agility test" |
| "saving throw" | "save" or "save ends" |
| "1d6 damage" | "5 damage" (fixed values) |
| "Dexterity save" | "Agility test" or "A < X" |
| "half damage on save" | Not used in Draw Steel |

### Conversion Examples

**Example 1: D&D Trap with DC Save → Potency Check**
```
❌ D&D: "DC 13 Dexterity save or take 2d6 piercing damage and be restrained"

✓ Draw Steel:
Power Roll + 2:
- ≤11: 5 damage
- 12-16: 7 damage; A < 1 slowed (save ends)
- 17+: 9 damage; A < 2 restrained (save ends)
```

**Example 2: D&D Skill Check to Disarm → Characteristic Test**
```
❌ D&D: "DC 12 Thieves' Tools check to disarm"

✓ Draw Steel:
As a maneuver, a creature adjacent to the trap can make an Agility test.
- ≤11: The creature triggers the trap.
- 12-16: The trap is deactivated but the creature is slowed (EoT).
- 17+: The trap is deactivated and doesn't trigger.
```

**Example 3: D&D Ongoing Damage → Burning Condition**
```
❌ D&D: "takes 1d6 fire damage at start of each turn, DC 12 Con save to end"

✓ Draw Steel:
M < 2 burning (save ends)

Note: Burning means "takes 1d6 fire damage at start of each turn". The target rolls d10 (6+ ends it).
```

## Power Roll Outcomes

### Active DTO Power Rolls (DTO Rolls)

```
Power Roll + 2:
- ≤11: [Tier 1 effect - weakest]
- 12-16: [Tier 2 effect - average]
- 17+: [Tier 3 effect - strongest]
```

### Passive Player Tests (Player Rolls)

For deactivation, avoidance, etc.:

```
As a maneuver, a creature adjacent to [DTO] can make an [Characteristic] test.
- ≤11: [Worst outcome for player]
- 12-16: [Partial success]
- 17+: [Best outcome for player]
```

### Potency Scaling by Tier

| Tier | Potency Value | Example (with +2 Might) |
|------|---------------|-------------------------|
| Tier 1 (≤11) | Characteristic - 2 | M < 0 slowed |
| Tier 2 (12-16) | Characteristic - 1 | M < 1 slowed |
| Tier 3 (17+) | Characteristic | M < 2 slowed |

## DTO Categories

### 1. Environmental Hazards

Natural elements that threaten creatures in an area.

**Format:** `[Name] (Level X Hazard [Role])`

**EV Ranges:**
- Level 1: 1 EV (Brambles, Frozen Pond)
- Level 2: 2-3 EV (Angry Beehive 2, Corrosive Pool 3)
- Level 3: 3-4 EV (Lava 4, Quicksand 3)

**Stamina Types:**
- Per-square: Multi-square terrain (Brambles 3/sq, Lava 12/sq)
- Fixed: Single objects (Angry Beehive 3)
- None: Indestructible (Quicksand -)

**Characteristics:**
- Often difficult terrain
- Activate on enter/start turn
- May have Immunity field

**Example:**
```
Lava (Level 3 Hazard Hexer)

- EV: 4 per 10 x 10 patch
- Stamina: 12 per square
- Size: One or more squares of difficult terrain
- Immunity: 20 to all damage except cold damage

> 🌀 Deactivate
> Each square of lava must be individually destroyed.

> ❕ Activate
> A creature or object enters the lava or starts their turn there, or starts their turn adjacent to the lava.
> Effect: The Liquid Hot Magma ability.

> ❗️ Liquid Hot Magma
> | Melee, Strike | Free triggered action |
> | 📏 Melee 1 | 🎯 The triggering creature or object |
> Power Roll + 2:
> - ≤11: 5 fire damage; M < 1 burning (save ends)
> - 12-16: 9 fire damage; M < 2 burning (save ends)
> - 17+: 12 fire damage; M < 3 burning (save ends)
```

### 2. Fieldworks

Military fortifications and traps placed by defenders.

**Format:** `[Name] (Level X [Type] [Role])` where Type = Trap or Fortification

**EV Ranges:**
- Level 1: 1-2 EV (Bear Trap 2, Hidey-Hole 1, Pavise Shield 1)
- Level 2: 3 EV (Spike Trap 3, Pillar 3, Ram 3)

**Stamina Types:**
- Fixed: Point traps (Bear Trap 6, Snare Trap 1)
- Per-square: Barriers (Archer's Stakes 3/sq)
- None: Non-physical (Hidey-Hole -, Flammable Oil -)

**Characteristics:**
- Often have Hidden property
- May have Allied Awareness
- Often calibrated to trigger on specific creature sizes
- Direction field for directional DTOs

**Example:**
```
Bear Trap (Level 1 Trap Ambusher)

- EV: 2
- Stamina: 6
- Size: 1S

> ⭐️ Hidden
> The bear trap is hidden until triggered or detected.

> 🌀 Deactivate
> As a maneuver, a creature adjacent to a bear trap can make an Agility test.
> - ≤11: The creature triggers the trap and is affected as if in its space.
> - 12-16: The trap is deactivated but the creature is slowed (EoT).
> - 17+: The trap is deactivated and doesn't trigger.

> ❕ Activate
> The bear trap is calibrated to be triggered by creatures or objects of a particular size. The trap triggers when a creature or object of the appropriate size enters its space.
> Effect: A triggering creature or object ends their movement and is targeted by the Bear Trap ability.

> ❗️ Bear Trap
> | Melee, Strike, Weapon | Free triggered action |
> | 📏 Melee 0 | 🎯 The triggering creature or object |
> Power Roll + 2:
> - ≤11: 1 damage; the target shifts 1 square away from the trap
> - 12-16: 3 damage; A < 1 slowed (save ends)
> - 17+: 5 damage; A < 2 slowed (save ends)
> Effect: The bear trap must be manually reset.
```

### 3. Mechanisms

Intricate devices that may be linked to triggers.

**Format:** `[Name] (Level X [Type] [Role])` where Type = Trap, Trigger, or Fortification

**EV Ranges:**
- Level 1: 1-2 EV (Dart Trap 1, Switch 1, Pressure Plate 2)
- Level 2: 3 EV (Pillar 3, Ram 3)
- Level 3: 3-4 EV (Column of Blades 3, Portcullis 4)

**Stamina Types:**
- Fixed: Single devices (Dart Trap 3, Switch 3, Pillar 6)
- Per-square: Large barriers (Portcullis 9/sq, Ram 3/sq)
- None: Triggers (Pressure Plate -)

**Trigger Mechanisms:**
Have Link field: "A [mechanism type] is linked to another mechanism that it activates when triggered."

**Linked DTOs:**
Activate section specifies: "A pressure plate, switch, or other linked trigger is activated."

**Example (Trigger Mechanism):**
```
Pressure Plate (Level 1 Trigger Support)

- EV: 2
- Stamina: -
- Size: Any area
- Typical Space: One square, up to a 4 x 4-square area
- Link: A pressure plate is linked to another mechanism that it activates when triggered.

> 🌀 Deactivate
> As a maneuver, a creature adjacent to a pressure plate can make an Agility test.
> - ≤11: The creature triggers the pressure plate.
> - 12-16: The pressure plate is deactivated but the creature is slowed (EoT).
> - 17+: The pressure plate is deactivated and doesn't trigger.

> ❕ Activate
> The pressure plate is calibrated to be triggered by creatures or objects of a particular size. The pressure plate triggers when a creature or object of the appropriate size enters its area.
> Effect: The linked mechanism is activated. A pressure plate automatically resets and can be triggered repeatedly.
```

### 4. Siege Engines

Large weapons requiring creatures to operate.

**Format:** `[Name] (Level X Siege Engine [Role])`

**EV Ranges:**
- Level 2: 8 EV (Arrow Launcher, Field Ballista)
- Level 3: 10 EV (Catapult, Boiling Oil Cauldron)
- Level 4: 12 EV (Iron Dragon)

**Stamina:**
- Level 2: 30-50 (Arrow Launcher 30, Field Ballista 40)
- Level 3: 25-60 (Exploding Mill Wheel 25, Catapult 50)
- Level 4: 60 (Iron Dragon 60)

**Siege Engine Abilities:**

All abilities labeled: `Main action (Adjacent creature)`

Required abilities:
1. **Primary Attack** - Main damaging ability
2. **Reload** - Enables primary attack again

Optional abilities:
3. **Spot** - Grants edge + range bonus
4. **Move** - Moves engine + operator

**Example:**
```
Arrow Launcher (Level 2 Siege Engine Artillery)

- EV: 8
- Stamina: 30
- Size: 1L

> 🌀 Deactivate
> As a maneuver, a creature adjacent to an arrow launcher can make an Agility test.
> - ≤11: The creature accidentally activates the Arrow Storm ability.
> - 12-16: The arrow launcher is deactivated but the creature is slowed (EoT).
> - 17+: The arrow launcher is deactivated and can't be used.

> 🔳 Arrow Storm
> | Area, Ranged, Weapon | Main action (Adjacent creature) |
> | 📏 5 cube within 20 | 🎯 Each creature and object in the area |
> Power Roll + 2:
> - ≤11: 5 damage
> - 12-16: 8 damage
> - 17+: 11 damage
> Effect: This ability can't be used again until the arrow launcher is reloaded.

> ⭐️ Reload
> | - | Main action (Adjacent creature) |
> | 📏 - | 🎯 - |
> Effect: The arrow launcher is reloaded, allowing Arrow Storm to be used again. This action can be used only once per round.

> ⭐️ Spot
> | - | Main action (Adjacent creature) |
> | 📏 - | 🎯 - |
> Effect: The next use of Arrow Storm gains an edge and has a +10 bonus to ranged distance. This action can be used only once per round.

> ⭐️ Move
> | - | Main action (Adjacent creature) |
> | 📏 - | 🎯 - |
> Effect: The arrow launcher and the creature using this action move together up to 3 squares.
```

### 5. Power Fixtures

Powerful fortifications for solo creature encounters.

**Format:** `[Name] (Level X Relic [Role])` or `[Name] (Level X Hazard [Role])`

**EV Ranges:**
- Level 5: 7-14 EV (Holy Idol 7, Psionic Shard 7, Tree of Might 14)

**Stamina:**
- Level 5: 35-60 (Holy Idol 35, Psionic Shard 40, Tree of Might 60)

**Characteristics:**
- Provide ongoing effects at start of round
- Often grant resources (dice, temporary Stamina, bonuses)
- May have defensive buffs or environmental control
- High durability

**Example:**
```
Holy Idol (Level 5 Relic Support)

- EV: 7
- Stamina: 35
- Size: 2

> 🌀 Deactivate
> The holy idol must be completely destroyed.

> ⭐️ Empowered Will
> At the start of each round while the holy idol is intact, the Director gains a d6 that lasts until the end of the round. When a Director-controlled creature deals or takes damage, the Director can roll the d6 to increase the damage the creature deals or reduce the damage the creature takes by an amount equal to the roll (to a minimum of 2 damage).
```

### 6. Supernatural Objects

Magical or psionic objects with complex abilities.

**Format:** `[Name] (Level X Relic [Role])`

**EV Ranges:**
- Level 3: 20 EV (Black Obelisk, Chronal Hypercube)
- Level 4: 24 EV (Throne of A'An)

**Stamina:**
- Level 3: 80-100 (Chronal Hypercube 80, Black Obelisk 100)
- Level 4: 140 (Throne of A'An 140)

**Characteristics:**
- Very high EV (20+)
- Effects target enemies and sometimes allies
- Unique, complex abilities
- Often require special conditions to deactivate

**Example:**
```
The Black Obelisk (Level 3 Relic Controller)

- EV: 20
- Stamina: 100
- Size: 2

> 🌀 Deactivate
> As a maneuver, a creature adjacent to the black obelisk can make a Reason test.
> - ≤11: The creature accidentally activates the Your Fears Become Manifest ability, which gains an edge.
> - 12-16: The creature must make another test to deactivate the obelisk. If they obtain this outcome a second time, they accidentally activate Your Fears Become Manifest.
> - 17+: The obelisk is deactivated until the end of the encounter.

> ❕ Activate
> A new round starts.
> Effect: The Your Fears Become Manifest ability.

> ❗️ Your Fears Become Manifest
> | Area, Magic | Free triggered action |
> | 📏 10 burst | 🎯 Each enemy in the area |
> Power Roll + 2:
> - ≤11: P < 1 slowed (EoT)
> - 12-16: P < 2 slowed and weakened (EoT)
> - 17+: P < 3 frightened, slowed, and weakened (EoT)
> Effect: The target is pushed 2 squares.
```

## EV Calculation Patterns

### EV by Category and Level

| Category | Level 1 | Level 2 | Level 3 | Level 4 | Level 5 |
|----------|---------|---------|---------|---------|---------|
| Environmental Hazard | 1 | 2-3 | 3-4 | - | - |
| Fieldwork | 1-2 | 3 | - | - | - |
| Mechanism | 1-2 | 3 | 3-4 | - | - |
| Siege Engine | - | 8 | 10 | 12 | - |
| Power Fixture | - | - | - | - | 7-14 |
| Supernatural Object | - | - | 20 | 24 | - |

### Linked EV

**CRITICAL: Linked mechanisms are TWO SEPARATE DTOs, not one combined stat block.**

When generating a linked system (pressure plate + trap), output:
1. **Trigger DTO** (e.g., Pressure Plate) - complete stat block
2. **Linked DTO** (e.g., Dart Trap) - complete stat block

**❌ WRONG - Combined stat block:**
```
EV: 3 (Pressure Plate 2 + Dart Trap 1)  ← NEVER do this
```

**✓ CORRECT - Two separate stat blocks:**

```
Pressure Plate (Level 1 Trigger Support)
- EV: 2
- Stamina: -
...
Link: A pressure plate is linked to another mechanism...

---

Dart Trap (Level 1 Trap Ambusher)
- EV: 1
- Stamina: 3
...
Activate: A pressure plate, switch, or other linked trigger is activated.
```

| Type | Description | Examples |
|------|-------------|----------|
| **Fixed** | Single object | Bear Trap 2, Dart Trap 1 |
| **Per-10×10** | Scales with size | Brambles 1/10×10, Lava 4/10×10 |

### Upgrade EV Costs

| Complexity | EV Cost | Examples |
|------------|---------|----------|
| Simple | +1 EV | Concealed Hive, Chain, Large Darts |
| Moderate | +2 EV | Killer Bees, Poison Darts |
| Major | +3-4 EV | Screamers, Magma Flow, Gatling Darts |
| Multiple items | +3 EV per item | Additional pillars, rams |

## Stamina Patterns

### By Category

| Category | Stamina Type | Range |
|----------|--------------|-------|
| Environmental Hazard | Per-square or Fixed | 3-12/sq or 3 fixed |
| Fieldwork | Fixed or Per-square | 1-9 or 3-9/sq |
| Mechanism | Fixed or None | 3-6 or - |
| Siege Engine | Fixed | 25-60 |
| Power Fixture | Fixed | 35-60 |
| Supernatural Object | Fixed | 80-140 |

### By Level

| Level | Siege Engine | Power Fixture | Supernatural Object |
|-------|--------------|---------------|---------------------|
| 2 | 30-50 | - | - |
| 3 | 25-60 | - | 80-100 |
| 4 | 60 | - | 140 |
| 5 | - | 35-60 | - |

## Damage Values by Level

### Power Roll Damage (Tier 1 / Tier 2 / Tier 3)

| Level | Tier 1 (≤11) | Tier 2 (12-16) | Tier 3 (17+) |
|-------|--------------|----------------|--------------|
| 1 | 1-4 | 3-5 | 5-6 |
| 2 | 3-5 | 6-9 | 9-11 |
| 3 | 3-5 | 6-9 | 9-12 |
| 4 | 6 | 10 | 13 |
| 5 | 6 | 11 | 14 |

### Mechanism Damage (Lower than Siege Engines)

Mechanisms (traps, devices) deal less damage than siege engines at the same level.

| Level | Mechanism (T1/T2/T3) | Siege Engine (T1/T2/T3) |
|-------|---------------------|------------------------|
| 1 | 2/4/5 | - |
| 2 | 3/5/7 to 4/6/9 | 5/8/11 |
| 3 | 3/7/10 | 5/9/12 |
| 4 | - | 6/10/13 |

**Examples:**
- Dart Trap (L1): 2/4/5 damage
- Pillar (L2): 4/6/9 damage
- Portcullis (L3): 3/7/10 damage
- Arrow Launcher (L2 Siege): 5/8/11 damage

### Siege Engine Damage

| Level | Tier 1 | Tier 2 | Tier 3 |
|-------|--------|--------|--------|
| 2 | 5 | 8 | 11 |
| 3 | 5 | 9 | 12 |
| 4 | 6 | 10 | 13 |

## Damage Types

**ALWAYS specify damage type - NEVER use generic "damage"**

> **When validating damage types or conditions:** `../shared/DRAW_STEEL_BASICS.md`

### Theme Matching

| DTO Theme | Damage Type |
|-----------|-------------|
| Lava, oil, fire | fire |
| Ice, cold | cold |
| Acid, corrosive | acid |
| Venomous, toxic | poison |
| Magical, supernatural | psychic, corruption, or holy |
| Physical traps | Just say "damage" (no type in power rolls) |

**Physical Trap Example (Bear Trap, Dart Trap, Column of Blades):**
```
Power Roll + 2:
- ≤11: 3 damage
- 12-16: 5 damage
- 17+: 7 damage
```

**Elemental Hazard Example (Lava, Angry Beehive):**
```
Power Roll + 2:
- ≤11: 5 fire damage
- 12-16: 9 fire damage
- 17+: 12 fire damage
```

## Conditions

> **When validating conditions:** `../shared/DRAW_STEEL_BASICS.md`

### Condition Durations

| Duration | Format | How It Ends |
|----------|--------|-------------|
| Save ends | `[condition] (save ends)` | Target rolls d10, 6+ ends condition |
| End of turn | `[condition] (EoT)` | Ends at end of current turn |
| End of encounter | `[condition] until the end of the encounter` | Ends when encounter ends |
| Conditional | `[condition]` with no duration | Ends by specific action |

### Special Conditions

| Condition | Duration Behavior |
|-----------|-------------------|
| grabbed | Ends by escape, release, or breaking adjacency |
| prone | Ends by standing up maneuver |
| frightened | Ends when source changes or is removed |
| burning | Takes 1d6 fire damage at start of each turn (save ends) |
| bleeding | Takes damage when using actions (save ends) |

**CRITICAL: grabbed NEVER uses "(save ends)"**

Grabbed is a conditional condition that ends when the target escapes or breaks adjacency. It does NOT end via saving throw.

```
❌ WRONG: M < 2 grabbed (save ends)
✓ CORRECT: M < 2 grabbed
```

**Example from Bear Trap:**
```
- 12-16: 3 damage; A < 1 slowed (save ends)  ← slowed uses save ends
- 17+: 5 damage; A < 2 slowed (save ends)    ← slowed uses save ends
```
Note: Bear Trap mentions grabbed in Effect text, not potency. When using grabbed in potency, just say "M < 2 grabbed" without (save ends).

## Special DTO Properties

### Hidden Property

Many DTOs are hidden until triggered or detected.

**Format:**
```
> ⭐️ Hidden
> The [DTO name] is hidden until triggered or detected.
```

**Discovery:** Intuition test as part of Search for Hidden Creatures maneuver:
- ≤11: Find hidden terrain objects adjacent to you
- 12-16: Find hidden terrain objects within 5 squares
- 17+: Find hidden terrain objects within 10 squares

**Common Hidden DTOs:** Bear Trap, Snare Trap, Spike Trap, Quicksand, Dart Trap, Portcullis, Ram, Pressure Plate

### Allied Awareness

Benefits for defenders familiar with the DTO.

**Format:**
```
> ⭐️ Allied Awareness
> [Description of benefits and options available to creatures with familiarity and training]
```

**Examples:**
- Corrosive Pool: Allies with torches can trigger Explosive Reaction
- Archer's Stakes: Allies ignore difficult terrain, take no damage, have cover
- Column of Blades: Allies who shift don't trigger

### Immunity

Durable DTOs have damage immunities.

**Format:** `Immunity: [value] to all damage except [type] damage`

**Examples:**
- Lava: Immunity 20 to all damage except cold
- Corrosive Pool: Immunity 20 to all damage except cold or fire
- Frozen Pond: Immunity 5 to all damage except fire
- Tree of Might: Immunity 5 to all damage except corruption or fire

### Link Field

Trigger mechanisms use Link field to indicate connection.

**Format:** `Link: A [mechanism type] is linked to another mechanism that it activates when triggered.`

### Direction Field

Directional DTOs indicate firing direction.

**Format:** `Direction: The [DTO name] fires in a fixed direction.`

### Typical Space

Large trigger areas have typical space guidance.

**Format:** `Typical Space: [size description]`

## Characteristic Tests by DTO

### Deactivation Test Characteristics

| Characteristic | Use Case | Example DTOs |
|----------------|----------|--------------|
| Agility | Traps, mechanisms, nimble work | Bear Trap, Dart Trap, Arrow Launcher, Catapult |
| Might | Physical strength tasks | Hidey-Hole, Pavise Shield |
| Reason | Intellectual or magical tasks | Black Obelisk, Exploding Mill Wheel |
| Intuition | Perception and awareness | Column of Blades (Allied Awareness) |
| Presence | Social or supernatural tasks | Throne of A'An |

### Deactivate Section Rules

**Deactivate sections have ONE primary method, optionally followed by a consequence note.**

| Pattern | Example |
|---------|---------|
| **Test-based** | "As a maneuver, a creature...can make an Agility test." |
| **Destruction** | "The [object] must be completely destroyed." |
| **Impossible** | "The [object] can't be deactivated." |
| **Impossible + consequence** | "The [object] can't be deactivated. If it takes damage, [effect]." |

```
❌ WRONG - Two separate methods:
> 🌀 Deactivate
> The spirits must be completely destroyed. As a maneuver, a creature can make a Presence test.

✓ CORRECT - One method:
> 🌀 Deactivate
> As a maneuver, a creature adjacent to the gravebound spirits can make a Presence test.

✓ CORRECT - Impossible with consequence (from Angry Beehive):
> 🌀 Deactivate
> The beehive can't be deactivated. If it takes damage or is destroyed, the hive unleashes a swarm of bees.
```

## DTO Stat Block Template

```markdown
###### [Name] (Level [X] [Category] [Role])

[Flavor text description]

- **EV:** [value] [per 10×10 if applicable]
- **Stamina:** [value] [per square if applicable, or "-"]
- **Size:** [size]
- **[Optional: Immunity/Direction/Typical Space/Link]**

<!-- -->
> 🌀 **Deactivate**
>
> [Deactivation method, often with characteristic test and outcomes]

<!-- -->
> ❕ **Activate**
>
> [Trigger condition]
>
> **Effect:** [What happens when triggered]

<!-- -->
> ❗️ **[Ability Name]**
>
> | **[Keywords]** | **[Action Type]** |
> | -------------- | ----------------: |
> | **📏 [Distance]** | **🎯 [Target]** |
>
> **[Trigger if applicable]**
>
> **Power Roll + 2:**
>
> - **≤11:** [Tier 1 effect]
> - **12-16:** [Tier 2 effect]
> - **17+:** [Tier 3 effect]
>
> **Effect:** [Additional effects]

<!-- -->
> ⭐️ **[Optional: Upgrades/Hidden/Allied Awareness]**
>
> [Upgrade name (+X EV)] [Description]
```

## Ability Keywords

DTOs DO NOT have object-level keywords. Their abilities use standard ability keywords.

### Valid DTO Ability Keywords

| Keyword | Use | Example |
|---------|-----|---------|
| `area` | Area attacks | Arrow Storm, Black Obelisk |
| `melee` | Melee attacks | Bear Trap, Lava |
| `ranged` | Ranged attacks | Dart Trap, Arrow Storm |
| `strike` | Attack abilities | Most DTO abilities |
| `weapon` | Physical traps | Bear Trap, Dart Trap |
| `magic` | Supernatural effects | Black Obelisk, Frozen Pond |

**Keywords are always lowercase.**

### Keyword + Distance Combinations

**CRITICAL: Keywords must match distance type.**

| Keywords | Distance Format | Example DTOs |
|----------|-----------------|--------------|
| `melee, strike, weapon` | `📏 Melee 0` or `📏 Melee 1` | Bear Trap, Column of Blades |
| `ranged, strike, weapon` | `📏 Ranged 5` | Dart Trap |
| `area, ranged, weapon` | `📏 5 cube within 20` | Arrow Storm |
| `area, magic` | `📏 10 burst` | Black Obelisk |
| `melee, strike` | `📏 Melee 0` or `📏 Melee 1` | Lava (no weapon) |
| `magic, melee, strike` | `📏 Melee 0` | Frozen Pond, Sleep Spores |

```
❌ WRONG - Keyword/distance mismatch:
| Melee, Strike, Weapon | Free triggered action |
| 📏 Ranged 5 | 🎯 One creature |    ← Melee keyword but Ranged distance

❌ WRONG - Keyword/distance mismatch:
| Ranged, Strike, Weapon | Free triggered action |
| 📏 Melee 1 | 🎯 One creature |    ← Ranged keyword but Melee distance

✓ CORRECT - Keyword/distance match:
| Ranged, Strike, Weapon | Free triggered action |
| 📏 Ranged 5 | 🎯 One creature |    ← Dart Trap
```

### Damage Type is NOT a Keyword

**CRITICAL: Do NOT use damage types as keywords.**

Damage type (`fire`, `cold`, `poison`, etc.) belongs in the power roll damage description, NOT in keywords.

```
❌ WRONG - Damage type as keyword:
| Fire, Area, Magic | Free triggered action |
| 📏 5 burst | 🎯 Each creature in area |
Power Roll + 2:
- ≤11: 5 fire damage    ← redundant "fire" keyword above

✓ CORRECT - Damage type in power roll only:
| Area, Magic | Free triggered action |
| 📏 5 burst | 🎯 Each creature in area |
Power Roll + 2:
- ≤11: 5 fire damage; M < 1 burning (save ends)
```

**Action Types:**
- `Free triggered action` - Most DTO activations
- `Main action (Adjacent creature)` - Siege engine abilities

## Special Sections

### Hidden Property Format

**Keep Hidden sections simple. Do not include discovery mechanics.**

```
✓ CORRECT:
> ⭐️ Hidden
> The bear trap is hidden until triggered or detected.

❌ WRONG - Too detailed:
> ⭐️ Hidden
> The illusory floor is hidden until triggered or detected. A creature who succeeds on an Intuition test as part of a Search for Hidden Creatures maneuver can see through the illusion.
```

Discovery rules are handled by the standard Search for Hidden Creatures maneuver, not in the Hidden section.

### Allied Awareness Format

Allied Awareness grants **automatic benefits** to allies familiar with the DTO, not test-based abilities.

```
✓ CORRECT - Automatic benefits:
> ⭐️ Allied Awareness
> Allies ignore difficult terrain, take no damage from moving through, and have cover.

❌ WRONG - Test-based ability:
> ⭐️ Allied Awareness
> Creatures familiar with the runes can make an Agility test as a maneuver to move through the area without triggering them.
```

**If you need a test-based ability, create it as a separate feature, not Allied Awareness.**

## Self-Validation Checklist

Before outputting a DTO, verify:

- [ ] Header line includes: Name (Level X Category Role)
- [ ] EV value present with correct type (fixed, per-area, linked)
- [ ] Stamina value present (fixed, per-square, or "-")
- [ ] Size value present (use "One or more squares" for variable-size DTOs)
- [ ] Deactivate section has ONE method (test OR destruction OR impossible)
- [ ] Activate section with trigger condition (if applicable)
- [ ] All damaging abilities use power roll with tiered outcomes
- [ ] All damage has a type specified (fire, acid, poison, etc.) OR just "damage" for physical traps
- [ ] Potency checks use correct format: `[Characteristic] < [value] [condition]`
- [ ] Condition durations specified: (save ends), (EoT), or conditional
- [ ] No D&D terminology used (no "DC", "saving throw", dice notation)
- [ ] Keywords lowercase and valid
- [ ] Keywords match distance type (Melee keyword → Melee distance, Ranged keyword → Ranged distance)
- [ ] No damage types used as keywords (fire, cold, poison are NOT keywords)
- [ ] Hidden property included for traps/hazards that should be concealed
- [ ] Hidden section is simple (no discovery mechanics)
- [ ] Allied Awareness grants automatic benefits (not test-based abilities)
- [ ] Upgrade EV costs reasonable (+1 simple, +2 moderate, +3-4 major)

## Validation Script

Run validation on generated DTOs:

```bash
python .claude/skills/draw-steel-dto-generator/scripts/validate_dto.py output/filename.md
```

**Output interpretation:**
- **PASSED (✓):** All checks successful
- **ERRORS (❌):** Critical issues - fix before using
- **WARNINGS (⚠️):** Minor issues - review but acceptable

This is MANDATORY when generating DTOs - never skip validation.

## Cross-System Conversion

When converting traps/hazards from other systems:

**✅ DO:**
- Extract THEME and CONCEPT
- Take ability CONCEPTS and reimagine with Draw Steel mechanics
- Use appropriate damage type for theme

**❌ DO NOT:**
- Copy D&D mechanics (DC, saving throws, dice notation)
- Use D&D terminology
- Try to recreate exact D&D effects

**Example Conversion:**

D&D 5e Fireball Trap:
> "DC 15 Dexterity save, 8d6 fire damage on fail, half on success"

Draw Steel DTO:
```
> ❗️ Fireball Trap
> | Area, Magic | Free triggered action |
> | 📏 4 cube within 5 | 🎯 Each creature in the area |
> Power Roll + 2:
> - ≤11: 5 fire damage
> - 12-16: 8 fire damage; A < 1 dazed (EoT)
> - 17+: 11 fire damage; A < 2 dazed (EoT)
```

## Foundry VTT Object Actor JSON Schema

### Output Workflow

**CRITICAL: All formats require internal Foundry JSON generation and validation.**

1. Generate Foundry Object actor JSON internally
2. Run validation: `python .claude/skills/draw-steel-dto-generator/scripts/validate_dto_json.py output/filename.json`
3. Convert validated JSON to requested format(s)
4. Display validation results to user
5. Return output

### Core Object Actor Structure

```json
{
  "name": "Bear Trap",
  "type": "object",
  "img": "systems/draw-steel/assets/roles/ambusher.webp",
  "system": {
    "stamina": { "value": 6, "max": 6, "temporary": 0 },
    "characteristics": {
      "might": { "value": 0, "banes": 0, "edges": 0 },
      "agility": { "value": 0, "banes": 0, "edges": 0 },
      "reason": { "value": 0, "banes": 0, "edges": 0 },
      "intuition": { "value": 0, "banes": 0, "edges": 0 },
      "presence": { "value": 0, "banes": 0, "edges": 0 }
    },
    "combat": {
      "save": { "threshold": 6, "bonus": "" },
      "size": { "value": 1, "letter": "S" },
      "stability": 0,
      "turns": 0
    },
    "movement": null,
    "damage": {
      "immunities": { "all": 0 },
      "weaknesses": {}
    },
    "statuses": { "canFlank": false },
    "biography": { "value": "", "director": "" },
    "source": { "book": "Dynamic Terrain", "page": "", "license": "Draw Steel Creator License" },
    "object": {
      "level": 1,
      "category": "trap",
      "role": "ambusher",
      "area": null,
      "squareStamina": false
    }
  },
  "prototypeToken": {
    "name": "Bear Trap",
    "displayName": 20,
    "displayBars": 20,
    "bar1": { "attribute": "stamina" },
    "width": 1,
    "height": 1,
    "disposition": -1,
    "texture": { "src": "systems/draw-steel/assets/roles/ambusher.webp" }
  },
  "items": [],
  "_stats": { "systemId": "draw-steel", "systemVersion": "0.10.0" },
  "_id": "I2HA61b5E3GHnHTH"
}
```

## _ID Format (Critical)

All `_id` fields must match `^[a-zA-Z0-9]{16}$` (exactly 16 alphanumeric chars).

**CRITICAL: All IDs must be UNIQUE within the same DTO.** This includes:
- The actor's `_id`
- Each item/ability's `_id`
- Each effect's `_id` inside `system.power.effects`

**⚠️ NEVER reuse the same ID for multiple entities:**
```json
// WRONG - same ID used for actor, ability, AND effect:
"_id": "Feu32e27L0EEvSda"           // Actor
...
{
  "_id": "Feu32e27L0EEvSda",        // Ability - DUPLICATE!
  "system": { "power": { "effects": {
    "Feu32e27L0EEvSda": {           // Effect - TRIPLE DUPLICATE!
      "_id": "Feu32e27L0EEvSda",
      ...
    }
  }}}
}
```

**✅ CORRECT - every ID is unique:**
```json
{
  "_id": "I2HA61b5E3GHnHTH",        // Actor ID
  "items": [
    {
      "_id": "XyPJJOU0fiU8VyHl",    // Ability 1 ID (unique)
      "system": { "power": { "effects": {
        "le5j4jZ6dJLk4UuE": {       // Effect ID (unique)
          "_id": "le5j4jZ6dJLk4UuE",
          ...
        }
      }}}
    },
    {
      "_id": "PdL6EvIAV8xSMb3m"     // Ability 2 ID (unique)
    }
  ]
}
```

**Workflow: Generate ALL IDs upfront, then assign them sequentially.**

```bash
# Calculate needed IDs:
# 1 actor + 3 abilities + 5 effects = 9 IDs
python scripts/generate_foundry_ids.py --count 9

# Assign in order:
# ID[0] = actor._id
# ID[1] = items[0]._id
# ID[2] = items[0].system.power.effects[effect_key]._id
# ID[3] = items[1]._id
# ...and so on
```

**Use the ID generator script to avoid errors:**

```bash
# Generate 1 ID (for actor)
python scripts/generate_foundry_ids.py

# Generate 5 IDs (for DTO abilities)
python scripts/generate_foundry_ids.py --count 5
```

**Example workflow:**
```bash
# 1. Generate IDs for your DTO
python scripts/generate_foundry_ids.py --count 5
# Output:
# aB2c3D4e5F6G7890
# mK9jn2Lp4Qr6St8u
# vX1yZ3w5A7b9C0dE
# fG2hI4j6K8lM0nO2
# pQ4rS6tU8vW0xY2z

# 2. Use these IDs in your JSON
"_id": "aB2c3D4e5F6G7890"  # Actor ID
"_id": "mK9jn2Lp4Qr6St8u"  # Ability 1 ID
"_id": "vX1yZ3w5A7b9C0dE"  # Ability 2 ID
```

**Manual generation is error-prone and discouraged.** Common errors:
- Wrong length (15 or 17 characters instead of 16)
- Including dashes (UUID format like `a1b2c3d4-e5f6-7890-abcd`)
- Using placeholder text like "BearTrapObject001"
- **Generating duplicate IDs within the same DTO ← THIS CAUSES VALIDATION FAILURES**

### Object Category Mapping

| DTO Category | Object Category |
|--------------|-----------------|
| Environmental Hazard | `hazard` |
| Fieldwork (Trap) | `trap` |
| Fieldwork (Fortification) | `fortification` |
| Mechanism (Trap) | `trap` |
| Mechanism (Trigger) | `trigger` |
| Mechanism (Fortification) | `fortification` |
| Siege Engine | `siegeEngine` |
| Power Fixture | `relic` |
| Supernatural Object | `relic` |

### Object Image Paths

**CRITICAL: Use role-based images, NOT category-specific paths.**

The Draw Steel system does NOT have category-specific icons (no `trap.svg`, `hazard.svg`, etc.). Use the role images from `assets/roles/`:

| DTO Role | Image Path |
|----------|------------|
| ambusher | `systems/draw-steel/assets/roles/ambusher.webp` |
| artillery | `systems/draw-steel/assets/roles/artillery.webp` |
| brute | `systems/draw-steel/assets/roles/brute.webp` |
| controller | `systems/draw-steel/assets/roles/controller.webp` |
| defender | `systems/draw-steel/assets/roles/defender.webp` |
| harrier | `systems/draw-steel/assets/roles/harrier.webp` |
| hexer | `systems/draw-steel/assets/roles/hexer.webp` |
| support | `systems/draw-steel/assets/roles/support.webp` |
| no role | `systems/draw-steel/assets/roles/minion.webp` |

**For DTOs without a role**, use `minion.webp` as a fallback.

```
❌ WRONG - These paths do NOT exist:
"img": "systems/draw-steel/assets/icons/svg/trap.svg"
"img": "systems/draw-steel/assets/icons/svg/hazard.svg"
"img": "systems/draw-steel/assets/icons/svg/fortification.svg"

✓ CORRECT - Use role-based images:
"img": "systems/draw-steel/assets/roles/ambusher.webp"
```

### Object Fields

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Always `"object"` for DTOs |
| `system.object.level` | integer | DTO level (1-5 typically) |
| `system.object.category` | string | One of: `hazard`, `trap`, `trigger`, `siegeEngine`, `relic`, `fortification` |
| `system.object.role` | string | Same roles as monsters: `ambusher`, `artillery`, `brute`, `controller`, `defender`, `harrier`, `hexer`, `mount`, `support`, or `""` |
| `system.object.area` | integer/null | Number of squares for multi-square DTOs |
| `system.object.squareStamina` | boolean | `true` if stamina is per-square |
| `system.movement` | null/object | `null` for static objects, object with movement for mobile |

### Static vs Mobile Objects

**Static Objects (most DTOs):**
```json
"movement": null
```

**Mobile Objects (e.g., mobile siege engines):**
```json
"movement": {
  "value": 3,
  "types": ["walk"],
  "hover": false,
  "disengage": 0
}
```

### Object Stamina Patterns

**Fixed Stamina:**
```json
"stamina": { "value": 6, "max": 6, "temporary": 0 },
"object": {
  "area": null,
  "squareStamina": false
}
```

**Per-Square Stamina:**
```json
"stamina": { "value": 3, "max": 3, "temporary": 0 },
"object": {
  "area": 4,
  "squareStamina": true
}
```

**No Stamina (indestructible):**
```json
"stamina": { "value": 0, "max": 0, "temporary": 0 },
"object": {
  "area": null,
  "squareStamina": false
}
```

### Damage Immunities & Weaknesses

```json
"damage": {
  "immunities": {
    "all": 0,
    "poison": 0,
    "acid": 0,
    "cold": 0,
    "corruption": 0,
    "fire": 0,
    "holy": 0,
    "lightning": 0,
    "psychic": 0,
    "sonic": 0
  },
  "weaknesses": { "all": 0, "cold": 5 }
}
```

#### Numeric Values Explained

**Official Rule:** "Damage immunity often has a value associated with it... Whenever a target with damage immunity takes damage of the indicated type, they can reduce the damage by the value of the immunity (to a minimum of 0 damage)."

**Immunities:**
- **0** = No immunity (takes full damage from this type)
- **Numeric value** = Reduces damage by that amount (e.g., `"poison": 7` reduces poison damage by 7)
- **1000** = Total immunity (Foundry VTT pattern for complete immunity)
- For DTOs, set value to DTO's level or a thematic amount

**Example:** A DTO with `"fire": 5` takes 10 fire damage → reduced to 5 damage. If it takes 4 fire damage → reduced to 0.

**Total Immunity:** Use `"psychic": 1000` (or similar high value) for complete immunity. This is appropriate for inanimate objects that cannot be affected by certain damage types at all.

**Weaknesses:**
- **0** = No weakness to this damage type
- **Numeric value** = Extra damage dealt TO the DTO when hit with this type

**Example:** `"cold": 5` means cold attacks deal +5 damage against this DTO.

**CRITICAL: Always use numeric values, NOT booleans:**

```
❌ WRONG - Boolean values:
"immunities": {"poison": true, "psychic": true}

✓ CORRECT - Numeric values:
"immunities": {"poison": 1000, "psychic": 1000}  // Total immunity
"immunities": {"poison": 3, "psychic": 3}        // Partial reduction (level-based)
```

#### Immunity Patterns by DTO Type

| DTO Type | Common Immunities | Typical Value |
|----------|-------------------|---------------|
| **Inanimate Objects** | poison, psychic | 1000 (total immunity) |
| **Constructs/Mechanisms** | poison, psychic, corruption | 1000 (total immunity) |
| **Elemental Hazards** | their element | Level or 1000 |
| **Durable Objects** | physical types | Level-based |

**Example - Steam Pressure Vent (construct):**
```json
"immunities": {
  "all": 0,
  "poison": 1000,
  "psychic": 1000,
  "corruption": 1000
}
```

### Object Ability Structure

DTO abilities use the same structure as monster abilities:

```json
{
  "name": "Bear Trap",
  "type": "ability",
  "system": {
    "type": "freeTriggered",
    "category": "signature",
    "keywords": ["melee", "strike", "weapon"],
    "distance": { "type": "melee", "primary": 0 },
    "target": { "type": "creatureObject", "value": 1 },
    "damageDisplay": "melee",
    "power": {
      "roll": { "formula": "@chr", "characteristics": ["agility"] },
      "effects": {
        "XyPJJOU0fiU8VyHl": {
          "_id": "XyPJJOU0fiU8VyHl",
          "type": "damage",
          "damage": {
            "tier1": { "value": "1", "types": [], "properties": [] },
            "tier2": { "value": "3", "types": [], "properties": [] },
            "tier3": { "value": "5", "types": [], "properties": [] }
          }
        }
      }
    },
    "effect": { "before": "", "after": "<p>The bear trap must be manually reset.</p>" },
    "spend": { "text": "", "value": null },
    "source": { "book": "Dynamic Terrain", "license": "Draw Steel Creator License" }
  },
  "_id": "le5j4jZ6dJLk4UuE"
}
```

### Validation Script

Run before outputting with `--format foundry` or `--format both`:

```bash
python .claude/skills/draw-steel-dto-generator/scripts/validate_dto_json.py output/filename.json
```

**Output interpretation:**
- **PASSED (✓):** All checks successful
- **ERRORS (❌):** Critical issues - fix before importing
- **WARNINGS (⚠️):** Minor issues - review but acceptable

This is MANDATORY - never skip validation.

## Published Examples Reference

| DTO | Level | Category | Role | EV | Stamina |
|-----|-------|----------|------|-----|---------|
| Brambles | 1 | Hazard | Defender | 1/10×10 | 3/sq |
| Bear Trap | 1 | Fieldwork | Ambusher | 2 | 6 |
| Dart Trap | 1 | Mechanism | Ambusher | 1 | 3 |
| Pressure Plate | 1 | Mechanism | Support | 2 | - |
| Angry Beehive | 2 | Hazard | Hexer | 2 | 3 |
| Arrow Launcher | 2 | Siege Engine | Artillery | 8 | 30 |
| Field Ballista | 2 | Siege Engine | Artillery | 8 | 40 |
| Lava | 3 | Hazard | Hexer | 4/10×10 | 12/sq |
| Column of Blades | 3 | Mechanism | Defender | 3 | 5 |
| Catapult | 3 | Siege Engine | Artillery | 10 | 50 |
| Black Obelisk | 3 | Supernatural | Controller | 20 | 100 |
| Holy Idol | 5 | Power Fixture | Support | 7 | 35 |
| Tree of Might | 5 | Power Fixture | Hexer | 14 | 60 |
| Iron Dragon | 4 | Siege Engine | Artillery | 12 | 60 |
| Throne of A'An | 4 | Supernatural | Controller | 24 | 140 |
