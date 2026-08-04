# Scripts

Automation scripts used by the AI Engineering OS.

---

## Project-Level Deployment

| Script | Purpose |
|--------|---------|
| `llm-init.sh` | Deploy Claude, Gemini, Codex, and Copilot configs into any repo |

Run from the target repository:
```bash
source /path/to/llm_settings/.llm_settings/scripts/llm-init.sh
llm-init --mcp github-fluence --mcp atlassian-fluence --mcp aws .
```

---

## Global Tool Deployment (opt-in)

The following scripts deploy to user-global config directories. They are **separate
from `llm-init.sh`** (project-level) and only run when the respective tool is installed.

| Script | Tool | Deploys to | Run when |
|--------|------|-----------|----------|
| `deploy-crush.sh` | Crush (Charmbracelet) | `~/.config/crush/skills/` | After installing Crush or updating skills |
| `deploy-opencode.sh` | OpenCode (SST) | `~/.config/opencode/agents/` | After installing OpenCode or updating agents |

### Crush — key constraint

Crush validates that `name:` in each `SKILL.md` frontmatter must **exactly match**
the skill's directory name (e.g., `name: i-aws` for `~/.config/crush/skills/i-aws/`).
`deploy-crush.sh` enforces this automatically — do not set `name: aws` in dir `i-aws`.

### Running

```bash
# Deploy development skill profile to Crush (default profile)
bash .llm_settings/scripts/deploy-crush.sh

# Deploy all skills to Crush
bash .llm_settings/scripts/deploy-crush.sh --skills all

# Preview without writing (works even if Crush is not installed)
bash .llm_settings/scripts/deploy-crush.sh --skills development --dry-run

# Deploy OpenCode agents
bash .llm_settings/scripts/deploy-opencode.sh

# Preview OpenCode deployment
bash .llm_settings/scripts/deploy-opencode.sh --dry-run
```

### What these scripts do NOT touch

- `~/.config/crush/crush.json` — device-specific (providers, MCP servers, API keys)
- `~/.config/opencode/opencode.json` — device-specific (model assignments, agent wiring)
