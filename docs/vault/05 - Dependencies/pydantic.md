---
title: pydantic
type: dependency
tags: [validation, models, python]
related: [Gateway Core/models.py, Gateway Core/config.py, Dependencies/All Dependencies]
status: documented
---

# Pydantic

**Package:** `pydantic` v2 + `pydantic-settings`
**Version:** ≥2.10.0,<3.0.0
**Used in:** Configuration models, request/response models throughout gateway

## Purpose

Data validation and serialization library. Used extensively to:
1. Define and validate all configuration models (from `agentshroud.yaml`)
2. Define request/response body models for all API endpoints
3. Enforce type safety at API boundaries

## Where Used

| Module | Usage |
|--------|-------|
| `gateway/ingest_api/config.py` | All configuration Pydantic models (`GatewayConfig`, `PIIConfig`, `RouterConfig`, etc.) |
| `gateway/ingest_api/models.py` | All API request/response models |
| `gateway/proxy/mcp_config.py` | MCP server configuration models |
| Nearly all security modules | Configuration and result models |

## Key Configuration Models

| Model | Purpose |
|-------|---------|
| `GatewayConfig` | Top-level gateway config |
| `PIIConfig` | PII detection settings |
| `LedgerConfig` | Audit ledger settings |
| `RouterConfig` | Multi-agent router |
| `SecurityConfig` | Security module modes |
| `ToolRiskConfig` | Tool risk tier classification |
| `ChannelsConfig` | Email/Telegram/iMessage permissions |

## Field Validators

Pydantic `@field_validator` is used extensively for:
- URL validation in `RouterConfig` (must be `http://localhost` or `http://openclaw`)
- Ensuring `default_url` doesn't point to external hosts

## v2 vs v1

Uses Pydantic v2 API (`model_validate`, `model_dump`, `@field_validator` not `@validator`). Code is NOT compatible with Pydantic v1.

## Related Notes

- [[Gateway Core/config.py|config.py]] — Primary config models
- [[Gateway Core/models.py|models.py]] — API request/response models
- [[Dependencies/All Dependencies]] — Full dependency list
