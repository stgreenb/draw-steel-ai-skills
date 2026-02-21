# Draw Steel Ability Templates by Role

Each role has a characteristic ability pattern. Use these as style reference when generating monsters.

## HARRIER: Mobility + Strikes

**Archetype:** Fast, evasive melee attacker with repositioning effects

**Characteristic:** Agility

**Force Movement Preference:** Pull (targets moved toward attacker)

**Signature Ability Pattern:**
```
[Name]: [Flying/Swift/Evasive] [Attack Type]
Power Roll: 2d10 + Agility
- Tier 1 (≤11): [Damage_T1] slashing/physical; pull [pull_T1]
- Tier 2 (12-16): [Damage_T2] slashing/physical; pull [pull_T2] + [condition] (save ends)
- Tier 3 (17+): [Damage_T3] slashing/physical; pull [pull_T3] + [condition] (save ends)
```

**Secondary Ability Pattern:**
```
[Name]: Repositioning action (non-damaging)
Power Roll: 2d10 + Agility
- Tier 1 (≤11): Shift [speed] squares, grant ally movement
- Tier 2 (12-16): Shift [speed] squares, grant ally movement + [condition] (EoT)
- Tier 3 (17+): Shift [speed] squares, grant ally movement + [condition] (save ends)
```

**Force Movement by Level:**
| Level | Pull (T1/T2/T3) |
|-------|-----------------|
| 1 | 1/2/2 |
| 2-4 | 2/3/4 |
| 5-7 | 3/4/5 |
| 8-10 | 4/5/6 |

**Examples:**
- Aerial Strike (Pegasus)
- Talons & Flight (Griffon)
- Striking Dive (Wyvern)

---

## BRUTE: High Damage + Area + Control

**Archetype:** Powerful area attacker with crowd control

**Characteristic:** Might

**Force Movement Preference:** Push (targets moved away from attacker)

**Signature Ability Pattern:**
```
[Name]: [Powerful] [Area Attack]
Power Roll: 2d10 + Might (Area)
- Tier 1 (≤11): [Damage_T1] bludgeoning/fire/physical; push [push_T1]
- Tier 2 (12-16): [Damage_T2] bludgeoning/fire/physical; push [push_T2] + [condition] (save ends)
- Tier 3 (17+): [Damage_T3] bludgeoning/fire/physical; push [push_T3] + [condition] (save ends)
```

**Secondary Ability Pattern:**
```
[Name]: [Crowd Control]
Power Roll: 2d10 + Might (Area)
- Tier 1 (≤11): All enemies [condition] (EoT)
- Tier 2 (12-16): All enemies [condition] (save ends)
- Tier 3 (17+): All enemies [condition] + [condition] (save ends)
```

**Force Movement by Level:**
| Level | Push (T1/T2/T3) |
|-------|-----------------|
| 1 | 1/1/1 |
| 2-4 | 1/2/2 |
| 5-7 | 2/2/3 |
| 8-10 | 2/3/3 |

**Examples:**
- Crushing Blow (Manticore)
- Fire Breath (Phoenix)
- Stomp (Giant)

---

## CONTROLLER: Debuffs + Positioning

**Archetype:** Tactical creature applying conditions and weak debuffs

**Characteristic:** Reason

**Force Movement Preference:** Pull or Slide (strategic repositioning)

**Signature Ability Pattern:**
```
[Name]: [Tactical] [Debuff Attack]
Power Roll: 2d10 + Reason
- Tier 1 (≤11): [Damage_T1] psychic/corruption; [condition] (EoT)
- Tier 2 (12-16): [Damage_T2] psychic/corruption; [condition] (save ends)
- Tier 3 (17+): [Damage_T3] psychic/corruption; [condition] + [condition] (save ends)
```

**Secondary Ability Pattern:**
```
[Name]: [Area Effect]
Power Roll: 2d10 + Reason (Area)
- Tier 1 (≤11): Create difficult terrain, enemies [condition] (EoT)
- Tier 2 (12-16): Expand area, enemies [condition] (save ends)
- Tier 3 (17+): Control area, enemies [condition] + [condition] (save ends)
```

**Force Movement by Level (Pull or Slide):**
| Level | Pull (T1/T2/T3) | Slide (T1/T2/T3) |
|-------|-----------------|------------------|
| 1 | 1/2/2 | 1/2/2 |
| 2-4 | 2/3/4 | 2/3/4 |
| 5-7 | 3/4/5 | 3/4/5 |
| 8-10 | 4/5/6 | 4/5/6 |

**Examples:**
- Mind Control (Mind Flayer)
- Web (Spider)
- Entangle (Treant)
- Tier 1 (≤11): Create terrain/effect (non-damaging)
- Tier 2 (12-16): Expand effect + weaken
- Tier 3 (17+): Control positioning
```

---

## DEFENDER: Protection + Reduction

**Archetype:** Tank protecting allies with damage reduction

**Characteristic:** Might

**Signature Ability Pattern:**
```
[Name]: [Protective] [Block Attack]
Power Roll: 2d10 + Might
- Tier 1 (≤11): [Damage_T1] + grant [Ally] +2 to next attack
- Tier 2 (12-16): [Damage_T2] + grant all allies +2 to next attack
- Tier 3 (17+): [Damage_T3] + grant all allies +2 to next attack + Damage Reduction until end of turn
```

**Malice Feature Pattern:**
```
[Name]: [Defensive Aura]
Passive: Nearby allies gain +1 to defense
```

---

## AMBUSHER: High Burst + Surprise

**Archetype:** Stealthy attacker dealing massive sudden damage

**Characteristic:** Agility

**Signature Ability Pattern:**
```
[Name]: [Surprise] [Burst Attack]
Power Roll: 2d10 + Agility
- Tier 1 (≤11): [Damage_T1] + Advantage on next attack
- Tier 2 (12-16): [Damage_T2] + Advantage + Quick (can act after target)
- Tier 3 (17+): [Damage_T3] + Advantage + Quick + Free Strike
```

**Secondary Ability Pattern:**
```
[Name]: [Evasion] [Escape]
Power Roll: 2d10 + Agility
- Tier 1 (≤11): Teleport 3 spaces + gain +2 defense
- Tier 2 (12-16): Teleport 5 spaces + invisible until end of turn
- Tier 3 (17+): Teleport 8 spaces + invisible + next attack deals +50% damage
```

**Examples:**
- Backstab (Assassin)
- Shadow Strike (Shadow Demon)
- Ambush (Tiger)

---

## ARTILLERY: Area Damage + Long Range

**Archetype:** Ranged attacker dealing area damage from distance

**Characteristic:** Reason

**Force Movement Preference:** Slide (strategic repositioning away from attacker)

**Signature Ability Pattern:**
```
[Name]: [Long Range] [Area Attack]
Power Roll: 2d10 + Reason (Range 10, Area 3×3)
- Tier 1 (≤11): [Damage_T1] fire/lightning/corrosive; slide [slide_T1]
- Tier 2 (12-16): [Damage_T2] fire/lightning/corrosive; slide [slide_T2] + [condition] (save ends)
- Tier 3 (17+): [Damage_T3] fire/lightning/corrosive; slide [slide_T3] + [condition] (save ends)
```

**Secondary Ability Pattern:**
```
[Name]: [Targeted] [Single Attack]
Power Roll: 2d10 + Reason (Range 8)
- Tier 1 (≤11): [Damage_T1] + slide [slide_T1]
- Tier 2 (12-16): [Damage_T2] + slide [slide_T2] + Impaired
- Tier 3 (17+): [Damage_T3] + slide [slide_T3] + Impaired + Blinded
```

**Force Movement by Level:**
| Level | Slide (T1/T2/T3) |
|-------|------------------|
| 1 | 1/2/2 |
| 2-4 | 2/3/4 |
| 5-7 | 3/4/5 |
| 8-10 | 4/5/6 |

**Malice Feature Pattern:**
```
[Name]: [Sniper]
Passive: Ignore 2 spaces of cover
```

**Examples:**
- Fireball (Efreeti)
- Lightning Bolt (Storm Giant)
- Cannon Shot (Siege Engine)

---

## HEXER: Conditions + Curses

**Archetype:** Debuffer applying multiple status effects

**Characteristic:** Reason

**Signature Ability Pattern:**
```
[Name]: [Cursed] [Affliction Attack]
Power Roll: 2d10 + Reason
- Tier 1 (≤11): [Damage_T1] psychic/corruption + Cursed
- Tier 2 (12-16): [Damage_T2] + Cursed + Weakened
- Tier 3 (17+): [Damage_T3] + Cursed + Weakened + Harrowed
```

**Secondary Ability Pattern:**
```
[Name]: [Area Effect] [Hex]
Power Roll: 2d10 + Reason (Area)
- Tier 1 (≤11): All enemies Slowed
- Tier 2 (12-16): All enemies Slowed + Weakened
- Tier 3 (17+): All enemies Slowed + Weakened + Harrowed
```

**Malice Feature Pattern:**
```
[Name]: [Hex Ward]
Passive: While above 50% HP, immune to conditions
```

**Examples:**
- Curse of Weakness (Witch)
- Haunting (Specter)
- Vile Touch (Night Hag)

---

## MOUNT: Carrying Capacity + Movement

**Archetype:** Creature designed to carry allies with enhanced movement

**Characteristic:** Might or Agility

**Signature Ability Pattern:**
```
[Name]: [Carry] [Transport Attack]
Power Roll: 2d10 + Might
- Tier 1 (≤11): [Damage_T1] + ally can mount as free action
- Tier 2 (12-16): [Damage_T2] + mounted ally gains Charge
- Tier 3 (17+): [Damage_T3] + mounted ally gains Charge + Free Strike
```

**Secondary Ability Pattern:**
```
[Name]: [Speed] [Movement]
- Tier 1 (≤11): Move 8 spaces, carry 1 ally
- Tier 2 (12-16): Move 10 spaces, carry 2 allies, grant them +1 to next attack
- Tier 3 (17+): Move 12 spaces, carry 2 allies, grant them +2 to next attack + Quick
```

**Malice Feature Pattern:**
```
[Name]: [Saddle]
Passive: Mounted rider uses mount's defense +2, can act when mount acts
```

**Examples:**
- Warhorse (Battle Mount)
- Flying Mount (Pegasus)
- Beast of Burden (Giant Elk)

---

## SUPPORT: Buffs + Healing + Utility

**Archetype:** Ally enhancer providing healing and bonuses

**Characteristic:** Presence

**Signature Ability Pattern:**
```
[Name]: [Aid] [Support Attack]
Power Roll: 2d10 + Presence
- Tier 1 (≤11): Heal [Heal_T1] + grant +1 to next attack
- Tier 2 (12-16): Heal [Heal_T2] + grant +2 to next attack + Quick
- Tier 3 (17+): Heal [Heal_T3] + grant +2 to next attack + Quick + Free Strike
```

**Secondary Ability Pattern:**
```
[Name]: [Buff] [Enhancement] (Area)
Power Roll: 2d10 + Presence (Area 3×3)
- Tier 1 (≤11): All allies gain +1 to attacks
- Tier 2 (12-16): All allies gain +2 to attacks + +1 defense
- Tier 3 (17+): All allies gain +3 to attacks + +2 defense + Quick
```

**Malice Feature Pattern:**
```
[Name]: [Inspiring Presence]
Passive: When ally within 3 spaces takes damage, gain +1 to next attack
```

**Examples:**
- Healing Light (Couatl)
- Rally (Bard)
- Bless (Guardian Angel)

---

## General Ability Design Guidelines

1. **Damage values:** Always use calculated T1/T2/T3 from formulas
2. **Conditions:** Scale from 1 condition at T1 to 3 at T3
3. **Keywords:** Match ability to creature theme
4. **Damage types:** Choose appropriate type (slashing for claws, fire for dragons, etc.)
5. **Non-damaging abilities:** Should provide tactical advantage
6. **Malice features:** Passive bonuses or powerful triggered actions

---

## Maneuver Requirements by Organization

Based on Bestiary analysis, most monsters have maneuvers, but **Minions NEVER have maneuvers**:

| Organization | Maneuver? | Notes |
|--------------|-----------|-------|
| **Minion** (any level) | ❌ No | Only signature ability + passive traits |
| **Horde** (any level) | ✅ Yes | Common: Hidden Movement, situational effects |
| **Platoon** (Level 1) | ⚠️ Usually | ~50% have maneuvers; acceptable to omit |
| **Platoon** (Level 2+) | ✅ Yes | Should have a maneuver |
| **Elite** (any level) | ✅ Yes | Must have a maneuver |
| **Leader** (any level) | ✅ Yes | Must have a maneuver |
| **Solo** (any level) | ✅ Yes | Must have a maneuver |

### Minion-Specific Notes

**Minions are unique:**
- Stamina uses **×0.125** modifier (NOT ×0.5)
- Only ONE signature ability (no maneuvers, no malice abilities)
- "With Captain" shown in stat block table, NOT as separate trait
- May have passive death traits (e.g., "explodes when killed")

### When to Omit a Maneuver

**OK to skip maneuvers for:**
- Minions (always)
- Level 1 Platoon monsters (optional)
- Monsters with 2+ main action abilities

**Should include maneuvers:**
- All Elites, Leaders, Solos
- Platoon monsters Level 2+
- Horde monsters

### Common Maneuver Types

| Type | Example Triggers | Role Fit |
|------|------------------|----------|
| **Movement** | Shift, teleport, relocate | Harrier, Ambusher |
| **Terrain** | Create difficult terrain, area effects | Controller, Artillery |
| **Buff/Debuff** | Grant edge, impose bane | Support, Hexer |
| **Utility** | Hide, recover, assist | Any role |

### Maneuver Examples by Role

**Controller Maneuver:**
```markdown
> ❇️ **Arcane Veil**
>
> | **Area, Magic** | **Maneuver** |
> | **📏 3 burst** | **🎯 Special** |
>
> **Effect:** Until the start of your next turn, the area is filled with magical fog. Creatures in the area have concealment.
```

**Brute Maneuver:**
```markdown
> 👤 **Brutal Charge**
>
> | **-** | **Maneuver** |
> | **📏 Self** | **🎯 Self** |
>
> **Effect:** You move up to your speed. The first creature you move adjacent to during this movement takes 3 damage.
```

**Harrier Maneuver:**
```markdown
> 👤 **Evasive Reposition**
>
> | **-** | **Maneuver** |
> | **📏 Self** | **🎯 Self** |
>
> **Effect:** You shift up to 3 squares and gain +2 to defense until the end of your next turn.
```

---

## Malice Abilities by Organization

Based on official Draw Steel monsters, malice ability counts vary by organization:

| Organization | Malice Abilities | Notes |
|--------------|------------------|-------|
| **Minion** | ❌ 0 | Never have malice abilities |
| **Horde** | 0-2 | Optional, usually 1-2 unique abilities |
| **Platoon** | 0-2 | Optional, may have shared faction abilities |
| **Elite** | 2-3 | Expected to have malice abilities |
| **Leader** | 2-3 | Plus 3 villain actions |
| **Solo** | 3 | Plus 3 villain actions |

**Malice costs range from 2-10**, with common values:
- **2-3**: Minor abilities, utility effects
- **5**: Standard ability cost
- **7**: Powerful abilities
- **10**: Ultimate-level effects

---

## Advanced Features

### ⚠️ Villain Actions (Leaders and Solos Only)

**Experimental Feature:** Villain Actions are unlikely to generate well through AI. Quality may vary.

Each Leader/Solo has exactly 3 Villain Actions, used once per encounter:

| Action | Purpose | Timing |
|--------|---------|--------|
| **Opener** | Relocation, minor damage, summons, buffs, or debuffs | End of any creature's turn |
| **Crowd Control** | Debuffing, area management, regaining upper hand | End of any creature's turn |
| **Ultimate** | High-damage finisher, dramatic finish | End of any creature's turn |

**Template:**
```markdown
<!-- -->
> ☠️ **Villain Action: [Name]**
>
> **Type:** [Opener / Crowd Control / Ultimate]
>
> **Trigger:** You can use this action at the end of any other creature's turn during combat.
>
> **Effect:** [Description]
>
> **Usage:** Once per encounter. No more than one villain action per round.
```

**Example - Solo Dragon:**
```markdown
> ☠️ **Villain Action: Smoke Bomb**
>
> **Type:** Opener
>
> **Effect:** The dragon exhales a cloud of smoke that fills a 5 burst. Creatures in the area are blinded until the end of their next turn.

> ☠️ **Villain Action: Tail Sweep**
>
> **Type:** Crowd Control
>
> **Effect:** The dragon sweeps their tail in a 3 line. Creatures in the area must be on the ground and are pushed 3 squares.

> ☠️ **Villain Action: Devastating Breath**
>
> **Type:** Ultimate
>
> **Effect:** The dragon unleashes their full breath weapon in a 5×10 line. Creatures in the area take damage equal to 2× their tier 3 signature ability damage.
```

### Solo Turn Rules

Solo creatures can take multiple turns per round:

| Solo Type | Turns per Round | Timing |
|-----------|-----------------|--------|
| Standard Solo | 2 | Start and middle, or middle and end |
| Boss Solo | 3 | Start, middle, and end |
| Mini-Boss | 2 | Start and end |

**Template:**
```markdown
<!-- -->
> ⭐️ **Solo Turns**
>
> **Effect:** At the start of each of the solo's turns, they take another turn. This allows the solo to take up to 2 turns per round (or 3 for particularly powerful solos).
>
> **Note:** Only one villain action can be used per round, even with multiple turns.
```

### Minion "With Captain" Trait

**CRITICAL:** Minions MUST have a "With Captain" trait shown in the stat block table, NOT as a separate ability!

Minions gain bonuses when led by a captain. This is shown in the table, not as a separate trait.

| Bonus Type | Example |
|------------|---------|
| Damage | `+2 damage bonus to strikes` |
| Speed | `+2 bonus to speed` |
| Accuracy | `Gain an edge on strikes` |
| Range | `+5 bonus to ranged distance` |
| Melee Range | `+2 bonus to melee distance` |

**Correct format - In stat block table:**
```markdown
| **+2 bonus to speed**<br/> With Captain | **-**<br/> Weaknesses |
```

**WRONG - As a separate trait (DO NOT DO THIS):**
```markdown
<!-- -->
> ⭐️ **With Captain**
>
> **Effect:** While a captain is present, this minion gains +2 speed.
```

### Minion Ability Structure

Minions have a simplified structure:
1. **Signature ability only** (one main action)
2. **With Captain** in the stat block table
3. **Optional passive trait** (death effects, special abilities)

**Minions do NOT have:**
- Maneuver abilities (type: "maneuver")
- Malice-cost abilities (resource > 0)
- Multiple main action abilities
- Villain actions

### Malice Features

All monsters have access to basic Malice features:

| Cost | Feature | Effect |
|------|---------|--------|
| 3 Malice | Brutal Effectiveness | Next ability's potency increased by 1 |
| 5+ Malice | Malicious Strike | Extra damage = highest characteristic, +1 per extra Malice (max 3x) |

**Template:**
```markdown
<!-- -->
> 💀 **[Creature Type] Malice Features**
>
> At the start of any monster's turn, you can spend Malice to activate one of the following:
>
> **Brutal Effectiveness (3 Malice):** The monster's next ability with a potency has that potency increased by 1.
>
> **Malicious Strike (5+ Malice):** The monster's next strike deals extra damage equal to their highest characteristic. +1 damage per additional Malice spent (max 3x).
```

### Triggered Actions by Organization

Based on Bestiary analysis, triggered actions are reserved for more powerful monsters:

| Organization | Level Range | Triggered Actions |
|--------------|-------------|-------------------|
| **Minion** | Any | None |
| **Horde** | Level 1-3 | None |
| **Platoon** | Level 1-5 | None |
| **Elite** | Level 4+ | 1 (situational) |
| **Leader** | Level 4+ | 1 (ally-focused) |
| **Solo** | Level 5+ | 1-2+ (core mechanics) |

**When to Add Triggered Actions:**
- Elite/Leader with thematic defensive ability
- Solo monsters needing reactive depth
- High-level (5+) monsters

**When to Skip:**
- Minions, Horde, Platoon monsters
- Any monster with 3+ abilities already

**Role-Specific Patterns:**

| Role | Type | Typical Trigger |
|------|------|-----------------|
| **Solo Controller** | Free | Zone/aura response |
| **Solo Brute** | Free | Counter-attack |
| **Elite Defender** | Triggered | Ally protection |

**Example (Level 5 Elite Defender):**
```markdown
> ❗️ **Shield Block**
>
> | **Melee** | **Triggered action** |
> | **📏 Melee 1** | **🎯 Self** |
>
> **Trigger:** An ally within distance is targeted by an enemy's ability.
>
> **Effect:** You become the target of the triggering ability, then can make a free strike against the enemy.
```

**Example (Level 8 Solo Controller):**
```markdown
> ❗️ **Aetheric Backlash**
>
> | **Arcane, Ranged** | **Free triggered action** |
> | **📏 Ranged 10** | **🎯 One creature** |
>
> **Trigger:** A creature within distance uses a triggered action.
>
> **Effect:** The target takes 8 psychic damage and is dazed until the end of their next turn.
```
