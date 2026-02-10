# Change: Update Foundry JSON patterns to match official Draw Steel

## Why

Generated monsters from LLMs using the skill show patterns that don't match official Draw Steel monsters, causing Foundry VTT crashes and incorrect behavior. Analysis of 6 generated monsters vs official Draw Steel monsters revealed several systematic differences in JSON structure.

## What Changes

- Add "weapon" keyword to all strike ability examples (all official strikes include it)
- Update target type from "creature" to "creatureObject" for strike abilities (more common pattern)
- Add example with "charge" keyword for charge attacks (with note that it's optional)
- Fix breath/spew ability keywords from incorrect types like "fire" to correct `['area', 'magic']` patterns
- Add "custom" field examples for area targets to improve clarity
- Add examples of different ability types: maneuver, freeTriggered, none (currently only "main" is shown)
- **DO NOT** add villain action examples - these are very specific to Solo/Leader only and always come in sets of 3 (opener, crowd control, ult)
- Add guidance that LLMs should use examples as inspiration, not copy them verbatim

## Impact

- Affected specs: foundry-json (new spec for Foundry VTT JSON structure)
- Affected code: `.claude/skills/draw-steel-monster-generator/SKILL.md`
- Breaking changes: None (documentation only)
- User impact: Generated monsters will now match official Draw Steel patterns and avoid Foundry VTT crashes