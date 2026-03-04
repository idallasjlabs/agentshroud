---
title: agent_isolation.py
type: module
file_path: gateway/security/agent_isolation.py
tags: [security, isolation, containers, docker, network-namespaces, shared-nothing]
related: ["[[Security Modules/drift_detector.py|drift_detector.py]]", "[[Security Modules/trust_manager.py|trust_manager.py]]", "[[Data Flow]]"]
status: documented
---

# agent_isolation.py

## Purpose
Manages the registry of per-agent container configurations and verifies isolation properties — ensuring each agent runs in its own network namespace and filesystem volume with hardened security settings.

## Threat Model
Agent-to-agent lateral movement — a compromised agent accessing another agent's network, filesystem, or process space due to shared resources. Also addresses container privilege escalation through weak security defaults (writable root filesystem, retained Linux capabilities, missing seccomp profiles).

## Responsibilities
- Maintain a registry (`AgentRegistry`) mapping agent IDs to `ContainerConfig` objects
- Verify that no two agents share a Docker network (network namespace isolation)
- Verify that no two agents share a Docker volume (filesystem isolation)
- Verify security hardening properties: read-only root filesystem, `no_new_privileges`, and capability dropping (`cap_drop: ALL`)
- Aggregate issues from network, volume, and security checks into a unified `verify_shared_nothing()` report
- Generate a valid Docker Compose configuration from the registry

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `IsolationStatus` | Enum | ISOLATED / SHARED / UNKNOWN / VIOLATION |
| `ContainerConfig` | Dataclass | Full container specification for one agent |
| `IsolationCheck` | Dataclass | Result of one isolation check: agent_id, status, issues, details |
| `AgentRegistry` | Class | In-memory registry; supports dict serialization |
| `AgentRegistry.register()` | Method | Add an agent's container config |
| `AgentRegistry.unregister()` | Method | Remove an agent |
| `AgentRegistry.to_dict()` | Method | Serialize to plain dict |
| `AgentRegistry.from_dict()` | Class method | Deserialize from dict |
| `IsolationVerifier` | Class | Runs isolation checks against a registry |
| `IsolationVerifier.verify_network_isolation()` | Method | Detects shared Docker networks |
| `IsolationVerifier.verify_volume_isolation()` | Method | Detects shared Docker volumes |
| `IsolationVerifier.verify_shared_nothing()` | Method | Combined network + volume + security check |
| `IsolationVerifier.generate_compose()` | Method | Outputs Docker Compose YAML structure |

## Function Details

### IsolationVerifier.verify_network_isolation()
**Purpose:** Walk all registered agents, detect if any two share the same Docker network name.
**Parameters:** None
**Returns:** `list[IsolationCheck]` — one entry per agent; status is VIOLATION if network is shared.
**Side effects:** None.

### IsolationVerifier.verify_volume_isolation()
**Purpose:** Detect if any two agents share the same Docker volume name.
**Returns:** `list[IsolationCheck]`
**Side effects:** None.

### IsolationVerifier.verify_shared_nothing()
**Purpose:** Merge network and volume checks with security property checks:
- `read_only_root` must be True
- `no_new_privileges` must be True
- `capabilities_drop` must contain `"ALL"`

**Returns:** `list[IsolationCheck]` with all issues aggregated. Status is VIOLATION if any issue exists.

### IsolationVerifier.generate_compose()
**Purpose:** Generate a complete Docker Compose v3.8 dict from the registry, with hardened defaults: internal bridge networks, read-only root, `no-new-privileges:true`, seccomp profile binding, and `cap_drop: ALL`.
**Returns:** dict suitable for `yaml.dump()`

## ContainerConfig Defaults

| Field | Default | Description |
|-------|---------|-------------|
| `image` | `agentshroud/agent:latest` | Container image |
| `cpu_limit` | `"1.0"` | CPU shares |
| `memory_limit` | `"512m"` | Memory limit |
| `read_only_root` | `True` | Root filesystem is read-only |
| `no_new_privileges` | `True` | Linux no-new-privileges flag |
| `seccomp_profile` | `"default"` | Seccomp profile name |
| `capabilities_drop` | `["ALL"]` | All capabilities dropped |
| `capabilities_add` | `[]` | No capabilities added by default |

## Mode: Enforce vs Monitor
This module is a verification layer, not a runtime enforcer. It reports violations but does not prevent container startup. Enforcement occurs at the Docker daemon level via the generated Compose configuration.

## Environment Variables
None. All configuration is supplied via `ContainerConfig` dataclass instances.

## Integration Notes
- `AgentRegistry.from_dict()` / `to_dict()` support persistence and hot-reload from configuration files.
- `generate_compose()` output should be diffed against the running Docker Compose state and fed to `drift_detector.py` for runtime change detection.
- The `IsolationVerifier` should be run at agent registration time and periodically as a health check.

## Related
- [[Data Flow]]
- [[Security Modules/drift_detector.py|drift_detector.py]]
- [[Security Modules/trust_manager.py|trust_manager.py]]
- [[Security Modules/env_guard.py|env_guard.py]]
