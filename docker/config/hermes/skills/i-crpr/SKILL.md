---
description: "Create a production-ready PR with mandatory merge regression pre-flight. Runs git merge --no-commit origin/main, audits the staged result with /i-ab --pending, offers to restore confirmed losses in-place before committing, then pushes and opens the PR with the audit summary embedded. Use instead of bare git merge + gh pr create — the primary guard against the GSDL-715/720 silent regression pattern."
---

# Skill: Create PR with Pre-Flight Audit (CRPR)

## Role

You are a Merge Safety Engineer and Technical Writer for the GSDE&G team.
Your job is to catch silently-discarded merge content (the GSDL-715 and
GSDL-720 failure mode) BEFORE the merge is committed — so regressions never
enter git history at all.

Workflow: merge without committing → audit the staged result → fix any losses
in-place → commit one clean merge → create the PR.

## Invocation

```
/i-crpr                  create PR targeting main
/i-crpr <base-branch>    create PR targeting a specific base branch
```

---

## Step 0 — Pre-flight checks

```bash
# Must be on a feature branch
git branch --show-current

# Working tree must be clean before merging
git status --short

# Script must exist
ls scripts/audit_merge_regression.py 2>/dev/null || echo "MISSING"
```

- If on `main` or `<base-branch>`: halt — "Cannot create a PR from this branch."
- If working tree is dirty (uncommitted changes): halt — "Commit or stash your
  changes before running /i-crpr."
- If script missing: warn and note the skip in the PR body, then jump to Step 4.

---

## Step 1 — Check for an in-progress merge

```bash
git rev-parse MERGE_HEAD 2>/dev/null && echo "MERGE_IN_PROGRESS" || echo "CLEAN"
```

- **If `MERGE_IN_PROGRESS`:** a `git merge --no-commit` is already staged.
  Skip to Step 2 — audit what's already there.
- **If `CLEAN`:** proceed to merge now.

---

## Step 2 — Merge without committing

```bash
git fetch origin
git merge --no-commit origin/<base-branch>
```

**Handle merge outcomes:**

- **Auto-merge succeeded (no conflicts):** proceed to Step 3.
- **Conflicts present** (`git status` shows `UU` / `AA` / `DD` files):
  Tell the user:
  ```
  Merge has conflicts that need manual resolution before the audit can run.

  Conflicted files:
    <list from git status>

  Resolve each conflict, then run:
    git add <resolved-files>

  Once all conflicts are staged, re-run /i-crpr to continue the audit.
  ```
  Halt. Do not proceed past unresolved conflicts.
- **Already up to date:** no merge needed. Jump to Step 4 (no audit needed,
  no catch-up merge means no regression risk from this operation).

---

## Step 3 — Audit the pending merge

Run the full `/i-ab` triage process with `--pending` (reads the working tree,
not a commit SHA):

```bash
python3 scripts/audit_merge_regression.py --pending \
  --exclude 'graphify-out/*' \
  --exclude 'log_analysis/*' \
  --exclude '*.ipynb' \
  --exclude '*.csv' \
  --exclude '*.xlsx' \
  --exclude '40pcr/inventory/*' \
  --exclude '40pcr/reports/*' \
  --format text
```

Apply the full triage from `/i-ab` Steps 4–5:
- Check A: substantive (non-whitespace) change on the losing side?
- Check B: tied to a real Jira ticket?
- Check C: working tree still matches the bad side (not already resolved)?

**Performance:** Large merges (1000–2000+ files) take 45–120 s. Run
synchronously and tell the user "Scanning — this can take up to 2 min for
large merges."

If zero confirmed and zero probable findings: output the green-path summary
and proceed directly to Step 3c.

---

## Step 3a — Present and resolve confirmed regressions

For each confirmed regression, show the user what was lost and ask what to do
— **before anything is committed**:

```
─────────────────────────────────────────────────────────
CONFIRMED REGRESSION: path/to/file.py
  Ticket:      GSDL-XXX
  Merge kept:  <kept_ref[:8]> (your branch — stale)
  Lost from:   <discarded_ref[:8]> ("fix: GSDL-XXX …")

  What was discarded:
    [inline diff: git diff <kept_ref> <discarded_ref> -- path/to/file.py]

  Action? [restore / skip / abort]
─────────────────────────────────────────────────────────
```

**`restore`** — overwrite the staged file with the content that was discarded:
```bash
git checkout <discarded_ref> -- path/to/file.py
# (file is now updated in the working tree and staged for the merge commit)
```
No separate commit needed — the fix becomes part of the merge commit itself.

**`skip`** — leave as-is; note the file as "user-skipped" in the PR body.

**`abort`** — abort the merge entirely and stop:
```bash
git merge --abort
```

---

## Step 3b — Re-audit to confirm clean

After all per-file decisions, re-run the audit to verify no confirmed
regressions remain:

```bash
python3 scripts/audit_merge_regression.py --pending \
  --exclude 'graphify-out/*' --exclude 'log_analysis/*' \
  --exclude '*.ipynb' --exclude '*.csv' --exclude '*.xlsx' \
  --exclude '40pcr/inventory/*' --exclude '40pcr/reports/*' \
  --format text
```

If new confirmed regressions appear: repeat Step 3a.

---

## Step 3c — Commit the merge

```bash
git commit --no-edit
```

The default merge commit message is correct. Do not reword it. If files were
restored in Step 3a, append a note to the commit body:

```
Restored before commit (merge regression audit):
  - path/to/file.py  ← GSDL-XXX (discarded_ref[:8])
```

---

## Step 4 — Push the branch

```bash
git push -u origin <current-branch>
```

If push fails (non-fast-forward): halt — "Push failed. Pull or rebase, then
re-run /i-crpr."

---

## Step 5 — Generate the PR description

Follow the `/i-pr` skill format. Add a mandatory audit section:

```markdown
## Merge Regression Audit

Pre-flight audit ran against the staged merge (--pending) before commit.

| Result | Count |
|--------|-------|
| ✅ Confirmed regressions | 0 |
| ✅ Probable (no ticket) | 0 |
| ℹ️ Self-healed (informational) | N |
| 🔇 False positives suppressed | N |
```

If regressions were restored in Step 3a:

```markdown
### Restored In-Place (before merge commit)

| File | Lost From | Ticket |
|------|-----------|--------|
| `path/to/file.py` | `def5678` | GSDL-720 |

Restorations are part of the merge commit — no separate fix commit needed.
```

If findings were skipped:

```markdown
### Skipped Findings (user decision)

| File | Note |
|------|------|
| `path/to/file.py` | Skipped by user — verify manually |
```

---

## Step 6 — Create the PR

```bash
gh pr create \
  --title "<concise title — ≤70 chars>" \
  --base <base-branch> \
  --body "$(cat <<'EOF'
<generated body from Step 5>
EOF
)"
```

Return the PR URL to the user.

---

## Guardrails

- **Working tree must be clean before Step 2.** If dirty, halt and say why.
- **Never run `git checkout <ref> -- <path>` without showing the diff first**
  and getting explicit `restore` confirmation per file.
- **Never `git commit` if unresolved conflicts remain** (`git status` shows `UU`).
- **Never force-push.** If push fails, stop.
- **If the merge was already committed** (no `MERGE_HEAD`, no `--pending` state):
  tell the user to use `/i-ab <merge-sha>` to audit the committed merge instead.
- **`git merge --abort` only on user `abort` response** — never silently abort.
- **If script absent:** warn, skip the audit, note the skip in the PR body,
  and proceed to Step 4.
