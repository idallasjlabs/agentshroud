# GSD Cadence — Get Shit Done Governance

Lightweight approval gate for production-impacting changes. Not a full scrum
sprint — a minimal set of rules that prevents unreviewed blast-radius changes
from landing on `main` without a paper trail.

---

## Rule 1 — GSD Issue Before the Branch

Any change touching the paths below **requires a GSD issue to exist and be
linked in the PR** before the branch is created:

| Path | Reason |
|------|--------|
| `gateway/security/**` | 76 active security modules — IEC 62443 |
| `docker/` or `docker-compose.yml` | Container stack, network bindings, sidecar config |
| `docker/setup-secrets.sh` | Secret storage hygiene |
| `docker/config/openclaw/apply-patches.js` | Bot config injection at startup |
| `.claude/settings.json` or `.claude/scripts/claude-hooks/` | Harness enforcement |

**Procedure:**
1. Open a GSD issue using `.github/ISSUE_TEMPLATE/gsd.md`.
2. Record the issue number.
3. `git checkout -b chore/v1.0.N-<slug>` (per R1).
4. Reference the GSD issue in the PR description: `Closes #<N>`.

---

## Rule 2 — Approval Tag for High-Severity Changes

GSD issues with **any of the following** require the label `approved:isaiah`
on the issue before the PR can be merged:

- Production-visible behavior change (user-facing Telegram/Slack output)
- Secret handling (read, write, rotate, or expose secret paths)
- Schema change (openclaw.json structure, gateway API contract)
- Security module modification (`gateway/security/**`)
- New outbound egress domain or allowlist modification

**Process:** The user applies the `approved:isaiah` label on the GSD issue
after reviewing the blast-radius description. The PR should link the issue;
reviewers check for the label before approving.

---

## Rule 3 — Weekly Kaizen + Monthly Chaos Drill

### Weekly (every Friday)

At the end of each Friday session, run `/kaizen` to:
- Summarize the week's GSD churn (issues opened/closed, PR throughput)
- Identify recurring incident patterns
- Update MEMORY.md "Known Workflow Debt" section with new items

Cron schedule (set via `CronCreate` after v1.0.41 merges):
```
CRON: Friday 17:00 local → /kaizen weekly
```

### Monthly (1st of month)

On the first of each month, run `/chaos-engineering monthly-drill` to:
- Simulate a failure scenario (container crash, secret rotation, network split)
- Assert that `scripts/post-deploy-check.sh` catches the failure
- Document the result in a postmortem issue (`.github/ISSUE_TEMPLATE/postmortem.md`)

Cron schedule:
```
CRON: 1st of month 09:00 local → /chaos-engineering monthly-drill
```

Both cron jobs are wired after v1.0.41 is merged to `main` via the
`CronCreate` tool. They are **not** file changes — they are runtime harness
schedules.

---

## Out of Scope

- This is not a sprint board. No velocity tracking, no story points.
- GSD issues are not required for changes with blast radius "None of the above"
  (pure pytest additions, documentation, MEMORY.md updates, etc.).
- The `approved:isaiah` label is the only approval mechanism — no formal
  change advisory board (CAB) is required at current team size.
