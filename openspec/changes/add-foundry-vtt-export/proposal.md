# Change: Add Foundry VTT Export Capability

## Why

Users want to import generated monsters directly into their Foundry VTT games using the Draw Steel system. Currently, the skill outputs Markdown stat blocks, but many GMs need Foundry VTT JSON format for immediate use in their games.

## What Changes

1. **Add Foundry VTT JSON export format** as an optional output mode
2. **Support all monster types**: Minion, Horde, Platoon, Elite, Leader, Solo
3. **Generate correct Foundry NPC structure** with:
   - Actor data (stamina, characteristics, combat stats)
   - Items (abilities, features, traits)
   - Proper Draw Steel system fields
4. **Support Foundry enrichers** in text fields for interactive elements
5. **Output to file or clipboard** for easy import

## Impact

- Affected specs: `foundry-export` (new capability)
- New capability: Generate Foundry VTT JSON from monster stat blocks
- No breaking changes to existing functionality
- Optional feature - users can still request Markdown output
- Enables seamless import to Foundry VTT Draw Steel games

## User Request

User provided:
- Foundry module path: `C:\Users\steve\code\draw-steel\src\packs\monsters\`
- Example monsters: Basilisk, Kobold Sagittarion
- Enrichers docs: `C:\Users\steve\code\draw-steel\src\docs\Enrichers.md`
