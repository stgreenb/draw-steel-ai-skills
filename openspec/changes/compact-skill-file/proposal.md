# Change: Compact Skill File to Follow Agent Skills Specification

## Why

The current `SKILL.md` file is 2,487 lines (91,280 bytes), far exceeding the Agent Skills specification's recommendation of under 500 lines and 5000 tokens for the body content. This causes truncation when loaded by LLMs, preventing users from accessing critical instructions. The specification explicitly recommends progressive disclosure: keep SKILL.md under 500 lines and move detailed reference material to separate files in the `references/` directory.

**Critical issue:** The file contains massive duplication (validation workflow repeated 3+ times) and extensive examples that could be loaded on-demand. However, we must keep all CRITICAL rules visible even if SKILL.md is slightly oversized.

## What Changes

- **BREAKING**: Restructure SKILL.md to follow progressive disclosure pattern with conservative approach
- **Consolidate duplicated content**: Merge 3+ repeated validation workflow sections into one
- **Keep in SKILL.md** (prioritized, may be up to ~600 lines):
  - Quick Start instructions
  - Core validation workflow (single consolidated version)
  - CRITICAL format rules checklist (all items marked "CRITICAL", "MANDATORY", "REQUIRED")
  - Generation workflow steps
  - Common pitfalls section
  - Task-specific file references with explicit "WHEN" triggers
- **Move to references/** (task-driven, action-oriented):
  - `FOUNDRY_JSON_SCHEMA.md` - Complete JSON schema and examples (load when generating Foundry format)
  - `DETAILED_RULES.md` - Extended DO/DON'T tables and edge cases (load when debugging)
  - `FORMULAS_AND_TABLES.md` - Stat calculation formulas and lookup tables (load when calculating stats)
  - `ABILITY_EXAMPLES.md` - Ability type examples and patterns (load when designing abilities)
- **Add strategic file references** with clear triggers:
  - "WHEN generating Foundry format, see `references/FOUNDRY_JSON_SCHEMA.md`"
  - "WHEN debugging validation errors, see `references/DETAILED_RULES.md`"
  - "WHEN calculating stats, see `references/FORMULAS_AND_TABLES.md`"
  - "WHEN designing abilities, see `references/ABILITY_EXAMPLES.md`"
- Ensure all file references are one level deep from SKILL.md (per specification)

## Impact

- Affected specs: `skill-format` (progressive disclosure requirement)
- Affected code: `.claude/skills/draw-steel-monster-generator/SKILL.md`
- Affected directories: `.claude/skills/draw-steel-monster-generator/references/`
- Benefits: Reduces SKILL.md from 2,487 lines to ~550-600 lines, prevents truncation, keeps all CRITICAL rules visible, consolidates duplication, improves reference file discoverability with explicit triggers