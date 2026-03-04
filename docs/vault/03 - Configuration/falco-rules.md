---
title: falco-rules.yaml
type: config
file_path: docker/falco/rules.yaml
tags: [security, falco, runtime-monitoring, containers]
related: [Security Modules/falco_monitor.py, Containers & Services/agentshroud-bot, Architecture Overview]
status: documented
---

# falco-rules.yaml

**Location:** `docker/falco/rules.yaml`
**Tool:** Falco — cloud-native runtime security / kernel-level anomaly detection
**Lines:** 86

## Purpose

Falco runtime security rules for AgentShroud containers. Detects threats at the kernel syscall level: shell spawning, unexpected outbound connections, file access outside workspace, privilege escalation, secret file access, and crypto mining.

## Rules Defined

| Rule | Priority | Description |
|------|----------|-------------|
| Container Shell Spawned | WARNING | Shell (`bash`, `sh`, `zsh`, `fish`, etc.) invoked inside container — allowed for startup scripts only |
| Unexpected Outbound Connection | ERROR | Bot container (`agentshroud`) connects to non-private IP (RFC1918 only allowed) |
| File Access Outside Workspace | ERROR | Write to paths outside `/home/node/`, `/tmp/`, `/proc/`, `/dev/null` |
| Privilege Escalation Attempt | CRITICAL | `sudo`, `su`, `setuid`, `chmod +s` inside any container |
| Secret File Access | CRITICAL | Read of `/etc/shadow`, `/etc/ssh/ssh_host*`, SSH private keys (`id_rsa`, `id_ed25519`) |
| Crypto Mining Detection | CRITICAL | Known miner processes or stratum protocol strings in `cmdline` |

## Shell Spawning Exceptions

The shell rule **allows** these parent processes (startup/entrypoint scripts):
```
start-agentshroud.sh
entrypoint-agentshroud.sh
security-entrypoint.sh
security-scheduler.sh
security-scan.sh
```

Any other shell spawn (e.g., agent running `bash -c ...`) triggers a WARNING.

## Network Enforcement

The outbound connection rule only fires for the `agentshroud` (bot) container. It blocks connections to non-RFC1918 addresses — the bot should only connect to the internal Docker network (`agentshroud-internal`) and reach the public internet exclusively through the gateway's proxy layer.

## Priority Levels

| Priority | Action |
|----------|--------|
| WARNING | Log event; continue |
| ERROR | Log event; alert via `falco_monitor.py` |
| CRITICAL | Log event; alert + potential kill switch trigger |

## Integration

Falco monitors are consumed by `gateway/security/falco_monitor.py`, which:
- Reads Falco output stream
- Classifies events by severity
- Triggers alerts via `alert_dispatcher.py`
- Can initiate kill switch for CRITICAL events

## Related Notes

- [[Security Modules/falco_monitor.py|falco_monitor.py]] — Python consumer of Falco events
- [[Containers & Services/agentshroud-bot]] — Container being monitored
- [[Architecture Overview]] — Security layer placement
- [[Runbooks/Kill Switch Procedure]] — CRITICAL event response
