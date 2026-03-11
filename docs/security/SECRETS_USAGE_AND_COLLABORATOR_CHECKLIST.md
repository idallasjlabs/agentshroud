# Secrets Usage and Collaborator Checklist

## Executive Summary
This document lists the local secret-bearing files collaborators may need after cloning the repository, whether they are required or optional, and where each secret is used.

## Root `.env`
- Status: removed from the repository working setup
- Needed: no
- Notes: the active model-switch workflow uses `docker/.env`, not repo-root `.env`

## Collaborator Setup Checklist

### Required for standard Docker runtime
- [ ] `docker/secrets/gateway_password.txt`
  - Example: `docker/secrets/gateway_password.txt.example`
  - Used by:
    - `docker/docker-compose.yml`
    - `docker/scripts/start-agentshroud.sh`
    - `gateway/ingest_api/config.py`
    - `gateway/ingest_api/main.py`
    - `gateway/ingest_api/lifespan.py`
- [ ] `docker/secrets/telegram_bot_token_production.txt`
  - Example: `docker/secrets/telegram_bot_token_production.txt.example`
  - Used by:
    - `docker/docker-compose.yml`
    - `docker/scripts/start-agentshroud.sh`
    - `docker/scripts/colima-health-check.sh`
    - `scripts/deploy.sh`

### Required if using 1Password-backed secret retrieval
- [ ] `docker/secrets/1password_service_account`
  - Example: `docker/secrets/1password_service_account.example`
  - Used by:
    - `docker/docker-compose.yml`
    - `gateway/ingest_api/main.py`
    - `gateway/ingest_api/lifespan.py`
- [ ] `docker/secrets/1password_bot_email.txt`
  - Example: `docker/secrets/1password_bot_email.txt.example`
  - Used by:
    - `gateway/ingest_api/main.py`
    - `gateway/ingest_api/lifespan.py`
- [ ] `docker/secrets/1password_bot_master_password.txt`
  - Example: `docker/secrets/1password_bot_master_password.txt.example`
  - Used by:
    - `gateway/ingest_api/main.py`
    - `gateway/ingest_api/lifespan.py`
- [ ] `docker/secrets/1password_bot_secret_key.txt`
  - Example: `docker/secrets/1password_bot_secret_key.txt.example`
  - Used by:
    - `docker/docker-compose.yml`
    - `gateway/ingest_api/main.py`
    - `gateway/ingest_api/lifespan.py`

### Required if using external LLM providers
- [ ] `docker/secrets/anthropic_oauth_token.txt`
  - Example: `docker/secrets/anthropic_oauth_token.txt.example`
  - Used by:
    - `docker/docker-compose.yml`
    - `docker/scripts/start-agentshroud.sh`
    - `gateway/security/credential_injector.py`
- [ ] `docker/secrets/anthropic_api_key.txt`
  - Example: `docker/secrets/anthropic_api_key.txt.example`
  - Used by:
    - `docker/scripts/agentshroud-entrypoint.sh`
- [ ] `docker/secrets/openai_api_key.txt`
  - Example: `docker/secrets/openai_api_key.txt.example`
  - Used by:
    - `docker/docker-compose.yml`
    - `docker/scripts/start-agentshroud.sh`
    - `docker/scripts/agentshroud-entrypoint.sh`
    - `gateway/security/credential_injector.py`
- [ ] `docker/secrets/google_api_key.txt`
  - Example: `docker/secrets/google_api_key.txt.example`
  - Used by:
    - `docker/docker-compose.yml`
    - `docker/scripts/start-agentshroud.sh`
    - `gateway/security/credential_injector.py`

### Required for local model-profile persistence
- [ ] `docker/.env`
  - Example: `docker/.env.example`
  - Used by:
    - `scripts/switch_model.sh`
  - Notes: not a core secret file, but local/runtime-specific configuration written by the model switch script

### Optional local tooling
- [ ] `llm_settings/mcp-servers/github/.env`
  - Example: `llm_settings/mcp-servers/github/.env.example`
  - Used by:
    - `llm_settings/mcp-servers/github/github-mcp-wrapper.sh`
    - `llm_settings/mcp-servers/github/start-mcp.sh`
    - `llm_settings/mcp-servers/github/call-tool.sh`
    - `llm_settings/mcp-servers/github/test-mcp.sh`
    - `llm_settings/mcp-servers/github/test-github.sh`
- [ ] `blueteam_assesment/.blueteam_env`
  - Example: `blueteam_assesment/.blueteam_env.example`
  - Used by:
    - `blueteam_assesment/blueteam_test.py`
  - Notes: only needed for Blueteam Telegram testing

## Files intentionally not for collaborators
These are local/operator-only or legacy-sensitive files and should not be committed for collaborators:
- `tg_export_session.session`
- `secrets/pihole_password.txt`
- old repo-root `.env`

## Restore Priority After Clean Build
1. Restore `docker/secrets/*`
2. Restore `docker/.env` if using `scripts/switch_model.sh`
3. Restore `llm_settings/mcp-servers/github/.env` only if using GitHub MCP tooling
4. Restore `blueteam_assesment/.blueteam_env` only if running Blueteam tests
