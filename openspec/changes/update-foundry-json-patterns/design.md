## Context

Generated monsters from LLMs using the draw-steel-monster-generator skill produce Foundry VTT JSON that differs from official Draw Steel monsters. This causes:
1. Foundry VTT crashes when trying to display abilities (e.g., "Cannot read properties of undefined")
2. Inconsistent patterns that don't match official Draw Steel examples
3. LLMs incorrectly copying example patterns (like "Brutal Effectiveness")

Analysis of 6 generated monsters vs 50+ official Draw Steel monsters revealed systematic differences in:
- Strike ability keywords (missing "weapon")
- Target types ("creature" vs "creatureObject")
- Breath/spew keywords (using damage types instead of area/magic)
- Ability type variety (only "main" type shown)
- Feature examples (Brutal Effectiveness copied incorrectly)

## Goals / Non-Goals

**Goals:**
- Make generated monsters match official Draw Steel patterns
- Prevent Foundry VTT crashes from invalid JSON structure
- Provide comprehensive examples for LLMs to follow
- Cover all common ability types in documentation

**Non-Goals:**
- Change the Draw Steel system rules
- Modify Foundry VTT system behavior
- Add new capability - only fixing documentation examples

## Decisions

### Decision 1: Always include "weapon" keyword in strikes
**What:** All strike abilities must include "weapon" keyword
**Why:** All 50+ official strike abilities examined include "weapon" keyword
**Evidence:** Basilisk Noxious Bite, Goblin Spear Charge, Griffon Claw Swipes all use `["melee", "strike", "weapon"]`
**Alternatives considered:**
- Make "weapon" optional - rejected because official pattern is consistent
- Only add for weapon-wielding creatures - rejected because even natural weapons (claws, bite) use "weapon"

### Decision 2: Use "creatureObject" for strike targets
**What:** Strike abilities targeting creatures should use "creatureObject" type
**Why:** More common in official examples (Basilisk Noxious Bite, Goblin Spear Charge, Omen Dragon Barbed Tail Swing)
**Evidence:** 80%+ of official strikes use "creatureObject", only 20% use "creature"
**Alternatives considered:**
- Keep "creature" for simplicity - rejected because "creatureObject" is the dominant pattern
- Use both patterns in examples - rejected because this confuses LLMs

### Decision 3: Breath/spew keywords use area/magic, not damage types
**What:** Breath weapons and spew abilities use `["area", "magic"]` keywords
**Why:** Official examples (Basilisk Petrifying Eye Beams, Omen Dragon Corroding Breath) use this pattern
**Evidence:** Damage types are specified in power.effects, not keywords
**Alternatives considered:**
- Use damage type keywords (e.g., "fire", "poison") - rejected because this is D&D pattern
- Use single keyword - rejected because official uses both "area" and "magic"

### Decision 4: Add "custom" field for area targets
**What:** Area abilities should include descriptive text in target.custom field
**Why:** Official examples include this for clarity (Omen Dragon abilities)
**Evidence:** Improves readability and matches official pattern
**Alternatives considered:**
- Skip custom field - rejected because it reduces clarity
- Make custom field required - rejected because some official examples omit it

### Decision 5: Show multiple ability types in examples (but NOT villain actions)
**What:** Documentation should include main, maneuver, freeTriggered, none types
**Why:** LLMs only generate "main" type currently, missing variety
**Evidence:** Official monsters use all these types (except villain which is specific)
**Villain action exception:** Villain actions are ONLY for Solo/Leader monsters, ALWAYS come in exactly 3 (opener, crowd control, ult), and have specific rules (once per encounter, one per round, used at end of turn)
**Existing guidance:** SKILL.md already has villain action guidance at lines 1808-1917, but it's missing the usage rules from Monster Basics.md
**Alternatives considered:**
- Include villain type - rejected because it's too specific and would mislead LLMs
- Show all ability types - rejected because villain is special case
- Add new villain action section - rejected because we're enhancing existing section

### Decision 6: Keep "Brutal Effectiveness" but add inspiration guidance
**What:** Keep "Brutal Effectiveness" in examples but add guidance that examples are for inspiration
**Why:** "Brutal Effectiveness" is a valid Basic Malice Feature from Monster Basics.md (lines 356-362)
**Evidence:** All monsters have access to Basic Malice features including Brutal Effectiveness
**Issue:** LLMs copy examples verbatim instead of creating unique features
**Solution:** Add clear guidance that examples should be used as inspiration, not copied
**Alternatives considered:**
- Remove "Brutal Effectiveness" - rejected because it's a valid feature
- Make examples abstract - rejected because concrete examples are better for learning

## Risks / Trade-offs

**Risk:** LLMs may still generate "creature" target type
**Mitigation:** Emphasize "creatureObject" in examples and validation

**Risk:** LLMs may overuse "charge" keyword
**Mitigation:** Add explicit note that "charge" is optional and only for actual charge attacks

**Risk:** LLMs may still copy examples verbatim instead of using them as inspiration
**Mitigation:** Add explicit guidance that examples should inspire unique creations, not be copied

**Risk:** Not showing villain action examples may limit Solo/Leader monster variety
**Mitigation:** Villain actions are very specific (exactly 3, once per encounter, one per round, opener/crowd control/ult) and should be in separate guidance, not general examples

**Trade-off:** More comprehensive examples increase documentation size
**Benefit:** Better LLM compliance and fewer generation errors

## Migration Plan

1. Update SKILL.md with new examples
2. Update keywords.json if needed
3. No code changes required (documentation only)
4. No breaking changes for users

## Open Questions

**Q:** Should "creature" target type be marked as invalid in validation?
**A:** No, it's still valid (used in 20% of official examples), just less common

**Q:** Should we add validation for "custom" field in area targets?
**A:** No, it's optional for clarity, not required

**Q:** Should we add examples for all 9 monster roles?
**A:** No, that's out of scope - this change focuses on JSON structure patterns

**Q:** How to enhance villain action guidance without bloating instructions?
**A:** Add concise bullet points for the 3 usage rules (once per encounter, one per round, end of turn) to existing section at lines 1808-1917