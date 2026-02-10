## Context

The current validation tool (`validate_foundry_json.py`) only runs when Foundry JSON format is requested. When users request markdown format only, validation is skipped entirely. This means markdown-only generations miss critical error detection for:
- Invalid keywords (e.g., D&D terms like "piercing" damage type)
- Missing required fields (e.g., spend field in abilities)
- Wrong data types (e.g., resource as object instead of integer)
- Formula compliance issues
- Power effects structure problems

Analysis shows that markdown-only generations have lower quality because they bypass this validation step.

## Goals / Non-Goals

**Goals:**
- Ensure all monster generations benefit from validation regardless of requested format
- Improve quality of markdown-only monster generations
- Provide users with validation feedback even when they don't request Foundry format
- Keep implementation simple and maintainable

**Non-Goals:**
- Change the validation script itself
- Add new validation rules
- Change markdown format output
- Modify the user-facing API or command-line interface

## Decisions

### Decision 1: Always generate Foundry JSON internally
**What:** Generate Foundry JSON internally for validation, then convert to markdown if needed
**Why:** Simplest approach - reuses existing validation without modification
**Evidence:** Validation script already exists and works well for Foundry JSON
**Alternatives considered:**
- Create separate markdown validation - rejected because it duplicates validation logic
- Modify validation script to accept markdown - rejected because validation is format-specific
- Skip validation for markdown - rejected because this is the current problem

### Decision 2: Provide validation feedback regardless of format
**What:** Show validation errors/warnings to user even when they request markdown format
**Why:** Users benefit from knowing about issues in their monsters
**Evidence:** Users have found validation helpful for Foundry format
**Alternatives considered:**
- Hide validation for markdown requests - rejected because users lose quality feedback
- Only show critical errors for markdown - rejected because all errors are valuable

### Decision 3: Don't block markdown output on validation errors
**What:** Always provide markdown output even if validation finds errors
**Why:** Markdown format doesn't require perfect compliance like Foundry JSON
**Evidence:** Markdown is for readability, not automated import
**Alternatives considered:**
- Block markdown output on errors - rejected because markdown is more flexible
- Fix errors automatically - rejected because this could change user's intent

### Decision 4: Suggest Foundry format for detailed error review
**What:** When validation errors occur, suggest user request Foundry format for more details
**Why:** Foundry JSON validation provides more specific error messages and line numbers
**Evidence:** Validation script provides detailed JSON-specific error messages
**Alternatives considered:**
- Provide detailed errors in markdown - rejected because errors are JSON-specific
- Create markdown-specific error messages - rejected because it duplicates validation logic

## Risks / Trade-offs

**Risk:** Users may be confused by seeing JSON validation errors when they requested markdown
**Mitigation:** Clearly indicate errors are from internal validation and suggest Foundry format for more details

**Risk:** Performance impact from generating both formats internally
**Mitigation:** Minimal impact - generation is fast (<30 sec) and validation is quick

**Trade-off:** More complexity in generation workflow
**Benefit:** Consistent quality across all output formats

## Migration Plan

1. Update SKILL.md to always generate Foundry JSON internally
2. Update workflow to run validation before format conversion
3. Update output handling to show validation results regardless of format
4. No breaking changes for users

## Open Questions

**Q:** Should validation be optional for markdown requests?
**A:** No - validation improves quality and should always run

**Q:** Should we provide different validation messages for markdown vs Foundry format?
**A:** No - use same validation messages, just clarify they're from internal validation

**Q:** Should we fix validation errors automatically before markdown conversion?
**A:** No - this could change user's intent and create unexpected results