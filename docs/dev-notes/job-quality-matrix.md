# Job Quality Matrix — local-model report/newsletter jobs (Mission 1)

Working doc on the dev branch (per 2026-08-29 dev-mission brief). Owner policy:
prompts and pipeline robustness are the fix path — never switch jobs to cloud
models. Newsletter/email jobs run on DEV until fixed (owner direction
2026-08-31); prod stays clean for productive use.

## Failure classes (prod investigation handover, 2026-08-31)

| # | Class | Symptom | Required behavior |
|---|-------|---------|-------------------|
| 1 | Search backend unreachable | searxng-local loses its `agentshroud-isolated` attachment when recreated (image bump 2026.8.29-d226b78bc drops it); Hermes web_search fails everything; newsletter emails an empty "nothing new" shell | HARD-FAIL the run when search is down — never email an empty shell. Fix attachment at searxng launch (not only at Hermes recreate); fix run-standalone.sh's misleading "not running, or already connected" warning |
| 2 | Memory-pressure garbling | Host swap thrash (30GB+ swap) → local model emits near-empty/garbled output (thin Aug 28–29 emails; Aug 28 Mac Clustering run failed) | Validate output length/shape BEFORE the email/delivery step; retry once; else fail loudly. Assume pressure recurs; stagger model loads (shared-host finding) |
| 3 | Local model call hangs | `TimeoutError: Cron job idle for 600s — waiting for non-streaming API response` (known local-backend hang family; see llm_proxy response.read() saga in project memory) | Streaming responses, or shorter per-search generations so no single call approaches the idle limit |

Quality bar: the July competitive-intel report format (cross-referenced, VERIFIED-labeled) — mine that pipeline for its differences.

## Related delivery-layer defects (separate from model quality)

- Telegram links stripped: gateway ToolResultSanitizer (enforce mode) collapses
  non-allowlisted markdown links to bare anchor text ("Full Story" dead text);
  policy decision pending with owner — proposal: `warn` mode for no-agent
  script-job deliveries, enforce for LLM output.
- Text corruption in delivery wrapper: `job_id: f$*`, garbled Daily Brief
  filename (`m֭khuƬZM-08-31`) — encoding/templating defect, uninvestigated.
- Hermes cron wrapper spams one message per mini-batch with full boilerplate;
  should batch digests.

## Per-job verdicts

| Job | Owner env | Model | Verdict | Notes |
|-----|-----------|-------|---------|-------|
| Breaking AI News | prod (script-only since 2026-08-30) | none (no-agent) | n/a — delivery-layer issues only | links stripped + wrapper spam, see above |
| Daily Brief | prod (script-only) | none | n/a | garbled filename in output |
| Collaborator Report (Morning/Evening) | dev | ollama/qwen3:14b | BLOCKED — ollama not running on dev account, no models pulled | pull in progress |
| Collaborator Daily Digest | dev | ollama/qwen3:14b | BLOCKED — same; prompt cleaned of denial-suppression clause 2026-08-29 | |
| Daily CVE Triage & Remediation Scan | dev | ollama/qwen3:14b | BLOCKED — same | scan-side :latest-tag bug partially fixed (hermes image still :latest) |
| Newsletter/email jobs (Hermes) | dev (moved from prod 2026-08-31) | nemotron/gemma via LM Studio | NEEDS-WORK — classes 1–3 above | golden-baseline loop not started |

## Env-split note (prod FYI, for init-config.sh work)

Prod boot pause-pass left 9 non-keep jobs ACTIVE after 2026-08-30 boots
(ordering vs seeding? keep-list quoting?) — root-cause in init-config.sh
env-split section. Prod force-paused manually to the 5-job keep list.
