# DEVELOPER.md — Development Context for AgentShroud

This file gives you the same development rules, standards, and tooling guidance that
Claude Code uses when working directly in this repository. Read it at the start of any
development session. For deeper context on a specific task, read the relevant skill or
agent file from `.claude/skills/` or `.claude/agents/` as directed below.

---

## 1. Owner & Governance Context

| Field | Value |
|-------|-------|
| **Owner** | Isaiah Jefferson, Chief Innovation Engineer, Fluence Energy |
| **Team** | GSDE&G (Global Services Digital Enablement & Governance) |
| **Sub-teams** | GSDE (Data Engineering), GSDEA (Digital Enablement), SORT (SysOps Reliability) |
| **Standards** | ITIL v4, ISO 20000/9001, NIST CSF, IEC 62443 |
| **Core principle** | Build systems, not one-offs. Automate everything worth repeating. |

**Working style:** structured output, markdown tables, production-ready code, no fluff,
explicit assumptions. Always include executive summary + risk callouts + verification steps.
Never suggest `apt-get install` or `brew install` — use Nix/Home Manager.

**Glossary:** BESS=Battery Energy Storage System, DAS=Distributed Acquisition System,
FODL=Fluence Online Data Lakehouse, EMS=Energy Management System, GSDE&G=Global Services
Digital Enablement & Governance, SORT=SysOps Reliability Team, MCP=Model Context Protocol,
ITIL=IT Infrastructure Library, PKE=Personal Knowledge Engine, OKE=Offspring Knowledge Engine.

---

## 2. Project

AgentShroud™ is a transparent security proxy between AI agents and the systems they interact
with. Every API call, file write, and tool invocation is intercepted, inspected, logged, and
policy-enforced without disrupting the agent's native workflow.

```
AI Agent → AgentShroud Gateway (33 security modules) → Target System
```

**Current branch:** `feat/v0.9.0-soc-team-collab` ("Sentinel") — v0.9.0 → v1.0.0
**Test coverage:** ≥94% — 3,404+ tests total; maintain or improve
**Language:** Python 3.9+, Node.js 22

| Path | Contents |
|------|----------|
| `gateway/` | Core proxy, runtime, ingest API, SSH proxy |
| `gateway/security/` | All 33 security modules |
| `gateway/soc/` | SOC team collaboration (v0.9.0 focus) |
| `gateway/proxy/` | Request interception and routing |
| `gateway/tests/` | Primary test suite |
| `docker/` | Container stack (Falco, ClamAV, Wazuh, Fluent Bit) |

---

## 3. Prime Directive

- **Do NOT create new files** unless absolutely required.
- **Prefer editing existing files** over adding new ones.
- **Never create documentation** (`*.md`, README) unless explicitly requested.
- Never broaden scope beyond the explicit request.
- Never perform opportunistic refactors.

---

## 4. Development Rules (TDD)

For ALL code behavior changes follow Red-Green-Refactor:

1. **RED** — Write the smallest failing unit test first. Confirm it fails for the right reason.
2. **GREEN** — Implement the minimum code to pass. No speculative features.
3. **REFACTOR** — Clean up while tests stay green. Run the full suite after every step.

**Test rules:**
- No real network calls, no real AWS calls, no sleeps, no timing dependencies.
- Prefer pure functions, dependency injection, small deterministic fixtures.
- Coverage ≥80% on new or modified code (project target: ≥94%).

**Definition of Done:** strictly scoped, existing behavior preserved, impacted workflow runs,
evidence of validation (tests first, then data validation, then script execution).

---

## 5. Language & Tooling Standards

**Python:**
- Test runner: `pytest` / `pytest -q`
- Format: `black .`
- Lint: `ruff check .` (with `--fix` for auto-fix)
- Type check: `mypy .`
- Coverage: `pytest --cov=gateway --cov-report=term-missing`

**Node.js:** `jest` or `vitest`, React Testing Library, `tsc`, ESLint

**Security:** treat all inputs as untrusted, parameterize queries, no secrets in code,
least privilege, validate at boundaries (user input, external APIs only).

---

## 6. SSH Development Workflow

You access the repo on marvin via SSH. Use these commands:

| Action | Command |
|--------|---------|
| Run tests | `ssh marvin dev test` |
| Build containers | `ssh marvin dev build` |
| Rebuild + restart | `ssh marvin dev rebuild` |
| Check status | `ssh marvin dev status` |
| View logs | `ssh marvin dev logs` |
| Git pull | `ssh marvin dev pull` |

**Repo path on marvin:** `/Users/agentshroud-bot/Development/agentshroud`
**Compose file:** `docker/docker-compose.yml`

**After Python changes — always run:**
```
ssh marvin dev test
```
And lint/format (single atomic commands via dev helper or separate ssh calls):
```
ssh marvin "ruff check --fix /Users/agentshroud-bot/Development/agentshroud/gateway/"
ssh marvin "black /Users/agentshroud-bot/Development/agentshroud/gateway/"
```

**Before dangerous bash — pause and warn yourself:** never run `rm -rf /`, `curl | sh`,
`chmod -R 777`, or fork bombs. If a requested command looks destructive, say so first.

---

## 7. Agent Orchestration

Before starting a task, read the relevant agent file from `.claude/agents/` for role-specific
guidance. Use these chains:

| Task | Agent Chain |
|------|-------------|
| Feature development | `product-agent` → `architecture-agent` → `tdd-engineer` → `qa-agent` → `security-reviewer` → `ci-agent` → `release-engineer` |
| Bug investigation | `debugging-agent` → `qa-agent` → `security-reviewer` |
| Production incident | `incident-commander` → `diagnostics-agent` → `sre-agent` → `observability-agent` → `postmortem-agent` |
| Release | `release-engineer` → `ci-agent` → `deploy-agent` |
| Architecture change | `architecture-agent` → `security-reviewer` → `performance-agent` |

**Example:** For a feature task, read `.claude/agents/tdd-engineer.md` before writing tests,
`.claude/agents/security-reviewer.md` before the security pass.

---

## 8. Skill Lookup

Before starting a task, read the relevant skill from `.claude/skills/{name}/SKILL.md`.
Skills contain detailed step-by-step instructions and checklists.

| Trigger | Skill Path |
|---------|-----------|
| Writing/reviewing tests | `.claude/skills/tdd/SKILL.md` |
| Creating a PR | `.claude/skills/pr/SKILL.md` |
| Security review | `.claude/skills/sec/SKILL.md` |
| Code review | `.claude/skills/cr/SKILL.md` |
| QA pass | `.claude/skills/qa/SKILL.md` |
| CI/CD pipeline work | `.claude/skills/cicd/SKILL.md` |
| Production safety check | `.claude/skills/ps/SKILL.md` |
| Git workflow / branch hygiene | `.claude/skills/gg/SKILL.md` |
| Defensive security audit | `.claude/skills/sec-defense/SKILL.md` |
| Red team / offensive test | `.claude/skills/sec-offense/SKILL.md` |
| SRE work | `.claude/skills/sre/SKILL.md` |
| AWS infrastructure | `.claude/skills/aws/SKILL.md` |
| Data validation | `.claude/skills/data/SKILL.md` |
| Architecture review | `.claude/skills/architecture-review/SKILL.md` |

Other available skills: `agile`, `bdd`, `bs`, `cd`, `chaos-engineering`, `ci`, `competitive-analysis`,
`daedalus`, `devsecops`, `gitops`, `hermes`, `icloud`, `incident-response`, `kaizen`, `kanban`,
`mac`, `mc`, `mcpm`, `mcpm-auth-reset`, `mcpm-aws-profile`, `mcpm-doctor`, `mm`, `mnemosyne`,
`observability`, `oracle`, `pm`, `production`, `sad`, `sav`, `scrum`, `sdlc`, `socrates`,
`ti`, `tw`, `ui`, `ux`, `value-stream-mapping`, `vulcan`, `8d`.

Full descriptions: `.claude/skills/reference/SKILLS_GUIDE.md`

---

## 9. Repository Guardrails

1. **Test coverage** — Must stay ≥94%. All new code requires tests before merge.
2. **No module stubs** — Every security module must be fully wired in the pipeline.
3. **Trademark** — Never remove or alter AgentShroud™ trademark notices.
4. **IEC 62443 alignment** — Security changes must reference IEC 62443 FRs.
5. **Semgrep rules** — New code must pass `.semgrep.yml` SAST rules.
6. **Approval queue** — Actions touching email_sending, file_deletion, external_api_calls,
   or skill_installation must route through the approval queue.
7. **Data platform** — No schema drift in Parquet outputs, validate schemas before publishing
   Athena tables, never break S3 partition compatibility.
8. **PII redaction** — Presidio engine at 0.9 confidence minimum; do not lower the threshold.
