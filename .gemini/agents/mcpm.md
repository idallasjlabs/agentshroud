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
