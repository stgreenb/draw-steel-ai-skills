# Design: Add Dynamic Terrain Objectives Support

## Context

The Draw Steel monster generator skill currently only supports generating monsters, but Draw Steel includes a rich system of Dynamic Terrain Objectives (DTOs) including Environmental Hazards, Fieldworks, Mechanisms, Siege Engines, Power Fixtures, and Supernatural Objects.

**Key Challenge:** Unlike monsters, DTOs have no published mathematical formulas. The EV, Stamina, and damage values are designed based on narrative and gameplay balance rather than formulaic calculations.

**Solution Approach:** Reverse-engineer patterns from 30+ published DTO examples in the Dynamic Terrain chapter to create guidance for LLMs to generate formula-compliant DTOs.

## Goals / Non-Goals

### Goals
- Enable generation of DTOs that match published patterns for EV, Stamina, and damage
- Support all six DTO categories (Environmental Hazards, Fieldworks, Mechanisms, Siege Engines, Power Fixtures, Supernatural Objects)
- Provide clear guidance for DTO stat block structure
- Include examples from published content for reference
- Create validation checklist for DTO output

### Non-Goals
- Create exact mathematical formulas (DTOs don't have official math)
- Support Foundry VTT export (DTOs are not currently supported in Foundry)
- Replace published DTO content (generated DTOs should be unique)
- Guarantee balance (DTOs rely on narrative judgment more than formulas)

## Decisions

### Decision 1: Pattern-Based Rather Than Formula-Based

**What:** Use pattern matching and ranges rather than exact formulas

**Why:** DTOs show significant variation within categories. For example:
- Level 2 hazards range from 2-4 EV
- Level 3 siege engines range from 8-12 EV
- Stamina varies widely based on size and material

**Alternatives Considered:**
1. **Exact formulas:** Rejected - DTOs don't have published formulas
2. **Random generation:** Rejected - Would produce inconsistent results
3. **Pattern-based ranges:** Chosen - Matches published examples while allowing flexibility

### Decision 2: Category-Specific Guidance

**What:** Provide separate guidance for each DTO category

**Why:** Each category has distinct characteristics:
- Environmental Hazards: Often per-square EV and Stamina
- Fieldworks: Frequently include Allied Awareness
- Siege Engines: Require adjacent creature actions
- Supernatural Objects: Very high EV (20+) and unique abilities

**Alternatives Considered:**
1. **Unified DTO guidance:** Rejected - Too much complexity in one system
2. **Role-based guidance (like monsters):** Rejected - DTOs don't map cleanly to monster roles
3. **Category-specific guidance:** Chosen - Clearer and more accurate

### Decision 3: Include Published Examples

**What:** Reference specific published DTOs in the skill guidance

**Why:** Examples provide concrete patterns for LLMs to follow:
- "Like Angry Beehive (Level 2 Hazard Hexer, EV 2, Stamina 3)"
- "Like Bear Trap (Level 1 Trap Ambusher, EV 2, Stamina 6)"
- "Like Catapult (Level 3 Siege Engine Artillery, EV 10, Stamina 50)"

**Alternatives Considered:**
1. **No examples:** Rejected - Too abstract for LLMs
2. **General descriptions:** Rejected - Less precise than examples
3. **Published examples:** Chosen - Most accurate reference

### Decision 4: No Foundry VTT Support

**What:** Do not include Foundry VTT JSON export for DTOs

**Why:** DTOs are not currently supported in Foundry's Draw Steel system. Adding validation for a non-existent system would be premature.

**Alternatives Considered:**
1. **Add Foundry support anyway:** Rejected - Would crash on import
2. **Wait for Foundry support:** Chosen - Defer until Foundry adds DTO support
3. **Create custom schema:** Rejected - Would conflict with future official support

## Risks / Trade-offs

### Risk 1: Pattern Inference May Be Inaccurate

**Risk:** Reverse-engineered patterns may not reflect designer intent

**Mitigation:**
- Use ranges rather than exact values
- Document that formulas are derived, not official
- Encourage manual review of generated DTOs
- Include disclaimer about lack of published math

### Risk 2: DTOs May Be Unbalanced

**Risk:** Generated DTOs could be too strong or too weak for their EV

**Mitigation:**
- Provide EV ranges rather than single values
- Include multiple published examples for each level
- Encourage user to adjust EV based on final design
- Note that DTOs rely on narrative judgment

### Trade-off: Flexibility vs. Consistency

**Trade-off:** Using ranges allows flexibility but reduces consistency

**Decision:** Prioritize flexibility - DTOs are inherently variable and narrative-driven

### Trade-off: Complexity vs. Usability

**Trade-off:** Category-specific guidance is more complex but more accurate

**Decision:** Prioritize accuracy - DTO categories are too different to merge

## Migration Plan

### Phase 1: Pattern Analysis
1. Read and analyze all published DTOs (30+ examples)
2. Extract EV, Stamina, damage values by level and category
3. Identify common structures (Deactivate, Activate, Effect, Upgrades)
4. Document exceptions and special cases

### Phase 2: Skill Creation
1. Create skill file with DTO generation guidance
2. Add category-specific sections
3. Include published examples
4. Add validation checklist

### Phase 3: Testing
1. Generate DTOs at various levels for each category
2. Compare generated values to published patterns
3. Adjust ranges and guidance as needed
4. Validate output format

### Phase 4: Documentation
1. Update skill documentation
2. Add usage examples
3. Document limitations
4. Add notes about lack of published formulas

### Rollback Plan
If generated DTOs don't match published patterns:
1. Re-analyze published examples with more granularity
2. Adjust EV ranges and damage values
3. Add more published examples for reference
4. Consider breaking into sub-categories if needed

## Open Questions

### Q1: Should DTOs Have Role-Like Classifications?

**Context:** Some DTOs have roles like "Defender", "Ambusher", "Hexer" similar to monsters

**Options:**
1. **Yes, use monster roles:** Maps to existing system but may be inaccurate
2. **No, use categories only:** Simpler but loses nuance
3. **Mixed approach:** Use categories for generation, roles for reference

**Decision:** Use categories only - DTO roles are more descriptive than functional

### Q2: How to Handle Per-Square vs. Fixed Stamina?

**Context:** Some DTOs have fixed Stamina, others have per-square Stamina

**Options:**
1. **Always use per-square:** More consistent but less accurate
2. **Always use fixed:** Simpler but doesn't fit all DTOs
3. **Context-dependent:** Use per-square for area-based DTOs, fixed for others

**Decision:** Context-dependent - match published patterns per category

### Q3: Should DTOs Have Keywords Like Monsters?

**Context:** Monsters have keywords (beast, undead, construct, etc.), DTOs don't

**Options:**
1. **Add keywords for consistency:** Helps with thematic generation
2. **No keywords:** DTOs don't have official keywords
3. **Optional keywords:** Include for flavor but not required

**Decision:** No keywords - DTOs don't have official keywords, adding them would be misleading

### Q4: How to Handle Upgrade EV Costs?

**Context:** Upgrades have EV costs that vary widely (+1 to +12 EV)

**Options:**
1. **Fixed upgrade costs:** Simpler but less accurate
2. **Published example costs:** More accurate but less flexible
3. **Guidance-based costs:** Provide ranges based on upgrade power

**Decision:** Published example costs - use actual upgrade costs from published DTOs as reference

### Q5: Should DTOs Have Damage Types?

**Context:** Many DTOs deal specific damage types (fire, poison, acid, etc.)

**Options:**
1. **Always include damage type:** More consistent
2. **Base on theme:** Match damage type to DTO theme
3. **Optional:** Include when relevant to DTO

**Decision:** Base on theme - match damage type to DTO theme (e.g., lava = fire, brambles with upgrade = poison)