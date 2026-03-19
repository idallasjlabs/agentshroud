# GSDE&G Claude Code Skills Reference

> Complete guide for using Claude Code skills in your GitHub workflow.
> Skills are invoked with: `/read skills/<category>/<skill-name>.md`

---

## Quick Reference: When to Use Each Skill

| Workflow Stage | Skill to Invoke | Purpose |
|----------------|-----------------|---------|
| Starting a task | `workflow/skill-git-guard.md` | Branch naming, workflow rules |
| Writing code | `workflow/skill-tdd.md` | TDD discipline (Red-Green-Refactor) |
| Testing in prod | `core/skill-qa.md` | Production testing procedures |
| Data validation | `data/skill-data-validation.md` | Athena queries, data quality |
| Using MCP tools | `mcp/skill-mcp-tools.md` | GitHub, Jira, AWS integrations |
| Code review | `core/skill-cr.md` | Review checklist, security |
| Creating PR | `core/skill-pr.md` | PR description template |
| Before merge | `production/skill-prod-safety.md` | Pre-deploy checklist |
| Incident | `production/skill-incident-response.md` | Rollback procedures |
| Quick reference | `reference/skill-master-checklist.md` | Combined checklist |

---

## GitHub Workflow Integration

### 1. Branch Creation
```bash
# Invoke: /read skills/workflow/skill-git-guard.md
git checkout main && git pull
git checkout -b feat/GSDE-123-add-partition-pruning
```

### 2. Development (TDD)
```bash
# Invoke: /read skills/workflow/skill-tdd.md
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
# Invoke: /read skills/core/skill-qa.md
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
# Invoke: /read skills/core/skill-pr.md
gh pr create --title "feat(data-lake): add partition pruning" --body "..."

# Invoke: /read skills/core/skill-cr.md
# Self-review using checklist
```

### 5. Pre-Merge
```bash
# Invoke: /read skills/production/skill-prod-safety.md
# Complete all checklist items:
# - [ ] RDS snapshot taken
# - [ ] Rollback plan documented
# - [ ] Blast radius assessed
```

---

## Skill Directory Structure

```
.claude/skills/
├── core/                           # Core development skills
│   ├── skill-qa.md                 # QA + Production Testing Runbook
│   ├── skill-cr.md                 # Code Review Checklist
│   └── skill-pr.md                 # PR Description Generator
├── workflow/                       # Development process
│   ├── skill-tdd.md                # TDD Coach
│   ├── skill-git-guard.md          # GitHub Workflow Rules
│   └── skill-cicd.md               # CI/CD Pipeline Design
├── production/                     # Production safety
│   ├── skill-prod-safety.md        # Pre/Post Deploy Checklist
│   └── skill-incident-response.md  # Incident Rollback Guide
├── data/                           # Data operations
│   └── skill-data-validation.md    # Athena Query Patterns
├── mcp/                            # Tool integrations
│   └── skill-mcp-tools.md          # MCP Server Usage
└── reference/                      # Quick reference
    ├── skill-master-checklist.md   # Combined Lifecycle
    └── SKILLS_GUIDE.md             # This document
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
- **QA** (`core/skill-qa.md`) - Production testing procedures, service control, DB test patterns
- **CR** (`core/skill-cr.md`) - Code review checklist with production safety checks
- **PR** (`core/skill-pr.md`) - PR description generator with rollback plans

### Workflow
- **TDD** (`workflow/skill-tdd.md`) - Test-driven development discipline
- **GIT-GUARD** (`workflow/skill-git-guard.md`) - GitHub workflow enforcement
- **CICD** (`workflow/skill-cicd.md`) - CI/CD pipeline design

### Production Safety
- **PROD-SAFETY** (`production/skill-prod-safety.md`) - Pre/post-deployment checklists
- **INCIDENT** (`production/skill-incident-response.md`) - Incident response and rollback

### Data Operations
- **DATA-VAL** (`data/skill-data-validation.md`) - Data quality validation with cost control

### MCP Tools
- **MCP-TOOLS** (`mcp/skill-mcp-tools.md`) - GitHub, Jira, AWS MCP integration

### Reference
- **MASTER** (`reference/skill-master-checklist.md`) - Combined quick-reference checklist
- **GUIDE** (`reference/SKILLS_GUIDE.md`) - This reference document

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
   - Verify cleanup with checklist (skill-qa.md Section H.4)

4. **Document everything**
   - Timestamped test logs in PR
   - Exact commands used
   - Test results and validation

---

## Emergency Procedures

### P1 Incident Response
1. **Assess** (5 min max) - Check Glue, Step Functions, CloudWatch, S3, RDS
2. **Communicate** - Post in #gsde-incidents, create Jira ticket, call lead
3. **Rollback** - Use procedures in `production/skill-incident-response.md`
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
/read skills/workflow/skill-git-guard.md
/read skills/workflow/skill-tdd.md

# When testing in production
/read skills/core/skill-qa.md

# When validating data
/read skills/data/skill-data-validation.md

# When using MCP tools
/read skills/mcp/skill-mcp-tools.md

# Before creating PR
/read skills/core/skill-pr.md
/read skills/core/skill-cr.md

# Before merge
/read skills/production/skill-prod-safety.md

# During incident
/read skills/production/skill-incident-response.md

# Quick reference
/read skills/reference/skill-master-checklist.md
```

---

## Related Documentation

- **Configuration Summary:** `.llm_settings/docs/CONFIGURATION_SUMMARY.md`
- **AI Tools Guide:** `.llm_settings/docs/AI_TOOLS_CONFIGURATION_GUIDE.md`
- **MCP Additional Services:** `.llm_settings/docs/MCP_ADDITIONAL_SERVICES.md`
- **Primary Developer Context:** `CLAUDE.md`
- **Secondary/Tertiary Agent Context:** `AGENTS.md`

---

**Last Updated:** 2026-02-09
**Repository:** LLM_Settings
**Deployment:** This file is copied to target repos via `llm-init.sh`
