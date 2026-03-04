---
title: drift_detector.py
type: module
file_path: gateway/security/drift_detector.py
tags: [security, drift-detection, containers, configuration, sqlite, integrity]
related: ["[[Security Modules/agent_isolation.py|agent_isolation.py]]", "[[Security Modules/alert_dispatcher.py|alert_dispatcher.py]]", "[[Data Flow]]"]
status: documented
---

# drift_detector.py

## Purpose
Detects unauthorized changes to container configurations by comparing live container state against known-good baselines stored in SQLite. Alerts on changes to seccomp profiles, Linux capabilities, mounts, environment variables, container images, and security flags.

## Threat Model
Container configuration tampering — an attacker or misconfiguration silently modifying a container's security posture after deployment (e.g., adding capabilities, mounting new paths, switching to a privileged mode, or substituting the container image) without triggering a deployment event.

## Responsibilities
- Store known-good `ContainerSnapshot` baselines in SQLite with SHA-256 config hashes
- Perform fast hash comparison before detailed field-by-field diffing
- Detect and classify drift across 6 categories: seccomp profile, capabilities, mounts, env vars, image, security flags
- Assign severity to each drift alert: critical (seccomp change, added capabilities, privileged mode), high (new mounts, new env vars, image change, read-only disabled), medium (removed capabilities)
- Persist all drift alerts to SQLite with acknowledged status tracking
- Support alert retrieval by container, unacknowledged filter, and result limit
- Support alert acknowledgement workflow

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `ContainerSnapshot` | Dataclass | Point-in-time container config: seccomp, capabilities, mounts, env vars, image, flags |
| `ContainerSnapshot.config_hash()` | Method | SHA-256 of JSON-serialized config for fast comparison |
| `DriftAlert` | Dataclass | One detected drift: container_id, timestamp, category, description, baseline vs current values, severity |
| `DriftDetector` | Class | Main detector backed by SQLite |
| `DriftDetector.set_baseline()` | Method | Store or update a known-good snapshot |
| `DriftDetector.get_baseline()` | Method | Retrieve stored baseline for a container |
| `DriftDetector.check_drift()` | Method | Compare current snapshot against baseline; return DriftAlerts |
| `DriftDetector.get_alerts()` | Method | Query stored alerts with filters |
| `DriftDetector.acknowledge_alert()` | Method | Mark an alert as acknowledged |

## Function Details

### DriftDetector.set_baseline(snapshot)
**Purpose:** Store (or replace) the known-good configuration for a container.
**Parameters:** `snapshot` (ContainerSnapshot)
**Returns:** str — the config hash (SHA-256 hex digest)
**Side effects:** Writes to `baselines` table.

### DriftDetector.check_drift(current)
**Purpose:** Compare `current` snapshot against the stored baseline. Uses `hmac.compare_digest()` for timing-safe hash comparison — if hashes match, returns empty list immediately. Otherwise performs field-by-field comparison.
**Parameters:** `current` (ContainerSnapshot)
**Returns:** `list[DriftAlert]` — empty if no baseline exists or no drift detected; one alert per difference found.
**Side effects:** Inserts all generated alerts into `drift_alerts` table.

### DriftDetector.get_alerts(container_id, unacknowledged_only, limit)
**Purpose:** Query drift alerts with optional filters.
**Parameters:**
- `container_id` (str | None) — filter to one container
- `unacknowledged_only` (bool) — filter to unacknowledged alerts
- `limit` (int, default 100) — max results
**Returns:** `list[dict]` — each entry has keys: id, container_id, timestamp, category, description, baseline_value, current_value, severity, acknowledged.

### DriftDetector.acknowledge_alert(alert_id)
**Purpose:** Mark a specific alert as acknowledged (acknowledged=1) in the DB.
**Returns:** bool — True if a row was updated.

### ContainerSnapshot.config_hash()
**Purpose:** Produce a deterministic SHA-256 hash of the snapshot config using `json.dumps(sort_keys=True)` for canonical serialization.
**Returns:** str (64-character hex digest)

## Drift Categories and Severity

| Category | Description | Severity |
|----------|-------------|----------|
| `seccomp` | Seccomp profile name changed | critical |
| `capabilities` | New capabilities added | critical |
| `capabilities` | Capabilities removed | medium |
| `mounts` | New mount points detected | high |
| `env` | New environment variables | high |
| `image` | Container image changed | high |
| `security` | Container is now privileged | critical |
| `security` | Root filesystem is no longer read-only | high |

## Configuration

| Parameter | Default | Description |
|-----------|---------|-------------|
| `db_path` | `":memory:"` | SQLite path; use file path for persistence |

WAL journal mode is enabled when using a file-backed database.

## Database Schema
Two tables:
- `baselines` — one row per container: container_id, snapshot_json, config_hash, created_at, updated_at
- `drift_alerts` — append-only: id, container_id, timestamp, category, description, baseline_value, current_value, severity, acknowledged

## Mode: Enforce vs Monitor
This module detects and records drift; it does not enforce remediation. The `check_drift()` method always runs in full-check mode. The caller (e.g., a health monitor or scheduled task) decides whether to alert, quarantine, or restart the container based on returned `DriftAlert` objects.

## Environment Variables
None. SQLite path is set at instantiation.

## Related
- [[Data Flow]]
- [[Security Modules/agent_isolation.py|agent_isolation.py]]
- [[Security Modules/alert_dispatcher.py|alert_dispatcher.py]]
