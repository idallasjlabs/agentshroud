---
title: installer.py
type: module
file_path: gateway/web/installer.py
tags: [setup, installer, web]
related: [Runbooks/First Time Setup, Web & Dashboard/api.py]
status: documented
---

# installer.py

**Location:** `gateway/web/installer.py`
**Lines:** ~230

## Purpose

Web-based installer and setup wizard for AgentShroud. Provides HTTP endpoints for guiding first-time setup through a browser interface — generating auth tokens, validating config, testing connectivity.

## Key Features

- Auth token generation endpoint
- Config validation (checks `agentshroud.yaml` syntax and required fields)
- Secret file creation guidance
- Connectivity tests to external services (Anthropic, Telegram, 1Password)
- Setup completion detection

## Endpoints (Inferred)

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/setup` | Setup wizard HTML |
| POST | `/setup/token` | Generate auth token |
| POST | `/setup/validate` | Validate agentshroud.yaml |
| GET | `/setup/status` | Check if setup is complete |

## When Used

- Initial deployment (first-time-setup)
- After config reset
- When `auth_token` is not configured

## Related Notes

- [[Runbooks/First Time Setup]] — Manual setup procedure
- [[Web & Dashboard/api.py|api.py]] — Production management API
- [[Configuration/agentshroud.yaml]] — Config being validated
