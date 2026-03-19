# AgentShroud Docker Configuration

**Status**: ✅ **READY TO RUN** (pending API key setup)
**Phase**: 3 (Hardened Container + Persona Integration)
**Last Updated**: February 14, 2026

---

## Quick Start

**Goal**: Working chat interface with Isaiah's personality in <5 minutes.

**See**: [QUICKSTART.md](./QUICKSTART.md) for detailed instructions.

**TL;DR**:
```bash
# 1. Add your Anthropic API key
echo "YOUR_ANTHROPIC_API_KEY" > secrets/anthropic_api_key.txt
chmod 600 secrets/anthropic_api_key.txt

# 2. Start the stack
docker-compose up -d

# 3. Test
curl http://localhost:8080/status
```

---

## Files

### Core Configuration
- **Dockerfile.openclaw** - OpenClaw container (Python 3.11, non-root user)
- **docker-compose.yml** - Full stack orchestration (Gateway + OpenClaw)
- **QUICKSTART.md** - Step-by-step setup guide
- **.gitignore** - Prevents committing secrets

### Secrets
- **secrets/README.md** - API key setup instructions
- **secrets/anthropic_api_key.txt** - Your API key (create this file)

### Documentation
- **README.md** - This file

---

## Architecture

### Container Stack

```
┌─────────────────────────────────────────┐
│  agentshroud-gateway                     │
│  - Port: 127.0.0.1:8080 (localhost only)│
│  - PII sanitization + audit ledger      │
│  - Multi-agent routing                  │
│  - Approval queue (WebSocket)           │
└──────────────┬──────────────────────────┘
               │ (Internal Docker network)
               │ 172.20.0.0/16
               ▼
┌─────────────────────────────────────────┐
│  openclaw-chat                          │
│  - Port: 18789 (internal only, no host) │
│  - Isaiah's persona (IDENTITY, SOUL, USER)│
│  - Security: Non-root, read-only tmpfs  │
│  - Session isolation enabled            │
└─────────────────────────────────────────┘
```

### Security Features (Implemented)

**Container Hardening**:
- ✅ Non-root execution (UID 1000:1000)
- ✅ Capability dropping (`cap_drop: ALL`)
- ✅ No new privileges (`no-new-privileges: true`)
- ✅ tmpfs on /tmp and /var/tmp only (noexec, nosuid)
- ✅ Resource limits (memory: 2GB, CPU: 2 cores, PIDs: 256)
- ✅ Health checks (30s interval, 3 retries)

**Network Isolation**:
- ✅ Internal-only Docker network
- ✅ Gateway bound to 127.0.0.1:8080 ONLY (no LAN access)
- ✅ OpenClaw not exposed to host (internal communication only)
- ✅ No 0.0.0.0 bindings

**Credential Security**:
- ✅ API key via Docker secrets (not environment variables)
- ✅ Mounted at `/run/secrets/anthropic_api_key` (400 permissions)
- ✅ Never logged or exposed in container output
- ✅ .gitignore prevents committing secrets

**Persona Integration**:
- ✅ IDENTITY, SOUL, USER files mounted read-only at `/workspace/`
- ✅ Loaded by OpenClaw on startup
- ✅ Session-scoped (no shared state between conversations)

**Data Persistence**:
- ✅ Gateway ledger: `gateway-data` volume
- ✅ OpenClaw conversations: `openclaw-data` volume
- ✅ Survives container restarts
- ✅ Can be wiped with `docker-compose down -v`

---

## Security Features (Deferred to Phase 5+)

These are planned but not yet implemented (Phase 3 has no skills, no external content):

- 🚧 Read-only root filesystem (requires OpenClaw compatibility testing)
- 🚧 Custom seccomp profile (skill execution hardening)
- 🚧 PromptGuard input filtering
- 🚧 SkillGuard sandboxing
- 🚧 MEMORY.md PII scrubber
- 🚧 Tailscale VPN for remote access
- 🚧 Outbound network allowlisting
- 🚧 ClawSec security suite

**Rationale**: Phase 3 delivers basic chat only. No skills = minimal attack surface. Advanced controls added when skills enabled in Phase 5.

---

## Usage

### Start the Stack

```bash
docker-compose up -d
```

### Check Status

```bash
docker-compose ps

# Expected:
# NAME                STATUS              PORTS
# agentshroud-gateway  Up (healthy)        127.0.0.1:8080->8080/tcp
# openclaw-chat       Up (healthy)
```

### View Logs

```bash
# All containers
docker-compose logs -f

# Specific container
docker-compose logs -f gateway
docker-compose logs -f openclaw
```

### Test Chat

```bash
# Get auth token from gateway logs
docker-compose logs gateway | grep "Generated new token"

# Send message
curl -X POST http://localhost:8080/forward \
  -H "Authorization: Bearer <YOUR_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "What is your expertise in battery energy storage?",
    "source": "api",
    "content_type": "text"
  }'
```

### Stop the Stack

```bash
# Graceful shutdown
docker-compose down

# Nuclear option (deletes all data)
docker-compose down -v
```

---

## Troubleshooting

See [QUICKSTART.md](./QUICKSTART.md) for detailed troubleshooting steps.

**Common Issues**:

1. **Missing API key** → Add to `secrets/anthropic_api_key.txt`
2. **Port 8080 in use** → Stop other services or change port in docker-compose.yml
3. **Container unhealthy** → Check logs: `docker-compose logs <service>`
4. **401 Unauthorized** → Get token from gateway logs
5. **Network errors** → Verify Docker network: `docker network ls`

---

## Development

### Rebuild Containers

```bash
# After code changes
docker-compose up -d --build

# Force rebuild (no cache)
docker-compose build --no-cache
docker-compose up -d
```

### Exec into Container

```bash
# Gateway
docker exec -it agentshroud-gateway bash

# OpenClaw
docker exec -it openclaw-chat bash

# Check user (should be non-root)
docker exec openclaw-chat whoami
# Output: openclaw
```

### Verify Security

```bash
# Check running processes
docker exec openclaw-chat ps aux

# Check file permissions
docker exec openclaw-chat ls -la /workspace/
docker exec openclaw-chat ls -la /run/secrets/

# Check network config
docker network inspect docker_agentshroud-internal

# Verify no external ports on openclaw
docker ps | grep openclaw
# Should show NO host port mappings
```

---

## Next Steps (Phase 4+)

Once chat is working:

1. **iOS Shortcuts** → Forward messages via Gateway API
2. **Shared File Volume** → Mount host directory for file access
3. **Browser Extension** → Forward URLs and selections
4. **Approval Dashboard** → Real-time UI for approval queue
5. **Advanced Security** → ClawSec suite, PromptGuard, SkillGuard
6. **Tailscale VPN** → Remote access via VPN only
7. **Auto-Deploy Scripts** → One-command setup

---

## Reference

**Phase 2 (Gateway)**: [../PHASE2_COMPLETE.md](../PHASE2_COMPLETE.md)
**Phase 3 (Container)**: [../PHASE3_REQUIREMENTS.md](../PHASE3_REQUIREMENTS.md)
**Project Status**: [../README.md](../README.md)
**Working State**: [../WORKING_STATE.md](../WORKING_STATE.md)

---

**Status**: ✅ Ready for user testing
**Pending**: User must add Anthropic API key to `secrets/anthropic_api_key.txt`
**Next**: Follow [QUICKSTART.md](./QUICKSTART.md) to start the stack
