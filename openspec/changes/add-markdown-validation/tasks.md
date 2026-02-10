## 1. Update SKILL.md Workflow

- [x] 1.1 Update generation workflow to always generate Foundry JSON internally
- [x] 1.2 Add instruction to run validation on internally generated JSON
- [x] 1.3 Add instruction to convert JSON to markdown if markdown format requested
- [x] 1.4 Add instruction to show validation results regardless of output format
- [x] 1.5 Add instruction to suggest Foundry format for detailed error review

## 2. Update Format Handling

- [x] 2.1 Update `--format markdown` workflow to generate JSON internally first
- [x] 2.2 Update `--format both` workflow to validate before converting to markdown
- [x] 2.3 Update `--format foundry` workflow to remain unchanged
- [x] 2.4 Add validation result display logic for all format requests

## 3. Update Validation Feedback

- [x] 3.1 Add validation error display for markdown-only requests
- [x] 3.2 Add validation warning display for markdown-only requests
- [x] 3.3 Add validation success message for all format requests
- [x] 3.4 Add suggestion to use Foundry format for detailed error review

## 4. Testing

- [x] 4.1 Test markdown-only request with valid monster
- [x] 4.2 Test markdown-only request with invalid monster (errors)
- [x] 4.3 Test markdown-only request with warnings
- [x] 4.4 Test both formats request
- [x] 4.5 Test Foundry-only request (should be unchanged)
- [x] 4.6 Verify validation errors are displayed for markdown requests
- [x] 4.7 Verify markdown output is still provided even with validation errors
- [x] 4.8 Verify suggestion to use Foundry format appears when errors exist

## Dependencies

- Tasks 1.1-1.5 must complete before tasks 2.1-2.4
- Tasks 2.1-2.4 must complete before tasks 3.1-3.4
- Tasks 3.1-3.4 must complete before tasks 4.1-4.8

## Parallelizable Work

- Tasks 4.1-4.8 can be done in parallel (independent test scenarios)