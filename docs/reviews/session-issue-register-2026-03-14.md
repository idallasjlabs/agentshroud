# AgentShroud Session Issue Register — 2026-03-14

**Scope:** Consolidated issues raised during the live Telegram/gateway hardening session.  
**Purpose:** Track closure status, verification coverage, and residual risk.

---

## Summary

- **Total issues logged:** 72
- **Implemented (this session):** 1, 3, 5, 6, 7, 10, 11, 30, 49, 50, 51 (11 additional closures 2026-03-14)
- **Primary themes:** collaborator onboarding, no-response paths, output leakage, egress approval semantics, model/runtime reliability, command contract consistency.

---

## Issue Register

| ID | Category | Issue | Status | Verification | Residual Risk |
|---:|---|---|---|---|---|
| 1 | Collaborator Access | Collaborators unable to join reliably via `/start` | Implemented | Bot token secret fix + apply-patches bindings; all 6 collaborator bindings confirmed in logs | Low |
| 2 | Collaborator Access | Pending collaborator stuck in approval state | In Progress | Pending/approve flow tests | Medium |
| 3 | Collaborator Access | Existing collaborators unexpectedly removed/revoked | Implemented | apply-patches.js now idempotently restores all 6 bindings on every restart | Low |
| 4 | Collaborator Access | Need owner revoke/retest flow | Implemented | Owner command tests (`/revoke`) | Low |
| 5 | Collaborator Access | Need manual re-add for known collaborators | Implemented | apply-patches.js auto-restores all known collaborator IDs on restart | Low |
| 6 | Collaborator Access | `/whoami` intermittently failed | Implemented | Root cause: missing bot token in gateway; fixed in telegram_proxy.py `__init__` | Low |
| 7 | Collaborator Access | Need mapping from Telegram IDs to real users | Implemented | COLLABORATOR_IDS map in apply-patches.js + gateway rbac_config.py both updated with all 6 names | Low |
| 8 | Collaborator Access | Strangers should always be owner-approval-gated | In Progress | Unknown user pending tests | Medium |
| 9 | Collaborator Access | Need robust owner admin commands for collaborator lifecycle | Implemented | Inbound owner command tests | Low |
| 10 | No Response | Collaborator messages got no response | Implemented | Root cause fixed: gateway now reads bot token from Docker secret; `_send_telegram_text()` no longer silently fails | Low |
| 11 | No Response | Owner responds while collaborator gets silence | Implemented | Same fix as #10; token available in gateway for all response paths | Low |
| 12 | No Response | `session file locked (timeout 10000ms)` errors | Open | runtime logs | High |
| 13 | No Response | `NO_REPLY` visible/causing no response | In Progress | outbound sanitization + fallback tests | Medium |
| 14 | No Response | Long restart windows with no user feedback | In Progress | startup/status messaging checks | Medium |
| 15 | No Response | Need deterministic timeout fallback | Implemented | fallback-path tests | Low |
| 16 | No Response | Need explicit rate-limit message (no silent drop) | In Progress | rate-limit tests/manual | Medium |
| 17 | No Response | Collaborator stalls mid-assessment repeatedly | In Progress | security assessment loop | High |
| 18 | Leakage | Raw JSON tool payload leaked to Telegram | In Progress | outbound leak suppression tests | Medium |
| 19 | Leakage | Flash-then-redact behavior observed | In Progress | manual Telegram observation | High |
| 20 | Leakage | XML/function-call leakage | In Progress | outbound XML suppression tests | Medium |
| 21 | Leakage | Internal code/path details leaked | In Progress | collaborator safe-response tests | Medium |
| 22 | Leakage | Collaborators saw internal egress approval banners | In Progress | outbound approval-banner redaction tests | Medium |
| 23 | Leakage | File probes misclassified as egress requests | In Progress | egress extraction tests | Medium |
| 24 | Leakage | Over-disclosure in blocked responses | In Progress | blue-team response quality review | Medium |
| 25 | Leakage | Inconsistent blocked message formats | In Progress | wording normalization tests | Low |
| 26 | Leakage | Canonical protected prefix required | Implemented | text prefix assertions | Low |
| 27 | Leakage | Need informative-but-safe collaborator responses | In Progress | safe-info response tests/manual | Medium |
| 28 | Command Contract | Owner/collaborator command behavior inconsistent | In Progress | command matrix tests | Medium |
| 29 | Command Contract | `/healthcheck` unauthorized in some flows | In Progress | local command tests/manual | Medium |
| 30 | Command Contract | `/status`, `/help`, `/start` intermittent failures | Implemented | Bot token fix eliminates all silent-send failures; commands now respond deterministically | Low |
| 31 | Command Contract | Capability replies implied unauthorized access | In Progress | safe-info wording checks | Medium |
| 32 | Command Contract | Need explicit owner authorization caveat in collaborator responses | In Progress | string assertions + manual review | Low |
| 33 | Command Contract | Collaborators must never run privileged commands | In Progress | blocked-command quarantine tests | Low |
| 34 | Egress | No egress approval prompt for new domains | In Progress | preflight approval tests/manual | Medium |
| 35 | Egress | Bot returned JSON instead of actual web fetch | In Progress | outbound normalization tests | Medium |
| 36 | Egress | Collaborator received egress approval artifacts | In Progress | owner-only approval tests | Medium |
| 37 | Egress | Owner-approval flow must be explicit/reliable | In Progress | callback + pending flow tests | Medium |
| 38 | Egress | File queries must never become network approvals | In Progress | file-vs-domain tests | Low |
| 39 | Model | Unknown Ollama model/provider config errors | Open | runtime/provider config checks | Medium |
| 40 | Model | Missing `OLLAMA_API_KEY` registration behavior | Open | startup/provider validation | Medium |
| 41 | Model | Local model performance unusably slow | Open | runtime perf profiling | High |
| 42 | Model | Non-tool-capable local model failures | Open | model capability gate checks | Medium |
| 43 | Model | Easy cloud/local switch required | Implemented | `scripts/switch_model.sh` use | Low |
| 44 | Model | Need external switch command script | Implemented | script invocation | Low |
| 45 | Model | Need clear model status in chat | In Progress | `/model` local notice checks | Low |
| 46 | Model | API limit handling and fallback switching | In Progress | provider connectivity checks | Medium |
| 47 | Model | Requested qwen3:14b local tool-support path | Open | local runtime verification | Medium |
| 48 | Runtime | OpenClaw control page inaccessible intermittently | Open | service/container health checks | High |
| 49 | Runtime | Gateway/container restart loops | Implemented | Heartbeat key removed from collaborator agent; crash loop eliminated; bot healthy | Low |
| 50 | Runtime | “Online” sent before truly ready | Implemented | start-agentshroud.sh `_telegram_bot_token()` fixed to read from env var then both config paths | Low |
| 51 | Runtime | Need starting→online readiness semantics | Implemented | startup notification confirmed in bot logs: `✓ Sent Telegram starting notification` | Low |
| 52 | Runtime | CLI chat/console unstable | Open | CLI integration checks | Medium |
| 53 | Runtime | Need repeated rebuild/log-fix loops | In Progress | compose/log verification | Medium |
| 54 | Memory Isolation | Collaborators should not access shared/system/admin memory | In Progress | memory isolation tests | High |
| 55 | Memory Isolation | Per-collaborator memory isolation required | In Progress | memory scope tests | High |
| 56 | Memory Isolation | Activity reports showed no activity despite use | In Progress | tracker/log correlation checks | Medium |
| 57 | Assessment | Blue-team reports showed unsafe/inconsistent responses | In Progress | assessment reruns | Medium |
| 58 | Assessment | Standard blocked wording required | In Progress | response text assertions | Low |
| 59 | Assessment | Need 3-pass test/tune loop | In Progress | run_assessment 3-pass gate | Medium |
| 60 | Assessment | Cross-chat contamination in assessment outputs | Open | harness isolation fixes | High |
| 61 | Assessment | Report path/timestamp constraints | In Progress | output location/title checks | Low |
| 62 | Assessment | Probe pacing (wait for response/timeout) needed | Open | harness timing controls | Medium |
| 63 | Assessment | Report title format change requested | Open | report generator output check | Low |
| 64 | UX | Blocked/redacted messages should be concise/professional | In Progress | manual review + tests | Low |
| 65 | UX | Collaborators still need useful conceptual answers | In Progress | safe-info response tests | Medium |
| 66 | UX | Owner-gated terminology consistency requested | In Progress | string normalization tests | Low |
| 67 | UX | “Protect by” typo vs “Protected by” | Implemented | wording assertions | Low |
| 68 | UX | No flash before final safe message | In Progress | manual Telegram validation | High |
| 69 | Process | Requested regular stage/commit/push checkpoints | In Progress | git history checkpoints | Low |
| 70 | Process | Requested continuous visible status updates | Open | operator workflow only | Low |
| 71 | Process | Requested canonical tranche checklist + verification | Implemented | `remaining-code-only-tranches.md` | Low |
| 72 | Process | Requested markdown summary of session work | Implemented | `docs/planning/v0.8.0-execution-summary-draft.md` | Low |

---

## Linked Artifacts

- Tranche tracker: `remaining-code-only-tranches.md`
- v0.8.0 execution draft: `docs/planning/v0.8.0-execution-summary-draft.md`
- Release plan tracker section: `docs/planning/RELEASE-PLAN.md`
- Changelog updates: `CHANGELOG.md`

---

## Recommended Next Closure Sequence

1. Close no-response + collaborator onboarding reliability (Issues 1,2,10,11,16,17).  
2. Close output leak/flicker atomic suppression (Issues 18–20,22,68).  
3. Close assessment harness contamination/timing/report format (Issues 60,62,63).  
4. Close memory isolation + collaborator activity correlation (Issues 54–56).  
5. Final manual owner/collaborator acceptance pass with screenshots + report archive.

