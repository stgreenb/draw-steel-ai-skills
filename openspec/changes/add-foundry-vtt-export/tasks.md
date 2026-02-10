# Tasks: Add Foundry VTT Export Capability

## Phase 1: Spec and Infrastructure

- [x] 1.1 Create `openspec/changes/add-foundry-vtt-export/specs/foundry-export/spec.md`
  - Define requirements for Foundry VTT JSON export
  - Add scenarios for each export mode
  - Document actor structure, item structure, and enricher support

- [x] 1.2 Validate OpenSpec proposal
  - Run `openspec validate add-foundry-vtt-export --strict --no-interactive`
  - Fix any validation errors

## Phase 2: Core Export Function

- [x] 2.1 Add `--format` parameter to skill interface
  - Support values: `markdown` (default), `foundry`, `both`
  - Document in SKILL.md

- [x] 2.2 Create `generate_foundry_vtt_json()` function
  - Takes monster data dictionary
  - Returns complete Foundry NPC JSON object
  - Generate UUIDs for actor and items

- [x] 2.3 Implement actor structure mapping
  - Map characteristics: might, agility, reason, intuition, presence
  - Map stamina value and max
  - Map size (1-3) and letter (S/M/L)
  - Map speed and stability
  - Map keywords and damage immunities/weaknesses
  - Map combat turns (solo = 2, others = 1)
  - Map save threshold based on level
  - Map disengage value (typically 1)
  - Map movement types (walk, fly, swim)
  - Map hover capability if applicable

- [x] 2.4 Implement monster metadata mapping
  - Level, EV, role, organization
  - Free strike value
  - Monster keywords

## Phase 3: Item Generation

- [x] 3.1 Implement ability type mapping
  - Main Action → type: `main`, category based on tier
  - Maneuver → type: `maneuver`
  - Free Triggered Action → type: `freeTriggered`
  - Triggered Action → type: `triggered`
  - Villain Action → type: `villain`, category: `villain`
  - Abilities with resource/trigger → type: `none`
  - Passive/Trait → type: `feature`

- [x] 3.2 Implement power roll to effects mapping
  - Parse damage tiers (≤11, 12-16, 17+)
  - Map damage types: acid, cold, corruption, fire, holy, lightning, poison, psychic, sonic
  - Map condition effects with save ends
  - Map force movement effects (push, pull, slide)
  - Support force movement properties (vertical)

- [x] 3.3 Implement ability item structure
  - Name, type, system fields
  - Distance types: melee, ranged, burst, line, cube, meleeRanged, self, special
  - Target types: creature, enemy, creatureObject, enemyObject, self, special
  - Power roll formula and characteristics
  - Effect definitions with tiers
  - Source citations
  - Resource and trigger fields for special abilities
  - Story field (empty string)

- [x] 3.4 Implement feature/trait item structure
  - Name, type: `feature`
  - System fields for passive abilities
  - Description with HTML formatting
  - Source citations

- [x] 3.5 Implement item effects for status conditions
  - Create effects array on items when needed
  - Map status conditions to effect structure
  - Set effect type: `base`
  - Define end conditions (save with roll formula)
  - Support effect changes (e.g., weakness additions)

## Phase 4: Enricher Support

- [x] 4.1 Add damage enricher parsing
  - Convert `[[/damage N]]` to Foundry format
  - Support damage types

- [x] 4.2 Add healing enricher parsing
  - Convert `[[/heal N]]` to Foundry format

- [x] 4.3 Add apply effect enricher parsing
  - Convert `[[/apply condition]]` to Foundry format
  - Support conditions: prone, slowed, weakened, etc.

- [x] 4.4 Add lookup and embed enricher support
  - Support `[[/lookup @name]]`
  - Support `@Embed[uuid]`

## Phase 5: Output Handling

- [x] 5.1 Implement file output
  - Create directory structure: `output/Monsters/{CreatureName}/`
  - Write JSON file: `npc_{CreatureName}_{actorId}.json`

- [x] 5.2 Implement clipboard output option
  - Allow users to copy JSON to clipboard

- [x] 5.3 Implement `both` format mode
  - Generate Markdown stat block
  - Generate Foundry JSON file
  - Output both to user

- [x] 5.4 Implement role-based token images
  - Map monster role to Draw Steel image path
  - Set `img` field to role-based image
  - Supported roles: Ambusher, Artillery, Brute, Controller, Defender, Harrier, Hexer, Mount, Support

- [x] 5.5 Implement prototype token configuration
  - Set token name matching actor name
  - Set displayName and displayBars to 20
  - Configure bar1.attribute to "stamina"
  - Set width and height (typically 1x1)
  - Set disposition to -1 (hostile)
  - Configure texture with role-based image path
  - Set token texture properties (anchor, fit, scale)
  - Configure light and sight settings

- [x] 5.6 Implement negotiation fields
  - Set default interest and patience values (5)
  - Set impression value (1)
  - Initialize empty motivations and pitfalls arrays

## Phase 6: Future Enhancement - AI Image Generation

- [ ] 6.1 Add `--generate-image` flag to skill interface
  - Check if model supports image generation
  - Fall back to role-based images if not supported

- [ ] 6.2 Implement image generation prompt
  - Create descriptive prompt based on monster name, role, keywords
  - Include style guidelines for Draw Steel aesthetic

- [ ] 6.3 Save generated image to output directory
  - Save as `{CreatureName}/portrait.png`
  - Update Foundry JSON to reference generated image

- [ ] 6.4 Handle image generation failures gracefully
  - Fall back to role-based images on error
  - Log warning when fallback occurs

## Phase 7: Testing and Validation

- [x] 7.1 Create test cases for each output format
  - Test Markdown output (existing)
  - Test Foundry JSON output (new)
  - Test both output (new)

- [x] 7.2 Validate generated JSON against Foundry schema
  - Verify actor structure matches Draw Steel module
  - Verify items have required fields
  - Test import to Foundry VTT (manual)

- [x] 7.3 Test all monster types and organizations
  - Minion, Horde, Platoon, Elite, Leader, Solo
  - All roles: Ambusher, Artillery, Brute, Controller, Defender, Harrier, Hexer, Mount, Support

- [x] 7.4 Test all ability types and effects
  - Main Action, Maneuver, Triggered, Free Triggered, Passive
  - Damage effects, condition effects, healing effects

- [x] 7.5 Test role-based image assignment
  - Verify correct image path for each role
  - Verify image field is set in actor

## Phase 8: Documentation

- [x] 8.1 Update SKILL.md with new format option
  - Document `--format` parameter
  - Provide usage examples

- [ ] 8.2 Add Foundry export examples to examples.md
  - Show example monster output in both formats
  - Demonstrate enricher usage

- [x] 8.3 Update templates.md if needed
  - Add any Foundry-specific templates

- [ ] 8.4 Document AI image generation (future enhancement)
  - Document `--generate-image` flag
  - Note model requirements and limitations

## Phase 9: Final Validation

- [ ] 9.1 Run full test suite
  - Ensure no regressions in existing functionality

- [ ] 9.2 Run lint and typecheck commands
  - Verify code quality

- [ ] 9.3 Validate OpenSpec
  - Run `openspec validate add-foundry-vtt-export --strict --no-interactive`
  - Archive proposal after approval
