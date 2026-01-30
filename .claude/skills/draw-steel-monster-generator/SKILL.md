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
- `"Convert Scalathrax from Pathfinder 2e, Level 2 Elite Harrier --format foundry"`

## Cross-System Monster Conversion

You can create Draw Steel monsters inspired by creatures from other game systems (D&D 5e, Pathfinder, etc.). **Important: NEVER use stats from other systems - only use them for creative inspiration.**

### Conversion Input Format

**Basic conversion:**
- `"Convert [Creature Name] from [System], [Level] [Organization] [Role]"`
- `"Convert [Creature Name], [Level] [Organization] [Role]"`

**Conversion with inspiration:**
- `"Convert [Creature Name]: [pasted stat block or description] [options]"`

**Examples:**
- `"Convert Ancient Red Dragon from D&D 5e, Level 8 Solo Brute"`
- `"Convert Beholder: [paste D&D beholder stat block] Level 7 Solo Controller"`
- `"Convert Lich from Pathfinder, Level 6 Solo Hexer --format both"`

### Conversion Rules (CRITICAL)

**DO:**
- Use creature name for theme/inspiration (fire dragon → fire keywords, dragon abilities)
- Extract creature type for keywords (undead, construct, aberration)
- Adapt ability concepts (fire breath → fire breath with Draw Steel damage)
- Apply Draw Steel formulas for ALL numerical stats

**DO NOT:**
- Use HP, damage, or attack bonuses from source systems
- Copy ability mechanics directly
- Use CR/level from source to determine Draw Steel level
- Reference source system mechanics (AC, saves, proficiency bonus)

### What Gets Extracted from Source Material

- **Theme:** Fire-breathing dragon → fire keywords and abilities
- **Creature type:** Undead lich → undead keyword, death magic theme
- **Ability concepts:** Fire breath → original fire breath ability using Draw Steel formulas
- **Damage types:** Acid monster → acid damage in abilities
- **Malice features:** For Elite/Leader/Solo organizations, generate 2-3 malice features inspired by creature theme

### What Is Calculated Using Draw Steel Math

- **Stamina:** `ceil(((10 × Level) + Role_Stamina_Modifier) × Organization_Modifier)`
- **EV:** `ceil(((2 × Level) + 4) × Organization_Modifier)`
- **Damage:** `ceil((4 + Level + Role_Damage_Modifier) × Tier_Modifier)`
- **Characteristics:** Based on echelon (Level 1=+1, 2-4=+2, 5-7=+3, 8-10=+4)
- **Free Strike:** Equal to Tier 1 damage
- **Malice Features:** 2 for Elite/Leader, 3 for Solo (0 for Minion/Horde, see Step 9)

### Output

Conversion produces standard Draw Steel stat blocks:
- Markdown format (default)
- Foundry VTT JSON (with `--format foundry` or `--format both`)
- Source noted as "Converted from [System]" in the stat block

### Conversion Example: Scalathrax

**Input:** `"Convert Scalathrax from Pathfinder 2e, Level 2 Elite Harrier --format foundry"`

**Conversion process:**
1. Extract theme: "slippery, scaly cave-dwelling horror with toxic oil"
2. Keywords: beast (scalathrax isn't a valid keyword, use beast)
3. Role: Harrier (mobile, hit-and-run tactics, climbing speed)
4. Apply Draw Steel formulas:
   - EV: ceil(((2×2)+4)×2.0) = 16
   - Stamina: ceil(((10×2)+20)×2.0) = 100
   - Damage T1: ceil((4+2+1)×0.6) = 5 → 7 with strike bonus
5. Generate malice features (2 for Elite):
   - Brutal Effectiveness (3 Malice): Increase next ability's potency
   - Quick Shift (5 Malice): Shift speed and gain bonus to next attack
6. Output Foundry VTT JSON with malice features as feature items

## Output Formats

The skill supports multiple output formats:

### Markdown (Default)
Standard Draw Steel stat block in Markdown format, suitable for documentation or manual use.

### Foundry VTT
Generates a JSON file compatible with Foundry VTT's Draw Steel system. Output includes:
- Complete NPC actor with all stats, characteristics, and combat properties
- Abilities as items with power roll effects
- Features and traits as passive items
- Role-based token images
- Solo Monster feature for solo creatures

### Both
Generates both Markdown stat block AND Foundry VTT JSON file.

### Format Options
Use the `--format` option to specify output format:
- `--format markdown` (default) - Standard Markdown stat block
- `--format foundry` - Foundry VTT JSON file
- `--format both` - Both Markdown and Foundry VTT

### Using Examples as Inspiration (IMPORTANT!)

**CRITICAL:** The examples in this skill are for **inspiration only**. Do NOT copy them verbatim!

When creating monster abilities and features:
- **Use unique names** that fit your creature's theme (not "Stinger Strike" unless it's actually a stinger)
- **Adapt mechanics** to match the creature's actual abilities
- **Vary damage types** and effects from examples
- **Consider the creature's keywords** when designing abilities
- **Create something unique** - don't just change the name and keep the same mechanics

**Why this matters:**
- Every monster should be distinct and thematic
- Copying examples verbatim defeats the purpose of generating unique monsters
- Foundry VTT will crash if you use invalid patterns from copied examples
- Your monsters will be more interesting and memorable

**Example:**
- ❌ **DON'T:** Copy "Stinger Strike" and just rename it to "Claw Strike"
- ✅ **DO:** Create "Rending Talons" with unique mechanics that fit a wolf's hunting style

### Foundry VTT Output Requires Validation (MANDATORY)

**For `--format foundry` or `--format both`, you MUST validate the JSON output.**

The validation script catches errors that will cause Foundry VTT import failures:
- Invalid monster/ability keywords
- Wrong `_id` format (must match `^[a-zA-Z0-9]{16}$`)
- Missing malice features for Elite/Leader/Solo monsters
- Invalid ability types or categories

**Run validation IMMEDIATELY after generating JSON:**
```bash
# From the ds-monster-generator project root:
python .claude/skills/draw-steel-monster-generator/scripts/validate_foundry_json.py output/filename.json
```

**Workflow:**
1. Generate JSON file in `output/` directory
2. Run validation script
3. Review output:
   - **ERRORS (❌):** Must fix before reporting success
   - **WARNINGS (⚠️):** Acceptable for official content
   - **PASSED (✓):** Validation successful
4. If errors exist, fix the JSON and re-run validation
5. **Only report completion when validation passes with no errors**

**Skipping validation is NOT acceptable.** If you cannot find or run the validation script, report the error rather than skipping validation.

## Foundry VTT JSON Schema (Required for --format foundry/both)

When generating Foundry VTT JSON, output a JSON object with this EXACT structure:

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
       "name": "Stinger Strike",
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
             },
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
                 "tier2": {
                   "display": "{{potency}} slowed (save ends)",
                   "potency": { "value": "0", "characteristic": "agility" },
                   "effects": {
                     "slowed": { "condition": "failure", "end": "save", "properties": [] }
                   }
                 },
                 "tier3": {
                   "display": "{{potency}} slowed (save ends)",
                   "potency": { "value": "1", "characteristic": "agility" },
                   "effects": {
                     "slowed": { "condition": "failure", "end": "save", "properties": [] }
                   }
                 }
               }
             }
           }
         },
         "effect": {
            "before": "",
            "after": "<p>You shift up to 2 squares.</p>"
          },
          "spend": {
            "text": "",
            "value": null
          },
          "source": { "book": "Monsters", "license": "Draw Steel Creator License" },
          "_dsid": "stinger-strike",
          "story": "",
          "resource": null,
          "trigger": ""
        },
       "_id": "a1B2c3D4e5F67890",  // Matches ^[a-zA-Z0-9]{16}$
       "effects": [],
       "ownership": { "default": 0 }
     }
   ],
  "_stats": { "systemId": "draw-steel", "systemVersion": "0.9.0" },
  "_id": "sJhjuVdliz3ThjEa"  // Matches ^[a-zA-Z0-9]{16}$, unique for each actor
}
```

**Charge Attack Example (optional "charge" keyword):**

```json
{
  "name": "Spear Charge",
  "type": "ability",
  "system": {
    "type": "main",
    "category": "signature",
    "keywords": ["charge", "melee", "strike", "weapon"],
    "distance": { "type": "melee", "primary": 1 },
    "target": { "type": "creatureObject", "value": 1 },
    "damageDisplay": "melee",
    "power": {
      "roll": { "formula": "@chr", "characteristics": ["agility"] },
      "effects": {
        "Y0x6xGOw9jHthmy2": {
          "type": "damage",
          "_id": "Y0x6xGOw9jHthmy2",
          "damage": {
            "tier1": {
              "value": "3",
              "types": [],
              "properties": [],
              "potency": { "value": "@potency.weak", "characteristic": "none" }
            },
            "tier2": {
              "value": "4",
              "types": [],
              "properties": [],
              "potency": { "value": "@potency.average", "characteristic": "" }
            },
            "tier3": {
              "value": "5",
              "types": [],
              "properties": [],
              "potency": { "value": "@potency.strong", "characteristic": "" }
            }
          }
        }
      }
    },
    "effect": {
      "before": "",
      "after": ""
    },
    "spend": {
      "text": "",
      "value": null
    },
    "source": { "book": "Monsters", "license": "Draw Steel Creator License" },
    "_dsid": "spear-charge",
    "story": "",
    "resource": null,
    "trigger": ""
  },
  "_id": "sPeArChArGe12Ab3C",
  "effects": [],
  "ownership": { "default": 0 }
}
```

**NOTE:** The "charge" keyword is optional - only include it for abilities that are actually charge-based (movement + attack in one action).

#### Breath Weapon Example (area/magic keywords, NOT damage types)

```json
{
  "name": "Corroding Breath",
  "type": "ability",
  "system": {
    "type": "main",
    "category": "signature",
    "keywords": ["area", "magic", "ranged"],
    "distance": { "type": "cube", "primary": 3 },
    "target": { "type": "creatureObject", "value": null, "custom": "Each creature and object in the area" },
    "damageDisplay": "",
    "power": {
      "roll": { "formula": "@chr", "characteristics": ["reason"] },
      "effects": {
        "jUXtXHkSkBIE3qfE": {
          "type": "damage",
          "_id": "jUXtXHkSkBIE3qfE",
          "damage": {
            "tier1": {
              "value": "14",
              "types": ["corruption"],
              "properties": [],
              "potency": { "value": "@potency.weak", "characteristic": "none" }
            },
            "tier2": {
              "value": "19",
              "types": ["corruption"],
              "properties": [],
              "potency": { "value": "@potency.average", "characteristic": "" }
            },
            "tier3": {
              "value": "23",
              "types": ["corruption"],
              "properties": [],
              "potency": { "value": "@potency.strong", "characteristic": "" }
            }
          }
        }
      }
    },
    "effect": {
      "before": "",
      "after": "<p>This ability gains an edge against targets the monster has previously dealt corrosion damage to.</p>"
    },
    "spend": {
      "text": "",
      "value": null
    },
    "source": { "book": "Monsters", "license": "Draw Steel Creator License" },
    "_dsid": "corroding-breath",
    "story": "",
    "resource": null,
    "trigger": ""
  },
  "_id": "cOrRoDiNgBrEaTh1A",
  "effects": [],
  "ownership": { "default": 0 }
}
```

**CRITICAL:** Breath weapons and spew abilities MUST use `["area", "magic"]` keywords, NOT damage type keywords like `"fire"` or `"poison"`. The damage type is specified in `power.effects`, not in `keywords`.

### Ability Type Variety

Different ability types serve different purposes. Use multiple types to create interesting monsters:

**Main:** Standard actions that consume the creature's main action
- Most common ability type
- Used for signature attacks and primary abilities

**Maneuver:** Movement or positioning abilities that don't consume the main action
- Used for repositioning, escaping, or controlling the battlefield
- Often includes area effects or movement keywords

**FreeTriggered:** Immediate reaction to triggers
- Used for defensive responses (e.g., when damaged, when adjacent)
- Does NOT consume main action
- Trigger field specifies when it can be used

**None:** Custom abilities with unique rules
- Used for abilities that don't fit standard action types
- Often has special distance or targeting

**Villain:** Special abilities for Solo/Leader only
- Exactly 3 per monster (opener, crowd control, ult)
- Can be used only once per encounter
- Used at end of any creature's turn
- See villain action guidance section above

### Foundry VTT Rules (CRITICAL - READ BEFORE GENERATING JSON)

| DO | DON'T |
|----|-------|
| `characteristics.might.value` | `characteristics.might` alone or `mod/bonus` |
| `stamina.value` and `stamina.max` | `hp` field |
| `combat.turns` (Solo=2, others=1) | Missing `combat` section |
| `power.effects` with structured damage/condition objects | HTML power roll display in `effect.before` |
| `type: "main"` in system | Put type in keywords like `["Main Action"]` |
| `systems/draw-steel/assets/roles/{role}.webp` | `modules/mcdm-monsters/...` |
| `prototypeToken` with `disposition: -1` | `token` instead of `prototypeToken` |
| `_stats.systemId: "draw-steel"` | Missing `_stats` section |
| `@potency.weak/average/strong` | `@potency.1/2/3` or plain numbers |
| `effect.before`/`effect.after` for flavor text | Power roll data in `effect.before` |
| `["fly"]` for wasps/birds/bats | `["walk", "fly"]` for flying creatures |
| `disengage: 1` | `disengage: 0` (unless specified) |
| `formula: "@chr"` | `formula: "@might"` or `formula: "@agility"` |
| Keywords lowercase: `["fey", "humanoid"]` | Keywords capitalized: `["Fey", "Humanoid"]` |
| Keywords match distance type | "Melee" in keywords for ranged abilities |
| `_id` matches `^[a-zA-Z0-9]{16}$` | UUID like `d4e5f6a7-b8c9-0123-defa-456789012345` |
| `resource: 3` (integer) for malice cost | `resource: {value: 3}` (object) |
| `spend` field in all abilities | Missing `spend` field (even if empty) |
| `damageDisplay: ""` for area abilities | `damageDisplay: "area"` (invalid choice) |
| Valid distance types: `burst`, `cube`, `line` | `cone` is NOT a valid area type in Draw Steel! |
| Strike keywords: `["melee", "strike", "weapon"]` | Strike keywords without "weapon" keyword |
| Target type: `"creatureObject"` for strikes | Target type: `"creature"` for strikes (less common) |
| Breath/spew keywords: `["area", "magic"]` | Breath/spew keywords with damage types like "fire" |
| Area targets: include `"custom"` field | Area targets without descriptive custom text |
| Use examples as inspiration for unique abilities | Copy examples verbatim with just name changes |
| Cone-like abilities use `cube` type | Using `cone` (not in official rules) for breath/spray |

### Self-Validation Checklist for Foundry VTT JSON (MANDATORY)

Before outputting JSON with `--format foundry` or `--format both`, verify ALL of these:

- [ ] **Actor type:** `type` is `"npc"` (not `"hero"` or other)
- [ ] **All `_id` fields:** Must match pattern `^[a-zA-Z0-9]{16}$` (16 alphanumeric chars, no dashes)
- [ ] **Item types:** All items have `type` of `"ability"` or `"feature"` (no `"class"`, `"ancestry"`, etc.)
- [ ] **Ability types:** All abilities have valid `system.type`:
  - `main`, `maneuver`, `freeManeuver`, `triggered`, `freeTriggered`, `move`, `none`, `villain`
- [ ] **Ability categories:** All abilities have valid `system.category`:
  - `heroic`, `freeStrike`, `signature`, `villain`, or empty (for features)
- [ ] **Monster role:** `system.monster.role` is valid:
  - `ambusher`, `artillery`, `brute`, `controller`, `defender`, `harrier`, `hexer`, `mount`, `support`, `solo`
- [ ] **Monster organization:** `system.monster.organization` is valid:
  - `minion`, `horde`, `platoon`, `elite`, `leader`, `solo`
- [ ] **Monster keywords:** All in `system.monster.keywords` are valid:
  - `abyssal`, `accursed`, `animal`, `beast`, `construct`, `dragon`, `elemental`, `fey`, `giant`, `horror`, `humanoid`, `infernal`, `plant`, `soulless`, `swarm`, `undead`
- [ ] **Ability keywords:** All in ability `system.keywords` are valid:
  - `animal`, `animapathy`, `area`, `charge`, `chronopathy`, `cryokinesis`, `earth`, `fire`, `green`, `magic`, `melee`, `metamorphosis`, `psionic`, `pyrokinesis`, `ranged`, `resopathy`, `rot`, `performance`, `strike`, `telekinesis`, `telepathy`, `void`, `weapon`
- [ ] **Distance types:** All abilities have valid `system.distance.type`:
  - `melee`, `ranged`, `meleeRanged` (single target)
  - `aura`, `burst`, `cube`, `line`, `wall`, `special` (area effects)
  - `self` (self-target)
  - **IMPORTANT:** "cone" is NOT a valid area type in Draw Steel rules!
  - **Cone-like abilities (breath weapons, sprays):** Use `cube` type, not `cone` or `burst`
- [ ] **Formula:** All `system.power.roll.formula` equal `"@chr"` (not `"@might"`, `"@agility"`, etc.)
- [ ] **Keywords lowercase:** All keywords are lowercase (no `"Melee"`, `"Weapon"`, `"Humanoid"`)
- [ ] **Power effects:** For abilities with power rolls (signature, heroic, villain), `system.power.effects` contains structured damage/condition objects, NOT empty `{}`
  - Check: `len(power.effects) > 0` for signature/heroic/villain abilities
  - Check: `effect.before` does NOT contain `power-roll-display` or `[[/damage`
- [ ] **No HTML entities:** `system.effect.before` and `system.effect.after` use raw `<`, `>`, `&` not `&lt;`, `&gt;`, `&amp;`
- [ ] **Required fields:** All required NPC fields present:
  - `system.stamina.value` and `system.stamina.max`
  - `system.characteristics` with all five characteristics
  - `system.combat.save.threshold`
  - `system.combat.size.value`
  - `system.monster.level` and `system.monster.ev`
  - `system.spend` field in all abilities (even if empty)
- [ ] **Token config:** `prototypeToken.bar1.attribute` equals `"stamina"`

**If any check fails, correct the JSON before outputting.**

### Mandatory Validation Script Execution (REQUIRED)

For `--format foundry` or `--format both`, you MUST run the validation script.

**Working directory:** The skill is executed from the `ds-monster-generator` project root.

**Run validation:**
```bash
python scripts/validate_foundry_json.py output/filename.json
```

**This is NOT optional - it is a required step before completing the task.**

**Workflow:**
1. Generate JSON file(s) in the `output/` directory
2. Run validation: `python .claude/skills/draw-steel-monster-generator/scripts/validate_foundry_json.py output/filename.json`
3. Review validation output:
   - **ERRORS (❌):** Must fix before proceeding - these will cause Foundry import failures
   - **WARNINGS (⚠️):** Acceptable for official content, review but proceed if intentional
   - **PASSED (✓):** Validation successful
4. If errors: Fix the JSON, then re-run validation
5. Only report success when validation passes with no errors

**Example workflow:**
```bash
# Generate JSON files (output/scalathrax.json)

# Run validation
$ python .claude/skills/draw-steel-monster-generator/scripts/validate_foundry_json.py output/scalathrax.json
# Review output - if errors, fix and re-run
# Only report completion after validation passes
```

**Validation script:** `.claude/skills/draw-steel-monster-generator/scripts/validate_foundry_json.py`

**CRITICAL:** Skipping validation will result in JSON that fails to import into Foundry VTT. If you cannot run the validation script, report this as an error rather than skipping validation.

### ID Format Requirement (CRITICAL!)
All `_id` fields must match regex pattern `^[a-zA-Z0-9]{16}$` (exactly 16 alphanumeric chars):

```json
// CORRECT (matches ^[a-zA-Z0-9]{16}$):
"_id": "aB2c3D4e5F6G7890"

// INCORRECT (15 chars - doesn't match ^[a-zA-Z0-9]{16}$):
"_id": "aB2c3D4e5F67890"

// INCORRECT (36 chars - UUID format - doesn't match ^[a-zA-Z0-9]{16}$):
"_id": "d4e5f6a7-b8c9-0123-defa-456789012345"

// INCORRECT (has dashes - doesn't match ^[a-zA-Z0-9]{16}$):
"_id": "aB2c-3D4e-5F6G-7890"
```

**Pattern:** `^[a-zA-Z0-9]{16}$` means:
- Start of string
- Exactly 16 characters from a-z, A-Z, 0-9
- End of string (no dashes, no extra chars)

Each item needs its own unique ID. Example:
```json
"items": [
  {
    "name": "Shield Bash",
    "_id": "sHiElDbAsH123456"
  },
  {
    "name": "Shield Wall",
    "_id": "sHiElDwAlL789012"
  }
]

### Power Roll Formula Syntax (CRITICAL!)
Always use `"formula": "@chr"` in the power roll - never use the characteristic name directly:

```json
"power": {
  "roll": {
    "formula": "@chr",
    "characteristics": ["agility"]
  },
  "effects": {}
}
```

The `characteristics` array specifies which characteristic(s) can be used for the power roll, while `formula` is always `"@chr"`.

For abilities that DON'T use a power roll (buffs, movement, protective reactions), use:
```json
"power": {
  "roll": { "formula": "@chr", "characteristics": [] },
  "effects": {}
}
```

### HTML in Effect Text
Use raw HTML tags in `effect.before` and `effect.after`, NOT HTML entities:
```json
// CORRECT:
"before": "<p>You push the target 2 squares.</p>"

// INCORRECT (will display literally):
"before": "<p>You push the target 2 squares &lt; 3.</p>"

Use `<`, `>`, `&` directly - the JSON renderer handles them correctly.

### Keywords Format (CRITICAL!)
Keywords are the monster's **tags** (ancestry, type, creature type), NOT action types:

**INCLUDE in keywords:**
- Ancestry/creature type: `["fey", "humanoid"]`, `["beast", "animal"]`, `["giant", "humanoid"]`
- Damage types in ability: `["piercing", "slashing", "bludgeoning"]`, `["fire", "cold"]`
- Magic/weapon tags: `["magic"]`, `["weapon"]`

**DO NOT include in keywords:**
- Action types: NOT `["Main Action"]`, `["Maneuver"]`, `["Triggered Action"]`
- Range types: NOT `["Melee"]`, `["Ranged"]` (use `distance.type` instead)

**Example:**
```json
"keywords": ["melee", "magic", "weapon"]  // NOT ["Main Action"]
```

### Potency Values (CRITICAL - use these EXACT strings)
- Tier 1 → `"value": "@potency.weak"`
- Tier 2 → `"value": "@potency.average"`
- Tier 3 → `"value": "@potency.strong"`

### Damage Immunities/Weaknesses Format
```json
"damage": {
  "immunities": { "all": 0, "poison": 0, "acid": 0, "cold": 0, "corruption": 0, "fire": 0, "holy": 0, "lightning": 0, "psychic": 0, "sonic": 0 },
  "weaknesses": { "all": 0, "cold": 0, "fire": 5 }
}
```

### Movement Types by Creature Type
- **Flying creatures** (birds, wasps, dragons): `["fly"]`
- **Walking creatures**: `["walk"]`
- **Amphibious**: `["walk", "fly"]` or `["walk", "swim"]`
- **Burrowing**: `["burrow"]` or `["walk", "burrow"]`

**Disengage value:** Always `1` unless specified otherwise (wasps have disengage 1, not 0)

### Combat Size and Token Configuration
```json
"combat": {
  "save": { "threshold": 6, "bonus": "" },
  "size": { "value": 3, "letter": "M" },
  "stability": 0,
  "turns": 1
}
```
- `size.value` = Number of tiles the creature occupies (1=1 tile, 3=3 tiles, 5=5 tiles for solo)
- `size.letter` = Size category: "T" (Tiny), "S" (Small), "M" (Medium), "L" (Large)
- Token size is always `width: 1, height: 1` regardless of creature size (Solo creatures use 2x2 tokens in tokens, but the actor's combat.size.value indicates tiles)

For typical monsters:
- Minion/Horde/Platoon/Elite/Leader: `size.value: 1` (1 tile)
- Solo monsters: `size.value: 3` to `5` (3-5 tiles)

### Enrichers in Effect Text (Required!)
Put `[[/apply condition]]` enrichers directly in `effect.before` or `effect.after`:
```json
"effect": {
  "before": "The target is [[/apply slowed end=save]] by your gaze.",
  "after": ""
}
```

### Distance Type Values
- Melee 1 → `{ "type": "melee", "primary": 1 }`
- Ranged 5 → `{ "type": "ranged", "primary": 5 }`
- 3 burst → `{ "type": "burst", "primary": 3 }`
- Self → `{ "type": "self" }`
- Wall/Line → `{ "type": "wall", "primary": 5 }`

### Target Type Values
- One creature → `{ "type": "creature", "value": 1 }`
- Each enemy in area → `{ "type": "creature", "value": null }` or `{ "type": "creatureObject", "value": null }`
- Zone/Area → `{ "type": "zone", "value": 5 }` (where 5 is zone size)
- Self → `{ "type": "self" }`

When an ability affects "each enemy in area" or "all targets", use `value: null` (not `value: 0`).

Self-target abilities should NOT have `"value": 1`:
```json
// CORRECT (self target):
"target": { "type": "self" }

// INCORRECT:
"target": { "type": "self", "value": 1 }
```

Non-damaging abilities (buffs, movement, etc.) should use empty damageDisplay:
```json
// CORRECT:
"damageDisplay": ""

// INCORRECT (don't use "melee" for non-damaging abilities):
"damageDisplay": "melee"

// INCORRECT ("area" is NOT a valid choice - will crash Foundry!):
"damageDisplay": "area"
```

**damageDisplay Valid Values:**
- `"melee"` - for melee/strike abilities
- `"ranged"` - for ranged abilities
- `""` (empty) - for area abilities, self-target, or non-damaging abilities

### Resource Cost for Malice-Spending Abilities

Elite/Leader/Solo monsters should have at least one heroic ability that costs malice. Set `resource` to an integer:

```json
// CORRECT (heroic ability that costs 3 malice):
"resource": 3

// INCORRECT (resource should be integer, not object):
"resource": {"value": 3}

// For abilities that don't cost malice:
"resource": null
```

**Critical:** Elite, Leader, and Solo monsters MUST have at least one ability with `resource: integer > 0`.

### Spend Field (Required for ALL abilities)

All abilities must include a `spend` field, even if they don't cost anything:

```json
// CORRECT (ability with no cost):
"spend": {
  "text": "",
  "value": null
}

// CORRECT (ability that costs 3 Malice):
"spend": {
  "text": "Spend 3 Malice to activate this ability",
  "value": 3
}

// INCORRECT (missing spend field - will crash Foundry):
// (no spend field at all)
```

**Critical:** Every ability MUST have `spend` field with `text` and `value` keys, even if empty.

### Power Roll Effects Structure (CRITICAL - Read This!)

For abilities with power rolls (signature, heroic, villain), you MUST structure damage and conditions in `system.power.effects` - NOT as HTML in `effect.before`.

**Why this matters:** Foundry VTT parses `power.effects` to create clickable damage buttons, condition applications, and automated power roll outcomes. Putting this data in `effect.before` as HTML breaks Foundry's automation.

**The WRONG way (what Bloodsiphon did - DO NOT DO THIS):**
```json
"power": {
  "roll": {"formula": "@chr", "characteristics": ["agility"]},
  "effects": {}  // EMPTY - WRONG!
},
"effect": {
  "before": "<p><dl class=\"power-roll-display\"><dt class=\"tier1\">...</dt><dd>[[/damage 10 corruption]]...</dd></dl></p>",
  "after": "<p>You pull the target 2 squares.</p>"
}
```

**The CORRECT way (official format from Basilisk/Goblins/Griffon):**
```json
"power": {
  "roll": {
    "formula": "@chr",
    "characteristics": ["agility"]
  },
  "effects": {
    "aB3c4D5e6F7g8H9i": {
      "_id": "aB3c4D5e6F7g8H9i",
      "type": "damage",
      "name": "",
      "img": null,
      "damage": {
        "tier1": {
          "value": "10",
          "types": ["corruption"],
          "properties": [],
          "potency": {"value": "@potency.weak", "characteristic": "none"}
        },
        "tier2": {
          "value": "18",
          "types": ["corruption"],
          "properties": [],
          "potency": {"value": "@potency.average", "characteristic": ""}
        },
        "tier3": {
          "value": "23",
          "types": ["corruption"],
          "properties": [],
          "potency": {"value": "@potency.strong", "characteristic": ""}
        }
      }
    },
    "jK9l8M7n6O5p4Q3r": {
      "_id": "jK9l8M7n6O5p4Q3r",
      "type": "forced",
      "name": "Pull",
      "img": null,
      "forced": {
        "tier1": {
          "movement": ["pull"],
          "distance": "2",
          "display": "{{potency}} {{forced}}",
          "properties": [],
          "potency": {"value": "0", "characteristic": "agility"}
        },
        "tier2": {
          "movement": ["pull"],
          "distance": "2",
          "display": "{{potency}} {{forced}}",
          "properties": [],
          "potency": {"value": "1", "characteristic": "agility"}
        },
        "tier3": {
          "movement": ["pull"],
          "distance": "2",
          "display": "{{potency}} {{forced}}",
          "properties": [],
          "potency": {"value": "2", "characteristic": "agility"}
        }
      }
    },
    "xY9z8W7v6U5t4S3r": {
      "_id": "xY9z8W7v6U5t4S3r",
      "type": "applied",
      "name": "Grabbed",
      "img": null,
      "applied": {
        "tier1": {
          "display": "{{potency}} grabbed",
          "potency": {"value": "0", "characteristic": "agility"},
          "effects": {
            "grabbed": {"condition": "failure", "end": "", "properties": []}
          }
        },
        "tier2": {
          "display": "{{potency}} grabbed",
          "potency": {"value": "1", "characteristic": "agility"},
          "effects": {
            "grabbed": {"condition": "failure", "end": "", "properties": []}
          }
        },
        "tier3": {
          "display": "{{potency}} grabbed (save ends)",
          "potency": {"value": "2", "characteristic": "agility"},
          "effects": {
            "grabbed": {"condition": "failure", "end": "save", "properties": []}
          }
        }
      }
    }
  }
},
"effect": {
  "before": "",
  "after": "<p>You pull the target 2 squares.</p>"
}
```

**Key Rules:**

1. **Each effect gets a unique 16-char `_id`** - generate these for each effect object
2. **Damage effects use `type: "damage"`** with `damage.tier1/tier2/tier3.value` as strings
3. **Condition effects use `type: "applied"`** with `applied.tier1/tier2/tier3.display` and `effects` object
4. **Force movement uses `type: "forced"`** with `forced.tier1/tier2/tier3.movement` array
5. **Potency values:**
   - `@potency.weak` for tier1 when no characteristic check
   - `@potency.average` for tier2 when no characteristic check
   - `@potency.strong` for tier3 when no characteristic check
   - Numeric values like `"0"`, `"1"`, `"2"` when using characteristic checks
   - Characteristic field: `"none"` for no check, `"agility"`/`"might"`/etc. for characteristic-based
6. **effect.before/after** are for flavor text ONLY - never put power roll data here

**Example: Simple damage-only ability (Goblin Warrior - Spear Charge):**
```json
"power": {
  "roll": {"formula": "@chr", "characteristics": ["agility"]},
  "effects": {
    "Y0x6xGOw9jHthmy2": {
      "type": "damage",
      "_id": "Y0x6xGOw9jHthmy2",
      "damage": {
        "tier1": {
          "value": "3",
          "types": [],
          "properties": [],
          "potency": {"value": "@potency.weak", "characteristic": "none"}
        },
        "tier2": {
          "value": "4",
          "types": [],
          "properties": [],
          "potency": {"value": "@potency.average", "characteristic": ""}
        },
        "tier3": {
          "value": "5",
          "types": [],
          "properties": [],
          "potency": {"value": "@potency.strong", "characteristic": ""}
        }
      }
    }
  }
}
```

**Example: Damage + movement effect (Griffon - Claw Swipes):**
```json
"power": {
  "roll": {"formula": "@chr", "characteristics": ["might"]},
  "effects": {
    "nhjhxzjjens59Vpd": {
      "type": "damage",
      "_id": "nhjhxzjjens59Vpd",
      "damage": {
        "tier1": {"value": "7", "types": [], "properties": [], "potency": {"value": "@potency.weak", "characteristic": "none"}},
        "tier2": {"value": "10", "types": [], "properties": [], "potency": {"value": "@potency.average", "characteristic": ""}},
        "tier3": {"value": "13", "types": [], "properties": [], "potency": {"value": "@potency.strong", "characteristic": ""}}
      }
    },
    "O5Bl6Quw9y6pfpTd": {
      "type": "other",
      "_id": "O5Bl6Quw9y6pfpTd",
      "other": {
        "tier1": {"display": "the griffon can shift 1 square", "potency": {"value": "@potency.weak", "characteristic": "none"}},
        "tier2": {"display": "the griffon shifts up to 2 squares", "potency": {"value": "@potency.average", "characteristic": ""}},
        "tier3": {"display": "the griffon shifts up to 3 squares", "potency": {"value": "@potency.strong", "characteristic": ""}}
      }
    }
  }
}
```

**Example: Damage + condition with potency check (Basilisk - Noxious Bite):**
```json
"power": {
  "roll": {"formula": "@chr", "characteristics": ["might"]},
  "effects": {
    "2zbjEF3LsDPSQ9zO": {
      "type": "damage",
      "_id": "2zbjEF3LsDPSQ9zO",
      "damage": {
        "tier1": {"value": "7", "types": ["poison"], "properties": [], "potency": {"value": "@potency.weak", "characteristic": "none"}},
        "tier2": {"value": "10", "types": ["poison"], "properties": [], "potency": {"value": "@potency.average", "characteristic": ""}},
        "tier3": {"value": "13", "types": ["poison"], "properties": [], "potency": {"value": "@potency.strong", "characteristic": ""}}
      }
    }
  }
}
```

**When to use which effect type:**

| Effect Type | Use For | Example |
|-------------|---------|---------|
| `damage` | Any damage, including with conditions | Strike with poison damage |
| `applied` | Conditions (prone, grabbed, slowed, etc.) | "A < 1, prone" |
| `forced` | Push, pull, slide force movement | "push 2 squares" |
| `other` | Flavor text, movement, non-mechanical effects | "shift up to 2 squares" |

**When can power.effects be empty?**

| Ability Type | power.effects | Reason |
|--------------|---------------|---------|
| `type: "main"` | MUST have structured effects | These are power roll abilities |
| `type: "triggered"` | Can be empty | Reactions (e.g., "when damaged, make free strike") |
| `type: "freeTriggered"` | Can be empty | Free reactions (e.g., "when adjacent, shift") |
| `type: "maneuver"` | Can be empty | Movement/positioning (e.g., "fly up to speed") |
| `type: "none"` | Can be empty OR old format | Custom abilities with special rules |

**Examples:**

- **Main action (MUST have effects):** Spear Charge, Noxious Bite, Claw Swipes
- **Triggered (can be empty):** Zephyr Feint ("when griffon takes damage, halve damage and shift")
- **FreeTriggered (can be empty):** Don't Turn Away ("when creature leaves aura, dragon shifts")
- **Maneuver (can be empty):** Swoop ("fly up to speed, make free strikes")
- **None (custom):** Piercing Cry, Swamp Stink (can use old HTML format in effect.before)

**Quick Reference: Effect Structure Template**

```json
"effects": {
  "[UNIQUE_16_CHAR_ID]": {
    "_id": "[UNIQUE_16_CHAR_ID]",
    "type": "damage|applied|forced|other",
    "name": "Display Name (optional)",
    "img": null,
    "[damage|applied|forced|other]": {
      "tier1": {
        "value|display": "string value",
        "types": ["damage", "types"],  // for damage only
        "movement": ["push", "pull", "slide"],  // for forced only
        "distance": "2",  // for forced only
        "properties": [],
        "potency": {
          "value": "@potency.weak|@potency.average|@potency.strong|numeric",
          "characteristic": "none|might|agility|reason|intuition|presence"
        },
        "effects": {  // for applied only
          "[condition]": {
            "condition": "failure|success",
            "end": "save|turn|encounter|respite|",
            "properties": []
          }
        }
      },
      "tier2": { /* same structure */ },
      "tier3": { /* same structure */ }
    }
  }
}
```

### Effect Types in `system.power.effects`
- Damage effects → `"type": "damage"` with nested `damage: { tier1: {...}, tier2: {...}, tier3: {...} }`
- Condition effects → `"type": "applied"` with nested `applied: { tier1: {...}, ... }`
- Force movement → `"type": "forced"` with nested `forced: { tier1: {...}, ... }`
- Other effects → `"type": "other"` with nested `other: { tier1: {...}, ... }`

### Valid Damage Types (CRITICAL!)

**ONLY these damage types are valid in Draw Steel Foundry VTT:**
- `acid`, `cold`, `corruption`, `fire`, `holy`, `lightning`, `poison`, `psychic`, `sonic`

**INVALID damage types (D&D terminology - will crash Foundry):**
- `physical`, `slashing`, `bludgeoning`, `piercing`, `force`, `necrotic`, `radiant`, `thunder`, `untyped`

**For untyped damage:** Use empty array `"types": []`

```json
// CORRECT (poison damage):
"types": ["poison"]

// CORRECT (untyped damage):
"types": []

// INCORRECT (D&D terminology - will crash Foundry):
"types": ["piercing"]

// INCORRECT (fake "untyped" type - will crash Foundry):
"types": ["untyped"]
```

### Ability Type Examples

**IMPORTANT:** Use these examples as **inspiration** for creating unique abilities. Do NOT copy them verbatim - adapt them to fit your creature's theme with unique names, damage types, and effects.

#### Maneuver Ability Example
```json
{
  "name": "Wing Buffet",
  "type": "ability",
  "system": {
    "type": "maneuver",
    "category": "signature",
    "keywords": ["area"],
    "distance": { "type": "burst", "primary": 2 },
    "target": { "type": "enemy", "value": null, "custom": "Each enemy in the area" },
    "damageDisplay": "",
    "power": {
      "roll": { "formula": "@chr", "characteristics": [] },
      "effects": {}
    },
    "effect": {
      "before": "",
      "after": "<p>Each enemy in the area is pushed 2 squares.</p>"
    },
    "spend": {
      "text": "",
      "value": null
    },
    "source": { "book": "Monsters", "license": "Draw Steel Creator License" },
    "_dsid": "wing-buffet",
    "story": "",
    "resource": null,
    "trigger": ""
  },
  "_id": "wInGbUfFeTs12R6a",
  "effects": [],
  "ownership": { "default": 0 }
}
```

#### FreeTriggered Ability Example
```json
{
  "name": "Zephyr Feint",
  "type": "ability",
  "system": {
    "type": "freeTriggered",
    "category": "",
    "keywords": [],
    "distance": { "type": "self" },
    "target": { "type": "self", "value": null },
    "damageDisplay": "",
    "power": {
      "roll": { "formula": "@chr", "characteristics": [] },
      "effects": {}
    },
    "effect": {
      "before": "",
      "after": "<p>Halve the damage and shift up to 3 squares.</p>"
    },
    "spend": {
      "text": "",
      "value": null
    },
    "source": { "book": "Monsters", "license": "Draw Steel Creator License" },
    "_dsid": "zephyr-feint",
    "story": "",
    "resource": null,
    "trigger": "When the monster takes damage, it can use this ability."
  },
  "_id": "zEpHyFeInTjK8L3m",
  "effects": [],
  "ownership": { "default": 0 }
}
```

#### None Type Ability Example
```json
{
  "name": "Piercing Cry",
  "type": "ability",
  "system": {
    "type": "none",
    "category": "",
    "keywords": [],
    "distance": { "type": "special" },
    "target": { "type": "special", "value": null, "custom": "" },
    "damageDisplay": "",
    "power": {
      "roll": { "formula": "@chr", "characteristics": [] },
      "effects": {}
    },
    "effect": {
      "before": "<p>The monster emits a piercing cry that deals 4 sonic damage to each creature in a line 5.</p>",
      "after": ""
    },
    "spend": {
      "text": "",
      "value": null
    },
    "source": { "book": "Monsters", "license": "Draw Steel Creator License" },
    "_dsid": "piercing-cry",
    "story": "",
    "resource": null,
    "trigger": ""
  },
  "_id": "pIeRcInGcRy4K9nO",
  "effects": [],
  "ownership": { "default": 0 }
}
```

**NOTE:** When creating abilities for your monster:
- Use unique names that fit the creature's theme (not "Stinger Strike" unless it's actually a stinger)
- Adapt damage types and effects to match the creature's abilities
- Consider the creature's keywords when designing abilities
- Vary the mechanics from examples to create something unique

## Step 1: Calculate Stats

Use these formulas **exactly**. All values use `ceil()` (round UP to nearest whole number).

### Encounter Value (EV)
```
EV = ceil(((2 × Level) + 4) × Organization_Modifier)
```

### Stamina
```
Stamina = ceil(((10 × Level) + Role_Stamina_Modifier) × Organization_Modifier)
```

### Damage (all tiers)
```
Damage = ceil((4 + Level + Role_Damage_Modifier) × Tier_Modifier)
```

**For Horde and Minion:** Divide damage by 2

### Free Strike
```
Free Strike = Damage at Tier 1 (always!)
```

## Step 2: Lookup Tables

### Organization Modifiers

| Organization | EV Mod | Stamina Mod | Damage |
|--------------|--------|-------------|--------|
| Minion | 0.5 | 0.5 | ÷2 |
| Horde | 0.5 | 0.5 | ÷2 |
| Platoon | 1.0 | 1.0 | 1.0 |
| Elite | 2.0 | 2.0 | 2.0 |
| Leader | 2.0 | 2.0 | 2.0 |
| Solo | 6.0 | 6.0 | 6.0 |

### Role Modifiers

| Role | Stamina Mod | Damage Mod | Power Roll Characteristic |
|------|-------------|------------|---------------------------|
| Ambusher | +20 | +1 | Agility |
| Artillery | +10 | +1 | Reason |
| Brute | +30 | +1 | Might |
| Controller | +10 | +0 | Reason |
| Defender | +30 | +0 | Might |
| Harrier | +20 | +0 | Agility |
| Hexer | +10 | +0 | Reason |
| Mount | +20 | +0 | Might or Agility |
| Support | +20 | +0 | Reason |

### Tier Multipliers

| Tier | Roll Range | Multiplier |
|------|------------|------------|
| Tier 1 | ≤11 | 0.6 |
| Tier 2 | 12-16 | 1.1 |
| Tier 3 | 17+ | 1.4 |

## Step 2b: Characteristics (from The Basics Official Rules)

Each creature has **five characteristics** from **-5 to +5**:

| Characteristic | Abbreviation | What It Represents |
|----------------|--------------|-------------------|
| **Might** | M | Strength and brawn - breaking doors, swinging axes, standing during earthquakes, hurling allies |
| **Agility** | A | Coordination and nimbleness - backflipping, shooting crossbows, dodging explosions, picking pockets |
| **Reason** | R | Logical mind and education - solving puzzles, recalling lore, deciphering codes, psionic powers |
| **Intuition** | I | Instincts and experience - recognizing sounds, reading people, calming animals, tracking monsters |
| **Presence** | P | Force of personality - lying, convincing crowds, impressing royalty, casting spells through song |

### Key Rules
- **0 = Average human** - Most creatures have characteristics around 0
- **-5 to +5 range** - -5 is very weak (baby bunny), +5 is very powerful (ancient dragon)
- **Power Rolls:** Roll 2d10 + characteristic
- **Tier outcomes:**
  - Tier 1: ≤11 (worst outcome)
  - Tier 2: 12-16 (average outcome)
  - Tier 3: 17+ (best outcome)
- **Natural 19-20:** Always tier 3, can be a critical hit

### Edges and Banes (from Official Rules)
- **Edge:** Situational advantage, +2 bonus to roll
- **Double Edge:** Automatic tier upgrade (don't add characteristic)
- **Bane:** Situational disadvantage, -2 penalty
- **Double Bane:** Automatic tier downgrade (don't subtract characteristic)
- **Cancel out:** One edge + one bane = normal roll

### Important Rounding Rule
**Always round DOWN** when dividing (for Horde/Minion damage).

### Potencies (from Classes Official Rules)

Potencies determine if a target can resist conditions and effects. This is **critical** for monster abilities!

#### What Are Potencies?
- An effect with a potency applies only if the effect's **potency value is HIGHER** than the target's indicated characteristic score
- Target **resists** if their characteristic score >= the potency value
- Target **suffers** the effect if their characteristic score < the potency value

#### Potency Format
```
[Characteristic] < [Value]
```

Written as:
- `M < WEAK` or `M < 0` (Might < Weak)
- `A < AVERAGE` or `A < 1` (Agility < Average)
- `R < STRONG` or `R < 2` (Reason < Strong)

#### How to Read Potencies
Say: **"If the target's [characteristic] is less than [potency value], they [suffer effect]"**

Example: `A < 1, prone` means "If the target's Agility is less than 1, they fall prone."

#### Monster Potency Values (Official Formula from Monster Basics.md)

Monsters use the **characteristic used in their power roll** to determine potencies using this formula:

| Tier | Formula | Example (+3 char) |
|------|---------|-------------------|
| Tier 1 | Highest − 2 | +1 |
| Tier 2 | Highest − 1 | +2 |
| Tier 3 | Highest | +3 |

**Formula:**
- Tier 1: Characteristic − 2
- Tier 2: Characteristic − 1
- Tier 3: Characteristic

**Leader/Solo Bonus:** Add +1 to all potencies (max 6)

#### Potency Examples

**Minion Harrier (Agility +2):**
- Weak: 0, Average: 1, Strong: 2
- Written: `A < 0`, `A < 1`, `A < 2`

**Solo Brute (Might +3):**
- Weak: 1, Average: 2, Strong: 3
- Written: `M < 1`, `M < 2`, `M < 3`

**Elite Controller (Reason +2):**
- Weak: 0, Average: 1, Strong: 2
- Written: `R < 0`, `R < 1`, `R < 2`

#### Malice and Potencies
Monsters can spend **3 Malice** on "Brutal Effectiveness" to increase their next ability's potency by 1.

#### Common Potency Effects in Monsters
- `A < 1, prone` - Knock prone if target's Agility < 1
- `M < 2, slowed` - Slow if target's Might < 2
- `R < 0, dazed` - Daze if target's Reason < 0
- `I < 1, weakened` - Weaken if target's Intuition < 1
- `P < 1, frightened` - Frighten if target's Presence < 1

### Echelon-Based Characteristic Scaling (from Monster Basics.md line 1376)

A monster's highest characteristic and power roll bonus is equal to **1 + their echelon**:

| Level Range | Echelon | Highest Characteristic |
|-------------|---------|------------------------|
| Level 1 | 0 | +1 |
| Level 2-4 | 1 | +2 |
| Level 5-7 | 2 | +3 |
| Level 8-10 | 3 | +4 |

**Leader/Solo Bonus:** Add +1 to highest characteristic (max +5)

### Strike Bonus (from Monster Basics.md line 1360)

For abilities with the **Strike** keyword, add the monster's highest characteristic to the damage:

```
Final_Damage = Base_Damage + Highest_Characteristic
```

**Example:** Level 3 Brute (Might +2) at Tier 2:
- Base damage: 8
- Strike bonus: +2
- Final damage: 10

### Target Counts (from Monster Basics.md line 13780)

| Organization | Normal Targets | Notes |
|--------------|----------------|-------|
| Minion | 1 | |
| Horde | 1 | |
| Platoon | 1 | |
| Elite | 2 | |
| Leader | 2 | |
| Solo | 2 | |

### Target Damage Scaling (from Monster Basics.md line 13781)

When targeting more or fewer creatures than normal:

| Target Change | Damage Multiplier |
|---------------|-------------------|
| -1 target | 1.2x |
| Normal | 1.0x |
| +1 target | 0.8x |
| +2+ targets | 0.5x |

**Example:** Elite Controller (2 targets) targeting 3 creatures:
- Base damage: 10
- Multiplier: 0.8x
- Final damage: 8 per tier

## Step 3: Size and Speed (from Bestiary Analysis)

### Size by Organization (Most Common)

| Organization | Most Common Size | Alternatives |
|--------------|-----------------|--------------|
| Minion | 1M (Medium) | 1S, 1T (Tiny) |
| Horde | 1M (Medium) | 1S, 1L |
| Platoon | 1M (Medium) | 1L |
| Elite | 1M (Medium) | 1L, 2-4 |
| Leader | 1M (Medium) | 1S, 1L, 2-5 |
| Solo | 1M or 1L | 2-5, 3 |

**Note:** Contrary to expectations, MCDM uses 1M (Medium) for most minions, not 1S (Small). Only use 1S for clearly small creatures like tiny fey or insects.

### Speed by Role (from Bestiary Data)

| Role | Avg Speed | Common Range |
|------|-----------|--------------|
| Minion Harrier | 6-7 | 6-8 |
| Elite Harrier | 7-8 | 6-10 |
| Platoon Harrier | 7 | 7-8 |
| Minion Ambusher | 6 | 5-10 |
| Elite Ambusher | 7-8 | 5-10 |
| Solo | 8 | 3-15 |
| Mount (Platoon) | 8 | 5-10 |
| Artillery/Controller/Hexer | 5-6 | 5-8 |
| Brute (Elite) | 6 | 5-8 |
| Defender (Elite) | 6 | 5-7 |
| Support (Elite) | 5-6 | 5-8 |

### Stability (from Bestiary)

| Stability | Percentage |
|-----------|------------|
| 0 | 57.5% (most common) |
| 1 | 11.5% |
| 2 | 16.8% |
| 3+ | 14.2% |

**Default to Stability 0** unless the creature has a defensive theme.

## Step 4: Characteristics by Echelon and Role

Use **echelon-based scaling** for the highest characteristic. Secondary characteristics can vary.

### Echelon Reference

| Level Range | Echelon | Highest Characteristic | Leader/Solo Bonus |
|-------------|---------|------------------------|-------------------|
| Level 1 | 0 | +1 | +2 |
| Level 2-4 | 1 | +2 | +3 |
| Level 5-7 | 2 | +3 | +4 |
| Level 8-10 | 3 | +4 | +5 |

### Minion Harrier (Level 1-4, Echelon 0-1)
| Might | Agility | Reason | Intuition | Presence |
|-------|---------|--------|-----------|----------|
| +0 to +1 | +1 to +2 | -1 to +0 | 0 to +1 | -1 to +0 |

### Minion Brute (Level 1-4, Echelon 0-1)
| Might | Agility | Reason | Intuition | Presence |
|-------|---------|--------|-----------|----------|
| +1 to +2 | 0 to +1 | -2 to 0 | -1 to 0 | -1 to +0 |

### Minion Hexer (Level 1-4, Echelon 0-1)
| Might | Agility | Reason | Intuition | Presence |
|-------|---------|--------|-----------|----------|
| -1 to +0 | +1 to +2 | +0 to +1 | 0 to +1 | 0 to +1 |

### Elite Brute (Level 2-4, Echelon 1)
| Might | Agility | Reason | Intuition | Presence |
|-------|---------|--------|-----------|----------|
| +2 to +3 | 0 to +1 | -2 to -1 | 0 to +1 | 0 to +0 |

### Elite Harrier (Level 2-4, Echelon 1)
| Might | Agility | Reason | Intuition | Presence |
|-------|---------|--------|-----------|----------|
| +1 to +2 | +2 to +3 | -1 to +1 | +1 to +2 | 0 to +0 |

### Elite Controller (Level 2-4, Echelon 1)
| Might | Agility | Reason | Intuition | Presence |
|-------|---------|--------|-----------|----------|
| 0 to +1 | 0 to +1 | +1 to +2 | +1 to +2 | 0 to +1 |

### Solo (Level 5-7, Echelon 2) - Add +1 bonus
| Might | Agility | Reason | Intuition | Presence |
|-------|---------|--------|-----------|----------|
| +3 to +4 | +2 to +3 | +1 to +2 | +2 to +3 | +2 to +3 |

### Leader (Level 5-7, Echelon 2) - Add +1 bonus
| Might | Agility | Reason | Intuition | Presence |
|-------|---------|--------|-----------|----------|
| +3 to +4 | +2 to +3 | +2 to +3 | +2 to +3 | +3 to +4 |

## Step 4b: Level-Scaled Force Movement (from Bestiary Analysis)

Force movement values (push, pull, slide) scale with monster level and echelon:

| Level Range | Echelon | Push (T1/T2/T3) | Pull (T1/T2/T3) | Slide (T1/T2/T3) |
|-------------|---------|-----------------|-----------------|------------------|
| Level 1 | 0 | 1/1/1 | 1/2/2 | 1/2/2 |
| Level 2-4 | 1 | 1/2/2 | 2/3/4 | 2/3/4 |
| Level 5-7 | 2 | 2/2/3 | 3/4/5 | 3/4/5 |
| Level 8-10 | 3 | 2/3/3 | 4/5/6 | 4/5/6 |

### Force Movement Types

| Type | Direction | Typical Range | Examples |
|------|-----------|---------------|----------|
| **Push** | Away from source | 1-3 | push 1, push 2, push 3 |
| **Pull** | Toward source | 2-6 | pull 2, pull 4, pull 6 |
| **Slide** | Any direction | 2-8 | slide 2, slide 5, slide 8 |
| **Vertical** | Up/down | 2-5 | vertical push 3 |

### Role-Specific Preferences

| Role | Preferred Force Movement | Typical Values |
|------|-------------------------|----------------|
| Harrier | Pull | 2/4/6 at Level 1, 4/5/6 at Level 8+ |
| Brute | Push | 1/2/3 at any level |
| Controller | Pull/Slide | 2/4/6 (low), 4/5/6 (high) |
| Artillery | Slide | 2/4/5 (low), 4/6/8 (high) |
| Ambusher | Pull | 2/3/4 |

### Movement with Attack Pattern
"The [creature] [jumps/shifts/flies] up to [X] squares before or after making this strike."

## Step 4c: Status Duration Conventions (from Official Conditions Docs)

### Critical Rule: Conditions Are Inherently Persistent

The official Draw Steel condition definitions do NOT include "(save ends)" as part of the condition itself. The duration is an EFFECT applied by monster abilities.

| Condition | Type | How It Ends |
|-----------|------|-------------|
| **Bleeding** | Persistent, ongoing | Until healed (triggers on action use) |
| **Grabbed** | Conditional | Escape, release, or break adjacency |
| **Prone** | Conditional | Stand up maneuver |
| **Slowed** | Persistent | Until healed |
| **Dazed** | Persistent | Until healed |
| **Weakened** | Persistent | Until healed |
| **Frightened** | Conditional | When source changes or is removed |
| **Restrained** | Persistent | Until healed or escaped |

### Condition Application Format

**With Save Ends:**
- Format: `[potency], [condition] (save ends)`
- Example: `M < 2, prone (save ends)`, `A < 1, slowed (save ends)`

**Conditional (no save ends):**
- Format: `[potency], [condition]`
- Example: `A < 2, prone` (ends by standing)

**Ongoing/Damage-over-time:**
- Format: `[condition]`
- Example: `bleeding` (triggers on action use)

### Tier-Based Patterns

| Tier | Pattern | Example |
|------|---------|---------|
| Tier 1 | Instant or conditional | "prone" (ends by standing) |
| Tier 2 | Save ends | "prone (save ends)" |
| Tier 3 | Save ends + secondary effect | "prone and bleeding (save ends)" |

### Combined Format (Potency + Condition + Duration)
```
- ≤11: 5 damage; M < 1, prone
- 12-16: 8 damage; M < 2, prone (save ends)
- 17+: 10 damage; M < 3, prone and bleeding (save ends)
```

### Foundry VTT Enrichers for Conditions (Required for --format foundry/both)

When generating Foundry VTT JSON, use enrichers in ability effect text for interactive conditions:

```markdown
[[/damage 18 corruption]]              - Damage button (18 corruption damage)
[[/damage 1d6]]                        - Damage button with dice
[[/apply bleeding]]                    - Apply Bleeding (no save)
[[/apply dazed save]]                  - Apply Dazed (save ends)
[[/apply dazed end=turn]]              - Apply Dazed (save ends, ends on turn)
[[/apply slowed end=save]]             - Apply Slowed (save ends)
[[/apply weakened]]                    - Apply Weakened (no save)
[[/apply prone end=save]]              - Apply Prone (save ends)
[[/apply taunted save]]                - Apply Taunted (save ends)
[[/apply grabbed]]                     - Apply Grabbed (save ends)
```

**Valid endings:** `encounter`, `respite`, `save`, `turn`

**Example in power roll effect (simplified):**
```json
"effect": {
  "before": "<p>The target is [[/apply slowed end=save]] by your gaze.</p>",
  "after": ""
}
```

**Free Strike:** Only listed in `monster.freeStrike` - do NOT create a "Free Strike" ability item.

**For custom status effects**, generate a UUID and define the effect on the item:

**For custom status effects**, generate a UUID and define the effect on the item:
```json
"effects": [{
  "name": "Dragonsealed",
  "type": "base",
  "system": {
    "end": { "type": "save", "roll": "1d10 + @combat.save.bonus" }
  },
  "statuses": [],
  "_id": "Dxo9mYDLbbNCb28K"
}]
```
Then reference it as `[[/apply Dxo9mYDLbbNCb28K save]]`

**Note:** Potency text like `R < 2` remains as plain text - only use `[[/apply]]` for the condition itself.

## Step 4d: Triggered Actions and Free Triggered Actions (from Combat.md)

### Core Rules
- **Triggered Actions:** Monsters can use 1 triggered action per round (on their turn OR another creature's turn)
- **Free Triggered Actions:** Same rules, but DON'T count against the 1/round limit
- **Priority:** Player creatures resolve first, then Director for monsters
- **Dazed:** A dazed creature can't use triggered or free triggered actions

### When to Use Each Type

**Use Free Triggered Actions for:**
- Essential counter-attacks (when damaged)
- Core defensive mechanics
- Abilities that should always be available

**Use Triggered Actions for:**
- Situational ally protection (save the free one for yourself)
- Area effects that might not trigger often
- Secondary reactions

### Format Templates

**Free Triggered Action (Counter-Attack):**
```markdown
> | **[Keywords]** | **Free triggered action** |
> | **📏 [Range]** | **🎯 [Target]** |
>
> **Trigger:** A creature damages you with a melee attack.
>
> **Effect:** Make a [type] strike against the triggering creature.
```

**Triggered Action (Ally Protection):**
```markdown
> | **[Keywords]** | **Triggered action** |
> | **📏 [Range]** | **🎯 [Target]** |
>
> **Trigger:** An ally within distance is targeted by an enemy's ability.
>
> **Effect:** Each target shifts up to 2 squares before the damage is resolved.
```

**Free Triggered Action (Zone Response):**
```markdown
> | **-** | **Free triggered action** |
> | **📏 Self** | **🎯 Self** |
>
> **Trigger:** A creature leaves the area of your [aura trait].
>
> **Effect:** You shift up to your speed, and [effect].
```

### Triggered Action Availability by Organization

Based on Bestiary analysis, triggered actions are reserved for more powerful monsters:

| Organization | Level Range | Typical Triggered Actions |
|--------------|-------------|---------------------------|
| **Minion** | Any | None (too fragile/simple) |
| **Horde** | Level 1-3 | None (swarms use area effects) |
| **Platoon** | Level 1-5 | None (focus on signature ability) |
| **Elite** | Level 4+ | 1 triggered action (situational) |
| **Leader** | Level 4+ | 1 triggered action (often ally-focused) |
| **Solo** | Level 5+ | 1-2+ free triggered actions (core mechanics) |

### Role-Based Triggered Action Patterns

| Role | Triggered Action Type | Typical Trigger |
|------|----------------------|-----------------|
| **Solo Controllers** | Free - Zone/Aura response | "Creature leaves aura" |
| **Solo Brutes** | Free - Counter-attack | "Damaged by melee" |
| **Elite Defenders** | Triggered - Ally protection | "Ally targeted" |
| **Leaders** | Triggered - Team coordination | "Enemy targets ally" |

### When to Skip Triggered Actions

**Do NOT add triggered actions for:**
- Minions (any level)
- Horde monsters (Level 1-3)
- Platoon monsters (Level 1-5)
- Monsters with 3+ abilities already

**Add triggered actions for:**
- Elites/Leaders with thematic defensive ability
- Solos with core mechanical reactions
- High-level (5+) monsters that need reactive depth

### Damage Scaling for Triggered Actions

Triggered action damage typically equals:
- **T1 damage** for simple counter-attacks
- **T2 damage** for enhanced reactions
- **T3 damage** for powerful callbacks

### Examples from Bestiary

**Counter-Attack (Fire Giant Red Fist - Level 9 Elite Brute):**
```markdown
> ❗️ **Heat and Pressure**
>
> | **Melee** | **Free triggered action** |
> | **📏 Melee 3** | **🎯 The triggering creature** |
>
> **Trigger:** A creature within distance willingly moves or shifts away from the red fist.
>
> **Effect:** The target makes a Might test.
> - ≤11: Weakened and slowed (save ends)
> - 12-16: Weakened (EoT)
> - 17+: No effect
```

**Ally Protection (Kobold Centurion - Level 1 Leader):**
```markdown
> ❗️ **Testudo!**
>
> | **Area** | **Triggered action** |
> | **📏 5 burst** | **🎯 Each ally in the area** |
>
> **Trigger:** A creature uses an ability that targets the centurion or an ally within distance.
>
> **Effect:** Each target shifts up to 2 squares before the damage is resolved.
```

**Solo Core Mechanic (Omen Dragon - Level 8 Solo):**
```markdown
> ❗️ **Don't Turn Away**
>
> | **-** | **Free triggered action** |
> | **📏 Self** | **🎯 Self** |
>
> **Trigger:** A creature leaves the area of the dragon's Stagnant Wyrmscale Aura trait.
>
> **Effect:** The dragon shifts up to their speed, and the Deathcount of each dragonsealed creature who comes adjacent to the dragon during this shift is reduced by 1.
```

### Common Mistakes to Avoid

1. **Don't use (save ends)** in triggered action effects - the trigger is already the condition
2. **Keep effects immediate** - triggered actions resolve instantly when trigger occurs
3. **One trigger per action** - if multiple triggers happen simultaneously, only one triggers

## Step 5: Select Keywords

Choose from these **exact** lists only. Do NOT invent keywords.

### Creature Keywords (Ancestry)
Based on Bestiary analysis, common combinations include:
- **Humanoid + Rival** (28x in Bestiary)
- **Abyssal + Demon** (27x)
- **Undead** (16x)
- **Human + Humanoid** (15x)
- **Humanoid + Orc** (13x)
- **Goblin + Hobgoblin + Humanoid + Infernal** (13x)
- **Fey + Humanoid + Shadow Elf** (13x)
- **Dwarf + Humanoid** (13x)
- **Fey + Humanoid + Wode Elf** (12x)
- **Humanoid + Kobold** (9x)
- **Goblin + Humanoid** (9x)
- **Abyssal + Gnoll** (9x)
- **Fey + High Elf + Humanoid** (9x)

**Standard keyword lists:**
- **Cosmological:** Abyssal, Elemental, Fey, Infernal
- **Biological:** Animal, Beast, Giant, Humanoid, Ooze, Plant
- **Supernatural:** Construct, Dragon, Horror, Undead
- **Special:** Accursed, Soulless, Swarm

### Ability Keywords
Strike, Magic, Weapon, Psionic, Area, Melee, Ranged, Free, Triggered, Maneuver

### Damage Types (Most Common in Bestiary)
1. **fire** (24.3%)
2. **corruption** (23.8%)
3. **poison** (20.4%)
4. **psychic** (16.6%)
5. **holy** (13.2%)
6. acid, lightning, sonic, cold

### Conditions (Most Common in Bestiary)
1. **prone** (30.6%)
2. **slowed** (26.4%)
3. **bleeding** (25.5%)
4. **dazed** (22.6%)
5. **restrained** (22.3%)
6. **weakened** (20.9%)
7. **grabbed** (17.9%)
8. **frightened** (14.2%)
9. **pushed** (8.5%)
10. **taunted** (6.2%)

## Step 6: Complete Stat Block Format

Output **MUST** match this exact MCDM format:

```markdown
---
ancestry:
  - [Keyword1]
  - [Keyword2]
ev: [X]
file_basename: [Creature Name]
file_dpath: Monsters/[Category]/Statblocks
free_strike: [Z]
level: [L]
might: [M]
agility: [A]
reason: [R]
intuition: [I]
presence: [P]
roles:
  - [Role]
size: [Size]
source: mcdm.monsters.v1
speed: [Speed]
stability: [Stability]
stamina: '[Y]'
type: monster
---

###### [Creature Name]

| [Ancestry1], [Ancestry2]... |          -          |      Level [L]       |             [Role]              |         EV [X]          |
| :--------------------------: | :-----------------: | :------------------: | :-----------------------------: | :---------------------: |
|        **[Size]**<br/> Size  | **[Speed]**<br/> Speed | **[Stamina]**<br/> Stamina | **[Stability]**<br/> Stability | **[Free Strike]**<br/> Free Strike |
|   **-**<br/> Immunity        | **-**<br/> Movement  |          -           | **-**<br/> With Captain         | **-**<br/> Weaknesses   |
|   **[Might]**<br/> Might     | **[Agility]**<br/> Agility | **[Reason]**<br/> Reason | **[Intuition]**<br/> Intuition | **[Presence]**<br/> Presence |

<!-- -->
> ⚔️ **[Signature Ability Name]**
>
> | **[Keywords]** |          **[Action Type]** |
> | -------------- | --------------------------: |
> | **📏 [Range]** | **🎯 [Target]** |
>
> **Power Roll + [Characteristic]:**
>
> - **≤11:** [D1] [Type]; [Potency], [Condition]
> - **12-16:** [D2] [Type]; [Potency], [Condition]
> - **17+:** [D3] [Type]; [Potency], [Condition]
>
> **Effect:** [Effect description]

<!-- -->
> ⭐️ **[Secondary/Trait Ability Name]**
>
> | **[Keywords]** |          **[Action Type]** |
> | -------------- | --------------------------: |
> | **📏 [Range]** | **🎯 [Target]** |
>
> **Effect:** [Effect description]

<!-- -->
> ❗️ **[Triggered Ability Name]**
>
> | **[Keywords]** |       **[Action Type]** |
> | -------------- | -----------------------: |
> | **📏 [Range]** | **🎯 [Target]** |
>
> **Trigger:** [Trigger condition]
>
> **Effect:** [Effect description]
```

### Icon Meanings
- ⚔️ = Signature Ability (Main Action)
- ❇️ = Secondary Ability (Main Action)
- 🏹 = Ranged Ability
- 🗡 = Melee Ability
- ⭐️ = Trait/Passive
- ❗️ = Triggered/Free Triggered Action
- 📏 = Range indicator (Melee 1, Ranged 5, 3 burst, etc.)
- 🎯 = Target (One creature, Each enemy, etc.)

### Action Types
- Main Action
- Maneuver
- Free Triggered Action
- Triggered Action
- Free Action

### Range Indicators
- Melee 1 (adjacent square)
- Melee 2 (nearby)
- Ranged 5 (short range)
- Ranged 8 (long range)
- 3 burst (area around target)
- 3 wall (linear area)

## Step 7: Design Signature Ability

**Format:**
- Use the table format with icons
- Include Power Roll + [Characteristic]
- Use calculated damage values (Damage_T1, T2, T3)
- **Include potencies for conditions** - most conditions should have a potency check
- Match damage type to creature theme

**Common potency patterns:**
- `A < 1, prone` - Knock prone (Agility check)
- `M < 2, slowed` - Slow (Might check)
- `R < 0, dazed` - Daze (Reason check)
- `I < 1, weakened` - Weaken (Intuition check)
- `P < 1, frightened` - Frighten (Presence check)

**Example with potencies:**
```
Power Roll + Agility:
- ≤11: 5 slashing; A < 0, prone
- 12-16: 8 slashing; A < 1, prone
- 17+: 10 slashing; A < 2, prone and can't stand (save ends)
```

**Common damage types:** fire, corruption, poison, psychic, holy
**Common conditions:** prone, slowed, bleeding, dazed, restrained, weakened

## Step 8: Design Secondary/Trait Abilities

- Use ⭐️ icon for traits/passives
- Use ❗️ icon for triggered abilities
- Common patterns: ally bonuses, defensive effects, movement abilities

## Self-Validation Checklist (MANDATORY)

Before outputting the monster, verify ALL of these:

- [ ] **EV Formula:** `ceil(((2 × L) + 4) × Org_Mod)` matches output
- [ ] **Stamina Formula:** `ceil(((10 × L) + Role_Mod) × Org_Mod)` matches output
- [ ] **Free Strike:** Equals calculated Tier 1 damage exactly
- [ ] **Damage T1:** `ceil((4 + L + Dmg_Mod) × 0.6)` matches output
- [ ] **Damage T2:** `ceil((4 + L + Dmg_Mod) × 1.1)` matches output
- [ ] **Damage T3:** `ceil((4 + L + Dmg_Mod) × 1.4)` matches output
- [ ] **Horde/Minion:** Damage correctly divided by 2
- [ ] **Size:** Matches common patterns (Minion=1M, Platoon=1M, Solo=1M/1L)
- [ ] **Speed:** Appropriate for role (Harrier=6-7, Mount=8, others=5-6)
- [ ] **Characteristics:** Within expected ranges for role
- [ ] **Stability:** 0 unless defensive theme
- [ ] **Ancestry:** All from approved lists (no inventions)
- [ ] **Conditions:** All from approved lists (no inventions)
- [ ] **Format:** Matches MCDM stat block template exactly

## Role Templates (Updated from Bestiary)

### HARRIER: Mobility + Strikes
- **Size:** 1M (Minion/Horde/Platoon), 1L (Elite/Solo)
- **Speed:** 6-8 (fastest of all roles)
- **Agility:** +2 to +3
- **Might:** +0 to +2
- **Signature:** Fast attacks with push/slow effects
- **Secondary:** Repositioning abilities, escape effects
- **Common abilities:** Skitter Away, Hit and Run

### BRUTE: High Damage + Area
- **Size:** 1M to 3 (larger = more minions)
- **Speed:** 5-6
- **Might:** +2 to +3
- **Signature:** Powerful attacks with prone/grab
- **Secondary:** Area control, forced movement
- **Common abilities:** Smash, Grab and Smash

### CONTROLLER: Debuffs + Positioning
- **Size:** 1M
- **Speed:** 5-6
- **Reason:** +1 to +2
- **Signature:** Magic/psionic attacks with debuffs
- **Secondary:** Battlefield control, zones
- **Common abilities:** Area effects, forced movement

### DEFENDER: Protection + Reduction
- **Size:** 1M
- **Speed:** 5-6
- **Might:** +1 to +2
- **Signature:** Defensive strikes with ally buffs
- **Secondary:** Protective effects, cover
- **Common abilities:** Shield allies, reduce damage

### AMBUSHER: Burst + Surprise
- **Size:** 1M
- **Speed:** 6-8
- **Agility:** +2 to +3
- **Signature:** High damage from ambush
- **Secondary:** Escape/evasion abilities
- **Common abilities:** Flanking, surprise attacks

### ARTILLERY: Area + Range
- **Size:** 1M
- **Speed:** 5
- **Reason:** +1 to +2
- **Signature:** Ranged area attacks
- **Secondary:** Positioning/sniping
- **Common abilities:** Ranged burst, multi-target

### HEXER: Conditions + Curses
- **Size:** 1M
- **Speed:** 5
- **Reason:** +0 to +1
- **Signature:** Debuff-focused attacks
- **Secondary:** Hexes and curses
- **Common abilities:** Status effects, conditions

### MOUNT: Carrying + Movement
- **Size:** 2-4 (Platoon), 3-5 (Elite)
- **Speed:** 8 (fastest overall)
- **Might:** +2, Agility: +1
- **Signature:** Transport-focused attacks
- **Secondary:** Movement enhancement
- **Common abilities:** Carry, Trample

### SUPPORT: Buffs + Healing
- **Size:** 1M
- **Speed:** 5
- **Reason/Intuition/Presence:** +0 to +1 each
- **Signature:** Support attacks with healing
- **Secondary:** Ally enhancement
- **Common abilities:** Buffs, healing, buffs for allies

## Step 9: Design Malice Features

Malice is a Director resource that monsters can spend to activate powerful abilities. All monsters should have malice features unless they're simple minions.

### Basic Malice Features (Universal Options)

These features are available to all monster types:

**Brutal Effectiveness (3 Malice)**
- **Effect:** The monster's next ability with a potency has that potency increased by 1.
- **Icon:** ⭐️

**Malicious Strike (5+ Malice)**
- **Effect:** The monster's next strike deals extra damage equal to their highest characteristic score. Extra damage increases by 1 for each additional Malice spent (max 3× highest characteristic).
- **Restriction:** Cannot be used two rounds in a row.
- **Icon:** 🗡️

### Malice Feature Icon Classification

Use icons to indicate malice feature type:

| Icon | Type | Description |
|------|------|-------------|
| ⭐️ | Trait | Always in effect or self-targeted |
| 🔳 | Area | Cube, line, or wall area effects |
| ❇️ | Aura/Burst | Affects creatures within a radius |
| 🌀 | Special | Unique distance, encounter map effects |
| ☠️ | Villain Action | Leader/Solo special abilities |

### Malice Feature Trigger Timing

All malice features activate at the start of the monster's turn:
> "At the start of any [monster name]'s turn, you can spend Malice to activate one of the following features:"

### Organization-Based Malice Selection

**Solo Organization:**
- Generate 3 malice features
- MUST include Solo Action (5 Malice) - extra main action, usable even when dazed
- Generate 3 villain actions (☠️) - ONLY Solos and Leaders get villain actions
- Level 1-3: Villain actions should cost 5-7 Malice (no 10-Malice features!)
- Level 4+: Can include 10-Malice ultimate villain action

**Leader Organization:**
- Generate 2 malice features
- Include team-buff effects
- Generate 3 villain actions (☠️) - ONLY Solos and Leaders get villain actions
- Level 1-3: Villain actions should cost 5-7 Malice

**Platoon/Elite Organization:**
- Generate 2 malice features
- Include ally-benefit effects
- **NO villain actions** - Villain Actions are for Leaders and Solos ONLY

**Minion/Horde Organization:**
- Generate 2 malice features
- Features benefit the swarm/horde
- Minions use shared malice (squad-based, not individual)
- **NO villain actions** - Villain Actions are for Leaders and Solos ONLY

### ⚠️ Critical: Malice Costs by Level (Based on Official Draw Steel Content)

**Level 1-3 Monsters:**
- Malice features: 2-7 Malice
- Villain actions: 5-7 Malice
- **10 Malice features are NOT used in official level 1-3 content!**
- Examples from Monsters book: Abyssal Rift (7), Dread March (7), Fodder Run (7)

**Level 4-6 Monsters:**
- Malice features: 3-9 Malice
- Villain actions: 5-9 Malice
- Can include 9 Malice features

**Level 7+ Monsters:**
- Malice features: 3-10 Malice
- Villain actions: 5-10 Malice
- 10 Malice features appropriate for ultimate abilities

**Solo Action:**
- Always **5 Malice** (confirmed across all official solo monsters: Thorn Dragon, Xorannox, Werewolf, Manticore, Lich, etc.)

**Examples for Level 1 Solo:**
- Brutal Effectiveness (3 Malice)
- Solo Action (5 Malice) - ALWAYS 5!
- Villain Action 1 (5-7 Malice) - opener
- Villain Action 2 (5-7 Malice) - crowd control
- Villain Action 3 (5-7 Malice) - devastating but NOT 10!
- Monster has access to all Level 1+ features
- Include "Prior Malice Features" feature that lists lower-level options

**Level 7+ Features:**
- Generate one new malice feature
- Features may include encounter-wide effects
- Access to all lower level features

**Level 10+ Features:**
- Generate one ultimate malice feature
- Access to all malice features from all tiers

### Triggered Action Malice Features

Some monsters (like Kingfissure Worm) have malice features that can also be used as triggered actions:

> "At the start of [monster]'s turn or when an action's trigger occurs, you can spend Malice to activate one of the following features:"

### Malice Section in Stat Block Output

When generating Markdown stat blocks, include a Malice section:

```markdown
<!-- -->
> ☠️ **Malice Features**
>
> At the start of any [monster name]'s turn, you can spend Malice to activate one of the following features:
>
> <!-- -->
> > ⭐️ **Brutal Effectiveness (3 Malice)**
> >
> > The monster's next ability with a potency has that potency increased by 1.
>
> <!-- -->
> > 🗡️ **Malicious Strike (5+ Malice)**
> >
> > The monster's next strike deals extra damage equal to their highest characteristic.
>
> <!-- -->
> > [Additional malice features based on organization - see rules above]
```

**Important - Only add Villain Actions for Leader/Solo organizations:**

**Villain Action Usage Rules (from Monster Basics.md):**
- Each villain action can be used only once per encounter
- No more than one villain action can be used per round
- Villain actions are used at the end of any creature's turn
- Always generate exactly 3 villain actions:
  - **Villain Action 1 (opener):** Shows heroes they're not battling a typical creature
  - **Villain Action 2 (crowd control):** Helps villain regain upper hand after heroes respond
  - **Villain Action 3 (ult):** Devastating showstopper before the battle ends

```markdown
<!-- ONLY for Leader and Solo monsters: -->
> <!-- -->
> > ☠️ **Villain Action 1**
> >
> > [Effect description - opener: deals damage, summons, buffs, debuffs, or moves]
> >
> <!-- -->
> > ☠️ **Villain Action 2**
> >
> > [Effect description - crowd control: more powerful than opener]
> >
> <!-- -->
> > ☠️ **Villain Action 3**
> >
> > [Effect description - ult: devastating blow]
```

**For Platoon/Elite/Minion/Horde monsters - stop at malice features, do NOT add villain actions.**

## Additional Resources

- **Templates:** [references/templates.md](references/templates.md) - Role archetypes and ability patterns
- **Examples:** [references/examples.md](references/examples.md) - Complete stat block examples
- **Formulas:** [references/formulas.md](references/formulas.md) - Quick reference formulas
- **Foundry VTT Export:** [references/foundry-export.md](references/foundry-export.md) - Extended examples (schema is in SKILL.md above)

## Critical Rules

1. **NO D&D terminology:** No "vs. AC", "Armor Class", "HP", "hit points", "d20", "DC"
2. **Use 2d10:** Power rolls use `2d10 + characteristic`
3. **Tier ranges:** ≤11 (T1), 12-16 (T2), 17+ (T3)
4. **Free Strike = T1 damage:** This is the definitive rule
5. **Horde/Minion damage:** Always divide by 2 after calculation
6. **All stats use ceil():** Round UP for calculations (EV, Stamina, Damage)
7. **Division uses round DOWN:** Always round down when dividing (for Horde/Minion)
8. **Natural 19-20:** Always tier 3, can be a critical hit
9. **Characteristics:** Range from -5 to +5, where 0 = average human
10. **Edges and Banes:** Edge = +2, Bane = -2, they cancel out
11. **Potencies:** Write as `[Char] < Value` (e.g., `A < 1, prone`). Target resists if their score >= value.
12. **Strike Bonus:** Add highest characteristic to strike damage
13. **Echelon scaling:** Highest characteristic = 1 + echelon (Level 1=+1, 2-4=+2, 5-7=+3, 8-10=+4)
14. **Leader/Solo bonuses:** +1 to highest characteristic (max +5), +1 to all potencies
15. **Target counts:** Normal=1, Elite/Leader/Solo=2
16. **Match the MCDM format exactly:** Use the table format, icons, and structure shown
17. **Use common damage types:** fire, corruption, poison, psychic, holy
18. **Use common conditions:** prone, slowed, bleeding, dazed, restrained, weakened
19. **Most minions are 1M size, not 1S:** Follow Bestiary patterns
