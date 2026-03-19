---
title: security.py
type: module
file_path: gateway/runtime/security.py
tags: [runtime, security, container-hardening, seccomp, capabilities, selinux, vm-isolation]
related: [[engine.py]], [[docker_engine.py]], [[podman_engine.py]], [[apple_engine.py]], [[config.py]]
status: documented
---

# security.py

## Purpose
Provides a runtime-agnostic registry of container security features and their support status across Docker, Podman, and Apple Containers. Generates gap warnings for missing features and returns recommended security CLI options per runtime.

## Responsibilities
- Maintain a master registry (`SECURITY_FEATURES`) of all security capabilities with per-runtime support flags and notes
- Provide query functions to get supported or missing features for a given runtime
- Return a comparison matrix across all three runtimes
- Generate and log `WARNING`-level messages for every missing feature on the target runtime
- Return recommended CLI security option dicts for Docker, Podman, and Apple Containers
- Validate runtime names to prevent attribute access injection

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `SecurityFeature` | Dataclass | A security capability: name, description, docker/podman/apple support bools, per-runtime notes |
| `SECURITY_FEATURES` | List | Master registry of all security features |
| `VALID_RUNTIMES` | FrozenSet | `{"docker", "podman", "apple"}` — validated against before all getattr calls |
| `get_features_for_runtime(runtime)` | Function | Return features available on the given runtime |
| `get_missing_features(runtime)` | Function | Return features NOT available on the given runtime |
| `get_security_comparison()` | Function | Return `{feature_name: {runtime: supported}}` matrix |
| `warn_missing_features(runtime)` | Function | Log WARNING for each missing feature; return list of warning strings |
| `get_security_options(runtime)` | Function | Return recommended CLI security option dict for a runtime |

## Function Details

### get_features_for_runtime(runtime)
**Purpose:** Filter `SECURITY_FEATURES` to those supported by the named runtime.
**Parameters:** `runtime` (str) — one of `docker`, `podman`, `apple`.
**Returns:** `list[SecurityFeature]`.

### get_missing_features(runtime)
**Purpose:** Filter `SECURITY_FEATURES` to those NOT supported by the named runtime.
**Returns:** `list[SecurityFeature]`.

### warn_missing_features(runtime)
**Purpose:** For each missing feature, log a `WARNING` with runtime-specific notes and return all warning strings.
**Returns:** `list[str]`.

### get_security_options(runtime)
**Purpose:** Return a dict of recommended security CLI options:
- Docker: `no-new-privileges` + custom seccomp + `cap_drop: ALL` + `cap_add: NET_BIND_SERVICE` + `read_only: True`
- Podman: same as Docker + `userns: auto`
- Apple: informational note only (VM isolation makes specific options unnecessary)
**Returns:** dict.

### _validate_runtime(runtime)
**Purpose:** Validate that `runtime` is in `VALID_RUNTIMES` before using it in `getattr()` calls to prevent attribute access injection.
**Raises:** `ValueError` for invalid runtimes.

## Security Feature Registry

| Feature | Docker | Podman | Apple | Notes |
|---------|--------|--------|-------|-------|
| seccomp | Yes | Yes | No | VM boundary makes it unnecessary for Apple |
| cap_drop | Yes | Yes | No | Not applicable under VM isolation |
| read_only_rootfs | Yes | Yes | No | VM filesystem differs |
| no_new_privileges | Yes | Yes | No | Default in Podman rootless |
| rootless | No | Yes | Yes | Docker requires explicit setup |
| selinux | No | Yes | No | Podman `:z`/`:Z` volume labels |
| vm_isolation | No | No | Yes | Hardware VM per container |
| user_namespace | Yes | Yes | Yes | Automatic in Podman rootless; VM in Apple |

## Configuration / Environment Variables
- No environment variables; runtime passed as a parameter to all functions
- Custom seccomp profile path: `docker/seccomp/agentshroud-seccomp.json` (referenced in Docker recommendations)

## Related
- [[engine.py]]
- [[docker_engine.py]]
- [[podman_engine.py]]
- [[apple_engine.py]]
- [[config.py]]
