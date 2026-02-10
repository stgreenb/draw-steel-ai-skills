## ADDED Requirements

### Requirement: Foundry VTT Export Format
The generator SHALL support outputting monsters as Foundry VTT JSON files compatible with the Draw Steel system.

#### Scenario: Export monster as Foundry JSON
- **WHEN** user requests `/create-monster "Level 3 Gremlin Brute" --format foundry`
- **THEN** the generator SHALL produce a valid Foundry NPC JSON file
- **AND** the JSON SHALL conform to the Draw Steel module actor structure

#### Scenario: Export monster as both formats
- **WHEN** user requests `/create-monster "Level 5 Dragon Solo" --format both`
- **THEN** the generator SHALL produce both Markdown stat block and Foundry JSON
- **AND** the JSON file SHALL be written to the output directory

### Requirement: Actor Structure Mapping
The generator SHALL map monster attributes to the correct Foundry actor structure.

#### Scenario: Map characteristics to actor
- **WHEN** generating Foundry JSON for a monster
- **THEN** characteristics SHALL map to `system.characteristics.{char}.value`
- **AND** characteristic names SHALL be: `might`, `agility`, `reason`, `intuition`, `presence`

#### Scenario: Map stamina values
- **WHEN** generating Foundry JSON for a monster
- **THEN** stamina SHALL map to `system.stamina.value` and `system.stamina.max`
- **AND** the value SHALL equal calculated stamina from formulas

#### Scenario: Map size and letter
- **WHEN** generating Foundry JSON for a monster
- **THEN** size SHALL map to `system.combat.size.value` (numeric 1-3, minimum 1)
- **AND** letter SHALL map to `system.combat.size.letter` (T/S/M/L for Tiny/Small/Medium/Large)

#### Scenario: Map monster metadata
- **WHEN** generating Foundry JSON for a monster
- **THEN** level SHALL map to `system.monster.level`
- **AND** EV SHALL map to `system.monster.ev`
- **AND** role SHALL map to `system.monster.role`
- **AND** organization SHALL map to `system.monster.organization`
- **AND** free strike SHALL map to `system.monster.freeStrike`

#### Scenario: Map monster keywords
- **WHEN** generating Foundry JSON for a monster
- **THEN** keywords SHALL be stored in `system.monster.keywords` as a Set
- **AND** supported keywords SHALL include: abyssal, accursed, animal, beast, construct, dragon, elemental, fey, giant, horror, humanoid, infernal, plant, soulless, swarm, undead

#### Scenario: Map negotiation fields
- **WHEN** generating Foundry JSON for a monster
- **THEN** `system.negotiation.interest` SHALL be `5`
- **AND** `system.negotiation.patience` SHALL be `5`
- **AND** `system.negotiation.impression` SHALL be `1`
- **AND** `system.negotiation.motivations` SHALL be an empty Set
- **AND** `system.negotiation.pitfalls` SHALL be an empty Set

#### Scenario: Map biography fields
- **WHEN** generating Foundry JSON for a monster
- **THEN** `system.biography.value` SHALL be empty string or HTML
- **AND** `system.biography.director` SHALL be empty string or HTML (GM only notes)
- **AND** `system.biography.languages` SHALL be an empty Set

#### Scenario: Map status immunities
- **WHEN** generating Foundry JSON for a monster
- **THEN** `system.statuses.immunities` SHALL be an empty Set (unless monster has status immunities)

### Requirement: Ability Item Generation
The generator SHALL create ability items with correct type, category, and effect structure.

#### Scenario: Generate main action ability
- **WHEN** a monster has a main action ability
- **THEN** the item SHALL have `type: "ability"`
- **AND** `system.type` SHALL be `"main"`
- **AND** `system.category` SHALL be `"signature"`, `"heroic"`, or `"malice"` based on tier

#### Scenario: Generate maneuver ability
- **WHEN** a monster has a maneuver ability
- **THEN** the item SHALL have `type: "ability"`
- **AND** `system.type` SHALL be `"maneuver"`
- **AND** `system.category` SHALL be based on tier

#### Scenario: Generate triggered action ability
- **WHEN** a monster has a triggered or free triggered action
- **THEN** the item SHALL have `type: "ability"`
- **AND** `system.type` SHALL be `"triggered"`

#### Scenario: Generate feature or trait
- **WHEN** a monster has a passive ability or trait
- **THEN** the item SHALL have `type: "feature"`

### Requirement: Power Roll Effect Mapping
The generator SHALL convert power roll text to Foundry effect structures.

#### Scenario: Map damage effects with tiers
- **WHEN** an ability has damage effects at different tiers
- **THEN** damage SHALL map to `system.power.effects.{effectId}.type: "damage"`
- **AND** tier 1 SHALL be `system.power.effects.{effectId}.damage.tier1`
- **AND** tier 2 SHALL be `system.power.effects.{effectId}.damage.tier2`
- **AND** tier 3 SHALL be `system.power.effects.{effectId}.damage.tier3`

#### Scenario: Map damage types
- **WHEN** damage has a damage type
- **THEN** the type SHALL be included in `types: []` array
- **AND** supported types SHALL include: `acid`, `cold`, `corruption`, `fire`, `holy`, `lightning`, `poison`, `psychic`, `sonic`

#### Scenario: Map condition effects with save ends
- **WHEN** an ability applies a condition with save ends
- **THEN** it SHALL map to `system.power.effects.{effectId}.type: "applied"`
- **AND** the effect SHALL include `potency` with characteristic
- **AND** the effect SHALL include `effects` with condition and end condition

#### Scenario: Map condition without save ends
- **WHEN** an ability applies a condition without save ends
- **THEN** it SHALL map to `system.power.effects.{effectId}.type: "applied"`
- **AND** the effect SHALL indicate no save required

### Requirement: Enricher Support
The generator SHALL support Foundry enrichers in ability descriptions.

#### Scenario: Support damage enricher
- **WHEN** an ability description contains `[[/damage N]]`
- **THEN** it SHALL be preserved in the Foundry JSON
- **AND** the enricher SHALL render as an interactive damage button in Foundry

#### Scenario: Support healing enricher
- **WHEN** an ability description contains `[[/heal N]]`
- **THEN** it SHALL be preserved in the Foundry JSON
- **AND** the enricher SHALL render as an interactive healing button in Foundry

#### Scenario: Support apply effect enricher
- **WHEN** an ability description contains `[[/apply condition]]`
- **THEN** it SHALL be preserved in the Foundry JSON
- **AND** the enricher SHALL apply the condition when clicked in Foundry

#### Scenario: Support lookup enricher
- **WHEN** an ability description contains `[[/lookup @name]]`
- **THEN** it SHALL be preserved in the Foundry JSON
- **AND** the enricher SHALL resolve to the actor's name at runtime

### Requirement: File Output Structure
The generator SHALL write JSON files to the correct directory structure.

#### Scenario: Create monster directory
- **WHEN** generating Foundry JSON for a monster named "Gremlin"
- **THEN** the generator SHALL create directory `output/Monsters/Gremlin/`

#### Scenario: Write actor JSON file
- **WHEN** generating Foundry JSON for a monster
- **THEN** the generator SHALL write `npc_{CreatureName}_{actorId}.json`
- **AND** the actorId SHALL be a valid UUID

#### Scenario: Generate unique IDs
- **WHEN** generating Foundry JSON
- **THEN** the actor SHALL have a unique `_id` field
- **AND** each item SHALL have a unique `_id` field
- **AND** each effect SHALL have a unique `_key` field

### Requirement: All Monster Types and Organizations
The generator SHALL support all Draw Steel monster organizations.

#### Scenario: Generate minion monster
- **WHEN** creating a Level 1 Minion monster
- **THEN** the Foundry JSON SHALL set `system.monster.organization: "Minion"`
- **AND** stamina SHALL reflect minion formula

#### Scenario: Generate horde monster
- **WHEN** creating a Level 3 Horde monster
- **THEN** the Foundry JSON SHALL set `system.monster.organization: "Horde"`

#### Scenario: Generate platoon monster
- **WHEN** creating a Level 5 Platoon monster
- **THEN** the Foundry JSON SHALL set `system.monster.organization: "Platoon"`

#### Scenario: Generate elite monster
- **WHEN** creating a Level 7 Elite monster
- **THEN** the Foundry JSON SHALL set `system.monster.organization: "Elite"`

#### Scenario: Generate leader monster
- **WHEN** creating a Level 9 Leader monster
- **THEN** the Foundry JSON SHALL set `system.monster.organization: "Leader"`

#### Scenario: Generate solo monster
- **WHEN** creating a Level 10 Solo monster
- **THEN** the Foundry JSON SHALL set `system.monster.organization: "Solo"`

### Requirement: All Monster Roles
The generator SHALL support all Draw Steel monster roles.

#### Scenario: Generate ambusher monster
- **WHEN** creating an Ambusher monster
- **THEN** the Foundry JSON SHALL set `system.monster.role: "Ambusher"`

#### Scenario: Generate artillery monster
- **WHEN** creating an Artillery monster
- **THEN** the Foundry JSON SHALL set `system.monster.role: "Artillery"`

#### Scenario: Generate brute monster
- **WHEN** creating a Brute monster
- **THEN** the Foundry JSON SHALL set `system.monster.role: "Brute"`

#### Scenario: Generate controller monster
- **WHEN** creating a Controller monster
- **THEN** the Foundry JSON SHALL set `system.monster.role: "Controller"`

#### Scenario: Generate defender monster
- **WHEN** creating a Defender monster
- **THEN** the Foundry JSON SHALL set `system.monster.role: "Defender"`

#### Scenario: Generate harrier monster
- **WHEN** creating a Harrier monster
- **THEN** the Foundry JSON SHALL set `system.monster.role: "Harrier"`

#### Scenario: Generate hexer monster
- **WHEN** creating a Hexer monster
- **THEN** the Foundry JSON SHALL set `system.monster.role: "Hexer"`

#### Scenario: Generate mount monster
- **WHEN** creating a Mount monster
- **THEN** the Foundry JSON SHALL set `system.monster.role: "Mount"`

#### Scenario: Generate support monster
- **WHEN** creating a Support monster
- **THEN** the Foundry JSON SHALL set `system.monster.role: "Support"`

### Requirement: Source Citation
The generator SHALL include source citations in Foundry items.

#### Scenario: Include Draw Steel license
- **WHEN** generating Foundry JSON
- **THEN** each item SHALL have `system.source.license: "Draw Steel Creator License"`

#### Scenario: Include book and page reference
- **WHEN** the monster or ability has a source reference
- **THEN** it SHALL be included in `system.source.book` and `system.source.page`

### Requirement: Combat Statistics
The generator SHALL map all combat statistics including turns, save threshold, and disengage.

#### Scenario: Map solo monster turns
- **WHEN** generating a Solo monster
- **THEN** `system.combat.turns` SHALL be `2`
- **AND** other organizations SHALL have `system.combat.turns` of `1`

#### Scenario: Map save threshold
- **WHEN** generating Foundry JSON
- **THEN** `system.combat.save.threshold` SHALL be a number between 1 and 10
- **AND** the default value SHALL be `6`
- **AND** `system.combat.save.bonus` MAY be an empty string or a formula

#### Scenario: Map disengage value
- **WHEN** generating Foundry JSON
- **THEN** `system.movement.disengage` SHALL be set (typically 1)

#### Scenario: Map stability value
- **WHEN** generating Foundry JSON
- **THEN** `system.combat.stability` SHALL be set based on monster size and role
- **AND** the value SHALL be a non-negative integer

### Requirement: Movement Types
The generator SHALL map movement types including special movement like flight.

#### Scenario: Map movement types array
- **WHEN** generating Foundry JSON
- **THEN** `system.movement.types` SHALL be a Set
- **AND** values MAY include: `["walk"]`, `["fly"]`, `["swim"]`, `["teleport"]`, `["burrow"]`, `["climb"]`
- **AND** default value SHALL be `["walk"]`

#### Scenario: Map hover capability
- **WHEN** a monster has hover capability
- **THEN** `system.movement.hover` SHALL be `true`

#### Scenario: Map default movement value
- **WHEN** generating Foundry JSON
- **THEN** `system.movement.value` SHALL be the monster's speed
- **AND** default value SHALL be `5`

### Requirement: Damage Immunities and Weaknesses with Values
The generator SHALL support numeric values for immunities and weaknesses.

#### Scenario: Map damage weakness with value
- **WHEN** a monster has a damage weakness
- **THEN** the weakness value SHALL be set in `system.damage.weaknesses.{type}`
- **EXAMPLE**: `holy: 5` means 5 holy weakness

#### Scenario: Map damage immunity
- **WHEN** a monster has damage immunity
- **THEN** `system.damage.immunities.{type}` SHALL be set (typically 0)

### Requirement: Extended Ability Types
The generator SHALL support all Draw Steel ability types.

#### Scenario: Generate villain action
- **WHEN** a monster has a villain action
- **THEN** the item SHALL have `type: "ability"`
- **AND** `system.type` SHALL be `"villain"`
- **AND** `system.category` SHALL be `"villain"`

#### Scenario: Generate free triggered action
- **WHEN** a monster has a free triggered action
- **THEN** the item SHALL have `type: "ability"`
- **AND** `system.type` SHALL be `"freeTriggered"`

#### Scenario: Generate ability without type
- **WHEN** an ability has no specific type
- **THEN** the item SHALL have `type: "ability"`
- **AND** `system.type` SHALL be `"none"`

### Requirement: Extended Distance and Target Types
The generator SHALL support all distance and target types.

#### Scenario: Map meleeRanged distance
- **WHEN** an ability has combined melee and ranged distance
- **THEN** `system.distance.type` SHALL be `"meleeRanged"`
- **AND** `system.distance.primary` SHALL be the melee reach
- **AND** `system.distance.secondary` SHALL be the ranged limit

#### Scenario: Map cube area
- **WHEN** an ability targets a cube area
- **THEN** `system.distance.type` SHALL be `"cube"`
- **AND** `system.distance.primary` SHALL be the cube size

#### Scenario: Map line area with dimensions
- **WHEN** an ability targets a line area
- **THEN** `system.distance.type` SHALL be `"line"`
- **AND** `system.distance.primary` SHALL be the length
- **AND** `system.distance.secondary` SHALL be the width
- **AND** `system.distance.tertiary` SHALL be the height

#### Scenario: Map target types including objects
- **WHEN** an ability can target creatures and objects
- **THEN** `system.target.type` MAY be `"creatureObject"` or `"enemyObject"`

### Requirement: Force Movement with Properties
The generator SHALL support force movement with additional properties.

#### Scenario: Map vertical force movement
- **WHEN** force movement has vertical component
- **THEN** the forced effect SHALL include `properties: ["vertical"]`

#### Scenario: Map forced movement types
- **WHEN** an ability causes force movement
- **THEN** the effect type SHALL be `"forced"`
- **AND** `system.power.effects.{id}.forced.{tier}.movement` SHALL be `["push"]`, `["pull"]`, or `["slide"]`

### Requirement: Item Effects for Status Conditions
The generator SHALL support item effects for status conditions.

#### Scenario: Generate status effect on item
- **WHEN** an ability applies a status condition
- **THEN** the item MAY have an `effects` array
- **AND** each effect SHALL have `type: "base"`
- **AND** effect SHALL have `statuses` array (e.g., `["slowed", "weakened"]`)

#### Scenario: Map effect end conditions
- **WHEN** a status effect has an end condition
- **THEN** effect.system.end.type SHALL be `"save"`
- **AND** effect.system.end.roll SHALL be the save formula

### Requirement: Prototype Token Configuration
The generator SHALL include prototype token configuration for Foundry.

#### Scenario: Set prototype token name
- **WHEN** generating Foundry JSON
- **THEN** `prototypeToken.name` SHALL match the actor name

#### Scenario: Set prototype token image
- **WHEN** generating Foundry JSON
- **THEN** `prototypeToken.texture.src` SHALL reference the role-based image
- **AND** other token texture properties SHALL be set (anchor, fit, scale, etc.)

#### Scenario: Set prototype token display settings
- **WHEN** generating Foundry JSON
- **THEN** `prototypeToken.displayName` SHALL be `20` (always show name)
- **AND** `prototypeToken.displayBars` SHALL be `20` (always show bars)
- **AND** `prototypeToken.bar1.attribute` SHALL be `"stamina"`

### Requirement: Token Images
The generator SHALL use role-based token images from the Draw Steel module.

#### Scenario: Use role-based default images
- **WHEN** generating Foundry JSON for a monster
- **THEN** the actor SHALL reference the Draw Steel role-based token image
- **AND** the image SHALL correspond to the monster's role (Ambusher, Artillery, Brute, Controller, Defender, Harrier, Hexer, Mount, Support)

#### Scenario: Image path for brute role
- **WHEN** generating Foundry JSON for a Brute monster
- **THEN** the image path SHALL reference the Draw Steel brute role image

### Requirement: AI Image Generation (Future Enhancement)
The generator SHALL support AI-generated custom monster images when the model supports it and user requests it.

#### Scenario: Generate custom image (future)
- **WHEN** the model supports image generation AND user requests `--generate-image`
- **THEN** the generator SHALL create a custom monster portrait
- **AND** the image SHALL be saved to the output directory
- **AND** the Foundry JSON SHALL reference the generated image

#### Scenario: Image generation fallback (future)
- **WHEN** image generation is requested but model doesn't support it
- **THEN** the generator SHALL fall back to role-based default images
