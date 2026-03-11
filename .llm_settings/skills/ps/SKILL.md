# Skill: Production Safety Checklist (PROD-SAFETY)

## Role
You are a Release Engineer for the GSDE&G team.  Every production change must
be safe, reversible, and auditable.

## Invoke Before
- ANY merge to `main`
- ANY AWS infrastructure change
- ANY database migration (PostgreSQL RDS or on-site MySQL)
- ANY Zabbix / Tailscale / IAM configuration change
- ANY Glue job or Step Function modification

---

## Pre-Deployment Checklist

### 1. Change Documentation
- [ ] Tracked in Jira (GSDE / GSDEA / SORT project).
- [ ] PR has motivation, changes, and risk assessment.
- [ ] Sub-team lead approved (KP/Revathi · Tala · Keith).

### 2. Testing Evidence
- [ ] `pytest tests/ -v` passes locally.
- [ ] AWS mocked with `moto`.
- [ ] If production testing was required:
  - [ ] `_test/` S3 prefix, `_test_flag` column, or `SAVEPOINT` used.
  - [ ] Test data cleaned up.
  - [ ] Timestamped test log attached to PR.

### 3. Backups & Rollback
- [ ] **PostgreSQL:**
  ```bash
  aws rds create-db-snapshot \
    --db-instance-identifier fe-gsdl-poc-database \
    --db-snapshot-identifier pre-deploy-$(date +%Y%m%d-%H%M%S)
  ```
- [ ] **MySQL (on-site):** `mysqldump` of affected tables.
- [ ] **S3:** versioning enabled on `fluenceenergy-ops-data-lakehouse`.
- [ ] **Glue / Step Functions:** previous definition in Git history.
- [ ] **IAM:** current policy exported to JSON.
- [ ] **Zabbix:** template exported before changes.
- [ ] Rollback procedure documented with **exact commands**.
- [ ] Estimated rollback time: ______ minutes.

### 4. Blast Radius
- [ ] BESS sites affected: ______ / 200+
- [ ] Incremental rollout possible?  (1 site → 10 → all)
- [ ] Breaking for downstream consumers (Grafana, dashboards, reports)?
- [ ] Will Zabbix alerts fire?
  - [ ] Maintenance window created for affected hosts.
  - [ ] On-call engineer notified.

### 5. Observability
- [ ] Logging added (`logging.info` / `logging.error`).
- [ ] CloudWatch log groups exist for new Glue / SF jobs.
- [ ] Zabbix items / triggers updated if infra changed.
- [ ] Athena queries validated with `EXPLAIN`.

### 6. Security
- [ ] No secrets in code — use AWS Secrets Manager.
- [ ] IAM least-privilege.
- [ ] `pip-audit` + `bandit` clean.
- [ ] S3 bucket policies reviewed if paths changed.

### 7. Communication
- [ ] Sub-team lead notified.
- [ ] Stakeholders notified if user-facing.
- [ ] Site ops team aware if on-site MySQL / Zabbix touched.

---

### 8. Service Control Commands

#### Pause Before Testing (Copy-Paste Ready)

**Glue Jobs:**
```bash
# List your Glue jobs
aws glue list-jobs --query "JobNames" --output table

# Disable trigger
aws glue update-trigger --name <TRIGGER_NAME> --trigger-update State=DISABLED

# Verify disabled
aws glue get-trigger --name <TRIGGER_NAME> --query "Trigger.State"
```

**Step Functions:**
```bash
# List state machines
aws stepfunctions list-state-machines --query "stateMachines[].name" --output table

# Check running executions
aws stepfunctions list-executions \\
  --state-machine-arn arn:aws:states:us-east-1:<ACCOUNT>:stateMachine:<SM_NAME> \\
  --status-filter RUNNING --max-results 10

# Disable EventBridge schedule
aws events disable-rule --name <RULE_NAME>
```

**Zabbix (via API):**
```python
from pyzabbix import ZabbixAPI
zapi = ZabbixAPI("https://<SITE>.zabbix.fluenceenergy.com")
zapi.login(user="admin", password="...")

# Create 4-hour maintenance window
zapi.maintenance.create(
    name="PROD-TEST-<JIRA>",
    active_since=int(time.time()),
    active_till=int(time.time()) + 14400,
    hostids=["<HOST_ID>"],
    timeperiods=[{"period": 14400, "timeperiod_type": 0}]
)
```

#### Resume After Testing (MANDATORY)
```bash
# Re-enable Glue trigger
aws glue update-trigger --name <TRIGGER_NAME> --trigger-update State=ENABLED

# Re-enable EventBridge rule
aws events enable-rule --name <RULE_NAME>

# Delete Zabbix maintenance (via UI or API)
```

#### Emergency Stop (P1 Incidents Only)
```bash
# Stop ALL running Glue jobs for a specific job name
JOB_RUNS=$(aws glue get-job-runs --job-name <JOB_NAME> \\
  --query "JobRuns[?JobRunState=='RUNNING'].Id" --output text)
if [ -n "$JOB_RUNS" ]; then
  aws glue batch-stop-job-run --job-name <JOB_NAME> --job-run-ids $JOB_RUNS
fi

# Stop Step Function execution
aws stepfunctions stop-execution --execution-arn <ARN> --cause "Emergency stop - P1"
```

---

## Post-Deployment Verification

### Immediate (0–15 min)
1. CloudWatch → `ERROR` in relevant log group:
   ```bash
   aws logs filter-log-events --log-group-name /aws/glue/jobs/JOB \
     --start-time $(date -d '15 minutes ago' +%s000) --filter-pattern "ERROR"
   ```
2. Database → `SELECT` confirms change applied.
3. Zabbix → `Monitoring → Latest Data` on affected hosts.
4. Step Functions → monitor next scheduled execution.

### Short-Term (15 min – 24 hr)
1. Zabbix: new triggered alerts?
2. Spot-check pipeline outputs (parquet files).
3. Athena queries return expected results?
4. CloudWatch metrics: anomalies?

### Sign-Off
- [ ] Smoke tests passed.
- [ ] Error rates nominal 15+ min.
- [ ] No unexpected Zabbix triggers.
- [ ] Rollback mechanism verified still functional.

## If Something Goes Wrong
1. **Don't panic.**  Follow the rollback plan.
2. **Roll back first, investigate second.**
3. Create Jira incident ticket.
4. Notify sub-team lead and Isaiah.
5. Blameless post-mortem within 48 hours.
