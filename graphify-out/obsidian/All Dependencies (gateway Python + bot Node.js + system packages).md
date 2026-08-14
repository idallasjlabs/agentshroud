---
source_file: "docs/vault/05 - Dependencies/All Dependencies.md"
type: "document"
community: "Bot Skill Config"
location: "gateway/requirements.txt"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Bot_Skill_Config
---

# All Dependencies (gateway Python + bot Node.js + system packages)

## Connections
- [[Dockerfile.gateway_1]] - `uses` [EXTRACTED]
- [[aiosqlite (≥0.20.0 — async SQLite driver for audit ledger and approval queue store)]] - `contains` [EXTRACTED]
- [[fastapi (≥0.115.0 — web framework for gateway API routing)]] - `contains` [EXTRACTED]
- [[httpx (≥0.28.0 — async HTTP client for proxying requests to external APIs)]] - `contains` [EXTRACTED]
- [[openclaw (Node.js — AI agent platform with MCP, skills, tools)]] - `contains` [EXTRACTED]
- [[playwright (Node.js — browser automation with Chromium)]] - `contains` [EXTRACTED]
- [[presidio-analyzer + presidio-anonymizer (≥2.2.0 — NER-based PII detection and redaction)]] - `contains` [EXTRACTED]
- [[psutil (≥6.0.0 — system monitoring for resource_guard.py)]] - `contains` [EXTRACTED]
- [[pydantic (≥2.10.0 — data validation and config models)]] - `contains` [EXTRACTED]
- [[pytest.ini (test configuration — cache_dir tmppytest_cache)]] - `uses` [EXTRACTED]
- [[python-josecryptography (≥3.3.0 — JWT token handling and HMAC operations)]] - `contains` [EXTRACTED]
- [[pyyaml (≥6.0.0 — parse agentshroud.yaml config file)]] - `contains` [EXTRACTED]
- [[uvicornstandard (≥0.34.0 — ASGI server for FastAPI, port 8080)]] - `contains` [EXTRACTED]
- [[websockets (≥14.0 — WebSocket server for approval queue and dashboard)]] - `contains` [EXTRACTED]

#graphify/document #graphify/EXTRACTED #community/Bot_Skill_Config