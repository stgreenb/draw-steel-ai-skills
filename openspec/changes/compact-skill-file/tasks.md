## 1. Analysis and Planning
- [ ] 1.1 Analyze current SKILL.md structure and identify sections to move
- [ ] 1.2 Identify ALL CRITICAL/MANDATORY/REQUIRED content that must stay in SKILL.md
- [ ] 1.3 Consolidate repeated validation workflow sections (3+ occurrences)
- [ ] 1.4 Plan task-driven reference file structure (FOUNDRY_JSON_SCHEMA.md, DETAILED_RULES.md, FORMULAS_AND_TABLES.md, ABILITY_EXAMPLES.md)
- [ ] 1.5 Map task-driven file references with explicit "WHEN" triggers

## 2. Create Reference Files
- [ ] 2.1 Create `references/FOUNDRY_JSON_SCHEMA.md` with complete JSON schema and examples
- [ ] 2.2 Create `references/DETAILED_RULES.md` with extended DO/DON'T tables and edge cases
- [ ] 2.3 Create `references/FORMULAS_AND_TABLES.md` with stat calculation formulas and lookup tables
- [ ] 2.4 Create `references/ABILITY_EXAMPLES.md` with ability type examples and patterns
- [ ] 2.5 Add task-driven descriptions to each reference file

## 3. Refactor SKILL.md (Conservative Approach)
- [ ] 3.1 Consolidate repeated validation workflow sections into ONE version
- [ ] 3.2 Keep ALL CRITICAL/MANDATORY/REQUIRED rules in SKILL.md
- [ ] 3.3 Remove moved sections from SKILL.md
- [ ] 3.4 Add task-driven file references with explicit "WHEN" triggers
- [ ] 3.5 Place references contextually after relevant sections
- [ ] 3.6 Ensure SKILL.md is ~550-600 lines (slightly oversized to preserve critical info)
- [ ] 3.7 Verify essential workflow remains intact
- [ ] 3.8 Check all file references are one level deep

## 4. Validation and Testing
- [ ] 4.1 Run `skills-ref validate` to ensure specification compliance
- [ ] 4.2 Verify SKILL.md line count is ~550-600 lines
- [ ] 4.3 Test that all references resolve correctly
- [ ] 4.4 Verify no CRITICAL/MANDATORY/REQUIRED information is lost
- [ ] 4.5 Check that progressive disclosure pattern is followed
- [ ] 4.6 Validate that reference file triggers appear in natural workflow contexts
- [ ] 4.7 Test that consolidation removed all duplication

## 5. Documentation
- [ ] 5.1 Document the new structure in CHANGELOG
- [ ] 5.2 Verify compatibility with all platforms (Claude Code, OpenCode, etc.)
- [ ] 5.3 Monitor for truncation issues after deployment