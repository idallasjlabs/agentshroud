---
title: subagent_monitor.py
type: module
file_path: gateway/security/subagent_monitor.py
tags: [security, subagent-oversight, trust, concurrency, audit, mcp]
related: [[session_security.py]], [[resource_guard.py]], [[token_validation.py]]
status: documented
---

# subagent_monitor.py

## Purpose
Tracks the lifecycle, concurrency, trust inheritance, and tool usage of sub-agents spawned within a session, providing an audit trail and optional hard enforcement of concurrency limits and trust-gated tool access controls.

## Threat Model
Addresses sub-agent proliferation and privilege escalation risks: a compromised or prompt-injected agent might spawn large numbers of sub-agents to bypass rate limits, or attempt to access high-privilege tools by delegating to a sub-agent that inherits inflated trust. The module enforces that trust cannot escalate through spawn chains — effective trust is the minimum of the parent's declared trust and the parent's own effective trust.

## Responsibilities
- Register sub-agent spawning events with parent lineage and trust levels
- Enforce configurable maximum concurrent sub-agents per session
- Track tool usage by sub-agents with required trust threshold checking
- Maintain an in-memory audit log of all lifecycle and tool usage events
- Support forced termination of individual agents or all agents in a session
- Expose flagged events (trust violations, limit breaches) separately from full audit log
- Operate in two modes: `monitor` (log only) or `enforce` (block on violations)

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `SubagentMonitor` | Class | Core oversight manager; tracks active agents and events per session |
| `SubagentMonitorConfig` | Dataclass | Configuration: `mode`, `max_concurrent_per_session`, `inherit_trust` |
| `SubagentInfo` | Dataclass | Per-agent record: IDs, session, parent trust, effective trust, spawn time |
| `SubagentEvent` | Dataclass | Audit log entry: timestamp, session_id, agent_id, event_type, details |
| `ToolCheckResult` | Dataclass | Result of a tool access check: `allowed`, `flagged`, `reason` |
| `SubagentEventType` | Enum | Event types: SPAWNED, TERMINATED, KILLED, TOOL_USED, TRUST_VIOLATION, LIMIT_EXCEEDED |

## Function Details

### SubagentMonitor.register_spawn(session_id, agent_id, parent_id, parent_trust)
**Purpose:** Registers a new sub-agent. Checks current concurrent count against the limit; in `enforce` mode raises `RuntimeError` if the limit is reached. Computes `effective_trust` as the minimum of `parent_trust` and the parent's own `effective_trust` (if the parent is itself a sub-agent), preventing trust escalation through spawn chains.
**Parameters:** `session_id`, `agent_id`, `parent_id` (all str), `parent_trust` (int)
**Returns:** `SubagentInfo`; raises `RuntimeError` in enforce mode if limit exceeded

### SubagentMonitor.deregister(session_id, agent_id)
**Purpose:** Removes a sub-agent from the active registry and logs a `TERMINATED` event.
**Parameters:** `session_id` (str), `agent_id` (str)

### SubagentMonitor.get_active(session_id)
**Purpose:** Returns a snapshot list of all currently active `SubagentInfo` records for the session.
**Returns:** `list[SubagentInfo]`

### SubagentMonitor.check_tool_usage(session_id, agent_id, tool_name, required_trust)
**Purpose:** Checks whether `agent_id`'s `effective_trust` meets `required_trust`. Logs `TRUST_VIOLATION` if not. In `enforce` mode, returns `allowed=False`; in `monitor` mode, returns `allowed=True` with `flagged=True`. Always logs a `TOOL_USED` event.
**Parameters:** `session_id`, `agent_id`, `tool_name` (str), `required_trust` (int, default 0)
**Returns:** `ToolCheckResult`

### SubagentMonitor.kill_all(session_id)
**Purpose:** Terminates all active sub-agents in the session, logging a `KILLED` event for each. Used for emergency shutdown.
**Parameters:** `session_id` (str)
**Returns:** `int` — number of agents killed

### SubagentMonitor.kill_agent(session_id, agent_id)
**Purpose:** Terminates a single sub-agent by ID and logs a `KILLED` event.

### SubagentMonitor.get_audit_log(session_id, agent_id)
**Purpose:** Returns all events for the session, optionally filtered to a specific agent.
**Returns:** `list[SubagentEvent]`

### SubagentMonitor.get_flagged_events(session_id)
**Purpose:** Returns only `TRUST_VIOLATION` and `LIMIT_EXCEEDED` events for a session. Used by alerting and health reporting pipelines.
**Returns:** `list[SubagentEvent]`

## Configuration / Environment Variables
- Configuration is passed via `SubagentMonitorConfig`; no environment variables
- `mode` — `"monitor"` (default) logs violations without blocking; `"enforce"` blocks and raises
- `max_concurrent_per_session` — default 20
- `inherit_trust` — default `True`; when `True`, effective trust propagates down spawn chains with minimum reduction

## Related
- [[session_security.py]]
- [[resource_guard.py]]
- [[token_validation.py]]
