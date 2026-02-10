# skill-format Specification

## Purpose
TBD - created by archiving change add-multi-platform-skill-compat. Update Purpose after archive.
## Requirements
### Requirement: SKILL.md Frontmatter Compliance

The skill's SKILL.md SHALL use YAML frontmatter compliant with the [Agent Skills specification](https://agentskills.io/specification).

#### Scenario: Required fields
- **WHEN** any platform parses the skill's SKILL.md
- **THEN** the frontmatter contains `name` field (1-64 chars, lowercase alphanumeric + hyphens)
- **AND** the frontmatter contains `description` field (1-1024 chars)

#### Scenario: name field format
- **WHEN** the name field is validated
- **THEN** it contains only lowercase letters (a-z), numbers (0-9), and hyphens (-)
- **AND** it does not start or end with a hyphen
- **AND** it does not contain consecutive hyphens (--)
- **AND** it matches the parent directory name

#### Scenario: description field content
- **WHEN** the description field is validated
- **THEN** it is 1-1024 characters
- **AND** it describes what the skill does and when to use it
- **AND** it includes specific keywords for task matching

### Requirement: Optional Frontmatter Fields

The skill SHALL include optional specification fields where applicable.

#### Scenario: license field
- **WHEN** the skill is distributed
- **THEN** the frontmatter contains a `license` field
- **AND** the value is a valid license identifier (e.g., "MIT")

#### Scenario: compatibility field
- **WHEN** the skill has environment requirements
- **THEN** the frontmatter contains a `compatibility` field (1-500 chars)
- **AND** it documents intended platforms or required dependencies

#### Scenario: metadata field
- **WHEN** additional metadata is needed
- **THEN** the frontmatter contains a `metadata` field
- **AND** it includes `author` and `version` keys
- **AND** values are strings

### Requirement: Specification-Compliant Directory Structure

The skill SHALL follow the agentskills.io directory structure.

#### Scenario: Required file
- **WHEN** the skill directory is examined
- **THEN** it contains a file named `SKILL.md` at the root

#### Scenario: references directory
- **WHEN** detailed documentation exists
- **THEN** it is stored in a `references/` subdirectory
- **AND** files are one level deep from SKILL.md

#### Scenario: scripts directory
- **WHEN** executable scripts exist
- **THEN** they are stored in a `scripts/` subdirectory
- **AND** they are self-contained or document dependencies

#### Scenario: assets directory
- **WHEN** static resources exist
- **THEN** they are stored in an `assets/` subdirectory
- **AND** they include templates, images, or data files

### Requirement: Progressive Disclosure

The skill SHALL be structured for efficient context management per the specification.

#### Scenario: SKILL.md size
- **WHEN** the skill is activated
- **THEN** SKILL.md body contains core workflow and instructions
- **AND** SKILL.md is under 500 lines

#### Scenario: Reference file loading
- **WHEN** SKILL.md references additional files
- **THEN** those files are in the references/ subdirectory
- **AND** they are loaded only when needed by the agent

#### Scenario: File references
- **WHEN** SKILL.md references other files
- **THEN** it uses relative paths from the skill root
- **AND** references are one level deep

### Requirement: Cross-Platform Discovery

The skill SHALL be discoverable by all platforms following the Agent Skills specification.

#### Scenario: Claude Code discovery
- **WHEN** Claude Code scans `.claude/skills/`
- **THEN** the skill appears in available skills
- **AND** the skill's name and description are visible

#### Scenario: Cursor discovery
- **WHEN** Cursor scans for Agent Skills
- **THEN** the skill is discoverable (via `.claude/skills/` or local directory)

#### Scenario: Gemini CLI discovery
- **WHEN** Gemini CLI scans for Agent Skills
- **THEN** the skill is discoverable (via `.claude/skills/` or local directory)

#### Scenario: Antigravity Google discovery
- **WHEN** Antigravity Google scans for Agent Skills
- **THEN** the skill is discoverable via the Agent Skills mechanism

### Requirement: Validation

The skill SHALL pass validation using the skills-ref tool.

#### Scenario: skills-ref validation
- **WHEN** `skills-ref validate ./skill-directory/` is run
- **THEN** the skill passes all validation checks
- **AND** frontmatter is valid YAML
- **AND** name field follows format rules
- **AND** description field meets length requirements

#### Scenario: Directory structure validation
- **WHEN** skills-ref validates the skill
- **THEN** SKILL.md exists at the root
- **AND** optional directories (scripts/, references/, assets/) are correctly structured

### Requirement: Consistent Skill Content

All platform directories SHALL contain consistent skill content.

#### Scenario: Skill name consistency
- **WHEN** the skill is discovered on any platform
- **THEN** the skill name is identical across all directories
- **AND** the name uses kebab-case (e.g., `draw-steel-monster-generator`)

#### Scenario: Skill description consistency
- **WHEN** the skill is discovered on any platform
- **THEN** the skill description is identical across all directories
- **AND** the description is under 1024 characters

