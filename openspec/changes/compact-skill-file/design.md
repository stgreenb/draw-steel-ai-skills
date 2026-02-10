## Context

The Draw Steel Monster Generator skill's SKILL.md file has grown to 2,487 lines (91,280 bytes), far exceeding the Agent Skills specification's recommendations:
- Recommended: under 500 lines for SKILL.md
- Recommended: under 5000 tokens for the body content
- Current: 2,487 lines (5x the recommendation)

This causes truncation when loaded by LLMs, preventing users from accessing critical instructions. The specification explicitly recommends progressive disclosure: keep SKILL.md under 500 lines and move detailed reference material to separate files in the `references/` directory.

## Goals / Non-Goals

**Goals:**
- Reduce SKILL.md from 2,487 lines to ~550-600 lines (slightly oversized to preserve critical info)
- Follow Agent Skills specification's progressive disclosure pattern with conservative approach
- Prevent truncation when skill is loaded by LLMs
- Keep ALL CRITICAL, MANDATORY, and REQUIRED rules visible in SKILL.md
- Consolidate duplicated content (validation workflow appears 3+ times)
- Maximize reference file loading with explicit task-based triggers
- Ensure file references are one level deep from SKILL.md

**Non-Goals:**
- Changing the skill's functionality or workflow
- Modifying the validation scripts or other code
- Changing the directory structure (only adding to `references/`)
- Reducing the quality or depth of instructions
- Moving critical rules to reference files

## Decisions

### Decision 1: Conservative SKILL.md Size Target

**What:** Target ~550-600 lines for SKILL.md (slightly above 500-line recommendation to preserve critical info).

**Why:**
- All CRITICAL, MANDATORY, and REQUIRED rules must remain visible
- Current file is 2,487 lines (5x the recommendation)
- ~550-600 lines is still ~75% reduction and prevents truncation
- Better to be slightly oversized than to hide critical information
- Follows specification's intent (prevent truncation) while being conservative

**Alternatives considered:**
1. **Strict under-500-lines limit** - Would force moving critical rules to references, causing import failures
2. **Keep current size** - Already causing truncation issues
3. **Aggressive reduction to ~300 lines** - Too risky, critical rules might be missed

### Decision 2: Reference File Structure

**What:** Create four task-driven reference files in `references/` directory with explicit triggers:
- `FOUNDRY_JSON_SCHEMA.md` - Complete JSON schema and examples (load when generating Foundry format)
- `DETAILED_RULES.md` - Extended DO/DON'T tables and edge cases (load when debugging)
- `FORMULAS_AND_TABLES.md` - Stat calculation formulas and lookup tables (load when calculating stats)
- `ABILITY_EXAMPLES.md` - Ability type examples and patterns (load when designing abilities)

**Why:**
- Follows specification's recommendation to use `references/` subdirectory
- Each file is task-specific with clear loading triggers
- Task-driven references increase likelihood of being loaded when needed
- Reduces SKILL.md size significantly while keeping critical info visible
- Maintains all information accessibility

**Alternatives considered:**
1. **Single reference file** - Would be too large and defeat the purpose of progressive disclosure
2. **Generic reference files** - Less likely to be loaded at the right time
3. **Keep everything in SKILL.md** - Not viable due to truncation issue

### Decision 3: Content Allocation (Conservative)

**What:** Keep in SKILL.md (prioritized):
1. Quick Start instructions
2. Core validation workflow (SINGLE consolidated version, not repeated)
3. CRITICAL format rules checklist (all items marked "CRITICAL", "MANDATORY", "REQUIRED")
4. Generation workflow steps
5. Common pitfalls section
6. Task-specific file references with explicit "WHEN" triggers

Move to reference files:
- Complete JSON schema and examples → `FOUNDRY_JSON_SCHEMA.md`
- Extended DO/DON'T tables and edge cases → `DETAILED_RULES.md`
- Stat calculation formulas and lookup tables → `FORMULAS_AND_TABLES.md`
- Ability examples and patterns → `ABILITY_EXAMPLES.md`

**Consolidation:**
- Merge 3+ repeated validation workflow sections into one
- Remove duplicate examples
- Consolidate repeated rule explanations

**Why:**
- Critical rules always visible in SKILL.md (prevents import failures)
- Task-driven references increase loading likelihood
- Consolidation reduces duplication significantly
- Progressive disclosure reduces initial context load
- Prevents truncation

**Alternatives considered:**
1. **Keep all repeated content** - Would cause truncation
2. **Move critical rules to references** - Too risky, causes import failures
3. **Keep everything in SKILL.md** - Already causing truncation issues

### Decision 4: Task-Driven File References

**What:** Use relative paths with explicit "WHEN" triggers to maximize reference file loading:

```markdown
**WHEN generating Foundry format:** See [Foundry VTT JSON Schema](references/FOUNDRY_JSON_SCHEMA.md) for complete schema details and examples.

**WHEN debugging validation errors:** See [Detailed Rules](references/DETAILED_RULES.md) for extended DO/DON'T tables and edge cases.

**WHEN calculating stats:** See [Formulas and Tables](references/FORMULAS_AND_TABLES.md) for stat calculation formulas and lookup tables.

**WHEN designing abilities:** See [Ability Examples](references/ABILITY_EXAMPLES.md) for ability type examples and patterns.
```

**Strategic placement:**
- Place references immediately after relevant sections in SKILL.md
- Use "WHEN you need to X, see Y" pattern
- Add "See X for more details" at the end of concise summaries
- Include reference triggers in workflow steps

**Why:**
- Explicit triggers increase likelihood of reference file loading
- Contextual placement makes references more discoverable
- Task-driven approach matches agent's workflow
- Follows specification's recommendation for file references
- One level deep from SKILL.md (per specification)

**Alternatives considered:**
1. **Generic "see X for details"** - Less likely to be loaded at the right time
2. **Absolute paths** - Would break if skill directory is moved
3. **Nested references** - Not allowed per specification
4. **Section at end with all references** - Less discoverable

## Risks / Trade-offs

### Risk 1: Reference Files Not Loaded at Critical Times

**Risk:** Reference files might not be loaded when needed, leading to incorrect output.

**Mitigation:**
- Use explicit "WHEN" triggers in file references
- Place references contextually after relevant sections
- Add reference triggers in workflow steps
- Use task-driven file names (FOUNDRY_JSON_SCHEMA.md, not REFERENCE1.md)
- Include "See X for more details" at the end of concise summaries
- Test that references appear in natural workflow contexts

### Risk 2: Platform Compatibility

**Risk:** Some platforms might not support loading reference files on-demand.

**Mitigation:**
- Agent Skills specification explicitly supports this pattern
- All major platforms (Claude Code, OpenCode, etc.) follow the specification
- File references are standard Markdown links

### Risk 3: Maintenance Overhead

**Risk:** Maintaining multiple files could be more complex than a single file.

**Mitigation:**
- Each file is focused on a single concern
- Clear separation of concerns makes maintenance easier
- File structure is documented in the proposal

### Trade-off: SKILL.md Size vs Critical Info Visibility

**Trade-off:** Targeting ~550-600 lines instead of strict under-500-lines limit to preserve critical rules.

**Rationale:**
- Critical rules (marked CRITICAL/MANDATORY/REQUIRED) must always be visible
- Current file is 2,487 lines (5x recommendation)
- ~550-600 lines is still ~75% reduction and prevents truncation
- Better to be slightly oversized than to cause import failures
- Follows specification's intent (prevent truncation) while being conservative

### Trade-off: Reference File Loading Probability

**Trade-off:** Task-driven references require careful placement to be effective.

**Rationale:**
- Explicit "WHEN" triggers increase loading likelihood
- Contextual placement makes references more discoverable
- Task-driven approach matches agent's natural workflow
- Testing will validate reference effectiveness

## Migration Plan

### Step 1: Create Reference Files
1. Analyze current SKILL.md and identify sections to move
2. Create `references/FOUNDRY_JSON_SCHEMA.md` with JSON schema content (lines 266-541, 748-1374)
3. Create `references/DETAILED_RULES.md` with extended DO/DON'T tables (lines 572-644, 2236-2487)
4. Create `references/FORMULAS_AND_TABLES.md` with formulas (lines 1382-1411+)
5. Create `references/ABILITY_EXAMPLES.md` with ability examples (lines 1264-1374)

### Step 2: Refactor SKILL.md
1. Remove moved sections from SKILL.md
2. Consolidate repeated validation workflow sections (3+ occurrences → 1)
3. Keep ALL CRITICAL/MANDATORY/REQUIRED rules in SKILL.md
4. Add task-driven file references with explicit "WHEN" triggers
5. Ensure SKILL.md is ~550-600 lines (slightly oversized to preserve critical info)
6. Verify essential workflow remains intact
7. Check all file references are one level deep
8. Test reference file placement in natural workflow contexts

### Step 3: Validation
1. Run `skills-ref validate` to ensure specification compliance
2. Verify SKILL.md line count is ~550-600 lines
3. Test that all references resolve correctly
4. Verify no CRITICAL/MANDATORY/REQUIRED information is lost
5. Check progressive disclosure pattern is followed
6. Validate that reference file triggers appear in natural workflow contexts
7. Test that consolidation removed all duplication

### Step 4: Documentation
1. Update CHANGELOG with the restructuring
2. Verify compatibility with all platforms
3. Document the new structure if needed

### Rollback Plan
1. Keep original SKILL.md backed up
2. If issues arise, restore original file
3. Remove newly created reference files

## Open Questions

- **Question 1:** What is the optimal SKILL.md size to prevent truncation while keeping critical info?
  - **Consideration:** 500-line recommendation vs. critical rule visibility
  - **Recommendation:** Target ~550-600 lines, monitor for truncation issues

- **Question 2:** Should we add a "When to use reference files" section at the end of SKILL.md?
  - **Consideration:** Could improve discoverability but adds redundancy
  - **Recommendation:** Use contextual "WHEN" triggers instead

- **Question 3:** Should we add inline examples in SKILL.md that point to detailed versions in reference files?
  - **Consideration:** Could improve discoverability but increases SKILL.md size
  - **Recommendation:** Include brief examples with "see X for more details" links

- **Question 4:** How should we validate that reference files are being loaded at the right times?
  - **Consideration:** Need to test with actual LLM interactions
  - **Recommendation:** Monitor user feedback and adjust reference triggers based on patterns