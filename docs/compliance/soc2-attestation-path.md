# SOC 2 Type II — Attestation Path & Go/No-Go Scoping

<!-- AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633) -->
<!-- Patent Pending — U.S. Provisional Application No. 64/018,744 -->
<!-- Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited. -->

**Status:** Scoping / decision doc · compiled 2026-07-12 (Jira SCRUM-99)
**Decision requested of owner:** GO / NO-GO / DEFER on pursuing a SOC 2 Type II attestation.
**Deliverable scope (per ticket):** readiness assessment against existing controls, auditor-selection considerations, indicative cost/timeline — **a recommendation with budget, not the audit itself.**

> **Estimate caveat:** dollar figures and durations below are *indicative market ranges* for a small single-product company (knowledge-cutoff, not vendor quotes). Marked `[indicative]`. Real numbers require RFPs to 2–3 auditors + a compliance-automation vendor. Nothing here is a commitment.

---

## Why this is on the board

The competitive matrix (Hermes report 2026-07-07) credits AgentShroud with "SOC 2 / compliance" coverage, but competitor **MintMCP holds a real SOC 2 Type II audit + HIPAA BAA** and AgentShroud does not. The positioning briefs (`.obsidian-vaults/agentshroud-business/competitors.md`) already enforce the honest line — *"IEC 62443-aligned, audit-chain evidence, SOC 2 attestation in progress"* — never implying a completed attestation. This doc decides whether "in progress" should become real work now.

---

## What SOC 2 Type II actually requires

SOC 2 is an AICPA attestation (SSAE 18) by a licensed CPA firm that a service org's controls, mapped to the Trust Services Criteria (TSC), are **suitably designed (Type I) and operating effectively over an observation window, typically 3–12 months (Type II)**.

| TSC category | Required? | AgentShroud posture |
|---|---|---|
| **Security** (Common Criteria) | Mandatory | Strong — see readiness table |
| Availability | Optional | Partial (single prod instance today; SCRUM-62 canary/2nd-host adds redundancy) |
| Confidentiality | Optional | Strong (PII sanitizer, encrypted store, egress control) |
| Processing Integrity | Optional | Partial (audit hash-chain covers integrity of records, not of agent output) |
| Privacy | Optional | Partial (redaction yes; formal privacy notice/consent lifecycle no) |

**Recommended scope for a first audit: Security (CC) only.** Adding categories multiplies control count and cost; Security is the criterion buyers actually ask for.

---

## Readiness assessment — existing controls vs SOC 2 Common Criteria

Maps the CC series to shipped modules (all cited files verified to exist in the EU AI Act matrix work, SCRUM-96). "Evidence" = what an auditor samples over the observation window.

| CC ref | Control area | AgentShroud control (module) | Readiness | Evidence source |
|---|---|---|---|---|
| CC1 | Control environment / governance | Agent role matrix, GSD cadence (`docs/governance/`) | **Amber** — documented, needs formal policy set + org chart | Governance docs, this repo |
| CC2 | Communication / info | Web control center, audit export (`gateway/security/audit_export.py`) | Green | Dashboards, CEF/JSON-LD exports |
| CC3 | Risk assessment | Canary self-tests, drift detector, resource guard (`gateway/security/canary.py`, `drift_detector.py`) | Green | Alert log, drift snapshots |
| CC4 | Monitoring | AlertDispatcher → Telegram, cron failure monitor (`gateway/security/alert_dispatcher.py`, `cron_state_monitor.py` — SCRUM-61) | Green | `alerts.jsonl`, alert history |
| CC5 | Control activities | Approval queue, RBAC, ToolACL (`gateway/approval_queue/`, `gateway/security/rbac_config.py`, `tool_acl.py`) | Green | Approval records, ACL denials |
| CC6 | **Logical & physical access** | RBAC, session isolation, credential isolation, progressive-trust ladder (`gateway/security/session_manager.py`, `trust_manager.py` — SCRUM-78) | Green | Access logs, trust ledger |
| CC7 | **System operations** (incident detection/response) | Kill switch, progressive lockdown, security sidecars (Falco/ClamAV/Trivy/Wazuh) (`gateway/security/killswitch_monitor.py`, `progressive_lockdown.py`) | Green | Killswitch verification logs, sidecar reports |
| CC8 | Change management | Branch→PR→admin-merge discipline, `pre-deploy` rollback tags, post-deploy checks (`scripts/post-deploy-check.sh`) | **Amber** — practiced, needs written change-mgmt policy + ticket linkage (this Jira board is the start) | Git history, PRs, Jira |
| CC9 | Risk mitigation (vendor / BCP) | — | **Red** — no formal vendor-risk register or BCP/DR runbook | GAP |

**Net readiness:** technically strong (most CC green on control existence), but SOC 2 grades **process + documentation**, not just capability. The gaps are organizational: formal written policies (infosec, access, change-mgmt, incident-response, vendor-risk, BCP/DR), an owned risk register, and continuous evidence collection over the window.

---

## Cost & timeline (indicative)

| Item | `[indicative]` range | Notes |
|---|---|---|
| Compliance-automation platform (Vanta/Drata/Secureframe-class) | $7k–$25k / yr | Automates evidence collection + control monitoring; strongly recommended for a small team |
| Readiness assessment / gap analysis (optional pre-audit) | $5k–$15k | Or self-serve via the automation platform |
| Type II audit (CPA firm, Security-only) | $12k–$40k | Higher with more TSC categories |
| Internal effort | ~0.25–0.5 FTE for 3–6 months | Policy authoring, evidence, auditor liaison — the real cost for a solo/small team |
| Observation window | 3 months (minimum, "Type II bridge") to 12 months | Buyers often accept a 3-month initial window |
| **Time to first report** | **~4–7 months** from GO | Window + audit fieldwork + report drafting |

**Rough first-year cash:** `[indicative]` **$25k–$80k** depending on automation vendor + auditor + TSC scope, plus meaningful founder time.

---

## Recommendation

**DEFER with a low-cost preparatory track — revisit GO in ~1–2 quarters.**

Rationale:
1. **Technical controls are audit-ready; organizational process/documentation is not.** Spending audit dollars now would front-load cost against gaps that are cheap to close first (write the policies, stand up evidence automation).
2. **Sales signal, not yet sales blocker.** SOC 2 becomes GO the moment a real prospect makes it a purchase condition. Until then, the honest positioning line ("attestation in progress") plus the IEC 62443 matrix + audit-chain evidence carries enterprise conversations.
3. **Availability criterion wants the 2nd prod instance first** (SCRUM-62). If Availability is ever in scope, sequence canary/multi-host before the audit window opens.

**Preparatory track to start now (cheap, compounding, no audit commitment):**
- [ ] Adopt a compliance-automation platform trial; connect this repo + cloud accounts for continuous evidence
- [ ] Author the written policy set (infosec, access control, change management, incident response, vendor risk, BCP/DR) — the CC1/CC8/CC9 ambers/reds
- [ ] Stand up a risk register (this Jira project is the muscle memory)
- [ ] Keep the change-management story tight: every prod change already flows branch→PR→tag→post-deploy-check; ensure Jira linkage is consistent
- [ ] Re-evaluate GO when either (a) a prospect requires it, or (b) the policy set + automation are in place and the 3-month window is cheap to run

**Flip to GO immediately if:** an enterprise deal is gated on SOC 2 — at which point the preparatory track collapses the time-to-report.

---

## Tracking

- Parent: SCRUM-99 (this doc) · epic SCRUM-66 (v1.3 platform)
- Related gaps: EU AI Act matrix §4 #1 (`docs/compliance/eu-ai-act-nist-matrix.md`), positioning briefs honesty guardrail
- Availability dependency: SCRUM-62 (canary / 2nd prod instance)

---

*AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. — USPTO Serial No. 99728633.*
*Not legal or audit advice; figures are indicative and require vendor RFPs before any commitment.*
