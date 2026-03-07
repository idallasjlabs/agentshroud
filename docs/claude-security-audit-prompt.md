# AgentShroud v0.8.0 — Full Security & Functionality Audit

## Context for Claude

You are being asked to perform a **full security audit and functional verification** of the AgentShroud v0.8.0 codebase. This is a production system. Be thorough, adversarial, and specific.

---

## What is AgentShroud?

AgentShroud is a **security proxy framework for autonomous AI agents**. The core premise:

1. **Fully enclosed bots** — The AI agent (OpenClaw bot) runs in a Docker container with NO direct internet access. ALL outbound traffic routes through a security gateway that inspects, filters, and logs everything.

2. **Log everything** — Every inbound message, outbound response, tool call, API request, and security decision is logged to an audit trail. Nothing happens silently.

3. **Protect everything** — 34 security modules form a defense-in-depth stack: PII redaction, prompt injection detection (35 languages), egress firewalling, DNS-level blocking (77K domains via Pi-hole), file sandboxing, session isolation, trust scoring, and more.

4. **Separate sessions for collaborators** — The bot owner (Isaiah) has full access. Collaborators (trusted advisors) get isolated sessions with a dedicated agent that has:
   - No exec/shell access
   - No access to owner's memory, credentials, or private files
   - No ability to send messages as the bot, modify config, or access other sessions
   - A mandatory daily disclosure notice that interactions are logged
   - Read-only advisory mode on a cheaper model (Sonnet vs Opus)

5. **Blocked functions for collaborators** — Collaborators cannot use: exec, gateway config, cron jobs, session management, memory access, message sending, browser control, node access, TTS, or PDF analysis. They get web search and file reading within their isolated workspace only.

---

## Architecture

```
┌─────────────────────────────────────────────┐
│  Marvin (Mac Studio, Apple Silicon)         │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │  Colima VM                          │    │
│  │                                     │    │
│  │  ┌──────────────┐  ┌────────────┐   │    │
│  │  │   Gateway     │  │    Bot     │   │    │
│  │  │ (port 8080)   │  │(port 18789)│   │    │
│  │  │ - Security    │  │ - OpenClaw │   │    │
│  │  │   Pipeline    │  │ - Telegram │   │    │
│  │  │ - DNS filter  │  │ - Agent    │   │    │
│  │  │ - LLM proxy   │  │   runtime  │   │    │
│  │  │ - Egress proxy│  │           │   │    │
│  │  │ - CONNECT     │  │           │   │    │
│  │  │   proxy       │  │           │   │    │
│  │  └──────────────┘  └────────────┘   │    │
│  │  Network: 172.10.0.0/16 (internal)  │    │
│  │  Network: 172.11.0.0/16 (isolated)  │    │
│  └─────────────────────────────────────┘    │
└─────────────────────────────────────────────┘
```

**Key constraint:** The bot container has NO direct internet access. HTTP_PROXY and HTTPS_PROXY env vars route all traffic through the gateway's CONNECT proxy on port 8181. DNS resolves through the gateway's built-in Pi-hole forwarder.

---

## The 34 Security Modules

Each module has a tier (P0=critical, P3=auxiliary) and a mode (enforce=blocks bad traffic, monitor/observatory=log only, active=always running).

| # | Module | Tier | Purpose | Mode |
|---|--------|------|---------|------|
| 1 | pii_sanitizer | P0 | Detect/redact PII (names, emails, SSNs, phones) via Presidio NLP | enforce (DISABLED — false positives) |
| 2 | approval_queue | P0 | Require human approval for sensitive ops (iMessage, critical tool calls) | enforce |
| 3 | security_pipeline | P0 | Central pipeline orchestrating all security checks on in/out messages | enforce |
| 4 | prompt_guard | P0 | Detect prompt injection (35 langs, regex, base64, unicode tricks) | observatory (too aggressive for enforce) |
| 5 | trust_manager | P0 | Track agent trust scores, escalate/de-escalate based on behavior | enforce |
| 6 | egress_filter | P0 | Outbound HTTP domain allowlist/denylist | enforce |
| 7 | context_guard | P1 | Detect context window manipulation and conversation hijacking | enforce |
| 8 | metadata_guard | P1 | Strip/sanitize metadata from messages | enforce |
| 9 | log_sanitizer | P1 | Redact secrets and PII from log output | enforce |
| 10 | env_guard | P1 | Prevent env var leakage (/proc/*/environ) | enforce |
| 11 | git_guard | P1 | Prevent git credential exposure | enforce |
| 12 | file_sandbox | P1 | Restrict filesystem access to allowed paths | enforce |
| 13 | resource_guard | P1 | Rate limiting and resource consumption monitoring | enforce |
| 14 | session_manager | P1 | Per-user session isolation and workspace separation | enforce |
| 15 | token_validator | P1 | Authentication token validation and management | enforce |
| 16 | consent_framework | P1 | User consent tracking for data processing | enforce |
| 17 | subagent_monitor | P1 | Monitor/control sub-agent spawning | monitor |
| 18 | agent_registry | P1 | Track registered agents and their permissions | enforce |
| 19 | dns_filter | P2 | DNS-level blocking via Pi-hole blocklists (77,526 domains) | enforce |
| 20 | egress_monitor | P2 | Monitor/log all outbound connections | enforce |
| 21 | browser_security | P2 | Security controls for Playwright browser automation | enforce |
| 22 | oauth_security | P2 | OAuth token validation for API integrations | enforce |
| 23 | network_validator | P3 | Validate network configs, detect anomalies | active |
| 24 | alert_dispatcher | P3 | Route security alerts to Telegram/email by severity | active |
| 25 | killswitch_monitor | P3 | Emergency shutdown via Telegram or API | active |
| 26 | drift_detector | P3 | Detect config drift from known-good baseline | active |
| 27 | encrypted_store | P3 | Encrypted storage for data at rest | active |
| 28 | key_vault | P3 | Secure key management and rotation | active |
| 29 | health_report | P3 | System health monitoring and reporting | active |
| 30 | canary | P3 | Output canary tokens to detect data exfiltration | active |
| 31 | clamav_scanner | P3 | Malware scanning for uploaded files | active |
| 32 | trivy_scanner | P3 | Container vulnerability scanning | active |
| 33 | falco_monitor | P3 | Runtime security monitoring (syscall-level) | active |
| 34 | wazuh_client | P3 | SIEM integration for centralized monitoring | active |

### Additional Security Components

| Component | Purpose | Status |
|-----------|---------|--------|
| RBAC System | Role-based access (Owner/Admin/Collaborator/Viewer) | Active |
| Multi-turn Tracker | Track disclosure risk across conversation turns | Active (owner exemption committed) |
| Telegram Proxy | Reverse proxy for Telegram API with middleware inspection | Active |
| LLM Proxy | Reverse proxy for Anthropic API with content scanning | Active |
| MCP Proxy | Tool call interception and security inspection | Active |
| HTTP CONNECT Proxy | Outbound traffic proxy with domain allowlist | Active |
| DNS Forwarder | Built-in DNS with Pi-hole blocklist integration | Active |

---

## Known Findings (Blue Team Assessment + Steve Hay's Review)

### Open Findings

| ID | Severity | Finding | Module |
|----|----------|---------|--------|
| C3 | CRITICAL | Bot token prefixes printed in debug output — need rotation via @BotFather | — |
| C4 | CRITICAL | Root `/` exposes metrics without auth | health_report |
| C5 | CRITICAL | `/status` exposes security posture without auth | health_report |
| H4 | HIGH | Docker network isolation not verified | network_validator |
| H5 | HIGH | ws-token endpoint returns master auth token | token_validator |
| H6 | HIGH | Session manager path traversal via crafted user ID | session_manager |
| H7 | HIGH | Error messages disclose internal details | log_sanitizer |
| M1 | MEDIUM | No rate limiting on security management endpoints | resource_guard |
| M2 | MEDIUM | subprocess calls have no resource limits | resource_guard |
| M4 | MEDIUM | Pi-hole auth token in URL query string | — |
| M5 | MEDIUM | LLM proxy has no authentication | LLM Proxy |

### Fixed Findings

| ID | Severity | Finding | Fix |
|----|----------|---------|-----|
| C1 | CRITICAL | Hardcoded owner ID in middleware.py | Uses RBACConfig now |
| C2 | CRITICAL | Hardcoded owner ID in webhook_receiver.py | Uses RBACConfig now |
| H1 | HIGH | Telegram proxy middleware_manager None | Fixed |
| H2 | HIGH | FileSandbox regex too broad | Uses path matching now |
| H3 | HIGH | Gateway password in config file | Uses env var now |
| M6 | MEDIUM | Telegram proxy no token validation | Fixed |

### Steve Hay's Specific Findings

Steve (collaborator, Telegram ID 8279589982) tested as an external reviewer:
- **PII sanitizer** was blocking ALL messages due to false positives — had to be disabled
- **Prompt guard** too aggressive in enforce mode — demoted to observatory
- **Multi-turn tracker** caused a 7-hour outage (trust score hit 552) — needs owner exemption
- **/proc/1/environ** still readable inside container (env_guard gap)
- **Path traversal** possible via crafted user ID in session manager
- **No rate limiting** on security management endpoints

---

## Your Tasks

### 1. Code Audit
Review the codebase for:
- Security vulnerabilities not yet found
- Logic errors in the 34 modules
- Bypass opportunities (can the bot escape the proxy? can a collaborator escalate?)
- Credential handling (are secrets properly isolated?)
- Error handling (do errors leak internal state?)

### 2. Verify Open Findings
For each open finding (C3-C5, H4-H7, M1-M5), verify:
- Is it still present?
- What's the actual risk?
- What's the fix?

### 3. Test Each Module
For each of the 34 modules, attempt to:
- Trigger its detection logic
- Bypass its protection
- Verify it actually runs in the security pipeline (not just loaded but wired in)

### 4. Collaborator Isolation
Test that a collaborator session CANNOT:
- Access owner's MEMORY.md, SOUL.md, or daily notes
- Execute shell commands
- Read credentials from 1Password
- SSH to infrastructure
- Send messages as the bot
- Modify gateway config
- Access other users' sessions
- Use blocked skills (1password, healthcheck, skill-creator)

### 5. Update the Module Matrix

After testing, update this table with your findings in the **Claude Tested** column:

| # | Module | Tier | Mode | Peer Reviewed | Blue Team | Steve's Findings | Owner Tested | Collaborator Tested | Claude Tested |
|---|--------|------|------|---------------|-----------|-----------------|--------------|---------------------|---------------|
| 1 | pii_sanitizer | P0 | enforce (OFF) | ✅ R1-R3 | ✅ | False positives — disabled | ⬜ | ⬜ | ⬜ |
| 2 | approval_queue | P0 | enforce | ✅ R1-R3 | ✅ | Working | ⬜ | ⬜ | ⬜ |
| 3 | security_pipeline | P0 | enforce | ✅ R1-R3 | ✅ | Core routing works | ⬜ | ⬜ | ⬜ |
| 4 | prompt_guard | P0 | observatory | ✅ R1-R3 | ✅ | Too aggressive for enforce | ⬜ | ⬜ | ⬜ |
| 5 | trust_manager | P0 | enforce | ✅ R1-R3 | ✅ | No findings | ⬜ | ⬜ | ⬜ |
| 6 | egress_filter | P0 | enforce | ✅ R1-R3 | ✅ | Working | ⬜ | ⬜ | ⬜ |
| 7 | context_guard | P1 | enforce | ✅ R1-R3 | ✅ | No findings | ⬜ | ⬜ | ⬜ |
| 8 | metadata_guard | P1 | enforce | ✅ R1-R3 | ✅ | No findings | ⬜ | ⬜ | ⬜ |
| 9 | log_sanitizer | P1 | enforce | ✅ R1-R3 | ✅ | No findings | ⬜ | ⬜ | ⬜ |
| 10 | env_guard | P1 | enforce | ✅ R1-R3 | ✅ | /proc/1/environ readable | ⬜ | ⬜ | ⬜ |
| 11 | git_guard | P1 | enforce | ✅ R1-R3 | ✅ | No findings | ⬜ | ⬜ | ⬜ |
| 12 | file_sandbox | P1 | enforce | ✅ R1-R3 | ✅ H2 fixed | Regex removed | ⬜ | ⬜ | ⬜ |
| 13 | resource_guard | P1 | enforce | ✅ R1-R3 | ✅ | M1: No rate limiting (OPEN) | ⬜ | ⬜ | ⬜ |
| 14 | session_manager | P1 | enforce | ✅ R1-R3 | ✅ | H6: Path traversal (OPEN) | ⬜ | ⬜ | ⬜ |
| 15 | token_validator | P1 | enforce | ✅ R1-R3 | ✅ | No findings | ⬜ | ⬜ | ⬜ |
| 16 | consent_framework | P1 | enforce | ✅ R1-R3 | ✅ | No findings | ⬜ | ⬜ | ⬜ |
| 17 | subagent_monitor | P1 | monitor | ✅ R1-R3 | ✅ | Default monitor mode | ⬜ | ⬜ | ⬜ |
| 18 | agent_registry | P1 | enforce | ✅ R1-R3 | ✅ | No findings | ⬜ | ⬜ | ⬜ |
| 19 | dns_filter | P2 | enforce | ✅ R1-R3 | ✅ | Working (77K domains) | ⬜ | ⬜ | ⬜ |
| 20 | egress_monitor | P2 | enforce | ✅ R1-R3 | ✅ | No findings | ⬜ | ⬜ | ⬜ |
| 21 | browser_security | P2 | enforce | ✅ R1-R3 | ✅ | No findings | ⬜ | ⬜ | ⬜ |
| 22 | oauth_security | P2 | enforce | ✅ R1-R3 | ✅ | No findings | ⬜ | ⬜ | ⬜ |
| 23 | network_validator | P3 | active | ✅ R1-R3 | ✅ | No findings | ⬜ | ⬜ | ⬜ |
| 24 | alert_dispatcher | P3 | active | ✅ R1-R3 | ✅ | No findings | ⬜ | ⬜ | ⬜ |
| 25 | killswitch_monitor | P3 | active | ✅ R1-R3 | ✅ | No findings | ⬜ | ⬜ | ⬜ |
| 26 | drift_detector | P3 | active | ✅ R1-R3 | ✅ | No findings | ⬜ | ⬜ | ⬜ |
| 27 | encrypted_store | P3 | active | ✅ R1-R3 | ✅ | No findings | ⬜ | ⬜ | ⬜ |
| 28 | key_vault | P3 | active | ✅ R1-R3 | ✅ | No findings | ⬜ | ⬜ | ⬜ |
| 29 | health_report | P3 | active | ✅ R1-R3 | ✅ | No findings | ⬜ | ⬜ | ⬜ |
| 30 | canary | P3 | active | ✅ R1-R3 | ✅ | No findings | ⬜ | ⬜ | ⬜ |
| 31 | clamav_scanner | P3 | active | ✅ R1-R3 | ✅ | Binary available | ⬜ | ⬜ | ⬜ |
| 32 | trivy_scanner | P3 | active | ✅ R1-R3 | ✅ | Binary available | ⬜ | ⬜ | ⬜ |
| 33 | falco_monitor | P3 | active | ✅ R1-R3 | ✅ | No findings | ⬜ | ⬜ | ⬜ |
| 34 | wazuh_client | P3 | active | ✅ R1-R3 | ✅ | No findings | ⬜ | ⬜ | ⬜ |

### Collaborator Access Control Tests

| # | Test Case | Expected | Claude Tested |
|---|-----------|----------|---------------|
| 1 | Send normal message | ✅ Allowed | ⬜ |
| 2 | Use weather skill | ✅ Allowed | ⬜ |
| 3 | Use 1password skill | ❌ Blocked | ⬜ |
| 4 | Use healthcheck skill | ❌ Blocked | ⬜ |
| 5 | Use skill-creator skill | ❌ Blocked | ⬜ |
| 6 | Read MEMORY.md | ❌ Blocked | ⬜ |
| 7 | Read SOUL.md | ❌ Blocked | ⬜ |
| 8 | Access 1Password vault | ❌ Blocked | ⬜ |
| 9 | SSH to hosts | ❌ Blocked | ⬜ |
| 10 | View credentials/secrets | ❌ Blocked | ⬜ |
| 11 | Execute shell commands | ❌ Blocked | ⬜ |
| 12 | Read gateway logs | ❌ Blocked | ⬜ |
| 13 | Send messages as bot | ❌ Blocked | ⬜ |
| 14 | Modify agent config | ❌ Blocked | ⬜ |
| 15 | Access other sessions | ❌ Blocked | ⬜ |

---

## Key Files to Review

- `gateway/ingest_api/main.py` — Main FastAPI app (route entrypoints)
- `gateway/ingest_api/middleware.py` — Security middleware stack
- `gateway/ingest_api/security_pipeline.py` — Central security orchestrator
- `gateway/modules/` — All 34 security module implementations
- `gateway/proxy/` — Telegram, LLM, and MCP proxy implementations
- `gateway/config.py` — RBAC config and security settings
- `docker/docker-compose.yml` — Container networking and isolation
- `docker/config/openclaw/apply-patches.js` — Startup config patching
- `docker/scripts/colima-health-check.sh` — Health monitoring
- `docker/scripts/colima-firewall.sh` — Network firewall rules
- `tests/` — Test suite (2225 tests)

## Output Format

Provide:
1. **Executive summary** — overall security posture assessment
2. **New findings** — anything not already in the known findings list
3. **Verified findings** — confirmation of open findings with current status
4. **Updated module matrix** — with Claude Tested column filled in (✅ pass, ❌ fail, ⚠️ partial, 🔍 needs manual test)
5. **Recommendations** — prioritized action items
