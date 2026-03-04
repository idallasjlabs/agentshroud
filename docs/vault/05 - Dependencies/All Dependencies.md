---
title: All Dependencies
type: reference
tags: [dependencies, packages, python, nodejs]
related: [Configuration/Dockerfile.gateway, Configuration/Dockerfile.bot, Architecture Overview]
status: documented
---

# All Dependencies

## Gateway Python Dependencies (`gateway/requirements.txt`)

### Core Framework

| Package | Version | Purpose |
|---------|---------|---------|
| `fastapi` | ≥0.115.0,<1.0 | Web framework — API routing, request handling, WebSockets |
| `uvicorn[standard]` | ≥0.34.0,<1.0 | ASGI server running FastAPI |
| `pydantic` | ≥2.10.0,<3.0 | Data validation, config models |
| `pydantic-settings` | ≥2.0.0,<3.0 | Settings management from env vars |

### PII Detection

| Package | Version | Purpose |
|---------|---------|---------|
| `presidio-analyzer` | ≥2.2.0,<3.0 | Microsoft Presidio NER-based PII detection |
| `presidio-anonymizer` | ≥2.2.0,<3.0 | PII redaction (replaces detected entities) |
| `spacy` | ≥3.8.0,<4.0 | NLP engine for Presidio; model: `en_core_web_sm` |

### Data Storage

| Package | Version | Purpose |
|---------|---------|---------|
| `aiosqlite` | ≥0.20.0,<1.0 | Async SQLite driver for audit ledger |

### Authentication

| Package | Version | Purpose |
|---------|---------|---------|
| `python-jose[cryptography]` | ≥3.3.0,<4.0 | JWT token handling and HMAC operations |

### Networking

| Package | Version | Purpose |
|---------|---------|---------|
| `websockets` | ≥14.0,<15.0 | WebSocket server for approval queue / dashboard |
| `httpx` | ≥0.28.0,<1.0 | Async HTTP client for proxying requests to external APIs |

### Configuration

| Package | Version | Purpose |
|---------|---------|---------|
| `pyyaml` | ≥6.0.0,<7.0 | Parse `agentshroud.yaml` config file |

### Utilities

| Package | Version | Purpose |
|---------|---------|---------|
| `python-multipart` | ≥0.0.18 | Multipart form data parsing (FastAPI file uploads) |
| `psutil` | ≥6.0.0,<7.0 | System monitoring (resource_guard.py) |
| `docker` | Latest | Docker API client (runtime engine integration) |

### Testing

| Package | Version | Purpose |
|---------|---------|---------|
| `pytest` | ≥8.0.0,<9.0 | Test runner |
| `pytest-asyncio` | ≥0.24.0,<1.0 | Async test support |
| `eval-type-backport` | ≥0.2.0 | Python <3.10 compatibility |

---

## Bot / Docker Container Dependencies

### Node.js Packages (installed globally)

| Package | Version | Purpose |
|---------|---------|---------|
| `openclaw` | latest | AI agent platform (MCP, skills, tools) |
| `playwright` | latest | Browser automation (Chromium) |
| `bun` | latest | Fast JS runtime |

### System Packages (apt)

| Package | Purpose |
|---------|---------|
| `openssh-client` | SSH proxy connections |
| `git` | Git operations by agent |
| `curl` | Health checks, API calls |
| `gosu` | Privilege dropping |
| `clamav, clamav-daemon` | Malware scanning |
| `libopenscap25, openscap-scanner` | Compliance scanning |

### Installed from External Sources

| Tool | Version | Purpose |
|------|---------|---------|
| `1password-cli (op)` | v2.32.0 | Credential management |
| `trivy` | latest | Container vulnerability scanning |

---

## Dependency Notes

- [[Dependencies/fastapi]] — FastAPI details
- [[Dependencies/presidio-analyzer]] — PII detection engine
- [[Dependencies/spacy]] — NLP model
- [[Dependencies/aiosqlite]] — Async SQLite
- [[Dependencies/httpx]] — HTTP client
- [[Dependencies/python-jose]] — JWT/HMAC
- [[Dependencies/pydantic]] — Data validation
- [[Dependencies/openclaw]] — Agent platform
- [[Dependencies/playwright]] — Browser automation
- [[Dependencies/1password-cli]] — Secret management
- [[Dependencies/trivy]] — Vulnerability scanner
- [[Dependencies/clamav]] — Malware scanner

---

## Related Notes

- [[Configuration/Dockerfile.gateway]] — How packages are installed
- [[Configuration/Dockerfile.bot]] — Bot package installation
- [[Architecture Overview]] — How components use these dependencies
