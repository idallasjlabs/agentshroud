# EU AI Act & NIST Alignment Matrix — AgentShroud™

<!-- AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633) -->
<!-- Patent Pending — U.S. Provisional Application No. 64/018,744 -->
<!-- Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited. -->

**Status:** Living document · compiled 2026-07-11 (Jira SCRUM-96)
**Regulatory anchor:** Regulation (EU) 2024/1689 (the "EU AI Act"), fully enforceable for high-risk systems **2026-08-02** · NIST AI RMF 1.0 · NIST AI Agent Standards Initiative (launched 2026-02-18)

---

## Positioning

AgentShroud is a **governance proxy for deployers of autonomous AI agents** — it is not
itself an AI system provider under the Act. Organizations that deploy agents
(OpenClaw, Hermes, or any proxied agent) inherit deployer obligations under Art. 26
and, where their use case is high-risk (Annex III), the operational halves of
Art. 9–15. AgentShroud's role is **compliance enabler**: it supplies the technical
controls — logging, human oversight, PII governance, robustness measures — that those
obligations require, at the proxy layer, without modifying the agent.

This matrix maps each relevant obligation to the **actual shipped module** that
implements the control. Per this repository's no-security-theater rules, every claim
cites a real file; requirements without a current control are listed as **GAP** in
§4 — the gap list is part of the deliverable.

---

## 1. EU AI Act — high-risk operational requirements

| Article | Requirement (operative summary) | AgentShroud control | Evidence module |
|---|---|---|---|
| **Art. 9** Risk management | Continuous, iterative risk identification and mitigation across the lifecycle | 76-module inspection pipeline on every message/tool call; periodic pipeline self-verification; container config drift detection; resource anomaly alerts | `gateway/security/canary.py` (pipeline working-state verification), `gateway/security/drift_detector.py`, `gateway/security/alert_dispatcher.py` |
| **Art. 10** Data governance | Personal data minimization and protection in operation | PII detection/redaction at ≥0.9 confidence (presidio) on inbound content; differential PII detection on tool RESULTS (adversarially formatted exfiltration); redaction before any external egress incl. alerts | `gateway/ingest_api/sanitizer.py`, `gateway/security/differential_pii_detector.py`, `gateway/ingest_api/alert_telegram_relay.py` (sanitize-before-egress) |
| **Art. 12** Record-keeping | Automatic event logging over the system lifetime, sufficient for traceability | Tamper-evident SHA-256 hash-chained audit store; append-only ingest ledger with content hashes; alert log persisted before notification | `gateway/security/audit_store.py`, `gateway/ingest_api/ledger.py`, `gateway/security/alert_dispatcher.py` |
| **Art. 13** Transparency to deployers | Operation sufficiently transparent for deployers to interpret output and use | Web control center + SOC views over live pipeline decisions; per-event bus with dashboard streaming; audit export in standard formats | `gateway/web/` (7-page control center), `gateway/ingest_api/event_bus.py`, `gateway/security/audit_export.py` (CEF / JSON-LD / JSON) |
| **Art. 14** Human oversight | Natural persons can effectively oversee, intervene, and interrupt | Human-in-the-loop approval queue for high-risk actions (email send, file deletion, external API calls, skill installation); egress approvals with inline owner controls; verified kill switch (FREEZE / SHUTDOWN) | `gateway/approval_queue/`, `gateway/proxy/telegram_egress_notify.py`, `gateway/security/killswitch_monitor.py` |
| **Art. 15** Accuracy, robustness, cybersecurity | Resilience against errors, faults, manipulation attempts | Prompt-injection defense; egress firewall (default-deny allowlist); output canary tokens for prompt-leak detection; provider-failure resilience (multi-provider overload/quota failover keeps operations on a governed local model) | `gateway/security/prompt_guard.py`, `gateway/security/egress_filter.py`, `gateway/security/output_canary.py`, `gateway/proxy/llm_quota_detector.py` |
| **Art. 26** Deployer obligations | Use per instructions, assign competent oversight, monitor operation, keep logs | RBAC with owner/roles; per-user session isolation; sub-agent oversight; per-agent container isolation registry; cron/job failure monitoring with owner alerting | `gateway/security/rbac_config.py`, `gateway/security/session_manager.py`, `gateway/security/subagent_monitor.py`, `gateway/security/agent_isolation.py`, `gateway/security/cron_state_monitor.py` |
| **Art. 12/26** Log retention | Logs kept for an appropriate period | Memory lifecycle manager — retention windows and integrity checks (R-19) | `gateway/security/memory_lifecycle.py` |

**GPAI note (Chapter V):** AgentShroud deployments consume general-purpose models via
API (Anthropic/OpenAI/Google/local). GPAI *provider* obligations sit with the model
vendors; AgentShroud's contribution is the deployer-side audit trail of every model
interaction (`gateway/proxy/llm_proxy.py` — all LLM traffic proxied and logged).

---

## 2. NIST AI RMF 1.0 mapping

| Function | AgentShroud implementation | Evidence |
|---|---|---|
| **GOVERN** | Role-based access, trust levels, tool ACLs, documented governance (AGENT_ROLES, GSD cadence) | `gateway/security/rbac_config.py`, `gateway/security/trust_manager.py`, `docs/governance/` |
| **MAP** | Per-agent registry and isolation verification; MCP server consent framework (pre-execution config validation) | `gateway/security/agent_isolation.py`, `gateway/security/consent_framework.py` |
| **MEASURE** | Canary self-tests, drift detection, resource guard, benchmark baselines | `gateway/security/canary.py`, `gateway/security/drift_detector.py`, `.benchmarks/baseline-v1.0.0.json` |
| **MANAGE** | Alert dispatch → owner Telegram within seconds; approval queue; kill switch; progressive lockdown | `gateway/security/alert_dispatcher.py`, `gateway/ingest_api/alert_telegram_relay.py`, `gateway/approval_queue/`, `gateway/security/killswitch_monitor.py` |

## 3. NIST AI Agent Standards Initiative (2026) — identity & authorization themes

The Initiative's concept paper ("Accelerating the Adoption of Software and AI Agent
Identity and Authorization", comment period closed 2026-04-02) centers on agent
identity, scoped authorization, and revocation. [verify: final framework text when
published]

| Theme | AgentShroud control | Evidence |
|---|---|---|
| Agent identity | Per-agent registry with container isolation verification; per-bot Telegram token identity | `gateway/security/agent_isolation.py`, BotConfig registry (`gateway/ingest_api/bot_config.py`) |
| Scoped authorization | MCP token claim validation (audience/issuer/scope/expiry) before passthrough; per-level tool ACLs | `gateway/security/token_validation.py`, `gateway/security/trust_manager.py` |
| Progressive/earned autonomy | Trust ladder — agents earn capability over time | `gateway/security/trust_manager.py` (enforcement rollout tracked in SCRUM-78) |
| Revocation / kill switch | Automated kill-switch verification (<1 s FREEZE, <5 s SHUTDOWN targets) | `gateway/security/killswitch_monitor.py` |

---

## 4. Honest gap list (with tracking)

| # | Gap | Impact | Action / tracking |
|---|---|---|---|
| 1 | No formal third-party attestation (SOC 2 Type II) backing the control claims | Enterprise procurement friction; competitor MintMCP holds a real audit | Scoping in **SCRUM-99** (go/no-go with budget) |
| 2 | No packaged conformity-assessment support kit (deployer-facing evidence bundle: control descriptions, log samples, DPIA input template) | Deployers assemble evidence manually | Extend this matrix into a deployer kit; candidate v1.2 marketing/compliance work under **SCRUM-54** |
| 3 | ProgressiveTrust ladder enforcement defaults OFF (monitor-only) | Art. 26 "competent oversight" story is partially aspirational until enforced | **SCRUM-78** (staged monitor→enforce rollout) |
| 4 | Art. 13 instructions-for-use: no single operator manual consolidating interpretation of pipeline decisions | Transparency obligation met by dashboards, not docs | Fold into docs backlog; candidate for the v1.2 WS-E audit outputs (**SCRUM-72**) |
| 5 | Historical open findings (29) not yet individually verified against current main | Unverified claims would be security theater | **SCRUM-95** triage feeds WS-E.3 fix-or-accept (**SCRUM-74**) |
| 6 | EU AI Act final harmonized standards (CEN-CENELEC) not yet mapped item-by-item | Mapping is at article level, not standard level | Revisit when harmonized standards publish [verify] |

---

## 5. Evidence trail — where an auditor looks

| Evidence | Location | Producer |
|---|---|---|
| Tamper-evident audit chain | gateway data volume (SHA-256 hash chain) | `gateway/security/audit_store.py` |
| Ingest ledger (all forwarded content, hashed) | `gateway-data` volume | `gateway/ingest_api/ledger.py` |
| Security alerts (persisted before notification) | `/tmp/security/alerts/alerts.jsonl` in-container | `gateway/security/alert_dispatcher.py` |
| Approval decisions (human oversight record) | approval queue store | `gateway/approval_queue/` |
| Standardized exports for SIEM/GRC | CEF / JSON-LD / JSON | `gateway/security/audit_export.py` |
| Runtime enforcement status | `/status` endpoint + web control center | `gateway/ingest_api/main.py`, `gateway/web/` |

---

*AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. — USPTO Serial No. 99728633.*
*Patent Pending — U.S. Provisional Application No. 64/018,744.*
*This document is positioning/enablement material, not legal advice; final compliance determinations rest with each deployer's counsel.*
