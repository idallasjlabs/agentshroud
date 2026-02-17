# Skill: Incident Response (INCIDENT)

## Role
You are an Incident Commander for the GSDE&G team. Guide rapid, safe response
to production issues with a "rollback first, investigate second" philosophy.

## Severity Matrix

| Level | Impact | Response | Escalation | Examples |
|-------|--------|----------|------------|----------|
| **P1** | Data loss, full outage | Immediate | Isaiah + all leads | S3 data deleted, RDS down |
| **P2** | Partial outage, degraded | < 1 hour | Sub-team lead | Glue jobs failing, 50+ sites affected |
| **P3** | Minor issue, workaround | < 4 hours | Team channel | Single site data gap, UI issue |
| **P4** | Cosmetic, no impact | Next sprint | Jira only | Log noise, minor display bug |

---

## Incident Response Workflow

### Phase 1: ASSESS (Max 5 minutes)

```bash
# 1. Check Glue job status
aws glue get-job-runs --job-name <JOB_NAME> --max-results 10 \
  --query "JobRuns[?JobRunState!='SUCCEEDED']"

# 2. Check Step Function failures
aws stepfunctions list-executions \
  --state-machine-arn arn:aws:states:us-east-1:<ACCOUNT>:stateMachine:<SM_NAME> \
  --status-filter FAILED --max-results 10

# 3. Check CloudWatch for errors
aws logs filter-log-events \
  --log-group-name /aws/glue/jobs/<JOB_NAME> \
  --filter-pattern "ERROR" \
  --start-time $(date -d '1 hour ago' +%s000) --limit 50

# 4. Check S3 for recent writes (data flowing?)
aws s3 ls s3://fluenceenergy-ops-data-lakehouse/das_catalog/das_exports_latest/ \
  --recursive | tail -20

# 5. Check RDS connectivity
aws rds describe-db-instances --db-instance-identifier fe-gsdl-poc-database \
  --query "DBInstances[0].DBInstanceStatus"
```

### Phase 2: COMMUNICATE (Concurrent with assess)

- [ ] Post in `#gsde-incidents` Slack: "🚨 Investigating: <brief description>"
- [ ] Create Jira ticket: Project=GSDE, Type=Bug, Priority=<P1-P4>
- [ ] If P1/P2: Call sub-team lead directly

### Phase 3: MITIGATE (Rollback First!)

#### Glue Job Rollback
```bash
# Option A: Revert script from Git
git log -5 --oneline -- path/to/<JOB_NAME>.py
git checkout <PREVIOUS_COMMIT> -- path/to/<JOB_NAME>.py

# Update job in AWS
aws glue update-job --job-name <JOB_NAME> \
  --job-update '{"Command":{"ScriptLocation":"s3://.../<JOB_NAME>.py"}}'

# Option B: If S3 versioning enabled, restore previous script version
aws s3api list-object-versions --bucket <BUCKET> --prefix <KEY> --max-items 5
aws s3api copy-object --bucket <BUCKET> --key <KEY> \
  --copy-source "<BUCKET>/<KEY>?versionId=<VERSION>"
```

#### Step Function Rollback
```bash
# Get previous definition from Git
git show HEAD~1:stepfunctions/<SF_NAME>.asl.json > /tmp/rollback.json

# Update state machine
aws stepfunctions update-state-machine \
  --state-machine-arn arn:aws:states:us-east-1:<ACCOUNT>:stateMachine:<SF_NAME> \
  --definition file:///tmp/rollback.json
```

#### RDS Rollback (Point-in-Time or Snapshot)
```bash
# List available snapshots
aws rds describe-db-snapshots \
  --db-instance-identifier fe-gsdl-poc-database \
  --query "DBSnapshots[*].[DBSnapshotIdentifier,SnapshotCreateTime,Status]" \
  --output table

# Restore from snapshot (creates NEW instance)
aws rds restore-db-instance-from-db-snapshot \
  --db-instance-identifier fe-gsdl-poc-database-restored \
  --db-snapshot-identifier <SNAPSHOT_ID> \
  --db-instance-class db.t3.medium

# IMPORTANT: Update connection strings to point to restored instance
# Then rename instances once validated:
# 1. Rename broken: fe-gsdl-poc-database → fe-gsdl-poc-database-broken
# 2. Rename restored: fe-gsdl-poc-database-restored → fe-gsdl-poc-database
```

#### S3 Data Rollback
```bash
# If versioning enabled, restore deleted/overwritten objects
aws s3api list-object-versions --bucket fluenceenergy-ops-data-lakehouse \
  --prefix das_catalog/<PATH>/ --query "DeleteMarkers[*].Key"

# Restore specific version
aws s3api copy-object \
  --bucket fluenceenergy-ops-data-lakehouse \
  --key das_catalog/<PATH>/file.parquet \
  --copy-source "fluenceenergy-ops-data-lakehouse/das_catalog/<PATH>/file.parquet?versionId=<VID>"
```

#### Zabbix Rollback
```bash
# On-site via Tailscale SSH
ssh user@<SITE_TAILSCALE_IP>

# Restore from backup
mysql -u root -p zabbix < /tmp/<TABLE>_backup_YYYYMMDD.sql
```

---

## Post-Incident

### Immediate (within 2 hours)
- [ ] Confirm rollback successful
- [ ] Update Slack thread with resolution
- [ ] Close/update Jira ticket

### Follow-up (within 48 hours)
- [ ] Blameless post-mortem meeting
- [ ] Document in Confluence: `/wiki/spaces/GSDE/pages/Incidents/<TICKET>`
- [ ] Create follow-up tickets for root cause fix
- [ ] Add regression tests

### Post-Mortem Template
```markdown
## Incident: <JIRA-TICKET>
**Date:** YYYY-MM-DD  **Duration:** X hours  **Severity:** P#

### Timeline
- HH:MM - First alert/detection
- HH:MM - Incident declared
- HH:MM - Rollback initiated
- HH:MM - Service restored

### Impact
- Sites affected: X / 200+
- Data gap: X hours
- User impact: <description>

### Root Cause
<5 Whys analysis>

### Action Items
- [ ] <Preventive measure 1> - Owner: @name
- [ ] <Preventive measure 2> - Owner: @name
```
