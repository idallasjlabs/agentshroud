# AgentShroud™ — Session Context

## Project Identity

| Field | Value |
|-------|-------|
| **Product** | AgentShroud™ — Enterprise Governance Proxy for Autonomous AI Agents |
| **Trademark** | AgentShroud™ — Isaiah Dallas Jefferson, Jr. — Federal registration pending |
| **Current Branch** | `feat/v0.9.0-soc-team-collab` ("Sentinel") |
| **Current Version** | v0.9.0 |
| **Target Version** | v1.0.0 |
| **Language** | Python 3.9+ |
| **Test Coverage** | 94% — 3,404 tests total; maintain or improve |

---

## Architecture Summary

AgentShroud sits as a transparent proxy between AI agents (Claude Code, Gemini CLI, Codex,
OpenClaw) and the systems they interact with. Every API call, file write, cloud change, and
tool invocation is intercepted, inspected, logged, and policy-enforced without disrupting
the agent's native workflow.

```
AI Agent → AgentShroud Gateway (33 security modules) → Target System
```

**Control surfaces:** Telegram, iOS Shortcuts, Browser Extension, SSH, REST API — all over Tailscale.

---

## Key Source Directories

| Path | Contents |
|------|----------|
| `gateway/` | Core proxy, runtime, approval queue, ingest API, SSH proxy |
| `gateway/security/` | All 33 security modules |
| `gateway/soc/` | SOC team collaboration features (v0.9.0 focus) |
| `gateway/proxy/` | Request interception and routing |
| `gateway/runtime/` | Agent runtime management |
| `gateway/approval_queue/` | Human-in-the-loop approval workflow |
| `gateway/web/` | Web control center (7-page dashboard) |
| `dashboard/` | Terminal control center (TUI + chat console) |
| `cli/` | CLI interface |
| `chatbot/` | Telegram bot integration |
| `browser-extension/` | Browser extension |
| `docker/` | Container stack (Falco, ClamAV, Wazuh, Fluent Bit) |
| `scripts/` | Build, security scan, deployment scripts |
| `gateway/tests/` | Primary test suite |

---

## v0.9.0 "Sentinel" — Active Feature Set

Three tranches delivered; all 33 security modules active (no stubs):

| Tranche | Feature | Key Files |
|---------|---------|-----------|
| T1 | True Collaboration Architecture | `gateway/security/delegation.py`, `shared_memory.py`, `rbac.py` |
| T2 | Private Service Data Isolation | `gateway/security/tool_acl.py`, `privacy_policy.py` |
| T3 | IEC 62443 Security Tools | `.semgrep.yml`, `docker/falco/`, `docker/wazuh/`, `scripts/security-scan.sh` |

**New in T1:** Owner-away privilege delegation, group shared memory, `Role.OPERATOR`
**New in T2:** Per-user/group tool ACL (PRIVATE/ADMIN/COLLABORATOR tiers), service privacy tiers
**New in T3:** Trivy CVE scan, Syft SBOM, Cosign signing, OpenSCAP CIS, Semgrep SAST

---

## Security Module Registry (33 Active)

**P0 — Core Pipeline:** PromptGuard, TrustManager, EgressFilter, PII Sanitizer, Gateway Binding
**P1 — Middleware:** SessionManager, TokenValidator, ConsentFramework, SubagentMonitor, AgentRegistry + 7 original
**P2 — Network:** 5 modules active in web proxy
**P3 — Infrastructure:** AlertDispatcher, DriftDetector, EncryptedStore, KeyVault, Canary, ClamAV, Trivy, Falco, Wazuh, HealthReport

---

## Constraints for This Repository

1. **Trademark protection** — Never remove or alter AgentShroud™ trademark notices.
2. **Test coverage** — Must stay ≥94%. All new code requires tests before merge.
3. **No module stubs** — Every security module must be fully wired in the pipeline; no dead code.
4. **IEC 62443 alignment** — Security changes must reference IEC 62443 Foundational Requirements (FRs).
5. **Semgrep rules** — New code must pass `.semgrep.yml` SAST rules (CWE-78, CWE-22, CWE-798, CWE-918, CWE-502, SQL injection).
6. **Docker sidecar integrity** — Do not remove or stub `falco`, `clamav`, `wazuh-agent`, or `fluent-bit` services.
7. **Approval queue** — Any agent action that touches `email_sending`, `file_deletion`, `external_api_calls`, or `skill_installation` must route through the approval queue.
8. **PII redaction** — presidio engine at 0.9 confidence minimum; do not lower threshold.

---

## Development Commands

```bash
# Run full test suite
pytest

# Run with coverage
pytest --cov=gateway --cov-report=term-missing

# Lint + format
ruff check .
black .

# Security scan (build-time)
scripts/security-scan.sh

# Start gateway (Docker)
docker-compose -f docker-compose.secure.yml up

# Start with security sidecars
docker-compose -f docker-compose.sidecar.yml up
```

---

## Path to v1.0.0

v0.9.0 → v1.0.0 is a hardening and stabilization release. No net-new security modules.
Focus areas:
- SOC team collaboration production-hardening (v0.9.0 feature set)
- Performance benchmarking under load
- Full IEC 62443 audit pass
- Public documentation and onboarding materials
