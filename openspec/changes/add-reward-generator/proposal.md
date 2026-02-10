# Change: Add Reward Generator Support

## Why

The Draw Steel monster generator skill currently only supports generating monsters and DTOs, but Draw Steel includes a rich Rewards system with Treasures (consumables, trinkets, leveled treasures, artifacts) and Titles. Unlike DTOs which have no published math, Rewards have clear patterns for crafting (project goals, prerequisites) and scaling. This proposal reverse-engineers patterns from the published Rewards chapter to enable LLMs to generate formula-compliant rewards.

## What Changes

- Add new capability: `reward-generator` for generating Draw Steel Rewards
- Extract and document patterns from 100+ published treasure examples across 4 treasure types
- Extract and document patterns from 50+ published title examples
- Create guidance for reward generation including:
  - Project goal formulas by treasure type and echelon
  - Item prerequisite patterns
  - Effect structure by treasure type
  - Title prerequisite and benefit patterns
  - Leveled treasure scaling (1st, 5th, 9th level)
- Include Foundry VTT JSON export support (rewards are supported in Foundry)

## Impact

- Affected specs: New capability `reward-generator`
- Affected code: New skill file `.claude/skills/reward-generator.md`
- Extends generator to support rewards alongside monsters and DTOs
- Foundry VTT compendium export for treasures and titles