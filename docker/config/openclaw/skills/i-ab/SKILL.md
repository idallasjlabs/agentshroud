---
description: "Audit a merge commit for silently-discarded changes — the GSDL-715/720 failure mode where conflict resolution keeps stale branch content and reverts already-landed fixes. Use after git merge origin/main to triage raw flags into confirmed regressions, false positives, and self-healed findings before anything reaches git history. Standalone audit tool; /i-crpr orchestrates this automatically as part of PR creation."
---

# Skill: Audit Branch (AB) — Merge Regression Detection

## Role

You are a Merge Safety Engineer for the GSDE&G team. Your job is to detect
merge conflict resolutions that silently discarded already-landed code — the
exact failure mode behind GSDL-715 and GSDL-720.

**Critical discipline:** Raw script output has a high false-positive rate. A
74-merge historical sweep of this repo showed most flags were generated/noise
files, "good direction" flags (main's newer fix correctly overwrote the stale
branch — the desired outcome), or self-healed (later commits already fixed
it). Never surface a raw finding without triage.

## Invocation Forms

```
/i-ab                        audit HEAD (must be a merge commit)
/i-ab <sha>                  audit a specific merge commit
/i-ab --pending              audit an in-progress merge (post `git merge --no-commit`, pre-commit)
```

---

## Step 1 — Verify the script exists

```bash
ls scripts/audit_merge_regression.py 2>/dev/null || echo "MISSING"
```

If missing: halt. Tell the user this script lives in the services-data-lake
repo and must be present for this skill to work.

---

## Step 2 — Determine the target

- **`/i-ab`** → `merge_commit = HEAD`; verify it is actually a merge commit:
  ```bash
  git rev-list --parents -n 1 HEAD | awk '{print NF-1}'
  ```
  If result is not `2`: halt, tell user HEAD is not a merge commit, suggest
  `git log --merges -5 --oneline` to find a valid target.

- **`/i-ab <sha>`** → `merge_commit = <sha>`
- **`/i-ab --pending`** → use `--pending` flag; verify `MERGE_HEAD` exists:
  ```bash
  git rev-parse MERGE_HEAD 2>/dev/null || echo "NO_MERGE_IN_PROGRESS"
  ```

---

## Step 3 — Run the audit script

Use the standard excludes that match CI (`.github/workflows/merge-regression-audit.yml`):

```bash
python3 scripts/audit_merge_regression.py [<merge_commit> | --pending] \
  --exclude 'graphify-out/*' \
  --exclude 'log_analysis/*' \
  --exclude '*.ipynb' \
  --exclude '*.csv' \
  --exclude '*.xlsx' \
  --exclude '40pcr/inventory/*' \
  --exclude '40pcr/reports/*' \
  --format text
```

**Performance note:** Merges with 1000–2000+ diverged files take 45–120 s.
This is normal. Do not background or kill the process — run it synchronously
and wait. Report "Scanning <N> files…" to the user while it runs.

If exit code is 0 (no raw findings): output "✅ No suspicious files found."
and stop — no triage needed.

Parse every `SUSPECT:` block from the output. Extract:
- `path` — the flagged file path
- `kept_ref` — the commit whose content the merge kept (8-char SHA)
- `discarded_ref` — the commit whose independent changes were dropped

---

## Step 4 — Triage each finding

Run all three checks. A finding is only **confirmed** if it passes A, B, and C.

### Check A — Substantive change on the losing side?

```bash
# Get the merge-base
base=$(git merge-base <kept_ref> <discarded_ref>)

# Diff: what did the discarded side actually change?
git diff $base <discarded_ref> -- <path>
```

**FALSE_POSITIVE** (stop triage) if the diff is:
- Whitespace-only (blank lines, trailing spaces, indentation)
- Comment-only (no logic change)
- A generated/auto-managed file pattern: `*.lock`, `*.min.js`, `*.pyc`,
  `__pycache__/`, `migrations/` (auto-generated), `graphify-out/`,
  `log_analysis/`, `*.ipynb` output cells, `*.csv`, `*.xlsx`

### Check B — Tied to a real ticket?

```bash
git log $base..<discarded_ref> -- <path> --oneline
```

Look for Jira refs in commit messages: `GSDL-\d+`, `GSDE-\d+`, `SORT-\d+`,
`GSDEA-\d+`, `FOD-\d+`. If found → ticket-linked. If not → mark
`LOW_CONFIDENCE` (still report, but note no ticket found).

### Check C — Still broken at HEAD (not self-healed)?

```bash
result_at_head=$(git rev-parse HEAD:<path> 2>/dev/null)
result_at_kept=$(git rev-parse <kept_ref>:<path> 2>/dev/null)
```

If `result_at_head == result_at_kept`: HEAD still matches the "bad" side →
**not yet healed**.

If `result_at_head != result_at_kept` AND `result_at_head != result_at_discarded`:
HEAD has diverged further → **UNKNOWN** (requires manual inspection).

If `result_at_head == result_at_discarded`: fully self-healed → **SELF_HEALED**.

---

## Step 5 — Classify findings

| Class | Criteria |
|-------|----------|
| **CONFIRMED** | Passes A (substantive) + B (ticket) + C (still broken) |
| **PROBABLE** | Passes A + C, no ticket reference found |
| **SELF_HEALED** | Passes A + B but fails C (already fixed at HEAD) |
| **FALSE_POSITIVE** | Fails A (no substantive change on losing side) |
| **GOOD_DIRECTION** | The kept side is demonstrably newer/better (document and suppress) |

---

## Step 6 — Output the report

```
## Merge Regression Audit — <sha[:8]>  (<branch>)

Audited: <N> files diverged | <M> raw flags | triage complete

---

### ✅ Confirmed Regressions  (action required)

| File | Merge kept | Changes lost from | Ticket | HEAD state |
|------|-----------|-------------------|--------|------------|
| `path/to/file.py` | `abc1234` (branch) | `def5678` (main) | GSDL-720 | Still broken |

Remediation for each confirmed regression:
  git show <discarded_ref> -- <path>        # review what was lost
  git checkout <discarded_ref> -- <path>    # restore (requires confirmation)
  git diff HEAD <path>                      # verify restoration

---

### ⚠️ Probable Regressions  (no ticket — verify manually)

| File | Merge kept | Changes lost from | Note |
|------|-----------|-------------------|------|
| `path/to/file.py` | ... | ... | No Jira ref in commit history |

---

### ℹ️ Self-Healed  (already fixed, informational only)

These were flagged but HEAD no longer matches the kept side:
  - `path/to/other.py`  — healed in <sha> ("fix: GSDL-XXX …")

---

### Suppressed false positives
<N> flags suppressed: <a> whitespace-only, <b> generated files, <c> noise
```

If zero confirmed + zero probable: output the green-path summary:

```
## ✅ Merge Regression Audit — CLEAN

<N> files diverged, <M> raw flags, all suppressed after triage.
  - <a> false positives (whitespace / generated)
  - <b> self-healed (already fixed at HEAD)
  - <c> good-direction (main's newer fix was correctly kept)

No action required.
```

---

## Jira / PR Comment Format

If the user says "post to Jira" or "format for PR comment":

```markdown
**Merge Regression Audit** — `<sha[:8]>` (`<branch>` → `main`)

| Result | Count |
|--------|-------|
| ✅ Confirmed regressions | N |
| ⚠️ Probable (no ticket) | N |
| ℹ️ Self-healed | N |
| 🔇 False positives suppressed | N |

[Confirmed/probable table here if N > 0]

Audit: `python3 scripts/audit_merge_regression.py <sha>`
CI gate: `.github/workflows/merge-regression-audit.yml`
Refs: GSDL-715, GSDL-720
```

---

## Guardrails

- **Never run `git checkout <ref> -- <path>` in this skill.** Report only.
  Restorations belong in `/i-crpr`.
- **Never surface raw script output without triage.** Every finding must pass
  through Steps 4–5 before appearing in the report.
- **If the script takes >2 min:** tell the user the count of files being
  checked and that large merges are expected to take up to 2 minutes.
- **If the audit script is absent from the repo:** halt immediately and
  explain — do not attempt to recreate it.
