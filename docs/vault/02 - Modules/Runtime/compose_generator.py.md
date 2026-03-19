---
title: compose_generator.py
type: module
file_path: gateway/runtime/compose_generator.py
tags: [runtime, compose, docker-compose, podman-compose, apple-containers, yaml-generation]
related: [[engine.py]], [[docker_engine.py]], [[podman_engine.py]], [[apple_engine.py]], [[security.py]]
status: documented
---

# compose_generator.py

## Purpose
Generates Docker/Podman Compose YAML files or Apple Containers shell scripts from a list of `ServiceDef` objects. Provides the default AgentShroud service definitions (gateway + openclaw) and handles runtime-specific differences such as Podman SELinux volume labels.

## Responsibilities
- Define `ServiceDef` dataclass for describing a service: image, build context, ports, volumes, environment, security options, health check, dependencies
- Provide `DEFAULT_SERVICES` list with pre-configured gateway and openclaw service definitions
- Generate `docker-compose.yml` / `podman-compose.yml` YAML via `generate_compose()`
- Apply Podman-specific `:z` SELinux label to volumes when `runtime="podman"`
- Auto-collect named volumes and network definitions from service specs
- Generate a `zsh` shell script for Apple Containers environments that lack compose support via `generate_apple_script()`
- Include security hardening options in generated compose: `no-new-privileges`, `cap_drop: ALL`, `cap_add: NET_BIND_SERVICE`, `read_only: true`

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `ServiceDef` | Dataclass | Service specification: image, build, ports, volumes, env, networks, depends_on, security_opt, cap_drop/add, healthcheck |
| `DEFAULT_SERVICES` | List | Pre-configured gateway and openclaw service definitions |
| `generate_compose` | Function | Generate YAML compose file for Docker or Podman |
| `generate_apple_script` | Function | Generate zsh start/stop script for Apple Containers |

## Function Details

### generate_compose(services, runtime)
**Purpose:** Build a `docker-compose.yml` / `podman-compose.yml` YAML string from `ServiceDef` objects. Adds Podman SELinux `:z` labels to volumes when `runtime="podman"`. Automatically collects all referenced networks and named volumes into top-level compose stanzas.
**Parameters:** `services` (list[ServiceDef] or None — uses `DEFAULT_SERVICES`), `runtime` (str, default `"docker"`).
**Returns:** YAML string.

### generate_apple_script(services)
**Purpose:** Generate a `zsh` script that implements `up`, `down`, and `status` actions for Apple Containers. Iterates services in dependency order for up and reverse order for down.
**Parameters:** `services` (list[ServiceDef] or None).
**Returns:** Executable shell script string.

## Default Service Configuration

### gateway service
| Setting | Value |
|---------|-------|
| Image | `agentshroud-gateway:latest` |
| Build | `gateway/Dockerfile` |
| Port | `127.0.0.1:8080:8080` (localhost only) |
| Volumes | `gateway-data:/app/data`, `agentshroud.yaml` (read-only) |
| Network | `agentshroud-internal` |
| Security | `no-new-privileges`, `cap_drop: ALL`, `cap_add: NET_BIND_SERVICE`, `read_only: true` |
| Health check | HTTP GET `http://127.0.0.1:8080/status` every 30s |

### openclaw service
| Setting | Value |
|---------|-------|
| Image | `agentshroud-openclaw:latest` |
| Build | `docker/Dockerfile.openclaw` |
| Port | `127.0.0.1:18789:18789` |
| Volumes | `openclaw-data:/home/node/.openclaw` |
| Network | `agentshroud-internal` |
| Depends on | `gateway` |
| Health check | `curl -f http://localhost:18789/api/health` every 30s |

## Configuration / Environment Variables
- No environment variables; runtime selection passed as `runtime` parameter to `generate_compose()`
- Output YAML uses compose schema version `3.8`

## Related
- [[engine.py]]
- [[docker_engine.py]]
- [[podman_engine.py]]
- [[apple_engine.py]]
- [[security.py]]
