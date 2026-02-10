# Project Context

## Purpose
The Draw Steel Monster Generator is a multi-platform AI Skill that generates mechanically-sound, thematically-appropriate Draw Steel TTRPG monsters from mythological creatures. It eliminates manual monster math by automating all calculations, ensuring 100% Draw Steel compliance. The skill works natively across OpenCode (primary), Claude Code, Claude Web, AnythingLLM, and FoundryVTT with a single codebase powering all platforms.

**Key Value Propositions:**
- Eliminates manual monster math (formulas automated)
- 100% Draw Steel compliance verified
- Multi-platform support (OpenCode primary, Claude Code, Claude Web, AnythingLLM, FoundryVTT)
- Zero infrastructure required
- Single GitHub repo powers all platforms

## Tech Stack
- **Core Calculation:** Python 3.8+ (stat calculations, formula implementation)
- **AI Skill Format:** SKILL.md (OpenCode, Claude Code, Claude Web instructions)
- **Platform Wrappers:** Node.js 18+ (AnythingLLM handler)
- **Output Formats:** YAML/Markdown, JSON (FoundryVTT), text (importer-compatible)
- **Testing:** Python unit tests, Jest (JavaScript), cross-platform validation
- **Platform Targets:**
  - OpenCode CLI/Web (native primary)
  - Claude Code (compatible secondary)
  - Claude Web UI (compatible)
  - AnythingLLM (JavaScript wrapper)
  - Gemini CLI (MCP server or CLI wrapper)
  - FoundryVTT (JSON export via draw-steel-monster-importer)

## Project Conventions

### Code Style
- **Python:** PEP 8 compliant, clear docstrings, type hints where appropriate
- **JavaScript:** ES6+, async/await patterns, clear error handling
- **File Naming:** snake_case for Python scripts, camelCase for JavaScript, UPPER_CASE for constants
- **Comments:** Explain "why", not "what" - code should be self-documenting
- **Function Names:** Descriptive verbs (calculate_ev, calculate_stamina, validate_input)
- **No Hardcoded Values:** Use enums and constants from keywords.json and formulas.md

### Architecture Patterns
- **Modular Design:** Separate concerns (calculations vs. instructions vs. platform wrappers)
- **Single Source of Truth:** Core Python formulas used by all platforms
- **Plugin Architecture:** Platform-specific files at root (plugin.json, handler.js, package.json)
- **Subprocess Pattern:** AnythingLLM handler calls Python scripts via spawn()
- **Single Repository Strategy:** All platforms in one repo for easier maintenance
- **Schema-Driven Output:** All JSON exports use structured schemas (FoundryVTT actor format)
- **Stateless Functions:** All calculation functions are pure (no side effects)

### Testing Strategy
- **Phase 1 (Claude Code/Web):**
  - 20 mythological creatures generated
  - 100% compliance with formulas
  - 5-10 user acceptance tests
  - Installation test (<5 min setup)
- **Phase 2 (OpenCode/AnythingLLM):**
  - OpenCode CLI + web IDE discovery
  - AnythingLLM plugin invocation (Docker + self-hosted)
  - Cross-platform regression testing
  - 10+ user acceptance tests per platform
- **Phase 3 (FoundryVTT/Gemini):**
  - FoundryVTT v12/v13 import tests
  - draw-steel-monster-importer compatibility
  - Gemini CLI invocation tests
  - End-to-end workflows (generation → export → import → use)
- **Unit Tests:** All formula calculations tested independently
- **Performance Targets:** Generation <30 sec, token usage <3K, JSON export <50 KB

### Git Workflow
- **Version Control:** Semantic versioning (v1.0.0, v1.1.0, v2.0.0)
- **Release Tags:**
  - v1.0.0: Phase 1 (OpenCode primary + Claude Code/Web compatible)
  - v1.1.0: Phase 2 (Claude Code full integration)
  - v1.2.0: Phase 3 (AnythingLLM + Gemini CLI)
  - v2.0.0: Phase 4 (FoundryVTT + Gemini)
- **Branching Strategy:** Main branch for releases, feature branches for platform-specific work
- **Commit Messages:** Conventional commits (feat:, fix:, docs:, refactor:)
- **Changelog Format:** Markdown with Added/Changed/Fixed sections per release

## Domain Context

### Draw Steel TTRPG System
- **Core Mechanics:** EV (Enemy Value), Stamina, Free Strike, Damage Tiers (T1/T2/T3)
- **Organizations (6 types):** Minion, Horde, Platoon, Elite, Leader, Solo
- **Roles (9 types):** Ambusher, Artillery, Brute, Controller, Defender, Harrier, Hexer, Mount, Support
- **Creature Keywords:** Animal, Beast, Construct, Dragon, Elemental, Fey, Giant, Horror, Humanoid, Infernal, Ooze, Plant, Soulless, Swarm, Undead
- **Damage Types:** acid, cold, corruption, fire, holy, lightning, poison, psychic, sonic
- **Conditions:** Bleeding, Dazed, Frightened, Grabbed, Prone, Restrained, Slowed, Taunted, Weakened
- **Ability Keywords:** Strike, Magic, Weapon, Psionic, Area

### Compliance Formulas (GOLDEN RULE: All values MUST come from formulas)
```
EV = (2 × Level) + Org_EV_Offset
Org offsets: Minion=-2, Horde=0, Platoon=+1, Elite=+2, Leader=+3, Solo=+4

Stamina = (10 × Level + Role_Stamina_Offset) × Org_Stamina_Multiplier
Org multipliers: Minion=0.5×, others=1.0×, Solo=1.5×
Role stamina offsets vary; see formulas.md

Free Strike = 2 + (Level / 2)

Damage(Tier) = (4 + Level + Role_Damage_Mod) × Tier_Multiplier × Org_Damage_Multiplier
Tier multipliers: T1=1.0×, T2=1.5×, T3=2.0×
Org damage multipliers: Minion=0.5×, others=1.0×, Solo=1.5×
```

### Ability Generation Patterns
- **Signature Ability:** 1 per monster, reflects creature theme
- **Secondary Abilities:** 2-3 additional abilities
- **Tier Structure:** All abilities have T1/T2/T3 damage variants
- **Conditions:** 0-2 conditions per tier (from fixed list)
- **Power Rolls:** Based on characteristics (might, agility, reason, intuition, presence)

## Important Constraints

### Platform-Specific Constraints
- **OpenCode:** Dual-path support required (`.opencode/` + `.claude/`), SKILL.md must support `compatibility` field with "opencode-agent" first
- **Claude Code/Web:** No browser storage (localStorage/sessionStorage unavailable), Python execution available (Claude Code only)
- **AnythingLLM:** Custom skills must be JavaScript (Node.js), ALL functions MUST return strings (JSON stringified), Python subprocess calls via spawn() or exec(), Must work in Docker + self-hosted environments
- **FoundryVTT:** Actor JSON structure must match v12+ schema, Compatible with Custom System Builder (flexible) and native Draw Steel system (strict), Import via draw-steel-monster-importer (text format)
- **Gemini CLI:** Requires MCP server or standalone wrapper, No direct SKILL.md support (unlike Claude)

### Technical Constraints
- **Python Version:** 3.8+ required
- **Node.js Version:** 18.0.0+ required for AnythingLLM wrapper
- **No Hardcoded Values:** All damage/stamina/EV values MUST be calculated via formulas
- **No D&D Terms:** NEVER use D&D terminology. Specifically prohibited:
  - "vs. AC" (no Armor Class in Draw Steel)
  - "Armor Class", "defense roll", "defense value" (no defensive stat)
  - "HP", "hit points" (use "Stamina" only)
  - "d20" (Draw Steel uses 2d10)
  - "DC", "Difficulty Class" (not used in Draw Steel)
- **Return Value Format:** AnythingLLM requires stringified JSON (not objects)
- **Subprocess Timeout:** 30-second timeout for Python subprocess calls
- **JSON Schema:** Must match FoundryVTT v12/v13 actor structure for exports
- **Token Budget:** Target <3K tokens per generation (40-60% below raw prompt)

### Business Constraints
- **Single Codebase:** Maintain multi-platform support in one repository
- **Zero Infrastructure:** No backend servers or databases required
- **Open Source:** MIT license for all code
- **Installation Time:** <5 minutes for all platforms
- **Compliance Rate:** 100% Draw Steel rule compliance mandatory

## External Dependencies

### Platform Installation Paths
- **OpenCode CLI:** `~/.config/opencode/skills/draw-steel-monsters/` (auto-scanned)
- **OpenCode Web:** `.opencode/skills/draw-steel-monsters/` (repo-local, auto-discovers)
- **Claude Code:** `~/.claude/skills/draw-steel-monsters/` (auto-scanned on startup)
- **Claude Web:** Upload via UI (manual, no Python execution)
- **AnythingLLM:** `$STORAGE_DIR/plugins/agent-skills/draw-steel-monsters/` (requires restart)
- **FoundryVTT:** Import JSON via UI or use draw-steel-monster-importer macro
- **Gemini CLI:** Standalone wrapper or MCP server (TBD)

### Key External Systems
- **Draw Steel Compendium:** https://steelcompendium.io/ (official rule reference)
- **draw-steel-monster-importer:** GitHub: kenpoh01/draw-steel-monster-importer (FoundryVTT import macro)
- **OpenCode Docs:** https://opencode.ai/docs/skills/ (skill format reference)
- **Claude Skills:** https://code.claude.com/docs/en/skills (Claude Code skill format)
- **AnythingLLM Docs:** https://docs.anythingllm.com/agent/custom/developer-guide (custom skill reference)
- **FoundryVTT API:** https://foundryvtt.com/api/v11/ (actor JSON structure reference)

### Phase Rollout Plan
- **Phase 1 (Weeks 1-6):** MVP for OpenCode (primary) + Claude Code/Web compatibility
- **Phase 2 (Weeks 7-8):** Claude Code full integration
- **Phase 3 (Weeks 9-18):** AnythingLLM + Gemini CLI wrappers
- **Phase 4 (Weeks 19+):** FoundryVTT JSON export + Gemini CLI

### Success Metrics
- **Phase 1:** 50+ GitHub stars, 50+ OpenCode users, 100% compliance, ≥4.0/5.0 satisfaction
- **Phase 2:** 25+ Claude Code users, cross-platform compatibility verified, ≥2 platforms tested
- **Phase 3:** 15+ AnythingLLM installations, ≥3 platforms tested, 3+ output formats
- **Phase 4:** 50+ FoundryVTT imports, 10+ Gemini CLI users, 300+ total users, 200+ GitHub stars
