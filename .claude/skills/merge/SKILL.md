# Skill: /merge — Admin PR Merge

## Role
You are the PR Merge Operator for AgentShroud. This skill merges PRs on
`main` when branch protection requires an approving review.

## When to Use
Invoke when asked to merge a PR and the merge fails due to branch protection,
or when the user says `/merge`.

## Auth Stack (try in order)

Use the first auth method that works:

1. **`gh` CLI** — check with `gh auth status`. If valid, proceed.
2. **MCP `.env` PAT** — extract and export:
   ```bash
   export GH_TOKEN=$(grep GITHUB_PERSONAL_ACCESS_TOKEN \
     .llm_settings/mcp-servers/github/.env | cut -d= -f2)
   gh auth status
   ```
3. **Ask user** — `! gh auth login -h github.com` in the conversation prompt.

The `gh` CLI **must be authenticated as `idallasj`** (admin) for branch
protection management. Verify with `gh auth status` before proceeding.

## Bot Account

- **GitHub username:** `agentshroud-ai`
- **1Password item:** `zjncjjozurlws7nbs66of7befa` in vault `Agent Shroud Bot Credentials`
- **Retrieve PAT (try in order — stop at first success):**
  ```bash
  # 1. .env file (no Touch ID required — preferred when remote)
  BOT_PAT=$(grep AGENTSHROUD_BOT_PAT .env 2>/dev/null | cut -d= -f2)

  # 2. 1Password CLI (requires Touch ID / biometrics)
  if [ -z "$BOT_PAT" ]; then
    BOT_PAT=$(op item get zjncjjozurlws7nbs66of7befa \
      --vault "Agent Shroud Bot Credentials" \
      --fields "personal access token" --reveal)
  fi
  ```
- `.env` lives at the repo root and is gitignored. Contains `AGENTSHROUD_BOT_PAT=<token>`.
- `agentshroud-ai` is a **write collaborator** on `idallasjlabs/agentshroud`.
  Its approvals count toward the required review.

## Procedure

### Step 1 — Verify auth
```bash
gh auth status
```
Confirm `idallasj` is active. If not, follow the Auth Stack above.

### Step 2 — Verify PR is ready
Use `mcp__github__pull_request_read` (method: `get`) to confirm:
- `state: "OPEN"`
- `mergeable_state` is not `"dirty"` (no conflicts)

Use `mcp__github__pull_request_read` (method: `get_check_runs`) to confirm
all required CI checks are green. If CI is failing and user explicitly
authorizes bypass, proceed; otherwise stop and report.

### Step 3 — Bot approval
Approve as `agentshroud-ai` (satisfies the 1-review requirement):
```bash
BOT_PAT=$(grep AGENTSHROUD_BOT_PAT .env 2>/dev/null | cut -d= -f2)
if [ -z "$BOT_PAT" ]; then
  BOT_PAT=$(op item get zjncjjozurlws7nbs66of7befa \
    --vault "Agent Shroud Bot Credentials" \
    --fields "personal access token" --reveal)
fi

GH_TOKEN="$BOT_PAT" gh api \
  repos/idallasjlabs/agentshroud/pulls/<PR_NUMBER>/reviews \
  --method POST \
  -H "Accept: application/vnd.github+json" \
  -f body="LGTM — automated merge via /merge skill" \
  -f event="APPROVE"
```
Confirm response: `"state": "APPROVED"`, `"user": {"login": "agentshroud-ai"}`.

### Step 4 — Merge
Use `mcp__github__merge_pull_request`:
- `owner: idallasjlabs`, `repo: agentshroud`
- `pullNumber: <PR_NUMBER>`
- `merge_method: squash`
- `commit_title: <original PR title> (#<PR_NUMBER>)`

**If merge still fails** (e.g., bot approval not counting), use the
protection-bypass fallback:

```bash
# 4a. Disable reviews (SAVE state first — always restore)
gh api --method PUT repos/idallasjlabs/agentshroud/branches/main/protection \
  -H "Accept: application/vnd.github+json" \
  --input - <<'EOF'
{
  "required_status_checks": null,
  "enforce_admins": false,
  "required_pull_request_reviews": null,
  "restrictions": null
}
EOF

# 4b. Merge via MCP (mcp__github__merge_pull_request)

# 4c. Restore IMMEDIATELY (even if 4b failed)
gh api --method PUT repos/idallasjlabs/agentshroud/branches/main/protection \
  -H "Accept: application/vnd.github+json" \
  --input - <<'EOF'
{
  "required_status_checks": null,
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "dismissal_restrictions": {},
    "dismiss_stale_reviews": true,
    "require_code_owner_reviews": true,
    "required_approving_review_count": 1,
    "require_last_push_approval": false
  },
  "restrictions": null
}
EOF
```
Confirm response contains `"enforce_admins": {"enabled": true}`.

### Step 5 — Version bump + tag
1. Read current version from `gateway/__init__.py` (`__version__`)
2. Increment patch: `1.0.62` → `1.0.63`
3. Create version-bump branch and update both files:
   - `gateway/__init__.py`: `__version__ = "<new_version>"`
   - `gateway/pyproject.toml`: `version = "<new_version>"` (line 7)
4. Commit, push, create PR, merge it (Steps 3–4 only, no recursive tagging)
5. Get the merge commit SHA:
   ```bash
   # Use the sha returned by mcp__github__merge_pull_request
   ```
6. Tag and push:
   ```bash
   git fetch origin
   git tag -a v<new_version> <merge_sha> -m "Release v<new_version> — PR #<original_PR_number>"
   git push origin v<new_version>
   ```

### Step 6 — Verify
```bash
gh api repos/idallasjlabs/agentshroud/branches/main/protection \
  -H "Accept: application/vnd.github+json" | python3 -c "
import json,sys; d=json.load(sys.stdin)
print('enforce_admins:', d.get('enforce_admins',{}).get('enabled'))
print('required_reviews:', d.get('required_pull_request_reviews',{}).get('required_approving_review_count'))
"
git tag --sort=-version:refname | head -3
```
Confirm: `enforce_admins: True`, `required_reviews: 1`, new tag present.

## Output Format
```
PR #<number> merged ✓
enforce_admins: restored ✓
Branch deleted: <branch-name>
Tagged: v<new_version> (bump PR #<bump_pr_number>)
Merged at: <timestamp>
```

## Safety Rules
- NEVER leave branch protection weakened — restore in Step 4c even if merge failed
- NEVER force-push to main
- NEVER skip Step 1 (auth check) or Step 2 (PR readiness)
- Auth chain: `gh auth status` → MCP `.env` → ask user to `gh auth login`
- Repo: `idallasjlabs/agentshroud` (main branch only)
- Bot account: `agentshroud-ai` (1Password `zjncjjozurlws7nbs66of7befa`)
- Default path is bot approval (Step 3); protection bypass is the fallback
