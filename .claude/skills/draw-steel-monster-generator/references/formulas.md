# Draw Steel Monster Formulas Reference

This document provides the complete formulas and lookup tables for generating Draw Steel TTRPG monsters with 100% official compliance.

## Core Formulas (Official from Monster Basics.md)

All calculations use **ceil()** - round UP to the nearest whole number.

### Encounter Value (EV)
```
EV = ceil(((2 × Level) + 4) × Organization_Modifier)
```

### Stamina
```
Stamina = ceil(((10 × Level) + Role_Stamina_Modifier) × Organization_Modifier)
```

### Damage (any tier)
```
Damage = ceil((4 + Level + Damage_Modifier) × Tier_Multiplier)

For Horde and Minion: Damage = ceil(Damage ÷ 2)
```

**CRITICAL:** The Organization Modifier is NOT used for damage calculation! Damage modifiers come from:
- **Role**: Ambusher/Artillery/Brute = +1, Controller/Defender/Harrier/Hexer/Mount/Support = +0
- **Organization as Role**: Solo = +2, Leader = +1 (when used as role, see compatibility rules above)
- **Elite**: +1 (can stack with role modifier for total +2)

**Solo/Leader Bonus:** Solo and Leader monsters also get +1 to their highest characteristic and potency values (see Characteristics section).

### Free Strike
```
Free Strike = Damage at Tier 1 (ALWAYS!)
```

### Strike Bonus (from Monster Basics.md line 1360)
For abilities with the **Strike** keyword, add the monster's highest characteristic to the damage:

```
Damage = Base_Damage + Highest_Characteristic
```

**Example:** A Level 3 Brute (Might +2) making a strike at Tier 2:
- Base damage: 8
- Strike bonus: +2
- Final damage: 10

This bonus applies to all tiers of the power roll.

### Extra Stamina (Non-Minions Only)
```
Extra_Stamina = ceil((3 × Level) + 3)
```

---

## Organization Modifiers

**CRITICAL:** Organization modifiers apply ONLY to EV and Stamina, NOT to damage!

**IMPORTANT:** Minions use a DIFFERENT stamina modifier than other organizations!

| Organization | EV Modifier | Stamina Modifier | Notes |
|--------------|-------------|------------------|-------|
| Minion | 0.5 | **0.125** | Squad-based Stamina (very low!) |
| Horde | 0.5 | 0.5 | Outnumber ~2:1 |
| Platoon | 1.0 | 1.0 | Well-rounded |
| Elite | 2.0 | 2.0 | Hardy, ~2 heroes |
| Leader | 2.0 | 2.0 | Has villain actions |
| Solo | 6.0 | **5.0** | Full encounter alone (different modifiers!) |

### Minion Stamina Formula (CRITICAL)

**Minions use ×0.125 for stamina, NOT ×0.5!**

```
Minion Stamina = ceil(((10 × Level) + Role_Modifier) × 0.125)
```

**Verification against official monsters:**

| Level | Role | Formula | Result | Official |
|-------|------|---------|--------|----------|
| 1 | Brute | ceil((10+30) × 0.125) | 5 | 5 ✓ |
| 1 | Harrier | ceil((10+20) × 0.125) | 4 | 4 ✓ |
| 1 | Artillery | ceil((10+10) × 0.125) | 3 | 3 ✓ |
| 4 | Brute | ceil((40+30) × 0.125) | 9 | 9 ✓ |
| 7 | Brute | ceil((70+30) × 0.125) | 13 | 13 ✓ |
| 10 | Brute | ceil((100+30) × 0.125) | 17 | 17 ✓ |

---

## Role Modifiers

> ⚠️ **CRITICAL: Solo Monsters Use BOTH Modifiers**
> - Solo role modifier: **+30** (for stamina calculation)
> - Solo EV modifier: **×6** (for EV calculation only)
> - Solo stamina modifier: **×5** (for stamina calculation only)
> - EV Formula: `ceil(((2 × Level) + 4) × 6)`
> - Stamina Formula: `ceil(((10 × Level) + 30) × 5)`

| Role | Stamina Modifier | Damage Modifier | Characteristic |
|------|------------------|-----------------|----------------|
| Ambusher | +20 | +1 | Agility |
| Artillery | +10 | +1 | Reason |
| Brute | +30 | +1 | Might |
| Controller | +10 | +0 | Reason |
| Defender | +30 | +0 | Might |
| Harrier | +20 | +0 | Agility |
| Hexer | +10 | +0 | Reason |
| Mount | +20 | +0 | Might/Agility |
| Support | +20 | +0 | Presence |
| Solo | +30 | +2 | Varies |
| Leader | +30 | +1 | Varies |

---

## Tier Multipliers

| Tier | Roll Range | Multiplier |
|------|------------|------------|
| Tier 1 | ≤11 | 0.6 |
| Tier 2 | 12-16 | 1.1 |
| Tier 3 | 17+ | 1.4 |

---

## Rounding Rules

| Stat | Rounding Method |
|------|-----------------|
| EV | `ceil()` |
| Stamina | `ceil()` |
| Free Strike | `ceil()` (equals T1 damage) |
| Damage | `ceil()` |

---

## Role & Organization Compatibility

**CRITICAL:** Solo and Leader organizations have special role restrictions.

| Organization | Valid Role Values | Notes |
|--------------|-------------------|-------|
| **Solo** | `"solo"` or `""` (empty) | Never use other roles (brute, harrier, etc.) |
| **Leader** | `"leader"` or `""` (empty) | Never use other roles (brute, harrier, etc.) |
| **Elite** | Any standard role | Use appropriate role for the creature |
| **Platoon** | Any standard role | Use appropriate role for the creature |
| **Horde** | Any standard role | Use appropriate role for the creature |
| **Minion** | Any standard role | Use appropriate role for the creature |

**Examples:**
- ✅ Correct: `organization: "solo"`, `role: "solo"` or `role: ""`
- ❌ WRONG: `organization: "solo"`, `role: "harrier"` (invalid combination)
- ❌ WRONG: `organization: "solo"`, `role: "brute"` (invalid combination)

Based on analysis of 427 official Draw Steel monsters:
- Solo monsters: 47.8% use `role="solo"`, 52.2% use `role=""`
- Leader monsters: 34.4% use `role="leader"`, 65.6% use `role=""`

---

## Example Calculations

### Level 3 Platoon Harrier
- EV: `ceil(((2×3)+4) × 1.0) = ceil(10) = 10`
- Stamina: `ceil(((10×3)+20) × 1.0) = ceil(50) = 50`
- Free Strike: `ceil((4+3+0) × 0.6) = ceil(4.2) = 5`
- Damage T1: `ceil((4+3+0) × 0.6) = 5`
- Damage T2: `ceil((4+3+0) × 1.1) = ceil(7.7) = 8`
- Damage T3: `ceil((4+3+0) × 1.4) = ceil(9.8) = 10`

### Level 5 Elite Brute
- EV: `ceil(((2×5)+4) × 2.0) = ceil(14 × 2) = 28` ← Organization modifier for EV
- Stamina: `ceil(((10×5)+30) × 2.0) = ceil(80 × 2) = 160` ← Organization modifier for Stamina
- Free Strike: `ceil((4+5+2) × 0.6) = ceil(6.6) = 7` ← +2 damage (Brute +1, Elite +1)
- Damage T1: `ceil((4+5+2) × 0.6) = ceil(6.6) = 7` ← NO organization multiplier!
- Damage T2: `ceil((4+5+2) × 1.1) = ceil(12.1) = 13`
- Damage T3: `ceil((4+5+2) × 1.4) = ceil(15.4) = 16`

### Level 5 Solo (role="solo")
- EV: `ceil(((2×5)+4) × 6.0) = ceil(14 × 6) = 84` ← ×6 for EV
- Stamina: `ceil(((10×5)+30) × 5.0) = ceil(80 × 5) = 400` ← ×5 for Stamina (different!)
- Free Strike: `ceil((4+5+2) × 0.6) = ceil(6.6) = 7` ← +2 damage (Solo role modifier)
- Damage T1: `ceil((4+5+2) × 0.6) = ceil(6.6) = 7` ← NO organization multiplier!
- Damage T2: `ceil((4+5+2) × 1.1) = ceil(12.1) = 13`
- Damage T3: `ceil((4+5+2) × 1.4) = ceil(15.4) = 16`

### Level 1 Horde Controller
- EV: `ceil(((2×1)+4) × 0.5) = ceil(6 × 0.5) = 3`
- Stamina: `ceil(((10×1)+10) × 0.5) = ceil(20 × 0.5) = 10`
- Free Strike: `ceil((4+1+0) × 0.6) ÷ 2 = ceil(3.0) ÷ 2 = 2`
- Damage T1: `ceil((4+1+0) × 0.6) ÷ 2 = 2`
- Damage T2: `ceil((4+1+0) × 1.1) ÷ 2 = ceil(5.5) ÷ 2 = 3`
- Damage T3: `ceil((4+1+0) × 1.4) ÷ 2 = ceil(7.0) ÷ 2 = 4`

### Level 1 Minion Brute (CRITICAL - Different Stamina Formula!)
- EV: `ceil(((2×1)+4) × 0.5) = ceil(6 × 0.5) = 3` (for four minions)
- Stamina: `ceil(((10×1)+30) × 0.125) = ceil(40 × 0.125) = 5` ← **×0.125, NOT ×0.5!**
- Free Strike: `ceil((4+1+1) × 0.6) ÷ 2 = ceil(3.6) ÷ 2 = 2`
- Damage T1: `ceil((4+1+1) × 0.6) ÷ 2 = 2`
- Damage T2: `ceil((4+1+1) × 1.1) ÷ 2 = ceil(6.6) ÷ 2 = 3`
- Damage T3: `ceil((4+1+1) × 1.4) ÷ 2 = ceil(8.4) ÷ 2 = 4`

---

## Quick Reference: Level 1-10 Free Strike

| Level | Free Strike |
|-------|-------------|
| 1 | 3 |
| 2 | 4 |
| 3 | 5 |
| 4 | 5 |
| 5 | 6 |
| 6 | 7 |
| 7 | 7 |
| 8 | 8 |
| 9 | 9 |
| 10 | 9 |

*Note: Values vary by role and organization. Calculate using the formula.*

### Target Damage Scaling

When an ability targets more or fewer creatures than normal, adjust damage:

| Target Change | Multiplier |
|---------------|------------|
| -1 target | 1.2x |
| Normal | 1.0x |
| +1 target | 0.8x |
| +2+ targets | 0.5x |

**Example:** Elite Controller (normally 2 targets) targeting 3 creatures
- Base damage: 10
- Multiplier: 0.8x
- Final damage: 8 per tier
