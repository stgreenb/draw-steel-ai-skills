## ADDED Requirements

### Requirement: Reward Mechanics and Conversion

The system SHALL generate rewards using Draw Steel's unique mechanics for tiered outcomes, potency checks, and action types, NOT the mechanics used in other game systems.

#### Scenario: Use Tiered Outcomes for Reward Effects

**WHEN** a reward's effect has variable outcomes

**THEN** the reward SHALL use Draw Steel's 3-tiered power roll system:
- **Tier 1 (≤11):** Weakest effect
- **Tier 2 (12-16):** Average effect
- **Tier 3 (17+):** Strongest effect

**Example power roll structure:**
```
Power Roll + 2:
- ≤11: 3 damage; push 1
- 12-16: 6 damage; push 2; M < 1 slowed (save ends)
- 17+: 9 damage; push 3; M < 2 restrained (save ends)
```

#### Scenario: Ignore D&D-Style Mechanics When Converting

**WHEN** converting rewards from other game systems (D&D, Pathfinder, etc.)

**THEN** the system SHALL NOT use:
- **DC values** (e.g., "DC 15 Constitution save")
- **Flat bonuses** (e.g., "+2 to AC", "+5 to attack rolls")
- **Proficiency bonuses**
- **Saving throws** (except for "save ends" conditions)
- **Flat damage dice** (e.g., "deals 2d6 fire damage")
- **Duration in rounds** (use "save ends" or encounter duration instead)

**INSTEAD use:**
- **Tiered outcomes** (≤11, 12-16, 17+)
- **Potency checks** (M/A/R/I/P < value)
- **Damage bonuses** (e.g., "+1 damage" not "+2d6 damage")
- **Action types** (main action, maneuver, triggered action)
- **Encounter or save ends duration**

#### Scenario: Convert D&D Potion Effects to Draw Steel

**WHEN** converting a D&D-style potion (e.g., "Potion of Healing" that restores 2d4+2 HP)

**THEN** the reward SHALL:
- **Remove:** The 2d4+2 HP formula
- **Add:** Draw Steel recovery-based effect: "regain Stamina equal to your recovery value without spending a Recovery"
- **Keep:** The thematic concept (healing potion)

**Example conversion:**
- **D&D:** "Potion of Greater Healing: restores 4d4+4 HP"
- **Draw Steel:** "Greater Healing Potion: regain Stamina equal to 2x your recovery value without spending a Recovery"

#### Scenario: Convert D&D Magic Item Bonuses to Draw Steel

**WHEN** converting a D&D-style magic item with flat bonuses (e.g., "+1 longsword")

**THEN** the reward SHALL:
- **Remove:** The +1 attack bonus (Draw Steel doesn't have attack bonuses)
- **Add:** Extra damage: "deals an extra 1 damage"
- **Keep:** The thematic concept

**Example conversion:**
- **D&D:** "+1 Longsword: +1 to attack and damage rolls"
- **Draw Steel:** "Enchanted Longsword (leveled treasure): deals an extra 1 damage"

#### Scenario: Convert D&D Spell Effects to Draw Steel

**WHEN** converting a D&D-style spell or magical effect (e.g., "Fireball: 8d6 fire damage, DC 15 Dexterity save for half")

**THEN** the reward SHALL:
- **Remove:** The 8d6 damage and DC 15 save
- **Add:** Tiered power roll with damage and potency checks
- **Keep:** The thematic concept

**Example conversion:**
- **D&D:** "Scroll of Fireball: 8d6 fire damage, DC 15 Dexterity save for half"
- **Draw Steel:** "Scroll of Inferno Burst: Power Roll +2 - ≤11: 10 fire damage; 12-16: 15 fire damage; 17+: 20 fire damage; M < 2 burning (save ends)"

#### Scenario: Use Potency Checks for Condition Application

**WHEN** a reward applies conditions (slowed, prone, grabbed, etc.)

**THEN** the reward SHALL use potency checks, NOT saves:
- **CORRECT:** "M < 1 slowed (save ends)" or "A < 2 prone"
- **INCORRECT:** "Target makes a Dexterity save or become slowed"
- **INCORRECT:** "DC 15 Constitution save or take poison damage"

**Potency check format:** `[Characteristic] < [Value] [condition]`
- M = Might, A = Agility, R = Reason, I = Intuition, P = Presence
- Value = potency threshold (typically -1, 0, 1, 2, 3)
- Condition = the condition applied (may include "(save ends)")

#### Scenario: Use Draw Steel Action Types

**WHEN** describing how a reward is activated

**THEN** the reward SHALL use Draw Steel action types:
- **Maneuver:** Quick action that doesn't consume main action (e.g., "As a maneuver, you drink this potion")
- **Main action:** Consumes main action (rare for consumables/trinkets)
- **Triggered action:** Reacts to something (e.g., "When targeted by a ranged strike, you can use a triggered action")
- **Free triggered action:** Immediate reaction that doesn't consume action
- **No action required:** Passive or automatic effects

**Do NOT use:**
- "Bonus action" (D&D 5e term)
- "Swift action" (Pathfinder term)
- "Immediate action" (3.5e term)

#### Scenario: Convert Duration to Draw Steel Format

**WHEN** a reward has a duration

**THEN** the reward SHALL use Draw Steel duration formats:
- **"save ends":** Condition ends when target rolls 6+ on d10 at start of turn
- **"until end of encounter":** Effect lasts for entire combat
- **"until end of your next turn":** Effect lasts until your next turn starts
- **Specific duration:** "for 1 hour", "for 10 minutes", etc.

**Do NOT use:**
- "Concentration: up to 1 minute" (Draw Steel doesn't have concentration)
- "Lasts for 3 rounds" (Draw Steel doesn't track rounds this way)

#### Scenario: Convert D&D Magic Item Properties to Draw Steel Keywords

**WHEN** converting a D&D-style magic item with properties

**THEN** map D&D concepts to Draw Steel:
- **D&D:** "Requires attunement" → **Draw Steel:** Leveled treasure (automatically attunes at appropriate levels)
- **D&D:** "Wondrous item" → **Draw Steel:** Trinket with appropriate body keyword
- **D&D:** "Weapon" → **Draw Steel:** Light Weapon, Medium Weapon, Heavy Weapon, Bow, Polearm, etc.
- **D&D:** "Armor" → **Draw Steel:** Light Armor, Medium Armor, Heavy Armor, Shield
- **D&D:** "Rod/Staff/Wand" → **Draw Steel:** Implement, Orb, Wand, etc.

#### Scenario: Convert D&D Feat-Like Abilities to Draw Steel

**WHEN** a reward grants abilities similar to D&D feats

**THEN** the reward SHALL:
- Use Draw Steel ability terminology
- Follow Draw Steel action economy
- Use tiered outcomes if the ability has variable effects
- Not reference D&D mechanics (proficiency, advantage, etc.)

**Example conversion:**
- **D&D:** "Boots of Striding and Springing: Your speed increases by 10 feet, and you can jump 3 times as far"
- **Draw Steel:** "Boots of the Fleet (trinket, Feet): You gain a +2 bonus to speed. Additionally, when you use the Jump maneuver, you can jump twice as far."

#### Scenario: Convert D&D Conditional Bonuses to Draw Steel

**WHEN** a D&D item has conditional bonuses (e.g., "+2 to hit against dragons")

**THEN** the reward SHALL:
- Remove flat bonuses to attack rolls (Draw Steel doesn't have attack roll bonuses)
- Convert to damage bonuses where appropriate: "+2 damage against dragons"
- Or convert to edges/banes: "gain an edge on power rolls against dragons"
- Or convert to triggered abilities with tiered outcomes

**Example conversion:**
- **D&D:** "Dragon Slayer Longsword: +2 to hit and damage against dragons"
- **Draw Steel:** "Dragon Slayer Longsword (leveled treasure): deals an extra 2 damage against creatures with the Dragon keyword. Additionally, when you use a weapon ability with this weapon against a dragon, gain an edge on the power roll."

#### Scenario: Convert D&D Saving Throw Effects to Potency Checks

**WHEN** a D&D item imposes effects on failed saves

**THEN** the reward SHALL use potency checks with tiered outcomes:

**Determine effect difficulty:**
- **Easy to apply:** Condition applies on tier 1 (≤11), lower potency (harder to resist)
- **Medium difficulty:** Condition applies on tier 2 (12-16), medium potency
- **Hard to apply:** Condition applies on tier 3 (17+ only), higher potency (easier to resist)

**Example conversions:**
- **D&D:** "DC 13 Constitution save or be poisoned" (easy)
- **Draw Steel:** "Power Roll +2: ≤11: M < 0 poisoned (save ends); 12-16: M < 1 poisoned (save ends); 17+: M < 2 poisoned (save ends)"
  - Applies even on tier 1, but low potency means only weak Might creatures are affected

- **D&D:** "DC 15 Dexterity save or be restrained" (medium)
- **Draw Steel:** "Power Roll +2: ≤11: 3 damage; 12-16: 6 damage, A < 1 restrained (save ends); 17+: 9 damage, A < 2 restrained (save ends)"
  - Applies on tier 2+, medium potency means average Agility creatures are affected

- **D&D:** "DC 18 Wisdom save or be frightened" (hard)
- **Draw Steel:** "Power Roll +2: ≤11: 3 damage; 12-16: 6 damage; 17+: 9 damage, P < 3 frightened (save ends)"
  - Applies only on tier 3, high potency means only very low Presence creatures are affected

**Key principle:** The harder the effect is to apply (higher DC), the later it should appear in tiered outcomes (tier 2 or 3). Potency then scales with the tier.

#### Scenario: Convert D&D Damage Types to Draw Steel

**WHEN** converting damage types from other systems

**THEN** use Draw Steel damage types:
- **Valid types:** acid, cold, corruption, fire, holy, lightning, poison, psychic, sonic
- **Invalid types:** force, necrotic, radiant, thunder, untyped

**Conversion examples:**
- **D&D:** "necrotic damage" → **Draw Steel:** "corruption damage"
- **D&D:** "radiant damage" → **Draw Steel:** "holy damage"
- **D&D:** "thunder damage" → **Draw Steel:** "sonic damage"
- **D&D:** "force damage" → **Draw Steel:** "psychic damage" (closest equivalent)

#### Scenario: Convert D&D Spell Slots to Heroic Resource

**WHEN** a D&D item uses spell slots or charges

**THEN** the reward SHALL use Heroic Resource (or be consumable):
- **D&D:** "Wand of Fireballs: 7 charges, regains 1d6+1 charges daily"
- **Draw Steel:** Make it a consumable (single use) or require Heroic Resource cost for abilities

**Example conversion:**
- **D&D:** "Wand of Magic Missiles: 7 charges, 1st-level spell"
- **Draw Steel:** "Wand of Force Bolts (consumable): As a maneuver, make a ranged free strike. The strike deals extra 2 psychic damage and adds tiered outcomes to the power roll."

### Requirement: Reward Generation

The system SHALL provide the capability to generate Draw Steel Rewards including Treasures (consumables, trinkets, leveled treasures, artifacts) and Titles.

#### Scenario: Generate Consumable Treasure

**WHEN** a user requests "Create a [Echelon]-Echelon Consumable [Name]" or "Create a [Echelon]-Echelon Potion [Name]"

**THEN** the system SHALL generate a consumable treasure with:
- Appropriate project goal for echelon
- Item prerequisite (materials needed)
- Project source (where to find crafting info)
- Project roll characteristic
- Effect description with action type
- Keywords (Magic, Psionic, Potion, Oil, Scroll, etc.)
- Optional yield information for consumables that create multiple items

#### Scenario: Generate Trinket Treasure

**WHEN** a user requests "Create a [Echelon]-Echelon Trinket [Name]" or "Create a [Body Part] Trinket [Name]"

**THEN** the system SHALL generate a trinket treasure with:
- Appropriate project goal for echelon (1st=150)
- Item prerequisite
- Project source
- Project roll characteristic
- Effect description (usually passive benefits or triggered actions)
- Keywords including body part (Arms, Feet, Hands, Head, Neck, Waist, Ring)
- Magic or Psionic keyword

#### Scenario: Generate Leveled Treasure

**WHEN** a user requests "Create a [Treasure Type] Leveled Treasure [Name]"

**THEN** the system SHALL generate a leveled treasure with:
- Project goal of 450
- Item prerequisite
- Project source
- Project roll characteristic
- Three level benefits (1st, 5th, 9th level)
- Keywords for treasure type (Light Weapon, Heavy Armor, Implement, Ring, etc.)
- Magic or Psionic keyword
- Scaling bonuses (Stamina, damage, effects)

#### Scenario: Generate Title

**WHEN** a user requests "Create a [Echelon]-Echelon Title [Name]" or "Create a Title [Name]"

**THEN** the system SHALL generate a title with:
- Prerequisite (what must be accomplished)
- Effect section with 3-4 benefit options
- Each benefit should be thematic and balanced
- Some titles may grant abilities with Heroic Resource costs
- Optional echelon recommendation

### Requirement: Project Goal Calculation

The system SHALL calculate project goals for treasures based on type and echelon using established patterns.

#### Scenario: Calculate Consumable Project Goal

**WHEN** generating a consumable treasure

**THEN** project goal SHALL be:
- 1st Echelon: 45 (most), 30 for simpler items (e.g., Portable Cloud)
- 2nd Echelon: 90
- 3rd Echelon: 180 (most), 120 for some items
- 4th Echelon: 360

#### Scenario: Calculate Trinket Project Goal

**WHEN** generating a trinket treasure

**THEN** project goal SHALL be:
- 1st Echelon: 150
- Higher echelons: Scale up (pattern to be determined from more examples)

#### Scenario: Calculate Leveled Treasure Project Goal

**WHEN** generating a leveled treasure

**THEN** project goal SHALL be 450 for all leveled treasures regardless of type

#### Scenario: Calculate Artifact Project Goal

**WHEN** generating an artifact treasure

**THEN** project goal SHALL be higher than leveled treasures (pattern to be determined from artifact examples)

### Requirement: Leveled Treasure Scaling

The system SHALL generate leveled treasure benefits that scale appropriately across 1st, 5th, and 9th levels.

#### Scenario: Scale Stamina Bonus

**WHEN** a leveled treasure provides Stamina bonus

**THEN** the bonus SHALL scale as:
- 1st Level: +6 Stamina
- 5th Level: +12 Stamina
- 9th Level: +21 Stamina

#### Scenario: Scale Extra Damage

**WHEN** a leveled treasure provides extra damage

**THEN** the bonus SHALL scale as:
- 1st Level: +1 damage
- 5th Level: +2 damage
- 9th Level: +3 damage

#### Scenario: Scale Effect Areas

**WHEN** a leveled treasure creates areas (bursts, cubes, etc.)

**THEN** the area SHALL scale as:
- 1st Level: Base area (e.g., 3 burst)
- 5th Level: Increased area (e.g., 4 burst)
- 9th Level: Further increased area (e.g., 5 burst)

#### Scenario: Scale Additional Effects

**WHEN** a leveled treasure has additional effects at higher levels

**THEN** the effects SHALL become more powerful:
- 1st Level: Basic effect
- 5th Level: Enhanced effect (more damage, additional condition, etc.)
- 9th Level: Powerful effect (maximum damage, additional targets, unique abilities, etc.)

### Requirement: Treasure Keywords

The system SHALL assign appropriate keywords to treasures based on their type and function.

#### Scenario: Assign Magic or Psionic Keywords

**WHEN** generating any treasure

**THEN** it SHALL have either the Magic or Psionic keyword (or both) to indicate how it was created

#### Scenario: Assign Treasure Type Keywords

**WHEN** generating a treasure

**THEN** it SHALL have appropriate type keywords:
- Consumables: Potion, Oil, Scroll (if applicable)
- Trinkets: Body part keywords (Arms, Feet, Hands, Head, Neck, Waist, Ring)
- Leveled Weapons: Light Weapon, Medium Weapon, Heavy Weapon, Bow, Polearm, etc.
- Leveled Armor: Light Armor, Medium Armor, Heavy Armor, Shield
- Leveled Implements: Implement, Orb, Wand, etc.

#### Scenario: Assign Damage Type Keywords

**WHEN** a treasure deals damage of a specific type

**THEN** the effect description SHALL indicate the damage type (e.g., "deals extra 1 fire damage"), NOT as a keyword

### Requirement: Title Structure

The system SHALL generate titles with the correct structure and balance.

#### Scenario: Create Title Prerequisites

**WHEN** generating a title prerequisite

**THEN** it SHALL be:
- A specific accomplishment (defeat a creature, complete a task, etc.)
- Measurable and verifiable
- Thematic to the title
- Appropriate for the title's echelon

#### Scenario: Create Title Benefits

**WHEN** generating title benefits

**THEN** each benefit SHALL:
- Be balanced with other titles of the same echelon
- Provide a clear mechanical advantage
- Be thematic to the title
- Be one of 3-4 options (or single benefit for individual titles)

#### Scenario: Create Title Abilities

**WHEN** a title grants an ability

**THEN** the ability SHALL:
- Have a Heroic Resource cost (typically 3-9)
- Include ability type (Main action, Maneuver, etc.)
- Include keywords, distance, target if applicable
- Include power roll if applicable
- Be thematically appropriate to the title

### Requirement: Foundry VTT Export

The system SHALL generate Foundry VTT JSON for treasures and titles.

#### Scenario: Export Treasure to Foundry

**WHEN** generating a treasure with `--format foundry` or `--format both`

**THEN** the system SHALL create a JSON file compatible with Draw Steel Foundry system with:
- Item type (treasure)
- All treasure properties (keywords, effects, prerequisites, etc.)
- Proper folder assignment (Treasures or Titles)
- Valid _id format

#### Scenario: Export Title to Foundry

**WHEN** generating a title with `--format foundry` or `--format both`

**THEN** the system SHALL create a JSON file compatible with Draw Steel Foundry system with:
- Item type (title)
- Title prerequisites and benefits
- Proper folder assignment (Titles)
- Valid _id format