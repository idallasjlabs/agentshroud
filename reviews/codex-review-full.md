OpenAI Codex v0.101.0 (research preview)
--------
workdir: /home/agentshroud-bot/Development/oneclaw
model: o4-mini
provider: openai
approval: never
sandbox: workspace-write [workdir, /tmp, $TMPDIR]
reasoning effort: none
reasoning summaries: auto
session id: 019c697e-820e-7e03-bcf9-8ee9890a5682
--------
user
You are reviewing AgentShroud infra fixes. For each finding: [SEVERITY] file - Description. Severities: CRITICAL, HIGH, MEDIUM, LOW, INFO.

Diff:
diff --git a/.claude/scripts/claude-hooks/run_targeted_tests.sh b/.claude/scripts/claude-hooks/run_targeted_tests.sh
index 1fdde65..bc24cd3 100755
--- a/.claude/scripts/claude-hooks/run_targeted_tests.sh
+++ b/.claude/scripts/claude-hooks/run_targeted_tests.sh
@@ -1,30 +1,29 @@
 #!/usr/bin/env bash
 set -euo pipefail
 
-# Detect changed Python files
 changed_py="$(git diff --name-only HEAD 2>/dev/null | grep -E '\.py$' || true)"
 
 if [[ -z "$changed_py" ]]; then
   exit 0
 fi
 
-# Run targeted tests for changed Python files
 if command -v pytest >/dev/null 2>&1; then
   echo "🧪 Running targeted tests for changed files..."
-  # Build test file list from changed Python files
   test_files=""
   for pyfile in $changed_py; do
-    # Convert module path to test path (e.g., src/module.py -> tests/test_module.py)
-    test_file="tests/test_$(basename "$pyfile")"
-    if [ -f "$test_file" ]; then
-      test_files="$test_files $test_file"
-    fi
+    # Check multiple test path patterns
+    base="$(basename "$pyfile")"
+    for test_dir in tests gateway/tests; do
+      test_file="$test_dir/test_$base"
+      if [ -f "$test_file" ]; then
+        test_files="$test_files $test_file"
+      fi
+    done
   done
 
   if [ -n "$test_files" ]; then
     pytest -q $test_files || true
   else
-    # Fallback: run all quick tests if no specific test files found
     pytest -q -m "not slow" || true
   fi
 fi
diff --git a/.claude/scripts/claude-hooks/warn_dangerous_bash.sh b/.claude/scripts/claude-hooks/warn_dangerous_bash.sh
index 399b206..7e3c472 100755
--- a/.claude/scripts/claude-hooks/warn_dangerous_bash.sh
+++ b/.claude/scripts/claude-hooks/warn_dangerous_bash.sh
@@ -3,16 +3,20 @@ set -euo pipefail
 
 cmd="${CLAUDE_TOOL_INPUT:-}"
 
-# Patterns we want to WARN about (not block)
 dangerous_patterns=(
   "rm -rf /"
   "rm -rf ~"
-  "rm -rf \\*"
-  "curl .*\\|.*sh"
-  "wget .*\\|.*sh"
+  "rm -rf \*"
+  "curl .*\|.*sh"
+  "wget .*\|.*sh"
   "chmod -R 777"
   "dd if="
-  ":(){ :|:& };:"   # fork bomb
+  ":(){ :|:& };:"
+  "eval \"\$("
+  "sudo rm"
+  "mkfs"
+  "> /dev/sd"
+  "> /dev/nvme"
 )
 
 for pattern in "${dangerous_patterns[@]}"; do
diff --git a/.claude/scripts/deploy-claude-skills.sh b/.claude/scripts/deploy-claude-skills.sh
index 6e4ba4f..f792827 100755
--- a/.claude/scripts/deploy-claude-skills.sh
+++ b/.claude/scripts/deploy-claude-skills.sh
@@ -2,28 +2,10 @@
 # =============================================================================
 # deploy-claude-skills.sh
 #
-# Deploys Claude Code skills for the GSDE&G Development Team.
-# Enforces: Test-Driven Development | GitHub Workflow | Production Safety
-#
-# Intended location:
-#   ~/Development/LLM_Settings/llm_settings/scripts/deploy-claude-skills.sh
-#
-# Deploys to:
-#   ../skills/   (relative to this script)
-#
-# Hierarchy:
-#   skills/
-#   ├── qa/    SKILL.md   — QA Testing + Production Test Runbooks
-#   ├── cr/    SKILL.md   — Code Review + Production Safety Checks
-#   ├── pr/    SKILL.md   — Pull Request Generator
-#   ├── tdd/   SKILL.md   — Test-Driven Development Coach
-#   ├── gg/    SKILL.md   — Git Guard (Workflow Enforcer)
-#   ├── cicd/  SKILL.md   — CI/CD Pipeline Advisor
-#   ├── ps/    SKILL.md   — Production Safety Checklist
-#   └── mc/    SKILL.md   — Master Checklist (Combined Reference)
+# Deploys Claude Code skills for the AgentShroud project.
+# Enforces: Test-Driven Development | Security Review | Production Safety
 #
 # Usage:
-#   chmod +x deploy-claude-skills.sh
 #   ./deploy-claude-skills.sh            # deploy
 #   ./deploy-claude-skills.sh --dry-run  # preview only
 #   ./deploy-claude-skills.sh --clean    # remove and redeploy
@@ -31,1117 +13,114 @@
 
 set -euo pipefail
 
-# ── Resolve paths relative to THIS script ────────────────────────────────────
 SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
 SKILLS_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)/skills"
-TIMESTAMP="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
 DRY_RUN=false
 CLEAN=false
 
-# ── Parse arguments ──────────────────────────────────────────────────────────
 while [[ $# -gt 0 ]]; do
   case "$1" in
     --dry-run) DRY_RUN=true; shift ;;
-    --clean)   CLEAN=true;   shift ;;
-    -h|--help)
-      echo "Usage: $0 [--dry-run] [--clean]"
-      echo ""
-      echo "  --dry-run  Preview what would be created (no writes)"
-      echo "  --clean    Remove existing skills directory and redeploy"
-      echo ""
-      echo "  Script:  $0"
-      echo "  Target:  $(cd "$SCRIPT_DIR/.." && pwd)/skills/"
-      exit 0
-      ;;
-    *) echo "Error: Unknown option '$1'"; exit 1 ;;
+    --clean)   CLEAN=true; shift ;;
+    *) echo "Unknown option: $1"; exit 1 ;;
   esac
 done
 
-# ── Helpers ──────────────────────────────────────────────────────────────────
-info()    { printf "\033[1;34m[INFO]\033[0m  %s\n" "$1"; }
-success() { printf "\033[1;32m  OK  \033[0m  %s\n" "$1"; }
-warn()    { printf "\033[1;33m[WARN]\033[0m  %s\n" "$1"; }
-
 write_skill() {
-  # $1 = directory name (e.g. "qa")   $2 = content
-  local dir_name="$1"
-  local fpath="$SKILLS_ROOT/$dir_name/SKILL.md"
-  if $DRY_RUN; then
-    info "[DRY RUN] Would create: $fpath"
-    return
-  fi
-  mkdir -p "$SKILLS_ROOT/$dir_name"
-  printf '%s\n' "$2" > "$fpath"
-  success "$dir_name/SKILL.md"
+  local dir="$1" content="$2"
+  local fpath="$SKILLS_ROOT/$dir/SKILL.md"
+  if $DRY_RUN; then echo "[DRY RUN] $fpath"; return; fi
+  mkdir -p "$SKILLS_ROOT/$dir"
+  printf '%s\n' "$content" > "$fpath"
+  echo "  ✓ $dir/SKILL.md"
 }
 
-# ── Clean if requested ───────────────────────────────────────────────────────
 if $CLEAN && ! $DRY_RUN; then
-  if [[ -d "$SKILLS_ROOT" ]]; then
-    warn "Removing existing: $SKILLS_ROOT"
-    rm -rf "$SKILLS_ROOT"
-  fi
+  [ -d "$SKILLS_ROOT" ] && rm -rf "$SKILLS_ROOT"
 fi
 
-# =============================================================================
-#  BANNER
-# =============================================================================
-echo ""
-echo "  ╔══════════════════════════════════════════════════════════════╗"
-echo "  ║        GSDE&G  Claude Code Skills — Deployer               ║"
-echo "  ╚══════════════════════════════════════════════════════════════╝"
-info "Script : $SCRIPT_DIR/$(basename "$0")"
-info "Target : $SKILLS_ROOT/"
-info "Time   : $TIMESTAMP"
-$DRY_RUN && warn "Mode   : DRY RUN — no files will be written"
-$CLEAN   && warn "Mode   : CLEAN — existing skills removed first"
-echo ""
-
-# =============================================================================
-#                         S K I L L   C O N T E N T
-# =============================================================================
-
-###############################################################################
-#  qa/SKILL.md  —  Quality Assurance + Production Testing Runbooks
-###############################################################################
-
-read -r -d '' SKILL_QA << 'ENDSKILL' || true
-# Skill: Quality Assurance (QA)
-
-## Role
-You are an expert QA Engineer specializing in comprehensive verification of
-software changes for the GSDE&G team at Fluence Energy.
-
-## Objective
-Analyze the provided code changes or feature requirements and develop a
-multi-layered testing strategy to ensure zero regressions and high reliability.
-
-## Testing Hierarchy
-For every task, you must address:
-
-1. **Unit Testing:** Logic paths, edge cases, and boundary conditions for
-   individual functions.
-2. **Integration Testing:** Touchpoints between modules, API contracts, and
-   database interactions.
-3. **System Testing:** End-to-end user flow — does the feature work in the
-   context of the whole application?
-4. **Regression Testing:** Existing high-risk areas that must be smoke-tested
-   to ensure no side effects.
-
-## Output Format
-- **Test Strategy Summary**
-- **Test Cases Table:** (ID | Layer | Scenario | Expected Result)
-- **Edge Cases:** "What-if" scenarios (null values, timeouts, empty partitions, etc.)
-- **Environment Requirements:** Specific data, mocks, or flags needed.
-
----
-
-## Production Testing Procedures  ⚠️  NO SEPARATE DEV ENVIRONMENT
-
-We do **not** have a dedicated development or staging environment.  Many changes
-must be validated directly in production.  Follow these procedures **exactly**.
-
-### General Rules
-1. **Never test during peak hours.**  Schedule outside business hours / weekends.
-2. **Always have a rollback plan written BEFORE you start.**
-3. **Use test-flagged data** — never modify real operational data without a backup.
-4. **Pair up** — one person executes, one monitors.
-5. **Log every step** with timestamps; paste the log into the PR / Jira ticket.
-
----
-
-### A. AWS Glue Jobs
-> Context: Normalize parquet data in `s3://fluenceenergy-ops-data-lakehouse/das_catalog/`.
-
-1. **Copy a small sample to a `_test/` prefix** (never run against the full dataset):
-   ```bash
-   aws s3 cp \
-     s3://fluenceenergy-ops-data-lakehouse/das_catalog/das_exports_latest/das_datasources/SITE_NAME/ \
-     s3://fluenceenergy-ops-data-lakehouse/das_catalog/_test/das_datasources/SITE_NAME/ \
-     --recursive --include "*.parquet" --page-size 10
-   ```
-2. **Override job parameters** in the Glue console (do NOT edit the production job):
-   ```
-   --input_prefix  = das_catalog/_test/das_datasources/
-   --output_prefix = das_catalog/_test/das_exports_normalized/das_datasources/
-   ```
-3. **Run the job manually** — never on the production schedule.
-4. **Validate output:**
-   ```bash
-   aws s3 ls s3://fluenceenergy-ops-data-lakehouse/das_catalog/_test/das_exports_normalized/ \
-     --recursive --human-readable
-   ```
-5. **Clean up:**
-   ```bash
-   aws s3 rm s3://fluenceenergy-ops-data-lakehouse/das_catalog/_test/ --recursive
-   ```
-
----
-
-### B. AWS Step Functions
-> Context: State machines prefixed `gs-dataeng-*`, `gsdl-*`, `ops-datalake-*`.
-
-1. **Start execution with a test input:**
-   ```bash
-   aws stepfunctions start-execution \
-     --state-machine-arn arn:aws:states:us-east-1:ACCOUNT:stateMachine:SM_NAME \
-     --name "TEST-$(date +%Y%m%d-%H%M%S)" \
-     --input '{"test_mode":true,"site":"TEST_SITE","date_range":"2024-01-01/2024-01-02"}'
-   ```
-2. **Design state machines to honour `test_mode: true`:**
-   - Skip SNS notifications.
-   - Write to `_test/` S3 prefixes.
-   - Process only 1 day of data.
-3. **Monitor** in the Step Functions console; watch for failed states.
-4. **Check CloudWatch:**
-   ```bash
-   aws logs filter-log-events \
-     --log-group-name /aws/stepfunctions/SM_NAME \
-     --filter-pattern "TEST-" --limit 50
-   ```
-
----
-
-### C. AWS Athena
-> Context: 275 TB data lakehouse, 23 M+ data points.
-
-1. **Always use `LIMIT`** — unbounded queries can cost hundreds of dollars:
-   ```sql
-   SELECT * FROM ops_datalake.das_datasources
-   WHERE das_date = DATE '2024-06-01' AND das_server = 'SITE'
-   LIMIT 100;
-   ```
-2. **Use CTAS for test outputs:**
-   ```sql
-   CREATE TABLE test_scratch.my_test
-   WITH (format='PARQUET',
-         external_location='s3://fluenceenergy-ops-data-lakehouse/das_catalog/_test/athena/')
-   AS SELECT … WHERE das_date BETWEEN … AND das_server = '…';
-   ```
-3. **Check cost first:**
-   ```sql
-   EXPLAIN SELECT …;
-   ```
-4. **Clean up:**
-   ```sql
-   DROP TABLE IF EXISTS test_scratch.my_test;
-   ```
-   ```bash
-   aws s3 rm s3://fluenceenergy-ops-data-lakehouse/das_catalog/_test/athena/ --recursive
-   ```
-
----
-
-### D. PostgreSQL — RDS (`fe-gsdl-poc-database`)
-
-1. **Wrap everything in a transaction + SAVEPOINT:**
-   ```sql
-   BEGIN;
-   SAVEPOINT before_test;
-   -- your operations here --
-   INSERT INTO tbl (col1, col2, _test_flag) VALUES ('x', 1, TRUE);
-   SELECT * FROM tbl WHERE _test_flag = TRUE;    -- validate
-   ROLLBACK TO SAVEPOINT before_test;             -- always rollback
-   ROLLBACK;
-   ```
-2. **Add a `_test_flag` column** to tables that need production testing:
-   ```sql
-   ALTER TABLE target ADD COLUMN IF NOT EXISTS _test_flag BOOLEAN DEFAULT FALSE;
-   ```
-3. **For DDL changes** — snapshot first:
-   ```bash
-   aws rds create-db-snapshot \
-     --db-instance-identifier fe-gsdl-poc-database \
-     --db-snapshot-identifier pre-test-$(date +%Y%m%d-%H%M%S)
-   ```
-4. **For large tables (20 GB+, e.g. `errortracker`):**
-   - Create new structure alongside old: `errortracker_v2`.
-   - Migrate a small date range to validate:
-     ```sql
-     INSERT INTO errortracker_v2
-     SELECT * FROM errortracker
-     WHERE das_date >= CURRENT_DATE - INTERVAL '7 days';
-     ```
-   - Swap with `ALTER TABLE … RENAME` only after full validation.
-   - Keep old table 7 days before dropping.
-
----
-
-### E. MySQL — On-Site Zabbix Databases (200+ sites)
-
-1. **Test on ONE low-risk site first.**
-2. **Backup before any change:**
-   ```bash
-   ssh user@SITE_TAILSCALE_IP
-   mysqldump -u root -p zabbix TABLE_NAME \
-     --where="clock > UNIX_TIMESTAMP(NOW() - INTERVAL 1 HOUR)" \
-     > /tmp/TABLE_backup_$(date +%Y%m%d).sql
-   ```
-3. **For schema changes:**
-   - Check Zabbix version compatibility matrix.
-   - Run migration on the single test site.
-   - Validate frontend shows current data.
-   - Wait **24 hours** before rolling to more sites.
-4. **For new items/triggers:**
-   - Put host in **Maintenance Mode** first (with data collection, 4-hr window):
-     ```
-     Configuration → Maintenance → Create
-     - Name: "TEST - <your_name> - <date>"
-     - Period: +4 hours
-     - Hosts: [test host only]
-     - Type: "With data collection"
-     ```
-   - Use **Zabbix trapper** type for safe manual testing:
-     ```
-     Configuration → Hosts → [Host] → Items → Create
-     - Name:    TEST_<description>
-     - Key:     test.<key_name>
-     - Type:    Zabbix trapper
-     - History: 1d
-     ```
-   - Push test values:
-     ```bash
-     zabbix_sender -z ZABBIX_SERVER -s "HOST" -k "test.key_name" -o "42"
-     ```
-   - Verify in Monitoring → Latest Data.
-   - Delete test items after validation.
-5. **For template changes:**
-   - Clone: `Configuration → Templates → Full clone` → name `TEST_<original>`.
-   - Link clone to ONE host, monitor 1 hour.
-   - If good → apply to real template, unlink/delete clone.
-
----
-
-### F. IAM Policies
-
-1. **Simulate first — always:**
-   ```bash
-   aws iam simulate-principal-policy \
-     --policy-source-arn arn:aws:iam::ACCOUNT:role/ROLE \
-     --action-names s3:GetObject glue:StartJobRun \
-     --resource-arns "arn:aws:s3:::fluenceenergy-ops-data-lakehouse/*"
-   ```
-2. **Use a test role** — never touch production roles directly:
-   ```bash
-   aws iam create-role --role-name TEST-role-$(date +%Y%m%d) \
-     --assume-role-policy-document file://trust.json
-   aws iam put-role-policy --role-name TEST-role-$(date +%Y%m%d) \
-     --policy-name test-pol --policy-document file://new-policy.json
-   # … test … then clean up:
-   aws iam delete-role-policy --role-name TEST-role-$(date +%Y%m%d) --policy-name test-pol
-   aws iam delete-role --role-name TEST-role-$(date +%Y%m%d)
-   ```
-3. **For production role changes:** export current policy first:
-   ```bash
-   aws iam get-role-policy --role-name ROLE --policy-name POLICY \
-     > policy_backup_$(date +%Y%m%d).json
-   ```
-
----
-
-### G. Tailscale / Network
-
-1. Test on **your own device** first.
-2. Exit node changes → test 1 site, confirm Zabbix + VPN, wait 1 hour.
-3. ACL changes → `tailscale debug` before and after.
-
----
-
-### H. Service Control for Production Testing
-
-#### H.1 Pause Glue Jobs Before Testing
-```bash
-# 1. List all triggers for the job
-aws glue get-triggers --query "Triggers[?Actions[?JobName=='<JOB_NAME>']].Name"
-
-# 2. Disable the scheduled trigger
-aws glue update-trigger --name <TRIGGER_NAME> --trigger-update State=DISABLED
-
-# 3. Verify no jobs currently running
-aws glue get-job-runs --job-name <JOB_NAME> --max-results 5 \\
-  --query "JobRuns[?JobRunState=='RUNNING']"
-
-# 4. After testing - RE-ENABLE (critical!)
-aws glue update-trigger --name <TRIGGER_NAME> --trigger-update State=ENABLED
-```
-
-#### H.2 Pause Step Functions Before Testing
-```bash
-# 1. Check for active executions
-aws stepfunctions list-executions \\
-  --state-machine-arn arn:aws:states:us-east-1:<ACCOUNT>:stateMachine:<SM_NAME> \\
-  --status-filter RUNNING
-
-# 2. If needed, stop test executions only (NEVER stop production executions)
-aws stepfunctions stop-execution \\
-  --execution-arn arn:aws:states:us-east-1:<ACCOUNT>:execution:<SM_NAME>:TEST-<ID> \\
-  --cause "Stopping for test cleanup"
+echo "Deploying AgentShroud skills to $SKILLS_ROOT/"
 
-# 3. Disable EventBridge rule (if scheduled)
-aws events disable-rule --name <RULE_NAME>
-
-# 4. After testing - RE-ENABLE
-aws events enable-rule --name <RULE_NAME>
-```
-
-#### H.3 Database Tables for Test Data
-
-**Pattern: Add \`_test_flag\` column to tables requiring production testing:**
-
-```sql
--- Step 1: Add test flag column (one-time setup)
-ALTER TABLE <TABLE_NAME> ADD COLUMN IF NOT EXISTS _test_flag BOOLEAN DEFAULT FALSE;
-CREATE INDEX IF NOT EXISTS idx_<TABLE_NAME>_test_flag ON <TABLE_NAME>(_test_flag) WHERE _test_flag = TRUE;
-
--- Step 2: Insert test data with flag
-BEGIN;
-SAVEPOINT test_start;
-INSERT INTO <TABLE_NAME> (..., _test_flag) VALUES (..., TRUE);
-
--- Step 3: Verify test data
-SELECT * FROM <TABLE_NAME> WHERE _test_flag = TRUE;
-
--- Step 4: ALWAYS rollback (never commit test data)
-ROLLBACK TO SAVEPOINT test_start;
-ROLLBACK;
-```
-
-**Known Tables (fe-gsdl-poc-database):**
-| Table | Size | Test Flag Support |
-|-------|------|-------------------|
-| \`errortracker\` | 20+ GB | Recommended - add \`_test_flag\` |
-| \`errortracker_v2\` | Migration | Recommended - add \`_test_flag\` |
-
-**Zabbix MySQL Tables (READ-ONLY in most cases):**
-| Table | Modify? | Safe Alternative |
-|-------|---------|------------------|
-| \`hosts\` | NEVER | Use maintenance mode |
-| \`items\` | Via API | Zabbix trapper items |
-| \`triggers\` | Via API | Clone template first |
-| \`history*\` | NEVER | Read-only queries |
-
-#### H.4 Cleanup Verification Checklist
-```bash
-# S3 test data removed?
-aws s3 ls s3://fluenceenergy-ops-data-lakehouse/das_catalog/_test/ --recursive
-
-# Athena test tables dropped?
-aws athena start-query-execution \\
-  --query-string "SHOW TABLES IN test_scratch" \\
-  --work-group primary
-
-# Database test rows removed?
-psql -h fe-gsdl-poc-database... -c "SELECT COUNT(*) FROM <TABLE> WHERE _test_flag = TRUE"
-
-# Triggers re-enabled?
-aws glue get-trigger --name <TRIGGER_NAME> --query "Trigger.State"
-```
-ENDSKILL
-
-write_skill "qa" "$SKILL_QA"
-
-###############################################################################
-#  cr/SKILL.md  —  Code Review + Production Safety Checks
-###############################################################################
-
-read -r -d '' SKILL_CR << 'ENDSKILL' || true
-# Skill: Code Review (CR)
-
-## Role
-You are a Senior Software Engineer and Security Advocate for the GSDE&G team.
-Provide constructive, high-standard feedback with special attention to production
-safety — we deploy directly to production.
-
-## Review Principles
-1. **Security-Critical Areas:** Authentication, Authorization, Data Validation,
-   Cryptography, API endpoints.  Extra scrutiny on IAM policies, S3 bucket
-   policies, and database credentials.
-2. **The 400-Line Rule:** PR exceeds 400 LoC → flag it, suggest breaking it down.
-3. **Functionality & Performance:** Does it work?  Will it scale?
-   For Athena queries — will this scan the full 275 TB or is it partitioned?
-4. **Readability:** Can a junior developer understand it without a walkthrough?
-5. **Static Analysis:** OWASP Top 10 / CWE Top 25.
-
-## Production-Specific Review Checks
-- [ ] **Test isolation:** `_test/` prefixes, `_test_flag` columns, or `SAVEPOINT`?
-      Tests NEVER touch real production data.
-- [ ] **Rollback path:** Documented undo within 5 minutes?
-- [ ] **Blast radius:** How many sites / pipelines affected?  Incremental rollout?
-- [ ] **Cost guard:** Athena `LIMIT` / partition `WHERE`?  Glue scoped to test prefix?
-- [ ] **Alert suppression:** False Zabbix alerts expected?  Maintenance window doc'd?
-- [ ] **Backup step:** RDS snapshot / mysqldump / IAM export?
-
-## Feedback Guidelines
-- **Be Constructive:** explain *why* a change is requested.
-- **Automate the Boring Stuff:** flag missing tests or linting.
-- **Junior Mentorship:** frame complex logic as learning opportunities.
-
-## Output Format
-- **Review Summary:** Pass / Request Changes / Comment
-- **Production Safety Audit:** blast radius, rollback, data safety
-- **Security Audit:** data handling and risks
-- **Detailed Comments:** line-by-line with "Refactor Suggestion" blocks
-ENDSKILL
-
-write_skill "cr" "$SKILL_CR"
-
-###############################################################################
-#  pr/SKILL.md  —  Pull Request Generator
-###############################################################################
-
-read -r -d '' SKILL_PR << 'ENDSKILL' || true
-# Skill: Pull Request (PR) Generator
-
-## Role
-You are a Technical Writer and DevOps specialist for the GSDE&G team.
-Document code changes for production readiness.
-
-## Objective
-Generate a high-quality PR description.  Since we deploy directly to production,
-every PR must clearly state what could go wrong and how to fix it.
-
-## Content Requirements
-
-### Header
-- **Summary:** concise overview of what changed.
-- **Motivation:** why?  Link to Jira ticket (GSDE / GSDEA / SORT).
-
-### Technical Detail
-- **Key Changes:** bulleted implementation details.
-- **Affected Systems** (check all that apply):
-  - [ ] AWS Glue Jobs — list job names
-  - [ ] AWS Step Functions — list state machine names
-  - [ ] AWS Athena — tables / schemas
-  - [ ] S3 Data Lake — paths under `fluenceenergy-ops-data-lakehouse`
-  - [ ] PostgreSQL RDS — `fe-gsdl-poc-database`
-  - [ ] MySQL on-site Zabbix — which sites?
-  - [ ] Zabbix templates / triggers / items
-  - [ ] IAM policies / roles
-  - [ ] Tailscale / network
-
-### Safety
-- **Security Considerations:** impact on security posture.
-- **Testing Evidence:**
-  - Test prefix / test flag / SAVEPOINT used.
-  - CI output or test log attached.
-  - Confirmation test data cleaned up.
-- **Production Testing Steps:** if required, step-by-step procedure
-  (reference `qa/SKILL.md` § Production Testing Procedures).
-- **Rollback Plan:**
-  - Exact CLI commands or console steps.
-  - Which RDS snapshot / S3 version to restore.
-  - On-call contact.
-  - Expected rollback time (minutes).
-
-## Constraints
-- Professional, succinct tone.
-- Clean GitHub-compatible Markdown.
-ENDSKILL
-
-write_skill "pr" "$SKILL_PR"
-
-###############################################################################
-#  tdd/SKILL.md  —  Test-Driven Development Coach
-###############################################################################
-
-read -r -d '' SKILL_TDD << 'ENDSKILL' || true
+# TDD Skill
+read -r -d '' SKILL_TDD << 'END' || true
 # Skill: Test-Driven Development (TDD)
 
-## Role
-You are a TDD Coach for the GSDE&G team.  You enforce the Red-Green-Refactor
-cycle in every coding task.
-
 ## Core Discipline: Red → Green → Refactor
-
-1. **RED  — Write a failing test first.**
-   Confirm it fails for the *right* reason.
-2. **GREEN — Write the minimum code to pass.**
-   No speculative features.  No premature optimisation.
-3. **REFACTOR — Clean up while tests stay green.**
-   Run the full suite after every refactor step.
+1. **RED** — Write a failing test first. Confirm it fails for the right reason.
+2. **GREEN** — Write the minimum code to pass. No speculative features.
+3. **REFACTOR** — Clean up while tests stay green.
 
 ## Rules
-- **Never skip RED.**  If you wrote implementation first → delete it, write the test.
-- **One behaviour per test.**
-- **Descriptive names:** `test_<unit>_<scenario>_<expected_result>`
-- **Test the interface, not the implementation.**
-- **Coverage is a signal, not a target.**
-
-## Test Structure
-```
-# Arrange — preconditions & inputs
-# Act    — execute the behaviour
-# Assert — verify the outcome
-```
-
-## Anti-Patterns to Flag
-- Tests written AFTER implementation.
-- Mocking the thing you're testing.
-- Testing private methods directly.
-- Brittle tests tied to implementation details.
-
----
-
-## Stack-Specific Testing Patterns
-
-### Python / Boto3 / AWS  →  `moto`
-```python
-import pytest, boto3
-from moto import mock_s3
-
-@mock_s3
-def test_list_parquet_files_returns_only_parquet():
-    # Arrange
-    s3 = boto3.client("s3", region_name="us-east-1")
-    s3.create_bucket(Bucket="fluenceenergy-ops-data-lakehouse")
-    s3.put_object(Bucket="fluenceenergy-ops-data-lakehouse",
-                  Key="das_catalog/site1/data.parquet", Body=b"fake")
-    s3.put_object(Bucket="fluenceenergy-ops-data-lakehouse",
-                  Key="das_catalog/site1/meta.json", Body=b"{}")
-    # Act
-    from our_module import list_parquet_files
-    result = list_parquet_files("das_catalog/site1/")
-    # Assert
-    assert len(result) == 1
-    assert result[0].endswith(".parquet")
-
-@mock_s3
-def test_list_parquet_files_empty_prefix():
-    s3 = boto3.client("s3", region_name="us-east-1")
-    s3.create_bucket(Bucket="fluenceenergy-ops-data-lakehouse")
-    from our_module import list_parquet_files
-    assert list_parquet_files("nonexistent/") == []
-```
-
-### PostgreSQL  →  `SAVEPOINT` + `ROLLBACK`
-```python
-import pytest, psycopg2
-
-@pytest.fixture
-def db_conn():
-    conn = psycopg2.connect(dsn="your_dsn")
-    conn.autocommit = False
-    yield conn
-    conn.rollback()          # ALWAYS rollback
-    conn.close()
-
-def test_migration_adds_column(db_conn):
-    cur = db_conn.cursor()
-    cur.execute("SAVEPOINT test_mig;")
-    cur.execute("ALTER TABLE target ADD COLUMN new_col VARCHAR(100);")
-    cur.execute("""SELECT column_name FROM information_schema.columns
-                   WHERE table_name='target' AND column_name='new_col';""")
-    assert cur.fetchone() is not None
-    cur.execute("ROLLBACK TO SAVEPOINT test_mig;")
-```
-
-### Zabbix API  →  `unittest.mock`
-```python
-from unittest.mock import patch
-
-def test_create_maintenance_window():
-    with patch("pyzabbix.ZabbixAPI") as MockAPI:
-        zapi = MockAPI.return_value
-        zapi.maintenance.create.return_value = {"maintenanceids": ["123"]}
-        from our_module import create_maintenance
-        result = create_maintenance(host_id="99", duration_hours=4)
-        assert result == "123"
-        assert zapi.maintenance.create.call_args[1]["name"].startswith("TEST -")
-```
-
-### Glue Job Logic  →  test transformations outside Spark
-```python
-import pandas as pd
-
-def test_normalize_fills_missing_columns():
-    raw = pd.DataFrame({"name": ["site1"], "host": ["10.0.0.1"]})
-    expected = ["name", "host", "port", "enabled"]
-    from our_module import normalize_schema
-    result = normalize_schema(raw, expected)
-    assert list(result.columns) == expected
-    assert result["port"].iloc[0] is None
-```
-
-### Step Function Input Validation
-```python
-import pytest
-
-def test_sf_input_rejects_missing_site():
-    from our_module import validate_sf_input
-    with pytest.raises(ValueError, match="site is required"):
-        validate_sf_input({"date_range": "2024-01-01/2024-01-02"})
-
-def test_sf_input_routes_test_mode_to_test_prefix():
-    from our_module import validate_sf_input
-    out = validate_sf_input({"site": "X", "test_mode": True})
-    assert out["output_prefix"].startswith("_test/")
-```
-ENDSKILL
-
+- Never skip RED. If you wrote implementation first → delete it, write the test.
+- One behaviour per test.
+- Descriptive names: `test_<unit>_<scenario>_<expected_result>`
+- Test the interface, not the implementation.
+- Coverage target: ≥ 80% on new code, ≥ 90% on security modules.
+END
 write_skill "tdd" "$SKILL_TDD"
 
-###############################################################################
-#  gg/SKILL.md  —  Git Guard (Workflow Enforcer)
-###############################################################################
-
-read -r -d '' SKILL_GG << 'ENDSKILL' || true
-# Skill: Git Workflow Guardian (GIT-GUARD)
-
-## Role
-You are a DevOps Gatekeeper for the GSDE&G team.  No change reaches production
-without passing through the approved GitHub workflow.  This is critical — we
-deploy directly to production.
-
-## Protected Branch
-- **`main`** — NEVER commit directly.  All changes arrive via approved PRs.
-- **Feature branches** — all work happens here.
-
-## Branch Naming
-| Prefix      | Use Case                     | Example                                  |
-|-------------|------------------------------|------------------------------------------|
-| `feat/`     | New feature                  | `feat/GSDE-42-athena-partition-pruning`  |
-| `fix/`      | Bug fix                      | `fix/SORT-101-zabbix-mysql-timeout`      |
-| `hotfix/`   | Critical production fix      | `hotfix/GSDE-88-glue-schema-mismatch`   |
-| `chore/`    | Maintenance / deps / config  | `chore/GSDEA-15-bump-boto3`             |
-| `refactor/` | Restructure, no Δ behaviour  | `refactor/GSDE-60-normalize-cleanup`    |
-| `test/`     | Tests only                   | `test/SORT-45-zabbix-api-tests`         |
-| `docs/`     | Documentation only           | `docs/GSDEA-22-runbook-update`          |
-
-## Mandatory Workflow  (10 steps)
-1. **Branch** from `main`: `<type>/<ticket>-<desc>`
-2. **Write tests first** → invoke `tdd/SKILL.md`
-3. **Implement** — commit with Conventional Commits
-4. **Run locally:**
-   ```bash
-   pytest tests/ -v --tb=short
-   ruff check . && ruff format --check .
-   mypy . --ignore-missing-imports
-   ```
-5. **Push** feature branch → open Pull Request
-6. **Code review** → invoke `cr/SKILL.md`
-7. **PR description** → invoke `pr/SKILL.md`
-8. **CI must pass** (all quality gates)
-9. **≥ 1 approval** from sub-team lead
-   - GSDE  → KP or Revathi
-   - GSDEA → Tala
-   - SORT  → Keith
-10. **Squash-merge** to `main`
-
-## Commit Messages  (Conventional Commits)
-```
-<type>(<scope>): <subject>
-```
-**Scopes:** `data-lake` · `zabbix` · `db` · `iam` · `pipeline` · `infra` · `docs`
-
-Examples:
-```
-feat(data-lake): add daily partition pruning for Athena
-fix(zabbix): resolve MySQL connection pool exhaustion
-chore(deps): bump boto3 to 1.35.x
-refactor(pipeline): consolidate normalize jobs into single SF
-```
-
-## REFUSE These
-- Direct pushes to `main`.
-- Commits without tests (except `docs/` or `chore/`).
-- Force-pushes rewriting shared history.
-- Merges that skip CI.
-- IAM changes without `simulate-principal-policy` evidence.
-- DB schema changes without an RDS snapshot step.
-
-## Emergency Hotfix
-1. `hotfix/<ticket>-<desc>` from `main`
-2. RDS snapshot / mysqldump / policy backup
-3. Regression test → fix → verify locally
-4. PR → expedited review (Isaiah or sub-team lead)
-5. Merge → monitor 30 min (Zabbix + CloudWatch)
-ENDSKILL
-
-write_skill "gg" "$SKILL_GG"
-
-###############################################################################
-#  cicd/SKILL.md  —  CI/CD Pipeline Advisor
-###############################################################################
-
-read -r -d '' SKILL_CICD << 'ENDSKILL' || true
-# Skill: CI/CD Pipeline Advisor (CICD)
-
-## Role
-You are a CI/CD Architect for the GSDE&G team.  Since we deploy directly to
-production, the CI pipeline IS our safety net.
-
-## Quality Gates  (execution order)
-1. **Lint & Format** — `ruff check .` + `ruff format --check .`
-2. **Type Check** — `mypy . --ignore-missing-imports`
-3. **Unit Tests** — `pytest tests/unit/ -v`  (moto for AWS)
-4. **Integration Tests** — `pytest tests/integration/ -v`
-5. **Security Scan** — `bandit -r src/` + `pip-audit`
-6. **Dry-Run Validation** — Glue compile, IAM simulate, SQL `EXPLAIN`
-7. **Manual Approval** — required for prod infra / DB / IAM
-8. **Deploy to Production** — rollback on smoke-test failure
-
-## GitHub Actions Best Practices
-- Pin actions to **SHA** (supply-chain security).
-- `concurrency` groups to cancel redundant runs.
-- Cache pip deps with `actions/cache`.
-- **OIDC** for AWS creds — no long-lived keys.
-- Separate workflows: `ci.yml` (on PR), `deploy.yml` (on merge to main).
-- `timeout-minutes` on every job.
-- `environment: production` with required reviewers for deploy jobs.
-
-## Deployment Matrix  (Direct to Prod)
-| Change            | CI Gate              | Deploy Method                           | Rollback                   |
-|-------------------|----------------------|-----------------------------------------|----------------------------|
-| Python script     | Full test suite      | Push to S3 / update Lambda              | Revert S3 object version   |
-| Glue job          | Unit tests + dry-run | `aws glue update-job`                   | Previous version in Git    |
-| Step Function     | Tests + ASL lint     | `aws stepfunctions update-state-machine`| Previous def in Git        |
-| SQL migration     | Syntax + `EXPLAIN`   | Manual apply post-approval              | RDS snapshot restore       |
-| Zabbix template   | API validation tests | Manual import post-approval             | Previous export in Git     |
-| IAM policy        | `simulate-principal` | Manual apply post-approval              | Previous JSON in Git       |
-
-## Review Flags  (block the merge)
-- Deploys without running tests.
-- Missing security scan.
-- Secrets not in GitHub Secrets.
-- AWS creds not OIDC.
-- No branch protection configured.
-ENDSKILL
-
-write_skill "cicd" "$SKILL_CICD"
-
-###############################################################################
-#  ps/SKILL.md  —  Production Safety Checklist
-###############################################################################
-
-read -r -d '' SKILL_PS << 'ENDSKILL' || true
-# Skill: Production Safety Checklist (PROD-SAFETY)
+# Security Review Skill
+read -r -d '' SKILL_SEC << 'END' || true
+# Skill: Security Review (SEC)
 
 ## Role
-You are a Release Engineer for the GSDE&G team.  Every production change must
-be safe, reversible, and auditable.
-
-## Invoke Before
-- ANY merge to `main`
-- ANY AWS infrastructure change
-- ANY database migration (PostgreSQL RDS or on-site MySQL)
-- ANY Zabbix / Tailscale / IAM configuration change
-- ANY Glue job or Step Function modification
-
----
-
-## Pre-Deployment Checklist
-
-### 1. Change Documentation
-- [ ] Tracked in Jira (GSDE / GSDEA / SORT project).
-- [ ] PR has motivation, changes, and risk assessment.
-- [ ] Sub-team lead approved (KP/Revathi · Tala · Keith).
-
-### 2. Testing Evidence
-- [ ] `pytest tests/ -v` passes locally.
-- [ ] AWS mocked with `moto`.
-- [ ] If production testing was required:
-  - [ ] `_test/` S3 prefix, `_test_flag` column, or `SAVEPOINT` used.
-  - [ ] Test data cleaned up.
-  - [ ] Timestamped test log attached to PR.
-
-### 3. Backups & Rollback
-- [ ] **PostgreSQL:**
-  ```bash
-  aws rds create-db-snapshot \
-    --db-instance-identifier fe-gsdl-poc-database \
-    --db-snapshot-identifier pre-deploy-$(date +%Y%m%d-%H%M%S)
-  ```
-- [ ] **MySQL (on-site):** `mysqldump` of affected tables.
-- [ ] **S3:** versioning enabled on `fluenceenergy-ops-data-lakehouse`.
-- [ ] **Glue / Step Functions:** previous definition in Git history.
-- [ ] **IAM:** current policy exported to JSON.
-- [ ] **Zabbix:** template exported before changes.
-- [ ] Rollback procedure documented with **exact commands**.
-- [ ] Estimated rollback time: ______ minutes.
-
-### 4. Blast Radius
-- [ ] BESS sites affected: ______ / 200+
-- [ ] Incremental rollout possible?  (1 site → 10 → all)
-- [ ] Breaking for downstream consumers (Grafana, dashboards, reports)?
-- [ ] Will Zabbix alerts fire?
-  - [ ] Maintenance window created for affected hosts.
-  - [ ] On-call engineer notified.
-
-### 5. Observability
-- [ ] Logging added (`logging.info` / `logging.error`).
-- [ ] CloudWatch log groups exist for new Glue / SF jobs.
-- [ ] Zabbix items / triggers updated if infra changed.
-- [ ] Athena queries validated with `EXPLAIN`.
-
-### 6. Security
-- [ ] No secrets in code — use AWS Secrets Manager.
-- [ ] IAM least-privilege.
-- [ ] `pip-audit` + `bandit` clean.
-- [ ] S3 bucket policies reviewed if paths changed.
-
-### 7. Communication
-- [ ] Sub-team lead notified.
-- [ ] Stakeholders notified if user-facing.
-- [ ] Site ops team aware if on-site MySQL / Zabbix touched.
-
----
-
-### 8. Service Control Commands
-
-#### Pause Before Testing (Copy-Paste Ready)
-
-**Glue Jobs:**
-```bash
-# List your Glue jobs
-aws glue list-jobs --query "JobNames" --output table
-
-# Disable trigger
-aws glue update-trigger --name <TRIGGER_NAME> --trigger-update State=DISABLED
-
-# Verify disabled
-aws glue get-trigger --name <TRIGGER_NAME> --query "Trigger.State"
-```
-
-**Step Functions:**
-```bash
-# List state machines
-aws stepfunctions list-state-machines --query "stateMachines[].name" --output table
-
-# Check running executions
-aws stepfunctions list-executions \\
-  --state-machine-arn arn:aws:states:us-east-1:<ACCOUNT>:stateMachine:<SM_NAME> \\
-  --status-filter RUNNING --max-results 10
-
-# Disable EventBridge schedule
-aws events disable-rule --name <RULE_NAME>
-```
-
-**Zabbix (via API):**
-```python
-from pyzabbix import ZabbixAPI
-zapi = ZabbixAPI("https://<SITE>.zabbix.fluenceenergy.com")
-zapi.login(user="admin", password="...")
-
-# Create 4-hour maintenance window
-zapi.maintenance.create(
-    name="PROD-TEST-<JIRA>",
-    active_since=int(time.time()),
-    active_till=int(time.time()) + 14400,
-    hostids=["<HOST_ID>"],
-    timeperiods=[{"period": 14400, "timeperiod_type": 0}]
-)
-```
-
-#### Resume After Testing (MANDATORY)
-```bash
-# Re-enable Glue trigger
-aws glue update-trigger --name <TRIGGER_NAME> --trigger-update State=ENABLED
-
-# Re-enable EventBridge rule
-aws events enable-rule --name <RULE_NAME>
-
-# Delete Zabbix maintenance (via UI or API)
-```
-
-#### Emergency Stop (P1 Incidents Only)
-```bash
-# Stop ALL running Glue jobs for a specific job name
-JOB_RUNS=$(aws glue get-job-runs --job-name <JOB_NAME> \\
-  --query "JobRuns[?JobRunState=='RUNNING'].Id" --output text)
-if [ -n "$JOB_RUNS" ]; then
-  aws glue batch-stop-job-run --job-name <JOB_NAME> --job-run-ids $JOB_RUNS
-fi
-
-# Stop Step Function execution
-aws stepfunctions stop-execution --execution-arn <ARN> --cause "Emergency stop - P1"
-```
-
----
-
-## Post-Deployment Verification
-
-### Immediate (0–15 min)
-1. CloudWatch → `ERROR` in relevant log group:
-   ```bash
-   aws logs filter-log-events --log-group-name /aws/glue/jobs/JOB \
-     --start-time $(date -d '15 minutes ago' +%s000) --filter-pattern "ERROR"
-   ```
-2. Database → `SELECT` confirms change applied.
-3. Zabbix → `Monitoring → Latest Data` on affected hosts.
-4. Step Functions → monitor next scheduled execution.
-
-### Short-Term (15 min – 24 hr)
-1. Zabbix: new triggered alerts?
-2. Spot-check pipeline outputs (parquet files).
-3. Athena queries return expected results?
-4. CloudWatch metrics: anomalies?
-
-### Sign-Off
-- [ ] Smoke tests passed.
-- [ ] Error rates nominal 15+ min.
-- [ ] No unexpected Zabbix triggers.
-- [ ] Rollback mechanism verified still functional.
-
-## If Something Goes Wrong
-1. **Don't panic.**  Follow the rollback plan.
-2. **Roll back first, investigate second.**
-3. Create Jira incident ticket.
-4. Notify sub-team lead and Isaiah.
-5. Blameless post-mortem within 48 hours.
-ENDSKILL
-
-write_skill "ps" "$SKILL_PS"
-
-###############################################################################
-#  mc/SKILL.md  —  Master Checklist (Combined Reference)
-###############################################################################
-
-read -r -d '' SKILL_MC << 'ENDSKILL' || true
-# GSDE&G Development Master Checklist
-
-> Combined quick-reference for the complete development lifecycle.
-> Use before every PR and deployment.
-
----
-
-## Phase 1 · Plan & Branch  → `gg/SKILL.md`
-- [ ] Jira ticket exists (GSDE / GSDEA / SORT).
-- [ ] Branch: `<type>/<ticket>-<desc>` from `main`.
-
-## Phase 2 · TDD  → `tdd/SKILL.md`
-- [ ] **RED:** failing test(s) written.
-- [ ] **GREEN:** minimum implementation to pass.
-- [ ] **REFACTOR:** cleaned up, tests still green.
-- [ ] AWS mocked with `moto`.  DB tests use `SAVEPOINT` + `ROLLBACK`.
-
-## Phase 3 · QA  → `qa/SKILL.md`
-- [ ] Unit + integration + regression coverage.
-- [ ] If production testing needed:
-  - [ ] `_test/` prefix · `_test_flag` column · `SAVEPOINT`
-  - [ ] Two people present.  Timestamped log attached.
-  - [ ] Test data cleaned up.
-
-## Phase 4 · Code Review  → `cr/SKILL.md`
-- [ ] ≤ 400 LoC.
-- [ ] Security: IAM, S3, credentials.
-- [ ] Prod safety: rollback, blast radius, alerts.
-- [ ] `ruff check .` + `mypy .` pass.
-
-## Phase 5 · Pull Request  → `pr/SKILL.md`
-- [ ] Affected systems listed.
-- [ ] Testing evidence attached.
-- [ ] Rollback plan with exact commands.
-
-## Phase 6 · CI  → `cicd/SKILL.md`
-- [ ] All checks pass (lint, type, test, security, build).
-- [ ] Manual approval for prod-impacting changes.
-
-## Phase 7 · Deploy  → `ps/SKILL.md`
-- [ ] Backups taken (RDS snapshot · mysqldump · policy export).
-- [ ] Blast radius assessed — incremental if > 1 site.
-- [ ] Maintenance window if Zabbix alerts expected.
-- [ ] Post-deploy smoke test passed, 15+ min nominal.
-
----
-
-## Emergency Hotfix
-```
-1. hotfix/<ticket>-<desc> from main
-2. Backup → regression test → fix → verify
-3. PR → expedited review → merge
-4. Monitor 30 min → rollback if bad
-5. Post-mortem within 48 hours
-```
-
----
-
-## Quick Commands
-```bash
-# ── Testing ──────────────────────────────────
-pytest tests/ -v --tb=short
-
-# ── Linting ──────────────────────────────────
-ruff check . && ruff format --check .
-mypy . --ignore-missing-imports
-
-# ── Security ─────────────────────────────────
-bandit -r src/ && pip-audit
-
-# ── RDS Snapshot ─────────────────────────────
-aws rds create-db-snapshot \
-  --db-instance-identifier fe-gsdl-poc-database \
-  --db-snapshot-identifier pre-deploy-$(date +%Y%m%d-%H%M%S)
-
-# ── IAM Simulate ─────────────────────────────
-aws iam simulate-principal-policy \
-  --policy-source-arn arn:aws:iam::ACCOUNT:role/ROLE \
-  --action-names s3:GetObject glue:StartJobRun
-
-# ── Athena Cost Check ────────────────────────
-EXPLAIN SELECT …;
-
-# ── Test Data Cleanup ────────────────────────
-aws s3 rm s3://fluenceenergy-ops-data-lakehouse/das_catalog/_test/ --recursive
-```
-
----
-
-## Skill Index
-| Skill | Path | Purpose |
-|-------|------|---------|
-| QA | `qa/SKILL.md` | Testing strategy + production test runbooks |
-| CR | `cr/SKILL.md` | Code review with prod-safety checks |
-| PR | `pr/SKILL.md` | PR description generator |
-| TDD | `tdd/SKILL.md` | Red-Green-Refactor + stack patterns |
-| GIT-GUARD | `gg/SKILL.md` | Branch policy & workflow enforcement |
-| CICD | `cicd/SKILL.md` | GitHub Actions pipeline design |
-| PROD-SAFETY | `ps/SKILL.md` | Pre/post-deploy checklists |
-| MASTER | `mc/SKILL.md` | This file |
-ENDSKILL
-
-write_skill "mc" "$SKILL_MC"
-
-# =============================================================================
-#  SUMMARY
-# =============================================================================
-echo ""
-
-if $DRY_RUN; then
-  warn "Dry run complete — no files were written."
-  echo ""
-  exit 0
-fi
+Senior security reviewer for AgentShroud — a security proxy for AI agents.
+
+## Focus Areas
+1. **Credential handling** — no hardcoded secrets, use 1Password/env
+2. **Input validation** — injection, traversal, SSRF, XSS
+3. **Container security** — least privilege, read-only fs, seccomp
+4. **PII protection** — Presidio integration, sanitizer coverage
+5. **Audit trail** — all actions logged, tamper-resistant
+6. **Network isolation** — containers properly segmented
+
+## Output
+For each finding: `[SEVERITY] file:line — Description + Suggested fix`
+Severities: CRITICAL, HIGH, MEDIUM, LOW, INFO
+END
+write_skill "sec" "$SKILL_SEC"
+
+# Code Review Skill
+read -r -d '' SKILL_CR << 'END' || true
+# Skill: Code Review (CR)
 
-success "All 8 skills deployed successfully."
-echo ""
-info "Verifying:"
-if command -v tree &>/dev/null; then
-  tree "$SKILLS_ROOT"
-else
-  find "$SKILLS_ROOT" -type f | sort | while read -r f; do
-    echo "  ${f#"$SKILLS_ROOT/"}"
-  done
-fi
+## Review Principles
+1. Security-critical areas get extra scrutiny
+2. The 400-line rule: flag PRs exceeding 400 LoC
+3. Functionality, performance, readability
+4. Static analysis: OWASP Top 10
+
+## Output
+- Review Summary: Pass / Request Changes
+- Security Audit
+- Detailed comments with suggested fixes
+END
+write_skill "cr" "$SKILL_CR"
 
-echo ""
-info "Next steps:"
-echo ""
-echo "  1.  Review the master checklist:"
-echo "        less $SKILLS_ROOT/mc/SKILL.md"
-echo ""
-echo "  2.  Commit to your repo:"
-echo "        cd $(dirname "$SKILLS_ROOT")"
-echo "        git add skills/"
-echo "        git commit -m 'chore: deploy Claude Code skills for TDD workflow'"
-echo ""
-echo "  3.  Use in Claude Code:"
-echo "        /read skills/tdd/SKILL.md"
-echo "        /read skills/qa/SKILL.md"
-echo ""
-echo "  4.  tmux tip (you're on 2.6+):"
-echo "        Ctrl+B %  → split pane"
-echo "        View a skill in one pane while coding in the other"
-echo ""
-echo "  5.  Re-deploy after edits:"
-echo "        $SCRIPT_DIR/$(basename "$0") --clean"
-echo ""
+# Environment Manager Skill
+read -r -d '' SKILL_ENV << 'END' || true
+# Skill: Environment Manager (ENV)
+
+## Responsibilities
+- Docker container configuration and health
+- 1Password CLI integration
+- Dependency management (conda, pip, npm)
+- Pi-specific constraints (ARM64, 8GB RAM, 2GB swap)
+- Shell configuration (zsh, env vars)
+END
+write_skill "env" "$SKILL_ENV"
+
+# Project Manager Skill
+read -r -d '' SKILL_PM << 'END' || true
+# Skill: Project Manager (PM)
+
+## Responsibilities
+- Phase tracking and milestone updates
+- Peer review process coordination
+- iCloud Calendar/Reminders sync
+- Memory and documentation maintenance
+- Risk assessment and blocker tracking
+END
+write_skill "pm" "$SKILL_PM"
+
+echo "✓ All skills deployed"
diff --git a/.claude/scripts/missing/deploy-claude-skills.sh b/.claude/scripts/missing/deploy-claude-skills.sh
deleted file mode 100755
index 9219958..0000000
--- a/.claude/scripts/missing/deploy-claude-skills.sh
+++ /dev/null
@@ -1,644 +0,0 @@
-#!/usr/bin/env bash
-# =============================================================================
-# deploy-claude-skills.sh (Additional Skills)
-#
-# Deploys additional Claude Code skills for the GSDE&G Development Team.
-# Adds: MCP Tools | Incident Response | Data Validation
-#
-# Intended location:
-#   .claude/scripts/missing/deploy-claude-skills.sh
-#
-# Deploys to:
-#   ../../skills/   (relative to this script)
-#
-# Hierarchy:
-#   skills/
-#   ├── mcp/                        ← MCP tools integration
-#   │   └── skill-mcp-tools.md
-#   ├── production/                 ← Additional production skills
-#   │   └── skill-incident-response.md
-#   └── data/                       ← Data validation
-#       └── skill-data-validation.md
-#
-# Usage:
-#   chmod +x deploy-claude-skills.sh
-#   ./deploy-claude-skills.sh            # deploy
-#   ./deploy-claude-skills.sh --dry-run  # preview only
-#   ./deploy-claude-skills.sh --clean    # remove and redeploy
-# =============================================================================
-
-set -euo pipefail
-
-# ── Resolve paths relative to THIS script ────────────────────────────────────
-SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
-SKILLS_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)/skills"
-TIMESTAMP="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
-DRY_RUN=false
-CLEAN=false
-
-# ── Parse arguments ──────────────────────────────────────────────────────────
-while [[ $# -gt 0 ]]; do
-  case "$1" in
-    --dry-run) DRY_RUN=true; shift ;;
-    --clean)   CLEAN=true;   shift ;;
-    -h|--help)
-      echo "Usage: $0 [--dry-run] [--clean]"
-      echo ""
-      echo "  --dry-run  Preview what would be created (no writes)"
-      echo "  --clean    Remove existing skills directory and redeploy"
-      echo ""
-      echo "  Script:  $0"
-      echo "  Target:  $SKILLS_ROOT/"
-      exit 0
-      ;;
-    *) echo "Error: Unknown option '$1'"; exit 1 ;;
-  esac
-done
-
-# ── Helpers ──────────────────────────────────────────────────────────────────
-info()    { printf "\033[1;34m[INFO]\033[0m  %s\n" "$1"; }
-success() { printf "\033[1;32m  OK  \033[0m  %s\n" "$1"; }
-warn()    { printf "\033[1;33m[WARN]\033[0m  %s\n" "$1"; }
-header()  { printf "\n\033[1;36m── %s ──\033[0m\n" "$1"; }
-
-write_file() {
-  # $1 = relative path under SKILLS_ROOT   $2 = content
-  local fpath="$SKILLS_ROOT/$1"
-  if $DRY_RUN; then
-    info "[DRY RUN] Would create: $fpath"
-    return
-  fi
-  mkdir -p "$(dirname "$fpath")"
-  printf '%s\n' "$2" > "$fpath"
-  success "$1"
-}
-
-# ── Clean if requested ───────────────────────────────────────────────────────
-if $CLEAN && ! $DRY_RUN; then
-  if [[ -d "$SKILLS_ROOT/mcp" ]]; then
-    warn "Removing existing: $SKILLS_ROOT/mcp"
-    rm -rf "$SKILLS_ROOT/mcp"
-  fi
-  if [[ -d "$SKILLS_ROOT/data" ]]; then
-    warn "Removing existing: $SKILLS_ROOT/data"
-    rm -rf "$SKILLS_ROOT/data"
-  fi
-  if [[ -f "$SKILLS_ROOT/production/skill-incident-response.md" ]]; then
-    warn "Removing existing: $SKILLS_ROOT/production/skill-incident-response.md"
-    rm -f "$SKILLS_ROOT/production/skill-incident-response.md"
-  fi
-fi
-
-# =============================================================================
-#  BANNER
-# =============================================================================
-echo ""
-echo "  ╔══════════════════════════════════════════════════════════════╗"
-echo "  ║   GSDE&G  Additional Claude Code Skills — Deployer          ║"
-echo "  ╚══════════════════════════════════════════════════════════════╝"
-info "Script : $SCRIPT_DIR/$(basename "$0")"
-info "Target : $SKILLS_ROOT/"
-info "Time   : $TIMESTAMP"
-$DRY_RUN && warn "Mode   : DRY RUN — no files will be written"
-$CLEAN   && warn "Mode   : CLEAN — existing skills removed first"
-
-# =============================================================================
-#                         S K I L L   C O N T E N T
-# =============================================================================
-
-###############################################################################
-# ┌─────────────────────────────────────────────────────────────────────────┐ #
-# │  mcp/skill-mcp-tools.md  —  MCP Server Usage Guide                     │ #
-# └─────────────────────────────────────────────────────────────────────────┘ #
-###############################################################################
-header "mcp/ — MCP Tools Integration"
-
-read -r -d '' SKILL_MCP << 'ENDSKILL' || true
-# Skill: MCP Tools Usage (MCP-TOOLS)
-
-## Role
-You are an integration specialist guiding the use of MCP (Model Context Protocol)
-servers for the GSDE&G team. Help developers leverage external tools effectively.
-
-## Available MCP Servers
-
-| Server | Purpose | Auth Required |
-|--------|---------|---------------|
-| GitHub | Code search, PRs, issues | OAuth (Device Flow) |
-| Atlassian | Jira tickets, Confluence docs | OAuth 2.0 (3LO) |
-| AWS API | All AWS CLI commands | AWS credentials |
-
----
-
-### 1. GitHub MCP
-
-**When to invoke:**
-- Searching code patterns across repos
-- Creating/reviewing pull requests
-- Checking CI/CD status
-- Managing issues
-
-**Common operations:**
-```
-# Search for error handling patterns
-mcp__github__search_code: "try.*except.*logging" language:python
-
-# Get PR details
-mcp__github__get_pull_request: owner=fluence-energy repo=gsdl pr_number=123
-
-# List open issues
-mcp__github__list_issues: owner=fluence-energy repo=gsdl state=open
-```
-
-**Best practices:**
-- Use `gh` CLI via Bash for complex operations
-- Search code before implementing (avoid duplication)
-- Link PRs to Jira tickets in description
-
----
-
-### 2. Atlassian MCP (Jira + Confluence)
-
-**When to invoke:**
-- Looking up ticket requirements (GSDE, GSDEA, SORT)
-- Reading runbooks in Confluence
-- Updating ticket status
-
-**Jira JQL Examples:**
-```jql
-# My open tickets
-project IN (GSDE, GSDEA, SORT) AND assignee = currentUser() AND status != Done
-
-# Tickets touching Glue jobs
-project = GSDE AND text ~ "Glue" AND status = "In Progress"
-
-# Recent bugs
-project = GSDE AND issuetype = Bug AND created >= -7d
-```
-
-**Confluence searches:**
-```
-# Find runbook
-mcp__atlassian__searchConfluenceUsingCql: cql='title ~ "runbook" AND space = GSDE'
-
-# Get specific page
-mcp__atlassian__getConfluencePage: pageId=12345 contentFormat=markdown
-```
-
-**Best practices:**
-- Always link commits/PRs to Jira tickets
-- Update ticket status when starting work
-- Document production testing results in ticket comments
-
----
-
-### 3. AWS API MCP
-
-**When to invoke:**
-- Checking job/pipeline status
-- Querying S3 data lake structure
-- Validating IAM permissions
-- Reading CloudWatch logs
-
-**Safe read-only queries:**
-```bash
-# S3 data lake structure
-aws s3 ls s3://fluenceenergy-ops-data-lakehouse/das_catalog/ --recursive --page-size 100
-
-# Glue job status
-aws glue get-job-runs --job-name <JOB_NAME> --max-results 5
-
-# Step Function executions
-aws stepfunctions list-executions \
-  --state-machine-arn arn:aws:states:us-east-1:<ACCOUNT>:stateMachine:<SM_NAME> \
-  --max-results 10
-
-# RDS instance status
-aws rds describe-db-instances --db-instance-identifier fe-gsdl-poc-database
-
-# CloudWatch recent errors
-aws logs filter-log-events --log-group-name /aws/glue/jobs/<JOB> \
-  --filter-pattern "ERROR" --limit 20
-
-# IAM policy simulation (always do before changes)
-aws iam simulate-principal-policy \
-  --policy-source-arn arn:aws:iam::<ACCOUNT>:role/<ROLE> \
-  --action-names s3:GetObject
-```
-
-**NEVER execute via MCP without approval:**
-- `aws s3 rm` (data deletion)
-- `aws glue delete-*` (infrastructure)
-- `aws iam put-*` (permissions)
-- `aws rds delete-*` (database)
-
----
-
-## MCP Troubleshooting
-
-### Authentication Issues
-```bash
-# Reset GitHub MCP auth
-/mcp-auth-reset github
-
-# Check MCP server status
-/mcp-doctor
-
-# Verify AWS credentials
-aws sts get-caller-identity
-```
-
-### Common Errors
-| Error | Cause | Fix |
-|-------|-------|-----|
-| "Token expired" | OAuth token timeout | Re-authenticate via browser |
-| "Access denied" | Missing permissions | Check IAM role/policy |
-| "Rate limited" | Too many API calls | Wait 60s, batch requests |
-ENDSKILL
-
-write_file "mcp/skill-mcp-tools.md" "$SKILL_MCP"
-
-###############################################################################
-# ┌─────────────────────────────────────────────────────────────────────────┐ #
-# │  production/skill-incident-response.md  —  Incident Response           │ #
-# └─────────────────────────────────────────────────────────────────────────┘ #
-###############################################################################
-header "production/ — Incident Response"
-
-read -r -d '' SKILL_INCIDENT << 'ENDSKILL' || true
-# Skill: Incident Response (INCIDENT)
-
-## Role
-You are an Incident Commander for the GSDE&G team. Guide rapid, safe response
-to production issues with a "rollback first, investigate second" philosophy.
-
-## Severity Matrix
-
-| Level | Impact | Response | Escalation | Examples |
-|-------|--------|----------|------------|----------|
-| **P1** | Data loss, full outage | Immediate | Isaiah + all leads | S3 data deleted, RDS down |
-| **P2** | Partial outage, degraded | < 1 hour | Sub-team lead | Glue jobs failing, 50+ sites affected |
-| **P3** | Minor issue, workaround | < 4 hours | Team channel | Single site data gap, UI issue |
-| **P4** | Cosmetic, no impact | Next sprint | Jira only | Log noise, minor display bug |
-
----
-
-## Incident Response Workflow
-
-### Phase 1: ASSESS (Max 5 minutes)
-
-```bash
-# 1. Check Glue job status
-aws glue get-job-runs --job-name <JOB_NAME> --max-results 10 \
-  --query "JobRuns[?JobRunState!='SUCCEEDED']"
-
-# 2. Check Step Function failures
-aws stepfunctions list-executions \
-  --state-machine-arn arn:aws:states:us-east-1:<ACCOUNT>:stateMachine:<SM_NAME> \
-  --status-filter FAILED --max-results 10
-
-# 3. Check CloudWatch for errors
-aws logs filter-log-events \
-  --log-group-name /aws/glue/jobs/<JOB_NAME> \
-  --filter-pattern "ERROR" \
-  --start-time $(date -d '1 hour ago' +%s000) --limit 50
-
-# 4. Check S3 for recent writes (data flowing?)
-aws s3 ls s3://fluenceenergy-ops-data-lakehouse/das_catalog/das_exports_latest/ \
-  --recursive | tail -20
-
-# 5. Check RDS connectivity
-aws rds describe-db-instances --db-instance-identifier fe-gsdl-poc-database \
-  --query "DBInstances[0].DBInstanceStatus"
-```
deprecated: `[features].web_search_request` is deprecated. Use `web_search` instead.
  Set `web_search` to `"live"`, `"cached"`, or `"disabled"` at the top level (or under a profile) in config.toml.
mcp: atlassian starting
mcp: awslabs.aws-api-mcp-server starting
mcp: github starting
mcp: awslabs.aws-api-mcp-server failed: MCP client for `awslabs.aws-api-mcp-server` failed to start: MCP startup failed: Invalid MCP server name 'awslabs.aws-api-mcp-server': must match pattern ^[a-zA-Z0-9_-]+$
2026-02-17T02:47:04.502360Z ERROR codex_core::rollout::list: state db missing rollout path for thread 019c68e0-b6b2-7fc3-b85e-19c8529e2954
2026-02-17T02:47:04.540340Z ERROR codex_core::rollout::list: state db missing rollout path for thread 019c68e9-fa57-7bd3-ab4b-a948fd4b2c65
mcp: github failed: MCP client for `github` failed to start: MCP startup failed: handshaking with MCP server failed: connection closed: initialize response
2026-02-17T02:47:04.576203Z ERROR codex_core::rollout::list: state db missing rollout path for thread 019c6900-d01b-7bd2-b9dd-f92b70af4cf5
mcp: atlassian failed: MCP client for `atlassian` timed out after 10 seconds. Add or adjust `startup_timeout_sec` in your config.toml:
[mcp_servers.atlassian]
startup_timeout_sec = XX
mcp startup: failed: awslabs.aws-api-mcp-server, github, atlassian
🌐 Searching the web...
🌐 Searched the web
🌐 Searching the web...
🌐 Searched the web
🌐 Searching the web...
🌐 Searched the web
🌐 Searching the web...
🌐 Searched the web
🌐 Searching the web...
🌐 Searched the web
codex
[HIGH] .claude/scripts/claude-hooks/run_targeted_tests.sh:12 – Unquoted expansions lead to word-splitting and globbing  
The loop `for pyfile in $changed_py; do` and later `pytest -q $test_files` build lists by splitting on whitespace. If any file names contain spaces or glob characters, this will break or even run unexpected tests.  
Suggested fix: collect changed files and test files into a bash array and invoke pytest with quoted array expansions, e.g.  
```bash
mapfile -t changed_py < <(git diff --name-only HEAD | grep -E '\.py$' || true)
test_files=()
for pyfile in "${changed_py[@]}"; do
  # …  
  test_files+=("$test_dir/test_$base")
done
if ((${#test_files[@]})); then
  pytest -q "${test_files[@]}"
else
  pytest -q -m "not slow"
fi
```

[HIGH] .claude/scripts/claude-hooks/run_targeted_tests.sh:17 – Silencing test failures hides regressions  
Both `pytest -q $test_files || true` and the fallback `pytest -q -m "not slow" || true` swallow any non-zero exit code, so no hook ever fails even when tests fail. This undermines CI safety.  
Suggested fix: remove the `|| true` so that `set -e` will abort on test failures, or explicitly check the return code and exit non-zero on failure.

[HIGH] .claude/scripts/claude-hooks/warn_dangerous_bash.sh:5 – Incorrect use of `\|` with grep -E breaks alternation  
The pattern `"curl .*\|.*sh"` is passed to `grep -E`, where `\|` is interpreted literally and does not act as an OR. As a result, a multi-step pipeline like `curl ... | sh` won’t be warned.  
Suggested fix: use proper ERE alternation without backslashes, e.g.  
```bash
dangerous_patterns+=("curl .*|.*sh" "wget .*|.*sh")
```

[MEDIUM] .claude/scripts/deploy-claude-skills.sh:27 – `--help` option was removed, losing user guidance  
The previous script supported `-h|--help` to describe usage; the new version rejects unknown options outright.  
Suggested fix: re-introduce a `-h|--help` case that prints a concise usage and exits.

[MEDIUM] .claude/scripts/deploy-claude-skills.sh:66 – Dry-run mode misleadingly shows “✓ All skills deployed”  
When `--dry-run` is passed, no files are written but the script still prints “✓ All skills deployed”.  
Suggested fix: at the end, check `if $DRY_RUN; then echo "Dry run complete — no files written."; else echo "✓ All skills deployed"; fi`

[LOW] .claude/scripts/deploy-claude-skills.sh:46 – Verbose comments and legacy code removed without deprecation notice  
The giant GSDE&G-specific skill definitions were dropped wholesale. If any downstream automation depended on those, this will silently break.  
Suggested fix: archive the old skill definitions (e.g. in a git tag or backup file) and log a deprecation note, so integrators can migrate.

[INFO] .claude/scripts/deploy-claude-skills.sh:13 – Skill directories hard-coded; no wildcard support  
New skills are explicitly listed (`sec`, `cr`, `env`, `pm`). Consider discovering all `SKILL_*.md` variables or scanning a directory to avoid updating the script whenever a new skill is added.
tokens used
30,251
[HIGH] .claude/scripts/claude-hooks/run_targeted_tests.sh:12 – Unquoted expansions lead to word-splitting and globbing  
The loop `for pyfile in $changed_py; do` and later `pytest -q $test_files` build lists by splitting on whitespace. If any file names contain spaces or glob characters, this will break or even run unexpected tests.  
Suggested fix: collect changed files and test files into a bash array and invoke pytest with quoted array expansions, e.g.  
```bash
mapfile -t changed_py < <(git diff --name-only HEAD | grep -E '\.py$' || true)
test_files=()
for pyfile in "${changed_py[@]}"; do
  # …  
  test_files+=("$test_dir/test_$base")
done
if ((${#test_files[@]})); then
  pytest -q "${test_files[@]}"
else
  pytest -q -m "not slow"
fi
```

[HIGH] .claude/scripts/claude-hooks/run_targeted_tests.sh:17 – Silencing test failures hides regressions  
Both `pytest -q $test_files || true` and the fallback `pytest -q -m "not slow" || true` swallow any non-zero exit code, so no hook ever fails even when tests fail. This undermines CI safety.  
Suggested fix: remove the `|| true` so that `set -e` will abort on test failures, or explicitly check the return code and exit non-zero on failure.

[HIGH] .claude/scripts/claude-hooks/warn_dangerous_bash.sh:5 – Incorrect use of `\|` with grep -E breaks alternation  
The pattern `"curl .*\|.*sh"` is passed to `grep -E`, where `\|` is interpreted literally and does not act as an OR. As a result, a multi-step pipeline like `curl ... | sh` won’t be warned.  
Suggested fix: use proper ERE alternation without backslashes, e.g.  
```bash
dangerous_patterns+=("curl .*|.*sh" "wget .*|.*sh")
```

[MEDIUM] .claude/scripts/deploy-claude-skills.sh:27 – `--help` option was removed, losing user guidance  
The previous script supported `-h|--help` to describe usage; the new version rejects unknown options outright.  
Suggested fix: re-introduce a `-h|--help` case that prints a concise usage and exits.

[MEDIUM] .claude/scripts/deploy-claude-skills.sh:66 – Dry-run mode misleadingly shows “✓ All skills deployed”  
When `--dry-run` is passed, no files are written but the script still prints “✓ All skills deployed”.  
Suggested fix: at the end, check `if $DRY_RUN; then echo "Dry run complete — no files written."; else echo "✓ All skills deployed"; fi`

[LOW] .claude/scripts/deploy-claude-skills.sh:46 – Verbose comments and legacy code removed without deprecation notice  
The giant GSDE&G-specific skill definitions were dropped wholesale. If any downstream automation depended on those, this will silently break.  
Suggested fix: archive the old skill definitions (e.g. in a git tag or backup file) and log a deprecation note, so integrators can migrate.

[INFO] .claude/scripts/deploy-claude-skills.sh:13 – Skill directories hard-coded; no wildcard support  
New skills are explicitly listed (`sec`, `cr`, `env`, `pm`). Consider discovering all `SKILL_*.md` variables or scanning a directory to avoid updating the script whenever a new skill is added.
