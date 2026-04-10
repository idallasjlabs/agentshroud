# Test Strategy

Decision matrix for choosing the right test type for each change category.
When in doubt, follow the rule: **test at the layer closest to the failure**.

---

## Test-Type Decision Matrix

| Change category | Test type | Location | Runner | CI gate? |
|----------------|-----------|----------|--------|----------|
| Application logic (Python) | pytest unit / integration | `gateway/tests/` | `pytest -q` | Yes — `test` job |
| New security module | pytest + IEC 62443 FR reference | `gateway/tests/test_<module>.py` | `pytest -q` | Yes — `test` job |
| Shell entry scripts (`start-agentshroud.sh`, etc.) | Static grep assertion | `tests/startup_smoke/test_bot_boot_static.sh` | `bash` | Yes — `smoke-static` job |
| JS config patches (`apply-patches.js`) | Node functional assertion | `tests/startup_smoke/test_apply_patches.js` | `node` | Yes — `smoke-static` job |
| Secret storage (`setup-secrets.sh`) | Byte-for-byte shell assertion | `tests/startup_smoke/test_setup_secrets.sh` | `bash` | Yes — `smoke-static` job |
| Docker assembly (Dockerfile, compose) | Live rebuild + health check | `tests/startup_smoke/test_bot_boot_live.sh` | `bash` (requires `SMOKE_LIVE=1`) | Self-hosted runner only |
| Data transformation (pipeline) | Data validation output | Stage 1/2 checks, schema verification | `scripts/validate_*` | No (manual) |
| Browser / UI | Browser automation | `.claude/skills/browser/` | Playwright | No (manual) |
| Chaos / failure scenarios | Monthly chaos drill | `/chaos-engineering monthly-drill` | Manual + `CronCreate` | No (monthly) |

---

## Coverage Thresholds

| Layer | Threshold | Enforced by |
|-------|-----------|-------------|
| Python (`gateway/`) | ≥ 94% | `pytest --cov=gateway` in CI |
| Shell / JS (startup_smoke) | 100% of known bugs have a regression assertion | PR checklist |

---

## When to Add a Smoke Assertion

**Add to `tests/startup_smoke/` whenever:**
- A bug is found in the container assembly layer (Dockerfile, entry scripts,
  JS patches, compose file, secret scripts).
- A fix touches `docker/scripts/`, `docker/config/openclaw/apply-patches.js`,
  `docker/setup-secrets.sh`, or `docker/docker-compose.yml`.
- The fix would not be caught by existing pytest tests (i.e., the failure
  manifests at runtime, not in Python unit logic).

**Assertion target:** the most specific grep/structural check that would have
caught the bug. Prefer `grep -q` on the source file (static, runs anywhere)
over live Docker assertions (requires Colima VM).

---

## Incident → Test Backfill Rule (R3 extension)

Every incident that produces a postmortem (`.github/ISSUE_TEMPLATE/postmortem.md`)
**must** include a "test added to prevent recurrence" field. The test is
added in the same PR as the fix — not deferred.

**Historical bug → smoke assertion mapping:**

| Bug | Assertion | Added in |
|-----|-----------|---------|
| ARM64 V8 stack overflow | S1: `--stack-size=65536` in `start-agentshroud.sh` | v1.0.38 |
| Telegram photo download via wrong apiRoot | A1/S2: `channels.telegram.apiRoot` set | v1.0.39 |
| Slack `invalid_auth` with empty tokens | A3–A5/S3: `xoxb-`/`xapp-` prefix guard | v1.0.39 |
| Stale Slack block on restart | A6/S7: `delete config.channels.slack` when no tokens | v1.0.40 |
| `read_secret_masked` stdout pollution | S6: `> /dev/tty` routing | v1.0.39 |
| Dockerfile COPY path drift | S4: COPY from `docker/config/openclaw/` | v1.0.39 |
| Gateway binding on 0.0.0.0 | S5: no `0.0.0.0:8080` in compose | v1.0.39 |

---

## Running Tests Locally

```bash
# Full test suite (Python)
pytest -q

# Static smoke (no Docker required — runs in CI)
bash tests/startup_smoke/test_bot_boot_static.sh
node tests/startup_smoke/test_apply_patches.js

# All static smoke via runner
bash scripts/smoke.sh

# Live smoke (requires Colima + asb rebuild)
SMOKE_LIVE=1 bash scripts/smoke.sh

# Post-deploy health gate (after asb up/rebuild)
bash scripts/post-deploy-check.sh
```
