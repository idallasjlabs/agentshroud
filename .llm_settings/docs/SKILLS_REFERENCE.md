# GSDE&G Claude Code Skills Reference

> Complete guide for using Claude Code skills. Skills are invoked with: `/<skill-name>`
> Example: `/tdd`, `/pr`, `/eightd`

**Last Updated:** 2026-08-10 | **Total Skills:** 59

---

## Quick Reference: When to Use Each Skill

| Workflow Stage | Skill | Purpose |
|----------------|-------|---------|
| Starting a task | `/gg` | Branch naming, workflow rules |
| Writing code (TDD) | `/tdd` | Red-Green-Refactor cycle |
| Code review | `/cr` | Security-focused review checklist |
| Creating PR | `/pr` | PR description with rollback plan |
| Pre-deploy safety | `/ps` | Pre/post-deploy checklist |
| Production incident | `/production` | Severity matrix + rollback |
| Incident response | `/incident-response` | Rollback-first procedures |
| Root cause analysis | `/eightd` | 8D-RCA for BESS incidents |
| Data validation | `/data` | Athena partition + schema checks |
| AWS operations | `/aws` | Cost, rightsizing, FinOps |
| Security audit | `/sec` | App/container/network security |
| Observability | `/observability` | Metrics, logs, traces, dashboards |
| CI/CD pipeline | `/cicd` | Pipeline design + quality gates |
| Architecture review | `/architecture-review` | Scalability, coupling, failure modes |
| MCP diagnostics | `/mcpm-doctor` | Diagnose MCP connectivity |

---

## Skill Directory Structure

All skills live under `.claude/skills/<name>/SKILL.md` (flat structure):

```
.claude/skills/
├── agile/SKILL.md
├── apollo/SKILL.md
├── architecture-review/SKILL.md
├── athena/SKILL.md
├── atlas/SKILL.md
├── aws/SKILL.md
├── bdd/SKILL.md
├── browser/SKILL.md
├── bs/SKILL.md
├── cd/SKILL.md
├── chaos-engineering/SKILL.md
├── ci/SKILL.md
├── cicd/SKILL.md
├── cr/SKILL.md
├── daedalus/SKILL.md
├── data/SKILL.md
├── devsecops/SKILL.md
├── eightd/SKILL.md
├── gg/SKILL.md
├── gitops/SKILL.md
├── hdev/SKILL.md
├── hermes/SKILL.md
├── icloud/SKILL.md
├── incident-response/SKILL.md
├── kaizen/SKILL.md
├── kanban/SKILL.md
├── mac/SKILL.md
├── mc/SKILL.md
├── mcpm/SKILL.md
├── mcpm-auth-reset/SKILL.md
├── mcpm-aws-profile/SKILL.md
├── mcpm-doctor/SKILL.md
├── mm/SKILL.md
├── mnemosyne/SKILL.md
├── observability/SKILL.md
├── odev/SKILL.md
├── oracle/SKILL.md
├── pm/SKILL.md
├── pr/SKILL.md
├── production/SKILL.md
├── ps/SKILL.md
├── qa/SKILL.md
├── sad/SKILL.md
├── sav/SKILL.md
├── scrum/SKILL.md
├── sdlc/SKILL.md
├── sec/SKILL.md
├── sec-defense/SKILL.md
├── sec-offense/SKILL.md
├── session-prompt/SKILL.md
├── socrates/SKILL.md
├── sre/SKILL.md
├── tdd/SKILL.md
├── ti/SKILL.md
├── tw/SKILL.md
├── ui/SKILL.md
├── ux/SKILL.md
├── value-stream-mapping/SKILL.md
├── vulcan/SKILL.md
└── reference/SKILLS_GUIDE.md
```

---

## Skills by Category

### Core Development (9)
| Skill | Invoke | Description |
|-------|--------|-------------|
| **tdd** | `/tdd` | Enforce Red-Green-Refactor cycle; pytest, moto, SAVEPOINT, and mocks |
| **cr** | `/cr` | Security-focused code review; production safety, blast radius, rollback |
| **pr** | `/pr` | Generate production-ready PR descriptions with safety assessment and rollback plans |
| **qa** | `/qa` | Multi-layered testing strategies (unit, integration, system, regression) |
| **bdd** | `/bdd` | Gherkin-style specs and Given/When/Then scenarios as living documentation |
| **architecture-review** | `/architecture-review` | Review system architecture for scalability, coupling, failure modes |
| **tw** | `/tw` | Write clear technical documentation (READMEs, runbooks, ADRs) |
| **sad** | `/sad` | System Audit Documentation — exhaustive plainly-written docs for any codebase |
| **sav** | `/sav` | System Audit Vault — full Obsidian vault of interconnected notes from a codebase |

### CI/CD & Deployment (6)
| Skill | Invoke | Description |
|-------|--------|-------------|
| **ci** | `/ci` | Configure CI pipelines: automated builds, test execution, artifact management |
| **cd** | `/cd` | Continuous delivery: automated promotion, feature flags, rollback gates |
| **cicd** | `/cicd` | Design and validate CI/CD pipelines with quality gates |
| **gitops** | `/gitops` | Manage infrastructure via Git: declarative state, drift detection |
| **gg** | `/gg` | Enforce GitHub workflow: branch naming, protected main, mandatory PR reviews |
| **devsecops** | `/devsecops` | Embed security into CI/CD: SAST, DAST, dependency scanning, secrets detection |

### Production Safety & Incident Response (4)
| Skill | Invoke | Description |
|-------|--------|-------------|
| **production** | `/production` | Incident response with severity matrix, mitigation, and rollback protocols |
| **ps** | `/ps` | Pre/post-deployment checklists: backups, blast radius, smoke tests |
| **incident-response** | `/incident-response` | Rapid incident response with rollback-first philosophy and blameless post-mortems |
| **eightd** | `/eightd` | 8D root cause analysis for BESS incidents; z-score anomaly detection |

### Security (4)
| Skill | Invoke | Description |
|-------|--------|-------------|
| **sec** | `/sec` | Audit application, container, network, and data security |
| **sec-defense** | `/sec-defense` | Blue team security: STPA-Sec methodology, module enforcement, heat map verification |
| **sec-offense** | `/sec-offense` | Red team: offensive testing, exploit PoCs, bypass testing, defense validation |
| **chaos-engineering** | `/chaos-engineering` | Inject controlled failures to test resilience and validate recovery paths |

### AWS & Data (3)
| Skill | Invoke | Description |
|-------|--------|-------------|
| **aws** | `/aws` | AWS infrastructure: cost optimization, rightsizing EC2/EBS/RDS/S3, tagging governance |
| **data** | `/data` | Validate data integrity and cost in Athena queries using partition filters |
| **observability** | `/observability` | Instrument systems with metrics, logs, traces; build dashboards and alerts |

### Agile / Process (7)
| Skill | Invoke | Description |
|-------|--------|-------------|
| **agile** | `/agile` | Apply Agile: iterative planning, sprint ceremonies, backlog refinement |
| **scrum** | `/scrum` | Run Scrum ceremonies: sprint planning, standups, reviews, retrospectives |
| **kanban** | `/kanban` | Visualize workflow, limit WIP, optimize cycle time with flow metrics |
| **kaizen** | `/kaizen` | Continuous improvement: identify waste, measure flow, drive incremental optimization |
| **sdlc** | `/sdlc` | SDLC governance: stage gates, artifact tracking, compliance checkpoints |
| **value-stream-mapping** | `/value-stream-mapping` | Map end-to-end value delivery to surface bottlenecks and handoff waste |
| **pm** | `/pm` | Project phases, task tracking, continuity files for delivery and status reporting |

### SRE & Reliability (2)
| Skill | Invoke | Description |
|-------|--------|-------------|
| **sre** | `/sre` | SRE practices: SLOs/SLIs/error budgets, toil reduction, runbooks, post-mortems |
| **mc** | `/mc` | Master checklist for the complete development lifecycle |

### MCP Management (4)
| Skill | Invoke | Description |
|-------|--------|-------------|
| **mcpm** | `/mcpm` | Guide MCP server usage for GitHub, Atlassian, AWS with tool-selection best practices |
| **mcpm-doctor** | `/mcpm-doctor` | Diagnose MCP server connectivity and configuration issues |
| **mcpm-auth-reset** | `/mcpm-auth-reset` | Reset authentication for GitHub, Atlassian, AWS MCP servers |
| **mcpm-aws-profile** | `/mcpm-aws-profile` | Configure and switch AWS profiles for MCP operations |

### UI / UX / Design (4)
| Skill | Invoke | Description |
|-------|--------|-------------|
| **ui** | `/ui` | UI components using brand tokens, CSS architecture, WCAG AA accessibility |
| **ux** | `/ux` | Information architecture, user flows, interaction patterns (Nielsen heuristics) |
| **bs** | `/bs` | Brand systems: design tokens, voice guidelines, visual consistency |
| **ti** | `/ti` | Mermaid diagrams from code with brand theme; validate before exporting SVG |

### Knowledge & Documentation (4)
| Skill | Invoke | Description |
|-------|--------|-------------|
| **mm** | `/mm` | Structure complex knowledge hierarchically using XMind and Markmap |
| **session-prompt** | `/session-prompt` | Survey a repo and generate SESSION_PROMPT.md for LLM config injection |
| **mac** | `/mac` | Discover and catalog all applications on a macOS system |
| **icloud** | `/icloud` | Manage iCloud Calendar, Contacts, Mail, and Notes |

### Browser Automation (1)
| Skill | Invoke | Description |
|-------|--------|-------------|
| **browser** | `/browser` | Playwright-powered browser automation with URL allowlisting and audit logging |

### Autonomous Remote Dev Workflows (2)
| Skill | Invoke | Description |
|-------|--------|-------------|
| **hdev** | `/hdev` | Autonomous dev workflow for Hermes under the `agentshroud-bot` account — branch, code, test, multi-LLM review, PR, halt for merge approval |
| **odev** | `/odev` | Autonomous dev workflow for OpenClaw under the `agentshroud-bot` account — branch, code, test, multi-LLM review, PR, halt for merge approval |

### Podcast Pipeline (9)
| Skill | Invoke | Role in Pipeline |
|-------|--------|-----------------|
| **atlas** | `/atlas` | Curriculum Architect — learning objectives, episode structure (Bloom's Taxonomy) |
| **socrates** | `/socrates` | Dialogue Architect — transforms curriculum into two-person dialogue |
| **daedalus** | `/daedalus` | Concept Illustrator — PlantUML and Mermaid diagrams for key concepts |
| **hermes** | `/hermes` | Reference Verifier — fact-checks claims, generates reference lists |
| **vulcan** | `/vulcan` | Subject Matter Auditor — quality gate before audio production |
| **apollo** | `/apollo` | Audio Producer — converts scripts to audio via ElevenLabs API |
| **athena** | `/athena` | Knowledge Distiller — extracts show notes and cheat sheets |
| **mnemosyne** | `/mnemosyne` | Retention Engineer — spaced repetition study materials |
| **oracle** | `/oracle` | Feedback Analyst — analyzes episode quality and audience impact |

---

## GitHub Workflow Integration

### 1. Branch Creation
```bash
# Invoke: /gg
git checkout main && git pull
git checkout -b feat/GSDE-123-add-partition-pruning
```

### 2. Development (TDD)
```bash
# Invoke: /tdd
# RED: Write failing test
pytest tests/test_new_feature.py -v  # Should fail
# GREEN: Implement minimum code
pytest tests/test_new_feature.py -v  # Should pass
# REFACTOR: Clean up
ruff check . && ruff format .
```

### 3. Pull Request
```bash
# Invoke: /pr then /cr
gh pr create --title "feat(data-lake): ..." --body "..."
# Self-review using CR checklist
```

### 4. Pre-Merge
```bash
# Invoke: /ps
# Complete all checklist items:
# - [ ] RDS snapshot taken
# - [ ] Rollback plan documented
# - [ ] Blast radius assessed
```

---

## Common Commands Quick Reference

```bash
# Testing
pytest tests/ -v --tb=short

# Linting
ruff check . && ruff format --check .
mypy . --ignore-missing-imports

# Security
bandit -r src/ && pip-audit

# AWS - RDS Snapshot (before deploy)
aws rds create-db-snapshot \
  --db-instance-identifier fe-gsdl-poc-database \
  --db-snapshot-identifier pre-deploy-$(date +%Y%m%d-%H%M%S)

# AWS - Athena Cost Check
EXPLAIN SELECT ...;

# AWS - Cleanup Test Data
aws s3 rm s3://fluenceenergy-ops-data-lakehouse/das_catalog/_test/ --recursive
```

---

## Production Testing Guidelines

Since we deploy directly to production:

1. **Always disable services before testing**
   - Glue triggers: `aws glue update-trigger --name <TRIGGER> --trigger-update State=DISABLED`
   - Step Function schedules: `aws events disable-rule --name <RULE>`

2. **Use test isolation patterns**
   - S3: `_test/` prefix
   - Database: `_test_flag` column with SAVEPOINT/ROLLBACK

3. **Always cleanup and re-enable**
   - Remove test data from S3, database, Athena
   - Re-enable all triggers and schedules

---

## Related Documentation

- **Configuration Summary:** `.llm_settings/docs/CONFIGURATION_SUMMARY.md`
- **AI Tools Guide:** `.llm_settings/docs/AI_TOOLS_CONFIGURATION_GUIDE.md`
- **MCP Setup:** `.llm_settings/docs/MCP_README.md`
- **AWS MCP:** `.llm_settings/docs/MCP_ADDITIONAL_SERVICES.md`
- **Primary Developer Context:** `CLAUDE.md`
- **Secondary/Tertiary Agent Context:** `AGENTS.md`
