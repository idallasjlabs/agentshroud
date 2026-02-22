#!/usr/bin/env bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
# =============================================================================
# deploy-claude-skills.sh (Additional Skills)
#
# Deploys additional Claude Code skills for the GSDE&G Development Team.
# Adds: MCP Tools | Incident Response | Data Validation
#
# Intended location:
#   .claude/scripts/missing/deploy-claude-skills.sh
#
# Deploys to:
#   ../../skills/   (relative to this script)
#
# Hierarchy:
#   skills/
#   ├── mcp/                        ← MCP tools integration
#   │   └── skill-mcp-tools.md
#   ├── production/                 ← Additional production skills
#   │   └── skill-incident-response.md
#   └── data/                       ← Data validation
#       └── skill-data-validation.md
#
# Usage:
#   chmod +x deploy-claude-skills.sh
#   ./deploy-claude-skills.sh            # deploy
#   ./deploy-claude-skills.sh --dry-run  # preview only
#   ./deploy-claude-skills.sh --clean    # remove and redeploy
# =============================================================================

set -euo pipefail

# ── Resolve paths relative to THIS script ────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)/skills"
TIMESTAMP="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
DRY_RUN=false
CLEAN=false

# ── Parse arguments ──────────────────────────────────────────────────────────
while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run) DRY_RUN=true; shift ;;
    --clean)   CLEAN=true;   shift ;;
    -h|--help)
      echo "Usage: $0 [--dry-run] [--clean]"
      echo ""
      echo "  --dry-run  Preview what would be created (no writes)"
      echo "  --clean    Remove existing skills directory and redeploy"
      echo ""
      echo "  Script:  $0"
      echo "  Target:  $SKILLS_ROOT/"
      exit 0
      ;;
    *) echo "Error: Unknown option '$1'"; exit 1 ;;
  esac
done

# ── Helpers ──────────────────────────────────────────────────────────────────
info()    { printf "\033[1;34m[INFO]\033[0m  %s\n" "$1"; }
success() { printf "\033[1;32m  OK  \033[0m  %s\n" "$1"; }
warn()    { printf "\033[1;33m[WARN]\033[0m  %s\n" "$1"; }
header()  { printf "\n\033[1;36m── %s ──\033[0m\n" "$1"; }

write_file() {
  # $1 = relative path under SKILLS_ROOT   $2 = content
  local fpath="$SKILLS_ROOT/$1"
  if $DRY_RUN; then
    info "[DRY RUN] Would create: $fpath"
    return
  fi
  mkdir -p "$(dirname "$fpath")"
  printf '%s\n' "$2" > "$fpath"
  success "$1"
}

# ── Clean if requested ───────────────────────────────────────────────────────
if $CLEAN && ! $DRY_RUN; then
  if [[ -d "$SKILLS_ROOT/mcp" ]]; then
    warn "Removing existing: $SKILLS_ROOT/mcp"
    rm -rf "$SKILLS_ROOT/mcp"
  fi
  if [[ -d "$SKILLS_ROOT/data" ]]; then
    warn "Removing existing: $SKILLS_ROOT/data"
    rm -rf "$SKILLS_ROOT/data"
  fi
  if [[ -f "$SKILLS_ROOT/production/skill-incident-response.md" ]]; then
    warn "Removing existing: $SKILLS_ROOT/production/skill-incident-response.md"
    rm -f "$SKILLS_ROOT/production/skill-incident-response.md"
  fi
fi

# =============================================================================
#  BANNER
# =============================================================================
echo ""
echo "  ╔══════════════════════════════════════════════════════════════╗"
echo "  ║   GSDE&G  Additional Claude Code Skills — Deployer          ║"
echo "  ╚══════════════════════════════════════════════════════════════╝"
info "Script : $SCRIPT_DIR/$(basename "$0")"
info "Target : $SKILLS_ROOT/"
info "Time   : $TIMESTAMP"
$DRY_RUN && warn "Mode   : DRY RUN — no files will be written"
$CLEAN   && warn "Mode   : CLEAN — existing skills removed first"

# =============================================================================
#                         S K I L L   C O N T E N T
# =============================================================================

###############################################################################
# ┌─────────────────────────────────────────────────────────────────────────┐ #
# │  mcp/skill-mcp-tools.md  —  MCP Server Usage Guide                     │ #
# └─────────────────────────────────────────────────────────────────────────┘ #
###############################################################################
header "mcp/ — MCP Tools Integration"

read -r -d '' SKILL_MCP << 'ENDSKILL' || true
# Skill: MCP Tools Usage (MCP-TOOLS)

## Role
You are an integration specialist guiding the use of MCP (Model Context Protocol)
servers for the GSDE&G team. Help developers leverage external tools effectively.

## Available MCP Servers

| Server | Purpose | Auth Required |
|--------|---------|---------------|
| GitHub | Code search, PRs, issues | OAuth (Device Flow) |
| Atlassian | Jira tickets, Confluence docs | OAuth 2.0 (3LO) |
| AWS API | All AWS CLI commands | AWS credentials |

---

### 1. GitHub MCP

**When to invoke:**
- Searching code patterns across repos
- Creating/reviewing pull requests
- Checking CI/CD status
- Managing issues

**Common operations:**
```
# Search for error handling patterns
mcp__github__search_code: "try.*except.*logging" language:python

# Get PR details
mcp__github__get_pull_request: owner=fluence-energy repo=gsdl pr_number=123

# List open issues
mcp__github__list_issues: owner=fluence-energy repo=gsdl state=open
```

**Best practices:**
- Use `gh` CLI via Bash for complex operations
- Search code before implementing (avoid duplication)
- Link PRs to Jira tickets in description

---

### 2. Atlassian MCP (Jira + Confluence)

**When to invoke:**
- Looking up ticket requirements (GSDE, GSDEA, SORT)
- Reading runbooks in Confluence
- Updating ticket status

**Jira JQL Examples:**
```jql
# My open tickets
project IN (GSDE, GSDEA, SORT) AND assignee = currentUser() AND status != Done

# Tickets touching Glue jobs
project = GSDE AND text ~ "Glue" AND status = "In Progress"

# Recent bugs
project = GSDE AND issuetype = Bug AND created >= -7d
```

**Confluence searches:**
```
# Find runbook
mcp__atlassian__searchConfluenceUsingCql: cql='title ~ "runbook" AND space = GSDE'

# Get specific page
mcp__atlassian__getConfluencePage: pageId=12345 contentFormat=markdown
```

**Best practices:**
- Always link commits/PRs to Jira tickets
- Update ticket status when starting work
- Document production testing results in ticket comments

---

### 3. AWS API MCP

**When to invoke:**
- Checking job/pipeline status
- Querying S3 data lake structure
- Validating IAM permissions
- Reading CloudWatch logs

**Safe read-only queries:**
```bash
# S3 data lake structure
aws s3 ls s3://fluenceenergy-ops-data-lakehouse/das_catalog/ --recursive --page-size 100

# Glue job status
aws glue get-job-runs --job-name <JOB_NAME> --max-results 5

# Step Function executions
aws stepfunctions list-executions \
  --state-machine-arn arn:aws:states:us-east-1:<ACCOUNT>:stateMachine:<SM_NAME> \
  --max-results 10

# RDS instance status
aws rds describe-db-instances --db-instance-identifier fe-gsdl-poc-database

# CloudWatch recent errors
aws logs filter-log-events --log-group-name /aws/glue/jobs/<JOB> \
  --filter-pattern "ERROR" --limit 20

# IAM policy simulation (always do before changes)
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::<ACCOUNT>:role/<ROLE> \
  --action-names s3:GetObject
```

**NEVER execute via MCP without approval:**
- `aws s3 rm` (data deletion)
- `aws glue delete-*` (infrastructure)
- `aws iam put-*` (permissions)
- `aws rds delete-*` (database)

---

## MCP Troubleshooting

### Authentication Issues
```bash
# Reset GitHub MCP auth
/mcpm-auth-reset github

# Check MCP server status
/mcpm-doctor

# Verify AWS credentials
aws sts get-caller-identity
```

### Common Errors
| Error | Cause | Fix |
|-------|-------|-----|
| "Token expired" | OAuth token timeout | Re-authenticate via browser |
| "Access denied" | Missing permissions | Check IAM role/policy |
| "Rate limited" | Too many API calls | Wait 60s, batch requests |
ENDSKILL

write_file "mcp/skill-mcp-tools.md" "$SKILL_MCP"

###############################################################################
# ┌─────────────────────────────────────────────────────────────────────────┐ #
# │  production/skill-incident-response.md  —  Incident Response           │ #
# └─────────────────────────────────────────────────────────────────────────┘ #
###############################################################################
header "production/ — Incident Response"

read -r -d '' SKILL_INCIDENT << 'ENDSKILL' || true
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
ENDSKILL

write_file "production/skill-incident-response.md" "$SKILL_INCIDENT"

###############################################################################
# ┌─────────────────────────────────────────────────────────────────────────┐ #
# │  data/skill-data-validation.md  —  Data Lakehouse Validation           │ #
# └─────────────────────────────────────────────────────────────────────────┘ #
###############################################################################
header "data/ — Data Validation"

read -r -d '' SKILL_DATA << 'ENDSKILL' || true
# Skill: Data Validation (DATA-VAL)

## Role
You are a Data Quality Engineer for the GSDE&G team. Ensure data integrity
in the `fluenceenergy-ops-data-lakehouse` S3 data lake (275 TB, 23M+ points).

## Critical: Cost Control

**ALWAYS check query cost before running:**
```sql
EXPLAIN SELECT ...;
-- Look for "Data scanned" estimate
-- Rule of thumb: $5 per TB scanned
```

**ALWAYS use partition filters:**
```sql
-- GOOD: Partition-pruned (scans ~MB)
SELECT * FROM ops_datalake.das_datasources
WHERE das_date = DATE '2024-06-01' AND das_server = '<SITE>'
LIMIT 100;

-- BAD: Full scan (scans 275 TB = ~$1,375!)
SELECT * FROM ops_datalake.das_datasources LIMIT 100;
```

---

## Validation Layers

### 1. Schema Validation

```sql
-- Check current schema
DESCRIBE ops_datalake.das_datasources;

-- Detect schema drift (compare against expected)
WITH expected_cols AS (
  SELECT column_name, data_type FROM (VALUES
    ('das_date', 'date'),
    ('das_server', 'varchar'),
    ('das_key', 'varchar'),
    ('value', 'double')
  ) AS t(column_name, data_type)
)
SELECT
  e.column_name,
  e.data_type as expected,
  c.data_type as actual,
  CASE WHEN c.data_type IS NULL THEN 'MISSING'
       WHEN c.data_type != e.data_type THEN 'TYPE_MISMATCH'
       ELSE 'OK' END as status
FROM expected_cols e
LEFT JOIN information_schema.columns c
  ON c.table_name = 'das_datasources' AND c.column_name = e.column_name;
```

### 2. Partition Coverage

```sql
-- Check for date gaps in last 30 days
WITH date_series AS (
  SELECT sequence(
    DATE '2024-06-01',
    CURRENT_DATE,
    INTERVAL '1' DAY
  ) as dates
),
flattened AS (
  SELECT d as expected_date FROM date_series CROSS JOIN UNNEST(dates) AS t(d)
),
actual AS (
  SELECT DISTINCT das_date
  FROM ops_datalake.das_datasources
  WHERE das_date >= DATE '2024-06-01'
    AND das_server = '<SITE>'
)
SELECT expected_date as missing_date
FROM flattened f
LEFT JOIN actual a ON f.expected_date = a.das_date
WHERE a.das_date IS NULL
ORDER BY expected_date;
```

### 3. Data Quality Checks

```sql
-- Null value analysis (partition-safe)
SELECT
  das_date,
  das_server,
  COUNT(*) as total_rows,
  SUM(CASE WHEN value IS NULL THEN 1 ELSE 0 END) as null_count,
  ROUND(100.0 * SUM(CASE WHEN value IS NULL THEN 1 ELSE 0 END) / COUNT(*), 2) as null_pct
FROM ops_datalake.das_datasources
WHERE das_date = DATE '2024-06-01'
  AND das_server = '<SITE>'
GROUP BY das_date, das_server
HAVING SUM(CASE WHEN value IS NULL THEN 1 ELSE 0 END) > 0;

-- Duplicate detection
SELECT das_date, das_server, das_key, COUNT(*) as dup_count
FROM ops_datalake.das_datasources
WHERE das_date = DATE '2024-06-01'
  AND das_server = '<SITE>'
GROUP BY das_date, das_server, das_key
HAVING COUNT(*) > 1
LIMIT 100;

-- Outlier detection (values outside expected range)
SELECT das_date, das_server, das_key, value
FROM ops_datalake.das_datasources
WHERE das_date = DATE '2024-06-01'
  AND das_server = '<SITE>'
  AND (value < 0 OR value > 1000000)  -- adjust thresholds
LIMIT 100;
```

### 4. Cross-Site Comparison

```sql
-- Compare record counts across sites for same date
SELECT
  das_server,
  COUNT(*) as record_count,
  COUNT(DISTINCT das_key) as unique_keys
FROM ops_datalake.das_datasources
WHERE das_date = DATE '2024-06-01'
GROUP BY das_server
ORDER BY record_count DESC
LIMIT 50;
```

---

## Test Data Validation Pattern

When validating after Glue job or pipeline changes:

```sql
-- 1. Create test output table
CREATE TABLE test_scratch.validation_<JIRA>
WITH (format='PARQUET',
      external_location='s3://fluenceenergy-ops-data-lakehouse/das_catalog/_test/validation/<JIRA>/')
AS SELECT * FROM ops_datalake.das_datasources
WHERE das_date = DATE '2024-06-01' AND das_server = 'TEST_SITE'
LIMIT 1000;

-- 2. Run validation queries against test table
SELECT COUNT(*), COUNT(DISTINCT das_key), SUM(CASE WHEN value IS NULL THEN 1 ELSE 0 END)
FROM test_scratch.validation_<JIRA>;

-- 3. Cleanup (MANDATORY)
DROP TABLE IF EXISTS test_scratch.validation_<JIRA>;
```

```bash
# Also cleanup S3
aws s3 rm s3://fluenceenergy-ops-data-lakehouse/das_catalog/_test/validation/<JIRA>/ --recursive
```
ENDSKILL

write_file "data/skill-data-validation.md" "$SKILL_DATA"

# =============================================================================
#  SUMMARY
# =============================================================================
echo ""

if $DRY_RUN; then
  warn "Dry run complete — no files were written."
  echo ""
  exit 0
fi

success "All 3 additional skills deployed successfully."
echo ""
info "Directory tree:"
echo ""
if command -v tree &>/dev/null; then
  tree "$SKILLS_ROOT"
else
  # Portable fallback
  echo "  $SKILLS_ROOT/"
  echo "  ├── mcp/"
  echo "  │   └── skill-mcp-tools.md          ← MCP server integration guide"
  echo "  ├── production/"
  echo "  │   └── skill-incident-response.md  ← Rollback & recovery procedures"
  echo "  └── data/"
  echo "      └── skill-data-validation.md    ← Athena query patterns & cost control"
fi
echo ""
info "Next steps:"
echo "  1.  Review the skills:"
echo "        less $SKILLS_ROOT/mcp/skill-mcp-tools.md"
echo "        less $SKILLS_ROOT/production/skill-incident-response.md"
echo "        less $SKILLS_ROOT/data/skill-data-validation.md"
echo ""
echo "  2.  Use in Claude Code:"
echo "        /read skills/mcp/skill-mcp-tools.md"
echo "        /read skills/production/skill-incident-response.md"
echo "        /read skills/data/skill-data-validation.md"
echo ""
