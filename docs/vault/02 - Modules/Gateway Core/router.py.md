---
title: router.py
type: module
file_path: gateway/ingest_api/router.py
tags: [routing, multi-agent, httpx, forwarding, gateway-core]
related: [Gateway Core/main.py, Gateway Core/models.py, Architecture Overview, Data Flow]
status: documented
---

# router.py

## Purpose
Implements multi-agent routing for the AgentShroud gateway. Resolves which downstream agent container should receive sanitized content and forwards it via HTTP POST. Handles graceful degradation when agents are offline.

## Responsibilities
- Maintain a registry of configured agent targets (`AgentTarget` objects)
- Resolve the appropriate target agent for each `ForwardRequest` using a priority chain
- Forward sanitized content to agent containers over HTTP (30-second timeout)
- Handle agent offline, timeout, and HTTP error conditions gracefully
- Perform health checks against agent `/health` endpoints
- Expose the target list for management endpoints

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `RouterError` | exception | Raised when no valid routing target is found |
| `ForwardError` | exception | Raised when the HTTP forward to an agent fails |
| `MultiAgentRouter` | class | Main routing engine |
| `__init__` | method | Builds the target registry from `RouterConfig`; creates default and additional targets |
| `resolve_target` | async method | Determines which `AgentTarget` to use for a given request |
| `forward_to_agent` | async method | HTTP POST to the resolved agent's `/chat` endpoint |
| `health_check` | async method | Checks `/health` on one or all configured targets |
| `list_targets` | method | Returns all registered `AgentTarget` objects |

## Function Details

### resolve_target(request)
**Purpose:** Applies a four-priority routing chain to select the target agent.
**Priority order:**
1. Explicit `request.route_to` field — if the named target exists, use it; if not, log a warning and fall through
2. Metadata tag matching — not yet implemented, reserved for future enhancement
3. Content type matching — not yet implemented, reserved for future enhancement
4. Default target from `config.default_target`
**Parameters:** `request: ForwardRequest`
**Returns:** `AgentTarget`
**Raises:** `RouterError` if the default target is not found in the registry

### forward_to_agent(target, sanitized_content, ledger_id, metadata)
**Purpose:** Sends a JSON payload to `{target.url}/chat` via `httpx.AsyncClient` with a 30-second timeout. The payload contains the sanitized content, ledger ID, source, content type, and full metadata.
**Parameters:**
- `target: AgentTarget`
- `sanitized_content: str` — PII-redacted text
- `ledger_id: str` — ledger entry UUID for distributed tracing
- `metadata: dict[str, Any]`
**Returns:** `dict` — parsed JSON response from the agent
**Raises:**
- `ForwardError` on `ConnectError` (agent offline — expected in Phase 2)
- `ForwardError` on `TimeoutException`
- `ForwardError` on `HTTPStatusError`

### health_check(target)
**Purpose:** GETs `{target.url}/health` with a 5-second timeout. Updates `target.healthy` and `target.last_health_check` in place.
**Parameters:** `target: AgentTarget | None` — None checks all targets
**Returns:** `dict[str, Any]` keyed by target name

## Environment Variables Used
- None — routing configuration comes from `RouterConfig` (loaded from `agentshroud.yaml`)

## Config Keys Read
- `config.default_target` — name of the default agent target
- `config.default_url` — URL of the default target (typically `http://openclaw:18080`)
- `config.targets` — dictionary of additional target `{name: url}` pairs

## Imports From / Exports To
- Imports: [[Gateway Core/models.py]] (`AgentTarget`, `ForwardRequest`), `.config` (`RouterConfig`), `httpx`
- Imported by: [[Gateway Core/main.py]] (`MultiAgentRouter`, `ForwardError`)

## Known Issues / Notes
- Priority levels 2 (metadata tags) and 3 (content type matching) are stubbed with TODO comments — only explicit and default routing are active.
- `forward_to_agent` calls `{target.url}/chat` — this endpoint name is hard-coded. If the downstream agent changes its chat endpoint path, this must be updated here.
- Agent health state (`target.healthy`) is only updated when `health_check` is called explicitly; there is no background polling.
- `ConnectError` is caught and converted to `ForwardError` with a non-fatal warning. Content is logged to the ledger even when the agent is offline.
- The `httpx.AsyncClient` is created fresh for every call — no connection pooling at the router level.

## Related
- [[Gateway Core/main.py]]
- [[Gateway Core/models.py]]
- [[Architecture Overview]]
- [[Data Flow]]
