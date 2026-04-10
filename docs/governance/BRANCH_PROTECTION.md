# GitHub Branch Protection — `main`

This document records the required GitHub repository settings for the `main`
branch. These are **manual UI toggles** — they cannot be applied via a PR.
After merging a PR that adds this file, apply the settings below.

---

## Required Settings

Navigate to: **GitHub → Repository → Settings → Branches → Branch protection rules → Edit (main)**

| Setting | Required value |
|---------|---------------|
| Require a pull request before merging | **Enabled** |
| Require approvals | **1** |
| Dismiss stale pull request approvals when new commits are pushed | Enabled |
| Require review from Code Owners | Enabled (CODEOWNERS already present at `.github/CODEOWNERS`) |
| Require status checks to pass before merging | **Enabled** |
| Required status checks | `test`, `lint`, `smoke-static` |
| Require branches to be up to date before merging | Enabled |
| Require conversation resolution before merging | **Enabled** |
| Include administrators | **Enabled** (no bypass for any account) |
| Allow force pushes | **Disabled** |
| Allow deletions | **Disabled** |

### Required Status Checks

The three checks listed above map to jobs in `.github/workflows/`:

| Check name | Workflow job | Notes |
|------------|--------------|-------|
| `test` | `pytest` full suite | `gateway/tests/` — must hold ≥ 94% coverage |
| `lint` | `ruff check . && black --check .` | Zero tolerance |
| `smoke-static` | `tests/startup_smoke/test_bot_boot_static.sh` | Runs on GitHub-hosted runner; no Docker required |

---

## Verification

After applying the settings, verify via the GitHub CLI:

```bash
gh api repos/idallasjlabs/agentshroud/branches/main/protection
```

A successful response returns a JSON object with `required_pull_request_reviews`,
`required_status_checks`, `enforce_admins`, `restrictions`, and
`allow_force_pushes: false`. A 404 means protection is not yet enabled.

To confirm force-push is blocked:

```bash
# From a clean clone — should be rejected by GitHub
git checkout main
git commit --allow-empty -m "test: force-push rejection"
git push origin main
# Expected: ERROR: GitHub has blocked the push — branch protection enforced
```

---

## Local Enforcement (already active)

GitHub branch protection is the **remote** enforcement layer. The local
PreToolUse hook at `.claude/scripts/claude-hooks/block_main_commits.sh`
provides the **local** enforcement layer — it blocks `git commit`, `git push`,
and `git merge` when the current branch is `main` before the command ever
reaches GitHub.

Both layers are required:
- Local hook catches mistakes before they create noise in the remote history.
- GitHub protection catches pushes from machines where the hook is not loaded
  (e.g., a second developer's machine or a Gemini/Codex agent session).
