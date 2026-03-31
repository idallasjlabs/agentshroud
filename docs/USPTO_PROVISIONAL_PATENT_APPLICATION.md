# AgentShroud -- USPTO Provisional Patent Application

## Filing Reference

| Field | Value |
|-------|-------|
| **USPTO Form** | PTO/SB/16 (Cover Sheet for Provisional Patent Application) |
| **Filing Method** | Patent Center (electronic) — https://patentcenter.uspto.gov |
| **Your Entity Status** | **Small Entity** |
| **Your Filing Fee** | **$130.00** |
| **Fee (Large Entity)** | $325.00 |
| **CFR Reference** | 37 CFR 1.16(d) |
| **Statute** | 35 U.S.C. Section 111(b) |
| **Pendency** | 12 months (non-extendable) — must file non-provisional within 12 months |

**Entity Status: SMALL ENTITY ($130).** You do not qualify as micro entity due to gross income exceeding the 3x median household income threshold and 4+ prior patent applications. You DO qualify as small entity because AgentShroud is personal IP with no obligation to assign to a large entity. File Form PTO/SB/15 (Certification of Small Entity Status) alongside the application.

---

## SECTION 1: COVER SHEET (Form PTO/SB/16)

### 1.1 Application Type

- [X] Provisional Application for Patent under 35 U.S.C. Section 111(b)

### 1.2 Inventor(s)

| Field | Value |
|-------|-------|
| **Given Name** | Isaiah |
| **Middle Name** | Dallas |
| **Family Name** | Jefferson, Jr. |
| **City** | [YOUR CITY] |
| **State** | [YOUR STATE] |
| **Country** | United States |
| **Citizenship** | United States |

> Add additional inventors if applicable. You are the sole inventor unless others contributed to the conception of the invention (not just implementation).

### 1.3 Title of Invention

**Enterprise Governance Proxy System and Method for Policy-Enforced Interception, Inspection, and Mediation of Autonomous AI Agent Communications with External Systems**

### 1.4 Correspondence Address

| Field | Value |
|-------|-------|
| **Name** | Isaiah Dallas Jefferson, Jr. |
| **Address Line 1** | [YOUR STREET ADDRESS] |
| **City** | [YOUR CITY] |
| **State** | [YOUR STATE] |
| **ZIP** | [YOUR ZIP] |
| **Country** | United States |
| **Phone** | [YOUR PHONE] |
| **Email** | [YOUR EMAIL] |

### 1.5 Attorney/Agent (if applicable)

| Field | Value |
|-------|-------|
| **Name** | N/A (Pro Se filing) |
| **Registration Number** | N/A |
| **Docket Number** | AGENTSHROUD-PROV-2026-001 |

### 1.6 U.S. Government Interest

- [ ] This invention was made with United States Government support.
  - **Note:** If any portion was developed during work hours at Fluence Energy or using Fluence resources, review your employment IP agreement. If the invention is entirely personal and outside scope of employment, check this as N/A.

### 1.7 Entity Status

- [ ] Large Entity
- [X] Small Entity (file PTO/SB/15 concurrently)
- [ ] Micro Entity — NOT ELIGIBLE (income > 3x median + 4+ prior applications)

---

## SECTION 2: WRITTEN DESCRIPTION OF THE INVENTION

> **Instructions:** This is the core of the provisional application. It must comply with 35 U.S.C. Section 112(a) — written description, enablement, and best mode. No formal claims are required for a provisional. The description below is structured to provide maximum breadth of coverage while protecting implementation secrets.

---

### ENTERPRISE GOVERNANCE PROXY SYSTEM AND METHOD FOR POLICY-ENFORCED INTERCEPTION, INSPECTION, AND MEDIATION OF AUTONOMOUS AI AGENT COMMUNICATIONS WITH EXTERNAL SYSTEMS

#### FIELD OF THE INVENTION

The present invention relates generally to computer security systems, and more particularly to a transparent proxy architecture that governs, mediates, and audits all communications between autonomous artificial intelligence (AI) agents and the external systems, services, and resources those agents interact with.

#### BACKGROUND OF THE INVENTION

The rapid adoption of autonomous AI agents — including but not limited to large language model (LLM)-based coding assistants, command-line AI tools, and multi-agent orchestration frameworks — has created a critical governance gap in enterprise IT environments. These agents are capable of executing API calls, file system operations, cloud resource modifications, network communications, and tool invocations with minimal or no human oversight.

Current approaches to AI agent security fall into three categories, each with significant limitations:

1. **Agent-native guardrails** — Security controls embedded within the AI agent itself. These are controlled by the agent vendor, not the enterprise, and can be bypassed, updated, or removed without the deploying organization's knowledge or consent.

2. **Network-level firewalls and proxies** — Traditional perimeter security tools that operate at the network layer. These lack semantic understanding of AI agent behavior, cannot distinguish between legitimate agent actions and policy violations at the application layer, and cannot inspect the content or intent of agent-initiated communications.

3. **Post-hoc audit logging** — Systems that record agent actions after execution. These provide no real-time prevention or mediation capability, leaving the enterprise in a reactive posture.

None of these approaches provide an enterprise-controlled, real-time, semantically-aware governance layer that sits between the AI agent and the systems it interacts with while remaining transparent to the agent's native workflow.

#### SUMMARY OF THE INVENTION

The present invention provides a transparent proxy system (hereinafter "governance proxy") that interposes between one or more autonomous AI agents and the external systems those agents communicate with. The governance proxy intercepts, inspects, policy-evaluates, and conditionally mediates every communication — including but not limited to API calls, file operations, network requests, tool invocations, and messaging platform interactions — without requiring modification to the AI agent itself.

The system comprises the following principal components and capabilities:

**A. Transparent Interception Architecture**

The governance proxy operates as a transparent intermediary, receiving all agent-originated communications destined for external systems. The agent is configured to route traffic through the proxy via standard network mechanisms (HTTP/HTTPS proxy configuration, DNS resolution, API endpoint redirection, or SDK-level patching), such that the agent's native functionality is preserved without code modification. The proxy supports multiple simultaneous AI agents from different vendors operating through the same governance layer.

**B. Multi-Stage Security Pipeline**

Each intercepted communication passes through an ordered pipeline of security modules, organized by priority tier:

- **Priority 0 (P0) — Core Pipeline modules** that perform fundamental security operations including but not limited to: prompt content inspection for injection attacks, trust level assessment of the originating agent and user, egress destination filtering against allowlists and denylists, personally identifiable information (PII) detection and redaction, and cryptographic binding of gateway sessions.

- **Priority 1 (P1) — Middleware modules** that perform session management, authentication token validation, user consent framework enforcement, sub-agent activity monitoring, agent identity registry verification, and additional content filtering operations.

- **Priority 2 (P2) — Network modules** that enforce network-level policies within the web proxy layer, including connection-level restrictions, protocol enforcement, and domain-level access controls.

- **Priority 3 (P3) — Infrastructure modules** that provide runtime security services including alert dispatch, configuration drift detection, encrypted credential storage, cryptographic key management, canary token monitoring, malware scanning integration, container vulnerability scanning, host-based intrusion detection integration, and system health reporting.

The pipeline architecture is extensible, allowing additional security modules to be inserted at any priority tier without disrupting existing module operation.

**C. Human-in-the-Loop Approval Queue**

For designated high-risk operations — including but not limited to external email transmission, file deletion, external API calls to unapproved destinations, and software installation — the governance proxy suspends the agent's pending action and routes an approval request to a designated human operator via one or more notification channels (messaging platforms, mobile push notifications, web dashboard, or API callback). The agent's action proceeds only upon explicit human approval, and the system supports configurable approval policies including time-bounded automatic expiration, one-time approval, and persistent allowlisting.

**D. PII Detection and Redaction Engine**

The governance proxy includes a real-time PII detection engine that scans all outbound agent communications for personally identifiable information using named entity recognition with configurable confidence thresholds. Detected PII is redacted, masked, or blocked according to configurable policy before the communication is forwarded to its destination.

**E. Trust-Differentiated Processing**

The governance proxy assigns trust levels to communications based on the identity and role of the originating user or agent. Communications from owner/administrator-level users may receive a different (e.g., less restrictive) security pipeline configuration than communications from collaborator-level or unknown users. The system supports role-based access control (RBAC) with at minimum owner, administrator, operator, and collaborator role tiers, each with independently configurable security policies.

**F. Multi-Platform Control Surface**

The governance proxy is controllable through multiple interfaces including but not limited to: a messaging bot interface (supporting platforms such as Telegram), a web-based dashboard, a terminal-based user interface (TUI), a command-line interface (CLI), a browser extension, mobile device shortcuts, and a REST API. All control surfaces converge on the same governance state, providing consistent policy enforcement regardless of the control channel used.

**G. Egress Filtering with Semantic Awareness**

The egress filtering component goes beyond traditional domain-based network filtering by incorporating semantic analysis of agent-generated content to detect: attempted data exfiltration patterns, internal system information disclosure (including but not limited to operating system details, network topology, credential material, and agent identity information), and communication patterns indicative of prompt injection or social engineering attacks against the governance proxy itself.

**H. Agent-Agnostic Operation**

The governance proxy is designed to operate with any AI agent that communicates over standard protocols (HTTP, HTTPS, WebSocket, SSH). The system has been demonstrated with multiple distinct AI agent implementations simultaneously, proving vendor-agnostic operation. Agent-specific adaptations are confined to the interception layer, not the security pipeline.

**I. Delegated Authority Model**

The system supports time-bounded delegation of specific administrative privileges from the owner to designated operators, enabling continued governance operations during owner absence. Delegable privileges include but are not limited to: egress approval authority, user management, and security policy modification. Delegations automatically expire after a configured time period.

**J. Collaborative Multi-Agent Governance**

The governance proxy supports simultaneous governance of multiple AI agents with per-agent and per-user isolation of: tool access permissions (configurable allowlists and blocklists per user, per group, and per access tier), shared memory spaces (with private, group-scoped, and public visibility tiers), and service privacy policies that control what data each agent or user can access.

**K. SOC (Security Operations Center) Team Integration**

The system provides real-time visibility into all governed agent activity through a dedicated API surface that exposes: per-user activity tracking, delegation status, tool access control policies, shared memory contents, privacy policy configuration, egress rule state, approval queue status, service health scorecards, and security scanner results. This enables integration with enterprise SOC workflows and security information and event management (SIEM) systems.

**L. Configuration Integrity Monitoring**

The governance proxy monitors its own configuration files for unauthorized modification, computing cryptographic hashes at startup and alerting the designated owner if configuration drift is detected. This provides defense against attacks that attempt to weaken governance policies by modifying proxy configuration.

**M. Progressive Enforcement**

The system implements escalating enforcement responses to repeated policy violations by a single user or agent, progressing through stages that may include: owner notification, rate limit escalation, and session suspension. Enforcement thresholds and escalation stages are configurable.

#### DETAILED DESCRIPTION — SYSTEM ARCHITECTURE

The governance proxy is deployed as a containerized service that operates on a host machine within the same network as the AI agents it governs. Communications flow as follows:

```
AI Agent ---> Governance Proxy Gateway ---> [Security Pipeline] ---> Target System
                     |                            |
                     v                            v
              [Audit Ledger]              [Approval Queue]
                     |                            |
                     v                            v
              [Control Surfaces]          [Human Operator]
```

1. The AI agent initiates a communication (API call, file operation, network request, tool invocation, or messaging action).

2. The communication is routed to the governance proxy gateway through one or more interception mechanisms: HTTP/HTTPS proxy configuration, API endpoint URL rewriting, SDK-level interception patching, DNS resolution redirection, or SSH proxy tunneling.

3. The gateway passes the communication through the multi-stage security pipeline. Each module in the pipeline may: allow the communication to proceed, modify the communication (e.g., redacting PII), block the communication, or suspend the communication pending human approval.

4. If the communication passes all pipeline stages, it is forwarded to the intended target system, and the response is returned to the agent.

5. All communications and pipeline decisions are recorded in an immutable audit ledger.

6. Pipeline decisions and alerts are surfaced through the multi-platform control surfaces for real-time monitoring and management.

#### DETAILED DESCRIPTION — SECURITY MODULE PIPELINE

The security pipeline comprises a plurality of independent security modules, each responsible for a specific governance function. Modules are organized into priority tiers (P0 through P3) and execute in a defined order within each tier. Each module receives the communication context and returns a disposition (allow, modify, block, or suspend).

The modular architecture enables:
- Independent development and testing of each security function
- Runtime enabling/disabling of specific modules without affecting others
- Configurable ordering within and across priority tiers
- Extension with new modules without modification to existing modules

#### DETAILED DESCRIPTION — INTERCEPTION MECHANISMS

The governance proxy supports multiple interception mechanisms to accommodate different AI agent architectures:

1. **HTTP/HTTPS Proxy** — Standard proxy protocol (HTTP CONNECT for HTTPS tunneling) that intercepts agent web traffic including API calls to cloud services, LLM providers, and external tools.

2. **API Endpoint Rewriting** — The governance proxy presents itself as the target API endpoint (e.g., a messaging platform API), processes the request through the security pipeline, and forwards it to the real endpoint. This requires only URL configuration changes, not agent code modification.

3. **SDK-Level Patching** — For agents built on specific SDKs, build-time patches redirect API calls to the governance proxy without source code modification of the agent.

4. **SSH Proxy** — For agents that interact with remote systems via SSH, the governance proxy intercepts and inspects SSH communications.

5. **WebSocket Relay** — For agents using real-time communication protocols, the governance proxy relays WebSocket connections through the security pipeline.

#### NOVEL ASPECTS

The present invention is believed to be novel in at least the following respects:

1. **Transparent governance of autonomous AI agents** — No prior art is known that provides a transparent, enterprise-controlled proxy specifically designed for governing autonomous AI agent communications across multiple agent vendors simultaneously, with semantic content analysis beyond network-level filtering.

2. **Multi-stage security pipeline with modular architecture** — The tiered priority system with independently configurable security modules operating on AI agent traffic represents a novel application of security pipeline architecture to the AI agent governance domain.

3. **Human-in-the-loop approval queue for AI agent actions** — The real-time suspension and approval mechanism for high-risk AI agent operations, with configurable policies and multi-channel notification, addresses a previously unmet need in AI agent deployment.

4. **Trust-differentiated security processing** — The application of role-based, trust-level-differentiated security pipelines to AI agent governance, where the same proxy applies different security policies based on the human user's role, is believed to be novel.

5. **Agent-agnostic governance with vendor-neutral operation** — The ability to simultaneously govern multiple AI agents from different vendors through a single governance layer, using standard protocol interception rather than agent-specific integrations, is believed to represent a novel approach.

6. **Semantic egress filtering for AI agents** — Content-aware egress filtering that detects AI-agent-specific exfiltration patterns (prompt injection artifacts, system information disclosure, credential leakage) beyond traditional network-level domain filtering.

7. **Progressive enforcement with escalating responses** — Automated escalation from notification through rate limiting to session suspension based on cumulative policy violation patterns by individual users or agents.

8. **Delegated governance authority with time-bounded expiration** — The ability to delegate specific governance privileges to designated operators with automatic expiration, enabling continued governance operations during owner absence.

#### INDUSTRIAL APPLICABILITY

The governance proxy system has direct industrial applicability in:

- Enterprise software development organizations deploying AI coding assistants
- Critical infrastructure operators (energy, utilities, transportation) using AI agents for operational automation
- Financial services organizations requiring audit trails for AI-initiated actions
- Healthcare organizations requiring PII protection for AI agent interactions
- Government and defense organizations requiring security governance of AI tools
- Any organization subject to regulatory compliance requirements (SOC 2, ISO 27001, HIPAA, GDPR, IEC 62443) that deploys autonomous AI agents

#### CROSS-REFERENCE TO RELATED APPLICATIONS

This is an original provisional application. No prior related applications have been filed.

#### ABSTRACT

A computer-implemented system and method for governing autonomous artificial intelligence (AI) agent communications with external systems. A transparent proxy gateway interposes between one or more AI agents and the systems those agents interact with, routing all agent-originated communications through a multi-stage security pipeline comprising independently configurable security modules organized by priority tier. The system provides real-time interception, inspection, policy enforcement, PII redaction, human-in-the-loop approval for high-risk operations, trust-differentiated processing based on user roles, and comprehensive audit logging, all without requiring modification to the AI agents themselves. The governance proxy is controllable through multiple interfaces and supports simultaneous governance of multiple AI agents from different vendors.

---

## SECTION 3: DRAWINGS

> **Preparation:** Convert each figure description below into a black-and-white line drawing.
> Use your existing Mermaid diagrams in `docs/diagrams/` as reference, but redraw as
> simplified patent-style figures with numbered reference elements. Export as PDF for upload.
> Tools: draw.io, Figma, or any vector editor. Black lines on white background, no color.

---

### FIGURE 1 — System Context Diagram

**Title:** Enterprise Governance Proxy System — Overall Architecture

```
    ┌──────────┐   ┌──────────┐   ┌──────────┐
    │ AI Agent │   │ AI Agent │   │ AI Agent │
    │    A     │   │    B     │   │    C     │
    └────┬─────┘   └────┬─────┘   └────┬─────┘
         │              │              │
         └──────────────┼──────────────┘
                        │
              ┌─────────▼──────────┐
              │                    │
              │   GOVERNANCE       │
              │   PROXY GATEWAY    │
              │                    │
              │  ┌──────────────┐  │
              │  │  Security    │  │
              │  │  Pipeline    │  │
              │  └──────────────┘  │
              │  ┌──────────────┐  │
              │  │  Approval    │  │
              │  │  Queue       │  │
              │  └──────────────┘  │
              │  ┌──────────────┐  │
              │  │  Audit       │  │
              │  │  Ledger      │  │
              │  └──────────────┘  │
              │                    │
              └──┬──────┬──────┬───┘
                 │      │      │
         ┌───────▼┐  ┌──▼───┐  ┌▼────────┐
         │ Target │  │Target│  │ Target   │
         │System 1│  │Sys. 2│  │ System 3 │
         └────────┘  └──────┘  └──────────┘

              ┌──────────────────────┐
              │   CONTROL SURFACES   │
              │ Web  TUI  CLI  Bot   │
              │ API  Mobile  Browser │
              └──────────────────────┘
```

**Reference Numerals:**

| Ref. | Element |
|------|---------|
| 100 | System context (overall) |
| 110 | AI Agent A (first autonomous agent) |
| 112 | AI Agent B (second autonomous agent, different vendor) |
| 114 | AI Agent C (third autonomous agent, different vendor) |
| 120 | Governance Proxy Gateway |
| 122 | Security Pipeline (within gateway) |
| 124 | Approval Queue (within gateway) |
| 126 | Audit Ledger (within gateway) |
| 130 | Target System 1 (e.g., cloud API) |
| 132 | Target System 2 (e.g., messaging platform) |
| 134 | Target System 3 (e.g., file system or database) |
| 140 | Control Surfaces (multi-platform management interfaces) |

**Description:** FIG. 1 illustrates the overall system architecture. A plurality of autonomous AI agents (110, 112, 114), which may be from different vendors, route all outbound communications through the governance proxy gateway (120). The gateway contains a security pipeline (122), an approval queue (124), and an audit ledger (126). Communications that pass the security pipeline are forwarded to the intended target systems (130, 132, 134). The gateway is managed through multiple control surfaces (140) including web, terminal, command-line, messaging bot, REST API, mobile, and browser interfaces.

---

### FIGURE 2 — Security Pipeline Flow Diagram

**Title:** Multi-Stage Security Pipeline — Inbound and Outbound Processing

```
INBOUND PIPELINE (Agent → Gateway):

  Agent Message
       │
       ▼
  ┌─────────────┐
  │ P0: Context  │──BLOCK──▶ [Deny + Log]
  │   Integrity  │
  └──────┬───────┘
         │ PASS
         ▼
  ┌──────────────┐
  │ P0: Prompt   │──BLOCK──▶ [Deny + Log]
  │  Inspection  │
  └──────┬───────┘
         │ PASS
         ▼
  ┌──────────────┐
  │ P0: PII      │──MODIFY─▶ [Redact + Continue]
  │  Detection   │
  └──────┬───────┘
         │ PASS/MODIFIED
         ▼
  ┌──────────────┐
  │ P0: Trust    │──BLOCK──▶ [Deny + Log]
  │  Assessment  │
  └──────┬───────┘
         │ PASS
         ▼
  ┌──────────────┐
  │ P1: Approval │──SUSPEND─▶ [Queue + Notify Owner]
  │  Check       │
  └──────┬───────┘
         │ PASS
         ▼
  ┌──────────────┐
  │ P1: Audit    │
  │  Chain Log   │
  └──────┬───────┘
         │
         ▼
  Forward to Agent


OUTBOUND PIPELINE (Agent → User/Target):

  Agent Response
       │
       ▼
  ┌──────────────┐
  │ P0: Content  │──MODIFY─▶ [Strip Internal Tags]
  │  Filtering   │
  └──────┬───────┘
         │
         ▼
  ┌──────────────┐
  │ P0: PII      │──MODIFY─▶ [Redact + Continue]
  │  Redaction   │
  └──────┬───────┘
         │
         ▼
  ┌──────────────┐
  │ P1: Info     │──BLOCK──▶ [Deny + Log]
  │  Disclosure  │
  │  Filter      │
  └──────┬───────┘
         │ PASS
         ▼
  ┌──────────────┐
  │ P2: Encoding │──BLOCK──▶ [Deny + Log]
  │  Bypass Det. │
  └──────┬───────┘
         │ PASS
         ▼
  ┌──────────────┐
  │ P2: Canary   │──BLOCK──▶ [Alert + Deny]
  │  Detection   │
  └──────┬───────┘
         │ PASS
         ▼
  ┌──────────────┐
  │ P2: Egress   │──BLOCK──▶ [Deny / Queue Approval]
  │  Filter      │
  └──────┬───────┘
         │ PASS
         ▼
  ┌──────────────┐
  │ P3: Audit    │
  │  Chain Log   │
  └──────┬───────┘
         │
         ▼
  Return to User
```

**Reference Numerals:**

| Ref. | Element |
|------|---------|
| 200 | Inbound pipeline (overall) |
| 210 | Context integrity check (P0) |
| 212 | Prompt injection inspection (P0) |
| 214 | PII detection and redaction — inbound (P0) |
| 216 | Trust level assessment (P0) |
| 220 | Approval queue check (P1) |
| 222 | Audit chain logging — inbound (P1) |
| 250 | Outbound pipeline (overall) |
| 252 | Content filtering / internal tag stripping (P0) |
| 254 | PII redaction — outbound (P0) |
| 256 | Information disclosure filter (P1) |
| 258 | Encoding bypass detection (P2) |
| 260 | Canary token detection (P2) |
| 262 | Egress destination filter (P2) |
| 264 | Audit chain logging — outbound (P3) |
| 270 | BLOCK disposition (deny + log) |
| 272 | MODIFY disposition (redact/strip + continue) |
| 274 | SUSPEND disposition (queue for human approval) |

**Description:** FIG. 2 illustrates the ordered security pipeline for both inbound (200) and outbound (250) communications. The inbound pipeline processes agent messages through context integrity (210), prompt injection inspection (212), PII detection (214), trust assessment (216), approval check (220), and audit logging (222). Each module may return a BLOCK (270), MODIFY (272), SUSPEND (274), or PASS disposition. The outbound pipeline processes agent responses through content filtering (252), PII redaction (254), information disclosure filtering (256), encoding bypass detection (258), canary detection (260), egress filtering (262), and audit logging (264). The pipeline is fail-closed: if any module encounters an error, the communication is blocked.

---

### FIGURE 3 — Approval Queue Flow Diagram

**Title:** Human-in-the-Loop Approval Queue Process

```
  Agent requests
  high-risk action
       │
       ▼
  ┌──────────────┐     NO
  │ Requires     ├──────────▶ Proceed immediately
  │ approval?    │
  └──────┬───────┘
         │ YES
         ▼
  ┌──────────────┐
  │ Classify     │
  │ risk tier    │
  │ (LOW/MED/    │
  │  HIGH/CRIT)  │
  └──────┬───────┘
         │
         ▼
  ┌──────────────┐
  │ Suspend      │
  │ agent action │
  │ + persist    │
  └──────┬───────┘
         │
         ├──────────────────────────────────┐
         ▼                                  ▼
  ┌──────────────┐                   ┌──────────────┐
  │ Notify owner │                   │ Start timeout│
  │ via messaging│                   │ timer        │
  │ platform     │                   │ (configurable│
  └──────┬───────┘                   │  per tier)   │
         │                           └──────┬───────┘
         ▼                                  │
  ┌──────────────┐                          │
  │ Owner        │                          │
  │ reviews      │◀─────────────────────────┘
  │ request      │         (timeout expires)
  └──┬───────┬───┘
     │       │
  APPROVE   DENY            TIMEOUT
     │       │                  │
     ▼       ▼                  ▼
  ┌──────┐ ┌──────┐      ┌──────────┐
  │Resume│ │Block │      │Auto-deny │
  │action│ │action│      │or auto-  │
  │      │ │+ log │      │approve   │
  └──┬───┘ └──┬───┘      │(per tier)│
     │        │           └────┬─────┘
     ▼        ▼                ▼
  ┌──────────────────────────────────┐
  │ Record decision in audit ledger  │
  │ (who, when, action, disposition) │
  └──────────────────────────────────┘
```

**Reference Numerals:**

| Ref. | Element |
|------|---------|
| 300 | Approval queue process (overall) |
| 310 | Approval requirement check |
| 312 | Risk tier classification (LOW, MEDIUM, HIGH, CRITICAL) |
| 314 | Action suspension and persistence |
| 320 | Owner notification (via messaging platform) |
| 322 | Timeout timer (configurable per risk tier) |
| 330 | Owner review interface |
| 332 | APPROVE decision — resume agent action |
| 334 | DENY decision — block agent action |
| 336 | TIMEOUT — automatic disposition per risk tier policy |
| 340 | Audit ledger recording (decision, approver, timestamp) |

**Description:** FIG. 3 illustrates the human-in-the-loop approval queue process (300). When an agent requests a high-risk action, the system checks whether approval is required (310). If yes, the action is classified by risk tier (312), suspended and persisted (314), and the designated owner is notified via messaging platform (320). A configurable timeout timer starts concurrently (322). The owner reviews the request (330) and may approve (332) to resume the action, or deny (334) to block it. If the timeout expires before a decision, the system applies an automatic disposition per the risk tier policy (336) — critical-tier actions default to auto-deny, while lower tiers may auto-approve. All decisions are recorded in the audit ledger (340).

---

### FIGURE 4 — Trust-Differentiated Processing

**Title:** Role-Based Trust Level Architecture

```
  Incoming communication
       │
       ▼
  ┌──────────────────┐
  │ Identify user /  │
  │ agent identity   │
  └──────┬───────────┘
         │
         ▼
  ┌──────────────────┐
  │ Lookup role in   │
  │ RBAC registry    │
  └──┬──┬──┬──┬──┬───┘
     │  │  │  │  │
     ▼  ▼  ▼  ▼  ▼

  OWNER    ADMIN    OPERATOR    COLLABORATOR    VIEWER
  (Lvl 5)  (Lvl 4)  (Lvl 3)     (Lvl 2)        (Lvl 1)
    │        │        │            │               │
    ▼        ▼        ▼            ▼               ▼
  ┌─────┐ ┌─────┐ ┌───────┐  ┌──────────┐    ┌────────┐
  │FULL │ │FULL │ │STNDRD │  │UNTRUSTED │    │READ    │
  │trust│ │trust│ │trust  │  │trust     │    │ONLY    │
  │path │ │path │ │path   │  │path      │    │        │
  └──┬──┘ └──┬──┘ └───┬───┘  └────┬─────┘    └───┬────┘
     │       │        │           │               │
     ▼       ▼        ▼           ▼               ▼
  [Minimal [Standard [Standard  [Full pipeline  [Block all
   pipeline] pipeline] pipeline   + additional    write
             ]        + limited   info disclosure  operations]
                       tool       filter +
                       access]    rate limiting]
```

**Reference Numerals:**

| Ref. | Element |
|------|---------|
| 400 | Trust-differentiated processing (overall) |
| 410 | User/agent identity resolution |
| 412 | RBAC registry lookup |
| 420 | OWNER role (Level 5) — full trust path, minimal pipeline restrictions |
| 422 | ADMIN role (Level 4) — full trust path, standard pipeline |
| 424 | OPERATOR role (Level 3) — standard trust, limited tool access |
| 426 | COLLABORATOR role (Level 2) — untrusted path, full pipeline + info disclosure filter + rate limiting |
| 428 | VIEWER role (Level 1) — read-only, all write operations blocked |
| 430 | Pipeline path selection (trust-level-dependent module configuration) |

**Description:** FIG. 4 illustrates the trust-differentiated processing architecture (400). Each incoming communication is first resolved to a user or agent identity (410), then looked up in the RBAC registry (412) to determine the assigned role. The system supports five hierarchical roles: OWNER (420), ADMIN (422), OPERATOR (424), COLLABORATOR (426), and VIEWER (428). Each role maps to a different security pipeline configuration (430). Higher-trust roles (OWNER, ADMIN) receive minimal pipeline restrictions, while lower-trust roles (COLLABORATOR, VIEWER) receive progressively more restrictive processing including additional content filtering, information disclosure prevention, tool access restrictions, and rate limiting.

---

### FIGURE 5 — Multi-Agent Governance with Isolation

**Title:** Simultaneous Multi-Agent Governance with Per-Agent Isolation

```
  ┌──────────┐  ┌──────────┐  ┌──────────┐
  │ Agent A  │  │ Agent B  │  │ Agent C  │
  │(Vendor 1)│  │(Vendor 2)│  │(Vendor 3)│
  └────┬─────┘  └────┬─────┘  └────┬─────┘
       │              │              │
  ┌────▼─────┐  ┌─────▼────┐  ┌─────▼────┐
  │Intercept │  │Intercept │  │Intercept │
  │Mechanism │  │Mechanism │  │Mechanism │
  │  A       │  │  B       │  │  C       │
  └────┬─────┘  └────┬─────┘  └────┬─────┘
       │              │              │
       └──────────────┼──────────────┘
                      │
            ┌─────────▼──────────┐
            │  GOVERNANCE PROXY  │
            │                    │
            │  ┌──────────────┐  │
            │  │ Agent        │  │
            │  │ Registry     │  │
            │  │ ┌──┐┌──┐┌──┐│  │
            │  │ │A ││B ││C ││  │
            │  │ └──┘└──┘└──┘│  │
            │  └──────────────┘  │
            │                    │
            │  ┌──────────────┐  │
            │  │ Isolated     │  │
            │  │ Contexts     │  │
            │  │ ┌──────────┐ │  │
            │  │ │ Agent A  │ │  │
            │  │ │ -tools   │ │  │
            │  │ │ -memory  │ │  │
            │  │ │ -session │ │  │
            │  │ └──────────┘ │  │
            │  │ ┌──────────┐ │  │
            │  │ │ Agent B  │ │  │
            │  │ │ -tools   │ │  │
            │  │ │ -memory  │ │  │
            │  │ │ -session │ │  │
            │  │ └──────────┘ │  │
            │  └──────────────┘  │
            │                    │
            │  ┌──────────────┐  │
            │  │  SHARED       │  │
            │  │  Security     │  │
            │  │  Pipeline     │  │
            │  └──────────────┘  │
            └────────────────────┘
```

**Reference Numerals:**

| Ref. | Element |
|------|---------|
| 500 | Multi-agent governance system (overall) |
| 510 | AI Agent A (first vendor) |
| 512 | AI Agent B (second vendor) |
| 514 | AI Agent C (third vendor) |
| 520 | Interception mechanism A (vendor-specific adapter) |
| 522 | Interception mechanism B |
| 524 | Interception mechanism C |
| 530 | Agent Registry (identity + capability tracking) |
| 540 | Isolated Contexts (per-agent) |
| 542 | Agent A context (tool permissions, memory space, session state) |
| 544 | Agent B context |
| 550 | Shared Security Pipeline (common to all agents) |

**Description:** FIG. 5 illustrates the multi-agent governance architecture (500). Multiple AI agents from different vendors (510, 512, 514) connect through vendor-specific interception mechanisms (520, 522, 524) that adapt each agent's protocol to the governance proxy's internal format. The agent registry (530) tracks registered agents and their capabilities. Each agent receives an isolated context (540) containing its own tool permissions, memory space, and session state (542, 544), preventing cross-agent data leakage. All agents share the same security pipeline (550) for consistent policy enforcement regardless of agent vendor.

---

### FIGURE 6 — Delegated Authority Model

**Title:** Time-Bounded Privilege Delegation Flow

```
  ┌──────────────┐
  │    OWNER     │
  │  (Primary    │
  │  Authority)  │
  └──────┬───────┘
         │
         │ Delegates specific
         │ privileges with
         │ time expiration
         │
         ▼
  ┌──────────────────────────────┐
  │     DELEGATION RECORD       │
  │                              │
  │  Delegator:  Owner ID       │
  │  Delegate:   Operator ID    │
  │  Privileges: [list]         │
  │  Granted:    timestamp      │
  │  Expires:    timestamp      │
  │  Status:     ACTIVE         │
  └──────────────┬───────────────┘
                 │
         ┌───────┴───────┐
         ▼               ▼
  ┌──────────────┐ ┌──────────────┐
  │  Delegable   │ │  Non-        │
  │  Privileges  │ │  Delegable   │
  │              │ │  Privileges  │
  │ - Egress     │ │              │
  │   approval   │ │ - Key        │
  │ - User       │ │   rotation   │
  │   management │ │ - Kill       │
  │ - Policy     │ │   switch     │
  │   modification│ │ - Delegation │
  │              │ │   of deleg.  │
  └──────┬───────┘ └──────────────┘
         │
         ▼
  ┌──────────────┐
  │  OPERATOR    │
  │  (Delegated  │
  │  Authority)  │
  └──────┬───────┘
         │
         │ Exercises delegated
         │ privileges within
         │ time window
         │
         ▼
  ┌──────────────────────────────┐
  │     TIME EXPIRATION          │
  │                              │
  │  On expiry:                  │
  │  - Status → EXPIRED          │
  │  - Privileges revoked        │
  │  - Owner notified            │
  │  - Audit logged              │
  └──────────────────────────────┘
```

**Reference Numerals:**

| Ref. | Element |
|------|---------|
| 600 | Delegated authority model (overall) |
| 610 | Owner (primary authority holder) |
| 620 | Delegation record (persisted) |
| 622 | Delegation metadata (delegator, delegate, privileges, timestamps, status) |
| 630 | Delegable privileges (egress approval, user management, policy modification) |
| 632 | Non-delegable privileges (key rotation, kill switch, delegation of delegation) |
| 640 | Operator (delegated authority recipient) |
| 650 | Time expiration mechanism |
| 652 | Expiration actions (status change, privilege revocation, notification, audit) |

**Description:** FIG. 6 illustrates the time-bounded privilege delegation model (600). The owner (610) creates a delegation record (620) that grants specific privileges to a designated operator (640) for a defined time period. Privileges are divided into delegable (630) — such as egress approval authority, user management, and policy modification — and non-delegable (632) — such as cryptographic key rotation, emergency kill switch activation, and meta-delegation. The operator exercises delegated privileges within the time window. Upon expiration (650), the delegation status is automatically changed to EXPIRED, all delegated privileges are revoked, the owner is notified, and the event is recorded in the audit ledger (652).

---

### Drawing Preparation Checklist

- [ ] Redraw each figure as a clean black-and-white line drawing (no color, no shading)
- [ ] Add reference numerals to each element as specified above
- [ ] Use consistent line weights: thick for system boundaries, thin for internal components
- [ ] Include figure title below each drawing: "FIG. 1", "FIG. 2", etc.
- [ ] Export all 6 figures as a single PDF document
- [ ] Verify no proprietary module names, vendor names, or source code appear in drawings
- [ ] Ensure each figure is legible when printed on standard letter-size (8.5" x 11") paper

---

## SECTION 4: FILING CHECKLIST

### Pre-Filing Preparation

- [ ] Fill in all `[YOUR ...]` placeholders in Sections 1.2 and 1.4 with your personal information
- [ ] Prepare drawings per Section 3 — redraw 6 figures as black-and-white line drawings, export as single PDF
- [ ] Convert Section 2 (Written Description) to a clean PDF (remove markdown formatting, instruction blocks, and this checklist)
- [ ] Review written description one final time — ensure no proprietary details leaked

### Patent Center Filing Steps

1. [ ] Navigate to https://patentcenter.uspto.gov
2. [ ] Log in or create a USPTO.gov account (requires multi-factor authentication)
3. [ ] Select **"New Provisional Application"**
4. [ ] Complete Form PTO/SB/16 (Cover Sheet) using data from Section 1
5. [ ] Complete Form PTO/SB/15 — **Certification of Small Entity Status**
   - Basis: Individual inventor, not under obligation to assign to a large entity
6. [ ] Upload Written Description PDF (Section 2)
7. [ ] Upload Drawings PDF (Section 3 — all 6 figures in one document)
8. [ ] Enter invention title: "Enterprise Governance Proxy System and Method for Policy-Enforced Interception, Inspection, and Mediation of Autonomous AI Agent Communications with External Systems"
9. [ ] Pay filing fee: **$130.00** (Small Entity)
10. [ ] Submit application

### Post-Filing

- [ ] Save confirmation page and provisional application serial number
- [ ] Download the filing receipt PDF from Patent Center
- [ ] Calendar the 12-month deadline — **must file non-provisional by [FILING DATE + 12 months]**
- [ ] At month 6: begin engaging a patent attorney for non-provisional preparation
- [ ] At month 9: patent attorney should have draft claims ready for review
- [ ] At month 11: final review and file non-provisional application

---

## SECTION 5: IMPORTANT NOTES

### What is NOT in this application (by design)

The following are intentionally omitted to protect trade secrets while maintaining adequate disclosure:

- Specific source code or algorithms
- Specific module names or internal architecture labels
- Configuration file formats or schema
- Specific third-party integrations or vendor names (referenced generically)
- Performance benchmarks or test coverage metrics
- Deployment topology details
- Specific protocol-level implementation details

### What you MUST file within 12 months

A non-provisional application (utility patent) under 35 U.S.C. Section 111(a) that:
- References this provisional application for priority date
- Includes formal patent claims
- Includes an oath/declaration
- Pays the non-provisional filing fee
- **Strongly recommend engaging a patent attorney for the non-provisional filing**

### Entity Status: Small Entity (Confirmed)

You do NOT qualify as micro entity for two independent reasons:
1. Gross income exceeds 3x median household income (~$225K threshold)
2. Named as inventor on 4+ previously filed US patent applications

You DO qualify as **small entity** because:
- You are an individual inventor
- AgentShroud is personal IP — no obligation to assign to a large entity
- File Form PTO/SB/15 (Certification of Small Entity Status) with your application

### Employment IP Considerations

**CONFIRMED:** AgentShroud is personal IP, developed on personal time with personal resources, outside scope of Fluence Energy employment duties. No obligation to assign.

**Recommendation:** Keep a brief contemporaneous record of this determination (date, basis) in case it is ever questioned. A single-paragraph memo to yourself is sufficient.

---

## SECTION 6: ESTIMATED COSTS

| Item | Cost |
|------|------|
| Provisional filing (small entity) | $130 |
| Patent attorney review of provisional (optional) | $500 - $2,000 |
| Non-provisional filing within 12 months (small entity) | $800 |
| Patent search (recommended before non-provisional) | $1,000 - $3,000 |
| Patent attorney for non-provisional (strongly recommended) | $5,000 - $15,000 |
| **Total (DIY provisional + attorney for non-provisional)** | **$6,930 - $20,930** |

### Combined Filing Costs (Patent + Trademark)

| Item | Cost |
|------|------|
| Provisional patent (small entity) | $130 |
| Trademark TEAS Plus (2 classes) | $700 |
| **Total immediate filing cost** | **$830** |
