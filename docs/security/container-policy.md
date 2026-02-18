# Container Security Policy — SecureClaw

> Last updated: 2026-02-18 | SecureClaw v0.2.0

## 1. Container Hardening

### 1.1 Capabilities

All containers drop all Linux capabilities by default and add back only what's needed:

```yaml
security_opt:
  - no-new-privileges:true
cap_drop:
  - ALL
# cap_add only if strictly required (none currently)
```

### 1.2 Seccomp Profile

Containers run with Docker's default seccomp profile, which blocks ~44 dangerous syscalls including `mount`, `reboot`, `kexec_load`, and `ptrace`.

**Future:** Custom seccomp profile (`seccomp/secureclaw.json`) restricting to the minimal syscall set.

### 1.3 Read-Only Filesystem (Planned)

Target state:
```yaml
read_only: true
tmpfs:
  - /tmp:size=64m
  - /run:size=16m
volumes:
  - data:/app/data  # Only writable mount
```

**Current status:** Not yet enforced. Requires audit of all write paths (audit ledger, temp files).

### 1.4 Non-Root Execution

The application runs as a non-root user inside the container:
```dockerfile
RUN adduser --disabled-password --no-create-home secureclaw
USER secureclaw
```

### 1.5 Resource Limits

```yaml
deploy:
  resources:
    limits:
      cpus: '1.0'
      memory: 512M
    reservations:
      memory: 128M
```

---

## 2. Network Isolation

### 2.1 Docker Networks

- **internal network:** Service-to-service communication (gateway ↔ dashboard). No external access.
- **external network:** Only the gateway container connects to the internet (Telegram API, LLM API).

```yaml
networks:
  internal:
    internal: true
  external:
    driver: bridge
```

### 2.2 Exposed Ports

| Port | Service | Binding | Access |
|------|---------|---------|--------|
| 8080 | Gateway API | 127.0.0.1:8080 | Localhost + Tailscale only |
| 18790 | Control UI | 127.0.0.1:18790 | Localhost + Tailscale only |
| 8050 | Dashboard | 127.0.0.1:8050 | Localhost + Tailscale only |

All ports bind to `127.0.0.1` — never `0.0.0.0`. External access is via Tailscale serve only.

### 2.3 Tailscale Network

- All remote access goes through Tailscale (WireGuard-encrypted)
- Tailscale ACLs restrict which devices can reach the Pi
- No ports exposed to the public internet

---

## 3. Secret Management

### 3.1 Hierarchy

1. **1Password** — Source of truth for all secrets
2. **Docker Secrets** — Runtime delivery to containers
3. **Environment variables** — Only for non-sensitive configuration

### 3.2 Rules

- ❌ No secrets in docker-compose.yml, Dockerfiles, or source code
- ❌ No secrets in environment variables (use Docker Secrets or file mounts)
- ❌ No `.env` files committed to git
- ✅ Secrets loaded at runtime from Docker Secrets (`/run/secrets/`)
- ✅ 1Password CLI (`op`) for secret retrieval in deployment scripts
- ✅ `.gitignore` includes `*.env`, `.env*`, `secrets/`

### 3.3 Secret Rotation

- API tokens: Rotate every 90 days
- Bot tokens: Rotate on suspected compromise
- SSH keys: Ed25519, rotate annually
- Process: Update in 1Password → redeploy containers

---

## 4. Image Provenance and Updates

### 4.1 Base Images

- Use official Python slim images: `python:3.11-slim`
- Pin to specific digest when possible
- Rebuild weekly to pick up security patches

### 4.2 Dependencies

- `requirements.txt` with pinned versions (exact, not ranges)
- `pip audit` run in CI to check for known vulnerabilities
- Dependabot enabled on GitHub for automated PR creation

### 4.3 Image Build

- Multi-stage builds to minimize final image size
- No build tools, compilers, or package managers in final stage
- `.dockerignore` excludes tests, docs, git history

### 4.4 Image Storage

- Images built locally on Pi (no registry push currently)
- **Future:** Push to GitHub Container Registry with signing via cosign

---

## 5. Runtime Monitoring

### 5.1 Health Checks

```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
  interval: 30s
  timeout: 10s
  retries: 3
  start_period: 10s
```

### 5.2 Logging

- Container logs to stdout/stderr (Docker captures)
- Audit ledger for security-relevant events (append-only)
- Log rotation via Docker daemon config:
  ```json
  {
    "log-driver": "json-file",
    "log-opts": { "max-size": "10m", "max-file": "3" }
  }
  ```

### 5.3 Monitoring Checklist

- [ ] Container restart count (should be 0 in steady state)
- [ ] Memory usage vs limits
- [ ] Audit ledger growth rate
- [ ] Failed authentication attempts
- [ ] Kill switch activations

---

## 6. Incident Response (Container-Specific)

If a container is compromised:

1. **Freeze:** Activate kill switch in freeze mode
2. **Isolate:** `docker network disconnect external <container>`
3. **Preserve:** `docker logs <container> > /tmp/evidence.log`
4. **Kill:** `docker stop <container>`
5. **Investigate:** Inspect image, check for unexpected processes
6. **Rebuild:** Rebuild from clean source, rotate all secrets
7. **Redeploy:** `docker compose up -d`

See [Incident Response Playbook](incident-response.md) for full procedures.
