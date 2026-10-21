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

> **Per-repo alternative:** `llm-init` now also deploys OpenCode, Crush, Antigravity (`agy`),
> Grok Build, Pi and Oh My Pi into each repo (`--tools`, default all) — skills, agents and the
> MCP servers selected with `--mcp`. These two global scripts remain for installing into your
> home config; they are not required for the per-repo deployment. See
> [`../docs/MCP_README.md`](../docs/MCP_README.md) §10.

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

---

## Security (`security/`)

Credential storage and resolution for every MCP wrapper under `mcp-servers/` —
zero manual approval at every tier (no Touch ID, no password dialog, no `op`
sign-in prompt), so wrappers work identically from an interactive shell or an
unattended launchd/systemd/cron/SSH context.

| Script | Purpose | Run when |
|--------|---------|----------|
| `resolve-cred.sh` | Shared resolver every MCP wrapper calls internally (OS-native store → 1Password). Not normally run directly. | N/A — called by wrapper scripts |
| `setup-keychain.sh` | Populate macOS Keychain with the full MCP secret catalog | Once per Mac |
| `setup-linux-keyring.sh` | Ubuntu-LTS equivalent of `setup-keychain.sh` (gnome-keyring/libsecret, systemd --user lingering session) | Once per Linux account that needs it — per-user opt-in, not fleet-wide; accounts that skip this fall through to `.env` |
| `setup-op-account.sh` | Store a 1Password Service Account token so `resolve-cred.sh`'s 1Password tier can activate non-interactively | Once per account, only if 1Password fallback is wanted |

Resolution order for any given secret (see each wrapper script's own header for
its exact keychain-service/account/op-reference):

1. Environment variable already exported
2. `.env` file in the wrapper's own directory
3. OS-native store — Keychain (macOS) or `secret-tool`/gnome-keyring (Linux)
4. 1Password — **only** if reachable without any prompt (Service Account token,
   or an already-authenticated `op` session); never triggers a new sign-in

```bash
# macOS, once per machine:
bash .llm_settings/scripts/security/setup-keychain.sh

# Linux, once per account that needs it:
sudo bash .llm_settings/scripts/security/setup-linux-keyring.sh --install
     bash .llm_settings/scripts/security/setup-linux-keyring.sh --init
     bash .llm_settings/scripts/security/setup-linux-keyring.sh --migrate
     bash .llm_settings/scripts/security/setup-linux-keyring.sh --verify

# Either OS, optional — enables the 1Password fallback tier:
bash .llm_settings/scripts/security/setup-op-account.sh 'ops_xxxxxxxxxxxx'
```
