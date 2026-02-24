# AgentShroud — Diagram Library

> AgentShroud™ is a trademark of Isaiah Jefferson · First use February 2026 · All rights reserved
> Unauthorized use of the AgentShroud name or brand is strictly prohibited · Federal trademark registration pending

All diagrams use [Mermaid](https://mermaid.js.org/) and render natively on GitHub.

---

## Index

| # | Diagram | Category | File |
|---|---------|----------|------|
| 1 | C4 Level 0 — Context (Executive View) | Architecture | [01-architecture.md](01-architecture.md) |
| 2 | C4 Level 1 — Container View | Architecture | [01-architecture.md](01-architecture.md) |
| 3 | Architecture Component — Gateway Internals | Architecture | [01-architecture.md](01-architecture.md) |
| 4 | Infrastructure — Hosting & Servers | Infrastructure | [02-infrastructure.md](02-infrastructure.md) |
| 5 | Network Topology — Subnets & Traffic Paths | Infrastructure | [02-infrastructure.md](02-infrastructure.md) |
| 6 | Deployment — CI/CD & What Runs Where | Infrastructure | [02-infrastructure.md](02-infrastructure.md) |
| 7 | Data Flow — End-to-End | Data | [03-data.md](03-data.md) |
| 8 | ERD — Database Tables & Relationships | Data | [03-data.md](03-data.md) |
| 9 | Data Lineage — Source to Consumption | Data | [03-data.md](03-data.md) |
| 10 | Data Dictionary / Catalog Map | Data | [03-data.md](03-data.md) |
| 11 | Trust Boundary — Roles & Policies | Security | [04-security.md](04-security.md) |
| 12 | Credential Flow — Secret Management | Security | [04-security.md](04-security.md) |
| 13 | Network Security — Egress Controls | Security | [04-security.md](04-security.md) |
| 14 | Logic Flow / Flowchart — Request Execution | Behavior | [05-behavior.md](05-behavior.md) |
| 15 | Sequence Diagram — Telegram to Response | Behavior | [05-behavior.md](05-behavior.md) |
| 16 | State Machine — Approval Queue Lifecycle | Behavior | [05-behavior.md](05-behavior.md) |
| 17 | State Machine — Bot Session / Context | Behavior | [05-behavior.md](05-behavior.md) |
| 18 | Runbook / Decision Tree — On-Call Logic | Operations | [06-operations.md](06-operations.md) |
| 19 | Incident Response — Severity & Escalation | Operations | [06-operations.md](06-operations.md) |
| 20 | Monitoring & Observability Map | Operations | [06-operations.md](06-operations.md) |
| 21 | Agile Team — Structure & Roles | Team | [07-team-planning.md](07-team-planning.md) |
| 22 | Dependency Graph — Component Dependencies | Planning | [07-team-planning.md](07-team-planning.md) |
| 23 | Roadmap / Gantt — Development Phases | Planning | [07-team-planning.md](07-team-planning.md) |

---

## Priority Reading Order

For onboarding, security audits, and incident response, read in this order:

1. **[C4 Level 0](01-architecture.md)** — Understand the system at a glance
2. **[ERD](03-data.md)** — Know what data exists and where
3. **[State Machine: Approval Queue](05-behavior.md)** — Understand human-in-the-loop lifecycle
4. **[Trust Boundary](04-security.md)** — Understand who can access what
5. **[Runbook](06-operations.md)** — Respond to incidents correctly
6. **[Sequence Diagram](05-behavior.md)** — Trace a request end-to-end
7. **[Credential Flow](04-security.md)** — Understand secret management

---

## Diagrams Not Yet Implemented

| Diagram | Notes |
|---------|-------|
| Wazuh SIEM integration map | Wazuh client present in codebase; not yet active |
| Falco runtime security map | falco_monitor.py present; container integration pending |
| Full Prometheus metrics map | Metrics export not yet wired |
| IEC 62443 compliance map | Planned for Phase 7 |
