---
title: docker_engine.py
type: module
file_path: gateway/runtime/docker_engine.py
tags: [runtime, docker, container-engine, compose]
related: [[engine.py]], [[podman_engine.py]], [[compose_generator.py]], [[security.py]]
status: documented
---

# docker_engine.py

## Purpose
Concrete `ContainerEngine` implementation backed by the Docker CLI (`docker` binary). Translates the abstract engine interface into `docker` CLI invocations, supporting full container lifecycle management, networking, volumes, and Docker Compose integration.

## Responsibilities
- Implement all `ContainerEngine` abstract methods using `docker` CLI commands
- Parse `docker ps --format "{{json .}}"` output into `ContainerInfo` objects
- Pass security options (`--security-opt=no-new-privileges`, `--read-only`, `--cap-add`, seccomp profiles) through the `run()` method
- Support Docker Compose via `docker compose -f <file> up/down`
- Verify Docker availability via `docker info`

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `DockerEngine` | Class | Docker CLI-backed container engine implementation |

## Function Details

### DockerEngine.run(image, name, *, ports, volumes, networks, env, privileged, caps, seccomp, detach, read_only, no_new_privileges)
**Purpose:** Launch a container with the specified configuration. Applies all security options when provided.
**Parameters:** All standard container run options including security hardening flags.
**Returns:** Container ID string (stdout of `docker run`).

### DockerEngine.ps(all)
**Purpose:** List containers by running `docker ps --format "{{json .}}"` and parsing each JSON line into a `ContainerInfo`.
**Returns:** `list[ContainerInfo]`.

### DockerEngine.inspect(name)
**Purpose:** Return full container metadata as a dict. Handles the case where `docker inspect` returns a list and unwraps the first element.
**Returns:** dict.

### DockerEngine.compose_up(file, detach)
**Purpose:** Run `docker compose -f <file> up [-d]`.
**Returns:** stdout string.

### DockerEngine.health_check()
**Purpose:** Run `docker info` with a 10-second timeout; return True on success.
**Returns:** bool.

### DockerEngine._cmd(*args, **kwargs)
**Purpose:** Convenience wrapper that prepends `self._cli` to args and returns stripped stdout.

## Docker Security Options Used

| Option | CLI Flag | Effect |
|--------|---------|--------|
| `no_new_privileges` | `--security-opt=no-new-privileges` | Prevent privilege escalation |
| `read_only` | `--read-only` | Read-only root filesystem |
| `seccomp` | `--security-opt seccomp=<profile>` | Syscall filtering |
| `caps` | `--cap-add <cap>` | Add individual capabilities |
| `privileged` | `--privileged` | Full host access (dangerous) |

## Configuration / Environment Variables
- `cli` constructor parameter — default `"docker"`; can be overridden to point to a different binary path

## Related
- [[engine.py]]
- [[podman_engine.py]]
- [[compose_generator.py]]
- [[security.py]]
