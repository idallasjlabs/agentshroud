---
title: Container Errors
type: troubleshooting
tags: [containers, docker, errors]
related: [Errors & Troubleshooting/Error Index, Shutdown & Recovery, Runbooks/Crash Recovery]
status: documented
---

# Container Errors

## Exit Code Reference

| Exit Code | Signal | Meaning | Common Cause |
|-----------|--------|---------|-------------|
| 0 | Normal | Clean exit | Intentional stop |
| 1 | | Python/Node exception | Application error |
| 137 | SIGKILL | Force killed | OOM kill, `docker kill` |
| 139 | SIGSEGV | Segfault | Memory corruption |
| 143 | SIGTERM | Terminated | Graceful stop, `docker stop` |

```bash
# Check exit code
docker inspect agentshroud-gateway --format='{{.State.ExitCode}}'
```

---

## OOM Kill (Exit Code 137)

**Symptom:** Container restarts repeatedly; `dmesg` shows OOM kill

**Diagnosis:**
```bash
# Check memory usage before/during OOM
docker stats agentshroud-gateway --no-stream

# Check if OOM killer was involved
docker logs agentshroud-gateway 2>&1 | tail -20
```

**Fixes:**

For gateway (default 1280 MB):
```yaml
# docker-compose.yml
mem_limit: 2560m
memswap_limit: 2560m
```

For bot (default 4 GB):
- Reduce Playwright concurrency
- Limit file operation sizes

**Most common OOM cause:** spaCy model loading + Presidio analyzer initialization peaks at ~600 MB. If concurrent requests arrive before model is warm, memory spikes.

---

## Read-Only Filesystem Errors

**Error:** `Read-only file system: '/path/to/file'`

**Cause:** Container has `read_only: true` and code is trying to write to a non-mounted path.

**Fix options:**
1. If the path should be writable: add a `tmpfs` or volume mount
2. If the write is a bug: fix the code to write to `/tmp` or an explicit volume

**Common write locations that need mounts:**

| Path | Current Mount |
|------|--------------|
| `/tmp` | tmpfs |
| `/var/tmp` | tmpfs |
| `/app/data` | `gateway-data` volume |

---

## Port Already in Use

**Error:** `Bind: address already in use: 0.0.0.0:8080`

**Fix:**
```bash
# Find what's using port 8080
lsof -i :8080
# or
docker ps | grep 8080

# Kill the conflicting process or container
docker rm -f <container-id>
```

---

## Container Won't Stop (Stuck in Stopping)

**Cause:** Container not responding to SIGTERM within `stop_grace_period` (15s)

**Fix:**
```bash
# Force kill
docker kill agentshroud-gateway
docker rm agentshroud-gateway
docker compose up -d agentshroud-gateway
```

---

## `no-new-privileges` Security Denial

**Error:** `Operation not permitted` when a subprocess tries to escalate privileges

**Cause:** Security option `no-new-privileges:true` blocking a legitimate operation

**Fix:** Review the subprocess. If it legitimately needs elevated permissions, use `gosu` to run as the correct user from the start, not via privilege escalation.

---

## Related Notes

- [[Shutdown & Recovery]] — Recovery procedures
- [[Runbooks/Crash Recovery]] — Post-crash steps
- [[Errors & Troubleshooting/Error Index]] — Full error index
- [[Configuration/docker-compose.yml]] — Container security settings
