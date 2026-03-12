# Foundry VTT JSON Export Reference - Retainers

This document provides the exact JSON structure required when generating Foundry VTT JSON for Draw Steel retainers (v0.11.0).

## Complete Retainer Actor Structure

```json
{
  "name": "Human Warrior",
  "type": "retainer",
  "img": "systems/draw-steel/assets/roles/defender.webp",
  "system": {
    "stamina": {
      "value": null,
      "max": 21,
      "temporary": 0
    },
    "combat": {
      "save": {
        "threshold": 6,
        "bonus": ""
      },
      "size": {
        "value": 1,
        "letter": "M"
      },
      "stability": 0,
      "turns": 1
    },
    "biography": {
      "value": "",
      "director": "",
      "languages": []
    },
    "movement": {
      "value": 5,
      "types": ["walk"],
      "hover": false,
      "disengage": 1
    },
    "damage": {
      "immunities": {
        "all": 0,
        "acid": 0,
        "cold": 0,
        "corruption": 0,
        "fire": 0,
        "holy": 0,
        "lightning": 0,
        "poison": 0,
        "psychic": 0,
        "sonic": 0
      },
      "weaknesses": {
        "all": 0,
        "acid": 0,
        "cold": 0,
        "corruption": 0,
        "fire": 0,
        "holy": 0,
        "lightning": 0,
        "poison": 0,
        "psychic": 0,
        "sonic": 0
      }
    },
    "statuses": {
      "immunities": []
    },
    "characteristics": {
      "might": {"value": 2},
      "agility": {"value": 0},
      "reason": {"value": 0},
      "intuition": {"value": 0},
      "presence": {"value": 1}
    },
    "source": {
      "book": "Monsters",
      "page": "367",
      "license": "Draw Steel Creator License"
    },
    "retainer": {
      "freeStrike": 2,
      "keywords": ["humanoid"],
      "role": "defender"
    },
    "recoveries": {
      "value": 6,
      "max": 6
    }
  },
  "prototypeToken": {
    "name": "Human Warrior",
    "displayName": 20,
    "actorLink": true,
    "width": 1,
    "height": 1,
    "texture": {
      "src": "systems/draw-steel/assets/roles/defender.webp",
      "anchorX": 0.5,
      "anchorY": 0.5,
      "fit": "contain",
      "scaleX": 1,
      "scaleY": 1
    },
    "lockRotation": false,
    "alpha": 1,
    "disposition": 1,
    "displayBars": 0,
    "bar1": {
      "attribute": "stamina"
    },
    "bar2": {
      "attribute": "hero.primary.value"
    }
  },
  "items": [],
  "_stats": {
    "systemId": "draw-steel",
    "systemVersion": "0.11.0"
  },
  "_id": "xxxxxxxxxxxxxxxxxxxxx"
}
```

## Key Differences: Retainer vs Monster

| Aspect | Retainer | Monster |
|--------|----------|---------|
| **Actor Type** | `"retainer"` | `"npc"` |
| **System Object** | `system.retainer` | `system.monster` |
| **Recoveries** | `system.recoveries.value: 6, max: 6` | Not present |
| **EV Field** | Not present | `system.monster.ev` |
| **Organization** | Not present | `system.monster.organization` |
| **Token Disposition** | `1` (friendly) | `-1` (hostile) |
| **Token Display Bars** | `0` (none) | `20` (visible) |
| **Token actorLink** | `true` | Not present |
| **Token bar2** | `"hero.primary.value"` | `"hero.resources"` |

## Retainer-Specific Fields

### system.retainer

```json
"retainer": {
  "freeStrike": 2,
  "keywords": ["humanoid"],
  "role": "defender"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `freeStrike` | integer | Free strike damage value |
| `keywords` | array | Creature type keywords |
| `role` | string | Retainer role (defender, brute, harrier, etc.) |

### system.recoveries

```json
"recoveries": {
  "value": 6,
  "max": 6
}
```

Retainers always have 6 recoveries (like player characters).

### prototypeToken.disposition

| Value | Meaning |
|-------|---------|
| `1` | Friendly (retainers) |
| `-1` | Hostile (monsters) |
| `0` | Neutral |

### prototypeToken.displayBars

| Value | Behavior |
|-------|-----------|
| `0` | No health bar displayed (retainers) |
| `20` | Health bar visible (monsters) |

## Valid Roles

- ambusher
- artillery
- brute
- controller
- defender
- harrier
- hexer
- mount
- support

## Valid Keywords

Valid creature type keywords for retainers:
- abyssal, accursed, animal, beast, construct, dragon, elemental, fey, giant, horror, humanoid, infernal, plant, soulless, swarm, undead

## Item Types for Retainers

Retainers use the same item types as monsters:
- `ability` - Combat abilities
- `feature` - Traits and features

### Ability Item Structure

```json
{
  "name": "Chop (Signature Ability)",
  "type": "ability",
  "system": {
    "type": "main",
    "category": "signature",
    "keywords": ["melee", "weapon"],
    "distance": {
      "type": "melee",
      "primary": 1
    },
    "target": {
      "type": "creature",
      "value": 1
    },
    "power": {
      "roll": {
        "formula": "@chr",
        "characteristics": ["might"]
      },
      "effects": {}
    },
    "effect": {
      "before": "<p><dl class=\"power-roll-display\"><dt class=\"tier1\"><p>!</p></dt><dd><p>3 damage.</p></dd><dt class=\"tier2\"><p>@</p></dt><dd><p>5 damage.</p></dd><dt class=\"tier3\"><p>#</p></dt><dd><p>7 damage.</p></dd></dl></p>",
      "after": ""
    },
    "source": {
      "book": "Monsters",
      "page": "",
      "license": "Draw Steel Creator License"
    }
  }
}
```

### Feature/Trait Item Structure

```json
{
  "name": "Supernatural Insight",
  "type": "feature",
  "system": {
    "description": {
      "value": "<p>The warrior ignores concealment if it's granted by a supernatural effect.</p>",
      "director": ""
    },
    "source": {
      "book": "Monsters",
      "license": "Draw Steel Creator License"
    }
  }
}
```

## Critical Rules

### DO:
- Use `type: "retainer"` (NOT `"npc"`)
- Use `system.retainer` (NOT `system.monster`)
- Set `system.recoveries.value: 6, max: 6`
- Set `prototypeToken.disposition: 1` for friendly
- Set `prototypeToken.displayBars: 0` (no health bar)
- Set `prototypeToken.actorLink: true`
- Use role-based token images

### DON'T:
- Don't add EV field to retainers
- Don't use `type: "npc"` - that's for monsters
- Don't use `system.monster` - use `system.retainer`
- Don't add organization field (not applicable to retainers)

## v0.11.0 Changes

This document reflects the v0.11.0 Foundry VTT system format. Key additions from earlier versions:
- New actor type: `"retainer"`
- New item type: `"follower"` (for tracking follower relationships on hero sheets)
- Retainers use `system.recoveries` field

The follower item type (`type: "follower"`) is used on hero actors to track which retainers serve them, but is not part of the retainer actor itself.
