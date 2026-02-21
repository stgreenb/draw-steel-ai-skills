---
name: draw-steel-retainer-generator
description: Generates Draw Steel TTRPG retainers (NPC followers) with formula-compliant stat blocks. Use when creating retainers, converting monsters to retainers, or designing NPC followers for the Draw Steel tabletop roleplaying game.
license: MIT
compatibility: Designed for Claude Code, Cursor, Gemini CLI, and Antigravity Google following the Agent Skills specification.
metadata:
  author: stgreenb
  version: "1.0"
---

# Draw Steel Retainer Generator

Generate Draw Steel TTRPG retainers that strictly conform to official MCDM stat block format from the Retainers chapter.

## Quick Start

**Input Format:** `"Create a [Level] [Retainer Name], [Role] [options]"`

**Examples:**
- `"Create a Level 1 Human Warrior, Defender"`
- `"Create a Level 5 Goblin Guide, Harrier"`
- `"Create a Level 3 Angulotl Hopper, Ambusher"`

**Output Formats:** `--format markdown` (default - Foundry VTT does not yet support retainers)

## Retainer Core Mechanics

### What is a Retainer?

Retainers are NPC followers who fight alongside heroes. They have distinct mechanics from monsters:

- **Mentor Relationship:** Each retainer is bound to a specific hero (their mentor)
- **Action Economy:** Retainers act on their mentor's turn - they get 1 move, 1 maneuver, and 1 main action
- **Recoveries:** Retainers have 6 recoveries (like heroes)
- **Death & Dying:** Retainers go dying at 0 Stamina and die at negative half their maximum Stamina
- **Surge Sharing:** Retainers share surges with their mentor - when the retainer spends a surge, the mentor loses one

### Mentor Relationship

- The retainer is bound to one specific hero (the mentor)
- Retainers act on their mentor's turn
- Abilities may reference "the retainer's mentor" or "adjacent to mentor"
- Positioning near mentor can provide bonuses (edges, cover, etc.)

### Action Economy

Retainers receive these actions each turn:
- **1 Move:** Standard movement
- **1 Maneuver:** Doesn't consume main action
- **1 Main Action:** Primary ability use

## Retainer Advancement Formulas

### Stamina Formula

```
Stamina = 21 + (9 × (Level - 1))
```

| Level | Stamina |
|-------|---------|
| 1 | 21 |
| 2 | 30 |
| 3 | 39 |
| 4 | 48 |
| 5 | 57 |
| 6 | 66 |
| 7 | 75 |
| 8 | 84 |
| 9 | 93 |
| 10 | 102 |

### Free Strike Damage Progression

Free strike is assigned thematically based on creature concept - there is NO fixed formula.

**Level 1 Typical Range:** 2-3
- 2 is most common
- 3 for martial types (Brute, Defender)

**Advancement Table Bonuses:** +2 at levels 3, 6, 9

| Level | Free Strike Bonus |
|-------|-------------------|
| 1-2 | Base (2-3) |
| 3-5 | Base + 2 |
| 6-8 | Base + 4 |
| 9-10 | Base + 6 |

**Role Guidance:**
- Brutes: Higher free strike
- Artillery/Controllers: Lower free strike at same level

### Characteristic Increases

Characteristics increase at levels 2, 5, and 8.

| Level | Characteristic Change | Max Characteristic |
|-------|----------------------|-------------------|
| 2 | +1 to one characteristic | +2 |
| 5 | +1 to all characteristics | +3 |
| 8 | +1 to one characteristic | +4 |

### Advancement Abilities

Retainers gain special abilities at levels 4, 7, and 10 based on their role.

### Retainer Advancement Table

| Level | Stamina | Free Strike Bonus | Characteristic Increase | Advancement Ability |
|-------|---------|-------------------|------------------------|---------------------|
| 1 | 21 | — | — | — |
| 2 | 30 | — | +1 to one (max +2) | — |
| 3 | 39 | +2 | — | — |
| 4 | 48 | — | — | Role ability (L4) |
| 5 | 57 | — | +1 to all (max +3) | — |
| 6 | 66 | +2 | — | — |
| 7 | 75 | — | — | Role ability (L7) |
| 8 | 84 | — | +1 to one (max +4) | — |
| 9 | 93 | +2 | — | — |
| 10 | 102 | — | — | Role ability (L10) |

## Signature Ability Rules

### What is a Signature Ability?

The signature ability is the retainer's primary combat ability. Every retainer MUST have exactly one signature ability.

**Format:**
- Name includes "(Signature Ability)" suffix
- Uses "Power Roll + highest characteristic"
- Has tier outcomes (≤11, 12-16, 17+)

### Signature Ability Damage Scaling

**Level 1 Base Damage Patterns:**
- Pattern A: 3/5/7 (tier 1/2/3)
- Pattern B: 4/7/10 (tier 1/2/3)

**Damage Scaling from Advancement Table:**
- Tier 1: +1 damage every 2nd level
- Tier 2/3: +1 damage every level

**Example Level 5 Signature:**
- Base (L1): 3/5/7
- L5 scaling: Tier 1 +2, Tier 2 +4, Tier 3 +4
- L5 total: 5/9/11

### Signature Ability Format

```markdown
> 🗡 **Ability Name (Signature Ability)**
> 
> **Melee 1** • **One creature**
> 
> Power Roll + highest characteristic:
> - **≤11:** 3 damage
> - **12-16:** 5 damage
> - **17+:** 7 damage
```

## Encounter Abilities

### Encounter Keyword

Some retainer abilities have the **Encounter** keyword, meaning they can only be used once per encounter.

### Recovery After Victory

Encounter abilities are recovered when the retainer's mentor earns a Victory.

### Encounter Ability Format

```markdown
> 🗡 **Ability Name (Encounter)**
> 
> **Ranged 5** • **One creature**
> 
> Power Roll + highest characteristic:
> - **≤11:** 4 damage
> - **12-16:** 7 damage
> - **17+:** 10 damage
```

## Role Advancement Abilities

Retainers gain special abilities at levels 4, 7, and 10 based on their role.

### Ambusher

| Level | Ability Name |
|-------|-------------|
| 4 | Go for the Jugular |
| 7 | Hamstring Slice |
| 10 | Hold 'Em Down |

### Artillery

| Level | Ability Name |
|-------|-------------|
| 4 | Supporting Volley |
| 7 | Line 'Em Up |
| 10 | Ricochet Shot |

### Brute

| Level | Ability Name |
|-------|-------------|
| 4 | Big Windup |
| 7 | Overhand Swat |
| 10 | Dizzying Sweep |

### Controller

| Level | Ability Name |
|-------|-------------|
| 4 | Elemental Blast |
| 7 | Oil Slick |
| 10 | Shattering Shards |

### Defender

| Level | Ability Name |
|-------|-------------|
| 4 | Watch Out! |
| 7 | It's Me You Want! |
| 10 | Last Stand |

### Harrier

| Level | Ability Name |
|-------|-------------|
| 4 | Tackle |
| 7 | Meet You There |
| 10 | Nab and Stab |

### Hexer

| Level | Ability Name |
|-------|-------------|
| 4 | Backfire Curse |
| 7 | Take Root |
| 10 | Mazed |

### Mount

| Level | Ability Name |
|-------|-------------|
| 4 | Cavalry Charge |
| 7 | Giddyup! |
| 10 | Rearing Trample |

### Support

| Level | Ability Name |
|-------|-------------|
| 4 | Battlefield Medic |
| 7 | Focus Fire |
| 10 | Back from the Dead |

### Magic/Psionic Keyword Swapping

In role advancement abilities:
- **Magic** keyword can be swapped for **Psionic**
- **Psionic** keyword can be swapped for **Magic**
- Keywords can be removed if effects are achieved through gadgetry or martial means

## Custom Retainer Creation

### Converting Monsters to Retainers

You can create custom retainers by converting existing monsters.

### Restrictions

**CANNOT be converted:**
- Minion monsters
- Leader monsters
- Solo monsters

### Conversion Rules

1. **Area/Multi-target abilities:** Convert to single target only
2. **No malice abilities:** Retainers don't have malice
3. **Use retainer stamina formula:** Replace monster stamina with retainer formula
4. **Assign appropriate role:** Match monster's combat style
5. **Create unique abilities:** Don't copy monster abilities directly

### Custom Retainer Example

**Original:** Level 3 Wolf (Platoon Harrier)
**Converted:** Level 3 Wolf Companion (Harrier Retainer)
- Stamina: Use retainer formula (39)
- Signature: Single-target bite (not pack tactics)
- Role abilities: Harrier advancement abilities

## Stat Block Format

### Markdown Stat Block Structure

```markdown
## Retainer Name

**Keywords** • Level X [Role]

|  |  |
|---|---|
| **1M** Size<br/> 5 Speed | 21 Stamina<br/> 2 Stability<br/> 2 Free Strike |
| **—** Immunity<br/> **—** Movement<br/> **—** With Captain<br/> **—** Weakness | **+2** Might<br/> **+1** Agility<br/> **−1** Reason<br/> **+1** Intuition<br/> **−1** Presence |

> 🗡 **Signature Ability Name (Signature Ability)**
> 
> [Distance] • [Target]
> 
> Power Roll + highest characteristic:
> - **≤11:** [Tier 1 effect]
> - **12-16:** [Tier 2 effect]
> - **17+:** [Tier 3 effect]

> ⭐️ **Trait Name**
> 
> [Trait description]

> 🗡 **Other Ability Name**
> 
> [Distance] • [Target]
> 
> [Ability description]
```

### Header Row

Contains: Keywords, Level, Role, EV

**EV Field:** Shows "—" for standard retainers

### Stats Row

Contains: Size, Speed, Stamina, Stability, Free Strike

**Size Notation:**
- 1M: Medium humanoid (most common)
- 1S: Small creature
- 1L: Large creature
- 2: Huge creature

**Speed by Role/Creature:**
- Standard: 5 (base humanoid)
- Fast: 6-7 (agile creatures, Harriers)
- Very Fast: 8 (maximum typical)
- Special: Fly, Swim, Climb, Burrow

### Defenses Row

Contains: Immunities, Movement types, With Captain, Weaknesses

**Immunities:** Thematic (devil → fire, undead → poison/corruption)
**With Captain:** Always "—" for retainers (unlike minions)
**Weaknesses:** Thematic or "—"

### Characteristics Row

Contains: Might, Agility, Reason, Intuition, Presence

**Characteristic Patterns by Role:**
- Physical roles (Brute, Defender, Harrier): Higher Might/Agility
- Caster roles (Hexer, Controller): Higher Reason/Intuition/Presence
- Support role: Distributed based on theme

**Typical Level 1 Range:** -1 to +2

### Ability Block Format

Abilities use blockquote format with icons:

| Icon | Ability Type |
|------|-------------|
| 🗡 | Melee strike abilities |
| 🏹 | Ranged strike abilities |
| ⚔️ | Melee or ranged abilities |
| 🔳 | Area abilities |
| ❗️ | Triggered actions |
| 👤 | Self/utility abilities |
| ⭐️ | Traits (passive) |

## Published Retainer Examples

### Angulotl Hopper (Level 1 Harrier)

```markdown
## Angulotl Hopper

**Angulotl, Humanoid** • Level 1 Harrier Retainer

|  |  |
|---|---|
| **1S** Size<br/> 6 Speed | 21 Stamina<br/> 0 Stability<br/> 2 Free Strike |
| **Poison 2** Immunity<br/> **Climb, swim** Movement<br/> **—** With Captain<br/> **—** Weakness | **+1** Might<br/> **+2** Agility<br/> **0** Reason<br/> **0** Intuition<br/> **0** Presence |

> 🗡 **Leapfrog (Signature Ability)**
> 
> **Melee 1** • **One creature or object**
> 
> Power Roll + highest characteristic:
> - **≤11:** 3 damage
> - **12-16:** 5 damage
> - **17+:** 7 damage
> 
> **Effect:** Before or after making this strike, the hopper jumps up to 2 squares, or up to 4 squares if they jump over their mentor's space.

> ⭐️ **Toxiferous**
> 
> Whenever an adjacent enemy grabs the hopper or uses a melee ability against them, that enemy takes 3 poison damage.
```

### Goblin Guide (Level 1 Harrier)

```markdown
## Goblin Guide

**Goblin, Humanoid** • Level 1 Harrier Retainer

|  |  |
|---|---|
| **1S** Size<br/> 5 Speed | 21 Stamina<br/> 0 Stability<br/> 2 Free Strike |
| **—** Immunity<br/> **Climb** Movement<br/> **—** With Captain<br/> **—** Weakness | **−1** Might<br/> **+1** Agility<br/> **0** Reason<br/> **0** Intuition<br/> **+1** Presence |

> 🗡 **Stabbity Stab (Signature Ability)**
> 
> **Melee 1** • **One creature or object**
> 
> Power Roll + highest characteristic:
> - **≤11:** 3 damage
> - **12-16:** 5 damage
> - **17+:** 7 damage
> 
> **Effect:** The target can't make opportunity attacks until the end of the guide's turn.

> ⭐️ **Crafty**
> 
> The guide doesn't provoke opportunity attacks by moving.
```

### Human Warrior (Level 1 Defender)

```markdown
## Human Warrior

**Human, Humanoid** • Level 1 Defender Retainer

|  |  |
|---|---|
| **1M** Size<br/> 5 Speed | 21 Stamina<br/> 0 Stability<br/> 2 Free Strike |
| **—** Immunity<br/> **—** Movement<br/> **—** With Captain<br/> **—** Weakness | **+2** Might<br/> **0** Agility<br/> **0** Reason<br/> **0** Intuition<br/> **+1** Presence |

> 🗡 **Chop (Signature Ability)**
> 
> **Melee 1** • **One creature or object**
> 
> Power Roll + highest characteristic:
> - **≤11:** 3 damage
> - **12-16:** 5 damage
> - **17+:** 7 damage
> 
> **Effect:** If the warrior is adjacent to their mentor, this ability gains an edge.

> ⭐️ **Supernatural Insight**
> 
> The warrior ignores concealment if it's granted by a supernatural effect.
```

## Cross-System Conversion

### D&D/PF2e Anti-Patterns (NEVER USE)

| D&D/PF2e Term | Draw Steel Approach | Never Use |
|---------------|---------------------|-----------|
| "hit points"/"HP" | Stamina | Use "stamina" |
| "armor class"/"AC" | — | Not used in Draw Steel |
| "saving throw" | Save | Use "save" not "saving throw" |
| "advantage"/"disadvantage" | Edge/Bane | D&D terminology |
| Dice notation (1d6, 2d8) | Fixed values | Use "5-6", "14-15" |
| "piercing", "slashing", "bludgeoning" | — | Invalid damage types |
| "necrotic", "radiant", "thunder" | — | Invalid damage types |
| "force" | — | Invalid damage type |
| "bonus action" | Maneuver | Use "maneuver" |
| "reaction" | Triggered action | Use "triggered action" |
| "short/long rest" | Respite | Use "respite" |

### Conversion Rules

**Inspiration Only - Do NOT copy mechanics directly:**

1. Extract THEME and CONCEPT
2. Use creature type for keywords
3. Reimagine abilities with Draw Steel mechanics
4. Calculate using Draw Steel formulas

### Dice to Fixed Value Conversion

| Dice | Fixed Value |
|------|-------------|
| 1d4 | 2-3 |
| 1d6 | 5-6 |
| 1d8 | 7-8 |
| 1d10 | 9-10 |
| 1d12 | 11-12 |
| 2d6 | 11-12 |
| 2d8 | 14-15 |
| 2d10 | 17-18 |

### Advantage/Disadvantage → Edge/Bane

- D&D "advantage" → Draw Steel "edge"
- D&D "disadvantage" → Draw Steel "bane"

### D&D Characteristics → Draw Steel

| D&D Stat | Draw Steel Characteristic |
|----------|--------------------------|
| Strength | Might |
| Dexterity | Agility |
| Intelligence | Reason |
| Wisdom | Intuition |
| Charisma | Presence |

## Valid Keywords Reference

> **When validating damage types or conditions:** `../shared/DRAW_STEEL_BASICS.md`

### Valid Creature Keywords

- abyssal, accursed, animal, beast, construct, dragon, elemental, fey, giant, horror, humanoid, infernal, plant, soulless, swarm, undead

### Valid Ability Keywords

- animal, animapathy, area, charge, chronopathy, cryokinesis, earth, fire, green, magic, melee, metamorphosis, psionic, pyrokinesis, ranged, resopathy, rot, performance, strike, telekinesis, telepathy, void, weapon

## Potency Notation

### Markdown Format

Use `<` notation for potency in markdown:

```
- **≤11:** 3 damage; M < 2 prone
- **12-16:** 5 damage; M < 3 prone
- **17+:** 7 damage; M < 4 prone
```

### Potency Levels

| Level | Formula | Example (Agility +3) |
|-------|---------|---------------------|
| WEAK | Characteristic - 2 | 1 |
| AVERAGE | Characteristic - 1 | 2 |
| STRONG | Characteristic | 3 |

### DC is Never Used

Draw Steel does NOT use DC (Difficulty Class). Always use potency notation.

## Fixed Damage Values

### Critical Rule

Draw Steel NEVER uses dice notation. Always use fixed values.

- ❌ WRONG: "1d6+3 damage"
- ✅ CORRECT: "6 damage"

### Damage Patterns

Signature ability damage follows predictable patterns based on level and tier.

## Validation

### Self-Validation Checklist

Before output, verify:

- [ ] Exactly one signature ability exists
- [ ] Signature ability has "(Signature Ability)" in name
- [ ] Power roll uses "highest characteristic" not specific characteristic
- [ ] Advancement abilities at levels 4, 7, 10 for appropriate levels
- [ ] Encounter abilities include "(Encounter)" in name
- [ ] Stamina matches formula: 21 + (9 × (Level - 1))
- [ ] Characteristics within bounds for level
- [ ] No D&D/PF2e terminology
- [ ] Damage types are valid Draw Steel types
- [ ] Conditions are valid Draw Steel conditions
- [ ] Ability keywords are lowercase and valid

### Stamina Validation

```
Expected Stamina = 21 + (9 × (Level - 1))
```

Verify calculated stamina matches expected.

### Characteristics Bounds

| Level | Max Characteristic |
|-------|-------------------|
| 1-4 | +2 |
| 5-7 | +3 |
| 8-10 | +4 |

### No D&D/PF2e Terminology

Scan for forbidden terms:
- hit points, HP, AC, saving throw
- advantage, disadvantage
- dice notation (d4, d6, d8, d20)
- invalid damage types (piercing, slashing, etc.)
- invalid conditions (stunned, paralyzed, etc.)

## Free Strike Values

### Assignment Rules

Free strike is assigned thematically based on creature concept, NOT by formula.

**Level 1 Guidelines:**
- Standard: 2 (most common)
- Martial/combat-focused: 3 (Brutes, some Defenders, Orc Charger)

**Advancement Bonuses:**
- Level 3: +2
- Level 6: +2
- Level 9: +2

### Role Guidance (Guidelines Only)

Free strike varies more by individual concept than by role:

| Role | Typical L1 Range | Notes |
|------|------------------|-------|
| Brute | 2-3 | Combat-focused often 3 |
| Defender | 2-3 | Varies by concept |
| Harrier | 2-3 | Orc Charger has 3, others 2 |
| Ambusher | 2 | Standard |
| Artillery | 2 | Standard |
| Controller | 2 | Standard |
| Hexer | 2 | Standard |
| Mount | 2-3 | Varies by creature type |
| Support | 2 | Standard |

## Stability Patterns by Role

Stability varies based on the retainer's individual concept, not just role. Use these as guidelines:

| Role | Stability Range | Notes |
|------|-----------------|-------|
| Defender | 0-4 | Shield-bearers tend toward 4, basic defenders may be 0 |
| Brute | 0-4 | Increases with level; L1 typically 0-2, L5+ often 2-4 |
| Artillery | 0-1 | Generally low stability |
| Hexer | 1-3 | Moderate based on casting theme |
| Harrier | 0 | Fast, mobile retainers |
| Ambusher | 0 | Light, stealthy retainers |
| Controller | 0 | Usually low stability |
| Mount | 0-4 | Varies by creature size/type |
| Support | 0 | Focus on abilities, not stability |

## Size Patterns

| Size | Notation | Use |
|------|----------|-----|
| Small | 1S | Halflings, goblins, small animals |
| Medium | 1M | Humans, elves, dwarves |
| Large | 1L | Minotaurs, bugbears, large animals |
| Huge | 2 | Giants, very large creatures |

## Speed Patterns

| Speed | Use |
|-------|-----|
| 5 | Standard humanoid |
| 6 | Agile creatures, some Harriers |
| 7 | Fast creatures, most Harriers |
| 8 | Very fast (maximum typical) |

**Special Movement:**
- Fly: Flying creatures
- Swim: Aquatic creatures
- Climb: Climbing creatures
- Burrow: Burrowing creatures

## Signature Ability Damage Patterns

### Level 1 Base Patterns

| Pattern | Tier 1 | Tier 2 | Tier 3 |
|---------|--------|--------|--------|
| A | 3 | 5 | 7 |
| B | 4 | 7 | 10 |

### Scaling Rules

- Tier 1: +1 every 2nd level
- Tier 2: +1 every level
- Tier 3: +1 every level

### Power Roll Format

Signature abilities always use:
```
Power Roll + highest characteristic:
```

Never specify a particular characteristic.

## Ability Count Patterns

### Standard Retainer

- 1 signature ability (required)
- 0-2 additional abilities
- Optional traits

### Trait Marking

Traits use ⭐️ symbol and don't consume actions:

```markdown
> ⭐️ **Trait Name**
> 
> [Trait description]
```

### Ability Types

| Type | Description |
|------|-------------|
| Main action | Primary combat abilities |
| Maneuver | Movement/utility (no main action) |
| Triggered action | Reactive abilities |
| Free triggered action | Immediate reactions |
| Trait | Passive/always-on |

## Immunity Patterns

### By Creature Type

| Type | Common Immunities |
|------|------------------|
| Devil | Fire |
| Undead | Poison, Corruption |
| Elemental | Matching element |
| Construct | Poison, Psychic |
| Humanoid | — (none) |

### Immunity Values

- Typically equals retainer level
- Or small fixed value (2-6)

## Movement Type Patterns

| Pattern | Notation |
|---------|----------|
| Ground only | — |
| Flying | Fly |
| Swimming | Swim |
| Climbing | Climb |
| Multiple | Climb, swim (comma-separated) |

## Characteristic Patterns by Role

### Physical Roles

**Brute:** High Might (+2), moderate Agility (+1), low mental stats
**Defender:** High Might (+2), moderate Agility (+1), moderate Presence (+1)
**Harrier:** High Agility (+2), moderate Might (+1), low mental stats

### Caster Roles

**Hexer:** High Intuition/Presence (+2), moderate Reason (+1), low physical
**Controller:** High Reason (+2), moderate Intuition (+1), low physical

### Other Roles

**Ambusher:** High Agility (+2), moderate Might (+1)
**Artillery:** Balanced Agility/Reason
**Mount:** High Might (+2), low mental
**Support:** Distributed based on theme

## Mentor Integration Patterns

### Abilities Benefiting Mentor

Abilities may reference the mentor:

```markdown
> ⭐️ **Protective Instinct**
> 
> While adjacent to their mentor, the retainer grants the mentor +2 stability.
```

### Triggered Abilities Involving Mentor

```markdown
> ❗️ **Guardian's Reflex**
> 
> **Trigger:** An enemy targets the retainer's mentor with an attack.
> **Effect:** The retainer shifts up to 2 squares to become adjacent to the mentor.
```

### Positioning Bonuses

Common when adjacent to mentor:
- Edge on abilities
- Cover bonuses
- Stability bonuses

## Create Unique Abilities

### Critical Rule

Each retainer should have unique, thematic abilities.

**✅ DO:**
- Create abilities fitting the retainer's theme
- Consider role, creature type, and concept
- Invent new names and effects
- Make abilities tell a story

**❌ DO NOT:**
- Copy published examples verbatim
- Use generic names ("Attack", "Strike")
- Copy D&D/PF2e mechanics

### Example

**Creating a Wolf Companion:**
- ❌ WRONG: Copy "Stinger Strike" renamed to "Bite"
- ✅ RIGHT: Create "Pack Hunter's Fang" with bleeding and isolation bonuses

## Power Roll Format

### Standard Format

```markdown
Power Roll + highest characteristic:
- **≤11:** [Tier 1 effect]
- **12-16:** [Tier 2 effect]
- **17+:** [Tier 3 effect]
```

### Advancement Abilities with Power Rolls

Same format, may have variable effects per tier:

```markdown
> 🗡 **Inspiring Word (Encounter)**
> 
> **Ranged 5** • **The retainer's mentor or one ally adjacent to the mentor**
> 
> Power Roll + Presence:
> - **≤11:** The target makes a save.
> - **12-16:** The target makes a save and gains 5 stamina.
> - **17+:** The target makes a save with an edge and gains 10 stamina.
```

## Ability Action Types

| Type | Description | Icon |
|------|-------------|------|
| Main action | Primary combat ability | 🗡 🏹 ⚔️ |
| Maneuver | Movement/utility | 🗡 |
| Triggered action | Reactive | ❗️ |
| Free triggered action | Immediate reaction | ❗️ |
| Trait | Passive | ⭐️ |

## Ability Distance Types

| Distance | Notation |
|----------|----------|
| Melee | Melee 1 (or higher for reach) |
| Ranged | Ranged X |
| Area burst | X burst |
| Area cube | X cube within Y |
| Line | X line |
| Self | Self |
| Special | Special or Self; See below |

## Ability Target Types

| Target | Notation |
|--------|----------|
| Single creature | One creature or object |
| Single creature only | One creature |
| Multiple | X creatures/objects |
| Area | Each enemy in the area |
| Self | Self |
| Mentor | The retainer's mentor |

## Stat Block Fields

### EV Field

Always shows "—" for standard retainers.

### With Captain Field

Always shows "—" for all retainers (unlike minions which have special bonuses).

Both fields appear in the defenses row of the stat block.

## Using Examples as Inspiration

**CRITICAL:** Published examples are templates only.

- ✅ Use for structure and format reference
- ❌ Do NOT copy abilities verbatim
- ✅ Create unique, thematic abilities for each retainer

## Self-Validation Checklist (Complete)

Run through all checks before output:

1. **Signature Ability**
   - [ ] Exactly one signature ability exists
   - [ ] Signature ability name includes "(Signature Ability)"
   - [ ] Power roll uses "highest characteristic" (not specific)

2. **Advancement Abilities**
   - [ ] L4+ retainers have appropriate role advancement ability
   - [ ] L7+ retainers have second advancement ability
   - [ ] L10 retainers have third advancement ability
   - [ ] Encounter abilities marked with "(Encounter)"

3. **Stamina & Stats**
   - [ ] Stamina matches formula: 21 + (9 × (Level - 1))
   - [ ] Characteristics within bounds for level
   - [ ] Stability appropriate for role
   - [ ] Speed appropriate for creature type

4. **Terminology**
   - [ ] No D&D/PF2e terminology
   - [ ] No dice notation (d4, d6, d8, d20)
   - [ ] Valid Draw Steel damage types
   - [ ] Valid Draw Steel conditions
   - [ ] Valid creature and ability keywords (lowercase)

5. **Stat Block Format**
   - [ ] Correct header format (Keywords • Level X Role)
   - [ ] Correct table structure
   - [ ] EV shows "—"
   - [ ] With Captain shows "—"
   - [ ] Ability icons used correctly
   - [ ] Traits marked with ⭐️
