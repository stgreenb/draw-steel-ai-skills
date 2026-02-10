## ADDED Requirements

### Requirement: Conservative Progressive Disclosure Structure

The skill SHALL follow the Agent Skills specification's progressive disclosure pattern with a conservative approach that prioritizes critical information visibility over strict size limits.

#### Scenario: SKILL.md size compliance with critical info preservation
- **WHEN** the skill is activated
- **THEN** SKILL.md body contains core workflow and instructions
- **AND** SKILL.md is ~550-600 lines (slightly above 500-line recommendation to preserve critical info)
- **AND** SKILL.md body is under 5000 tokens to prevent truncation
- **AND** all CRITICAL/MANDATORY/REQUIRED rules remain visible in SKILL.md

#### Scenario: Task-driven reference file organization
- **WHEN** SKILL.md references additional files
- **THEN** those files are in the `references/` subdirectory
- **AND** they are loaded only when needed by the agent
- **AND** file references are one level deep from SKILL.md
- **AND** reference files have task-driven names and explicit "WHEN" triggers

#### Scenario: Essential content in SKILL.md
- **WHEN** SKILL.md is loaded
- **THEN** it contains Quick Start instructions
- **AND** it contains consolidated core validation workflow (not repeated)
- **AND** it contains all CRITICAL/MANDATORY/REQUIRED rules
- **AND** it contains core generation workflow steps
- **AND** it contains common pitfalls section
- **AND** it references supplementary files with explicit task triggers

#### Scenario: Reference file content and triggers
- **WHEN** reference files are loaded
- **THEN** `FOUNDRY_JSON_SCHEMA.md` contains complete JSON schema and examples (trigger: "WHEN generating Foundry format")
- **AND** `DETAILED_RULES.md` contains extended DO/DON'T tables and edge cases (trigger: "WHEN debugging validation errors")
- **AND** `FORMULAS_AND_TABLES.md` contains stat calculation formulas and lookup tables (trigger: "WHEN calculating stats")
- **AND** `ABILITY_EXAMPLES.md` contains ability type examples and patterns (trigger: "WHEN designing abilities")

#### Scenario: Content consolidation
- **WHEN** SKILL.md is refactored
- **THEN** repeated sections are consolidated (e.g., validation workflow appears once, not 3+ times)
- **AND** duplicate examples are removed
- **AND** consolidated content maintains all critical information

## MODIFIED Requirements

### Requirement: Progressive Disclosure

The skill SHALL be structured for efficient context management per the specification with a conservative approach that prioritizes critical information visibility.

#### Scenario: SKILL.md size with critical info preservation
- **WHEN** the skill is activated
- **THEN** SKILL.md body contains core workflow and instructions
- **AND** SKILL.md is ~550-600 lines (slightly above 500-line recommendation)
- **AND** SKILL.md body is under 5000 tokens to prevent truncation
- **AND** all CRITICAL/MANDATORY/REQUIRED rules remain visible in SKILL.md
- **AND** detailed reference material is moved to `references/` directory

#### Scenario: Task-driven reference file loading
- **WHEN** SKILL.md references additional files
- **THEN** those files are in the `references/` subdirectory
- **AND** they are loaded only when needed by the agent
- **AND** file references use relative paths from the skill root
- **AND** references are one level deep from SKILL.md
- **AND** references use explicit "WHEN" triggers to increase loading likelihood

#### Scenario: File references with task triggers
- **WHEN** SKILL.md references other files
- **THEN** it uses relative paths from the skill root
- **AND** references are one level deep
- **AND** reference files are task-specific with clear loading triggers
- **AND** references are placed contextually after relevant sections