# Recommended Root Inventory

## Keep at repository root

### Core project files
- `README.md`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `CHANGELOG.md`
- `LICENSE`

### Agent / tool context files
- `AGENTS.md`
- `CLAUDE.md`

### Active runtime / tooling config
- `agentshroud.yaml`
- `docker-compose.secure.yml`
- `docker-compose.sidecar.yml`
- `pytest.ini`
- `gitleaks.toml`
- `.gitignore`
- `.dockerignore`
- `.pre-commit-config.yaml`
- `.gitallowed`
- `.mcp.json`

## Okay to keep if actively used, but optional
- `docker-compose.yml` variants only if they are part of active workflows
- `.github/`, `.claude/`, `.codex/`, `.gemini/` directories
- `docker/`, `docs/`, `scripts/`, `gateway/`, `src/`, `web/`, `branding/`, `archive/`, `session-notes/`
- `memory-backups/` if runtime still bind-mounts it
- `memory-backups/` only if you want local backup logs/artifacts in-repo; otherwise move outside repo

## Should not return to root
- session notes
- todo files
- whitepapers / papers / plans / runbooks / issue logs
- generated caches (`__pycache__/`, `.pytest_cache/`, `.ruff_cache/`)
- generated outputs (`coverage.json`)
- secrets / session artifacts (`.env`, `tg_export_session.session`, secret files)
- backup tarballs

## Practical target root layout

### Files
- `README.md`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `CHANGELOG.md`
- `LICENSE`
- `AGENTS.md`
- `CLAUDE.md`
- `agentshroud.yaml`
- `docker-compose.secure.yml`
- `docker-compose.sidecar.yml`
- `pytest.ini`
- `gitleaks.toml`
- `.gitignore`
- `.dockerignore`
- `.pre-commit-config.yaml`
- `.gitallowed`
- `.mcp.json`
- `ROOT_INVENTORY_RECOMMENDED.md`

### Directories
- `.github/`
- `.claude/`
- `.codex/`
- `.gemini/`
- `archive/`
- `security_assessment/`
- `branding/`
- `browser-extension/`
- `chatbot/`
- `containers/`
- `dashboard/`
- `data/`
- `docker/`
- `docs/`
- `examples/`
- `gateway/`
- `llm_settings/`
- `memory-backups/`
- `memory-backups/` *(optional to keep in-repo)*
- `reviews/`
- `scripts/`
- `secrets/` *(ignored/local only; ideally absent in shared clones)*
- `session-notes/`
- `shortcuts/`
- `skills/`
- `src/`
- `web/`
- `whogoesthere/`
