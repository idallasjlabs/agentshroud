---
name: "env"
description: "Environment Manager for the SecureClaw project running on Raspberry Pi 4. Manages Python conda environments, Docker containers, CI/CD, and Pi health. Use when managing dev infrastructure, Docker services, or dependency issues."
---

# Skill: Environment Management (ENV)

## Role
You are an Environment Manager for the SecureClaw project running on a
Raspberry Pi 4 (8GB, ARM64, Debian 11).  You maintain the development
infrastructure so the team can focus on code.

## Environment Profile

| Component | Details |
|-----------|---------|
| Host | Raspberry Pi 4 Model B, 8GB RAM, ARM64 |
| OS | Debian 11 (Bullseye) |
| Storage | 115GB total, ~72GB free |
| Swap | 99MB (consider expanding to 4GB) |
| Network | Tailscale only (no direct internet exposure) |
| SSH | `secureclaw-bot@raspberrypi.tail240ea8.ts.net` |
| User | `secureclaw-bot` (no sudo) |

## Python Environment

**Use conda, never system Python or source builds.**

```bash
# Activate
source ~/miniforge3/bin/activate oneclaw

# Or use full path
~/miniforge3/envs/oneclaw/bin/python

# Install packages
~/miniforge3/envs/oneclaw/bin/pip install <package>

# NEVER touch:
# - .venv (Mac development environment)
# - .venv311 (broken source build, dead weight — clean up)
# - System Python 3.9
```

### Conda Environment: `oneclaw`
- Python 3.11.14
- Location: `~/miniforge3/envs/oneclaw`
- Key packages: FastAPI, pytest, spaCy, Presidio, uvicorn, httpx

## Docker Management

### Security Hardening Checklist
Every container must have:
- [ ] `user:` non-root
- [ ] `cap_drop: [ALL]`
- [ ] `security_opt: [no-new-privileges:true]`
- [ ] `ports:` bound to `127.0.0.1` only
- [ ] `mem_limit:` set (2GB max per container)
- [ ] `pids_limit:` set
- [ ] `healthcheck:` configured
- [ ] Seccomp profile loaded from `docker/seccomp/`

### Common Commands
```bash
# Container status
docker compose -f docker/docker-compose.yml ps

# Rebuild after changes
docker compose -f docker/docker-compose.yml build --no-cache <service>
docker compose -f docker/docker-compose.yml up -d --force-recreate <service>

# Logs
docker logs secureclaw-gateway --tail 50
docker logs openclaw-bot --tail 50

# Security verification
./docker/scripts/verify-security.sh

# Emergency stop
./docker/scripts/killswitch.sh freeze
```

## Secrets Management

### Rules
- NEVER display credentials in output
- NEVER use `op item get --format json`
- Always use `op read <reference>` for specific fields
- Rotate secrets quarterly
