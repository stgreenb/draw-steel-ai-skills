## 1. Update SKILL.md Examples

- [x] 1.1 Add "weapon" keyword to all strike ability examples
- [x] 1.2 Update target type from "creature" to "creatureObject" in strike examples
- [x] 1.3 Add charge keyword example with note that it's optional
- [x] 1.4 Fix breath/spew keywords to use `["area", "magic"]` pattern
- [x] 1.5 Add "custom" field examples for area targets
- [x] 1.6 Add maneuver type ability example
- [x] 1.7 Add freeTriggered type ability example
- [x] 1.8 Add none type ability example (for custom abilities)
- [x] 1.9 Enhance existing villain action guidance with usage rules (once per encounter, one per round, end of turn)
- [x] 1.10 Add guidance that examples should inspire unique creations, not be copied verbatim

## 2. Update Documentation Sections

- [x] 2.1 Update DO/DON'T table with new keyword rules
- [x] 2.2 Add ability type variety section with examples
- [x] 2.3 Update breath/spew keyword documentation
- [x] 2.4 Add note about "charge" keyword being optional
- [x] 2.5 Update target type documentation to emphasize "creatureObject"
- [x] 2.6 Add guidance about using examples as inspiration for creativity

## 3. Update Examples and Templates

- [x] 3.1 Update main JSON example with correct strike keywords
- [x] 3.2 Add charge attack example with "charge" keyword
- [x] 3.3 Add breath weapon example with `["area", "magic"]` keywords
- [x] 3.4 Add maneuver ability example
- [x] 3.5 Add freeTriggered ability example
- [x] 3.6 Add none type ability example

## 4. Validation

- [x] 4.1 Test that all examples have "weapon" keyword in strikes
- [x] 4.2 Test that all strike examples use "creatureObject" target type
- [x] 4.3 Test that breath/spew examples use `["area", "magic"]` keywords
- [x] 4.4 Test that area examples include "custom" field
- [x] 4.5 Test that examples include all ability types (main, maneuver, freeTriggered, none)
- [x] 4.6 Run validator on example JSON to ensure no errors

## 5. Testing

- [x] 5.1 Generate test monster using updated SKILL.md
- [x] 5.2 Verify generated monster has "weapon" keyword in strikes
- [x] 5.3 Verify generated monster uses "creatureObject" target type
- [x] 5.4 Verify generated breath/spew uses correct keywords
- [x] 5.5 Verify generated monster includes different ability types
- [x] 5.6 Verify generated monster uses unique names (not copied from examples)
- [x] 5.7 Test import to Foundry VTT (if available)

## Dependencies

- Tasks 1.1-1.10 must complete before tasks 2.1-2.6
- Tasks 2.1-2.6 must complete before tasks 3.1-3.6
- Tasks 3.1-3.6 must complete before tasks 4.1-4.6
- Tasks 4.1-4.6 must complete before tasks 5.1-5.7

## Parallelizable Work

- Tasks 1.1-1.10 can be done in parallel (independent sections of SKILL.md)
- Tasks 4.1-4.6 can be done in parallel (independent validation checks)
- Tasks 5.1-5.7 can be done in parallel (independent test scenarios)