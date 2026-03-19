---
title: SSH Proxy Errors
type: troubleshooting
tags: [ssh, proxy, errors]
related: [Gateway Core/ssh_config.py, Configuration/agentshroud.yaml, Errors & Troubleshooting/Error Index]
status: documented
---

# SSH Proxy Errors

## HTTP 403 — SSH Host Not Allowed

**Error:** `SSH host not in allowlist: unknown-host.example.com`

**Cause:** The requested SSH host is not in the `ssh.hosts` allowlist in `agentshroud.yaml`.

**Fix:** Add the host to the configuration:
```yaml
ssh:
  hosts:
    new-host:
      host: "new-host.tail240ea8.ts.net"
      port: 22
      username: "agentshroud-bot"
      key_path: "/var/agentshroud-ssh/id_ed25519"
      max_session_seconds: 300
```

---

## SSH Key Not Found

**Error:** `SSH key not found: /var/agentshroud-ssh/id_ed25519`

**Cause:** The `agentshroud-ssh` volume is empty (SSH keys not generated yet, or volume missing).

**Fix:**
```bash
# Check volume contents
docker exec agentshroud-bot ls /home/node/.ssh/

# If empty, SSH keys need to be generated (happens on first bot startup)
# Restart bot container to trigger key generation
docker compose restart agentshroud-bot
```

---

## SSH Connection Timeout

**Error:** `SSH connection to host timed out`

**Cause:** Host unreachable via Tailscale, or host is offline.

**Fix:**
```bash
# Test connectivity from macOS host
ping raspberrypi.tail240ea8.ts.net

# Check Tailscale status
tailscale status
```

---

## Session Duration Exceeded

**Error:** `SSH session terminated: max_session_seconds exceeded`

**Cause:** SSH session ran longer than `max_session_seconds` (default: 300s = 5 minutes).

**Fix:** Increase `max_session_seconds` for the specific host:
```yaml
ssh:
  hosts:
    pi:
      max_session_seconds: 600   # 10 minutes
```

---

## Globally Denied Command

**Error:** `SSH command denied: command matches global deny list`

**Cause:** Command matches a pattern in `ssh.global_denied_commands`.

**Default denied patterns:**
- `rm -rf /`
- `mkfs`
- `dd if=`

These are hardcoded safety measures and cannot be bypassed through the gateway.

---

## Related Notes

- [[Gateway Core/ssh_config.py|ssh_config.py]] — SSH configuration models
- [[Configuration/agentshroud.yaml]] — `ssh` section
- [[Errors & Troubleshooting/Error Index]] — Full error index
