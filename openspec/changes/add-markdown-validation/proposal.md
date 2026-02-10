# Change: Add validation for markdown-only monster generation

## Why

Users requesting monsters in markdown format get lower quality output compared to Foundry format requests because the validation tool only runs on Foundry JSON. Markdown output bypasses validation entirely, missing critical errors like invalid keywords, wrong damage types, missing fields, and formula compliance issues.

## What Changes

- Always generate Foundry JSON internally (even when user only requests markdown)
- Run validation on the generated Foundry JSON
- Convert validated JSON to markdown if markdown format was requested
- Return validation errors/warnings along with markdown output
- Ensure all monster generations benefit from validation regardless of requested format

## Impact

- Affected specs: generation-workflow (new spec)
- Affected code: `.claude/skills/draw-steel-monster-generator/SKILL.md`
- Breaking changes: None (improves quality without changing API)
- User impact: All users get higher quality monsters, even when requesting markdown format