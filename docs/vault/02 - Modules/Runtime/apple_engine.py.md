---
title: apple_engine.py
type: module
file_path: gateway/runtime/apple_engine.py
tags: [runtime, apple-containers, macos, vm-isolation, apple-silicon]
related: [[engine.py]], [[docker_engine.py]], [[compose_generator.py]], [[security.py]]
status: documented
---

# apple_engine.py

## Purpose
Concrete `ContainerEngine` implementation backed by Apple Containers (`container` CLI, macOS 26+). Each container runs in a lightweight hardware-isolated virtual machine. Compose is not supported — use `compose_generator.generate_apple_script()` instead. Security flags like `--privileged` and `--seccomp` are not applicable because VM isolation provides stronger boundaries.

## Responsibilities
- Implement all `ContainerEngine` abstract methods using Apple's `container` CLI
- Parse Apple Containers text-based `container list` output (no JSON format)
- Gracefully degrade on unsupported operations (`pause`, `unpause`, networking, volumes) with warning logs instead of hard failures
- Raise `NotImplementedError` for `compose_up` and `compose_down` (not supported by Apple Containers)
- Log informational messages when `seccomp`, `caps`, or `privileged` flags are passed (not applicable under VM isolation)
- Verify Apple Containers availability via `container --version`

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `AppleContainerEngine` | Class | Apple Containers CLI-backed engine; strongest isolation model (per-container VM) |

## Function Details

### AppleContainerEngine.run(image, name, *, ports, volumes, env, privileged, caps, seccomp, detach, ...)
**Purpose:** Launch a container. Ports, volumes, and env are passed through. Logs warnings for `privileged`, `seccomp`, and `caps` flags since VM isolation makes them redundant.
**Returns:** Container ID string.

### AppleContainerEngine.ps(all)
**Purpose:** Run `container list [--all]` and parse the text table output (skips header line, splits on whitespace).
**Returns:** `list[ContainerInfo]`.

### AppleContainerEngine.inspect(name)
**Purpose:** Run `container inspect`; attempts JSON parse, falls back to returning `{"raw": output}` on parse failure.
**Returns:** dict.

### AppleContainerEngine.pause(name) / unpause(name)
**Purpose:** Attempt pause/unpause; on failure, logs a warning and calls `stop()` as a fallback (pause may not be supported on all macOS versions).

### AppleContainerEngine.compose_up(file, detach) / compose_down(file)
**Purpose:** Always raises `NotImplementedError`. Users must use `compose_generator.generate_apple_script()` to manage services.

### AppleContainerEngine.network_create / network_rm / volume_create / volume_rm
**Purpose:** Attempt the operation; catches exceptions and logs a warning if unsupported (graceful degradation).

### AppleContainerEngine.health_check()
**Purpose:** Run `container --version` with a 10-second timeout; return True on success.
**Returns:** bool.

## Apple Containers vs Docker/Podman

| Feature | Apple Containers | Docker/Podman |
|---------|-----------------|--------------|
| Isolation model | Hardware VM per container | Namespace/cgroup |
| Compose support | No (use generated script) | Yes |
| seccomp profiles | Not needed (VM boundary) | Supported |
| Linux capabilities | Not applicable | Supported |
| Rootless | Yes (no daemon) | Podman default; Docker optional |
| Platform | macOS 26+ / Apple Silicon | Cross-platform |

## Configuration / Environment Variables
- `cli` constructor parameter — default `"container"` (Apple Containers CLI binary)
- Requires macOS 26+ and Apple Containers framework installed

## Related
- [[engine.py]]
- [[docker_engine.py]]
- [[compose_generator.py]]
- [[security.py]]
