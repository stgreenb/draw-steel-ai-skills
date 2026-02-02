# Draw Steel Monster Generator

Skill for generating Draw Steel TTRPG monsters with (optional) Foundry VTT JSON output. Compatible with Claude Code, OpenCode, and other LLM coding tools.

Don't have an LLM tool? Browse available options at [AgentSkills.io](https://agentskills.io/).

## Quick Start

### Web Interface (Recommended for non-technical users)

1. Install Docker and Docker Compose
2. Copy `webapp/.env.example` to `webapp/.env` and configure your LLM proxy
3. Run `docker-compose up -d` from the `webapp/` directory
4. Access the web interface at `http://localhost:8080`
5. Login with the credentials from your `.env` file

The web interface provides:
- Three generation modes: Create from idea, Convert from stat block, Fetch from URL
- Real-time markdown output with validation results
- Downloadable Foundry VTT JSON
- Split-view UI with AI thinking process display

### Claude Code / OpenCode

1. Copy `.claude/skills/draw-steel-monster-generator/` to your skills directory
2. Talk to your LLM using the example commands below

## What It Does

- Generates Draw Steel monsters using official Monster Basics formulas
- Converts monsters from other systems (D&D 5e, Pathfinder, etc.) - ignores source math, uses for inspiration only
- Creates and validates Foundry VTT-ready JSON for import

## Example Commands

```
"Create a Level 3 Griffin, Platoon, Harrier"
"Convert Slaad from D&D 5e, Level 5, Solo, Controller in foundry compatible json"
"Create a swarm of 10 Level 1 Giant Rats, Horde, Ambusher"
"Take this Pathfinder monster <insert monster block> and convert it to a level 3 elite in Draw Steel"
```

## Project Structure

```
.claude/
├── commands/
│   └── monster.md           # Slash command definition
├── skills/draw-steel-monster-generator/
│   ├── SKILL.md             # AI skill definition
│   └── scripts/
│       ├── generate_monster.py
│       └── validate_foundry_json.py  # Foundry JSON validator
└── output/                  # Generated monsters
```

## Validation (if Foundry Format is Requested)

The validator checks:
- Valid ability/distance/monster keywords
- Proper damageDisplay values (melee/ranged/"")
- Required villain actions for Solo/Leader monsters
- Malice costs appropriate for monster level
- Foundry schema compliance

## Web Interface

The web interface provides a user-friendly way to generate Draw Steel monsters without requiring LLM coding tools.

### Features

- **Three Generation Modes:**
  - Create from idea: Generate monsters from text descriptions
  - Convert from stat block: Convert D&D 5e, Pathfinder, or other system stat blocks
  - Fetch from URL: Import monster data from URLs

- **Output Formats:**
  - Markdown only: Human-readable format
  - JSON only: Foundry VTT-compatible JSON
  - Both: Display markdown and provide JSON download

- **Real-time Validation:**
  - Draw Steel validation rules applied to all generated monsters
  - Validation errors and warnings displayed in the UI
  - Supports the complete Draw Steel validation checklist

- **User Experience:**
  - Split-view layout with input, output, and thinking panels
  - Session-based authentication for 2-3 users
  - Rate limiting to respect LLM API limits
  - Responsive design for various screen sizes

### Setup

1. **Prerequisites:**
   - Docker and Docker Compose installed
   - OpenAI-compatible LLM proxy (LocalAI, vLLM, Ollama, etc.)

2. **Configuration:**
   ```bash
   cd webapp
   cp .env.example .env
   # Edit .env with your LLM proxy URL and credentials
   ```

3. **Environment Variables:**
    - `LLM_PROXY_URL`: Your LLM proxy endpoint (e.g., `http://localhost:7980/v1`)
    - `LLM_API_KEY`: API key for your LLM proxy (if required)
    - `OPENAI_MODEL`: Model to use (e.g., `gpt-4`)
    - `WEBAPP_USERNAME`: Login username (default: admin)
    - `WEBAPP_PASSWORD`: Login password (default: admin)
    - `PORT`: Web server port (default: 8080)
    - `LLM_PROVIDER_SELECTION`: Provider selection mode (`auto` or `manual`, default: `auto`)
    - `LLM_MAX_PARALLEL_PROVIDERS`: Max parallel providers to try (`0` = all, default: `5`)
    - `LLM_PROVIDER_LOG_FILE`: Path to health log file (default: `webapp/provider_health.log`)
    - `LLM_PROVIDER_REFRESH_INTERVAL`: Provider cache refresh in seconds (default: `300`)

4. **Run:**
   ```bash
   docker-compose up -d
   ```

5. **Access:**
   - Open `http://localhost:8080` in your browser
   - Login with credentials from `.env`

### LLM Proxy Options

The web interface requires an OpenAI-compatible LLM proxy. Popular options:

- **LocalAI:** Self-hosted, OpenAI-compatible
- **vLLM:** High-performance serving
- **Ollama:** Simple local LLM management
- Text Generation WebUI: Multi-backend support

See `webapp/.env.example` for configuration examples.

### Multi-Provider Support

The web interface supports multiple LLM providers for improved reliability:

- **Automatic Mode:** Tries multiple working models in parallel, uses first successful response
- **Manual Mode:** Select a specific model from the dropdown
- **Health Tracking:** Monitors provider success/failure rates automatically
- **Working Model Cache:** Identifies and caches models that work without authentication

**Provider Selection UI:**
- Dashboard includes a provider selector dropdown
- Shows working models count and total models available
- Displays which model was used after generation
- Supports automatic refresh of provider list

**Health Monitoring:**
- Success and failure rates tracked per model
- Response times logged for performance monitoring
- Health report available via `/api/providers/health` endpoint
- Logs written to `webapp/provider_health.log`

### Troubleshooting

- **LLM Connection Failed:** Verify `LLM_PROXY_URL` is correct and proxy is running
- **Authentication Failed:** Check `WEBAPP_USERNAME` and `WEBAPP_PASSWORD` in `.env`
- **Rate Limit Exceeded:** Wait for the reset time (10/hour, 50/day limits)
- **Validation Errors:** Review validation feedback and try again with clearer input
- **All Providers Failed:** Check health log at `webapp/provider_health.log` for details
- **No Working Models:** Run `python webapp/quick_health_check.py` to identify working models
- **Provider Discovery Failed:** Ensure your proxy supports `/v1/providers` endpoint
- **Slow Generation:** Try reducing `LLM_MAX_PARALLEL_PROVIDERS` or selecting a faster model manually

### SKILL.md Workflow Alignment

The web interface follows the exact SKILL.md workflow:
1. Always generates Foundry JSON internally first
2. Runs Draw Steel validation on all generated JSON
3. Converts validated JSON to markdown when markdown format is requested
4. Returns validation results (errors/warnings/success) with all output formats
5. Uses the complete Draw Steel validation checklist (22 validation checks)

This ensures feature parity with the CLI tool and consistent monster generation across all interfaces.
