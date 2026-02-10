# Change: Add ID Generator Script for Foundry VTT

## Why

LLMs frequently struggle with generating valid 16-character alphanumeric IDs for Foundry VTT JSON. The current requirement that IDs must match `^[a-zA-Z0-9]{16}$` (exactly 16 alphanumeric characters) is error-prone when generated manually by LLMs. Common issues include:
- Wrong length (15 or 17 characters instead of 16)
- Including dashes (UUID format)
- Using placeholder text like "monster-uuid"
- Generating duplicate IDs within the same monster

This causes validation failures and requires multiple correction cycles. A simple Python script to generate unique IDs would eliminate this pain point and improve reliability.

## What Changes

- Add a new Python script `scripts/generate_foundry_ids.py` that generates unique 16-character alphanumeric IDs
- Update SKILL.md to instruct LLMs to use the script instead of manually generating IDs
- The script will:
  - Generate one or more unique 16-character IDs (alphanumeric, case-insensitive)
  - Accept an optional count parameter (default: 1)
  - Output IDs one per line to stdout
  - Use cryptographically secure random generation to ensure uniqueness
  - Be simple and self-contained (no external dependencies beyond Python standard library)
- Update the self-validation checklist to reference the ID generator script
- Update the validation script to detect duplicate IDs (enhancement)

## Impact

- Affected specs: `foundry-export` (ID generation workflow)
- Affected code: `.claude/skills/draw-steel-monster-generator/SKILL.md`, `scripts/generate_foundry_ids.py` (new)
- Benefits: Eliminates ID generation errors, reduces validation cycles, improves reliability, simpler for LLMs to use
- Risks: Minimal - script is simple and self-contained