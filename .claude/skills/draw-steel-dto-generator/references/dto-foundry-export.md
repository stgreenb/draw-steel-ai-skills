# Foundry VTT Object Actor Export Reference

This document provides the exact JSON structure required when generating Foundry VTT Object actor JSON for the Draw Steel system (v0.10.0+).

## Complete Object Actor Structure

```json
{
  "name": "Bear Trap",
  "type": "object",
  "img": "systems/draw-steel/assets/roles/ambusher.webp",
  "system": {
    "stamina": {
      "value": 6,
      "max": 6,
      "temporary": 0
    },
    "characteristics": {
      "might": {"value": 0, "banes": 0, "edges": 0},
      "agility": {"value": 0, "banes": 0, "edges": 0},
      "reason": {"value": 0, "banes": 0, "edges": 0},
      "intuition": {"value": 0, "banes": 0, "edges": 0},
      "presence": {"value": 0, "banes": 0, "edges": 0}
    },
    "combat": {
      "save": {"threshold": 6, "bonus": ""},
      "size": {"value": 1, "letter": "S"},
      "stability": 0,
      "turns": 0
    },
    "movement": null,
    "damage": {
      "immunities": {"all": 0},
      "weaknesses": {}
    },
    "statuses": {
      "canFlank": false
    },
    "biography": {
      "value": "",
      "director": ""
    },
    "source": {
      "book": "Dynamic Terrain",
      "page": "",
      "license": "Draw Steel Creator License"
    },
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
    "bar1": {"attribute": "stamina"},
    "width": 1,
    "height": 1,
    "disposition": -1,
    "texture": {
      "src": "systems/draw-steel/assets/roles/ambusher.webp"
    }
  },
  "items": [],
  "_stats": {
    "systemId": "draw-steel",
    "systemVersion": "0.10.0"
  },
  "_id": "BearTrapObject001"
}
```

## Object Category Mapping

| DTO Category | Object `category` | Example |
|--------------|-------------------|---------|
| Environmental Hazard | `hazard` | Lava, Brambles, Quicksand |
| Fieldwork (Trap) | `trap` | Bear Trap, Snare Trap, Spike Trap |
| Fieldwork (Fortification) | `fortification` | Pavise Shield, Archer's Stakes |
| Mechanism (Trap) | `trap` | Dart Trap, Column of Blades |
| Mechanism (Trigger) | `trigger` | Pressure Plate, Switch |
| Mechanism (Fortification) | `fortification` | Pillar, Portcullis, Ram |
| Siege Engine | `siegeEngine` | Arrow Launcher, Catapult, Iron Dragon |
| Power Fixture | `relic` | Holy Idol, Tree of Might, Psionic Shard |
| Supernatural Object | `relic` | Black Obelisk, Throne of A'An |

## Object Fields Reference

### Core Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Always `"object"` for DTOs |
| `name` | string | Yes | DTO name |
| `img` | string | No | Image path (defaults to system icon) |

### system.object Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `level` | integer | Yes | DTO level (typically 1-5) |
| `category` | string | Yes | One of: `hazard`, `trap`, `trigger`, `siegeEngine`, `relic`, `fortification` |
| `role` | string | No | Same roles as monsters, or `""` |
| `area` | integer/null | No | Number of squares for multi-square DTOs |
| `squareStamina` | boolean | No | `true` if stamina is per-square |

### system.movement

| Value | When to Use |
|-------|-------------|
| `null` | Static objects (most DTOs) |
| `{"value": 3, "types": ["walk"], "hover": false, "disengage": 0}` | Mobile siege engines or moving hazards |

### system.statuses.canFlank

| Value | When to Use |
|-------|-------------|
| `false` | Default for objects - most cannot flank |
| `true` | Rare - only for objects that can coordinate attacks |

## Stamina Patterns

### Fixed Stamina (Single Object)

```json
{
  "stamina": {"value": 6, "max": 6, "temporary": 0},
  "object": {
    "area": null,
    "squareStamina": false
  }
}
```

**Examples:** Bear Trap (6), Dart Trap (3), Holy Idol (35), Black Obelisk (100)

### Per-Square Stamina (Multi-Square Terrain)

```json
{
  "stamina": {"value": 3, "max": 3, "temporary": 0},
  "object": {
    "area": 4,
    "squareStamina": true
  }
}
```

**Examples:** Brambles (3/sq), Lava (12/sq), Archer's Stakes (3/sq)

### No Stamina (Indestructible or Trigger)

```json
{
  "stamina": {"value": 0, "max": 0, "temporary": 0},
  "object": {
    "area": null,
    "squareStamina": false
  }
}
```

**Examples:** Pressure Plate, Quicksand (-), Hidey-Hole (-)

## Damage Immunities

For durable DTOs like Lava or Corrosive Pool:

```json
{
  "damage": {
    "immunities": {
      "all": 20
    },
    "weaknesses": {
      "cold": 5
    }
  }
}
```

## Object Ability Structure

DTO abilities use the same structure as monster abilities:

```json
{
  "name": "Bear Trap",
  "type": "ability",
  "system": {
    "type": "freeTriggered",
    "category": "signature",
    "keywords": ["melee", "strike", "weapon"],
    "distance": {"type": "melee", "primary": 0},
    "target": {"type": "creatureObject", "value": 1},
    "damageDisplay": "melee",
    "power": {
      "roll": {"formula": "@chr", "characteristics": ["agility"]},
      "effects": {
        "effect001": {
          "_id": "effect001",
          "type": "damage",
          "damage": {
            "tier1": {"value": "1", "types": [], "properties": []},
            "tier2": {"value": "3", "types": [], "properties": []},
            "tier3": {"value": "5", "types": [], "properties": []}
          }
        }
      }
    },
    "effect": {
      "before": "",
      "after": "<p>The bear trap must be manually reset.</p>"
    },
    "spend": {"text": "", "value": null},
    "source": {"book": "Dynamic Terrain", "license": "Draw Steel Creator License"}
  },
  "_id": "BearTrapAbility001"
}
```

## Ability Types for DTOs

| Ability Type | When to Use | Example |
|--------------|-------------|---------|
| `freeTriggered` | Most DTO activations (triggered when condition met) | Bear Trap, Lava, Dart Trap |
| `main` | Siege engine abilities (requires operator) | Arrow Storm, Reload, Spot |
| `maneuver` | Special positioning (rare for DTOs) | Move (mobile siege engines) |
| `none` | Passive effects | Empowered Will (Holy Idol) |

## Complete Examples

### Bear Trap (Level 1 Trap Ambusher)

```json
{
  "name": "Bear Trap",
  "type": "object",
  "img": "systems/draw-steel/assets/roles/ambusher.webp",
  "system": {
    "stamina": {"value": 6, "max": 6, "temporary": 0},
    "characteristics": {
      "might": {"value": 0, "banes": 0, "edges": 0},
      "agility": {"value": 0, "banes": 0, "edges": 0},
      "reason": {"value": 0, "banes": 0, "edges": 0},
      "intuition": {"value": 0, "banes": 0, "edges": 0},
      "presence": {"value": 0, "banes": 0, "edges": 0}
    },
    "combat": {
      "save": {"threshold": 6, "bonus": ""},
      "size": {"value": 1, "letter": "S"},
      "stability": 0,
      "turns": 0
    },
    "movement": null,
    "damage": {"immunities": {"all": 0}, "weaknesses": {}},
    "statuses": {"canFlank": false},
    "biography": {"value": "", "director": ""},
    "source": {"book": "Dynamic Terrain", "page": "", "license": "Draw Steel Creator License"},
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
    "bar1": {"attribute": "stamina"},
    "width": 1,
    "height": 1,
    "disposition": -1,
    "texture": {"src": "systems/draw-steel/assets/roles/ambusher.webp"}
  },
  "items": [
    {
      "name": "Bear Trap",
      "type": "ability",
      "system": {
        "type": "freeTriggered",
        "category": "signature",
        "keywords": ["melee", "strike", "weapon"],
        "distance": {"type": "melee", "primary": 0},
        "target": {"type": "creatureObject", "value": 1},
        "damageDisplay": "melee",
        "power": {
          "roll": {"formula": "@chr", "characteristics": ["agility"]},
          "effects": {
            "effect001": {
              "_id": "effect001",
              "type": "damage",
              "damage": {
                "tier1": {"value": "1", "types": [], "properties": []},
                "tier2": {"value": "3", "types": [], "properties": []},
                "tier3": {"value": "5", "types": [], "properties": []}
              }
            },
            "effect002": {
              "_id": "effect002",
              "type": "applied",
              "applied": {
                "tier1": {"display": "", "potency": {"value": "@potency.weak", "characteristic": "agility"}},
                "tier2": {"display": "{{potency}} slowed (save ends)", "potency": {"value": "-1", "characteristic": "agility"}},
                "tier3": {"display": "{{potency}} slowed (save ends)", "potency": {"value": "-2", "characteristic": "agility"}}
              }
            }
          }
        },
        "effect": {"before": "", "after": "<p>The bear trap must be manually reset.</p>"},
        "spend": {"text": "", "value": null},
        "source": {"book": "Dynamic Terrain", "license": "Draw Steel Creator License"}
      },
      "_id": "BearTrapAbility001"
    },
    {
      "name": "Hidden",
      "type": "feature",
      "system": {
        "description": {"value": "<p>The bear trap is hidden until triggered or detected.</p>", "director": ""},
        "source": {"book": "Dynamic Terrain", "license": "Draw Steel Creator License"}
      },
      "_id": "BearTrapHidden001"
    }
  ],
  "_stats": {"systemId": "draw-steel", "systemVersion": "0.10.0"},
  "_id": "BearTrapObject001"
}
```

### Lava (Level 3 Hazard Hexer)

```json
{
  "name": "Lava",
  "type": "object",
  "img": "systems/draw-steel/assets/roles/hexer.webp",
  "system": {
    "stamina": {"value": 12, "max": 12, "temporary": 0},
    "characteristics": {
      "might": {"value": 0, "banes": 0, "edges": 0},
      "agility": {"value": 0, "banes": 0, "edges": 0},
      "reason": {"value": 0, "banes": 0, "edges": 0},
      "intuition": {"value": 0, "banes": 0, "edges": 0},
      "presence": {"value": 0, "banes": 0, "edges": 0}
    },
    "combat": {
      "save": {"threshold": 6, "bonus": ""},
      "size": {"value": 1, "letter": "M"},
      "stability": 0,
      "turns": 0
    },
    "movement": null,
    "damage": {
      "immunities": {"all": 20},
      "weaknesses": {"cold": 5}
    },
    "statuses": {"canFlank": false},
    "biography": {"value": "", "director": ""},
    "source": {"book": "Dynamic Terrain", "page": "", "license": "Draw Steel Creator License"},
    "object": {
      "level": 3,
      "category": "hazard",
      "role": "hexer",
      "area": 4,
      "squareStamina": true
    }
  },
  "prototypeToken": {
    "name": "Lava",
    "displayName": 20,
    "displayBars": 20,
    "bar1": {"attribute": "stamina"},
    "width": 1,
    "height": 1,
    "disposition": -1,
    "texture": {"src": "systems/draw-steel/assets/roles/hexer.webp"}
  },
  "items": [
    {
      "name": "Liquid Hot Magma",
      "type": "ability",
      "system": {
        "type": "freeTriggered",
        "category": "signature",
        "keywords": ["melee", "strike"],
        "distance": {"type": "melee", "primary": 1},
        "target": {"type": "creatureObject", "value": 1},
        "damageDisplay": "melee",
        "power": {
          "roll": {"formula": "@chr", "characteristics": ["might"]},
          "effects": {
            "effect001": {
              "_id": "effect001",
              "type": "damage",
              "damage": {
                "tier1": {"value": "5", "types": ["fire"], "properties": []},
                "tier2": {"value": "9", "types": ["fire"], "properties": []},
                "tier3": {"value": "12", "types": ["fire"], "properties": []}
              }
            },
            "effect002": {
              "_id": "effect002",
              "type": "applied",
              "applied": {
                "tier1": {"display": "{{potency}} burning (save ends)", "potency": {"value": "-1", "characteristic": "might"}},
                "tier2": {"display": "{{potency}} burning (save ends)", "potency": {"value": "-2", "characteristic": "might"}},
                "tier3": {"display": "{{potency}} burning (save ends)", "potency": {"value": "-3", "characteristic": "might"}}
              }
            }
          }
        },
        "effect": {"before": "", "after": ""},
        "spend": {"text": "", "value": null},
        "source": {"book": "Dynamic Terrain", "license": "Draw Steel Creator License"}
      },
      "_id": "LavaAbility001"
    }
  ],
  "_stats": {"systemId": "draw-steel", "systemVersion": "0.10.0"},
  "_id": "LavaObject001"
}
```

### Arrow Launcher (Level 2 Siege Engine Artillery)

```json
{
  "name": "Arrow Launcher",
  "type": "object",
  "img": "systems/draw-steel/assets/roles/artillery.webp",
  "system": {
    "stamina": {"value": 30, "max": 30, "temporary": 0},
    "characteristics": {
      "might": {"value": 0, "banes": 0, "edges": 0},
      "agility": {"value": 0, "banes": 0, "edges": 0},
      "reason": {"value": 0, "banes": 0, "edges": 0},
      "intuition": {"value": 0, "banes": 0, "edges": 0},
      "presence": {"value": 0, "banes": 0, "edges": 0}
    },
    "combat": {
      "save": {"threshold": 6, "bonus": ""},
      "size": {"value": 1, "letter": "L"},
      "stability": 0,
      "turns": 0
    },
    "movement": null,
    "damage": {"immunities": {"all": 0}, "weaknesses": {}},
    "statuses": {"canFlank": false},
    "biography": {"value": "", "director": ""},
    "source": {"book": "Dynamic Terrain", "page": "", "license": "Draw Steel Creator License"},
    "object": {
      "level": 2,
      "category": "siegeEngine",
      "role": "artillery",
      "area": null,
      "squareStamina": false
    }
  },
  "prototypeToken": {
    "name": "Arrow Launcher",
    "displayName": 20,
    "displayBars": 20,
    "bar1": {"attribute": "stamina"},
    "width": 1,
    "height": 1,
    "disposition": -1,
    "texture": {"src": "systems/draw-steel/assets/roles/artillery.webp"}
  },
  "items": [
    {
      "name": "Arrow Storm",
      "type": "ability",
      "system": {
        "type": "main",
        "category": "signature",
        "keywords": ["area", "ranged", "weapon"],
        "distance": {"type": "cube", "primary": 5},
        "target": {"type": "creatureObject", "value": null, "custom": "Each creature and object in the area"},
        "damageDisplay": "",
        "power": {
          "roll": {"formula": "@chr", "characteristics": ["agility"]},
          "effects": {
            "effect001": {
              "_id": "effect001",
              "type": "damage",
              "damage": {
                "tier1": {"value": "5", "types": [], "properties": []},
                "tier2": {"value": "8", "types": [], "properties": []},
                "tier3": {"value": "11", "types": [], "properties": []}
              }
            }
          }
        },
        "effect": {"before": "", "after": "<p>This ability can't be used again until the arrow launcher is reloaded.</p>"},
        "spend": {"text": "", "value": null},
        "source": {"book": "Dynamic Terrain", "license": "Draw Steel Creator License"}
      },
      "_id": "ArrowStormAbility001"
    },
    {
      "name": "Reload",
      "type": "ability",
      "system": {
        "type": "main",
        "category": "heroic",
        "keywords": [],
        "distance": {"type": "self"},
        "target": {"type": "self"},
        "damageDisplay": "",
        "power": {"roll": {"formula": "@chr", "characteristics": []}, "effects": {}},
        "effect": {"before": "", "after": "<p>The arrow launcher is reloaded, allowing Arrow Storm to be used again. This action can be used only once per round.</p>"},
        "spend": {"text": "", "value": null},
        "source": {"book": "Dynamic Terrain", "license": "Draw Steel Creator License"}
      },
      "_id": "ReloadAbility001"
    },
    {
      "name": "Spot",
      "type": "ability",
      "system": {
        "type": "main",
        "category": "heroic",
        "keywords": [],
        "distance": {"type": "self"},
        "target": {"type": "self"},
        "damageDisplay": "",
        "power": {"roll": {"formula": "@chr", "characteristics": []}, "effects": {}},
        "effect": {"before": "", "after": "<p>The next use of Arrow Storm gains an edge and has a +10 bonus to ranged distance. This action can be used only once per round.</p>"},
        "spend": {"text": "", "value": null},
        "source": {"book": "Dynamic Terrain", "license": "Draw Steel Creator License"}
      },
      "_id": "SpotAbility001"
    },
    {
      "name": "Move",
      "type": "ability",
      "system": {
        "type": "main",
        "category": "heroic",
        "keywords": [],
        "distance": {"type": "self"},
        "target": {"type": "self"},
        "damageDisplay": "",
        "power": {"roll": {"formula": "@chr", "characteristics": []}, "effects": {}},
        "effect": {"before": "", "after": "<p>The arrow launcher and the creature using this action move together up to 3 squares.</p>"},
        "spend": {"text": "", "value": null},
        "source": {"book": "Dynamic Terrain", "license": "Draw Steel Creator License"}
      },
      "_id": "MoveAbility001"
    }
  ],
  "_stats": {"systemId": "draw-steel", "systemVersion": "0.10.0"},
  "_id": "ArrowLauncherObject001"
}
```

## Critical Rules

### DO:
- Use `type: "object"` for DTOs
- Use `movement: null` for static objects
- Use `system.object.category` for DTO type
- Use `system.statuses.canFlank: false` for most objects
- Use same ability structure as monsters
- Use `_stats.systemVersion: "0.10.0"`

### DON'T:
- Don't use `type: "npc"` for DTOs
- Don't use `movement: {value: 0}` for static objects - use `null`
- Don't use monster-specific fields like `monster.role` - use `object.role`
- Don't forget `canFlank` field in statuses
