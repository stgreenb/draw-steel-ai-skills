## ADDED Requirements

### Requirement: Always Generate Foundry JSON for Validation

The skill MUST always generate Foundry JSON internally for validation purposes, even when the user only requests markdown format.

#### Scenario: User requests markdown format
- **WHEN** user requests monster in markdown format only
- **THEN** skill generates Foundry JSON internally
- **AND** skill runs validation on the JSON
- **AND** skill converts validated JSON to markdown
- **AND** skill returns markdown output to user

#### Scenario: User requests both formats
- **WHEN** user requests monster in both markdown and Foundry formats
- **THEN** skill generates Foundry JSON
- **AND** skill runs validation on the JSON
- **AND** skill converts validated JSON to markdown
- **AND** skill returns both markdown and JSON outputs to user

#### Scenario: User requests Foundry format only
- **WHEN** user requests monster in Foundry format only
- **THEN** skill generates Foundry JSON
- **AND** skill runs validation on the JSON
- **AND** skill returns JSON output to user

### Requirement: Validation Feedback for All Formats

The skill MUST provide validation feedback to users regardless of requested output format.

#### Scenario: Validation errors in markdown-only request
- **WHEN** validation finds errors in internally generated JSON
- **THEN** skill reports validation errors to user
- **AND** skill indicates errors are from internal validation
- **AND** skill still returns markdown output (with potential issues)

#### Scenario: Validation warnings in markdown-only request
- **WHEN** validation finds warnings in internally generated JSON
- **THEN** skill reports validation warnings to user
- **AND** skill indicates warnings are from internal validation
- **AND** skill returns markdown output

#### Scenario: Validation passes
- **WHEN** validation passes with no errors or warnings
- **THEN** skill indicates validation passed
- **AND** skill returns requested output format

### Requirement: Validation Failure Handling

The skill MUST handle validation failures appropriately without blocking markdown output.

#### Scenario: Validation has errors
- **WHEN** validation errors are found
- **THEN** skill reports errors to user
- **AND** skill still provides markdown output
- **AND** skill suggests user review errors or request Foundry format for more details

#### Scenario: Validation has critical errors
- **WHEN** critical validation errors are found (would crash Foundry)
- **THEN** skill highlights critical errors prominently
- **AND** skill still provides markdown output
- **AND** skill strongly suggests user reconsider or fix errors

## MODIFIED Requirements

None

## REMOVED Requirements

None

## RENAMED Requirements

None