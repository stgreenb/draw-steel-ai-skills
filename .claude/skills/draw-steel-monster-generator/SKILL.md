---
name: draw-steel-monster-generator
description: Generates Draw Steel TTRPG monsters with formula-compliant stat blocks. Use when creating monsters, calculating stats, or designing encounters for the Draw Steel tabletop roleplaying game.
license: MIT
compatibility: Designed for Claude Code, Cursor, Gemini CLI, and Antigravity Google following the Agent Skills specification.
metadata:
  author: stgreenb
  version: "1.0"
---

# Draw Steel Monster Generator

Generate Draw Steel TTRPG monsters that strictly conform to official MCDM stat block format from Monster Basics chapter.

## Quick Start

**Input Format:** `"Create a [Level] [Creature Name], [Organization], [Role] [options]"`

**Examples:**
- `"Create a Level 3 Gremlin, Minion Harrier"`
- `"Create a Level 5 Red Dragon, Solo Brute --format foundry"`
- `"Create a Level 8 Lich, Solo Hexer --format both"`

**Output Formats:** `--format markdown` (default), `--format foundry`, `--format both`

## Cross-System Monster Conversion

**CRITICAL WARNING:** When converting monsters from other systems (D&D 5e, Pathfinder, etc.), use the source monster for **INSPIRATION ONLY**. Do NOT create equivalents or try to recreate D&D/PF2e mechanics in Draw Steel.

### What This Means

**✅ DO (Inspiration Only):**
- Extract the THEME and CONCEPT (fire dragon, shadow assassin, undead warrior)
- Use creature type for keywords (dragon → dragon keyword, undead → undead keyword)
- Take ability CONCEPTS and reimagine them with Draw Steel mechanics (fire breath → area fire ability with Draw Steel formulas)
- Use the source monster's ROLE and LEVEL as a starting point

**❌ DO NOT (Never Create Equivalents):**
- Copy D&D/PF2e mechanics (flat-footed, advantage, saving throws, AC, etc.)
- Use D&D/PF2e terminology (hit points, proficiency, critical hit, etc.)
- Use dice notation (1d6, 2d8) - Draw Steel uses fixed damage values
- Use D&D/PF2e damage types (piercing, slashing, bludgeoning, necrotic, radiant, thunder, force)
- Try to recreate D&D/PF2e abilities - create NEW abilities that fit the theme

### Conversion Input Format

- `"Convert [Creature Name] from [System], [Level] [Organization] [Role]"`
- `"Convert [Creature Name]: [stat block/description] [options]"`

**Example:** `"Convert Scalathrax from Pathfinder 2e, Level 2 Elite Harrier --format foundry"`

### D&D/PF2e Anti-Patterns (NEVER USE)

| D&D/PF2e Term | Draw Steel Approach | Never Use |
|---------------|---------------------|-----------|
| "flat-footed" | - | Not a Draw Steel condition |
| "advantage"/"disadvantage" | Edge/Double Edge | D&D 5e terminology |
| "saving throw" | Save | Use "save" not "saving throw" |
| "hit points"/"HP" | Stamina | Use "stamina" not "hit points" |
| "armor class"/"AC" | - | Not used in Draw Steel |
| "proficiency bonus" | - | Not used in Draw Steel |
| "critical hit" | - | Draw Steel uses crits but doesn't name them |
| "multiple attack penalty" | Multiple action penalty | Draw Steel term |
| Dice notation (1d6, 2d8) | Fixed damage values | Use "6", "11", "14" not "1d6+3" |
| "piercing", "slashing", "bludgeoning" | - | Invalid damage types |
| "necrotic", "radiant", "thunder" | - | Invalid damage types |
| "force" | - | Invalid damage type (unless "forced movement") |

### Conversion Rules

**Extract from source (for inspiration):**
- Theme & creature type (fire dragon → fire keywords, dragon abilities)
- Ability concepts (fire breath → create NEW area fire ability with Draw Steel formulas)
- Damage types and malice features (use Draw Steel damage types only)

### Conversion Rules

**Extract from source (for inspiration):**
- Theme & creature type (fire dragon → fire keywords, dragon abilities)
- Ability concepts (fire breath → create NEW area fire ability with Draw Steel formulas)
- Damage types and malice features (use Draw Steel damage types only)

**Calculate using Draw Steel math:**
- **Stamina:** `ceil(((10 × Level) + Role_Stamina_Modifier) × Organization_Modifier)`
  - ⚠️ **Solo monsters:** Role Modifier **+30**, Org Modifier **×6** → L1 Solo: `ceil((10+30)×6) = 240`
  - ⚠️ **Leader monsters:** Role Modifier **+0**, Org Modifier **×2** → L2 Leader: `ceil((20+0)×2) = 40`
  - ⚠️ **Elite/Platoon/Horde/Minion:** See table below
- **EV:** `ceil(((2 × Level) + 4) × Organization_Modifier)`
- **Damage:** `ceil((4 + Level + Role_Damage_Modifier) × Tier_Modifier)` ← **NO organization modifier!**
- **Characteristics:** Based on echelon (Levels 1-2=+1, 3-4=+2, 5-6=+3, 7-8=+4, 9-10=+5)
- **Malice Features:** 2 for Elite/Leader, 3 for Solo (0 for Minion/Horde)

### Modifiers Quick Reference

| Organization | Org Modifier | Role (if not Solo/Leader) | Role Modifier | Damage Modifier |
|--------------|--------------|---------------------------|---------------|-----------------|
| Solo | ×6 | `"solo"` or `""` | +30 | +2 |
| Leader | ×2 | `"leader"` or `""` | +30 | +1 |
| Elite | ×2 | Any role | See below | +1 (stacks with role) |
| Platoon | ×1 | Any role | See below | +0 or +1 |
| Horde | ×0.5 | Any role | See below | +0 or +1 |
| Minion | ×0.5 | Any role | See below | +0 or +1 |

**Stamina Formula Examples:**
- L1 Solo: `ceil((10+30)×6) = 240`
- L2 Leader: `ceil((20+30)×2) = 100`
- L5 Elite Brute: `ceil((50+30)×2) = 160`
- L3 Platoon Harrier: `ceil((30+20)×1) = 50`
- L1 Horde Controller: `ceil((10+10)×0.5) = 10`
- L2 Minion Brute: `ceil((20+30)×0.5) = 25`

**CRITICAL - Damage Calculation:** The Organization Modifier (×6 for Solo, ×2 for Elite/Leader) is used ONLY for EV and Stamina, NOT for damage! Solo monsters get their damage boost from the Solo damage modifier (+2), not from multiplying by 6.

**Never copy:**
- HP, damage, attack bonuses from source systems
- Ability mechanics directly
- CR/level or AC/saves references
- D&D/PF2e terminology, mechanics, or damage types

## Output Workflow

**CRITICAL: All formats require internal Foundry JSON generation and validation.**

### Process (All Formats)

1. Generate Foundry JSON internally
2. Run validation: `python .claude/skills/draw-steel-monster-generator/scripts/validate_foundry_json.py output/filename.json`
3. Convert validated JSON to requested format(s)
4. Display validation results to user
5. Return output

### Validation Results Format

Display one of:
```
**Validation: ✓ Passed** - All checks successful
**Validation found [N] error(s):** - CRITICAL issues (use --format foundry for details)
**Validation found [N] warning(s):** - Minor issues (acceptable but review)
```

For markdown format with errors:
```
**Validation found 1 error:**
- ❌ Invalid keyword "piercing" in ability keywords

The monster stat block is provided below. For detailed error information including line numbers and field names, use --format foundry.

[Markdown stat block here]
```

## Foundry VTT JSON Schema

### Core Actor Structure

```json
{
  "name": "MonsterName",
  "type": "npc",
  "img": "systems/draw-steel/assets/roles/brute.webp",
  "system": {
    "stamina": { "value": 50, "max": 50, "temporary": 0 },
    "characteristics": {
      "might": { "value": 2 },
      "agility": { "value": 1 },
      "reason": { "value": -1 },
      "intuition": { "value": 1 },
      "presence": { "value": -1 }
    },
    "combat": {
      "save": { "threshold": 6, "bonus": "" },
      "size": { "value": 1, "letter": "L" },
      "stability": 0,
      "turns": 1
    },
    "movement": {
      "value": 7,
      "types": ["fly"],
      "hover": false,
      "disengage": 1
    },
    "damage": {
      "immunities": { "all": 0, "poison": 0, "acid": 0, "cold": 0, "corruption": 0, "fire": 0, "holy": 0, "lightning": 0, "psychic": 0, "sonic": 0 },
      "weaknesses": { "all": 0 }
    },
    "biography": { "value": "", "director": "", "languages": [] },
    "source": { "book": "Monsters", "page": "", "license": "Draw Steel Creator License" },
    "negotiation": { "interest": 5, "patience": 5, "motivations": [], "pitfalls": [], "impression": 1 },
    "monster": {
      "freeStrike": 6,
      "keywords": ["Beast", "Animal"],
      "level": 2,
      "ev": 8,
      "role": "brute",
      "organization": "platoon"
    }
  },
  "prototypeToken": {
    "name": "MonsterName",
    "displayName": 20,
    "displayBars": 20,
    "bar1": { "attribute": "stamina" },
    "width": 1,
    "height": 1,
    "disposition": -1,
    "texture": { "src": "systems/draw-steel/assets/roles/brute.webp" }
  },
  "items": [
    {
      "name": "Strike Ability",
      "type": "ability",
      "system": {
        "type": "main",
        "category": "signature",
        "keywords": ["melee", "strike", "weapon"],
        "distance": { "type": "melee", "primary": 1 },
        "target": { "type": "creatureObject", "value": 1 },
        "damageDisplay": "melee",
        "power": {
          "roll": { "formula": "@chr", "characteristics": ["agility"] },
          "effects": {
            "aB3c4D5e6F7g8H9i": {
              "_id": "aB3c4D5e6F7g8H9i",
              "type": "damage",
              "name": "",
              "img": null,
              "damage": {
                "tier1": { "value": "6", "types": ["poison"], "properties": [], "potency": { "value": "@potency.weak", "characteristic": "agility" } },
                "tier2": { "value": "11", "types": ["poison"], "properties": [], "potency": { "value": "@potency.average", "characteristic": "" } },
                "tier3": { "value": "14", "types": ["poison"], "properties": [], "potency": { "value": "@potency.strong", "characteristic": "" } }
              }
            }
          }
        },
        "effect": { "before": "", "after": "<p>You shift up to 2 squares.</p>" },
        "spend": { "text": "", "value": null },
        "source": { "book": "Monsters", "license": "Draw Steel Creator License" },
        "_dsid": "strike-ability",
        "story": "",
        "resource": null,
        "trigger": ""
      },
      "_id": "a1B2c3D4e5F67890",
      "effects": [],
      "ownership": { "default": 0 }
    }
  ],
  "_stats": { "systemId": "draw-steel", "systemVersion": "0.9.0" },
  "_id": "sJhjuVdliz3ThjEa"
}
```

### Ability Type Reference

| Type | When to Use | Example |
|------|-------------|---------|
| **main** | Standard attacks, signature actions | Spear Charge, Power Strike |
| **maneuver** | Movement/positioning (doesn't consume main action) | Wing Buffet, Reposition |
| **freeTriggered** | Immediate defensive reactions | Zephyr Feint, Counter |
| **none** | Custom abilities with unique rules | Piercing Cry, Special trap |
| **villain** | Solo/Leader only - 3 per monster, once per encounter, NO malice cost | Breath, Ultimate |

**Maneuver Recommendation:** Most non-minion creatures have at least one maneuver ability for movement/positioning effects (shifts, pushes, repositioning). Based on official Draw Steel monsters: Solo (100%), Leader (93.8%), Elite (80.6%), Horde/Platoon (~70%), Minion (13% - optional).

### Ability Categories

| Category | Usage | Limit |
|----------|-------|-------|
| **signature** | Primary ability (first ability ONLY) | Exactly 1 |
| **heroic** | Regular special abilities | Unlimited |
| **freeStrike** | Basic attack (usually signature) | 0-1 |
| **villain** | Ultimate abilities (Solo/Leader) - NO malice cost | 3 total |

**CRITICAL: Villain actions require BOTH type and category to be "villain":**
```json
{
  "type": "villain",
  "category": "villain",
  "resource": null,  // Villain actions NEVER cost malice
  "keywords": ["area", "magic"],
  ...
}
```

Solo and Leader monsters MUST have exactly 3 villain actions. These are special abilities used once per encounter at the end of any other creature's turn. **Villain actions do NOT cost malice** - they are separate from malice abilities.

**Villain Actions vs Malice Abilities:**
- **Villain Actions**: type="villain", category="villain", resource=null, 3 per Solo/Leader, once per encounter
- **Malice Abilities**: type varies (main/maneuver/none/triggered), category="heroic" or "none", resource=1-10, 2-3 per Elite/Leader, 3 per Solo

### Common Ability Patterns

#### Melee Strike (Default)
```json
"keywords": ["melee", "strike", "weapon"],
"distance": { "type": "melee", "primary": 1 },
"target": { "type": "creatureObject", "value": 1 },
"damageDisplay": "melee"
```

#### Area Damage (Breath/Spew)
```json
"keywords": ["area", "magic", "ranged"],
"distance": { "type": "cube", "primary": 3 },
"target": { "type": "creatureObject", "value": null, "custom": "Each creature in area" },
"damageDisplay": ""
```

#### Charge Attack
Add `"charge"` to keywords, include `"effect.after"` with movement text.

#### Condition/Effect Only (No Damage)
```json
"power": { "roll": { "formula": "@chr", "characteristics": [] }, "effects": {} },
"damageDisplay": ""
```

## Foundry VTT Rules (Critical Reference)

| DO | DON'T |
|----|-------|
| `characteristics.might.value` | `characteristics.might` alone |
| `stamina.value` and `stamina.max` | `hp` field |
| `combat.turns` (Solo=2, others=1) | Missing `combat` section |
| `power.effects` with structured damage objects | HTML power display in `effect.before` |
| `type: "main"` in system | Type as keyword like `["Main Action"]` |
| `systems/draw-steel/assets/roles/{role}.webp` | `modules/mcdm-monsters/...` paths |
| `prototypeToken` with `disposition: -1` | `token` instead of `prototypeToken` |
| `_stats.systemId: "draw-steel"` | Missing `_stats` section |
| `@potency.weak/average/strong` | `@potency.1/2/3` or plain numbers |
| Keywords lowercase: `["melee", "weapon"]` | Capitalized: `["Melee", "Weapon"]` |
| `formula: "@chr"` always | `formula: "@might"` or characteristic name |
| `_id` matches `^[a-zA-Z0-9]{16}$` | UUIDs with dashes |
| `distance: "burst"`, `"cube"`, `"line"` | `cone` (NOT valid in Draw Steel) |
| Valid role: `ambusher`, `artillery`, `brute`, `controller`, `defender`, `harrier`, `hexer`, `mount`, `support`, `solo` | Invalid role names |
| Valid org: `minion`, `horde`, `platoon`, `elite`, `leader`, `solo` | Invalid organization |
| Solo org + role: `"solo"` or `""` | Solo org + role: `"harrier"`, `"brute"`, etc. |
| Leader org + role: `"leader"` or `""` | Leader org + role: other role names |
| Valid monster keywords: `abyssal`, `accursed`, `animal`, `beast`, `construct`, `dragon`, `elemental`, `fey`, `giant`, `horror`, `humanoid`, `infernal`, `plant`, `soulless`, `swarm`, `undead` | Undefined keywords |
| Valid ability keywords: `animal`, `animapathy`, `area`, `charge`, `chronopathy`, `cryokinesis`, `earth`, `fire`, `green`, `magic`, `melee`, `metamorphosis`, `psionic`, `pyrokinesis`, `ranged`, `resopathy`, `rot`, `performance`, `strike`, `telekinesis`, `telepathy`, `void`, `weapon` | Invalid ability keywords |
| `spend` field in ALL abilities (even if empty) | Missing `spend` field |
| `resource: 3` (integer) for malice cost | `resource: {value: 3}` (object) |
| `damageDisplay: ""` for area abilities | `damageDisplay: "area"` (invalid) |
| `target: { "type": "creatureObject", "value": null }` for area | Lowercase `"creature"` for strikes |

## Valid Damage Types (CRITICAL!)

**ONLY these damage types are valid in Draw Steel Foundry VTT:**
- `acid`, `cold`, `corruption`, `fire`, `holy`, `lightning`, `poison`, `psychic`, `sonic`

**INVALID damage types (D&D terminology - will crash Foundry):**
- `physical`, `slashing`, `bludgeoning`, `piercing`, `force`, `necrotic`, `radiant`, `thunder`, `untyped`

**For untyped damage:** Use empty array `"types": []`

## Breath/Spew Keywords (CRITICAL)

**CRITICAL:** Breath weapons and spew abilities MUST use `["area", "magic"]` keywords, NOT damage type keywords like `"fire"` or `"poison"`. The damage type is specified in `power.effects`, not in `keywords`.

**Correct breath weapon example:**
```json
"keywords": ["area", "magic", "ranged"],
"distance": { "type": "cube", "primary": 3 },
"target": { "type": "creatureObject", "value": null, "custom": "Each creature in area" },
"power": {
  "effects": {
    "effect_id": {
      "type": "damage",
      "damage": {
        "tier1": { "value": "14", "types": ["fire"], "properties": [], "potency": { "value": "@potency.weak", "characteristic": "none" } }
      }
    }
  }
}
```

## Characteristics & Potencies (Quick Reference)

**Characteristics:** Range -5 to +5 representing natural abilities.
- **Echelon modifiers:** Levels 1-2=+1, 3-4=+2, 5-6=+3, 7-8=+4, 9-10=+5

**Potencies:** Effect strength based on target's characteristic.

| Tier | Potency Value | Roll Modifier |
|------|---------------|---------------|
| 1 (Weak) | `@potency.weak` | Characteristic − 2 |
| 2 (Average) | `@potency.average` | Characteristic − 1 |
| 3 (Strong) | `@potency.strong` | Characteristic (Leader/Solo +1) |

**Example:** Agility +3 target vs. poison weakness:
- Tier 1: Potency = 1 (fails if Agility < 1)
- Tier 2: Potency = 2 (fails if Agility < 2)
- Tier 3: Potency = 3 (fails if Agility < 3)

## _ID Format (Critical)

All `_id` fields must match `^[a-zA-Z0-9]{16}$` (exactly 16 alphanumeric chars).

**CRITICAL: All IDs must be UNIQUE within the same monster.** This includes:
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
# 1 actor + 8 abilities + 10 effects = 19 IDs
python scripts/generate_foundry_ids.py --count 19

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

# Generate 5 IDs (for monster abilities)
python scripts/generate_foundry_ids.py --count 5
```

**Example workflow:**
```bash
# 1. Generate IDs for your monster
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
- Using placeholder text like "monster-uuid"
- **Generating duplicate IDs within the same monster ← THIS CAUSES VALIDATION FAILURES**

## Power Roll Formula & Effects

**Formula:** Always use `"formula": "@chr"` - never use characteristic names directly.

```json
"power": {
  "roll": {
    "formula": "@chr",
    "characteristics": ["agility"]  // Which chars can power the roll
  },
  "effects": {
    // Structured damage/condition objects go here
  }
}
```

**Non-damaging abilities** (buffs, movement):
```json
"power": {
  "roll": { "formula": "@chr", "characteristics": [] },
  "effects": {}
}
```

## Effect Text with HTML

Use raw HTML tags in `effect.before` and `effect.after` (NOT encoded entities):

```json
// CORRECT:
"before": "<p>You push the target 2 squares.</p>"

// INCORRECT:
"before": "<p>You push &lt; 2 squares.</p>"
```

## Power Roll Effects Structure (CRITICAL)

Damage and conditions MUST be structured in `system.power.effects`, NOT as HTML in `effect.before`. Foundry VTT parses these for clickable buttons and automation.

**Damage effect example:**
```json
"aB3c4D5e6F7g8H9i": {
  "_id": "aB3c4D5e6F7g8H9i",
  "type": "damage",
  "name": "",
  "img": null,
  "damage": {
    "tier1": {
      "value": "6",
      "types": ["poison"],
      "properties": [],
      "potency": { "value": "@potency.weak", "characteristic": "agility" }
    },
    "tier2": {
      "value": "11",
      "types": ["poison"],
      "properties": [],
      "potency": { "value": "@potency.average", "characteristic": "" }
    },
    "tier3": {
      "value": "14",
      "types": ["poison"],
      "properties": [],
      "potency": { "value": "@potency.strong", "characteristic": "" }
    }
  }
}
```

**Applied condition example:**
```json
"jK9l8M7n6O5p4Q3r": {
  "_id": "jK9l8M7n6O5p4Q3r",
  "type": "applied",
  "name": "Slowed",
  "img": null,
  "applied": {
    "tier1": {
      "display": "{{potency}} slowed (save ends)",
      "potency": { "value": "-1", "characteristic": "agility" },
      "effects": {
        "slowed": { "condition": "failure", "end": "save", "properties": [] }
      }
    },
    "tier2": { /* ... */ },
    "tier3": { /* ... */ }
  }
}
```

## Movement & Combat Size

**Movement types by creature:**
- Flying creatures: `["fly"]`
- Walking creatures: `["walk"]`
- Amphibious: `["walk", "swim"]` or `["walk", "fly"]`
- Burrowing: `["walk", "burrow"]`
- Disengage: Always `1` unless specified (wasps have disengage 1)

**Combat size:**
```json
"combat": {
  "size": { "value": 1, "letter": "M" },
  "turns": 1  // Solo monsters: turns=2
}
```

| Size Value | Letter | Typical Use |
|-----------|--------|------------|
| 1 | S/M | Minion, Horde, Platoon, Elite, Leader |
| 3-5 | L | Solo monsters |

## Distance Type Values

| Ability Range | Configuration |
|---------------|---------------|
| Melee 1 | `{ "type": "melee", "primary": 1 }` |
| Ranged 5 | `{ "type": "ranged", "primary": 5 }` |
| 3 burst | `{ "type": "burst", "primary": 3 }` |
| Self | `{ "type": "self" }` |
| 5 line | `{ "type": "line", "primary": 5 }` |
| Wall | `{ "type": "wall", "primary": 5 }` |

## Target Type Values

| Target | Configuration |
|--------|---------------|
| Single creature | `{ "type": "creatureObject", "value": 1 }` |
| Area (all in range) | `{ "type": "creatureObject", "value": null, "custom": "Each enemy in area" }` |
| Self-target | `{ "type": "self" }` |

**Critical:** Self-target abilities should NOT have `"value": 1`:
```json
// CORRECT:
"target": { "type": "self" }

// INCORRECT:
"target": { "type": "self", "value": 1 }
```

## Damage Display & Spend Field

**damageDisplay valid values:**
- `"melee"` - for melee/strike abilities
- `"ranged"` - for ranged abilities
- `""` (empty) - for area, self-target, or non-damaging abilities

**Spend field (required for ALL abilities):**
```json
// No cost:
"spend": { "text": "", "value": null }

// Costs malice:
"spend": { "text": "Spend 3 Malice", "value": 3 }
```

## Resource Costs (Malice)

Elite, Leader, and Solo monsters MUST have at least one ability with `resource: integer > 0`:

```json
// CORRECT (costs 3 malice):
"resource": 3

// INCORRECT (use integer, not object):
"resource": { "value": 3 }

// No cost:
"resource": null
```

## Malice Cost Guidelines

**CRITICAL:** Malice costs represent game-changing abilities, NOT just damage boosts. Higher costs = more dramatic battlefield impact.

| Cost | Effect Type | Examples |
|------|-------------|----------|
| **1** | Quick, targeted effects | Small area (burst/cube 3) with movement, triggered reactions, size restrictions |
| **2** | Moderate control & resource manipulation | Opposed tests, steal stamina, swap positions, strong triggered abilities |
| **3** | Significant battlefield impact | Ally buffs (movement, free actions), free strikes with bonuses, defensive stances, teleport |
| **4** | Strong main actions | Potent main abilities, strong control effects, multiple conditions |
| **5** | MAJOR game-changing effects | **Solo Action** (extra main action, works if dazed), environment manipulation, split mechanics, strong auras |
| **7** | Encounter-wide effects | Map-wide environmental changes, multiple targets, permanent buffs, invisibility + movement |
| **10** | Ultimate abilities | Multiple areas (e.g., four 3-cubes within 10), massive impact on entire encounter |

**Key Principles:**
- **NEVER just add "more damage"** - malice must do something unique
- **Think about battlefield control**, not raw numbers
- **Solo Action appears in EVERY Solo monster** at cost 5
- **Environment manipulation** common at costs 5+
- **Map-wide effects** reserved for high costs (7+)

**Design Patterns:**
- **Cost 1-2**: Quick reactions, small areas, simple conditions
- **Cost 3-4**: Ally buffs, defensive stances, teleportation, free strikes
- **Cost 5**: Solo action, environment manipulation, split mechanics, strong auras
- **Cost 7**: Map-wide changes, permanent buffs, multi-part effects
- **Cost 10**: Ultimate abilities, multiple areas, encounter-altering effects

## Damage Immunities & Weaknesses

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
  "weaknesses": { "all": 0, "cold": 5, "fire": 3 }
}
```

## Valid Conditions (Draw Steel Only)

**ONLY these conditions are valid in Draw Steel:**
- `bleeding`, `dazed`, `frightened`, `grabbed`, `prone`, `restrained`, `slowed`, `taunted`, `weakened`

**Condition Duration Rules:**

| Condition | Type | How It Ends |
|-----------|------|-------------|
| **bleeding** | Persistent, ongoing | Until healed (triggers on action use) |
| **grabbed** | Conditional | Escape, release, or break adjacency |
| **prone** | Conditional | Stand up maneuver |
| **slowed** | Persistent | Until healed |
| **dazed** | Persistent | Until healed |
| **weakened** | Persistent | Until healed |
| **frightened** | Conditional | When source changes or is removed |
| **restrained** | Persistent | Until healed or escaped |

**CRITICAL:** Condition durations are applied by monster abilities, NOT part of the condition name itself.

## Self-Validation Checklist (Before Output)

- [ ] Actor `type` is `"npc"`
- [ ] All `_id` were generated using `scripts/generate_foundry_ids.py`
- [ ] All `_id` match `^[a-zA-Z0-9]{16}$` (16 chars)
- [ ] No duplicate `_id` values within the same monster (actor, items, AND effects must all have unique IDs)
- [ ] Exactly ONE ability has `category: "signature"`
- [ ] Monster role is valid (`ambusher`, `artillery`, `brute`, `controller`, `defender`, `harrier`, `hexer`, `mount`, `support`, `solo`)
- [ ] Monster organization is valid (`minion`, `horde`, `platoon`, `elite`, `leader`, `solo`)
- [ ] Role and organization are compatible (Solo org → role="solo" or ""; Leader org → role="leader" or "")
- [ ] Monster keywords are valid (lowercase from approved list)
- [ ] Ability keywords are valid (lowercase from approved list)
- [ ] Distance types are valid (`melee`, `ranged`, `burst`, `cube`, `line`, `self`, etc. - NOT `cone`)
- [ ] For minion organization: "With Captain" effect present
- [ ] For Elite/Leader/Solo: At least one ability with `resource: integer > 0`
- [ ] For Solo/Leader: At least one maneuver ability (type: "maneuver")
- [ ] For Elite/Horde/Platoon: Consider adding at least one maneuver (recommended but not required)
- [ ] All abilities have `spend` field
- [ ] `power.effects` contains structured objects (not empty) for signature/heroic/villain abilities
- [ ] `formula: "@chr"` used (never characteristic names)
- [ ] All required NPC system fields present (stamina, characteristics, combat, monster, etc.)
- [ ] Token config has `bar1.attribute: "stamina"`

## Using Examples as Inspiration

**CRITICAL:** Examples are templates only - create unique abilities for each monster.

- ✅ **DO:** Create "Rending Talons" with unique mechanics for a wolf
- ❌ **DON'T:** Copy "Stinger Strike" and rename to "Claw Strike"

Every monster should be distinct and thematic. Copying examples verbatim defeats the purpose and may break Foundry VTT imports.

## Create Unique Abilities

**CRITICAL:** Each monster should have unique, thematic abilities. Do NOT copy abilities from other monsters or source systems.

**✅ DO:**
- Create abilities that fit the monster's theme and concept
- Use Draw Steel mechanics and formulas
- Invent new ability names and effects
- Consider the monster's role and organization
- Make abilities that tell a story about the creature

**❌ DO NOT:**
- Copy abilities from examples (even with new names)
- Recreate D&D/PF2e abilities with Draw Steel stats
- Use generic ability names ("Melee Attack", "Fireball")
- Copy mechanics from source monster conversions
- Make every monster feel the same

**Example: Converting a D&D Red Dragon**
- ❌ **WRONG:** Copy "Fire Breath" with D&D mechanics (8d6 damage, Dexterity save for half)
- ✅ **RIGHT:** Create "Inferno Breath" with Draw Steel mechanics (cube 3, fire damage, tier-based values, Draw Steel conditions)

**Example: Creating a Wolf Monster**
- ❌ **WRONG:** Copy "Stinger Strike" and rename to "Bite Attack"
- ✅ **RIGHT:** Create "Pack Hunter's Fang" with unique mechanics (bleeding on hit, bonus against isolated targets)

## Validation Script

Run before outputting with `--format foundry` or `--format both`:

```bash
python .claude/skills/draw-steel-monster-generator/scripts/validate_foundry_json.py output/filename.json
```

**Output interpretation:**
- **PASSED (✓):** All checks successful
- **ERRORS (❌):** Critical issues - fix before importing
- **WARNINGS (⚠️):** Minor issues - review but acceptable

This is MANDATORY - never skip validation.
