---
title: All Dependencies
type: index
tags: [#type/index, #type/dependency]
related: ["[[fastapi]]", "[[presidio]]", "[[httpx]]", "[[pydantic]]", "[[agentshroud-gateway]]"]
status: active
last_reviewed: 2026-03-09
---

# All Dependencies

## Gateway Python Dependencies (`gateway/requirements.txt`)

| Package | Version | Type | Used For | Required By |
|---------|---------|------|---------|-------------|
| [[fastapi]] | `>=0.115.0,<1.0.0` | Framework | Async web framework, routing | [[main]], all routes |
| `uvicorn[standard]` | `>=0.34.0,<1.0.0` | Server | ASGI server | Container entrypoint |
| [[pydantic]] | `>=2.10.0,<3.0.0` | Validation | Config models, request models | [[config]], [[bot_config]], [[main]] |
| `pydantic-settings` | `>=2.0.0,<3.0.0` | Config | Settings management | [[config]] |
| [[presidio]] (`presidio-analyzer`) | `>=2.2.0,<3.0.0` | NLP | PII entity detection | [[sanitizer]] |
| `presidio-anonymizer` | `>=2.2.0,<3.0.0` | NLP | PII redaction/anonymization | [[sanitizer]] |
| `spacy` | `>=3.8.0,<4.0.0` | NLP | Language model for Presidio | [[sanitizer]] |
| `aiosqlite` | `>=0.20.0,<1.0.0` | Database | Async SQLite access | Ledger, audit store, approval DB |
| `aiohttp` | `>=3.9.0,<4.0.0` | HTTP | DNS management (legacy) | dns_blocklist |
| `websockets` | `>=14.0,<15.0` | WebSocket | Dashboard live updates | dashboard |
| `pyyaml` | `>=6.0.0,<7.0.0` | Config | YAML parsing | [[config]] `load_config()` |
| `python-multipart` | `>=0.0.18,<1.0.0` | Parsing | Multipart form data (photo uploads) | [[telegram_proxy]] |
| [[httpx]] | `>=0.28.0,<1.0.0` | HTTP | Async HTTP client | [[llm_proxy]], egress notifier |
| `pytest` | `>=8.0.0,<9.0.0` | Testing | Test runner | All `gateway/tests/` |
| `pytest-asyncio` | `>=0.24.0,<1.0.0` | Testing | Async test support | All async tests |
| `psutil` | `>=6.0.0,<7.0.0` | System | Process/resource monitoring | health report, resource guard |
| `docker` | `>=7.0.0,<8.0.0` | Docker | Docker daemon interaction | network validator, compose generator |

## Bot Node.js Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `openclaw` | `2026.3.2` | AI agent framework (Claude-powered) |
| `grammy` | (bundled with openclaw) | Telegram Bot API SDK |
| `playwright` | `1.50.1` | Browser automation |
| `bun` | `1.2.4` | JavaScript runtime (fast npm alternative) |

## System Binaries (in containers)

| Binary | Container | Purpose |
|--------|-----------|---------|
| `trivy` | Both | Container/image vulnerability scanning |
| `clamscan` / `clamdscan` | Both | Malware/antivirus file scanning |
| `freshclam` | Both | ClamAV virus DB updater |
| `op` (1Password CLI) | Both | Credential management |
| `openscap-scanner` | Both | SCAP compliance scanning |
| `ssh` | Gateway | SSHProxy remote execution |
| `uvicorn` | Gateway | ASGI server |

## Removed Dependencies (for security)

| Package | Reason |
|---------|--------|
| `python-jose` | CVE-2024-33663, CVE-2024-33664 — removed, was unused |
