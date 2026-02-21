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
      "immunities": {"all": 0, "acid": 0, "cold": 0, "corruption": 0, "fire": 0, "holy": 0, "lightning": 0, "poison": 0, "psychic": 0, "sonic": 0},
      "weaknesses": {"all": 0, "acid": 0, "cold": 0, "corruption": 0, "fire": 0, "holy": 0, "lightning": 0, "poison": 0, "psychic": 0, "sonic": 0}
    },
    "statuses": {
      "immunities": []
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
    "ev": 2,
    "object": {
      "level": 1,
      "category": "trap",
      "role": "ambusher",
      "area": "",
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
  "_id": "aB3cD4eF5gH6iJ7k"
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
| `role` | string | Yes | Same roles as monsters (e.g., `defender`, `hexer`, `ambusher`) |
| `area` | string | Yes | Number of squares as string (e.g., `"4"`) or `""` for single-square |
| `squareStamina` | boolean | No | `true` if stamina is per-square |

### system.ev

**REQUIRED** - Encounter Value for the DTO:

| DTO Type | Typical EV |
|----------|------------|
| Level 1 Hazard/Trap | 1-2 |
| Level 2 Hazard | 2-3 |
| Level 3 Hazard | 3-4 |
| Level 2 Siege Engine | 8 |
| Level 3 Siege Engine | 10 |
| Level 3 Supernatural Object | 20 |

### system.movement

| Value | When to Use |
|-------|-------------|
| `null` | Static objects (most DTOs) |
| `{"value": 3, "types": ["walk"], "hover": false, "disengage": null}` | Mobile siege engines or moving hazards |

### system.statuses

Objects use `immunities` array, not `canFlank`:

```json
"statuses": {
  "immunities": []
}
```

## Stamina Patterns

### Fixed Stamina (Single Object)

```json
{
  "stamina": {"value": 6, "max": 6, "temporary": 0},
  "ev": 2,
  "object": {
    "area": "",
    "squareStamina": false
  }
}
```

**Examples:** Bear Trap (6, EV 2), Dart Trap (3, EV 1), Holy Idol (35, EV 7), Black Obelisk (100, EV 20)

### Per-Square Stamina (Multi-Square Terrain)

```json
{
  "stamina": {"value": 3, "max": 3, "temporary": 0},
  "ev": 1,
  "object": {
    "area": "4",
    "squareStamina": true
  }
}
```

**Examples:** Brambles (3/sq, EV 1/10×10), Lava (12/sq, EV 4/10×10), Archer's Stakes (3/sq, EV 2)

### No Stamina (Indestructible or Trigger)

```json
{
  "stamina": {"value": null, "max": 0, "temporary": 0},
  "ev": 2,
  "object": {
    "area": "",
    "squareStamina": false
  }
}
```

**Examples:** Pressure Plate (EV 2), Quicksand (EV varies), Hidey-Hole (EV 1)

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
        "aB1cD2eF3gH4iJ5k": {
          "_id": "aB1cD2eF3gH4iJ5k",
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
  "_id": "K9mN2pQ8rS4tU6vW"
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
    "damage": {"immunities": {"all": 0, "acid": 0, "cold": 0, "corruption": 0, "fire": 0, "holy": 0, "lightning": 0, "poison": 0, "psychic": 0, "sonic": 0}, "weaknesses": {"all": 0, "acid": 0, "cold": 0, "corruption": 0, "fire": 0, "holy": 0, "lightning": 0, "poison": 0, "psychic": 0, "sonic": 0}},
    "statuses": {"immunities": []},
    "biography": {"value": "", "director": ""},
    "source": {"book": "Dynamic Terrain", "page": "", "license": "Draw Steel Creator License"},
    "ev": 2,
    "object": {
      "level": 1,
      "category": "trap",
      "role": "ambusher",
      "area": "",
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
      "name": "Deactivate",
      "type": "feature",
      "img": "icons/commodities/tech/console-steel.webp",
      "system": {
        "description": {"value": "<p>As a maneuver, a creature adjacent to a bear trap can make an Agility test.</p><ul><li><strong>≤11:</strong> The creature triggers the trap.</li><li><strong>12-16:</strong> The trap is deactivated but the creature is slowed (EoT).</li><li><strong>17+:</strong> The trap is deactivated and doesn't trigger.</li></ul>", "director": ""},
        "source": {"book": "Dynamic Terrain", "license": "Draw Steel Creator License"}
      },
      "_id": "X5yZ7aB2cD8eF4gH"
    },
    {
      "name": "Activate",
      "type": "feature",
      "img": "icons/skills/targeting/crosshair-ringed-gray.webp",
      "system": {
        "description": {"value": "<p>The bear trap is calibrated to be triggered by creatures or objects of a particular size. The trap triggers when a creature or object of the appropriate size enters its space.</p><p><strong>Effect:</strong> A triggering creature or object ends their movement and is targeted by the Bear Trap ability.</p>", "director": ""},
        "source": {"book": "Dynamic Terrain", "license": "Draw Steel Creator License"}
      },
            "_id": "Q1wE2rT3yU4iO5pA"
    },
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
            "aB1cD2eF3gH4iJ5k": {
              "_id": "aB1cD2eF3gH4iJ5k",
              "type": "damage",
              "damage": {
                "tier1": {"value": "1", "types": [], "properties": []},
                "tier2": {"value": "3", "types": [], "properties": []},
                "tier3": {"value": "5", "types": [], "properties": []}
              }
            },
            "lM6nO7pQ8rS9tU0v": {
              "_id": "lM6nO7pQ8rS9tU0v",
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
"_id": "K9mN2pQ8rS4tU6vW"
    },
    {
      "name": "Hidden",
      "type": "feature",
      "system": {
        "description": {"value": "<p>The bear trap is hidden until triggered or detected.</p>", "director": ""},
        "source": {"book": "Dynamic Terrain", "license": "Draw Steel Creator License"}
      },
            "_id": "L6kJ7hG8fD9sA2zX"
    }
  ],
  "_stats": {"systemId": "draw-steel", "systemVersion": "0.10.0"},
    "_id": "M3nP4qR5sT6uV7wX"
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
      "immunities": {"all": 20, "acid": 0, "cold": 0, "corruption": 0, "fire": 0, "holy": 0, "lightning": 0, "poison": 0, "psychic": 0, "sonic": 0},
      "weaknesses": {"all": 0, "acid": 0, "cold": 5, "corruption": 0, "fire": 0, "holy": 0, "lightning": 0, "poison": 0, "psychic": 0, "sonic": 0}
    },
    "statuses": {"immunities": []},
    "biography": {"value": "", "director": ""},
    "source": {"book": "Dynamic Terrain", "page": "", "license": "Draw Steel Creator License"},
    "ev": 4,
    "object": {
      "level": 3,
      "category": "hazard",
      "role": "hexer",
      "area": "",
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
      "name": "Deactivate",
      "type": "feature",
      "img": "icons/commodities/tech/console-steel.webp",
      "system": {
        "description": {"value": "<p>Each square of lava must be individually destroyed.</p>", "director": ""},
        "source": {"book": "Dynamic Terrain", "license": "Draw Steel Creator License"}
      },
      "_id": "W2xE3yC4zV5bN6mQ"
    },
    {
      "name": "Activate",
      "type": "feature",
      "img": "icons/skills/targeting/crosshair-ringed-gray.webp",
      "system": {
        "description": {"value": "<p>A creature or object enters the lava or starts their turn there, or starts their turn adjacent to the lava.</p><p><strong>Effect:</strong> The Liquid Hot Magma ability.</p>", "director": ""},
        "source": {"book": "Dynamic Terrain", "license": "Draw Steel Creator License"}
      },
      "_id": "K7jH8gF6dS5aZ9xW"
    },
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
            "aB1cD2eF3gH4iJ5k": {
              "_id": "aB1cD2eF3gH4iJ5k",
              "type": "damage",
              "damage": {
                "tier1": {"value": "5", "types": ["fire"], "properties": []},
                "tier2": {"value": "9", "types": ["fire"], "properties": []},
                "tier3": {"value": "12", "types": ["fire"], "properties": []}
              }
            },
            "lM6nO7pQ8rS9tU0v": {
              "_id": "lM6nO7pQ8rS9tU0v",
              "type": "applied",
              "applied": {
                "tier1": {"display": "{{potency}} burning (save ends)", "potency": {"value": "-1", "characteristic": "might"}},
                "tier2": {"display": "{{potency}} burning (save ends)", "potency": {"value": "-2", "characteristic": "might"}},
                "tier3": {"display": "{{potency}} burning (save ends)", "potency": {"value": "-3", "characteristic": "might"}}
              }
            }
          }
        },
        "effect": {"before": "", "after": "<p>A burning creature takes 1d6 fire damage at the start of each of their turns.</p>"},
        "spend": {"text": "", "value": null},
        "source": {"book": "Dynamic Terrain", "license": "Draw Steel Creator License"}
      },
      "_id": "P1oI2uY3tR4eW5qA"
    }
  ],
  "_stats": {"systemId": "draw-steel", "systemVersion": "0.10.0"},
  "_id": "S6dF7gH8jK3lZ9xC"
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
    "damage": {"immunities": {"all": 0, "acid": 0, "cold": 0, "corruption": 0, "fire": 0, "holy": 0, "lightning": 0, "poison": 0, "psychic": 0, "sonic": 0}, "weaknesses": {"all": 0, "acid": 0, "cold": 0, "corruption": 0, "fire": 0, "holy": 0, "lightning": 0, "poison": 0, "psychic": 0, "sonic": 0}},
    "statuses": {"immunities": []},
    "biography": {"value": "", "director": ""},
    "source": {"book": "Dynamic Terrain", "page": "", "license": "Draw Steel Creator License"},
    "ev": 8,
    "object": {
      "level": 2,
      "category": "siegeEngine",
      "role": "artillery",
      "area": "",
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
            "aB1cD2eF3gH4iJ5k": {
              "_id": "aB1cD2eF3gH4iJ5k",
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
      "_id": "N4bV5cX6zL7kM8pQ"
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
      "_id": "J9hG6fD4sA3zX2wE"
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
      "_id": "T5yU8iO1pA4sD7fG"
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
      "_id": "H2jK5lZ9xC3vB6nM"
    }
  ],
  "_stats": {"systemId": "draw-steel", "systemVersion": "0.10.0"},
  "_id": "Q8wE7rT6yU5iO4pA"
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
