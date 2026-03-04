---
title: seccomp-profiles
type: config
file_path: docker/seccomp/
tags: [security, seccomp, containers, syscall-filtering]
related: [Configuration/docker-compose.yml, Containers & Services/agentshroud-gateway, Containers & Services/agentshroud-bot]
status: documented
---

# Seccomp Profiles

**Location:** `docker/seccomp/`
**Files:**
- `gateway-seccomp.json` — Gateway container profile
- `agentshroud-seccomp.json` — Bot container profile
**Applied via:** `docker-compose.yml` → `security_opt: seccomp:/path/to/profile.json`

## Purpose

Linux seccomp (Secure Computing Mode) profiles restrict which kernel syscalls the containers are allowed to make. The default action is `SCMP_ACT_ERRNO` — any syscall not in the allowlist returns `EPERM`. This dramatically reduces the container's attack surface by preventing syscalls used by privilege escalation, container breakout, and kernel exploits.

## Default Action

```json
{
  "defaultAction": "SCMP_ACT_ERRNO",
  "defaultErrnoRet": 1
}
```

All unlisted syscalls fail with `errno=1` (EPERM). This is **deny-by-default**.

## Architecture Support

Both profiles support:
- `SCMP_ARCH_X86_64` (with `X86`, `X32` subarchitectures)
- `SCMP_ARCH_AARCH64` (with `ARM` subarchitecture)

This ensures the profiles work on both AMD64 (server) and ARM64 (Apple Silicon, Raspberry Pi) deployments.

## Allowed Syscall Categories

The profiles allowlist these categories of syscalls:

| Category | Example Syscalls | Purpose |
|----------|-----------------|---------|
| **Network I/O** | `accept`, `bind`, `connect`, `recv*`, `send*` | HTTP server, proxy connections |
| **File I/O** | `read`, `write`, `open`, `close`, `stat` | File operations |
| **Process** | `clone`, `fork`, `execve`, `wait4`, `exit` | Process lifecycle |
| **Memory** | `brk`, `mmap`, `mprotect`, `munmap` | Memory management |
| **Signals** | `kill`, `sigaction`, `sigreturn` | Signal handling |
| **Time** | `clock_gettime`, `nanosleep` | Timing operations |
| **Polling** | `epoll_*`, `poll`, `select` | Async I/O |
| **Capabilities** | `capget`, `capset` | Linux capabilities check |

## Blocked Syscalls (Notable)

These dangerous syscalls are NOT in the allowlist:
- `ptrace` — Process tracing (used in container breakouts)
- `mount` — Filesystem mounting
- `kexec_load` — Kernel replacement
- `create_module` — Kernel module loading
- `init_module` — Kernel module insertion
- `perf_event_open` — Kernel performance monitoring (side channels)
- `unshare` — Namespace manipulation

## Gateway vs Bot Profile Differences

| Profile | Tuned For |
|---------|-----------|
| `gateway-seccomp.json` | Python/FastAPI server: network-heavy, no subprocess spawning |
| `agentshroud-seccomp.json` | Node.js + Playwright: includes browser subprocess syscalls (`clone3`, `ptrace` for Chromium sandbox) |

> **Note:** Playwright/Chromium requires some additional syscalls. The bot profile is slightly more permissive than the gateway profile to accommodate the browser sandbox process.

## Applied By

In `docker-compose.yml`:
```yaml
security_opt:
  - seccomp:./docker/seccomp/gateway-seccomp.json
```

## Related Notes

- [[Configuration/docker-compose.yml]] — Where profiles are referenced
- [[Containers & Services/agentshroud-gateway]] — Gateway container (gateway profile)
- [[Containers & Services/agentshroud-bot]] — Bot container (bot profile)
- [[Architecture Overview]] — Security hardening overview
