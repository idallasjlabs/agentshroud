---
title: engine.py
type: module
file_path: gateway/runtime/engine.py
tags: [runtime, container-engine, abstract-base, docker, podman, apple-containers]
related: [[docker_engine.py]], [[podman_engine.py]], [[apple_engine.py]], [[compose_generator.py]]
status: documented
---

# engine.py

## Purpose
Defines the abstract base class `ContainerEngine` that all container runtime implementations must implement. Provides a unified interface for image lifecycle, container lifecycle, networking, volumes, and compose operations regardless of whether the underlying runtime is Docker, Podman, or Apple Containers.

## Responsibilities
- Define the canonical container management API as abstract methods
- Provide a `_run()` helper for invoking CLI commands via `subprocess.run` with consistent settings (timeout, text mode, captured output)
- Define the `ContainerInfo` dataclass as a common return type for container listing
- Enforce that all runtime implementations expose identical method signatures

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `ContainerInfo` | Dataclass | Lightweight container metadata: name, id, image, status, ports, labels, raw dict |
| `ContainerEngine` | Abstract Class | Interface contract for all container runtimes |

## Abstract Method Reference

| Method | Signature | Description |
|--------|-----------|-------------|
| `build` | `(dockerfile, tag, context, build_args) -> str` | Build an image; returns image id/tag |
| `pull` | `(image) -> str` | Pull image from registry |
| `push` | `(image) -> str` | Push image to registry |
| `run` | `(image, name, *, ports, volumes, networks, env, privileged, caps, seccomp, detach, read_only, no_new_privileges) -> str` | Start container; returns container id |
| `stop` | `(name, timeout) -> None` | Stop a running container |
| `rm` | `(name, force) -> None` | Remove a container |
| `pause` | `(name) -> None` | Pause a container |
| `unpause` | `(name) -> None` | Unpause a container |
| `ps` | `(all) -> list[ContainerInfo]` | List containers |
| `logs` | `(name, tail) -> str` | Retrieve container logs |
| `exec` | `(name, command) -> str` | Execute command inside container |
| `inspect` | `(name) -> dict` | Detailed container metadata |
| `network_create` | `(name, internal) -> str` | Create a network |
| `network_rm` | `(name) -> None` | Remove a network |
| `volume_create` | `(name) -> str` | Create a volume |
| `volume_rm` | `(name) -> None` | Remove a volume |
| `compose_up` | `(file, detach) -> str` | Start services from compose file |
| `compose_down` | `(file) -> str` | Stop services from compose file |
| `health_check` | `() -> bool` | True if runtime is available |

## Function Details

### ContainerEngine._run(cmd, check, capture, timeout)
**Purpose:** Shared subprocess runner. Called by all concrete implementations as `self._run([...])`.
**Parameters:** `cmd` (list[str]), `check` (bool, default True — raises on non-zero exit), `capture` (bool, default True), `timeout` (int, default 300s).
**Returns:** `subprocess.CompletedProcess`.

## Configuration / Environment Variables
- No direct environment variables; runtime selection is handled by [[config.py]]
- `_run()` timeout defaults to 300 seconds; long-running operations (large image builds) should pass a higher value

## Related
- [[docker_engine.py]]
- [[podman_engine.py]]
- [[apple_engine.py]]
- [[compose_generator.py]]
- [[config.py]]
