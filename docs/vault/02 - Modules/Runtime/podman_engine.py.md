---
title: podman_engine.py
type: module
file_path: gateway/runtime/podman_engine.py
tags: [runtime, podman, rootless, selinux, container-engine, systemd]
related: [[engine.py]], [[docker_engine.py]], [[compose_generator.py]], [[security.py]]
status: documented
---

# podman_engine.py

## Purpose
Concrete `ContainerEngine` implementation backed by the Podman CLI. Largely CLI-compatible with Docker but adds rootless-by-default operation, SELinux volume label support (`:z`/`:Z`), auto-detection of the compose binary (`podman-compose` plugin or `podman compose`), and the ability to generate systemd unit files.

## Responsibilities
- Implement all `ContainerEngine` abstract methods using `podman` CLI commands
- Auto-detect whether `podman-compose` or `podman compose` is available for compose operations
- Automatically append `:z` SELinux label to volume mounts for shared SELinux context
- Parse Podman JSON output from `podman ps --format json` (handles both list and dict response shapes)
- Generate systemd unit files for containers via `podman generate systemd`
- Verify Podman availability via `podman info`

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `PodmanEngine` | Class | Podman CLI-backed container engine with rootless and SELinux support |

## Function Details

### PodmanEngine.__init__(cli)
**Purpose:** Initialize Podman engine and detect available compose implementation.
**Parameters:** `cli` (str, default `"podman"`).

### PodmanEngine._detect_compose()
**Purpose:** Check if `podman-compose` binary exists on PATH; fall back to `[podman, compose]`.
**Returns:** list[str] — compose command prefix.

### PodmanEngine.run(image, name, *, volumes, ...)
**Purpose:** Launch a container. Volumes get `:z` appended for SELinux shared label unless already `:ro` (in which case `:ro,z` is appended). All other flags mirror `DockerEngine.run()`.
**Returns:** Container ID string.

### PodmanEngine.ps(all)
**Purpose:** Run `podman ps --format json` and parse the JSON response. Handles both list-of-dicts and single-dict response formats, and both `Names`/`Name` and `Id`/`ID` field variants.
**Returns:** `list[ContainerInfo]`.

### PodmanEngine.generate_systemd(name)
**Purpose:** Podman-specific extension — generate a systemd unit file for managing the named container as a service.
**Parameters:** `name` (str).
**Returns:** str — systemd unit file content.

### PodmanEngine.compose_up(file, detach) / compose_down(file)
**Purpose:** Use the detected compose command (`podman-compose` or `podman compose`) to bring services up or down.

### PodmanEngine.health_check()
**Purpose:** Run `podman info` with a 10-second timeout; return True on success.
**Returns:** bool.

## Key Differences from DockerEngine

| Aspect | Docker | Podman |
|--------|--------|--------|
| Daemon | Required | None (daemonless) |
| Default user | root | Rootless (current user) |
| Volume SELinux | Manual | `:z` flag auto-applied |
| Compose | `docker compose` | `podman-compose` or `podman compose` |
| systemd units | Not built-in | `podman generate systemd` |
| Capabilities | Explicit drop | Rootless drops more by default |

## Configuration / Environment Variables
- `cli` constructor parameter — default `"podman"`
- `AGENTSHROUD_RUNTIME_SOCKET` — see [[config.py]] for socket path configuration

## Related
- [[engine.py]]
- [[docker_engine.py]]
- [[compose_generator.py]]
- [[security.py]]
