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
  --input /dev/null
```
Expected: JSON body with `"enabled": true`. Verify this field is present.
Note: Do NOT pass `-f enabled=true` — the GitHub API rejects that key (HTTP 422).

### Step 6 — Bump version and tag the merge
1. Read the current version from `gateway/__init__.py` (`__version__`)
2. Increment the patch: e.g., `1.0.60` → `1.0.61`
3. Create a version-bump branch and update both version files:
   - `gateway/__init__.py`: `__version__ = "<new_version>"`
   - `gateway/pyproject.toml`: `version = "<new_version>"`
4. Commit, push, create PR, and merge it using this same skill (Steps 1–5 only — no recursive tagging)
5. Get the merge commit SHA of the version-bump PR:
   ```bash
   gh pr view <BUMP_PR_NUMBER> --json mergeCommit -q .mergeCommit.oid
   ```
6. Tag that commit and push:
   ```bash
   git fetch origin
   git tag -a v<new_version> <merge_sha> -m "Release v<new_version> — PR #<original_PR_number>"
   git push origin v<new_version>
   ```

### Step 7 — Verify
```bash
gh pr view <PR_NUMBER> --json state,mergedAt
gh api repos/{owner}/{repo}/branches/main/protection/enforce_admins
git tag --sort=-version:refname | head -3
```
Confirm: `state: "MERGED"`, `"enabled": true`, and new tag is present.

## Output Format
Report the following after completing:
```
PR #<number> merged successfully.
enforce_admins: restored ✓
Branch deleted: <branch-name>
Tagged: v<new_version> (bump PR #<bump_pr_number>)
Merged at: <timestamp>
```

## Safety Rules
- NEVER leave enforce_admins disabled — always run Step 5 regardless of outcome
- NEVER force-push to main
- NEVER merge without running Step 1 first
- If the user provides a PR number, use it; do not guess
- Always substitute actual owner/repo (from Step 2) for `{owner}/{repo}`
- This skill applies to the `main` branch only
