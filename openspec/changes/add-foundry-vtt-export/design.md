## Context

The Draw Steel Monster Generator skill currently outputs Markdown stat blocks. Users want the ability to export monsters directly to Foundry VTT as JSON actors that work with the Draw Steel system.

## Goals / Non-Goals

**Goals:**
- Generate valid Foundry VTT NPC JSON for the Draw Steel system
- Support all monster organizations (Minion, Horde, Platoon, Elite, Leader, Solo)
- Support all monster roles (Ambusher, Artillery, Brute, Controller, Defender, Harrier, Hexer, Mount, Support)
- Include all ability types (Main Action, Maneuver, Free Triggered Action, Triggered Action)
- Support Foundry enrichers for interactive text (damage, healing, apply effect)
- Output to file or clipboard
- Maintain backwards compatibility with Markdown output

**Non-Goals:**
- Generate hero/player characters
- Support custom advancement or modifications
- Create compendium packs directly (just NPC JSON export)
- Handle images/assets (use default Draw Steel images)

## Key Decisions

### 1. Export Format Strategy

**Decision:** Generate individual NPC JSON files that can be imported via Foundry's Compendium import feature.

**Rationale:**
- Individual files are easier to manage than creating full compendium structures
- Users can import into existing compendiums or create new ones
- Matches the structure of existing Draw Steel module files

**File Structure:**
```
output/
├── Monsters/
│   └── {CreatureName}/
│       └── npc_{CreatureName}_{actorId}.json
```

### 2. Output Modes

**Decision:** Add optional flag to request Foundry VTT output.

| Mode | Output | Usage |
|------|--------|-------|
| Default | Markdown stat block | For documentation/reference |
| `--format foundry` | JSON file | For direct import |
| `--format both` | Markdown + JSON | For documentation + import |

**Usage:**
```
/create-monster "Level 3 Gremlin, Platoon Brute" --format foundry
/ create-monster "Level 5 Dragon, Solo Brute" --format both
```

### 3. Actor Structure Mapping

Map skill output to Foundry NPC format:

| Skill Field | Foundry Path |
|-------------|--------------|
| Name | `name` |
| Level | `system.monster.level` |
| EV | `system.monster.ev` |
| Role | `system.monster.role` |
| Organization | `system.monster.organization` |
| Free Strike | `system.monster.freeStrike` |
| Stamina | `system.stamina.value` / `max` |
| Characteristics | `system.characteristics.{char}.value` |
| Size | `system.combat.size.value` (1-3) / `letter` (S/M/L) |
| Speed | `system.movement.value` |
| Stability | `system.combat.stability` |
| Ancestry Keywords | `system.monster.keywords[]` |
| Immunity/Weakness | `system.damage.immunities/weaknesses` |

### 4. Ability Type Mapping

Map skill ability types to Foundry ability types:

| Skill Type | Foundry Type | Foundry Category |
|------------|--------------|------------------|
| Main Action | `main` | `signature` / `heroic` / `malice` |
| Maneuver | `maneuver` | `signature` / `heroic` / `malice` |
| Free Triggered Action | `freeTriggered` | `signature` / `heroic` / `malice` |
| Triggered Action | `triggered` | `signature` / `heroic` / `malice` |
| Villain Action | `villain` | `villain` |
| Passive/Trait | `feature` | N/A |
| Malice Feature | `feature` | N/A |
| No Type | `none` | `heroic` (for features with resource/trigger) |

### 5. Power Roll to Foundry Effects

Convert power roll effects to Foundry's effect system:

```
Skill Format:
- ≤11: 5 fire damage; M < 1, prone

Foundry Format:
system.power.effects.[effectId] = {
  type: "damage",
  damage: {
    tier1: { value: "5", types: ["fire"] },
    tier2: { ... },
    tier3: { ... }
  }
}
system.power.effects.[effectId] = {
  type: "applied",
  applied: {
    tier1: {
      display: "{{potency}} prone (save ends)",
      potency: { value: "@potency.weak", characteristic: "might" },
      effects: {
        prone: { condition: "failure", end: "save" }
      }
    }
  }
}
```

### 6. Enricher Support

Support Foundry enrichers in ability descriptions:

| Enricher | Example | Purpose |
|----------|---------|---------|
| Damage | `[[/damage 5]]` | Interactive damage button |
| Healing | `[[/heal 10]]` | Interactive healing button |
| Apply Effect | `[[/apply bleeding]]` | Apply status effect |
| Lookup | `[[/lookup @name]]` | Dynamic text |
| Item Embed | `@Embed[uuid]` | Reference other items |

### 7. Item Structure

Generate abilities as Foundry items:

```json
{
  "name": "Ability Name",
  "type": "ability",
  "system": {
    "type": "main" | "maneuver" | "triggered" | "freeTriggered" | "villain" | "none",
    "category": "signature" | "heroic" | "malice" | "villain",
    "keywords": ["melee", "strike", "weapon"],
    "distance": {
      "type": "melee" | "ranged" | "burst" | "line" | "cube" | "meleeRanged" | "self" | "special",
      "primary": 1-10,
      "secondary": 0-5,
      "tertiary": 0-3
    },
    "target": {
      "type": "creature" | "enemy" | "creatureObject" | "enemyObject" | "self" | "special",
      "value": 1+,
      "custom": "Custom target description"
    },
    "power": {
      "roll": {
        "formula": "@chr",
        "characteristics": ["might" | "agility" | "reason" | "intuition" | "presence"]
      },
      "effects": { ... }
    },
    "effect": {
      "before": "...",
      "after": "..."
    },
    "spend": {
      "text": "",
      "value": null | number
    },
    "resource": null | number,
    "trigger": "Trigger condition text",
    "source": {
      "book": "...",
      "page": "...",
      "license": "Draw Steel Creator License"
    },
    "_dsid": "ability-name",
    "story": ""
  }
}
```

### 8. Extended Combat and Movement Fields

Map additional combat and movement statistics:

```
system.combat.turns: 1 | 2  // Solo monsters have 2 turns, default 1
system.combat.save.threshold: number  // 1-10, initial: 6, based on level
system.combat.save.bonus: "" | string  // FormulaField, can be empty

system.movement.value: number  // Speed, min: 0, initial: 5
system.movement.types: Set(["walk"]) | Set(["fly"]) | Set(["swim"]) | etc.  // Set, initial: ["walk"]
system.movement.hover: false | true  // Boolean, for flying creatures
system.movement.disengage: number  // min: 0, initial: 1

// Size Model (embedded)
system.combat.size = {
  value: number,  // min: 1, initial: 1
  letter: "T" | "S" | "M" | "L"  // Tiny, Small, Medium, Large
}

system.damage.immunities: { all: 0, fire: 0, cold: 0, ... }
system.damage.weaknesses: { all: 0, holy: 5, fire: 5, ... }  // Can have values

system.biography: {
  value: "<html content>",  // HTMLField
  director: "<html content>",  // HTMLField, gmOnly
  languages: Set()  // Set of language strings
}

system.statuses.immunities: Set()  // Status immunities
```

### 9. Force Movement with Properties

Support force movement with additional properties:

```json
system.power.effects.[effectId] = {
  type: "forced",
  name: "push",
  forced: {
    tier1: {
      movement: ["push"],
      distance: "3",
      display: "{{forced}}",
      properties: ["vertical"],  // Vertical push/pull/slide
      potency: { value: "@potency.weak", characteristic: "might" }
    }
  }
}
```

### 10. Item Effects for Status Conditions

Support item effects for status conditions:

```json
item.effects = [
  {
    "name": "Slowed and Weakened",
    "type": "base",
    "statuses": ["slowed", "weakened"],
    "system": {
      "end": {
        "type": "save",
        "roll": "1d10 + @combat.save.bonus"
      }
    },
    "changes": [
      { "key": "system.damage.weakness.fire", "mode": 2, "value": "5" }
    ]
  }
]
```

### 11. Prototype Token Configuration

Set up prototype token for Foundry:

```json
prototypeToken = {
  "name": "Monster Name",
  "displayName": 20,  // Always show
  "displayBars": 20,  // Always show
  "bar1": { "attribute": "stamina" },
  "bar2": { "attribute": "hero.resources" },
  "width": 1,
  "height": 1,
  "disposition": -1,  // Hostile
  "texture": {
    "src": "systems/draw-steel/assets/roles/brute.webp",
    "anchorX": 0.5,
    "anchorY": 0.5,
    "fit": "contain",
    "scaleX": 1,
    "scaleY": 1
  }
}
```

## Technical Implementation

### 1. New Template Function

Create `generate_foundry_vtt_json(monster_data)` that:
- Takes parsed monster data from the generation process
- Returns complete NPC JSON object
- Generates unique IDs for items and effects

### 2. Output Handler

Add output format selection:
- `generate_stat_block()` - existing Markdown
- `generate_foundry_vtt_json()` - new JSON generation
- `output_both()` - generate both formats

### 3. File Writing

Write JSON to file structure:
```
output/
└── Monsters/
    └── {CreatureName}/
        └── npc_{CreatureName}_{randomId}.json
```

### 4. ID Generation

Use deterministic ID generation for consistency:
- Actor ID: Generated UUID
- Item IDs: Generated UUIDs for each ability/feature
- Effect IDs: Generated UUIDs for each effect

## Open Questions

- [x] Should we generate token images? **Decision:** Use Draw Steel role-based images
- [x] Should we include source citations? **Decision:** Yes, per examples
- [ ] Should we support importing to specific compendium? (Future enhancement)
- [x] What default images to use for generated monsters? **Decision:** Role-based defaults from Draw Steel module

### Future Enhancement: AI Image Generation

If the LLM/model supports image generation, the system MAY generate custom monster images as an optional enhancement.

**Potential Implementation:**
- Accept `--generate-image` flag to create custom monster portrait
- Use model image generation capabilities (DALL-E, Stable Diffusion, etc.)
- Save image to output directory alongside JSON
- Reference image in Foundry JSON for token display

**Considerations:**
- Requires API key or local image generation setup
- May incur costs for image generation
- Quality varies by model and prompt
- Could be triggered automatically or manually
