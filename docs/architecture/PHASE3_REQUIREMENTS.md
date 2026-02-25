# Phase 3 Requirements: Working Chat Container

**Status**: READY TO START
**Date**: February 14, 2026
**Prerequisites**: Phase 1 (Complete), Phase 2 (Complete - 89% coverage, 87 tests passing)

---

## Critical Constraint

**Phase 3 MUST deliver a WORKING CHAT INTERFACE FIRST.**

No feature creep. No advanced features until basic chat works. Focus:
1. Basic OpenClaw container that can respond to messages
2. Isaiah's personality loaded
3. Container security hardening (rootless, no LAN, read-only where possible)
4. Integration with Phase 2 gateway (localhost only)

**Test criteria**: Send "Hello" via Gateway → Receive Isaiah-style response → Phase 3 complete.

---

## Part 1: Isaiah's Persona Package

### Core Identity (from IDENTITY.md, SOUL.md, USER.md)

**Name**: Choose during onboarding (suggestions: IsaiahPlays, idallasj_go, IsaiahNextUp)
**Represents**: Isaiah Dallas Jefferson, Jr. - Chief Innovation Engineer at Fluence Energy

### Personality Traits to Embed

**Communication Style**:
- Direct, technically precise, efficient - no fluff
- Command-line first mindset
- Provides context when it matters, not filler words
- "Give me the working solution, not the theory"
- Like a senior engineer in a technical conversation

**Core Values** (to guide decision-making):
- Technical excellence: production-ready, documented, distributable code
- Security first: credentials in env vars, clean git history, least-privilege
- Team empowerment: cross-platform, copy-paste ready, well-commented tools
- Cost consciousness: every resource tagged, justified, right-sized
- Continuous improvement: adopt tools that genuinely improve workflow

**Problem-Solving Approach**:
- Methodical: gather context before acting (check logs, run diagnostics, understand state)
- Reversible changes: dry-run modes, backups, test in staging when possible
- Iterative: rapid feedback cycles, refine quickly
- Escalate appropriately: know when to loop in team vs solve independently

**Technical Background Context**:
- NOT a developer - a systems architect, "gozinta and comesouta guy"
- Gozinta = input ports/signal flow in
- Comesouta = output ports/signal flow out
- Focus on system design, signal flow, input/output requirements

### Professional Context (for relevant responses)

**Current Role**:
- Chief Innovation Engineer - Digital Enablement & Governance
- Fluence Energy (Nasdaq: FLNC), Arlington, VA
- Team: Global Services Digital Enablement & Governance (GSDE&G)
- Focus: Cloud infrastructure, data engineering, security governance, cost optimization

**Team Members** (for context when asked):
- KP (Kasthurica Panigrahy) & Revathi A - Data Engineering (GSDE)
- Tala - Digital Enablement and Advancement (GSDEA)
- Keith - SysOps Reliability Team (SORT)

**Technical Environment** (for contextual awareness):
- Primary OS: macOS (Tahoe)
- Terminals: iTerm2 (primary), Ghostty, Warp
- Shell: zsh with Powerlevel10k
- Tools: tmux (prefix Ctrl-a), conda environments, VS Code
- Languages: Python (primary), Bash scripting, SQL
- Cloud: AWS (Glue, Step Functions, Athena, IAM, S3, SNS, EC2, RDS)
- Networking: Tailscale (domain: tail240ea8.ts.net), hosts named after Hitchhiker's Guide (marvin, trillian, bionic)
- Data lakehouse: 275TB, 23M+ data points

**Industry Expertise** (for technical conversations):
- Battery Energy Storage Systems (BESS): Gridstack, Sunstack, Edgestack
- Industrial protocols: Modbus, DNP3, IEC 61850
- Grid operations: PJM capacity markets, energy dispatch algorithms

### Files to Mount in Container

```yaml
# Container persona files (read-only)
~/.agentshroud/workspace/IDENTITY    → /tobeornottobe/IDENTITY.md
~/.agentshroud/workspace/SOUL.md     → /tobeornottobe/SOUL.md
~/.agentshroud/workspace/USER        → /tobeornottobe/USER.md
```

**Implementation**: Mount these as read-only volumes in docker-compose.yml

---

## Part 2: Phase 3 Feature Scope

### MUST HAVE (Phase 3 - Minimum Viable Chat)

**Container Requirements**:
1. OpenClaw container responding to messages via Gateway
2. Isaiah persona files loaded and active
3. Basic chat functionality only (no skills, no browser, no external services)
4. Security hardening (from 10_skills_to_harden_openclaw.txt):
   - Rootless container (Podman preferred, Docker fallback)
   - Network isolation: `network: internal` + proxy for API calls only
   - Read-only root filesystem: `readOnlyRoot: true`
   - No new privileges: `no-new-privileges: true`
   - Drop all capabilities: `cap_drop: ALL`
   - Memory limits: 2GB default
   - PID limits: 256
   - tmpfs on /tmp and /var/tmp only
   - Bind gateway to localhost only (127.0.0.1:8080)

**Deployment Requirements**:
5. Docker Compose stack: Gateway + OpenClaw containers
6. Gateway → OpenClaw communication via internal Docker network
7. Localhost-only exposure (no LAN, no 0.0.0.0 binding)
8. Auto-generated API token (printed on first start)

**Security Baseline** (non-negotiable):
9. Session isolation enabled (`scope: "session"`, not "shared")
10. mDNS/Bonjour disabled (`OPENCLAW_DISABLE_BONJOUR=1`)
11. Credential injection via Docker secrets (not env vars in docker-compose.yml)
12. Container healthcheck script (verifies rootless, localhost-only binding, file permissions)

### DEFERRED TO PHASE 4+ (Advanced Features)

**From additional_featues/ directory**:

**Phase 4 - Enhanced Productivity**:
- iOS/Mac Shortcuts integration (`create_ios_and_mac_shortcuts.txt`)
- Shared folder with symbolic links (`add_folder_where_files_and_synbolic_links_can_be_shared.txt`)
- Browser extension integration
- Real-time approval dashboard (Gateway WebSocket ready, need frontend)

**Phase 5 - Advanced Security**:
- ClawSec security suite installation (`10_skills_to_harden_openclaw.txt` - skill #1)
- Input filtering / PromptGuard (skill #2)
- SkillGuard sandboxing (skill #3)
- MEMORY.md scrubber (skill #4)
- Credential vault integration (skill #5)
- Read-only reader agent (skill #6)
- Exec approval profiles (skill #7)
- Outbound network allowlisting (skill #8)
- Security vulnerability monitoring agent (`security_agent.txt`)

**Phase 6 - Platform Expansion**:
- Apple containers option (`add_option_to_use_apple_containers_instead_of_docker.txt`)
- Web-based setup wizard (`easy_setup_webpage.txt`)
- Limited-fund digital wallet (`limited_fund_digital_wallet.txt`)

**Phase 7 - Auto-Deploy Hardening**:
- All features from `10_skils_for_the_openclaw_autodeploy_repo.txt`:
  - Hardened docker-compose with network isolation
  - Rootless Podman alternative script
  - Container hardening baseline script
  - VPN-only networking with iptables lockdown (Tailscale integration)
  - Reverse proxy with auth (Nginx/Caddy + TLS)
  - Credential injection via Docker secrets
  - `openclaw security audit` CI/CD integration
  - ClawHub skill scanner pre-install gate
  - Log aggregation & anomaly detection (integrate with Zabbix)
  - Automated health check & drift detection script

---

## Part 3: Security Requirements for Base Container

### Must-Implement Security Controls (from 10_skills_to_harden_openclaw.txt)

**Critical for Phase 3**:

1. **Network Isolation** (Priority 1)
   - Container on internal-only Docker network
   - No LAN access, no internet access except via proxy
   - Gateway bound to 127.0.0.1:8080 ONLY
   - Use Docker network: `internal` mode

2. **Container Hardening** (Priority 1)
   - Run as non-root user (UID 1000 or higher)
   - `readOnlyRoot: true` with tmpfs exceptions
   - `no-new-privileges: true`
   - `cap_drop: ALL`
   - `pidsLimit: 256`
   - Memory limit: 2GB
   - CPU limit: 2 cores

3. **Session Isolation** (Priority 1)
   - `scope: "session"` in OpenClaw config
   - No shared context between requests
   - DM mode only (no open mode)

4. **Service Discovery Disablement** (Priority 1)
   - Set `OPENCLAW_DISABLE_BONJOUR=1`
   - Prevents mDNS broadcasts with filesystem paths

5. **File Permissions** (Priority 2)
   - `~/.openclaw/` → 700 (owner only)
   - `agentshroud.yaml` → 600 (owner read/write only)
   - Verify on every container start

6. **Credential Management** (Priority 2)
   - API keys via Docker secrets (not environment variables)
   - Mount secrets as files at `/run/secrets/`
   - Never log credentials

### Deferred Security Controls (Phase 5+)

- PromptGuard input filtering
- SkillGuard least-privilege sandboxing
- MEMORY.md PII scrubber
- Credential vault integration (Composio)
- Read-only reader agent for untrusted content
- Multi-agent segregation with exec approval profiles
- Outbound network allowlisting
- ClawSec security suite

**Rationale**: Phase 3 has NO skills enabled, NO external content ingestion, NO file access beyond read-only persona files. Attack surface is minimal. Focus on basic container hardening first.

---

## Part 4: Implementation Checklist

### Step 1: Container Configuration (Day 1)

- [ ] Create `docker/Dockerfile.openclaw`
  - Base: `python:3.13-slim` (not latest - for stability)
  - Install OpenClaw dependencies
  - Create non-root user `openclaw` (UID 1000)
  - Set working directory `/home/openclaw/.openclaw`
  - Copy persona files to `/workspace/`
  - Healthcheck: verify process running, localhost binding

- [ ] Create `docker/docker-compose.yml`
  - Service: `agentshroud-gateway` (from Phase 2)
  - Service: `openclaw-chat` (new)
  - Network: `internal` (no external access)
  - Volumes: persona files (read-only), data directory (read/write)
  - Secrets: Anthropic API key
  - Environment: `OPENCLAW_DISABLE_BONJOUR=1`

- [ ] Create `docker/entrypoint.sh`
  - Verify file permissions (700 on ~/.openclaw, 600 on config)
  - Load secrets from `/run/secrets/anthropic_oauth_token`
  - Start OpenClaw with persona files
  - Trap SIGTERM for graceful shutdown

### Step 2: Persona Integration (Day 1)

- [ ] Copy persona files to container workspace
  - Mount `tobeornottobe/IDENTITY.md` → `/workspace/IDENTITY`
  - Mount `tobeornottobe/SOUL.md` → `/workspace/SOUL.md`
  - Mount `tobeornottobe/USER.md` → `/workspace/USER`
  - All mounted read-only

- [ ] Configure OpenClaw to load persona on startup
  - Add system prompt loader in entrypoint
  - Verify persona active in first response

### Step 3: Security Hardening (Day 2)

- [ ] Implement container security baseline
  - Rootless user (UID 1000)
  - Read-only root filesystem with tmpfs exceptions
  - Drop all capabilities
  - Memory/CPU limits
  - PID limit

- [ ] Create healthcheck script (`docker/healthcheck.sh`)
  - Verify OpenClaw process running as non-root
  - Verify gateway bound to 127.0.0.1 only
  - Verify file permissions (700, 600)
  - Verify network isolation (no routes to LAN)
  - Exit 0 if healthy, exit 1 if unhealthy

- [ ] Test security controls
  - Attempt to escalate privileges → should fail
  - Attempt to access LAN → should fail
  - Attempt to modify read-only files → should fail
  - Attempt to spawn excessive processes → should fail

### Step 4: Integration Testing (Day 2)

- [ ] End-to-end test: Gateway → OpenClaw → Response
  - Start stack: `docker-compose up -d`
  - Send test message via Gateway API
  - Verify OpenClaw receives message
  - Verify response reflects Isaiah's persona
  - Verify response returned to Gateway
  - Verify ledger entry created

- [ ] Security validation test
  - Run `docker inspect openclaw-chat` → verify security settings
  - Run healthcheck manually → verify all checks pass
  - Attempt network access from container → verify blocked
  - Check logs for any privilege escalation attempts

### Step 5: Documentation (Day 3)

- [ ] Create `docker/README.md`
  - Quick start guide
  - Security architecture diagram
  - Troubleshooting common issues
  - How to verify security controls

- [ ] Update `PHASE3_COMPLETE.md` (after all tests pass)
  - What was built
  - Security controls implemented
  - Test results
  - Known limitations
  - Next steps (Phase 4)

---

## Success Criteria

**Phase 3 is COMPLETE when**:

1. ✅ OpenClaw container running as non-root (UID 1000+)
2. ✅ Gateway → OpenClaw → Response flow working
3. ✅ Response demonstrates Isaiah's personality (direct, technical, efficient)
4. ✅ Container bound to localhost only (127.0.0.1)
5. ✅ Network isolation verified (no LAN, no internet except via proxy)
6. ✅ Read-only root filesystem active (tmpfs exceptions only)
7. ✅ All security baseline controls passing healthcheck
8. ✅ Ledger entry created for every message
9. ✅ No warnings or errors in logs
10. ✅ Docker Compose can be stopped/started cleanly

**Test Command**:
```bash
# From host machine
curl -X POST http://localhost:8080/forward \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Hello, what is your primary area of expertise?",
    "source": "api",
    "content_type": "text"
  }'

# Expected response should include:
# - Reference to energy storage, BESS, or grid technology
# - Direct, technical tone (no fluff)
# - Mention of systems architecture or Fluence Energy context
```

---

## Timeline

**Day 1**: Container configuration + persona integration (4-6 hours)
**Day 2**: Security hardening + integration testing (4-6 hours)
**Day 3**: Documentation + validation (2-3 hours)

**Total**: 10-15 hours to working chat MVP

---

## Notes

**Gozinta/Comesouta Mindset**:
- Gateway = Gozinta (user data flows in)
- OpenClaw = Processing (signal transformation)
- Gateway response = Comesouta (processed response flows out)
- Keep it simple: one input port, one output port, clear signal flow

**No Feature Creep**:
- No skills in Phase 3
- No browser extension yet
- No iOS shortcuts yet
- No dashboard UI yet
- Just Gateway + Chat + Persona + Security

**Security Philosophy**:
- Defense in depth, but start with basics
- Container isolation first, advanced controls later
- Fail closed: if healthcheck fails, container stops
- Principle of least privilege: minimal permissions to function

---

## References

**Persona Files**:
- `/Users/ijefferson.admin/Development/agentshroud/tobeornottobe/IDENTITY.md`
- `/Users/ijefferson.admin/Development/agentshroud/tobeornottobe/SOUL.md`
- `/Users/ijefferson.admin/Development/agentshroud/tobeornottobe/USER.md`
- `/Users/ijefferson.admin/Development/agentshroud/tobeornottobe/aboutme.txt`

**Feature Planning**:
- `/Users/ijefferson.admin/Development/agentshroud/additional_featues/10_skills_to_harden_openclaw.txt`
- `/Users/ijefferson.admin/Development/agentshroud/additional_featues/10_skils_for_the_openclaw_autodeploy_repo.txt`
- `/Users/ijefferson.admin/Development/agentshroud/additional_featues/security_agent.txt`

**Phase 2 Deliverables**:
- `/Users/ijefferson.admin/Development/agentshroud/PHASE2_COMPLETE.md`
- Gateway API: 10 endpoints, 89% test coverage, 87 tests passing
- PII sanitization, audit ledger, multi-agent routing, approval queue

**Phase 1 Deliverables**:
- `/Users/ijefferson.admin/Development/agentshroud/docs/PHASE-1-COMPLETION.md`
- Clean slate, new directory structure, configuration templates

---

**Phase 3 Status**: READY TO START
**Next Action**: Create `docker/Dockerfile.openclaw`
**Estimated Completion**: 3 days (10-15 hours total)
