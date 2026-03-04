---
title: fastapi
type: dependency
tags: [python, web, framework]
related: [Dependencies/All Dependencies, Gateway Core/main.py, Gateway Core/router.py]
status: documented
---

# FastAPI

**Version:** ≥0.115.0,<1.0.0
**Type:** Python web framework
**Used in:** Gateway container

## Purpose

FastAPI is the web framework that powers the AgentShroud gateway. It provides:
- HTTP and WebSocket routing
- Automatic request/response validation via Pydantic models
- OpenAPI/Swagger documentation generation
- Dependency injection for auth middleware
- Async request handling (critical for proxy performance)

## Where Used

| Module | Usage |
|--------|-------|
| `gateway/ingest_api/main.py` | Primary `FastAPI()` app instance, all route definitions |
| `gateway/web/api.py` | Management API router |
| `gateway/web/management.py` | Management commands router |
| `gateway/web/dashboard_endpoints.py` | Dashboard API router |
| `gateway/ingest_api/version_routes.py` | Version endpoint router |

## Key FastAPI Features Used

| Feature | Usage |
|---------|-------|
| `FastAPI()` | App instance with lifespan context manager |
| `@app.get/post/websocket` | Route decorators |
| `Depends()` | Auth dependency injection |
| `HTTPException` | Error responses (400, 401, 403, 429, 500) |
| `Request` | Raw request access for middleware |
| `WebSocket` | Real-time approval queue notifications |
| `APIRouter` | Modular route grouping |

## Related Notes

- [[Gateway Core/main.py|main.py]] — Primary FastAPI app
- [[Dependencies/pydantic]] — Request/response validation
- [[Dependencies/All Dependencies]] — Full dependency list
