---
name: draw-steel-reward-generator
description: Generates Draw Steel TTRPG rewards (treasures and titles) with formula-compliant stat blocks. Use when creating treasures, titles, or crafting projects for the Draw Steel tabletop roleplaying game.
license: MIT
compatibility: Designed for Claude Code, Cursor, Gemini CLI, and Antigravity Google following the Agent Skills specification.
metadata:
  author: stgreenb
  version: "1.0"
---

# Draw Steel Reward Generator

Generate Draw Steel TTRPG rewards (treasures and titles) that strictly conform to official patterns from the Rewards chapter.

## Quick Start

**Input Format:** `"Create a [Treasure Type] [Reward Name], [Echelon] [options]"`

**Examples:**
- `"Create a 1st Echelon Consumable Healing Potion"`
- `"Create a 1st Echelon Trinket Color Cloak, Blue --format foundry"`
- `"Create a Leveled Treasure Fire Blade --format both"`
- `"Create a 1st Echelon Title Brawler --format foundry"`

**Output Formats:** `--format markdown` (default), `--format foundry`, `--format both`

## Cross-System Reward Conversion

**CRITICAL WARNING:** When converting rewards from other systems (D&D 5e, Pathfinder, etc.), use the source reward for **INSPIRATION ONLY**. Do NOT create equivalents or try to recreate D&D/PF2e mechanics in Draw Steel.

### What This Means

**✅ DO (Inspiration Only):**
- Extract the THEME and CONCEPT (fire sword, invisibility cloak, healing potion)
- Use the item type for keywords (potion → potion keyword, sword → weapon keyword)
- Take ability CONCEPTS and reimagine them with Draw Steel mechanics (fire damage → Draw Steel fire damage with proper effects)
- Use the source reward's echelon/level as a starting point

**❌ DO NOT (Never Create Equivalents):**
- Copy D&D/PF2e mechanics (saving throws, AC, ability scores, charges, attunement)
- Use D&D/PF2e terminology (hit points, proficiency, critical hit, DC, spell slots)
- Use D&D/PF2e damage types (piercing, slashing, bludgeoning, necrotic, radiant, thunder, force)
- Use D&D/PF2e characteristics (STR, DEX, CON, WIS, CHA)
- Try to recreate D&D/PF2e items - create NEW rewards that fit the theme

> **When converting from other systems:** `../shared/ANTI_PATTERNS.md`
> **When validating damage types or conditions:** `../shared/DRAW_STEEL_BASICS.md`

### Conversion Input Format

- `"Convert [Reward Name] from [System], [Echelon] [options]"`
- `"Convert [Reward Name]: [stat block/description] [options]"`

**Example:** `"Convert Vorpal Sword from D&D 5e, 3rd Echelon Leveled Treasure --format foundry"`

### Conversion Rules

**Extract from source (for inspiration):**
- Theme & concept (fire sword → fire keywords, fire damage)
- Item type & category (potion → consumable/potion, sword → weapon)
- Effect concepts (invisibility → stealth bonuses, teleportation)
- Echelon/power level (use as starting point)

**Calculate using Draw Steel patterns:**
- **Project Goals:** Use echelon-based formulas (see Project Goal Formulas section)
- **Keywords:** Magic or Psionic (creation method) + body/equipment keywords
- **Characteristics:** Use Draw Steel characteristics (Might, Agility, Reason, Intuition, Presence)
- **Project Roll:** Use characteristic-based power rolls with potency
- **Effects:** Use Draw Steel action types (maneuver, triggered) and conditions

## Fixed Damage Values (CRITICAL!)

Draw Steel NEVER uses dice notation. Always use fixed values calculated from Draw Steel formulas.

- ❌ WRONG: "1d6+3 damage"
- ✅ CORRECT: "6 damage"

**Common fixed damage values in Draw Steel rewards:**
- Extra damage on strikes: 1-5 (echelon 1), 5-10 (echelon 2-3)
- Area/environmental damage: 5 (echelon 1-2), 10 (echelon 2-3), 20 (echelon 4)
- Weapon enhancement: +1 to +3 damage bonus

> **When converting from other systems:** `../shared/ANTI_PATTERNS.md`
> **When validating damage types or conditions:** `../shared/DRAW_STEEL_BASICS.md`

## Damage Patterns in Draw Steel Rewards

**Draw Steel rewards handle damage differently than D&D items.** Unlike D&D where many items directly deal damage (e.g., Flask of Alchemist's Fire, Potion of Giant Strength), Draw Steel rewards use damage more sparingly and strategically.

### CRITICAL: Draw Steel Damage Philosophy

**Draw Steel rewards are NOT direct damage dealers like D&D items.**

| D&D Philosophy | Draw Steel Philosophy |
|----------------|------------------------|
| Many items deal damage directly | Few items deal damage directly |
| Damage is primary effect | Damage is secondary/tactical |
| Dice notation (1d6, 2d8) | Fixed values (1, 2, 5, 10, 20) |
| "deals X damage" is common | "deals X damage" is rare |
| Weapons have "+1 to hit and damage" | Weapons have "+1 to damage" |
| Simple damage output | Strategic damage with conditions |

**Key Takeaway:** In Draw Steel, rewards are more about:
- **Enhancement:** Modifying existing abilities (+1 damage)
- **Area Control:** Creating tactical areas (clouds, vortexes)
- **Defense:** Immunities, weakness trade-offs, reflection
- **Utility:** Movement, healing, condition removal

**Damage is a tool, not the primary purpose.**

### Key Differences from D&D

| Aspect | D&D Items | Draw Steel Rewards |
|--------|-----------|-------------------|
| **Direct damage items** | Common (potions, oils, scrolls) | Rare - mostly area/environmental |
| **Damage values** | Dice notation (1d6, 2d8, etc.) | Fixed values (1, 2, 5, 10, 20) |
| **Damage on use** | "deals X damage" when used | Usually conditional or area-based |
| **Weapon enhancement** | "+1 to hit and damage" | "+1 to damage" only |
| **Damage reflection** | Rare (Shield of Reflection) | More common (Mirror Token, Color Cloaks) |
| **Damage reduction** | Rare (Ring of Protection) | Appears (Stygian Liquor, Elixir of Saint Elspeth) |

### Damage Patterns by Reward Type

#### Consumables

**1. Small Extra Damage on Strikes (Common)**
- **Pattern:** "deals an extra [1-5] damage"
- **Examples:**
  - Black Ash Dart: "deals an extra 1 damage"
  - Snapdragon: "deals an extra 5 damage"
- **Usage:** Thrown weapons, darts, consumable attack items
- **Damage values:** 1-5 (echelon 1), 5-10 (echelon 2-3), 10+ (echelon 4)

**2. Area/Environmental Damage (Common)**
- **Pattern:** "Each creature who enters [area] takes [5-20] [type] damage"
- **Examples:**
  - Noxious Cloud: "Each creature who enters the cloud... takes 5 poison damage"
  - Thunderhead Cloud: "Each creature who enters the cloud... takes 5 lightning damage"
  - Vial of Ethereal Attack: "Each creature who enters the vortex... takes 10 psychic damage"
  - Page From Infinite Library: "takes 20 fire damage"
- **Usage:** Clouds, vortexes, walls, areas
- **Damage values:** 5 (echelon 1-2), 10 (echelon 2-3), 20 (echelon 4)
- **Common additions:** + condition (weakened, slowed, dazed)

**3. Weapon Enhancement Damage (Uncommon)**
- **Pattern:** "Whenever you use a weapon ability... deals an extra [1-2] [type] damage"
- **Examples:**
  - Giant's-Blood Flame: "deals an extra 2 fire damage"
  - Growth Potion: "damage bonus equal to your highest characteristic score"
- **Usage:** Oils, coatings, consumable buffs
- **Damage values:** 1-2 (echelon 1), 2-3 (echelon 2-3), 3-5 (echelon 4)

**4. Conditional Damage Bonuses (Rare)**
- **Pattern:** "If [condition], your strikes deal an extra [5] damage"
- **Examples:**
  - Chocolate of Immovability: "if you don't use your movement... strikes deal an extra 5 damage"
- **Usage:** Buffs with tactical conditions
- **Damage values:** 5 (echelon 2), 10 (echelon 3-4)

**5. Damage Reflection/Redirect (Rare)**
- **Pattern:** "Half the damage... imposed on the creature" or "redirects the triggering effect"
- **Examples:**
  - Mirror Token: "Half the damage you would have take... imposed on the creature making the strike"
  - G'Allios Visiting Card: "the devil redirects the triggering effect to a target"
- **Usage:** Defensive consumables
- **Damage values:** Half of incoming damage, or full redirect

**6. Damage Reduction (Rare)**
- **Pattern:** "take half the damage dealt by [condition]"
- **Examples:**
  - Stygian Liquor: "take half the damage dealt by the bleeding condition"
- **Usage:** Protective consumables
- **Damage values:** Half damage from specific sources

**7. Damage-Based Healing (Rare)**
- **Pattern:** "regain Stamina equal to [half/full] the damage dealt"
- **Examples:**
  - Blood Essence Vial: "regain Stamina equal to half the damage dealt"
- **Usage:** Vampiric/life-stealing consumables

**8. Variable Damage (Very Rare)**
- **Pattern:** "damage equal to [multiplier] × [characteristic]"
- **Examples:**
  - Anamorphic Larva: "psychic damage equal to three times their Intuition score"
- **Usage:** Complex, high-echelon consumables

#### Trinkets

**1. Immunity/Weakness Trade-offs (Common)**
- **Pattern:** "grants [type] immunity... becomes [type] weakness when used"
- **Examples:**
  - Color Cloak (Blue): "cold immunity... becomes cold weakness"
  - Color Cloak (Red): "fire immunity... becomes fire weakness"
  - Color Cloak (Yellow): "lightning immunity... becomes lightning weakness"
- **Usage:** Protective trinkets with triggered abilities
- **Damage values:** Immunity equal to level, weakness equal to level

**2. Damage Bonuses on Strikes (Uncommon)**
- **Pattern:** "gain a [+2] damage bonus for any weapon ability"
- **Examples:**
  - Bracers of Strife: "gain a +2 damage bonus for any weapon ability"
- **Usage:** Combat enhancement trinkets
- **Damage values:** +2 (echelon 3), +3 (echelon 4)

**3. Damage on Triggered Action (Uncommon)**
- **Pattern:** "cause the next damage-dealing ability you use to deal extra [type] damage"
- **Examples:**
  - Color Cloak (Yellow): "deals extra lightning damage equal to your level"
- **Usage:** Reactive trinkets
- **Damage values:** Equal to level or characteristic

**4. Environmental/Hazard Damage (Rare)**
- **Pattern:** "takes [damage] for each [unit] of [hazard]"
- **Examples:**
  - Deadweight: "extra 1 damage for each square you fall"
- **Usage:** Hazard-related trinkets

**5. Projectile Damage (Rare)**
- **Pattern:** "Each [projectile] you launch deals [5] damage"
- **Examples:**
  - Mask of Oversight: "Each eye you launch deals 5 damage"
- **Usage:** Trinkets with projectile abilities

**6. Psychic/Energy Blade Damage (Rare)**
- **Pattern:** "make a melee free strike that deals an extra [3] [psychic] damage"
- **Examples:**
  - Psi Blade: "extra 3 psychic damage"
- **Usage:** Energy-based trinkets
- **Damage values:** 3 (echelon 4)

#### Leveled Treasures

**1. Damage Bonus Scaling (Universal)**
- **Pattern:** "deals an extra [+1/+2/+3] damage" (1st/5th/9th level)
- **Examples:**
  - All weapons: +1/+2/+3 damage
  - All implements: +1/+2/+3 damage
  - Some special items: +2/+3/+4 extra psychic damage
- **Usage:** ALL leveled weapons and implements
- **Damage values:** Fixed scaling by level

**2. Immunity at Higher Levels (Common)**
- **Pattern:** "9th Level: have immunity [10] to [damage types]"
- **Examples:**
  - Blade of Quintessence: "immunity 10 to cold, fire, lightning, and sonic"
- **Usage:** High-level leveled treasures
- **Damage values:** Immunity 10 (typically)

**3. Extra Damage Type (Common)**
- **Pattern:** "change the damage type to [type]"
- **Examples:**
  - Blade of Quintessence: "change the damage type to cold, fire, lightning, or sonic"
- **Usage:** Weapons with elemental properties

### Damage Value Guidelines by Echelon

| Echelon | Small Extra Damage | Area Damage | Weapon Bonus | Maximum Damage |
|---------|-------------------|--------------|--------------|----------------|
| 1st | 1-2 | 5 | 1 | 10 |
| 2nd | 2-3 | 5-10 | 2 | 15 |
| 3rd | 3-5 | 10-15 | 2-3 | 20 |
| 4th | 5-10 | 15-20 | 3-5 | 25+ |

### Common Mistakes to Avoid

**❌ DON'T create rewards like D&D items:**
- Flask of Alchemist's Fire → Don't make "deals 1d6 fire damage"
- Potion of Fire Breath → Don't make "deals 8d6 fire damage in a cone"
- Oil of Sharpness → Don't make "+1d6 damage on critical hits"

**✅ DO create Draw Steel-style rewards:**
- "Deals an extra 2 fire damage" (weapon enhancement)
- "Each creature in the area takes 10 fire damage" (area effect)
- "+2 damage bonus for any weapon ability" (trinket bonus)

### When Rewards Deal Damage (vs. When They Don't)

**Rewards SHOULD deal damage when:**
- Creating area/environmental effects (clouds, vortexes, walls)
- Enhancing weapons temporarily (oils, coatings)
- Providing tactical bonuses (conditional damage)
- Reflecting or redirecting damage
- Creating projectiles or energy attacks

**Rewards SHOULD NOT deal damage when:**
- Providing healing (use fixed stamina values)
- Granting immunities/weaknesses (use immunity values)
- Providing movement bonuses (use speed/shift values)
- Granting characteristic bonuses (use +1/+2/+3)
- Applying or removing conditions (use condition names)

### Example: Converting D&D Items to Draw Steel

**Example 1: Flask of Alchemist's Fire (D&D 5e)**

**D&D Description:**
> "This sticky, adhesive fluid ignites when exposed to air. As an action, you can throw this flask up to 20 feet, shattering it on impact. A target takes 1d4 fire damage at the start of each of its turns. A creature can end this damage by using its action to scrape off the fluid or by spending 10 feet of movement to do so."

**WRONG Draw Steel Conversion:**
> "Fire Flask: As a maneuver, you throw this flask up to 4 squares. The target takes 1d4 fire damage at the start of each of its turns."
> - Uses D&D dice notation (1d4)
> - Directly copies D&D mechanics

**CORRECT Draw Steel Reward:**
> "Inferno Oil: As a maneuver, you coat a weapon in this oil and ignite it. Whenever you use a weapon ability that deals rolled damage using a weapon that is ignited this way, the ability deals an extra 2 fire damage. Alternatively, you can throw the pot up to 5 squares, coating the square where it lands. If the oil takes any fire damage, it burns persistently and deals 5 fire damage at the end of each of your turns to anything it has coated."
> - Uses fixed damage values (2, 5)
> - Provides weapon enhancement OR area effect
> - Follows Draw Steel patterns

**Example 2: Potion of Giant Strength (D&D 5e)**

**D&D Description:**
> "When you drink this potion, your Strength score becomes 25 for 1 hour. The potion has no effect if your Strength is already equal to or greater than that score."

**WRONG Draw Steel Conversion:**
> "Giant's Tonic: When you drink this potion, your Might becomes 25 for 1 hour."
> - Uses D&D characteristic score concept (Might 25)
> - Directly copies D&D mechanics

**CORRECT Draw Steel Reward:**
> "Titan's Tonic: As a maneuver, you drink this tonic to gain +3 to Might and an edge on Might tests until the end of your next turn. Additionally, you gain immunity 5 to being grabbed or restrained for the same duration."
> - Uses Draw Steel characteristic bonuses (+3, edge)
> - Uses Draw Steel mechanics (immunity, conditions)
> - Uses tactical duration (end of next turn, not 1 hour)

**Example 3: Scroll of Fireball (D&D 5e)**

**D&D Description:**
> "You can cast the Fireball spell from this scroll. The spell creates a 20-foot-radius sphere of fire. Each creature in the area must make a DC 15 Dexterity saving throw, taking 8d6 fire damage on a failed save, or half as much on a successful one."

**WRONG Draw Steel Conversion:**
> "Scroll of Inferno Burst: As a maneuver, you cast this scroll to create a 4 cube of fire. Each creature in the area takes 8d6 fire damage."
> - Uses D&D dice notation (8d6)
> - Uses D&D saving throw concept
> - Directly copies D&D mechanics

**CORRECT Draw Steel Reward:**
> "Scroll of Inferno Burst: As a maneuver, you spend 1 Heroic Resource to destroy this page and create a 4-cube area within 20 squares. The area is filled with the energy of a tiny sun that lasts until the end of the encounter. Any creature who enters the area for the first time in a combat round or starts their turn there takes 20 fire damage and is dazed."
> - Uses fixed damage value (20, not 8d6)
> - Uses Draw Steel area mechanics (4 cube, not 20-foot radius)
> - Uses Draw Steel condition (dazed, not saving throw)
> - Uses Heroic Resource cost and encounter duration

### Examples

**D&D 5e Potion of Healing:**
> "You regain 2d4+2 hit points."

**WRONG Draw Steel:**
> "You gain 2d4+2 stamina."

**CORRECT Draw Steel:**
> "You gain 6 stamina." (average of 2d4+2 = 7, rounded down)

**D&D 5e Fireball:**
> "Each creature in a 20-foot radius takes 8d6 fire damage."

**WRONG Draw Steel:**
> "Each creature in a 4 cube takes 8d6 fire damage."

**CORRECT Draw Steel:**
> "Each creature in a 4 cube takes 28 fire damage." (average of 8d6 = 28)

### Validation Note

The validation script will flag any occurrence of `d4`, `d8`, `d12`, or `d20` as an error. These dice types are **never valid** in Draw Steel reward descriptions.

**Use fixed values only.**

## Reward Types

### Consumables
Single-use items with immediate effects. Includes potions, oils, scrolls, darts, dusts, tokens, and other one-use items.

### Trinkets
Wearable items with passive effects and optional triggered abilities. Include body keywords (Arms, Feet, Hands, Head, Neck, Waist, Ring).

### Leveled Treasures
Equipment that scales with hero level (1st, 5th, 9th). Includes weapons, armor, shields, implements, rings, and other wearable items.

### Titles
Accomplishments heroes can earn. Each title has prerequisites and 3-4 benefit options (or single benefit for individual titles).

## Project Goal Formulas

### Consumables

| Echelon | Project Goal | Notes |
|---------|--------------|-------|
| 1st | 30 or 45 | 30 for simple items, 45 for most |
| 2nd | 90 | Standard |
| 3rd | 120 or 180 | 120 for some, 180 for most |
| 4th | 360 | Standard |

### Trinkets

| Echelon | Project Goal | Formula |
|---------|--------------|---------|
| 1st | 150 | 150 × 1 |
| 2nd | 300 | 150 × 2 |
| 3rd | 450 | 150 × 3 |
| 4th | 600 | 150 × 4 |

### Leveled Treasures

| Treasure Type | Project Goal | Notes |
|---------------|--------------|-------|
| All Leveled Treasures | 450 | Weapons, armor, shields, implements, rings, etc. |

### Artifacts

| Echelon | Project Goal | Notes |
|---------|--------------|-------|
| 1st | 600+ | Higher than leveled treasures |
| 2nd | 750+ | Further analysis needed |
| 3rd | 900+ | Further analysis needed |
| 4th | 1050+ | Further analysis needed |

**Note:** Artifact patterns need further analysis. Use higher values than leveled treasures as starting point.

## Required Keywords

### All Treasures
Every treasure must have **Magic** or **Psionic** keyword (or both). These indicate creation method, not usage restrictions.

- **Magic:** Standard magical creation
- **Psionic:** Psionic/mental creation
- **Magic, Psionic:** Both methods possible

**Keywords do NOT restrict use.** Magic items can be used by anyone, Psionic items can be used by anyone.

### Consumable Type Keywords

| Keyword | When to Use | Examples |
|---------|-------------|---------|
| **Potion** | Drinkable liquid consumables | Healing Potion, Bull Shot, Growth Potion |
| **Oil** | Applied to weapons or thrown | Buzz Balm, Giant's-Blood Flame |
| **Scroll** | Readable/chantable magic texts | Scroll of Resurrection |
| (None) | Other consumables | Black Ash Dart, Catapult Dust, Mirror Token |

### Body Keywords (Trinkets/Leveled Treasures)

| Keyword | Location | Notes |
|---------|----------|-------|
| **Arms** | Bracers, gauntlets | Can wear multiple with same keyword if Director allows |
| **Feet** | Boots, sandals | Can wear multiple with same keyword if Director allows |
| **Hands** | Gloves, rings | Can wear multiple with same keyword if Director allows |
| **Head** | Helmets, crowns | Can wear multiple with same keyword if Director allows |
| **Neck** | Cloaks, amulets, necklaces | Can wear multiple with same keyword if Director allows |
| **Waist** | Belts, sashes | Can wear multiple with same keyword if Director allows |
| **Ring** | Rings | Can wear multiple with same keyword if Director allows |

**Rule:** Can wear multiple treasures with same body keyword IF Director allows. If Director deems too many, NONE function.

### Equipment Keywords (Leveled Treasures)

- **Weapon Categories:** Light Weapon, Medium Weapon, Heavy Weapon, Bow, Polearm, etc.
- **Armor Categories:** Light Armor, Medium Armor, Heavy Armor, Shield
- **Implement Types:** Implement, Orb, Wand, etc.

## Leveled Treasure Scaling

### Armor Scaling (Light, Medium, Heavy)

| Level | Stamina |
|-------|---------|
| 1st | +6 |
| 5th | +12 |
| 9th | +21 |

**Examples:** Adaptive Second Skin of Toxins, Chain of the Sea and Sky, Grand Scarab

### Shield Scaling

| Shield | 1st | 5th | 9th |
|--------|-----|-----|-----|
| King's Roar | +3 Stamina | +6 Stamina | +9 Stamina |
| Telekinetic Bulwark | +2 Stamina | +5 Stamina | +9 Stamina |

### Implement Scaling

| Level | Damage Bonus |
|-------|--------------|
| 1st | +1 |
| 5th | +2 |
| 9th | +3 |

**Alternative:** +2 → +3 → +4 extra psychic damage (Brittlebreaker - starts higher)

**Examples:** Abjurer's Bastion, Chaldorb, Ether-Fueled Vessel, Foesense Lenses

### Weapon Scaling

| Level | Damage Bonus |
|-------|--------------|
| 1st | +1 |
| 5th | +2 |
| 9th | +3 |

**Extra damage examples:** +1/+2/+3 psychic (Displacer), +1/+2/+3 cold (Icemaker Maul), +1/+2/+3 poison (Onerous Bow)

**Examples:** 15+ published weapon examples

### Other Leveled Treasures

| Treasure Type | 1st | 5th | 9th |
|---------------|-----|-----|-----|
| Ring (Bloodbound Band) | +6 Stamina | +12 Stamina | +21 Stamina |
| Hand wraps (Bloody Hand Wraps) | +1 damage | +2 damage | +3 damage |
| Feet (Lightning Treads) | +1 extra lightning | +2/+3 extra lightning | +6 extra lightning |
| Neck (Revenger's Wrap) | Special effect | Special effect | Special effect |

## Project Source Patterns

Every treasure has a Project Source specifying WHERE the knowledge comes from:

| Region | Theme | Examples |
|--------|-------|----------|
| **Caelian** | Standard magic (most common) | Healing Potion, Catapult Dust, Growth Potion |
| **Anjali** | Infernal/contract magic, licensing | Vial of Ethereal Attack, Color Cloaks, Stygian Liquor |
| **Zaliac** | Psionic technology, constructs | Pocket Homunculus, Telemagnet, Ward Token |
| **Khelt** | Fey magic, nature-based | Float Powder, Divine Vine, Flameshade Gloves |
| **Yllyric** | Specialized magic | Snapdragon, Concealment Potion, Purified Jelly |
| **Variac** | Psychic/mental magic | Mirror Token, Anamorphic Larva, Wellness Tonic |
| **Hyrallic** | Divine/spiritual magic | Breath of Dawn, Mediator's Charm |
| **Ullorvic** | Memory/mind magic | Key of Inquiry |
| **High Kuric** | Physical strength magic | Bastion Belt |
| **First Language** | Ancient/powerful magic | Scroll of Resurrection, Breath of Creation |
| **Proto-Ctholl** | Blood magic, vampiric | Blood Essence Vial |
| **Voll** | Time magic | Timesplitter |
| **Szetch** | Shadow magic | Black Ash Dart |
| **Kalliak** | Elemental/nature magic | Buzz Balm |
| **Khemharic** | Death magic, resurrection | Personal Effigy |

**Match source to effect theme:**
- Teleportation → Zaliac (psionic tech)
- Fire/elemental → Caelian (standard magic) or Kalliak (nature)
- Blood/life essence → Proto-Ctholl
- Divine/resurrection → First Language or Hyrallic
- Fey/nature → Khelt or Yllyric
- Psionic/mental → Variac or Zaliac
- Time → Voll
- Shadow → Szetch
- Infernal/contracts → Anjali

## Project Roll Characteristic Patterns

Every treasure specifies which characteristics can be used for crafting tests:

### Reason or Intuition (~70% of treasures)
- General magic/psionic crafting
- Alchemical preparations
- Standard enchanting
- **Examples:** Healing Potion, Catapult Dust, Portable Cloud, Bull Shot

### Agility or Intuition (~15%)
- Delicate construction
- Precise application magic
- **Examples:** Black Ash Dart, Concealment Potion, Shifting Ring

### Might or Intuition (~10%)
- Physical reagents with spiritual components
- Requires strength to manipulate materials
- **Examples:** Anamorphic Larva, Ward Token, Wellness Tonic

### Intuition or Presence (~10%)
- Divine magic
- Fey magic
- Requires force of personality
- **Examples:** Breath of Dawn, Float Powder, Restorative of Bright Court

### Presence Only (Rare)
- Requires exceptional force of personality
- **Example:** Elixir of Saint Elspeth

### Reason Only (Rare)
- Requires exceptional technical knowledge
- **Example:** Pocket Homunculus, Professor Veratismo's Quaff

### Multiple Characteristics
Some allow 3 options:
- **Examples:** King's Roar (Might, Reason, or Intuition), Chain of the Sea and Sky (Might, Reason, or Intuition)

**Valid characteristic names (lowercase):** `reason`, `intuition`, `agility`, `might`, `presence`

## Power Rolls and Tiered Outcomes

**IMPORTANT:** Rewards have TWO types of power rolls:
1. **Project Roll** - For crafting the treasure (documented above)
2. **Effect Power Roll** - For using the treasure's abilities (documented here)

### When Rewards Use Power Rolls

Rewards use power rolls for their effects when:
- The reward creates a variable effect based on the roll
- The reward has tiered outcomes (≤11, 12-16, 17+)
- The effect requires a characteristic test
- The reward enhances an existing ability with variable bonuses

**Examples:**
- Black Ash Dart: "adds the following effects to the tier outcomes of the power roll"
- Lachomp Tooth: "adds the following effects to the tier outcomes of the power roll"
- Timesplitter: "adds the following effects to the tier outcomes of the power roll"

### Power Roll Structure

When a reward uses a power roll for its effect, it follows this format:

```
Effect: As a maneuver, you [action]. The [ability] adds the following effects to the tier outcomes of the power roll:
- ≤11: [Effect 1]
- 12-16: [Effect 2]
- 17+: [Effect 3]
```

**Key Points:**
- **≤11:** Weak outcome (minimum effect)
- **12-16:** Average outcome (moderate effect)
- **17+:** Strong outcome (maximum effect)
- The roll uses the same characteristics as the ability being enhanced
- The roll result determines which effect applies

### Tiered Outcome Patterns

**1. Distance/Range Scaling**
- **≤11:** 2 squares
- **12-16:** 4 squares
- **17+:** 6 squares
- **Example:** Black Ash Dart (teleport distance)

**2. Target Count Scaling**
- **≤11:** 1 additional target
- **12-16:** 3 additional targets
- **17+:** 7 additional targets
- **Example:** Lachomp Tooth (multi-target strike)

**3. Area Size Scaling**
- **≤11:** 3 cube
- **12-16:** 5 cube
- **17+:** 8 cube
- **Example:** Timesplitter (area of slowed condition)

**4. Condition + Area Scaling**
- **≤11:** Condition within 3 squares
- **12-16:** Condition within 5 squares
- **17+:** Condition within 8 squares
- **Example:** Timesplitter (slowed condition area)

**5. Damage + Condition Scaling**
- **≤11:** X damage, condition (weak potency)
- **12-16:** Y damage, condition (medium potency)
- **17+:** Z damage, condition (strong potency)
- **Example:** Not common in rewards, but possible

### Potencies in Rewards

**Potencies determine how hard an effect is to resist.** Potencies are used with conditions to determine if they succeed.

**Potency Levels:**
- **Weak:** Characteristic - 2 (easiest to resist)
- **Average:** Characteristic - 1 (moderate difficulty)
- **Strong:** Characteristic (hardest to resist)

**Potency Usage:**
- **With conditions:** "slowed (M < 2)" means Might less than 2
- **With saves:** "(save ends)" means target makes a save at end of each turn
- **Without potency:** Effect always applies

**Example from Stygian Liquor:**
> "while you are dying, you gain on edge on power rolls"

This is NOT a potency - it's a bonus to the roll itself.

### Save Ends

**"Save ends"** indicates a persistent condition that ends when the target makes a successful save.

**How it works:**
1. Condition is applied (e.g., "slowed save ends")
2. At the end of each of the target's turns, they make a save
3. If save succeeds, condition ends
4. If save fails, condition continues

**Save vs. Potency:**
- **"save ends":** Target makes their own save each turn
- **"A < 2":** Potency check against Agility characteristic
- **"M < 3":** Potency check against Might characteristic
- **"R < 1":** Potency check against Reason characteristic

**Common Mistake:**
- ❌ WRONG: "DC 15 save" (D&D terminology)
- ✅ RIGHT: "slowed (save ends)" or "slowed (A < 2)"

### NO DC in Draw Steel Rewards

**Rewards NEVER use DC (Difficulty Class).**

| D&D Term | Draw Steel Term | Why It's Wrong |
|----------|-----------------|---------------|
| "DC 15" | "A < 2" or "save ends" | DC is D&D terminology |
| "DC 15 Constitution save" | "M < 2" or "potency weak" | Wrong system |
| "save DC" | "save" or "potency" | DC not used in Draw Steel |
| "saving throw" | "save" | Use "save" not "saving throw" |

**How to Convert D&D DCs:**

| D&D DC | Draw Steel Equivalent | When to Use |
|---------|---------------------|-------------|
| DC 10 | "save ends" (no potency) | Easy effects |
| DC 13 | "A/R/M/P < 1" (characteristic - 2) | Weak potency |
| DC 15 | "A/R/M/P < 2" (characteristic - 1) | Average potency |
| DC 18 | "A/R/M/P" (characteristic) | Strong potency |
| DC 20+ | "A/R/M/P + 1" (characteristic + 1) | Very strong potency |

**Example Conversion:**

**D&D:**
> "Target makes a DC 15 Dexterity saving throw or be slowed."

**WRONG Draw Steel:**
> "Target makes a DC 15 Agility save or is slowed."

**CORRECT Draw Steel:**
> "Target is slowed (A < 2)."

**OR:**
> "Target is slowed (save ends)."

## Characteristic Bonuses vs. Edges

**CRITICAL:** No treasure type grants direct characteristic bonuses like "+2 to Might". This pattern does not exist in Draw Steel.

### What This Means

**Consumables and Trinkets:**
- ✅ **USE:** "gain an edge on Intuition tests" or "gain a double edge on Might tests"
- ❌ **DON'T:** "gain +2 to Intuition" or "gain +3 to Might"
- ❌ **DON'T:** "characteristic bonus +2" (this is not Draw Steel terminology)

**Leveled Treasures:**
- Do NOT grant direct characteristic increases either
- Use damage bonuses (+1/+2/+3), stamina bonuses (+6/+12/+21), or characteristic-based calculations
- Example: "damage bonus equal to your highest characteristic score" (Growth Potion, Revenger's Wrap)
- Example: "bonus to Stamina equal to twice your highest characteristic score" (Thief of Joy)

### Scaling Patterns

**Consumable Scaling:**
- **Echelon 1:** Single edge ("gain an edge on Intuition tests")
- **Echelon 2:** Single edge with additional effect
- **Echelon 3:** Double edge ("gain a double edge on Intuition tests")
- **Echelon 4:** Double edge with additional effect

**Leveled Treasure Scaling:**
- **1st Level:** +1 damage bonus or +6 Stamina
- **5th Level:** +2 damage bonus or +12 Stamina
- **9th Level:** +3 damage bonus or +21 Stamina

### Examples from Published Content

**CORRECT (Edges):**
- Growth Potion: "gain an edge on Might tests"
- Stygian Liquor: "gain on edge on power rolls"
- Most buff consumables: "gain an edge on [characteristic] tests"

**CORRECT (Situational Bonuses - Rare):**
- Buzz Balm: "gain a +2 bonus to speed"
- Chocolate of Immovability: "gain a +10 bonus to Stability"

**INCORRECT (Direct Characteristic Bonuses):**
- "gain +2 to Intuition" - NOT Draw Steel pattern
- "gain +3 to Might" - NOT Draw Steel pattern
- "characteristic bonus +2" - NOT Draw Steel terminology

### When to Use Edges vs. Direct Bonuses

**Use EDGES when:**
- Enhancing tests (Intuition tests, Reason tests, etc.)
- Temporary buffs from consumables or trinkets
- All characteristic-related enhancements

**Use SITUATIONAL BONUSES when:**
- Speed bonuses (+2 to speed)
- Stability bonuses (+5 to +10 Stability)
- Distance bonuses (+2 to +5 to distance)
- Damage reduction bonuses

**Use CHARACTERISTIC-BASED CALCULATIONS when:**
- "equal to your highest characteristic score" (damage, stamina, immunity)
- "equal to [multiplier] × your highest characteristic score" (Thief of Joy)
- NEVER use direct "+X to [characteristic]"

### Example: Converting D&D Items

**D&D 5e Potion of Insight:**
> "When you drink this potion, you gain a +1d4 bonus to Wisdom saving throws and Wisdom (Perception) checks for 1 hour."

**WRONG Draw Steel Conversion:**
> "gain +2 to Intuition for 1 hour"

**CORRECT Draw Steel Conversion:**
> "gain an edge on Intuition tests until the end of your next turn"

**Key Differences:**
- No +X to characteristic - use edge instead
- No "saving throws" - use tests
- No "1 hour" - use encounter-based duration
- Edge is more flexible and tactical

### Summary

| Reward Type | Enhancement Pattern | Example |
|-------------|---------------------|---------|
| **Consumables** | Edge on tests | "gain an edge on Intuition tests" |
| **Trinkets** | Edge on tests or passive effects | "gain an edge on Might tests" |
| **Leveled Treasures** | Damage/Stamina bonuses | "+1 damage bonus" or "+6 Stamina" |
| **Situational** | Speed/Stability/Distance bonuses | "+2 bonus to speed" |
| **Characteristic-based** | Multiplier of score | "equal to your highest characteristic score" |

**Rule:** If you're about to write "+X to [characteristic]", stop and use "edge on [characteristic] tests" or "equal to your [characteristic] score" instead.

## Immunity Patterns

Draw Steel uses THREE distinct immunity patterns. Choose based on the treasure's design:

### Pattern 1: Level-Based Scaling

**Format:** `immunity equal to your level`

**Examples:**
- Color Cloak (Blue): "grants you cold immunity equal to your level"
- Color Cloak (Red): "grants you fire immunity equal to your level"
- Color Cloak (Yellow): "grants you lightning immunity equal to your level"

**When to Use:**
- Trinkets with immunity/weakness trade-offs
- Effects that scale with hero progression
- 1st-echelon trinkets

### Pattern 2: Characteristic-Based Scaling

**Format:** `immunity equal to your highest characteristic score`

**Examples:**
- Adaptive Second Skin of Toxins: "immunity to acid and poison damage equal to your highest characteristic score"
- Elemental Dabbler title: "immunity to the chosen damage type equal to your highest characteristic score"

**When to Use:**
- Leveled treasures at 1st level
- Characteristic-themed effects
- When the immunity should vary by character build

### Pattern 3: Fixed Values

**Format:** `immunity [value]` (typically 5 or 10)

**Examples:**
- Chain of the Sea and Sky (5th): "cold immunity 5"
- Chain of the Sea and Sky (9th): "cold immunity 10"
- Blade of Quintessence (9th): "immunity 10 to cold, fire, lightning, and sonic"

**When to Use:**
- Higher-level benefits in leveled treasures (5th/9th level)
- Artifacts
- Static protective effects

### When NOT to Use

**NEVER use these patterns (not in published content):**
- ❌ "immunity equal to half your level"
- ❌ "immunity equal to your level divided by 2"
- ❌ Fractional or minimum value scaling

**Choose one of the three valid patterns instead.**

## When Rewards Use Power Rolls vs. Fixed Effects

**Use Power Rolls when:**
- Effect is variable and depends on the roll
- Multiple outcomes based on roll result (≤11, 12-16, 17+)
- Reward enhances an existing ability
- Effect requires a characteristic test

**Use Fixed Effects when:**
- Effect is always the same (no variation)
- Single outcome regardless of roll
- Simple, straightforward effects
- Most consumables (healing, buffs, debuffs)

**Examples:**

**Power Roll (Variable):**
```
Black Ash Dart: "adds the following effects to the tier outcomes of the power roll:
- ≤11: You can teleport the target up to 2 squares.
- 12-16: You can teleport the target up to 4 squares.
- 17+: You can teleport the target up to 6 squares."
```

**Fixed Effect (No Variable):**
```
Healing Potion: "you gain 6 stamina and remove the weakened condition."
```

### Power Roll Characteristics

**The power roll uses the same characteristics as the ability being enhanced:**

| Ability Type | Power Roll Characteristics | Example |
|---------------|---------------------------|---------|
| Melee weapon ability | Might, Agility, Reason | Black Ash Dart (thrown weapon) |
| Ranged weapon ability | Might, Agility, Reason | Lachomp Tooth (attached to weapon) |
| Magic ability | Reason, Intuition | Most consumable power rolls |

**Rule:** Match the power roll characteristics to the type of ability the treasure enhances.

## Effect Structure Patterns

### Consumables

**Primary Format:** "As a maneuver, you [action] to [effect]..."

- **Drinking:** "you drink this potion" (Healing Potion, Bull Shot, Growth Potion)
- **Applying:** "you rub/coat [target]" (Buzz Balm, Giant's-Blood Flame)
- **Throwing:** "you throw [item] up to X squares" (Portable Cloud, Vial of Ethereal Attack)
- **Activating:** "you [activate/use/crush/tear] [item]" (Mirror Token, Snapdragon)

**Triggered Action Format:**
"When/Whenever [trigger], you can use a triggered action to [action]..."
- **Examples:** Mirror Token, Blood Essence Vial, G'Allios Visiting Card

**Respite Activity Format:**
"As a respite activity, you [action]..."
- **Examples:** Scroll of Resurrection

**Typical Duration:**
- **Instant:** Healing, damage, teleport (Healing Potion, Black Ash Dart)
- **1 hour:** Utility effects (Imp's Tongue, Float Powder, Purified Jelly)
- **3-10 rounds:** Combat buffs (Growth Potion, Chocolate of Immovability)
- **End of encounter:** Major combat effects (Ward Token, Chocolate of Immovability)
- **Until condition ends:** Triggered protections

### Trinkets

**Primary Format:** "While worn, [passive effect]..."
**Secondary Format:** "Additionally, [triggered ability]..."

**Pattern:** Passive bonus + situational triggered action
- **Example:** Color Cloak grants immunity, triggered action has tradeoff (immunity becomes weakness)

### Triggered Action Treasure Design Pattern

**Common Structure:**
1. **Passive Benefit:** Constant effect while worn
2. **Triggered Action:** "when [condition], you can use a triggered action to [effect]"
3. **Trade-off:** Powerful effect with temporary downside

**Color Cloak Template:**
- Passive: Immunity X (equal to level)
- Trigger: When targeted by X damage
- Effect: [Powerful response]
- Downside: Immunity becomes weakness (same value) until end of next round
- Restriction: "You can't use this again until [downside] ends"

**Design Guidance:**
- Trigger should relate to passive benefit (thematic synergy)
- Effect should be proportionally powerful to downside
- Downside duration should be meaningful but not crippling (1-2 rounds)

### Trinkets with Embedded Abilities

Some trinkets grant the wearer a new ability. When a trinket grants an ability with a power roll, use the embedded ability format:

**Structure:**
```
**Effect:** [Passive effect]. Additionally, you have the following ability.

###### Ability Name

*Flavor text for the ability*

| **Keywords, Distance Type** |             **Action Type** |
| --------------------------- | -------------------------: |
| **📏 Distance**             | **🎯 Target**              |

**Power Roll + Characteristic:**
- **≤11:** Effect (weak outcome)
- **12-16:** Effect with potency condition
- **17+:** Effect with stronger potency condition

**Effect:** Additional effects not tied to tier outcomes.
```

**Example (Mirage Band):**
```
**Effect:** While wearing the Mirage Band, you automatically perceive illusions for what they are, you can see invisible creatures, and supernatural effects can't conceal creatures and objects from you.

Additionally, you have the following ability.

###### Hallucination Field

*A blanket of illusion twists around you and your allies, making you seem as if you belong wherever you are.*

| **Psionic, Ranged** |             **Maneuver** |
| ------------------- | -----------------------: |
| **📏 Ranged 10**    | **🎯 Self and any ally** |

**Effect:** Each target is covered by an illusion causing them to appear exactly as any creature an observer most expects to see.
```

**Example (Nullfield Resonator Ring):**
```
**Effect:** You must be a null to wear this ring. While you do so, the area of your Null Field ability increases by 1.

Additionally, you have the following ability.

###### Nullring Strike

*Your punch delivers a devastating burst of psionic energy.*

| **Melee, Psionic**, **Strike, Weapon** |               **Main action** |
| -------------------------------------- | ----------------------------: |
| **📏 Melee 1**                         | **🎯 One creature or object** |

**Power Roll + Might or Agility:**
- **≤11:** 3 psychic damage
- **12-16:** 5 psychic damage; I < AVERAGE, slowed (save ends)
- **17+:** 8 psychic damage; I < STRONG, slowed (save ends)

**Effect:** While slowed in this way, the target takes a bane on magic or psionic abilities.
```

**When to Use Embedded Abilities:**
- Trinkets that grant a full ability (main action, maneuver with power roll)
- When the ability has its own distinct name and flavor
- When the ability is substantial enough to warrant separate documentation

**When NOT to Use Embedded Abilities:**
- Simple triggered actions (use standard Effect format)
- Passive bonuses (use standard Effect format)
- Abilities that modify existing actions (use standard Effect format)

## Yield Mechanics for Consumables

### When to Include Yield
- Small, portable items (darts, teeth, flowers, powder)
- Items that can be divided (doses, vials)
- Crafting recipes that produce batches
- **This is COMMON, not rare** - core mechanic for economical crafting

### Typical Yield Formulas
- **1d3:** Common for small items (Black Ash Dart: 1d3 darts, Lachomp Tooth: 1d3 teeth, Float Powder: 1d3 vials)
- **1d6 + 1:** Flowers, natural materials (Snapdragon: 1d6 + 1 snapdragons)
- **Fixed:** Some items give exact multiples (Black Ash Dart: "three darts if crafted by a shadow")

### When NOT to Include Yield
- Single-use potions (consumed entirely - Healing Potion, Bull Shot, Growth Potion)
- Unique items (tokens, scrolls - Mirror Token, Scroll of Resurrection)
- Large items (can't mass-produce)

## Conditional Crafting Bonuses

### Crafter-Specific Bonuses
Some treasures have enhanced yield for specific ancestries/backgrounds:
- **Example:** Black Ash Dart: "yields 1d3 darts, or **three darts if crafted by a shadow**"

### Design Guidance
- Use crafter bonuses sparingly
- Tie to thematic connection (shadows crafting shadow items)
- Bonus can be:
  - Fixed yield instead of random (3 instead of 1d3)
  - Higher yield (1d6 instead of 1d3)
  - Reduced project goal (special knowledge)

## Item Prerequisite Guidelines

### NOT a Formula - Use Thematic Appropriateness

**Echelon 1** (Common but supernatural):
- Monster parts (giant blood, imp tongue, lachomp tooth)
- Cultivated magical plants (seagrass, nightshade roots, snapdragon seeds)
- Processed materials (witherite crystal, costmary leaves)
- Simple rarities (moonstone, sacred grove rainwater)

**Echelon 2** (Rare and specific):
- Specific monster parts (bovine essence, hag hair, algae from glacial water)
- Processed supernatural materials (sap from psionic-burned tree)
- Materials requiring specific conditions (breath captured at sunrise)
- Craftsman-specific items (gnome confectioner's chocolate)

**Echelon 3** (Extremely rare or dangerous):
- Major monster parts (voiceless talker bile, grub in bile)
- Sacrifice components (month's lifespan, ground sapphire)
- Negotiated components (signed agreement with ghost, expired infernal contract)
- Ancient materials (coven's used cauldron scrapings)

**Echelon 4** (Legendary/impossible without adventure):
- Divine components (breath of a god, blood of Saint Elspeth)
- Major sacrifice (year's lifespan)
- Epic quest items (archdevil's blood, sacred ink + blessed parchment + Infinite Library access)
- Unique artifacts (time crystal)

### Generation Guidelines
1. Match theme to treasure effect (fire → fire giant blood, teleport → time crystal)
2. Add narrative requirements for higher echelons (stolen, captured, signed agreement)
3. Consider who can obtain it (anyone vs. requires specific quest)
4. More powerful = more dangerous/costly to acquire

## Title Patterns

### Title Prerequisites by Echelon

**1st Echelon Titles:**
- Common accomplishments achievable in early adventures
- **Examples:** Defeat enemies without killing them, explore specific locations, complete minor quests
- **Pattern:** "You [accomplishment]" or "You [action] [target]"

**2nd Echelon Titles:**
- More significant accomplishments requiring multiple adventures
- **Examples:** Defeat major villains, complete long quests, earn renown in a region
- **Pattern:** "You [accomplishment] in [location/context]" or "You [action] [major target]"

**3rd Echelon Titles:**
- Legendary accomplishments that define a hero's career
- **Examples:** Defeat solo monsters, complete epic quests, earn widespread fame
- **Pattern:** "You [epic accomplishment]" or "You [action] [legendary target]"

**4th Echelon Titles:**
- World-changing accomplishments
- **Examples:** Save kingdoms, defeat world-ending threats, achieve immortality
- **Pattern:** "You [world-changing accomplishment]"

### Title Benefit Types

**Characteristic Bonuses:**
- Direct bonuses to characteristics (Might, Agility, Reason, Intuition, Presence)
- **Example:** "+1 to Might" or "Gain an edge on Might tests"

**New Abilities:**
- Main actions, maneuvers, or triggered actions
- May have Heroic Resource costs
- **Example:** "Come Out to Play" maneuver with 1 Heroic Resource

**Passive Effects:**
- Ongoing benefits while the title is held
- **Example:** "Gain +2 bonus to speed" or "Have cold immunity 5"

**Triggered Actions:**
- Reactive abilities activated by conditions
- **Example:** "When you take damage, you can use a triggered action to shift 2 squares"

**Skill Bonuses:**
- Edge or bonuses to specific skills
- **Example:** "Gain an edge on Intuition tests to read emotions"

### Group vs Individual Titles

**Group Titles:**
- Multiple heroes can earn the same title
- 3-4 benefit options, each hero chooses one
- **Examples:** Brawler, Angler, City Rat, Doom Slayer
- **Structure:** Use `advancements` with `itemGrant` type and `chooseN: 1`

**Individual Titles:**
- Only one hero can earn the title at a time
- Single benefit (no choice)
- Often tied to specific accomplishments or positions
- **Structure:** Direct benefit grant without choice pool

## Treasure Variation Pattern

**Structure:**
- **Base Item:** Simple version with lower project goal
- **Variants:** Enhanced versions with:
  - Higher project goal (usually +15)
  - Additional item prerequisite
  - Stronger/different effect

**Portable Cloud Template:**
- **Base** (PG 30): "rainwater from sacred fey grove" → fog cloud (no damage)
- **Noxious** (PG 45): +undead flesh → poison damage + weakened
- **Thunderhead** (PG 45): +copper wire → lightning damage + slowed

**When to Use Variants:**
- Item has simple base effect that can be enhanced
- Enhancements are thematic (fog → poison fog, fire → bigger fire)
- Each variant needs distinct identity (different damage + condition)
- Variants share name family ("X Cloud", "X Shot", "X Elixir")

**Design Guidance:**
- Base version: 30-45 project goal
- Variants: +15 to +30 project goal
- Each variant: +1 distinct prerequisite
- Effects should be parallel (all damage + condition, or all utility variations)

## Foundry VTT JSON Structure

### Effect System

**Effects Array Structure:**
- Each level (1st, 5th, 9th) of leveled treasure is a separate effect
- `type: "abilityModifier"` for damage bonuses and distance bonuses
- `type: "base"` for immunities, weaknesses, and passive effects
- `filters.keywords` allows targeting specific ability types (weapon, ranged, magic, etc.)
- `mode: 2` = additive, `mode: 4` = override/set value
- `disabled: true` by default (activated when worn/equipped)

**Damage Bonus Changes:**
- Keys: `damage.tier1.value`, `damage.tier2.value`, `damage.tier3.value`
- All three tiers get the same bonus value

**Immunity/Weakness Changes:**
- Keys: `system.damage.immunities.{type}` and `system.damage.weaknesses.{type}`
- Valid types: acid, cold, corruption, fire, holy, lightning, poison, psychic, sonic

### Duration Tracking

Effects with temporary duration use this structure:
```json
"duration": {
  "startTime": null,
  "combat": null,
  "seconds": null,
  "rounds": 1,
  "turns": null,
  "startRound": null,
  "startTurn": null
}
```
- `rounds`: duration in rounds
- `turns`: duration in turns
- Other fields track timing (null by default)

### Title Advancements

Titles use `itemGrant` type for benefit selection:
```json
"advancements": {
  "id": {
    "name": "Benefit",
    "type": "itemGrant",
    "pool": [{"uuid": "Compendium.draw-steel.rewards.Item.uuid"}],
    "chooseN": 1
  }
}
```

### Naming Conventions

**File Names:**
- Consumables: `treasure_{Name}_{ID}.json` (spaces → underscores)
- Variants: `treasure_{Base_Name}__{Variant_Name}_{ID}.json` (double underscore)
- Trinkets: `treasure_{Name}_{ID}.json`
- Leveled Treasures: `treasure_{Name}_{ID}.json`
- Titles: `title_{Name}_{ID}.json`
- Grants: `ability_{Name}_{ID}.json` or `feature_{Name}_{ID}.json`

**_dsid Values:**
- Use kebab-case of the name: `black-ash-dart`, `color-cloak-blue`
- Variants: `cloud-portable`, `cloud-noxious`

### Project Roll Characteristics

Use **lowercase** characteristic names:
- Single: `"reason"` or `["reason"]`
- Multiple: `["reason", "intuition"]`
- Valid: reason, intuition, agility, might, presence

### Yield Structure

```json
"yield": {
  "amount": "1d3",
  "display": ""
}
```
- `amount`: string values ("1", "1d3", "1d6 + 1")
- `display`: always empty string

## Example Treasure Stat Blocks

### Example 1: 1st Echelon Consumable

```
Black Ash Dart

A diamond-shaped dart holds a shimmering black vial at its core.

Keywords: Magic

Item Prerequisite: Three vials of black ash from the College of Black Ash
Project Source: Texts or lore in Szetch
Project Roll Characteristic: Agility or Intuition
Project Goal: 45 (yields 1d3 darts, or three darts if crafted by a shadow)

Effect: As a maneuver, you make a ranged free strike using a black ash dart. The strike deals an extra 1 damage and adds the following effects to the tier outcomes of the power roll:
- ≤11: You can teleport the target up to 2 squares.
- 12-16: You can teleport the target up to 4 squares.
- 17+: You can teleport the target up to 6 squares.
```

### Example 2: 1st Echelon Consumable with Variants

```
Portable Cloud

This thin glass sphere holds a tiny roiling cloud.

Keywords: Magic

Item Prerequisite: A cup of rainwater from a sacred fey grove, plus an optional prerequisite
Project Source: Texts or lore in Caelian
Project Roll Characteristic: Reason or Intuition
Project Goal: 30

Effect: As a maneuver, you throw this delicate glass sphere up to 5 squares, breaking it and creating a 4 cube of fog. The fog dissipates after 10 minutes or if a strong gust of wind created by a storm or magic passes through the area.

Enterprising mages within various thieves' guilds have developed variations of the Portable Cloud. Each variation has a secondary item prerequisite and a project goal of 45.

Noxious Cloud: Filled with a green or putrid yellow haze, this sphere spreads a choking, foul-smelling mist when broken. Each creature who enters the cloud for the first time in a combat round or starts their turn there takes 5 poison damage. Additionally, any creature is weakened while in the fog.

Item Prerequisite: An ounce of undead flesh.

Thunderhead Cloud: Small lightning bolts arc around the black cloud in this sphere, which creates a 3 cube of cloud and lightning when broken. Each creature who enters the cloud for the first time in a combat round or starts their turn there takes 5 lightning damage. Additionally, any creature is slowed while in the cloud.

Item Prerequisite: A spool of copper wire.
```

### Example 3: 1st Echelon Trinket with Trade-off

```
Color Cloak (Blue)

This silky-blue hooded cloak is emblazoned with a golden Anjali sigil meaning "ice."

Keywords: Magic, Neck

Item Prerequisite: A pint of blue ichor, soul chalk
Project Source: Licensing agreements in Anjali
Project Roll Characteristic: Reason or Intuition
Project Goal: 150

Effect: While worn, a blue Color Cloak grants you cold immunity equal to your level.

Additionally, when you are targeted by any effect that deals cold damage, you can use a triggered action to shift a number of squares equal to your level. If you do so, the cold immunity granted by the cloak becomes cold weakness with the same value until the end of the next round. You can't use this triggered action again until this weakness ends.
```

### Example 4: Leveled Treasure (Weapon)

```
Blade of Quintessence

This crystal blade houses a stormy vortex of fire, ice, and lightning.

Keywords: Magic, Medium Weapon

Item Prerequisite: A ruby hardened in the fires of the City of Brass, a sapphire that has been struck by lightning
Project Source: Texts or lore in Zaliac
Project Roll Characteristic: Might, Reason, or Intuition
Project Goal: 450

1st Level: Any weapon ability that deals rolled damage using this weapon gains a +1 damage bonus. Additionally, you can change the damage type of such abilities to cold, fire, lightning, or sonic.

5th Level: The weapon's damage bonus increases to +2. Additionally, the weapon can be used with ranged weapon abilities, and returns to you when a ranged ability is resolved. Ranged abilities used with the weapon increase their distance by 3, and must deal cold, fire, lightning, or sonic damage (chosen when you use the ability).

9th Level: The weapon's damage bonus increases to +3. Additionally, while you wield or carry the weapon, you have immunity 10 to cold, fire, lightning, and sonic damage.
```

### Example 5: Leveled Treasure (Armor)

```
Chain of the Sea and Sky

This set of heavy chain mail is created to allow free movement in extreme environments without sacrificing protection.

Keywords: Heavy Armor, Magic

Item Prerequisite: A set of wings from a flying carp, a set of chain mail rusted by seawater
Project Source: Texts or lore in Zaliac
Project Roll Characteristic: Might, Reason, or Intuition
Project Goal: 450

1st Level: While you wear this armor, you gain a +6 bonus to Stamina, you can automatically swim at full speed while moving, and you can breathe underwater for up to 1 hour. Returning to the surface to breathe air again for any length of time reset's the armor's water-breathing benefit.

5th Level: The armor's bonus to Stamina increases to +12, and you have cold immunity 5. Additionally, whenever you fall, you can extend your arms (no action required) to unfurl a thick membrane between your arms and your body, slowing your fall and allowing you to glide. While gliding this way, you move downward at 1 square per round, and you can glide up to 6 squares horizontally as a free maneuver once during each of your turns.

9th Level: The armor's bonus to Stamina increases to +21, and you have cold immunity 10. Additionally, whenever your feet are not touching the ground (including floating in water or being in midair), you gain an edge on ability rolls, and any ability takes a bane when targeting you.
```

### Example 6: Title

```
Brawler

We won't kill you. But you might wish we had.

Prerequisites: You triumph in battle without killing any of your foes.

Benefits (choose one):
- Duck!: When you take damage from a melee attack, you can use a triggered action to shift 2 squares.
- Furniture Fighter: You can wield improvised weapons (chairs, tables, etc.) as if they were light weapons.
- Headbutt: As a maneuver, you make a melee attack that deals extra 2 psychic damage and dazes the target.
- If I Wanted You Dead, You'd Be Dead: Whenever you reduce a creature to 0 Stamina without killing them, you can use a free action to shift 3 squares and make another attack.
```

## Foundry VTT Treasure Item Structure (CRITICAL)

### Required Fields

Every treasure item MUST have these fields:

| Field | Type | Valid Values |
|-------|------|--------------|
| `type` | string | `"treasure"` (NOT "equipment"!) |
| `system.kind` | string | `"other"`, `"armor"`, `"implement"`, `"weapon"` or `""` |
| `system.category` | string | `"consumable"`, `"trinket"`, `"leveled"`, `"artifact"` |
| `system.echelon` | integer | `1`, `2`, `3`, `4` |
| `system.keywords` | array | Must include `"magic"` or `"psionic"` |
| `system.quantity` | integer | Default `1` |
| `system.project` | object | See Project Structure below |

### Common Errors (NEVER USE)

```json
// ❌ WRONG - These will cause import errors:
{
  "type": "equipment",           // WRONG! Must be "treasure"
  "system": {
    "type": {"value": "implement"},  // WRONG! Use "kind": "implement"
    "equipmentSlot": {"value": "..."}, // WRONG! Not a valid field
    "damage": {"tier1": {...}},      // WRONG! Not a valid field
    "benefits": {...},               // WRONG! Not a valid field
    "level": {"value": 1}            // WRONG! Use "echelon": 1
  }
}

// ✓ CORRECT:
{
  "type": "treasure",
  "system": {
    "kind": "implement",
    "category": "leveled",
    "echelon": 1,
    "keywords": ["magic", "implement"],
    "quantity": 1,
    "project": {...}
  }
}
```

### Project Structure

```json
"project": {
  "prerequisites": "String describing materials needed",
  "source": "Region name (lowercase): caelian, anjali, khemharic, etc.",
  "rollCharacteristic": ["reason", "intuition"],
  "yield": {
    "amount": "1d3",
    "display": ""
  },
  "goal": 450
}
```

## Foundry JSON Schema Examples

### Example 1: Consumable (Black Ash Dart)

```json
{
  "folder": "rusZqMj7kWieXI2t",
  "name": "Black Ash Dart",
  "type": "treasure",
  "_id": "URT9F9h3X4fUTnbw",
  "img": "icons/weapons/ammunition/arrowhead-glowing-blue.webp",
  "system": {
    "description": {
      "value": "<p><em>A diamond-shaped dart holds a shimmering black vial at its core.</em></p><p><strong>Effect</strong>: As a maneuver, you make a ranged free strike using a black ash dart. The strike deals an extra 1 damage and adds the following effects to the tier outcomes of the power roll:</p><ul><li><strong>≤11:</strong> You can teleport the target up to 2 squares.</li><li><strong>12-16:</strong> You can teleport the target up to 4 squares.</li><li><strong>17+:</strong> You can teleport the target up to 6 squares.</li></ul>",
      "director": ""
    },
    "source": {
      "book": "Heroes",
      "page": "314",
      "license": "Draw Steel Creator License"
    },
    "_dsid": "black-ash-dart",
    "kind": "",
    "category": "consumable",
    "echelon": 1,
    "keywords": ["magic"],
    "quantity": 1,
    "project": {
      "prerequisites": "Three vials of black ash from the College of Black Ash",
      "source": "Texts or lore in Szetch",
      "rollCharacteristic": ["agility", "intuition"],
      "yield": {
        "amount": "1d3",
        "display": ""
      },
      "goal": 45
    }
  },
  "effects": [],
  "sort": 100000,
  "ownership": {"default": 0},
  "flags": {},
  "_stats": {
    "compendiumSource": null,
    "duplicateSource": null,
    "exportSource": null,
    "coreVersion": "13.348",
    "systemId": "draw-steel",
    "systemVersion": "0.8.1",
    "createdTime": 1757755174216,
    "modifiedTime": null,
    "lastModifiedBy": null
  },
  "_key": "!items!URT9F9h3X4fUTnbw"
}
```

### Example 2: Trinket with Effects (Color Cloak Blue)

```json
{
  "folder": "GbJ95cA5I5QZ4Sz5",
  "name": "Color Cloak (Blue)",
  "type": "treasure",
  "_id": "zIWGFr3n5qDmAR1t",
  "img": "icons/equipment/back/cape-layered-blue.webp",
  "system": {
    "description": {
      "value": "<p><em>This silky-blue hooded cloak is emblazoned with a golden Anjali sigil meaning \"ice.\"</em></p><p><strong>Effect:</strong> While worn, a blue Color Cloak grants you cold immunity equal to your level.</p><p>Additionally, when you are targeted by any effect that deals cold damage, you can use a triggered action to shift a number of squares equal to your level. If you do so, the cold immunity granted by the cloak becomes cold weakness with the same value until the end of the next round. You can't use this triggered action again until this weakness ends.</p>",
      "director": ""
    },
    "source": {
      "book": "Heroes",
      "page": "321",
      "license": "Draw Steel Creator License"
    },
    "_dsid": "color-cloak-blue",
    "kind": "",
    "category": "trinket",
    "echelon": 1,
    "keywords": ["magic", "neck"],
    "quantity": 1,
    "project": {
      "prerequisites": "A pint of blue ichor, soul chalk",
      "source": "Licensing agreements in Anjali",
      "rollCharacteristic": ["reason", "intuition"],
      "yield": {
        "amount": "1",
        "display": ""
      },
      "goal": 150
    }
  },
  "effects": [
    {
      "name": "Cold Immunity",
      "img": "icons/equipment/back/cape-layered-blue.webp",
      "type": "base",
      "origin": "Compendium.draw-steel.rewards.Item.zIWGFr3n5qDmAR1t",
      "_id": "gfVgPV1HVUECIQ90",
      "system": {
        "end": {
          "type": "",
          "roll": "1d10 + @combat.save.bonus"
        }
      },
      "changes": [
        {
          "key": "system.damage.immunities.cold",
          "mode": 2,
          "value": "1",
          "priority": null
        }
      ],
      "disabled": false,
      "duration": {
        "startTime": null,
        "combat": null,
        "seconds": null,
        "rounds": null,
        "turns": null,
        "startRound": null,
        "startTurn": null
      },
      "description": "<p>While worn, a blue Color Cloak grants you cold immunity equal to your level.</p>",
      "tint": "#ffffff",
      "transfer": true,
      "statuses": [],
      "sort": 0,
      "flags": {},
      "_stats": {
        "compendiumSource": null,
        "duplicateSource": null,
        "exportSource": null,
        "coreVersion": "13.348",
        "systemId": "draw-steel",
        "systemVersion": "0.8.1",
        "createdTime": 1757914155621,
        "modifiedTime": null,
        "lastModifiedBy": null
      },
      "_key": "!items.effects!zIWGFr3n5qDmAR1t.gfVgPV1HVUECIQ90"
    },
    {
      "name": "Cold Weakness",
      "img": "icons/equipment/back/cape-layered-blue.webp",
      "type": "base",
      "origin": "Compendium.draw-steel.rewards.Item.zIWGFr3n5qDmAR1t",
      "disabled": true,
      "_id": "JQzBbpEg27tg34dV",
      "system": {
        "end": {
          "type": "",
          "roll": "1d10 + @combat.save.bonus"
        }
      },
      "changes": [
        {
          "key": "system.damage.weaknesses.cold",
          "mode": 2,
          "value": "1",
          "priority": null
        }
      ],
      "duration": {
        "startTime": null,
        "combat": null,
        "seconds": null,
        "rounds": 1,
        "turns": null,
        "startRound": null,
        "startTurn": null
      },
      "description": "<p>The cold immunity granted by the cloak becomes cold weakness with the same value until the end of the next round</p>",
      "tint": "#ffffff",
      "transfer": true,
      "statuses": [],
      "sort": 0,
      "flags": {},
      "_stats": {
        "compendiumSource": null,
        "duplicateSource": null,
        "exportSource": null,
        "coreVersion": "13.348",
        "systemId": "draw-steel",
        "systemVersion": "0.9.0",
        "createdTime": 1757914189575,
        "modifiedTime": null,
        "lastModifiedBy": null
      },
      "_key": "!items.effects!zIWGFr3n5qDmAR1t.JQzBbpEg27tg34dV"
    }
  ],
  "sort": 100000,
  "ownership": {"default": 0},
  "flags": {},
  "_stats": {
    "compendiumSource": null,
    "duplicateSource": null,
    "exportSource": null,
    "coreVersion": "13.348",
    "systemId": "draw-steel",
    "systemVersion": "0.9.0",
    "createdTime": 1757757078946,
    "modifiedTime": null,
    "lastModifiedBy": null
  },
  "_key": "!items!zIWGFr3n5qDmAR1t"
}
```

### Example 3: Leveled Treasure (Blade of Quintessence)

```json
{
  "name": "Blade of Quintessence",
  "type": "treasure",
  "img": "icons/weapons/swords/sword-flanged-lightning.webp",
  "folder": "78VTHX5tnOWffNOa",
  "effects": [
    {
      "name": "Blade of Quintessence (1st level)",
      "type": "abilityModifier",
      "origin": "Compendium.draw-steel.rewards.Item.HNa2e8SpegGkw6jm",
      "_id": "Gnsu1r6Co0bNTN4s",
      "system": {
        "end": {"type": "", "roll": "1d10 + @combat.save.bonus"},
        "filters": {"keywords": ["weapon"]}
      },
      "changes": [
        {"key": "damage.tier1.value", "mode": 2, "value": "1"},
        {"key": "damage.tier2.value", "mode": 2, "value": "1"},
        {"key": "damage.tier3.value", "mode": 2, "value": "1"}
      ],
      "disabled": true,
      "duration": {"startTime": null, "combat": null, "seconds": null, "rounds": null, "turns": null, "startRound": null, "startTurn": null},
      "description": "",
      "tint": "#ffffff",
      "transfer": true,
      "statuses": [],
      "sort": 0,
      "flags": {},
      "_key": "!items.effects!HNa2e8SpegGkw6jm.Gnsu1r6Co0bNTN4s"
    },
    {
      "name": "Blade of Quintessence (5th level)",
      "type": "abilityModifier",
      "origin": "Compendium.draw-steel.rewards.Item.HNa2e8SpegGkw6jm",
      "_id": "iOq0uDUCwLeC5r9f",
      "system": {
        "end": {"type": "", "roll": "1d10 + @combat.save.bonus"},
        "filters": {"keywords": ["weapon"]}
      },
      "changes": [
        {"key": "damage.tier1.value", "mode": 2, "value": "2"},
        {"key": "damage.tier2.value", "mode": 2, "value": "2"},
        {"key": "damage.tier3.value", "mode": 2, "value": "2"}
      ],
      "disabled": true,
      "duration": {"startTime": null, "combat": null, "seconds": null, "rounds": null, "turns": null, "startRound": null, "startTurn": null},
      "description": "",
      "tint": "#ffffff",
      "transfer": true,
      "statuses": [],
      "sort": 0,
      "flags": {},
      "_key": "!items.effects!HNa2e8SpegGkw6jm.iOq0uDUCwLeC5r9f"
    },
    {
      "name": "Blade of Quintessence (9th level)",
      "type": "abilityModifier",
      "origin": "Compendium.draw-steel.rewards.Item.HNa2e8SpegGkw6jm",
      "_id": "cK2EhVgiEE5qr82q",
      "system": {
        "end": {"type": "", "roll": "1d10 + @combat.save.bonus"},
        "filters": {"keywords": ["weapon"]}
      },
      "changes": [
        {"key": "damage.tier1.value", "mode": 2, "value": "3"},
        {"key": "damage.tier2.value", "mode": 2, "value": "3"},
        {"key": "damage.tier3.value", "mode": 2, "value": "3"}
      ],
      "disabled": true,
      "duration": {"startTime": null, "combat": null, "seconds": null, "rounds": null, "turns": null, "startRound": null, "startTurn": null},
      "description": "",
      "tint": "#ffffff",
      "transfer": true,
      "statuses": [],
      "sort": 200000,
      "flags": {},
      "_key": "!items.effects!HNa2e8SpegGkw6jm.cK2EhVgiEE5qr82q"
    },
    {
      "name": "Blade of Quintessence (9th level)(Immunities)",
      "type": "base",
      "origin": "Compendium.draw-steel.rewards.Item.HNa2e8SpegGkw6jm",
      "_id": "3HSYQpwAEWpso0yA",
      "system": {"end": {"type": "", "roll": "1d10 + @combat.save.bonus"}},
      "changes": [
        {"key": "system.damage.immunities.cold", "mode": 4, "value": "10"},
        {"key": "system.damage.immunities.fire", "mode": 4, "value": "10"},
        {"key": "system.damage.immunities.lightning", "mode": 4, "value": "10"},
        {"key": "system.damage.immunities.sonic", "mode": 4, "value": "10"}
      ],
      "disabled": true,
      "duration": {"startTime": null, "combat": null, "seconds": null, "rounds": null, "turns": null, "startRound": null, "startTurn": null},
      "description": "",
      "tint": "#ffffff",
      "transfer": true,
      "statuses": [],
      "sort": 300000,
      "flags": {},
      "_key": "!items.effects!HNa2e8SpegGkw6jm.3HSYQpwAEWpso0yA"
    }
  ],
  "flags": {},
  "system": {
    "description": {
      "value": "<p><em>This crystal blade houses a stormy vortex of fire, ice, and lightning.</em></p><p><strong>1st Level:</strong> Any weapon ability that deals rolled damage using this weapon gains a +1 damage bonus. Additionally, you can change the damage type of such abilities to cold, fire, lightning, or sonic.</p><p><strong>5th Level:</strong> The weapon's damage bonus increases to +2. Additionally, the weapon can be used with ranged weapon abilities, and returns to you when a ranged ability is resolved. Ranged abilities used with the weapon increase their distance by 3, and must deal cold, fire, lightning, or sonic damage (chosen when you use the ability).</p><p><strong>9th Level:</strong> The weapon's damage bonus increases to +3. Additionally, while you wield or carry the weapon, you have immunity 10 to cold, fire, lightning, and sonic damage.</p>",
      "director": ""
    },
    "source": {
      "book": "Heroes",
      "page": "331",
      "license": "Draw Steel Creator License"
    },
    "_dsid": "treasure",
    "kind": "weapon",
    "category": "leveled",
    "echelon": 1,
    "keywords": ["magic", "medium"],
    "quantity": 1,
    "project": {
      "prerequisites": "A ruby hardened in the fires of the City of Brass, a sapphire that has been struck by lightning",
      "source": "Texts or lore in Zaliac",
      "rollCharacteristic": ["might", "reason", "intuition"],
      "yield": {"amount": "1", "display": ""},
      "goal": 450
    }
  },
  "_id": "HNa2e8SpegGkw6jm",
  "sort": 100000,
  "ownership": {"default": 0},
  "flags": {},
  "_stats": {
    "compendiumSource": null,
    "duplicateSource": null,
    "exportSource": null,
    "coreVersion": "13.351",
    "systemId": "draw-steel",
    "systemVersion": "0.10.0",
    "createdTime": 1763173316034,
    "modifiedTime": null,
    "lastModifiedBy": null
  },
  "_key": "!items!HNa2e8SpegGkw6jm"
}
```

### Example 4: Title (Brawler)

```json
{
  "folder": "M0xNtYu0IzR83TAL",
  "name": "Brawler",
  "type": "title",
  "_id": "kkJlb2w4CM8mH40V",
  "img": "icons/skills/melee/unarmed-punch-fist-yellow-red.webp",
  "system": {
    "description": {
      "value": "<p><strong>Effect:</strong> Choose one of the following benefits:</p><ul><li><p><em>Duck!:</em> @Embed[Compendium.draw-steel.rewards.Item.zCgGKvBdCeOKONOu inline]</p></li><li><p><em>Furniture Fighter:</em> @Embed[Compendium.draw-steel.rewards.Item.tt6PRlfJ8cuVGLej inline]</p></li><li><p><em>Headbutt:</em> @Embed[Compendium.draw-steel.rewards.Item.YXIFafFxOPENQdht inline]</p></li><li><p><em>If I Wanted You Dead, You'd Be Dead:</em> @Embed[Compendium.draw-steel.rewards.Item.Sfd4wPykoAxF4bT0 inline]</p></li></ul>",
      "director": ""
    },
    "source": {
      "book": "Heroes",
      "page": "339",
      "license": "Draw Steel Creator License"
    },
    "_dsid": "brawler",
    "advancements": {
      "94u8mVYTuK09aEu6": {
        "name": "Benefit",
        "img": null,
        "type": "itemGrant",
        "requirements": {"level": null},
        "_id": "94u8mVYTuK09aEu6",
        "description": "<p>Choose one of the following benefits:</p>",
        "pool": [
          {"uuid": "Compendium.draw-steel.rewards.Item.zCgGKvBdCeOKONOu"},
          {"uuid": "Compendium.draw-steel.rewards.Item.tt6PRlfJ8cuVGLej"},
          {"uuid": "Compendium.draw-steel.rewards.Item.YXIFafFxOPENQdht"},
          {"uuid": "Compendium.draw-steel.rewards.Item.Sfd4wPykoAxF4bT0"}
        ],
        "chooseN": 1
      }
    },
    "echelon": 1,
    "story": "We won't kill you. But you might wish we had.",
    "prerequisites": {
      "value": "You triumph in battle without killing any of your foes."
    }
  },
  "effects": [],
  "sort": 0,
  "ownership": {"default": 0},
  "flags": {},
  "_stats": {
    "compendiumSource": null,
    "duplicateSource": null,
    "exportSource": null,
    "coreVersion": "13.348",
    "systemId": "draw-steel",
    "systemVersion": "0.8.1",
    "createdTime": 1757642472344,
    "modifiedTime": null,
    "lastModifiedBy": null
  },
  "_key": "!items!kkJlb2w4CM8mH40V"
}
```

## Validation Script

Run before outputting with `--format foundry` or `--format both`:

```bash
python .claude/skills/draw-steel-reward-generator/scripts/validate_reward.py output/filename.json
```

**Output interpretation:**
- **PASSED (✓):** All checks successful
- **ERRORS (❌):** Critical issues - fix before importing
- **WARNINGS (⚠️):** Minor issues - review but acceptable

This is MANDATORY - never skip validation.

## Self-Validation Checklist

### All Rewards
- [ ] Item type is valid ("treasure" or "title")
- [ ] All `_id` match `^[a-zA-Z0-9]{16}$` (16 chars)
- [ ] No duplicate `_id` values within the same reward
- [ ] Keywords are lowercase
- [ ] Magic or Psionic keyword present (for treasures)
- [ ] Project roll characteristics are lowercase strings or arrays
- [ ] **NO dice notation** (d4, d8, d12, d20) - use fixed values only (e.g., "6" not "1d6")
- [ ] **NO DC values** - use potencies or "save ends" (e.g., "A < 2" not "DC 13")
- [ ] **NO direct characteristic bonuses in consumables** - use edges (e.g., "edge on Intuition tests" not "+2 to Intuition")

### Power Rolls and Tiered Outcomes (if used)
- [ ] Tiered outcomes use correct format (≤11, 12-16, 17+)
- [ ] Effects scale appropriately by tier (small → medium → large)
- [ ] Potencies use characteristic comparisons (A < 2, M < 2, etc.)
- [ ] "save ends" used correctly (not "DC X")
- [ ] Power roll characteristics match ability type being enhanced
- [ ] NO D&D terminology: "DC", "saving throw", "save DC"
- [ ] Fixed values used for damage (not dice notation in tiered outcomes)
- [ ] Conditions use correct format: "condition (save ends)" or "condition until the end of your next turn"
- [ ] **NEVER use "until healed"** - NOT used in Draw Steel

### Consumables
- [ ] Category is "consumable"
- [ ] Echelon is 1-4
- [ ] Project goal matches echelon pattern (30/45, 90, 120/180, 360)
- [ ] Effect uses proper format ("As a maneuver, you...")
- [ ] **ALL damage/stamina values are fixed** (e.g., "6" not "1d6")
- [ ] Yield included if item produces multiple (yield field uses dice notation, which is allowed)

### Trinkets
- [ ] Category is "trinket"
- [ ] Echelon is 1-4
- [ ] Project goal is 150 × echelon (150, 300, 450, 600)
- [ ] Body keyword present (Arms, Feet, Hands, Head, Neck, Waist, Ring)
- [ ] Effect uses "While worn, [passive effect]" format

### Leveled Treasures
- [ ] Category is "leveled"
- [ ] Echelon is 1-4
- [ ] Project goal is 450
- [ ] Equipment keyword present (weapon, armor categories, implement types)
- [ ] Scaling follows published patterns (damage: +1/+2/+3, stamina: +6/+12/+21)
- [ ] Effects array has separate effects for 1st, 5th, 9th level

### Titles
- [ ] Item type is "title"
- [ ] Echelon is 1-4
- [ ] Prerequisites are clear and measurable
- [ ] Story is 1-2 sentences, flavorful
- [ ] Advancements structure is correct (itemGrant type)
- [ ] Pool has 3-4 UUIDs (group titles) or 1 UUID (individual titles)

### Foundry JSON
- [ ] `_stats.systemId` is "draw-steel"
- [ ] `_dsid` is kebab-case
- [ ] Project source is valid region
- [ ] Yield structure is correct (amount string, display empty)
- [ ] Effects use valid types (abilityModifier, base)
- [ ] Duration fields are properly structured

## Using Examples as Inspiration

**CRITICAL:** Examples are templates only - create unique rewards for each request.

- ✅ **DO:** Create "Flamestrike Potion" with unique mechanics
- ❌ **DON'T:** Copy "Healing Potion" and rename to "Cure Potion"

Every reward should be distinct and thematic.

## Create Unique Rewards

**CRITICAL:** Each reward should be unique and thematic. It is **more important to follow Draw Steel rules** than to create a perfect recreation of an item from another system.

**✅ DO:**
- Create rewards that fit the theme and concept
- Use Draw Steel patterns and formulas (project goals, scaling, keywords)
- Invent new names and effects
- Consider the reward's type and echelon
- Make rewards that tell a story
- **Follow Draw Steel terminology** even if it differs from other systems
- **Prioritize correctness over perfect recreation** - a Draw Steel-compliant item is better than a perfect copy that breaks the rules

**❌ DO NOT:**
- Copy rewards from examples
- Use generic names ("Magic Ring", "Fire Potion")
- Copy mechanics from published content
- Make every reward feel the same
- **Use D&D/PF2e terminology** (HP, DC, STR/DEX/CON/WIS/CHA, saving throws, etc.)
- **Try to recreate items perfectly** if it means breaking Draw Steel rules

### Example: Converting a D&D Item

**Source:** D&D 5e "Potion of Healing" (restores 2d4+2 HP)

**WRONG Approach (Perfect Recreation):**
- "Healing Potion that restores 2d4+2 stamina"
- Uses D&D dice notation (2d4+2)
- Doesn't follow Draw Steel patterns

**RIGHT Approach (Draw Steel-Compliant):**
- "Vitality Tonic - As a maneuver, you drink this tonic to gain 10 stamina and remove the weakened condition"
- Uses Draw Steel mechanics (maneuver action, fixed stamina value, Draw Steel condition)
- Follows project goal pattern (45 for 1st echelon consumable)
- Uses proper keywords (Magic, Potion)

**Key Difference:** The RIGHT approach creates a unique reward that **follows Draw Steel rules** rather than trying to perfectly recreate the D&D item. The theme is preserved (healing potion), but the mechanics are Draw Steel-compliant.

### Why Following Draw Steel Rules Is More Important

1. **System Integrity:** Draw Steel has its own balance and mechanics. Using D&D terms breaks the system.
2. **Playability:** Players familiar with Draw Steel will be confused by mixed terminology.
3. **Validation:** Items with D&D terminology will fail validation checks.
4. **Import Issues:** Foundry VTT will crash or have issues with invalid damage types/conditions.
5. **Design Intent:** Draw Steel is designed with specific patterns - breaking them creates inconsistent rewards.

**If you must choose between:**
- ✅ **Follow Draw Steel rules** (even if the item isn't a perfect match)
- ❌ **Perfect recreation** (that breaks Draw Steel rules)

**Always choose the first option.**

## Common D&D Terminology Mistakes

These are the most common errors when creating rewards from D&D/PF2e sources. **Avoid these at all costs.**

### Damage Type Mistakes

| D&D Term | Draw Steel Term | Why It's Wrong |
|----------|-----------------|---------------|
| "deals 1d6+3 fire damage" | "deals 6 fire damage" | D&D dice notation, use fixed values |
| "necrotic damage" | "corruption damage" | Invalid damage type |
| "radiant damage" | "holy damage" | Invalid damage type |
| "thunder damage" | "sonic damage" | Invalid damage type |
| "force damage" | psychic or untyped | Invalid damage type |
| "bludgeoning/slashing/piercing" | untyped or use effect | Invalid damage types |

### DC and Saving Throw Mistakes (CRITICAL!)

**Draw Steel NEVER uses DC (Difficulty Class) or "saving throws" in the D&D sense.**

| D&D Term | Draw Steel Term | Why It's Wrong |
|----------|-----------------|---------------|
| "DC 10" | "save ends" (no potency) | DC is D&D terminology |
| "DC 13" | "A/R/M/P < 1" (weak potency) | DC is D&D terminology |
| "DC 15" | "A/R/M/P < 2" (average potency) | DC is D&D terminology |
| "DC 18" | "A/R/M/P" (strong potency) | DC is D&D terminology |
| "DC 20" | "A/R/M/P + 1" (very strong potency) | DC is D&D terminology |
| "DC 15 Constitution save" | "M < 2" or "save ends" | Wrong system |
| "Dexterity save" | "Agility save" or "power roll with Agility" | Wrong terminology |
| "saving throw" | "save" | Use "save" not "saving throw" |
| "save DC" | "save" or "potency" | DC not used in Draw Steel |

**How to Convert D&D DCs:**

| D&D DC | Draw Steel Equivalent | Example |
|---------|---------------------|---------|
| DC 10-12 | "save ends" (no potency) | Easy effects that end on successful save |
| DC 13-14 | "A/R/M/P < 1" (weak potency) | "slowed (A < 1)" - Agility less than 1 |
| DC 15-16 | "A/R/M/P < 2" (average potency) | "dazed (M < 2)" - Might less than 2 |
| DC 17-18 | "A/R/M/P" (strong potency) | "weakened (R)" - Reason characteristic |
| DC 19-20+ | "A/R/M/P + 1" (very strong) | "frightened (P + 1)" - Presence + 1 |

**Potency Formulas:**
- **Weak:** Characteristic - 2 (e.g., A < 1, M < 2)
- **Average:** Characteristic - 1 (e.g., A < 2, M < 3)
- **Strong:** Characteristic (e.g., A, M, R, P)
- **Very Strong:** Characteristic + 1 (e.g., P + 1)

**Save Ends vs. Potency:**

| When to Use | Example |
|-------------|---------|
| **"save ends"** | Condition ends when target makes successful save each turn |
| **"A < 2"** | Potency check against Agility characteristic |
| **"M < 2"** | Potency check against Might characteristic |
| **"R < 1"** | Potency check against Reason characteristic |
| **"P < 1"** | Potency check against Presence characteristic |

**Example Conversion:**

**D&D 5e:**
> "Target makes a DC 15 Constitution saving throw or be slowed."

**WRONG Draw Steel:**
> "Target makes a DC 15 Might save or is slowed."

**CORRECT Draw Steel (Option 1):**
> "Target is slowed (M < 2)."

**CORRECT Draw Steel (Option 2):**
> "Target is slowed (save ends)."

**Examples:**

| D&D Term | Draw Steel Conversion | Why |
|----------|----------------------|-----|
| "DC 13 Dexterity save" | "slowed (A < 1)" | Potency weak against Agility |
| "DC 15 Wisdom save" | "taunted (I < 2)" | Potency average against Intuition |
| "DC 18 Strength save" | "grabbed (M)" | Potency strong against Might |
| "DC 20 Charisma save" | "frightened (P + 1)" | Potency very strong against Presence |

**Validation will fail if DC or "saving throw" is detected.**

### Characteristic Bonus Mistakes (CRITICAL!)

**Draw Steel consumables use EDGES, not direct characteristic bonuses.**

| D&D Term | Draw Steel Term | Why It's Wrong |
|----------|-----------------|---------------|
| "+1 to Wisdom" | "edge on Intuition tests" | Direct characteristic bonus not used in consumables |
| "+2 to Dexterity" | "edge on Agility tests" | Direct characteristic bonus not used in consumables |
| "+3 to Constitution" | "edge on Might tests" | Direct characteristic bonus not used in consumables |
| "+1d4 to a characteristic" | "edge on [characteristic] tests" | D&D dice notation + wrong pattern |
| "characteristic bonus +2" | "edge on [characteristic] tests" | Not Draw Steel terminology |
| "+1d4 bonus to Wisdom checks" | "edge on Intuition tests" | D&D dice notation + wrong terminology |

**Why Direct Characteristic Bonuses Are Wrong:**

**Consumables:**
- ✅ **USE:** "gain an edge on Intuition tests" or "gain a double edge on Might tests"
- ❌ **DON'T:** "gain +2 to Intuition" or "gain +3 to Might"
- ❌ **DON'T:** "characteristic bonus +2"

**Leveled Treasures (ONLY):**
- Direct characteristic increases are VERY rare
- Most use damage bonuses (+1/+2/+3) or stamina bonuses (+6/+12/+21)

**Scaling Patterns:**

**Consumable Scaling:**
- **Echelon 1:** Single edge
- **Echelon 2:** Single edge with additional effect
- **Echelon 3:** Double edge
- **Echelon 4:** Double edge with additional effect

**Leveled Treasure Scaling:**
- **1st Level:** +1 damage bonus or +6 Stamina
- **5th Level:** +2 damage bonus or +12 Stamina
- **9th Level:** +3 damage bonus or +21 Stamina

**Correct Examples from Published Content:**
- Growth Potion: "gain an edge on Might tests"
- Stygian Liquor: "gain on edge on power rolls"
- Most buff consumables: "gain an edge on [characteristic] tests"

**Incorrect Examples (What the LLM Created):**
- "gain +2 to Intuition" - NOT Draw Steel pattern
- "gain +3 to Intuition" - NOT Draw Steel pattern
- "gain +4 to Intuition" - NOT Draw Steel pattern

**How to Convert D&D Characteristic Bonuses:**

| D&D Term | Draw Steel Equivalent | Example |
|----------|----------------------|---------|
| "+1 to Wisdom" | "edge on Intuition tests" | Wisdom → Intuition |
| "+2 to Dexterity" | "edge on Agility tests" | Dexterity → Agility |
| "+3 to Constitution" | "edge on Might tests" | Constitution → Might |
| "+1 to Charisma" | "edge on Presence tests" | Charisma → Presence |
| "+1d4 to Intelligence" | "edge on Reason tests" | No dice, use edge |
| "+1d6 bonus to Wisdom checks" | "edge on Intuition tests" | No dice, use edge |

**Example Conversion:**

**D&D 5e Potion of Insight:**
> "When you drink this potion, you gain a +1d4 bonus to Wisdom saving throws and Wisdom (Perception) checks for 1 hour."

**WRONG Draw Steel:**
> "gain +2 to Intuition for 1 hour"

**CORRECT Draw Steel:**
> "gain an edge on Intuition tests until the end of your next turn"

**Key Differences:**
- No +X to characteristic - use edge instead
- No "saving throws" - use tests
- No "1 hour" - use encounter-based duration
- Edge is more flexible and tactical

**Validation will fail if direct characteristic bonuses are detected in consumables.**

### Dice Notation Mistakes (CRITICAL!)

**Draw Steel NEVER uses dice notation for damage, healing, or effects.** Calculate values using Draw Steel patterns, not by converting D&D dice.

| ❌ D&D Term (NEVER USE) | Why It's Wrong |
|------------------------|----------------|
| "2d4+2 hit points" | D&D dice notation - use fixed values from Draw Steel formulas |
| "1d6 fire damage" | D&D dice notation - use fixed values from Draw Steel formulas |
| "1d8 lightning damage" | D&D dice notation - use fixed values from Draw Steel formulas |
| "2d6 poison damage" | D&D dice notation - use fixed values from Draw Steel formulas |
| "gain 1d4+1 temporary HP" | D&D dice notation - use fixed values from Draw Steel formulas |
| "roll 2d10 for effect" | D&D dice notation - use fixed values from Draw Steel formulas |
| "1d4 rounds" | D&D dice notation - use fixed values from Draw Steel formulas |

**Prohibited Dice Types:**
- `d4` - NEVER use
- `d8` - NEVER use
- `d12` - NEVER use
- `d20` - NEVER use

**Validation will fail if any of these dice types are detected.**

### Characteristic Mistakes

| D&D Term | Draw Steel Term | Why It's Wrong |
|----------|-----------------|---------------|
| "Strength check" | "Might test" | Wrong characteristic name |
| "Dexterity save" | "Agility save" or "power roll with Agility" | Wrong terminology |
| "Intelligence check" | "Reason test" | Wrong characteristic name |
| "Wisdom save" | "Intuition save" or "power roll with Intuition" | Wrong characteristic name |
| "Charisma check" | "Presence test" | Wrong characteristic name |
| "+2 to DEX" | "+2 to Agility" | Wrong characteristic name |

### Condition Mistakes

| D&D Term | Draw Steel Term | Why It's Wrong |
|----------|-----------------|---------------|
| "poisoned" | "weakened" or "poison damage" | Invalid condition |
| "paralyzed" | "dazed" or "grabbed" | Invalid condition |
| "stunned" | "dazed" | Invalid condition |
| "blinded" | "dazed" or use effect description | Invalid condition |
| "charmed" | "taunted" or use effect description | Invalid condition |
| "frightened" | "frightened" | Valid! ✓ |
| "grappled" | "grabbed" | Valid! ✓ |
| "restrained" | "restrained" | Valid! ✓ |
| "prone" | "prone" | Valid! ✓ |
| "incapacitated" | "dazed" or use effect description | Invalid condition |
| "exhaustion" | "weakened" or "slowed" | Invalid condition |

### Mechanic Mistakes

| D&D Term | Draw Steel Term | Why It's Wrong |
|----------|-----------------|---------------|
| "as a bonus action" | "as a maneuver" | Wrong action type |
| "as a reaction" | "as a triggered action" | Wrong action type |
| "DC 15 Constitution save" | "potency weak (Might - 2)" | Wrong mechanic |
| "regains 2d8+4 hit points" | "gains 11 stamina" | D&D dice notation |
| "lasts for 1 minute" | "lasts for 10 rounds" | Use rounds, not minutes |
| "once per short rest" | "once per respite" | Wrong terminology |
| "requires attunement" | - | Not used in Draw Steel |
| "charges: 3" | "quantity: 3" or describe in effect | Wrong terminology |
| "spell slot" | - | Not used in Draw Steel |
| "concentration" | - | Not used in Draw Steel |
| "AC +2" | "edge on defense" or describe effect | Wrong mechanic |

### Item Property Mistakes

| D&D Term | Draw Steel Term | Why It's Wrong |
|----------|-----------------|---------------|
| "rarity: uncommon" | "echelon: 1" | Use echelons, not rarity |
| "requires attunement by a cleric" | - | Not used in Draw Steel |
| "weapon (longsword), melee" | "medium weapon, melee keyword" | Proper formatting |
| "armor class 15" | - | Not used in Draw Steel |
| "saving throw +3" | "save bonus +3" | Wrong terminology |
| "speed 30 ft." | "speed 6" | Use squares, not feet |
| "range 60 ft." | "distance 12" | Use squares, not feet |
| "duration: 1 hour" | "duration: 10 rounds" or "1 hour" | Context-dependent |

### Example: Correcting D&D Terminology

**Original D&D 5e Item:**
> "Potion of Giant Strength: When you drink this potion, your Strength score becomes 25 for 1 hour. The potion has no effect if your Strength is already equal to or greater than that score."

**WRONG Draw Steel Conversion:**
> "Strength Potion: When you drink this potion, your Strength becomes 25 for 1 hour. This has no effect if your Strength is already 25 or higher."
> - Uses D&D characteristic name ("Strength")
> - Uses D&D duration format ("1 hour")
- Uses D&D mechanic (ability score becomes 25)

**CORRECT Draw Steel Reward:**
> "Titan's Tonic: As a maneuver, you drink this tonic to gain +3 to Might and an edge on Might tests until the end of your next turn. Additionally, you gain immunity 5 to being grabbed or restrained for the same duration."
> - Uses Draw Steel characteristic ("Might")
> - Uses Draw Steel action type ("maneuver")
> - Uses Draw Steel mechanics (+3 bonus, edge, immunity)
> - Uses Draw Steel conditions (grabbed, restrained)
- Uses Draw Steel duration format ("end of your next turn")

**Key Differences:**
- "Strength" → "Might"
- "becomes 25" → "+3 to Might" (Draw Steel uses bonuses, not fixed scores)
- "1 hour" → "end of your next turn" (more tactical duration)
- Added flavor with immunity and edge bonuses
- Uses proper Draw Steel mechanics throughout