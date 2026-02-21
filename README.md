# Draw Steel AI Skills

AI skills for generating Draw Steel TTRPG content with formula-compliant stat blocks. Works with Claude Code, OpenCode, Cursor, and other LLM tools.

## Skills

| Skill | Description |
|-------|-------------|
| **Monster Generator** | Creates monsters with organization, roles, abilities, and Foundry VTT export |
| **DTO Generator** | Creates Dynamic Terrain Objectives (traps, hazards, siege engines, fieldworks) |
| **Reward Generator** | Creates treasures (consumables, trinkets, leveled) and titles |
| **Retainer Generator** | Creates NPC followers with mentor relationships and advancement |

## Quick Start

### Monsters

**Input Format:** `"Create a [Level] [Creature Name], [Organization], [Role]"`

**Examples:**
- `"Create a Level 3 Gremlin, Minion Harrier"`
- `"Create a Level 5 Red Dragon, Solo Brute"`

### Dynamic Terrain Objectives (DTOs)

**Input Format:** `"Create a Level [X] [Category] [Name]"`

**Examples:**
- `"Create a Level 2 Environmental Hazard Acidic Bog"`
- `"Create a Level 1 Fieldwork Snap Trap"`
- `"Create a Level 3 Siege Engine Scorpion Ballista"`

### Rewards

**Input Format:** `"Create a Level [X] [Type] [Name]"`

**Examples:**
- `"Create a Level 3 Treasure Crown of Shadows"`
- `"Create a Level 5 Title Dragonslayer"`

**Don't have a LLM enviroment? Try OpenCode?** See the [Complete Beginner's Guide](opencode-desktop-tutorial.md) for step-by-step setup instructions on Windows.

## What It Does

- Generates Draw Steel monsters using official Monster Basics formulas
- Creates Dynamic Terrain Objectives (traps, hazards, mechanisms, siege engines, power fixtures, supernatural objects)
- Generates retainers (NPC followers) with advancement abilities
- Generates treasures and titles as rewards
- Converts content from other systems (D&D 5e, Pathfinder, etc.) - ignores source math, uses for inspiration only
- Creates and validates Foundry VTT-ready JSON for import

## Installation

### Claude Code / OpenCode

1. Copy `.claude/skills/` directory to your project
2. Restart your LLM tool
3. Skills will be automatically discovered

See [the monster skill README](.claude/skills/draw-steel-monster-generator/README.md) for detailed platform-specific setup instructions.
