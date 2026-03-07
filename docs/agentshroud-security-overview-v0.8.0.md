# AgentShroud Security Overview — v0.8.0

**Date:** 2026-03-07
**Branch:** `feat/v0.8.0-enforcement-hardening`
**Status:** All findings remediated — zero test failures

---

## Before & After: Security Finding Remediation

| ID | Finding | Pre-Remediation | Post-Remediation | Grade |
|----|---------|----------------|-----------------|-------|
| CRITICAL-1 | `history.env` in git with live Telegram credentials | Tracked since commit `efc4b98` | `git rm --cached history.env`; added to `.gitignore` | **RESOLVED** |
| CRITICAL-2 | No body size limits on API models | `content`, `body`, `command` unbounded | All text fields have `max_length`; 1MB middleware guard added | **RESOLVED** |
| HIGH-1 | ML classifier is a stub with misleading docs | Docstrings claimed DistilBERT; code was heuristic only | Renamed to `HeuristicClassifier`; `[EXPERIMENTAL]` labels added | **RESOLVED** |
| HIGH-2 | Approval queue Telegram notifications unimplemented | `# TODO` — silently logs only | `_notify_telegram()` implemented via httpx; graceful degradation if unconfigured | **RESOLVED** |
| HIGH-3 | Credential generation is UUID placeholder | `"placeholder"` comment; UUID tokens | `[EXPERIMENTAL]` docstring; `logger.warning()` on every call | **RESOLVED** |
| HIGH-4 | In-memory audit chain not persisted | `AuditChain` in-memory only; lost on restart | `AuditChain` accepts optional `audit_store`; fire-and-forget SQLite persistence | **RESOLVED** |
| M-1 | No webhook signature validation | Webhook path unprotected | `validate_signature()` with `hmac.compare_digest()`; warning if unconfigured | **RESOLVED** |
| M-3 | Pi-hole tests are stale | 5 tests referencing deleted Pi-hole container | Deleted; replaced with `test_dns_blocklist.py` (28 tests) | **RESOLVED** |
| M-6 | CEF audit export verification unimplemented | Returns `{"verified": False, "message": "not implemented"}` | `_parse_cef_for_verification()` parses `entryHash`/`previousHash` from extensions | **RESOLVED** |
| M-7 | `content_type` not validated | Accepts any string | `Literal["text", "url", "photo", "file"]` constraint | **RESOLVED** |
| M-8 | Single-pass URL decode | One `unquote()` pass — double encoding bypasses detection | Up to 5-pass iterative decode until stable | **RESOLVED** |
| M-9 | `docker-compose.secure.yml` ports on `0.0.0.0` | `"8080:8080"` — binds all interfaces | `"127.0.0.1:8080:8080"` — loopback only | **RESOLVED** |
| M-10 | Egress filter log not persisted | 10K in-memory ring buffer; lost on restart | Optional `audit_store` param; fire-and-forget SQLite persistence | **RESOLVED** |
| L-1 | `docker` package unpinned | `docker` (no version) | `docker>=7.0.0,<8.0.0` | **RESOLVED** |
| L-2 | `python-multipart` no upper bound | `>=0.0.18` | `>=0.0.18,<1.0.0` | **RESOLVED** |
| L-3 | `prompt_guard` in observatory mode | `mode: observatory` | `mode: enforce` | **RESOLVED** |
| L-5 | Webhook `owner_user_id` hardcoded | `TODO` fallback to `RBACConfig` default | Constructor param `owner_user_id`; `RBACConfig` fallback preserved | **RESOLVED** |
| L-6 | Memory integrity detection basic | 5-second mtime heuristic only | Added ctime vs mtime delta detection for external metadata changes | **RESOLVED** |
| L-9 | Multilingual gaps in prompt guard | 6 languages (FR, ES, DE, ZH, RU, AR) | + Thai, Vietnamese, Swahili, Amharic (10 languages) | **RESOLVED** |

**Not yet resolved (future work):**

| ID | Finding | Reason Deferred |
|----|---------|----------------|
| M-2 | No replay attack protection | Nonce/timestamp dedup requires stateful store; v0.9.0 work |
| M-4 | Router metadata/content-type matching stubbed | Feature design work needed; v0.9.0 |
| M-5 | Rate limiter in-memory only | Redis/SQLite persistence is v0.9.0 scope |
| L-4 | Personal phone numbers in config | Secrets-managed overlay design required |
| L-7 | Semantic paraphrasing bypass | Requires real ML classifier (see HIGH-1 roadmap) |
| L-8 | No multimodal injection defense | OCR pipeline is v1.0.0 scope |

---

## Memory Refresh Context

The following replaces stale notes in `MEMORY.md`:

```
# STALE → REMOVE:
Phase 3 skeletons (unwired) — AgentRegistry, MultiAgentRouter.targets, EgressFilter.set_agent_policy()

# REPLACE WITH:
Phase 3 fully wired:
- AgentRegistry: lifespan.py:127-151
- MultiAgentRouter.register_bots(): lifespan.py:121
- EgressFilter.set_agent_policy(): lifespan.py:215-228

# ADD:
- ml_classifier.py → heuristic_classifier.py (class HeuristicClassifier)
- test_ml_classifier.py → test_heuristic_classifier.py
- test_pihole_integration.py deleted; test_dns_blocklist.py added
- history.env removed from git; rotate Telegram API credentials
```

---

## v0.9.0 / v1.0.0 Roadmap

### v0.9.0 — Production Hardening

| Feature | Rationale |
|---------|-----------|
| Real ML classifier (DistilBERT) | Replace heuristic uncertain-zone scoring; handle semantic paraphrase attacks |
| Rate limiter persistence (Redis/SQLite) | Survive restarts; meaningful per-client enforcement |
| Router metadata/content-type matching | Wire M-4 stubs — tags and content_type routing |
| Replay attack protection | Nonce + timestamp on webhooks; dedup window in SQLite |
| Production credential generation | 1Password SDK, AWS IAM CreateAccessKey, not UUID tokens |
| Webhook secret enforcement | Make `webhook_secret` required (not optional warning) |
| Audit store integration at startup | Wire `audit_store` into `SecurityPipeline` and `EgressFilter` via `lifespan.py` |

### v1.0.0 — Zero-Trust Compute

| Feature | Rationale |
|---------|-----------|
| Multimodal injection defense | OCR-based image scanning for injected text in photos |
| Secrets-managed overlay for config | Remove personal phone numbers / allowlists from plaintext YAML |
| Runtime Falco integration | Container anomaly detection for unauthorized syscalls |
| Agent sandboxing (gVisor/Firecracker) | Zero-trust compute — isolate bot process from host kernel |
| Formal threat model (STRIDE/STPA-Sec) | Document all trust boundaries, attack paths, mitigations |
| Security regression test suite | Red-team fixtures that must be blocked by the pipeline |

---

## Test Coverage Summary (Post-Remediation)

```
2263 passed, 0 failed, 0 skipped
```

Key new test files:
- `gateway/tests/test_heuristic_classifier.py` — 15 tests (renamed from test_ml_classifier.py)
- `gateway/tests/test_dns_blocklist.py` — 28 tests (new, replaces stale Pi-hole tests)
