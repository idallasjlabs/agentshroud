---
title: ssh_config.py
type: module
file_path: gateway/ingest_api/ssh_config.py
tags: [ssh, configuration, pydantic, security, gateway-core]
related: [Gateway Core/main.py, Gateway Core/models.py, Architecture Overview]
status: documented
---

# ssh_config.py

## Purpose
Defines Pydantic configuration models for the SSH proxy feature of the AgentShroud gateway. Specifies per-host connection parameters, command allowlists/denylists, session limits, and auto-approval rules.

## Responsibilities
- Model the SSH proxy configuration loaded from `agentshroud.yaml`
- Expand `~` in `key_path` and `known_hosts_file` paths at model validation time
- Provide per-host granular control over which commands are allowed, denied, or auto-approved
- Control global SSH proxy enable/disable and the default `require_approval` setting

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `SSHHostConfig` | class | Configuration for a single SSH host |
| `SSHHostConfig.expand_key_path` | validator | Expands `~` in `key_path` using `os.path.expanduser` |
| `SSHHostConfig.expand_known_hosts` | validator | Expands `~` in `known_hosts_file` |
| `SSHConfig` | class | Top-level SSH proxy configuration |

## SSHHostConfig Fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `host` | str | required | SSH hostname or IP address |
| `port` | int | 22 | SSH port |
| `username` | str | `"root"` | SSH username |
| `key_path` | str | `""` | Path to SSH private key file (tilde-expanded) |
| `known_hosts_file` | str | `"~/.ssh/known_hosts"` | Path to known_hosts for host key verification (tilde-expanded) |
| `allowed_commands` | list[str] | `[]` | Commands explicitly permitted (empty = all allowed) |
| `denied_commands` | list[str] | `[]` | Commands explicitly denied (takes precedence) |
| `max_session_seconds` | int | 60 | Maximum duration for a single SSH session |
| `auto_approve_commands` | list[str] | `[]` | Commands that bypass the approval queue |

## SSHConfig Fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `enabled` | bool | `False` | Whether the SSH proxy feature is active |
| `hosts` | dict[str, SSHHostConfig] | `{}` | Named host configurations |
| `global_denied_commands` | list[str] | `[]` | Commands denied across all hosts |
| `require_approval` | bool | `True` | Whether SSH commands require approval queue sign-off |

## Environment Variables Used
- None directly — configuration is loaded from `agentshroud.yaml` via `GatewayConfig`

## Config Keys Read
- `config.ssh.enabled`
- `config.ssh.hosts` — dict of named `SSHHostConfig` entries
- `config.ssh.global_denied_commands`
- `config.ssh.require_approval`

## Imports From / Exports To
- Imports: `os`, `pydantic` (`BaseModel`, `Field`, `field_validator`)
- Imported by: `gateway.ssh_proxy.proxy` (`SSHProxy`), [[Gateway Core/main.py]] (reads `config.ssh` to decide whether to create `SSHProxy`)

## Known Issues / Notes
- `username` defaults to `"root"` — this is a least-privilege risk. Production deployments should set a non-root user in `agentshroud.yaml`.
- `allowed_commands` with an empty list means all commands are permitted (except denied ones). The validation logic in `SSHProxy` must handle this correctly.
- `auto_approve_commands` bypasses the approval queue entirely for matching commands — this list should be kept minimal and reviewed regularly.
- Host key verification uses `known_hosts_file`; if this file does not exist or the host key is not present, SSH connections will fail. There is no `StrictHostKeyChecking=no` fallback.
- `max_session_seconds` is defined in the config model but enforcement depends on `SSHProxy.execute()` implementation.

## Related
- [[Gateway Core/main.py]]
- [[Gateway Core/models.py]]
- [[Architecture Overview]]
