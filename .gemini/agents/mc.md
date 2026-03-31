# GSDE&G Development Master Checklist

> Combined quick-reference for the complete development lifecycle.
> Use before every PR and deployment.

---

## Phase 1 · Plan & Branch  → `gg/SKILL.md`
- [ ] Jira ticket exists (GSDE / GSDEA / SORT).
- [ ] Branch: `<type>/<ticket>-<desc>` from `main`.

## Phase 2 · TDD  → `tdd/SKILL.md`
- [ ] **RED:** failing test(s) written.
- [ ] **GREEN:** minimum implementation to pass.
- [ ] **REFACTOR:** cleaned up, tests still green.
- [ ] AWS mocked with `moto`.  DB tests use `SAVEPOINT` + `ROLLBACK`.

## Phase 3 · QA  → `qa/SKILL.md`
- [ ] Unit + integration + regression coverage.
- [ ] If production testing needed:
  - [ ] `_test/` prefix · `_test_flag` column · `SAVEPOINT`
  - [ ] Two people present.  Timestamped log attached.
  - [ ] Test data cleaned up.

## Phase 4 · Code Review  → `cr/SKILL.md`
- [ ] ≤ 400 LoC.
- [ ] Security: IAM, S3, credentials.
- [ ] Prod safety: rollback, blast radius, alerts.
- [ ] `ruff check .` + `mypy .` pass.

## Phase 5 · Pull Request  → `pr/SKILL.md`
- [ ] Affected systems listed.
- [ ] Testing evidence attached.
- [ ] Rollback plan with exact commands.

## Phase 6 · CI  → `cicd/SKILL.md`
- [ ] All checks pass (lint, type, test, security, build).
- [ ] Manual approval for prod-impacting changes.

## Phase 7 · Deploy  → `ps/SKILL.md`
- [ ] Backups taken (RDS snapshot · mysqldump · policy export).
- [ ] Blast radius assessed — incremental if > 1 site.
- [ ] Maintenance window if Zabbix alerts expected.
- [ ] Post-deploy smoke test passed, 15+ min nominal.

---

## Emergency Hotfix
```
1. hotfix/<ticket>-<desc> from main
2. Backup → regression test → fix → verify
3. PR → expedited review → merge
4. Monitor 30 min → rollback if bad
5. Post-mortem within 48 hours
```

---

## Quick Commands
```bash
# ── Testing ──────────────────────────────────
pytest tests/ -v --tb=short

# ── Linting ──────────────────────────────────
ruff check . && ruff format --check .
mypy . --ignore-missing-imports

# ── Security ─────────────────────────────────
bandit -r src/ && pip-audit

# ── RDS Snapshot ─────────────────────────────
aws rds create-db-snapshot \
  --db-instance-identifier fe-gsdl-poc-database \
  --db-snapshot-identifier pre-deploy-$(date +%Y%m%d-%H%M%S)

# ── IAM Simulate ─────────────────────────────
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::ACCOUNT:role/ROLE \
  --action-names s3:GetObject glue:StartJobRun

# ── Athena Cost Check ────────────────────────
EXPLAIN SELECT …;

# ── Test Data Cleanup ────────────────────────
aws s3 rm s3://fluenceenergy-ops-data-lakehouse/das_catalog/_test/ --recursive
```

---

## Skill Index
| Skill | Path | Purpose |
|-------|------|---------|
| QA | `qa/SKILL.md` | Testing strategy + production test runbooks |
| CR | `cr/SKILL.md` | Code review with prod-safety checks |
| PR | `pr/SKILL.md` | PR description generator |
| TDD | `tdd/SKILL.md` | Red-Green-Refactor + stack patterns |
| GIT-GUARD | `gg/SKILL.md` | Branch policy & workflow enforcement |
| CICD | `cicd/SKILL.md` | GitHub Actions pipeline design |
| PROD-SAFETY | `ps/SKILL.md` | Pre/post-deploy checklists |
| MASTER | `mc/SKILL.md` | This file |
