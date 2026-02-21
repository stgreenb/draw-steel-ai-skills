# Draw Steel Basics

Common rules and terminology for all Draw Steel content generation.

## Valid Damage Types (CRITICAL!)

**ONLY these damage types are valid in Draw Steel:**
- `acid`, `cold`, `corruption`, `fire`, `holy`, `lightning`, `poison`, `psychic`, `sonic`

**INVALID damage types (D&D terminology - will cause issues):**
- `physical`, `slashing`, `bludgeoning`, `piercing`, `force`, `necrotic`, `radiant`, `thunder`, `untyped`

**For untyped damage:** Use empty array `"types": []` or describe in effect text

## Valid Conditions (Draw Steel Only)

**ONLY these conditions are valid in Draw Steel:**
- `bleeding`, `dazed`, `frightened`, `grabbed`, `prone`, `restrained`, `slowed`, `taunted`, `weakened`

**Condition Duration Rules:**

| Pattern | Format | When to Use | How It Ends |
|---------|--------|-------------|-------------|
| **Save ends** | `[condition] (save ends)` | Most conditions in combat | Target makes a save at end of each turn |
| **Until end of next turn** | `[condition] until the end of your next turn` | Temporary buffs/debuffs | Ends automatically at end of your next turn |
| **Until end of encounter** | `[condition] until the end of the encounter` | Special effects | Ends when encounter ends |

**Conditional Conditions (no duration specified):**
- **grabbed** - Ends by escape, release, or breaking adjacency
- **prone** - Ends by standing up maneuver
- **frightened** - Ends when source changes or is removed

**NEVER Use "until healed":** NOT used in published Draw Steel content. Conditions end by save, by specific action, or by time.

**Fallback to Edges/Banes:** If converting from another system and no Draw Steel condition fits, apply edges or banes instead of inventing conditions. Example: D&D "stunned" has no direct equivalent—use "dazed" plus a bane, or "the target takes a bane on all power rolls."

## Valid Characteristics

**ONLY these characteristics are valid in Draw Steel:**
- **Might (M):** Physical strength and force
- **Agility (A):** Speed, reflexes, coordination
- **Reason (R):** Intellect, logic, technical knowledge
- **Intuition (I):** Perception, insight, magical/psionic aptitude
- **Presence (P):** Charisma, force of personality, leadership

**INVALID characteristics (D&D terminology - NEVER USE):**
- `STR`, `DEX`, `CON`, `INT`, `WIS`, `CHA`

## Valid Action Types

**ONLY these action types are valid in Draw Steel:**
- **Main Action:** Primary combat abilities
- **Maneuver:** Movement/positioning (doesn't consume main action)
- **Triggered Action:** Immediate reactions to conditions
- **Free Action:** Quick actions that don't count as maneuvers
- **Respite Activity:** Actions taken during rests

**INVALID action types (D&D terminology - NEVER USE):**
- `bonus action`, `reaction`, `full action`, `standard action`

## Valid Potencies

**Potency values in Draw Steel:**
- **Weak:** Characteristic - 2
- **Average:** Characteristic - 1
- **Strong:** Characteristic (Leader/Solo +1)

**Markdown notation:** `M < 2` means "if target's Might is less than 2"

## Power Roll Format

**Standard power roll:**
```
Power Roll + [characteristic]:
- **≤11:** [Tier 1 effect]
- **12-16:** [Tier 2 effect]
- **17+:** [Tier 3 effect]
```

## Fixed Damage Values (CRITICAL!)

Draw Steel NEVER uses dice notation. Always use fixed values calculated from Draw Steel formulas.

- ❌ WRONG: "1d6+3 damage"
- ✅ CORRECT: "6 damage"

## Forced Movement (CRITICAL!)

Forced movement is a common mechanic across monsters, DTOs, and rewards. The three types are:

- **Push X:** Move target up to X squares away in a straight line (each square must be farther)
- **Pull X:** Move target up to X squares toward in a straight line (each square must be closer)
- **Slide X:** Move target up to X squares in any direction (no straight line required)

**Key rules:**
- Forced movement ignores difficult terrain
- Never provokes opportunity attacks
- Target affected by damaging terrain/environment effects as if they moved willingly
- Movement can always be fewer squares than indicated
- Add "vertical" to allow up/down movement (e.g., "vertical push 5")

**Stability:** Creatures can reduce forced movement by their stability value.

**Slamming:** Force moving into creatures/objects deals damage based on remaining movement.

## Edges and Banes (CRITICAL!)

Edges and banes modify power rolls, representing situational advantages/disadvantages.

| Type | Effect |
|------|--------|
| **Edge** | +2 to power roll |
| **Double Edge** | No bonus, but outcome improves one tier (max tier 3) |
| **Bane** | -2 to power roll |
| **Double Bane** | No penalty, but outcome decreases one tier (min tier 1) |

**Combining:**
- Edge + Bane = No modifier
- Double edge + Bane = Single edge
- Double bane + Edge = Single bane

**Common sources:**
- **Edge:** Flanking, high ground, prone target (melee), hidden attacker, cover from target
- **Bane:** Prone attacker, cover on target, concealment, weakened condition

**Capped at two:** Maximum of double edge or double bane on any roll.
