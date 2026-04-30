# GSDE&G Skills Reference

> Complete guide for using skills across all LLM CLIs.
> - **Claude Code:** invoke with `/skill-name`
> - **Gemini CLI / Codex CLI:** paste `.gemini/agents/<name>.md` or `.codex/agents/<name>.md` into your prompt

---

## Quick Reference: When to Use Each Skill

| Workflow Stage | Skill | Purpose |
|----------------|-------|---------|
| Starting a task | `/gg` | Branch naming, workflow rules |
| Writing code | `/tdd` | TDD discipline (Red-Green-Refactor) |
| Testing in prod | `/qa` | Production testing procedures |
| Data validation | `/data` | Athena queries, data quality |
| Using MCP tools | `/mcpm` | GitHub, Jira, AWS integrations |
| MCP diagnostics | `/mcpm-doctor` | Diagnose MCP server issues |
| MCP auth reset | `/mcpm-auth-reset` | Reset MCP authentication |
| AWS MCP profile | `/mcpm-aws-profile` | Configure AWS MCP profile |
| Code review | `/cr` | Review checklist, security |
| Creating PR | `/pr` | PR description template |
| Before merge | `/ps` | Pre-deploy checklist |
| Incident response | `/production` | Rollback procedures |
| AWS operations | `/aws` | Cloud inventory, cost optimization, FinOps |
| Root cause analysis | `/8d` | BESS incident investigation, 8D methodology |
| Mac app inventory | `/mac` | Discover all macOS applications |
| Security review | `/sec` | SecureClaw 4-layer security review |
| Defensive security | `/sec-defense` | Blue team STPA-Sec audit |
| Offensive security | `/sec-offense` | Red team adversarial testing |
| Environment setup | `/env` | SecureClaw Pi environment management |
| Project tracking | `/pm` | SecureClaw roadmap and sprint tracking |
| Technical writing | `/tw` | Documentation authoring |
| Technical diagrams | `/ti` | Mermaid diagram generation |
| Branding | `/bs` | Visual brand consistency |
| Quick reference | `/mc` | Combined checklist |
| Browser automation | `/browser` | Playwright browser automation with security controls |
| iCloud services | `/icloud` | Calendar, Contacts, Mail via CalDAV/CardDAV |
| Podcast audio | `/apollo` | Convert scripts to audio via ElevenLabs |
| Podcast notes | `/athena` | Show notes and cheat sheets |
| Podcast curriculum | `/atlas` | Episode learning architecture |
| Podcast diagrams | `/daedalus` | PlantUML/Mermaid concept illustrations |
| Podcast references | `/hermes` | Fact-check and reference verification |
| Podcast retention | `/mnemosyne` | Spaced repetition study materials |
| Podcast feedback | `/oracle` | Episode quality analysis |
| Podcast dialogue | `/socrates` | Curriculum-to-dialogue script writing |
| Podcast audit | `/vulcan` | Technical accuracy quality gate |
| System audit docs | `/sad` | 13-section exhaustive codebase documentation |
| System audit vault | `/sav` | Complete Obsidian vault for a codebase |

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
# ... write code ...
pytest tests/test_new_feature.py -v  # Should pass

# REFACTOR: Clean up
ruff check . && ruff format .
```

### 3. Production Testing (if needed)
```bash
# Invoke: /qa
# Follow Section H for service control

# 1. Disable triggers
aws glue update-trigger --name <TRIGGER> --trigger-update State=DISABLED

# 2. Run test with _test/ prefix
# 3. Validate results
# 4. Clean up test data
# 5. Re-enable triggers (CRITICAL!)
aws glue update-trigger --name <TRIGGER> --trigger-update State=ENABLED
```

### 4. Pull Request
```bash
# Invoke: /pr
gh pr create --title "feat(data-lake): add partition pruning" --body "..."

# Invoke: /cr
# Self-review using checklist
```

### 5. Pre-Merge
```bash
# Invoke: /ps
# Complete all checklist items:
# - [ ] RDS snapshot taken
# - [ ] Rollback plan documented
# - [ ] Blast radius assessed
```

---

## Skill Directory Structure

```
.claude/skills/
├── 8d/SKILL.md                    # 8D Root Cause Analysis
├── aws/SKILL.md                   # AWS Cloud Management & FinOps
├── bs/SKILL.md                    # Branding Specialist
├── cicd/SKILL.md                  # CI/CD Pipeline Design
├── cr/SKILL.md                    # Code Review Checklist
├── data/SKILL.md                  # Athena Query Patterns
├── env/SKILL.md                   # Environment Management
├── gg/SKILL.md                    # GitHub Workflow Rules
├── mac/SKILL.md                   # Mac App Discovery
├── mc/SKILL.md                    # Combined Lifecycle Checklist
├── mcpm/SKILL.md                  # MCP Server Usage
├── mcpm-auth-reset/SKILL.md       # MCP Auth Reset
├── mcpm-aws-profile/SKILL.md      # AWS MCP Profile Configuration
├── mcpm-doctor/SKILL.md           # MCP Diagnostics
├── pm/SKILL.md                    # Project Management
├── pr/SKILL.md                    # PR Description Generator
├── production/SKILL.md            # Incident Rollback Guide
├── ps/SKILL.md                    # Pre/Post Deploy Checklist
├── qa/SKILL.md                    # QA + Production Testing Runbook
├── sec/SKILL.md                   # Security Review
├── tdd/SKILL.md                   # TDD Coach
├── ti/SKILL.md                    # Technical Illustrator
├── tw/SKILL.md                    # Technical Writer
└── reference/
    └── SKILLS_GUIDE.md            # This document
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

# AWS - IAM Simulate (before policy changes)
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::<ACCOUNT>:role/<ROLE> \
  --action-names s3:GetObject glue:StartJobRun

# AWS - Athena Cost Check
EXPLAIN SELECT ...;

# AWS - Cleanup Test Data
aws s3 rm s3://fluenceenergy-ops-data-lakehouse/das_catalog/_test/ --recursive
```

---

## Skills by Category

### Core Development
- **QA** (`/qa`) - Production testing procedures, service control, DB test patterns
- **CR** (`/cr`) - Code review checklist with production safety checks
- **PR** (`/pr`) - PR description generator with rollback plans

### Workflow
- **TDD** (`/tdd`) - Test-driven development discipline
- **GIT-GUARD** (`/gg`) - GitHub workflow enforcement
- **CICD** (`/cicd`) - CI/CD pipeline design

### Production Safety
- **PROD-SAFETY** (`/ps`) - Pre/post-deployment checklists
- **INCIDENT** (`/production`) - Incident response and rollback

### Data Operations
- **DATA-VAL** (`/data`) - Data quality validation with cost control

### Cloud & FinOps
- **AWS** (`/aws`) - AWS cloud inventory, cost optimization, FY26 40% reduction plan, script templates (bash/python), tagging governance, EBS/RDS/S3 rightsizing

### Investigation
- **8D** (`/8d`) - BESS incident root cause analysis, Athena telemetry queries, 8D methodology (D0-D8), anomaly detection, IS/IS NOT matrix, 5 Whys

### System Utilities
- **MAC** (`/mac`) - macOS application inventory (10 collection methods), categorization (22 categories), JSON manifest + Markdown catalog, web-sourced alternatives

### SecureClaw (Project-Specific)
- **SEC** (`/sec`) - 4-layer security review (application, container, network, data flow), threat model
- **ENV** (`/env`) - Raspberry Pi environment management, Docker hardening, ARM64 considerations, CI/CD workflow
- **PM** (`/pm`) - 8-phase roadmap tracking, continuity files, sprint management, 6-agent coordination

### MCP Tools
- **MCPM** (`/mcpm`) - GitHub, Jira, AWS MCP integration
- **MCPM-DOCTOR** (`/mcpm-doctor`) - Diagnose MCP server issues
- **MCPM-AUTH-RESET** (`/mcpm-auth-reset`) - Reset MCP authentication
- **MCPM-AWS-PROFILE** (`/mcpm-aws-profile`) - Configure AWS MCP profile

### Content & Communication
- **TW** (`/tw`) - Technical documentation authoring: READMEs, runbooks, ADRs, API reference
- **TI** (`/ti`) - Mermaid diagram generation: architecture, data flow, sequence, ER, state diagrams
- **BS** (`/bs`) - Brand consistency: color tokens, typography, diagram themes, voice & tone

### Reference
- **MASTER** (`/mc`) - Combined quick-reference checklist
- **GUIDE** (this document) - Skills reference guide

---

## Production Testing Guidelines

Since we deploy directly to production:

1. **Always disable services before testing**
   - Glue triggers: `aws glue update-trigger --name <TRIGGER> --trigger-update State=DISABLED`
   - Step Function schedules: `aws events disable-rule --name <RULE>`
   - Zabbix: Put host in maintenance mode

2. **Use test isolation patterns**
   - S3: `_test/` prefix
   - Database: `_test_flag` column with SAVEPOINT/ROLLBACK
   - Never commit test data

3. **Always cleanup and re-enable**
   - Remove test data from S3, database, Athena
   - Re-enable all triggers and schedules
   - Verify cleanup with checklist (`/qa` Section H.4)

4. **Document everything**
   - Timestamped test logs in PR
   - Exact commands used
   - Test results and validation

---

## Emergency Procedures

### P1 Incident Response
1. **Assess** (5 min max) - Check Glue, Step Functions, CloudWatch, S3, RDS
2. **Communicate** - Post in #gsde-incidents, create Jira ticket, call lead
3. **Rollback** - Use `/production` for detailed rollback procedures
4. **Post-mortem** - Blameless review within 48 hours

### Emergency Contacts
- **GSDE Lead:** KP or Revathi
- **GSDEA Lead:** Tala
- **SORT Lead:** Keith
- **Overall:** Isaiah

---

## Skill Invocation Examples

```bash
# When starting a new feature
/gg
/tdd

# When testing in production
/qa

# When validating data
/data

# When using MCP tools
/mcpm

# MCP diagnostics
/mcpm-doctor

# Reset MCP auth
/mcpm-auth-reset

# Configure AWS MCP profile
/mcpm-aws-profile

# Before creating PR
/pr
/cr

# Before merge
/ps

# During incident
/production

# AWS operations
/aws

# Root cause analysis
/8d

# Mac app inventory
/mac

# SecureClaw security review
/sec

# SecureClaw environment setup
/env

# SecureClaw project tracking
/pm

# Technical documentation
/tw

# Creating a diagram
/ti

# Brand consistency check
/bs

# Quick reference
/mc
```

---

## Related Documentation

- **Configuration Summary:** `.llm_settings/docs/CONFIGURATION_SUMMARY.md`
- **AI Tools Guide:** `.llm_settings/docs/AI_TOOLS_CONFIGURATION_GUIDE.md`
- **MCP Additional Services:** `.llm_settings/docs/MCP_ADDITIONAL_SERVICES.md`
- **Primary Developer Context:** `CLAUDE.md`
- **Secondary/Tertiary Agent Context:** `AGENTS.md`

---

**Last Updated:** 2026-03-02
**Repository:** LLM_Settings
**Deployment:** This file is copied to target repos via `llm-init.sh`
**Skills:** 36 skills — universal across Claude Code (`/skill`), Gemini CLI (`@skill`), Codex CLI (`@skill`)
