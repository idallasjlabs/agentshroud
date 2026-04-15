# Skill: /merge — Admin PR Merge

## Role
You are the PR Merge Operator for AgentShroud. This skill automates the
3-step `enforce_admins` bypass required to merge PRs when branch protection
is active with `enforce_admins: true`.

## When to Use
Invoke this skill when asked to merge a PR and the normal `gh pr merge`
fails with a branch protection error, or when the user says `/merge`.

## Procedure

### Step 1 — Verify PR is ready
```bash
gh pr view <PR_NUMBER> --json state,mergeable,statusCheckRollup
```
- Confirm `state: "OPEN"` and `mergeable: "MERGEABLE"`
- If CI is failing and user explicitly authorizes bypass, proceed
- If PR is not mergeable (conflicts), stop and report

### Step 2 — Get repo info
```bash
gh repo view --json nameWithOwner
```
Capture `{owner}/{repo}` for use in the API calls below.

### Step 3 — Disable enforce_admins
```bash
gh api \
  --method DELETE \
  repos/{owner}/{repo}/branches/main/protection/enforce_admins \
  -H "Accept: application/vnd.github+json"
```
Expected: HTTP 204 (no content). Any other response is a failure — stop and
re-enable (Step 5) before reporting the error.

### Step 4 — Merge with admin flag
```bash
gh pr merge <PR_NUMBER> --squash --delete-branch --admin
```
If this fails, immediately run Step 5 before reporting the error.

### Step 5 — Re-enable enforce_admins (ALWAYS — even on failure)
```bash
gh api \
  --method POST \
  repos/{owner}/{repo}/branches/main/protection/enforce_admins \
  -H "Accept: application/vnd.github+json" \
  -f enabled=true
```
Expected: JSON body with `"enabled": true`. Verify this field is present.

### Step 6 — Verify
```bash
gh pr view <PR_NUMBER> --json state,mergedAt
gh api repos/{owner}/{repo}/branches/main/protection/enforce_admins
```
Confirm: `state: "MERGED"` and `"enabled": true`.

## Output Format
Report the following after completing:
```
PR #<number> merged successfully.
enforce_admins: restored ✓
Branch deleted: <branch-name>
Merged at: <timestamp>
```

## Safety Rules
- NEVER leave enforce_admins disabled — always run Step 5 regardless of outcome
- NEVER force-push to main
- NEVER merge without running Step 1 first
- If the user provides a PR number, use it; do not guess
- Always substitute actual owner/repo (from Step 2) for `{owner}/{repo}`
- This skill applies to the `main` branch only
