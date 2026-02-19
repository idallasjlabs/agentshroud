# SSH Configuration Guide

## Configuration File

SSH proxy settings live in the `ssh:` section of `agentshroud.yaml`. The gateway reads this on startup and constructs the `SSHConfig` / `SSHHostConfig` models.

## Full Annotated Example

```yaml
ssh:
  # Master switch — set to false to disable all SSH functionality
  enabled: true

  # When true, commands not in auto_approve_commands require human approval
  require_approval: true

  # Commands blocked across ALL hosts (substring match)
  global_denied_commands:
    - "rm -rf /"
    - "mkfs"
    - "dd if="

  hosts:
    # Key is the logical host name used in API requests
    pi:
      # Hostname or IP of the target
      host: "raspberrypi.tail240ea8.ts.net"

      # SSH port (default: 22)
      port: 22

      # SSH username (default: "root")
      username: "agentshroud-bot"

      # Path to private key (~ is expanded; empty string = use SSH agent/defaults)
      key_path: "/home/agentshroud-bot/.ssh/id_ed25519"

      # Whitelist of allowed commands. If non-empty, ONLY these commands
      # (and commands starting with them + arguments) are permitted.
      # If empty, all commands are allowed (subject to deny lists).
      allowed_commands:
        - "git status"
        - "git log"
        - "ls"
        - "cat"
        - "whoami"
        - "df -h"
        - "uptime"

      # Commands blocked for this host (substring match)
      denied_commands:
        - "rm -rf"
        - "shutdown"
        - "reboot"

      # Maximum execution time in seconds. Command is killed on timeout.
      max_session_seconds: 30

      # Commands that execute immediately without human approval.
      # Requires EXACT match — no extra arguments allowed.
      auto_approve_commands:
        - "git status"
        - "ls"
        - "whoami"
        - "uptime"
```

## Field Reference

| Field | Scope | Type | Default | Description |
|-------|-------|------|---------|-------------|
| `enabled` | Global | bool | `false` | Enable/disable the SSH proxy entirely |
| `require_approval` | Global | bool | `true` | Require human approval for non-auto-approved commands |
| `global_denied_commands` | Global | list[str] | `[]` | Substring patterns blocked on all hosts |
| `host` | Per-host | str | — | Hostname or IP of the SSH target |
| `port` | Per-host | int | `22` | SSH port |
| `username` | Per-host | str | `"root"` | SSH username |
| `key_path` | Per-host | str | `""` | Path to SSH private key (`~` expanded) |
| `known_hosts_file` | Per-host | str | `"~/.ssh/known_hosts"` | Path to known_hosts file for host key verification |
| `allowed_commands` | Per-host | list[str] | `[]` | Command whitelist (empty = allow all) |
| `denied_commands` | Per-host | list[str] | `[]` | Command blacklist (substring match) |
| `max_session_seconds` | Per-host | int | `60` | Timeout before killing the command |
| `auto_approve_commands` | Per-host | list[str] | `[]` | Commands that skip the approval queue (exact match) |

## How to Add a New Trusted Host

### Step 1: Choose a logical name

Pick a short, descriptive name (e.g., `staging`, `prod-web`, `nas`). This is the key in the `hosts:` dictionary and the value you'll use in API requests.

### Step 2: Add the host entry

```yaml
ssh:
  hosts:
    staging:
      host: "staging.example.com"
      port: 22
      username: "deploy"
      key_path: "/home/agentshroud-bot/.ssh/id_ed25519"
      allowed_commands: []        # start open, restrict later
      denied_commands:
        - "rm -rf"
        - "shutdown"
      max_session_seconds: 60
      auto_approve_commands: []   # nothing auto-approved initially
```

### Step 3: Set up SSH keys

Ensure the private key at `key_path` exists and the corresponding public key is in `~deploy/.ssh/authorized_keys` on the target host.

### Step 4: Pre-populate known_hosts (recommended)

```bash
ssh-keyscan -p 22 staging.example.com >> ~/.ssh/known_hosts
```

Or specify a dedicated file:

```yaml
      known_hosts_file: "/etc/agentshroud/known_hosts"
```

### Step 5: Restart the gateway

The config is loaded at startup. Restart the gateway to pick up the new host.

## How Allow/Deny Lists Work

**Evaluation order:**

1. **Injection check** — Shell metacharacters are blocked regardless of lists
2. **Global deny list** — Substring match against `global_denied_commands`
3. **Per-host deny list** — Substring match against host's `denied_commands`
4. **Per-host allow list** — If non-empty, command must match an entry:
   - Exact match: `"ls"` matches `ls`
   - Prefix match with args: `"ls"` matches `ls -la /tmp` (injection patterns already caught above)

**Deny always wins over allow** — a command matching both lists is denied.

## How Auto-Approve Works

Auto-approve commands bypass the approval queue and execute immediately. They require:

1. **Exact string match** — `"ls"` auto-approves `ls` but NOT `ls -la`
2. **All validation still applies** — injection detection, deny lists, and allow lists are checked first
3. **`require_approval` must be `true`** — If `require_approval` is `false`, all validated commands execute without approval anyway

## Example: Production Server with Strict Restrictions

```yaml
ssh:
  hosts:
    prod-db:
      host: "db-primary.internal.example.com"
      port: 2222
      username: "monitor"
      key_path: "/etc/agentshroud/keys/prod_monitor"
      known_hosts_file: "/etc/agentshroud/known_hosts"

      # Only allow read-only monitoring commands
      allowed_commands:
        - "pg_isready"
        - "psql -c 'SELECT 1'"
        - "df -h"
        - "free -m"
        - "uptime"
        - "systemctl status postgresql"

      denied_commands:
        - "DROP"
        - "DELETE"
        - "TRUNCATE"
        - "shutdown"
        - "reboot"
        - "rm"
        - "systemctl stop"
        - "systemctl restart"

      max_session_seconds: 15
      auto_approve_commands:
        - "pg_isready"
        - "uptime"
```

This configuration ensures the `monitor` user can only run read-only health checks. Destructive SQL keywords and system management commands are explicitly denied. Only `pg_isready` and `uptime` execute without approval.
