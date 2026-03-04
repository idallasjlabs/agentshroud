---
title: ssh_proxy.py
type: module
file_path: gateway/ssh_proxy/proxy.py
tags: [ssh, proxy, security]
related: [Gateway Core/ssh_config.py, Configuration/agentshroud.yaml, Errors & Troubleshooting/SSH Proxy Errors]
status: documented
---

# ssh_proxy.py

**Location:** `gateway/ssh_proxy/proxy.py`
**Lines:** ~185

## Purpose

SSH proxy that routes the OpenClaw agent's SSH connections through the gateway to an approved set of hosts. The agent cannot SSH to arbitrary hosts — only those in the `ssh.hosts` allowlist in `agentshroud.yaml`.

## Responsibilities

- Validate requested SSH host against `ssh.hosts` allowlist
- Use pre-configured SSH key from `agentshroud-ssh` volume
- Enforce `max_session_seconds` timeout per session
- Block globally denied commands (`global_denied_commands` list)
- Log all SSH sessions to audit ledger

## Key Class: `SSHProxy`

### `execute(host: str, command: str, session_id: str) → SSHExecResult`

Establishes an SSH connection to an approved host and runs the given command.

**Parameters:**
- `host` — Must match a key in `ssh.hosts` config
- `command` — Command to run (checked against `global_denied_commands`)
- `session_id` — Unique identifier for audit logging

**Returns:** `SSHExecResult` with stdout, stderr, exit_code

**Raises:**
- `403` if host not in allowlist
- `403` if command matches global deny list
- `408` if session exceeds `max_session_seconds`

## Configured Hosts

From `agentshroud.yaml`:
```yaml
ssh:
  hosts:
    pi:    raspberrypi.tail240ea8.ts.net:22
    marvin:    marvin.tail240ea8.ts.net:22
    trillian:  trillian.tail240ea8.ts.net:22
```

All hosts use `agentshroud-bot` username with ed25519 key at `/var/agentshroud-ssh/id_ed25519`.

## Security Notes

- The SSH key is stored in `agentshroud-ssh` Docker volume (not in the image)
- Key is generated inside the bot container on first run
- Gateway reads the key as read-only
- `known_hosts` stored at `/tmp/ssh_known_hosts` (tmpfs)

## Related Notes

- [[Gateway Core/ssh_config.py|ssh_config.py]] — SSH configuration models
- [[Configuration/agentshroud.yaml]] — `ssh` section
- [[Errors & Troubleshooting/SSH Proxy Errors]] — SSH error diagnosis
