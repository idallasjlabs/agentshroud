# `docs/planning/` — Index

All AgentShroud plans, roadmaps, feature lists, recovery procedures, red-team scenarios, and review reports live here. Anything you'd call "documentation" (setup guides, API references, ADRs, runbooks, papers, etc.) stays in the rest of `docs/`.

## Layout

```
docs/planning/
├── README.md                    ← you are here
├── MASTER-FEATURE-LIST.md       ← cross-version master feature inventory
├── RELEASE-PLAN.md              ← rolling release plan
│
├── v0.7/                        ← v0.7.0 era (reserved; currently empty)
├── v0.8/                        ← v0.8.0 "Watchtower" — full security suite landing
├── v0.9/                        ← v0.9.0 — testing + release plan
├── v1.0/                        ← v1.0.0 "Fortress" — roadmap, post-v1.0 work
├── v1.2/                        ← v1.2.0 active — master plan + workstream docs
│
├── redteam/                     ← all red-team scenario writeups + remediation plans
├── reviews/                     ← phase reviews + blue-team audits (older, not yet bucketed by version)
└── recovery/                    ← repo recovery procedures
```

## Active

- **[v1.2/v1.2.0-master-plan.md](v1.2/v1.2.0-master-plan.md)** — 5-workstream consolidated plan (groups & teamwork, security extensions, local-model parity, skills sync, blue+red scans)
- **[v1.2/LOCAL_LLM_REVIEW.md](v1.2/LOCAL_LLM_REVIEW.md)** — design baseline for Workstream C (local-model parity)
- **[MASTER-FEATURE-LIST.md](MASTER-FEATURE-LIST.md)** — superset of "everything ever mentioned"; consult before adding new features to confirm not already planned
- **[RELEASE-PLAN.md](RELEASE-PLAN.md)** — rolling release plan (versioning, cut criteria, deploy checklist)

## Historic / archive

- **v0.8/** — 12 files: original release plan, egress firewall design, security overview, blue-team assessments (v0.8.0 + 3 revisions + final), 25-domain security assessment, container security audit, wiring audit, plan reset doc
- **v0.9/** — 3 files: release plan, feature-final list, testing guide, release notes
- **v1.0/** — 3 files: post-v1.0 roadmap, release announcement, post-Fable5 task delegation
- **redteam/** — 11 files: scenarios 00–06, feature priorities, live assessment results, master plan, v0.7.0 remediation plan
- **reviews/** — phase reviews (Feb–Mar 2026), blue-team v0.7.0 audit, enforcement audit, prompt-injection assessment, session issue register, plus `enforcement-audit-script.py` (the executable that produced the report)
- **recovery/** — `RECOVERY_PLAN.md` and partial variant; consult only during incident response

## How to add a plan

1. Pick the right bucket: version (v1.2/, v1.3/, etc.) if it's release-scoped, otherwise `redteam/`, `reviews/`, or `recovery/`
2. Name the file with the version prefix when possible (`v1.2.0-foo-plan.md`)
3. Update this README's "Active" section if the plan is current work
4. Link cross-references inline; do not duplicate plan content across files

## What does NOT live here

- Documentation for end users → `docs/` root + subdirs (`api/`, `setup/`, `operations/`, `runbooks/`, `reference/`, `architecture/`, `papers/`)
- Architecture Decision Records → `docs/architecture/adr/`
- Diagrams → `docs/diagrams/` or `docs/flows/`
- Security/compliance reference material (threat model, access control matrix, IEC 62443 matrix, etc.) → `docs/security/` and `docs/compliance/`
- Legal/IP → `docs/project/legal/`
- Vault snapshots → `docs/vault/` (Obsidian knowledge graph)
