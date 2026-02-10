## Context

Foundry VTT requires all `_id` fields to match the regex `^[a-zA-Z0-9]{16}$` - exactly 16 alphanumeric characters. This is a strict requirement that causes frequent validation failures when LLMs generate IDs manually.

**Current Problem:**
- LLMs struggle with exact character counts (often generate 15 or 17 characters)
- LLMs often include dashes (UUID format: `a1b2c3d4-e5f6-7890-abcd`)
- LLMs sometimes use placeholder text like "monster-uuid"
- LLMs may generate duplicate IDs within the same monster
- This causes validation failures and requires multiple correction cycles

**Current Requirement (SKILL.md line 312-323):**
```markdown
All `_id` fields must match `^[a-zA-Z0-9]{16}$` (exactly 16 alphanumeric chars):

// CORRECT:
"_id": "aB2c3D4e5F6G7890"  // 16 chars, letters & numbers only

// INCORRECT:
"_id": "aB2c3D4e5F67890"    // 15 chars
"_id": "d4e5f6a7-b8c9-0123" // Has dashes (UUID format)

Each item needs unique ID. Generate fresh for each monster.
```

## Goals / Non-Goals

**Goals:**
- Eliminate ID generation errors caused by LLMs
- Reduce validation cycles and correction iterations
- Provide a simple, reliable way to generate valid IDs
- Keep the script self-contained (no external dependencies)
- Ensure IDs are "somewhat unique" (cryptographically secure random)
- Make it easy for LLMs to use via command-line invocation

**Non-Goals:**
- UUID-style uniqueness guarantees (not required for Foundry)
- Complex ID generation with semantic meaning
- ID collision detection across different monsters (only within same monster needed)
- Database-backed ID management
- Web service or API for ID generation

## Decisions

### Decision 1: Use Python Standard Library Only

**What:** Generate IDs using `secrets` module from Python standard library.

**Why:**
- No external dependencies required
- `secrets.choice()` provides cryptographically secure random selection
- Available in Python 3.6+ (well-supported)
- Simple and self-contained
- Fast and lightweight

**Alternatives considered:**
1. **UUID module** - Generates UUIDs with dashes, would require post-processing to remove dashes
2. **random module** - Not cryptographically secure, potential for collisions
3. **External library** - Adds dependency, unnecessary complexity
4. **Hash-based generation** - Would require input data, not needed for random IDs

### Decision 2: Simple Command-Line Interface

**What:** Script accepts optional count parameter and outputs IDs one per line.

```bash
# Generate 1 ID (default)
python scripts/generate_foundry_ids.py

# Generate 5 IDs
python scripts/generate_foundry_ids.py --count 5

# Generate 10 IDs
python scripts/generate_foundry_ids.py -c 10
```

**Why:**
- Simple for LLMs to invoke
- Output format is easy to parse (one per line)
- Optional count parameter provides flexibility
- Follows standard CLI conventions

**Alternatives considered:**
1. **Interactive mode** - More complex, harder for LLMs to use
2. **JSON output** - Unnecessary complexity for simple string generation
3. **File output** - Adds I/O complexity, stdout is sufficient

### Decision 3: Alphanumeric, Case-Insensitive

**What:** Generate IDs using characters: a-z, A-Z, 0-9 (62 possible characters per position).

**Why:**
- Matches Foundry VTT requirement: `^[a-zA-Z0-9]{16}$`
- Provides sufficient randomness (62^16 ≈ 4.8×10^28 possibilities)
- Easy to read and copy
- No special characters that might cause issues

**Alternatives considered:**
1. **Lowercase only** - Reduces randomness (36^16 vs 62^16)
2. **Hexadecimal only** - Further reduces randomness (16^16), less readable
3. **Include special characters** - Not required by Foundry, could cause issues

### Decision 4: No Duplicate Detection in Generator

**What:** Generator script does not check for duplicates within the same run.

**Why:**
- With 62^16 possibilities, collision probability is negligible
- Validation script will detect duplicates (added enhancement)
- Keeps generator script simple and fast
- Duplicates across different monsters are acceptable (Foundry handles this)

**Alternatives considered:**
1. **Track generated IDs in memory** - Adds complexity, unnecessary
2. **Check against existing JSON files** - Adds I/O complexity, not needed
3. **Use timestamp prefix** - Reduces randomness, not required

## Risks / Trade-offs

### Risk 1: LLMs May Not Use the Script

**Risk:** LLMs might continue to generate IDs manually, ignoring the script.

**Mitigation:**
- Update SKILL.md with clear instructions to use the script
- Remove manual ID generation examples from SKILL.md
- Add script usage in the self-validation checklist
- Emphasize that manual generation is error-prone

### Risk 2: Script Output Parsing Errors

**Risk:** LLMs might not correctly parse script output (one ID per line).

**Mitigation:**
- Simple output format (one ID per line)
- Clear examples in SKILL.md
- Test with actual LLM invocations
- Consider adding JSON output mode if parsing issues arise

### Risk 3: Cross-Platform Compatibility

**Risk:** Script might not work on all platforms (Windows, macOS, Linux).

**Mitigation:**
- Use Python standard library only (cross-platform)
- Test on multiple platforms
- Add shebang line for Unix: `#!/usr/bin/env python3`
- Document Python version requirement (3.6+)

### Trade-off: Uniqueness vs. Simplicity

**Trade-off:** Using cryptographically secure random generation instead of guaranteed uniqueness.

**Rationale:**
- 62^16 possibilities makes collisions extremely unlikely
- Foundry doesn't require global uniqueness, only uniqueness within a monster
- Validation script will detect duplicates (enhancement)
- Simplicity is more important than theoretical guarantees

## Migration Plan

### Step 1: Create ID Generator Script
1. Create `scripts/generate_foundry_ids.py`
2. Implement secure random ID generation using `secrets` module
3. Add command-line argument parsing for count parameter
4. Test script output format and ID validity

### Step 2: Update SKILL.md
1. Replace manual ID generation instructions with script usage
2. Add example: "Generate 5 IDs with: `python scripts/generate_foundry_ids.py --count 5`"
3. Update self-validation checklist to reference script
4. Remove manual ID examples that LLMs might copy

### Step 3: Enhance Validation Script
1. Add duplicate ID detection logic
2. Test with sample JSON containing duplicate IDs
3. Update error messages for duplicate IDs

### Step 4: Testing
1. Test ID generator with various counts
2. Verify generated IDs match regex `^[a-zA-Z0-9]{16}$`
3. Test integration: Generate IDs → Create JSON → Validate
4. Test duplicate detection with validation script

### Step 5: Documentation
1. Update CHANGELOG
2. Verify script is executable on Unix systems
3. Test with actual LLM generation workflow

### Rollback Plan
1. Keep original SKILL.md sections backed up
2. If script causes issues, revert to manual ID generation instructions
3. Remove script from repository

## Open Questions

- **Question 1:** Should we add a JSON output mode for easier parsing?
  - **Consideration:** One-per-line format is simple, but JSON might be more robust
  - **Recommendation:** Start with simple format, add JSON mode if parsing issues arise

- **Question 2:** Should we add a prefix option for semantic grouping?
  - **Consideration:** Could help with debugging but adds complexity
  - **Recommendation:** Defer until proven need arises

- **Question 3:** Should the script validate existing JSON files and replace invalid IDs?
  - **Consideration:** Could be useful for fixing existing files
  - **Recommendation:** Keep script simple (generation only), validation script handles validation