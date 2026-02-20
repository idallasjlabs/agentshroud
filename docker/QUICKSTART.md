# AgentShroud Phase 3 - Quick Start Guide

**Goal**: Get a working chat interface with Isaiah's personality in <5 minutes.

---

## Prerequisites

1. **Docker** or **Docker Desktop** installed
2. **Anthropic API Key** (get from https://console.anthropic.com/)
3. **Phase 2 Gateway** tested and working

---

## Setup (One-Time)

### Step 1: Add Your API Key

```bash
# Navigate to docker directory
cd /Users/ijefferson.admin/Development/agentshroud/docker

# Create API key file
echo "sk-ant-api03-YOUR_KEY_HERE" > secrets/anthropic_api_key.txt

# Set secure permissions
chmod 600 secrets/anthropic_api_key.txt

# Verify
ls -la secrets/anthropic_api_key.txt
# Should show: -rw------- (600 permissions)
```

**IMPORTANT**: Replace `YOUR_KEY_HERE` with your actual Anthropic API key.

---

## Launch the Stack

### Start Everything

```bash
# From docker directory
docker-compose up -d

# Expected output:
# Creating network "docker_agentshroud-internal"
# Creating volume "docker_gateway-data"
# Creating volume "docker_openclaw-data"
# Building gateway...
# Building openclaw...
# Creating agentshroud-gateway ... done
# Creating openclaw-chat       ... done
```

### Check Status

```bash
# View running containers
docker-compose ps

# Expected output:
# NAME                STATUS              PORTS
# agentshroud-gateway  Up (healthy)        127.0.0.1:8080->8080/tcp
# openclaw-chat       Up (healthy)

# View logs
docker-compose logs -f

# Press Ctrl+C to stop following logs
```

---

## Test the System

### 1. Health Check (Gateway)

```bash
curl http://localhost:8080/status

# Expected response:
# {
#   "status": "healthy",
#   "version": "0.1.0",
#   "uptime_seconds": 12.34,
#   "ledger_entries": 0,
#   "pending_approvals": 0,
#   "pii_engine": "regex",
#   "config_loaded": true
# }
```

### 2. Get Auth Token (Gateway)

```bash
# View gateway logs to find auto-generated token
docker-compose logs gateway | grep "Generated new token"

# Copy the token (looks like: a1b2c3d4e5f6...)
# Save it for the next step
```

### 3. Send Test Message

```bash
# Replace YOUR_TOKEN with the token from step 2
curl -X POST http://localhost:8080/forward \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Hello! What is your primary area of expertise?",
    "source": "api",
    "content_type": "text"
  }'

# Expected response:
# {
#   "id": "abc123...",
#   "sanitized": true,
#   "redactions": [],
#   "redaction_count": 0,
#   "content_hash": "sha256:...",
#   "forwarded_to": "openclaw-chat",
#   "timestamp": "2026-02-14T20:30:00Z"
# }
```

### 4. Verify Isaiah's Personality

The response should demonstrate:
- **Direct, technical tone** (no fluff)
- **Relevant expertise** (energy storage, BESS, grid tech, or cloud infrastructure)
- **Systems architect perspective** (not "I'm just an AI")

Example expected response:
> "My primary focus is cloud infrastructure and data engineering for battery energy storage systems at Fluence Energy. I architect solutions for grid operations, handle 275TB data lakehouses, and work across AWS services (Glue, Athena, Step Functions). What specific area are you interested in?"

---

## Troubleshooting

### Container Won't Start

```bash
# Check logs for errors
docker-compose logs gateway
docker-compose logs openclaw

# Common issues:
# - Missing API key: Add to secrets/anthropic_api_key.txt
# - Port conflict: Stop other services using port 8080
# - Permission denied: Run chmod 600 on API key file
```

### API Key Error

```bash
# Verify secret file exists
ls -la secrets/anthropic_api_key.txt

# Check content (should show your API key, not example text)
cat secrets/anthropic_api_key.txt

# Rebuild containers after fixing
docker-compose down
docker-compose up -d --build
```

### Gateway Returns 401 Unauthorized

```bash
# Get the current token from gateway logs
docker-compose logs gateway | grep "token"

# Use that token in Authorization header
curl -H "Authorization: Bearer <ACTUAL_TOKEN>" ...
```

### OpenClaw Not Responding

```bash
# Check OpenClaw container health
docker exec openclaw-chat curl -f http://localhost:18789/health

# View OpenClaw logs
docker-compose logs openclaw

# Restart just OpenClaw
docker-compose restart openclaw
```

---

## Stop the Stack

### Graceful Shutdown

```bash
# Stop all containers
docker-compose down

# Expected output:
# Stopping openclaw-chat       ... done
# Stopping agentshroud-gateway  ... done
# Removing openclaw-chat       ... done
# Removing agentshroud-gateway  ... done
# Removing network docker_agentshroud-internal
```

### Nuclear Option (Reset Everything)

```bash
# Stop and remove all data (WARNING: deletes conversation history!)
docker-compose down -v

# Rebuild from scratch
docker-compose up -d --build
```

---

## Next Steps

Once chat is working:

1. **Save your auth token** → Add to `agentshroud.yaml` under `gateway.auth_token`
2. **Test personality** → Ask questions about energy storage, AWS, data engineering
3. **Verify security** → Run security audit script (Phase 3, Day 2)
4. **Add iOS Shortcut** → Forward messages to gateway (Phase 4)
5. **Build dashboard** → Real-time approval UI (Phase 5)

---

## Security Validation

### Verify Isolation

```bash
# Check network configuration
docker network inspect docker_agentshroud-internal

# Verify no external ports on openclaw
docker ps | grep openclaw
# Should show NO port mappings (only "expose")

# Verify running as non-root
docker exec openclaw-chat whoami
# Should output: openclaw (not root)
```

### Check File Permissions

```bash
# Verify persona files are read-only
docker exec openclaw-chat ls -la /workspace/

# Verify secret permissions
docker exec openclaw-chat ls -la /run/secrets/
# Should show: -r-------- (400 permissions)
```

---

## Architecture Diagram

```
┌─────────────────┐
│  Your Machine   │
│  localhost:8080 │
└────────┬────────┘
         │ (Gateway API)
         ▼
┌─────────────────────────────────┐
│  agentshroud-gateway container   │
│  - PII sanitization             │
│  - Audit ledger                 │
│  - Routing                      │
└────────┬────────────────────────┘
         │ (Internal Docker network)
         │ 172.20.0.x
         ▼
┌─────────────────────────────────┐
│  openclaw-chat container        │
│  - Isaiah's personality         │
│  - No external network          │
│  - Non-root (UID 1000)          │
└─────────────────────────────────┘
```

---

## Success Criteria

Phase 3 is complete when:

- ✅ Gateway returns HTTP 200 on `/status`
- ✅ OpenClaw container running as `openclaw` user (UID 1000)
- ✅ Auth token auto-generated and captured
- ✅ Test message forwarded successfully
- ✅ Response demonstrates Isaiah's personality
- ✅ No external ports exposed on openclaw container
- ✅ Persona files mounted read-only at `/workspace/`
- ✅ Ledger entry created in gateway database
- ✅ Stack can be stopped/started cleanly

---

**Ready to start? Run**: `docker-compose up -d`

**Need help?** Check logs: `docker-compose logs -f`

**Phase 3 Status**: Ready for first run (pending API key setup)
