#!/usr/bin/env python
"""Test script to test NVIDIA GLM 4.7 streaming"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "webapp"))

from llm_client import LLMClient

client = LLMClient()

print("Testing NVIDIA GLM 4.7 streaming...")
print("Model: z-ai/glm4.7")
print()

system_prompt = """You are an expert monster designer for the Draw Steel tabletop RPG. Generate Draw Steel TTRPG monsters that strictly conform to official MCDM stat block format.

CRITICAL RULES:
- Use Draw Steel terminology: EV, Stamina, Keywords, Organization, Role
- Make stats balanced using Draw Steel formulas
- Use ONLY valid keywords, damage types, and ability types

DRAW STEEL FORMULAS:
- EV = ceil(((2 × Level) + 4) × Organization_Modifier)
- Stamina = ceil(((10 × Level) + Role_Stamina_Modifier) × Organization_Modifier)
- Damage = ceil((4 + Level + Role_Damage_Modifier) × Tier_Modifier)
- Free Strike = Damage at Tier 1

VALID VALUES:
- Organization: minion, horde, platoon, elite, leader, solo
- Role: ambusher, artillery, brute, controller, defender, harrier, hexer, mount, support, solo
- Monster keywords: abyssal, accursed, animal, beast, construct, dragon, elemental, fey, giant, horror, humanoid, infernal, plant, soulless, swarm, undead
- Ability keywords: animal, animapathy, area, charge, chronopathy, cryokinesis, earth, fire, green, magic, melee, metamorphosis, psionic, pyrokinesis, ranged, resopathy, rot, performance, strike, telekinesis, telepathy, void, weapon
- Damage types: acid, bludgeoning, cold, corruption, fire, holy, lightning, poison, piercing, psychic, slashing, sonic

REQUIRED MARKDOWN OUTPUT FORMAT:
```markdown
---
ancestry:
  - keyword1
  - keyword2
ev: 'XX'
file_basename: MonsterName
free_strike: 'X'
level: X
might: X
agility: X
reason: X
intuition: X
presence: X
roles:
  - Level X Organization Role
size: 1M
speed: X
stability: 0
stamina: 'XXX'
type: monster
---

###### Monster Name

| Keyword1, Keyword2 | - | Level X | Organization Role | EV XX |
| :-----------------: | :-: | :-----: | :--------------: | :---: |
| **Size**<br/> Size | **Speed**<br/> Speed | **Stamina**<br/> Stamina | **Stability**<br/> Stability | **Free Strike**<br/> Free Strike |
| **-**<br/> Immunity | **-**<br/> Movement | - | **-**<br/> With Captain | **-**<br/> Weaknesses |
| **+M**<br/> Might | **+A**<br/> Agility | **+R**<br/> Reason | **+I**<br/> Intuition | **+P**<br/> Presence |

<!-- -->
> ⚔️ **Ability Name - 2d10 + X**
>
> | **Keywords** | **Type** |
> | :----------- | :------: |
> | **Distance** | **Target** |
>
> **Power Roll + Characteristic:**
>
> - **≤11:** X damage; condition
> - **12-16:** X damage; condition
> - **17+:** X damage; condition
>
> **Effect:** Detailed effect description.
```

ABILITY REQUIREMENTS:
- EXACTLY ONE ability with category: "signature"
- All keywords must be lowercase
- Include tiered damage (≤11, 12-16, 17+) with different values
- Include potency notation for conditions
- Include proper distance (melee, ranged, burst X, etc.)
- Include roll: @chr for abilities that use characteristics
- Include damage value for abilities that deal damage
- Write clear, concise effect descriptions"""

user_prompt = "Create a Draw Steel monster: Level 1 Goblin, Minion Harrier\n\nIMPORTANT: Output ONLY the complete Markdown stat block in the required format. Do not include any explanations or text outside the Markdown."

print("Starting stream...")
print("=" * 80)

full_content = []
full_reasoning = []
chunk_count = 0

try:
    for chunk in client.generate_stream(
        system_prompt=system_prompt, user_prompt=user_prompt, model="z-ai/glm4.7"
    ):
        chunk_count += 1
        chunk_type = chunk.get("type")

        if chunk_type == "reasoning":
            reasoning_chunk = chunk.get("content", "")
            full_reasoning.append(reasoning_chunk)

        elif chunk_type == "content":
            content_chunk = chunk.get("content", "")
            full_content.append(content_chunk)
            print(f"[{chunk_count}] Got content chunk: {repr(content_chunk[:100])}")

        elif chunk_type == "done":
            print("\n" + "=" * 80)
            print("DONE CHUNK RECEIVED!")
            print("=" * 80)
            print(f"Tokens: {chunk.get('tokens', {})}")
            print(f"Reasoning chunks: {len(full_reasoning)}")
            print(f"Content chunks: {len(full_content)}")
            print(f"Reasoning length: {len(''.join(full_reasoning))}")
            print(f"Content length: {len(''.join(full_content))}")
            print("\n>>> FULL CONTENT <<<")
            full_output = "".join(full_content)
            print(full_output)
            print(">>> END CONTENT <<<")

            # Save to file
            with open("nvidia_glm_output.md", "w") as f:
                f.write(full_output)
            print(f"\nSaved to nvidia_glm_output.md")
            break

        elif chunk_type == "error":
            print(f"\nERROR: {chunk.get('error')}")
            break

        if chunk_count > 1000:
            print(f"\nStopping after {chunk_count} chunks")
            print(f"Reasoning chunks: {len(full_reasoning)}")
            print(f"Content chunks: {len(full_content)}")
            break

except Exception as e:
    print(f"\nException: {e}")
    import traceback

    traceback.print_exc()
