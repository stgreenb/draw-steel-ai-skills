# Draw Steel Monster Generator

A skill for generating Draw Steel TTRPG monsters with formula-compliant stat blocks.

## Quick Start

**Input Format:** `"Create a [Level] [Creature Name], [Organization], [Role]"`

**Examples:**
- `"Create a Level 3 Gremlin, Minion Harrier"`
- `"Create a Level 5 Red Dragon, Solo Brute"`
- `"Create a Level 1 Kobold Veles, Minion Harrier"`

**New to OpenCode?** See the [Complete Beginner's Guide](opencode-desktop-tutorial.md) for step-by-step setup instructions on Windows.

## What It Does

- Generates Draw Steel monsters using official Monster Basics formulas
- Converts monsters from other systems (D&D 5e, Pathfinder, etc.) - ignores source math, uses for inspiration only
- Creates and validates Foundry VTT-ready JSON for import

## Installation

### Claude Code / OpenCode

1. Copy `.claude/skills/draw-steel-monster-generator/` to your skills directory
2. Restart your LLM tool
3. The skill will be automatically discovered

See [the skill README](.claude/skills/draw-steel-monster-generator/README.md) for detailed platform-specific setup instructions.