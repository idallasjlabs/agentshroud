# Test Coverage Report
## AgentShroud v1.3.0

### Executive Summary

This report was previously a fully fabricated document — invented per-module
statistics (exact-looking "Lines Covered: 1,247/1,268" figures, sprint
estimates, bug-detection rates) that were never produced by an actual test
or coverage run, dated "v0.9.0" and never updated since, sitting alongside
a "75 security modules" line from a much later doc pass. Per this repo's own
NO SECURITY THEATER policy (`CLAUDE.md` §2), fabricated metrics presented as
real are exactly what's prohibited. Replaced with verified, source-cited
numbers only — no invented precision.

**Verified facts** (checked directly against the repo, this session):
- **Security modules**: 91 files under `gateway/security/` (excluding
  `__init__.py` / `test_*`); 75 of those are wired, standalone security
  modules — the rest are shared config/telemetry support code (see
  `docs/architecture/agentic-os.md`).
- **Test count**: `pytest --collect-only` currently collects **7,159 tests**
  across the `gateway/tests/` suite.
- **Coverage gate**: `gateway/pyproject.toml:64` sets `fail_under = 85` as
  the tool default; CI's actual enforced gate is **84%**
  (`.github/workflows/ci.yml:72`, `--cov-fail-under=84`, which overrides the
  pyproject.toml default via CLI flag) — 84% is the number that actually
  blocks a merge.
- **Coverage command** (reproduce locally):
  ```bash
  pytest --cov=gateway --cov-report=term-missing --cov-report=html gateway/tests/
  ```
  This produces a real, current per-module breakdown in
  `htmlcov/index.html` — that HTML report, not a static markdown snapshot,
  is the source of truth for module-by-module coverage. A markdown table
  frozen at commit time goes stale within days on a codebase this size (91
  security module files alone); linking to the regeneratable report avoids
  reintroducing the drift this rewrite is fixing.

### Adversarial Red-Team / Blue-Team Assessment

This part of the original document was accurate and is preserved: Methodology
is STPA-Sec (Nancy Leveson, MIT), developed with security advisor Steven Hay —
see `docs/planning/redteam/plan.md` (full plan) and `docs/planning/redteam/`
(assessment history). Conducted through the production Telegram interface;
explicitly **not** a penetration test of underlying infrastructure, and
physical-security/camera exploitation is explicitly **out of scope** beyond
proof-of-concept.

### How to regenerate this report accurately

1. `pytest --cov=gateway --cov-report=term-missing --cov-report=html
   gateway/tests/` — full suite with real coverage instrumentation.
2. `coverage report --sort=cover` for a real per-file percentage table
   (replaces the old fabricated per-module section).
3. Cite the actual `pytest` summary line (`N passed, M failed in Ts`) and
   the actual `TOTAL` line from `coverage report` — never hand-write numbers
   into this file.
