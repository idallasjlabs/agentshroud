---
title: config.py
type: module
file_path: gateway/runtime/config.py
tags: [runtime, configuration, environment-variables, container-selection, rootless]
related: [[engine.py]], [[docker_engine.py]], [[podman_engine.py]], [[apple_engine.py]], [[security.py]]
status: documented
---

# config.py

## Purpose
Defines the `RuntimeConfig` dataclass for container runtime selection and behavior. Loaded from environment variables or a config dictionary. Controls which container engine is used (or triggers auto-detection), whether rootless mode is active, and the target compose file path.

## Responsibilities
- Load runtime configuration from environment variables via `from_env()`
- Load runtime configuration from a YAML-sourced dict via `from_dict()`
- Provide an `effective_rootless` property that resolves the rootless setting based on the selected runtime (Podman defaults to rootless; Docker and Apple do not)
- Log the loaded config at INFO level for traceability

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `RuntimeConfig` | Dataclass | Runtime selection configuration: runtime name, rootless flag, compose file path, socket path |

## Function Details

### RuntimeConfig.from_env()
**Purpose:** Read configuration from environment variables and return a populated `RuntimeConfig` instance.
**Parameters:** None.
**Returns:** `RuntimeConfig`.

### RuntimeConfig.from_dict(data)
**Purpose:** Parse configuration from a dictionary (e.g. the `runtime` section of a loaded YAML config file).
**Parameters:** `data` (dict).
**Returns:** `RuntimeConfig`.

### RuntimeConfig.effective_rootless (property)
**Purpose:** Resolve whether rootless mode should be used. If `rootless` is explicitly set, return that value. Otherwise, default to `True` for Podman and `False` for Docker/Apple.
**Returns:** bool.

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `AGENTSHROUD_RUNTIME` | None (auto-detect) | Force runtime: `docker`, `podman`, or `apple` |
| `AGENTSHROUD_ROOTLESS` | None (runtime default) | `true`/`1`/`yes` to enable; any other value to disable |
| `AGENTSHROUD_COMPOSE_FILE` | `docker-compose.secure.yml` | Path to the compose file to use |
| `AGENTSHROUD_RUNTIME_SOCKET` | None | Custom container runtime socket path |

## Rootless Resolution Table

| Runtime | `rootless` Set | `effective_rootless` |
|---------|---------------|---------------------|
| `podman` | not set | True (default) |
| `docker` | not set | False (default) |
| `apple` | not set | False (default) |
| Any | `true` | True |
| Any | `false` | False |

## Configuration / Environment Variables
- All configuration is environment-variable-driven (see table above)
- `AGENTSHROUD_ROOTLESS` parsing: `true`, `1`, `yes` → True; anything else → False

## Related
- [[engine.py]]
- [[docker_engine.py]]
- [[podman_engine.py]]
- [[apple_engine.py]]
- [[security.py]]
