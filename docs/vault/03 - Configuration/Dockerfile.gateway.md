---
title: Dockerfile.gateway
type: config
file_path: gateway/Dockerfile
tags: [docker, build, gateway, python]
related: [Configuration/docker-compose.yml, Containers & Services/agentshroud-gateway, Dependencies/All Dependencies]
status: documented
---

# Dockerfile — Gateway

**Location:** `gateway/Dockerfile`
**Runtime:** Python 3.13
**Base image:** `python:3.13-slim` (multi-stage build)
**Exposes:** Port 8080
**User:** `agentshroud` (UID 1000, non-root)

## Build Stages

### Stage 1: Builder (`python:3.13-slim AS builder`)

Installs Python build dependencies (gcc, g++) and all Python packages into `/install` prefix. Keeps build tools out of the runtime image.

```
python:3.13-slim AS builder
├── apt: gcc, g++
├── pip install -r gateway/requirements.txt → /install
```

### Stage 2: Runtime (`python:3.13-slim`)

```
python:3.13-slim
├── apt: libopenscap33, openscap-scanner      # OpenSCAP compliance
├── apt: clamav, clamav-daemon, clamdscan     # ClamAV malware scanning
├── apt: 1password-cli                         # op credential proxy
├── curl install: trivy                        # Vulnerability scanning
├── useradd agentshroud (UID 1000)
├── COPY --from=builder /install → /usr/local  # Python packages
├── COPY gateway/ → /app/gateway/             # Application code
├── mkdir /app/data (ledger volume mount point)
├── COPY ssg-debian12-ds.xml                  # SCAP compliance content
├── COPY docker/scripts/security-*.sh         # Security scan scripts
├── python3 -m spacy download en_core_web_sm  # spaCy NLP model (~560MB)
├── find / -perm /6000 → strip setuid bits    # CIS Docker Benchmark 4.8
├── USER agentshroud
├── EXPOSE 8080
└── CMD uvicorn gateway.ingest_api.main:app --host 0.0.0.0 --port 8080
```

## Security Hardening

| Measure | Implementation |
|---------|---------------|
| Non-root user | `USER agentshroud` (UID 1000) |
| No setuid/setgid bits | `find / -perm /6000 -exec chmod a-s` |
| No bytecode files | `ENV PYTHONDONTWRITEBYTECODE=1` |
| op CLI tmpfs | `ENV XDG_CONFIG_HOME=/tmp` |
| Read-only rootfs | Enforced by docker-compose `read_only: true` |
| Seccomp | `./seccomp/gateway-seccomp.json` (applied by compose) |
| All capabilities dropped | Applied by compose `cap_drop: ALL` |

## Pre-installed Tools

| Tool | Purpose | Version |
|------|---------|---------|
| ClamAV | Malware scanning | Latest from apt |
| Trivy | Container vulnerability scanning | Latest |
| 1Password CLI | Credential proxy (`op` command) | From 1password apt repo |
| OpenSCAP | Compliance scanning | libopenscap33 |
| spaCy | NLP for PII detection | `en_core_web_sm` model |

## Environment Variables Set

| Variable | Value | Purpose |
|----------|-------|---------|
| `PYTHONDONTWRITEBYTECODE` | 1 | Read-only fs compatibility |
| `XDG_CONFIG_HOME` | /tmp | op CLI config on tmpfs |
| `PYTHONPATH` | /app | Module resolution |

## Image Labels (OCI)

```
org.opencontainers.image.title: AgentShroud Gateway
org.opencontainers.image.version: 0.7.0
```

## Runtime Command

```
uvicorn gateway.ingest_api.main:app --host 0.0.0.0 --port 8080
```

> Note: Binds to `0.0.0.0` inside the container, but `docker-compose.yml` maps only `127.0.0.1:8080`, so the port is not accessible from the network.

## Related Notes

- [[Configuration/Dockerfile.bot]] — Bot container Dockerfile
- [[Containers & Services/agentshroud-gateway]] — Runtime container details
- [[Configuration/docker-compose.yml]] — Container orchestration
- [[Dependencies/All Dependencies]] — Python package list
