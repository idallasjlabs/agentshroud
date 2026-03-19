---
title: env_guard.py
type: module
file_path: gateway/security/env_guard.py
tags: [security, environment-variables, credential-leakage, command-blocking, output-scrubbing]
related: ["[[Security Modules/egress_filter.py|egress_filter.py]]", "[[Security Modules/encrypted_store.py|encrypted_store.py]]", "[[Data Flow]]"]
status: documented
---

# env_guard.py

## Purpose
Prevents AI agents from reading or leaking host environment variables and API credentials by blocking access to `/proc/*/environ` paths, blocking environment-dumping commands, detecting environment variable expansion in commands, and scrubbing credentials from command output.

## Threat Model
Credential theft via environment variable access — an agent that can read `OPENAI_API_KEY`, `AWS_SECRET_ACCESS_KEY`, `ANTHROPIC_API_KEY`, or similar secrets from the process environment can exfiltrate those credentials to an attacker-controlled endpoint, enabling lateral movement, cloud resource abuse, or supply chain attacks.

## Responsibilities
- Block file access to `/proc/self/environ`, `/proc/1/environ`, and `/proc/[pid]/environ` paths
- Block execution of environment-dumping commands: `env`, `printenv`, `set`, `export`, `declare -p`
- Block commands containing shell environment variable expansion patterns (`$VAR`, `${VAR}`) or direct procfs access
- Scrub known credential patterns from command output using API key regexes (OpenAI, AWS, GitHub, Slack, 1Password)
- Scrub named environment variables matching a credential name set from command output
- Detect values that look like credentials by pattern and length heuristics
- Record all leakage detections to an in-memory log with severity, source, and context
- Provide per-agent monitoring summaries aggregating detection history
- Provide a global singleton `EnvironmentGuard` instance via `get_env_guard()`
- Expose module-level `check_command()` and `scrub_output()` convenience functions

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `EnvironmentLeakage` | Dataclass | Record of one detected leakage event |
| `EnvironmentGuard` | Class | Main guard; all state is per-instance |
| `EnvironmentGuard.check_file_access()` | Method | Block access to procfs environ files |
| `EnvironmentGuard.check_command_execution()` | Method | Block env-dumping commands and env-access patterns |
| `EnvironmentGuard.scrub_command_output()` | Method | Redact credentials from command stdout |
| `EnvironmentGuard.monitor_environment_access()` | Method | Per-agent leakage summary |
| `EnvironmentGuard.get_leakage_summary()` | Method | Aggregate summary across all agents |
| `EnvironmentGuard.export_leakage_report()` | Method | Write full JSON report to file |
| `global_env_guard` | Module-level | Singleton `EnvironmentGuard` instance |
| `get_env_guard()` | Function | Access the global singleton |
| `check_command()` | Function | Module-level command check via singleton |
| `scrub_output()` | Function | Module-level output scrub via singleton |

## Function Details

### EnvironmentGuard.check_file_access(file_path, agent_id)
**Purpose:** Normalize the path and compare against blocked paths, including wildcard `/proc/*/environ` matching via regex substitution.
**Parameters:** `file_path` (str), `agent_id` (str)
**Returns:** bool — True if access is allowed, False if blocked.
**Side effects:** Logs warning; calls `_record_leakage()` with severity `"critical"`.

### EnvironmentGuard.check_command_execution(command, agent_id)
**Purpose:** Parse command with `shlex.split()`, check base command against blocked list, then check full command string for env access patterns.
**Parameters:** `command` (str), `agent_id` (str)
**Returns:** bool — True if allowed, False if blocked.
**Side effects:** Logs warning; calls `_record_leakage()` with severity `"high"` for command blocks, `"medium"` for pattern blocks.

### EnvironmentGuard.scrub_command_output(output, command)
**Purpose:** Two-pass scrubbing: first apply API key regex patterns (OpenAI `sk-`, AWS `AKIA*`, GitHub `ghp_`, 1Password `op_`, Slack `xoxb-`/`xoxp-`, generic 32+ alphanumeric), then scan for `NAME=VALUE` pairs where NAME is in the credential variable set or VALUE matches credential heuristics.
**Parameters:** `output` (str), `command` (str)
**Returns:** str — scrubbed output with matched values replaced by `[REDACTED-API-KEY]` or `[REDACTED]`.
**Side effects:** Records leakage if credentials found.

### EnvironmentGuard.monitor_environment_access(agent_id)
**Purpose:** Return a monitoring summary for one agent: total access attempts, blocked attempts, suspicious patterns, and a risk level (low / medium / high / critical).
**Returns:** dict

### check_command(cmd)
**Purpose:** Module-level convenience wrapper around the global `EnvironmentGuard.check_command_execution()`. Provides a categorized rejection reason string.
**Returns:** `tuple[bool, str]` — (allowed, reason)

### scrub_output(text)
**Purpose:** Module-level convenience scrubber using a standalone set of regex patterns (independent of the `EnvironmentGuard` instance patterns). Replaces matches with `[SCRUBBED-<PATTERN_NAME>]`.
**Returns:** str

## Blocked Paths
- `/proc/self/environ`
- `/proc/1/environ`
- `/proc/[0-9]+/environ` (wildcard via regex)

## Blocked Commands
`env`, `printenv`, `set`, `export`, `declare -p`

## Blocked Command Patterns (via `_contains_env_access_patterns`)
- `$VARNAME` — shell variable expansion
- `${VARNAME}` — shell variable expansion with braces
- `cat /proc/[pid|self]/environ`
- `strings /proc/[pid|self]/environ`
- `grep .* /proc/[pid|self]/environ`

## Tracked Credential Variable Names (subset)
`API_KEY`, `SECRET_KEY`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GITHUB_TOKEN`, `DATABASE_URL`, `JWT_SECRET`, `ENCRYPTION_KEY` — 25 total names in `credential_env_vars` set.

## Mode: Enforce vs Monitor
This module always enforces. `check_file_access()` and `check_command_execution()` return False (blocked) unconditionally when a threat is detected. There is no monitor-only mode toggle.

## Environment Variables
None read by this module. It protects against leakage of environment variables but does not read any itself.

## Global Singleton
`global_env_guard = EnvironmentGuard()` is instantiated at module load. Use `get_env_guard()` to access it. The module-level `check_command()` and `scrub_output()` functions operate on this singleton.

## Related
- [[Data Flow]]
- [[Configuration/agentshroud.yaml]]
- [[Security Modules/egress_filter.py|egress_filter.py]]
- [[Security Modules/encrypted_store.py|encrypted_store.py]]
- [[Security Modules/agent_isolation.py|agent_isolation.py]]
