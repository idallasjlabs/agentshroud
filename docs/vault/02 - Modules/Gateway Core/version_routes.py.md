---
title: version_routes.py
type: module
file_path: gateway/ingest_api/version_routes.py
tags: [version-management, approval-gate, fastapi, router, gateway-core]
related: [Gateway Core/main.py, Gateway Core/models.py, Architecture Overview]
status: documented
---

# version_routes.py

## Purpose
Exposes API routes for AgentShroud version management (upgrade, downgrade, rollback). All mutation operations require a pre-approved `approval_id` from the approval queue before execution. Read-only operations (current version, history, available versions, security review) require no approval.

## Responsibilities
- Provide read-only introspection of the current OpenClaw version and version history
- Gate all mutation operations (upgrade, downgrade, rollback) behind the approval queue
- Support dry-run mode for previewing changes without execution
- Delegate all actual version logic to `gateway.tools.agentshroud_manager`
- Mask credentials in version history output using `mask_credentials`

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `VersionRequest` | class | Pydantic request body for upgrade/downgrade/review operations |
| `RollbackRequest` | class | Pydantic request body for rollback (only needs `approval_id`) |
| `router` | `APIRouter` | FastAPI router mounted at `/api/v1/versions` with tag `versions` |
| `get_current_version` | async route | GET `/current` — returns installed version info |
| `get_version_history` | async route | GET `/history` — returns history with credentials masked |
| `get_available_versions` | async route | GET `/available` — lists available versions |
| `review_version` | async route | POST `/review` — runs security review for a target version |
| `upgrade_version` | async route | POST `/upgrade` — upgrades to target; requires `approval_id` unless dry-run |
| `downgrade_version` | async route | POST `/downgrade` — downgrades; requires `approval_id` unless dry-run |
| `rollback_version` | async route | POST `/rollback` — rolls back to previous; always requires `approval_id` |

## Function Details

### upgrade_version(request)
**Purpose:** Validates that `approval_id` is present for non-dry-run requests, then calls `upgrade(target_version, approval_id, dry_run)` from `agentshroud_manager`. Returns 422 if the manager returns `status="blocked"`.
**Parameters:** `request: VersionRequest`
**Returns:** dict from `agentshroud_manager.upgrade()`
**Raises:** HTTP 400 if `approval_id` missing for non-dry-run; HTTP 422 if manager blocks the change

### downgrade_version(request)
**Purpose:** Same approval gate and behavior pattern as `upgrade_version` but calls `downgrade()`.
**Raises:** HTTP 400 if `approval_id` missing; HTTP 422 if blocked

### rollback_version(request)
**Purpose:** Always requires `approval_id` (no dry-run support). Calls `rollback(approval_id)` from `agentshroud_manager`.
**Raises:** HTTP 400 if `approval_id` missing; HTTP 422 if rollback returns error status

### get_version_history()
**Purpose:** Fetches version history and passes any `security_review` fields through `mask_credentials()` before returning to the caller. Prevents sensitive data from appearing in history responses.

## VersionRequest Fields
- `target_version: str` — semver string (required)
- `approval_id: str | None` — required for mutations unless `dry_run=True`
- `dry_run: bool` — default False; allows preview without execution

## Environment Variables Used
- None directly — underlying `agentshroud_manager` may use environment variables

## Config Keys Read
- None at route level — auth is applied via `Depends(auth_dep)` in `main.py`

## Imports From / Exports To
- Imports: `gateway.tools.agentshroud_manager` (all version functions), FastAPI, Pydantic
- Imported by: [[Gateway Core/main.py]] as `version_router` (mounted at `/api/v1/versions` with gateway Bearer auth dependency)

## Known Issues / Notes
- Approval validation is enforced in the route itself, not delegated to the `agentshroud_manager`. If the manager's `upgrade()` is called directly (bypassing the route), the approval gate is not enforced.
- `rollback` does not support `dry_run` — there is no preview mode for rollback operations.
- `get_version_history` masks credentials in `security_review` fields only; other fields are returned as-is from the manager.
- The router is mounted with `dependencies=[Depends(auth_dep)]` in `main.py`, meaning all routes in this file require gateway Bearer token authentication.

## Related
- [[Gateway Core/main.py]]
- [[Architecture Overview]]
