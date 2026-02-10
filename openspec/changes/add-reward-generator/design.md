# Design: Add Reward Generator Support

## Context

The Draw Steel monster generator skill currently supports generating monsters and DTOs. Draw Steel includes a comprehensive Rewards system with Treasures (consumables, trinkets, leveled treasures, artifacts) and Titles that heroes can earn through adventure, crafting, or accomplishment.

**Key Challenge:** Unlike DTOs which have no published math, Rewards have clear patterns for:
- Project goals (crafting difficulty)
- Item prerequisites (materials needed)
- Leveled treasure scaling (1st, 5th, 9th level)
- Title prerequisites and benefits

**Solution Approach:** Extract and document patterns from 100+ published treasure examples and 50+ published title examples to enable LLMs to generate formula-compliant rewards.

## Goals / Non-Goals

### Goals
- Enable generation of treasures that match published patterns for project goals, prerequisites, and effects
- Support all four treasure types (Consumables, Trinkets, Leveled Treasures, Artifacts)
- Support title generation with appropriate prerequisites and benefits
- Provide clear guidance for reward stat block structure
- Include Foundry VTT JSON export (rewards are supported in Foundry)
- Include examples from published content for reference

### Non-Goals
- Create exact mathematical formulas for effect balance (rewards are narrative-driven)
- Generate Wealth or Renown mechanics (these are character tracking, not generation)
- Replace published reward content (generated rewards should be unique)
- Generate downtime project rules (rewards use existing project system)

## Decisions

### Decision 1: Pattern-Based Project Goals

**What:** Use fixed project goal values based on treasure type and echelon

**Why:** Published examples show clear patterns:
- 1st Echelon Consumables: 45 (most), 30 (simpler)
- 2nd Echelon Consumables: 90
- 3rd Echelon Consumables: 180 (most), 120 (some)
- 4th Echelon Consumables: 360
- Trinkets (1st echelon): 150
- Leveled Treasures: 450 (all)

**Alternatives Considered:**
1. **Formula-based:** Rejected - No clear formula exists
2. **Random generation:** Rejected - Would produce inconsistent results
3. **Pattern-based values:** Chosen - Matches published examples

### Decision 2: Leveled Treasure Scaling Formulas

**What:** Use established scaling patterns for leveled treasures

**Why:** Published leveled treasures show consistent scaling:
- Stamina: +6 → +12 → +21
- Extra damage: +1 → +2 → +3
- Areas: Base → +1 → +2

**Alternatives Considered:**
1. **Linear scaling:** Rejected - Doesn't match published pattern (+6, +12, +21 is not linear)
2. **Random scaling:** Rejected - Would be inconsistent
3. **Published pattern:** Chosen - Matches official scaling

### Decision 3: Magic vs. Psionic Keywords

**What:** Every treasure must have either Magic or Psionic keyword

**Why:** Published treasures always include one or both keywords to indicate creation method. These keywords don't restrict use (Magic items can be used by anyone, Psionic items can be used by anyone).

**Alternatives Considered:**
1. **Optional keywords:** Rejected - All published treasures have these keywords
2. **Restrictive keywords:** Rejected - Keywords indicate creation, not usage
3. **Required keywords:** Chosen - Matches published pattern

### Decision 4: Title Benefit Structure

**What:** Titles have 3-4 benefit options (or single benefit for individual titles)

**Why:** Published titles offer choice to allow customization:
- Group titles: 3-4 options, each hero chooses one
- Individual titles: Single benefit
- Some titles grant abilities with Heroic Resource costs

**Alternatives Considered:**
1. **Single benefit only:** Rejected - Reduces customization
2. **All titles have 3-4 options:** Rejected - Individual titles should have single benefit
3. **Hybrid approach:** Chosen - Matches published pattern

### Decision 5: Foundry VTT Support

**What:** Include Foundry VTT JSON export for treasures and titles

**Why:** Rewards are supported in Foundry's Draw Steel system. Unlike DTOs which are not supported, rewards can be imported into Foundry.

**Alternatives Considered:**
1. **No Foundry support:** Rejected - Rewards are supported in Foundry
2. **Full Foundry validation:** Chosen - Include validation script for JSON output

## Risks / Trade-offs

### Risk 1: Effect Balance May Be Inaccurate

**Risk:** Generated treasure effects may be more or less powerful than published examples

**Mitigation:**
- Use published examples as templates
- Encourage manual review of generated rewards
- Note that rewards are narrative-driven and balance is subjective
- Provide multiple examples for reference

### Risk 2: Project Goal Patterns May Be Incomplete

**Risk:** Pattern analysis may miss edge cases or variations

**Mitigation:**
- Document that patterns are derived, not official
- Include ranges where appropriate
- Encourage Director to adjust project goals based on treasure complexity
- Note that Artifacts may have different patterns (not fully analyzed)

### Trade-off: Flexibility vs. Consistency

**Trade-off:** Using patterns allows consistency but limits creativity

**Decision:** Prioritize consistency - Rewards should match published patterns for crafting integration

### Trade-off: Complexity vs. Usability

**Trade-off:** Four treasure types + titles is complex but necessary

**Decision:** Prioritize accuracy - Each type has distinct characteristics that must be preserved

## Migration Plan

### Phase 1: Pattern Analysis
1. Analyze all Consumable treasures (30+ examples)
2. Analyze all Trinket treasures (20+ examples)
3. Analyze all Leveled treasures (50+ examples)
4. Analyze all Artifacts (if examples available)
5. Analyze all Titles (50+ examples)
6. Extract project goal patterns
7. Extract scaling patterns
8. Document keywords and their usage

### Phase 2: Skill Creation
1. Create skill file with reward generation guidance
2. Add treasure type sections
3. Add title generation guidance
4. Include published examples
5. Add validation checklist

### Phase 3: Foundry Support
1. Analyze Foundry reward JSON structure
2. Create JSON export format for treasures
3. Create JSON export format for titles
4. Add validation script
5. Test import into Foundry

### Phase 4: Testing
1. Generate consumables at all echelons
2. Generate trinkets
3. Generate leveled treasures (all types)
4. Generate titles at various echelons
5. Verify project goals match patterns
6. Verify scaling matches published patterns
7. Test Foundry import

### Phase 5: Documentation
1. Update skill documentation
2. Add usage examples
3. Document limitations
4. Add notes about crafting integration

### Rollback Plan
If generated rewards don't match published patterns:
1. Re-analyze published examples with more granularity
2. Adjust project goal values
3. Adjust scaling formulas
4. Add more published examples for reference

## Open Questions

### Q1: What Are Artifact Project Goals?

**Context:** Haven't analyzed enough artifact examples to determine project goal patterns

**Options:**
1. **Use higher values than leveled treasures:** Likely correct (artifacts are more powerful)
2. **Use same as leveled treasures:** Unlikely (artifacts are unique and powerful)
3. **Analyze more artifacts first:** Need more data

**Decision:** Note that artifacts need further analysis, initially use higher values (600+)

### Q2: How to Handle Yield Information?

**Context:** Some consumables yield multiple items (1d3, 1d6+1, etc.)

**Options:**
1. **Always include yield:** May be excessive for single-use items
2. **Include only when relevant:** More accurate
3. **Make yield optional:** Flexible but inconsistent

**Decision:** Include yield only when consumable creates multiple items, follow published pattern

### Q3: What About 2nd+ Echelon Trinkets?

**Context:** Haven't analyzed enough trinket examples beyond 1st echelon

**Options:**
1. **Scale project goals:** Likely correct (150 → 300 → 600)
2. **Use same as 1st echelon:** Unlikely (higher echelon = harder to craft)
3. **Analyze more trinkets first:** Need more data

**Decision:** Note that higher echelon trinkets need further analysis, initially scale project goals

### Q4: How to Balance Title Benefits?

**Context:** Title benefits should be balanced but there are no official guidelines

**Options:**
1. **Use published examples as reference:** Best approach
2. **Create balance formulas:** Too complex
3. **Director discretion:** Most flexible but least consistent

**Decision:** Use published examples as templates, note that balance is subjective

### Q5: Should Rewards Have Damage Type Keywords?

**Context:** Monsters have damage type keywords, treasures don't seem to

**Options:**
1. **Include damage type keywords:** Incorrect based on published examples
2. **Include only in effect description:** Correct based on published examples
3. **Both:** Redundant

**Decision:** Damage types go in effect description only (e.g., "deals extra 1 fire damage"), NOT as keywords