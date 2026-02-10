# Change: Remove Webapp Version

## Why
The webapp version has been problematic with high failure rates and clunky behavior. We will focus solely on the skill version which provides better reliability and user experience.

## What Changes
- **BREAKING:** Remove entire webapp directory and webapp.backup directory
- **BREAKING:** Remove webapp-related log files from root
- Remove webapp references from README.md
- Archive webapp-related changes from openspec/changes
- Update project.md to reflect skill-only focus

## Impact
- Affected specs: monster-generation (REMOVED webapp-specific requirements)
- Affected code: webapp/, webapp.backup/, webapp*.log files, README.md