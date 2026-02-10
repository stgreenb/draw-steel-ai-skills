# Change: Add Dynamic Terrain Objectives Support

## Why

The current Draw Steel monster generator skill is focused exclusively on monsters, but Draw Steel also includes Dynamic Terrain Objectives (DTOs) - traps, hazards, fieldworks, mechanisms, siege engines, and supernatural objects. Unlike monsters, DTOs have no published mathematical formulas for EV, Stamina, or damage. This proposal reverse-engineers patterns from the published DTO chapter to enable LLMs to generate formula-compliant DTOs.

## What Changes

- Add new capability: `dynamic-terrain-objectives` for generating Draw Steel DTOs
- Extract and document patterns from 30+ published DTO examples
- Create guidance for DTO stat block generation including:
  - EV estimation formulas by DTO category
  - Stamina calculation patterns
  - Power roll damage ranges by level
  - Deactivate/Activate/Effect structure
  - Upgrade system with EV costs
- No Foundry VTT requirements (DTOs are not currently supported in Foundry)

## Impact

- Affected specs: New capability `dynamic-terrain-objectives`
- Affected code: New skill file `.claude/skills/dynamic-terrain-objectives-generator.md`
- Extends monster generator to support DTOs alongside monsters