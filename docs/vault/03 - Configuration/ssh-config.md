---
title: ssh-config
type: config
file_path: docker/config/ssh/ (applied to /home/node/.ssh/config)
tags: [ssh, security, configuration]
related: [Configuration/agentshroud.yaml, Other/ssh_proxy.py, Containers & Services/agentshroud-bot]
status: documented
---

# SSH Config

**Location:** `docker/config/ssh/` (baked into image; applied at startup)
**Applied by:** `init-openclaw-config.sh` on every container startup
**Written to:** `/home/node/.ssh/config`

## Purpose

SSH client configuration for the bot container. Defines approved SSH hosts, forces key-based authentication, and restricts the bot's SSH capabilities.

## Key Configuration

```
Host pi
  HostName raspberrypi.tail240ea8.ts.net
  Port 22
  User agentshroud-bot
  IdentityFile /home/node/.ssh/id_ed25519
  StrictHostKeyChecking accept-new
  UserKnownHostsFile /home/node/.ssh/known_hosts

Host marvin
  HostName marvin.tail240ea8.ts.net
  Port 22
  User agentshroud-bot
  IdentityFile /home/node/.ssh/id_ed25519
  StrictHostKeyChecking accept-new

Host *
  PasswordAuthentication no    # Key-only auth
  IdentitiesOnly yes
```

## Applied By

`init-openclaw-config.sh` copies this config to `/home/node/.ssh/config` on every startup, ensuring it cannot be modified by the agent.

## Relationship to agentshroud.yaml

The `ssh.hosts` section in `agentshroud.yaml` controls which hosts the **gateway's SSH proxy** allows. This SSH config controls how the **bot's SSH client** connects to those hosts.

## Related Notes

- [[Configuration/agentshroud.yaml]] — `ssh.hosts` allowlist
- [[Other/ssh_proxy.py|ssh_proxy.py]] — Gateway-side SSH proxy
- [[Startup Sequence]] — When this config is applied
