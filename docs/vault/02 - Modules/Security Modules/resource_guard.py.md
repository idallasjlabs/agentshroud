---
title: resource_guard.py
type: module
file_path: gateway/security/resource_guard.py
tags: [security, resource-limits, dos-prevention, rate-limiting, monitoring, psutil]
related: [[subagent_monitor.py]], [[egress_monitor.py]], [[health_report.py]]
status: documented
---

# resource_guard.py

## Purpose
Monitors and enforces per-agent resource consumption limits for CPU time, memory, disk writes, open files, temporary files, and request rate to prevent denial-of-service conditions and runaway agent behavior.

## Threat Model
Defends against resource exhaustion attacks — both intentional (a compromised agent consuming unbounded CPU, memory, or disk to degrade the gateway) and unintentional (runaway loops or infinite recursion in agent code). Uses `psutil` for real system metrics, operates as a background async task with a 10-second polling interval, and fires configurable alert callbacks when system-wide thresholds are exceeded.

## Responsibilities
- Track per-agent resource baselines at request start time
- Enforce configurable limits on CPU seconds, memory (MB), disk writes (MB/min), temp file count, and request rate per minute
- Run a background async monitoring loop checking system-wide CPU and memory percentages
- Fire registered alert callbacks on threshold breaches
- Register, track, and clean up temporary files created by agents
- Expose usage statistics per agent and system-wide
- Provide a global singleton instance with a setup function for custom limits

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `ResourceGuard` | Class | Core guard; tracks usage per agent and enforces limits |
| `ResourceLimits` | Dataclass | Configurable limit values (CPU, memory, disk, files, requests, alert thresholds) |
| `ResourceUsage` | Dataclass | Current per-agent usage metrics snapshot |
| `get_resource_guard` | Function | Returns the global singleton `ResourceGuard` instance |
| `setup_resource_guard` | Function | Replaces the global instance with a custom-configured one |

## Function Details

### ResourceGuard.__init__(limits)
**Purpose:** Initializes usage dictionaries, captures baseline disk I/O stats, and starts the async background monitoring task if an event loop is running.
**Parameters:** `limits` — `ResourceLimits | None`

### ResourceGuard.check_resource(agent_id, resource_type, amount)
**Purpose:** Checks whether granting `amount` of `resource_type` would exceed the configured limit for `agent_id`. Maintains a 60-second sliding window for disk writes and request counts. Increments usage on success.
**Parameters:** `agent_id` (str), `resource_type` ("disk_writes_mb" | "temp_files" | "requests"), `amount` (int)
**Returns:** `tuple[bool, str]` — `(allowed, reason)`

### ResourceGuard.start_request_tracking(agent_id)
**Purpose:** Records the current CPU time, memory RSS, and open file count as the baseline for a new request from this agent.
**Parameters:** `agent_id` (str)
**Returns:** `agent_id` (str)

### ResourceGuard.check_cpu_limit(agent_id) / check_memory_limit(agent_id) / check_disk_write_limit(agent_id)
**Purpose:** Compare current process metrics against the baseline captured at `start_request_tracking`. Log warnings and return `False` if the limit is exceeded.
**Returns:** `bool` — `True` if within limit

### ResourceGuard.register_temp_file(agent_id, file_path)
**Purpose:** Records a temp file path under `agent_id`. Returns `False` and logs a warning if the per-agent temp file limit is reached.
**Parameters:** `agent_id` (str), `file_path` (str)
**Returns:** `bool`

### ResourceGuard.cleanup_temp_files(agent_id)
**Purpose:** Deletes all registered temp files for an agent from disk and clears the tracking list.
**Parameters:** `agent_id` (str)

### ResourceGuard.get_usage_stats(agent_id)
**Purpose:** Returns per-agent metrics if `agent_id` is provided, or system-wide stats (total agents, system CPU/memory percent, configured limits) if called with no argument.
**Returns:** `dict`

### ResourceGuard.add_alert_callback(callback)
**Purpose:** Registers a callable that receives an alert dict when system CPU or memory thresholds are breached.
**Parameters:** `callback` — `callable`

## Configuration / Environment Variables
- No environment variables; limits are set via `ResourceLimits` dataclass or the `setup_resource_guard()` function

## Default Limits

| Limit | Default Value |
|---|---|
| Max CPU seconds per request | 30.0 s |
| Max memory per agent | 512 MB |
| Max disk writes per minute | 100 MB |
| Max temp files per agent | 1,000 |
| Max open files per agent | 100 |
| Max requests per minute | 300 |
| CPU spike alert threshold | 80% |
| Memory spike alert threshold | 90% |

## Related
- [[subagent_monitor.py]]
- [[egress_monitor.py]]
- [[health_report.py]]
