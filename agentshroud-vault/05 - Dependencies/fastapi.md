---
title: FastAPI
type: dependency
tags: [#type/dependency, #status/active]
related: ["[[main]]", "[[lifespan]]", "[[agentshroud-gateway]]"]
status: active
last_reviewed: 2026-03-09
---

# FastAPI

**Version:** `>=0.115.0,<1.0.0`
**Type:** Core async web framework

## What It Does

The web framework that powers the gateway. Provides async request handling, automatic OpenAPI documentation, dependency injection, middleware support, and WebSocket support.

## Where It's Used

- [[main]] — `app = FastAPI(title="AgentShroud Gateway", lifespan=lifespan)`
- All route modules in `gateway/ingest_api/routes/`
- WebSocket endpoints in dashboard

## Key Features Used

| Feature | How Used |
|---------|---------|
| `lifespan` context manager | All startup/shutdown orchestration in [[lifespan]] |
| `APIRouter` | Modular route groups (health, forward, approval, etc.) |
| `Depends()` | Auth dependency injection |
| `StreamingResponse` | LLM proxy SSE streaming |
| `Request` | Raw request access for proxy endpoints |
| `HTTPException` | Standardized error responses |

## What Breaks If Missing/Wrong Version

Gateway fails to start. `uvicorn` will crash during import.

## Install

```nix
# Nix/Home Manager:
python311Packages.fastapi
```
