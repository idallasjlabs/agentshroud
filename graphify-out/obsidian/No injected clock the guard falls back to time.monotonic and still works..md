---
source_file: "gateway/tests/test_rate_limit_guard.py"
type: "rationale"
community: "CI/CD Pipeline Advisor (SKILL)"
location: "L209"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/CI/CD_Pipeline_Advisor_SKILL
---

# No injected clock: the guard falls back to time.monotonic and still works.

## Connections
- [[test_default_clock_is_monotonic()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/CI/CD_Pipeline_Advisor_SKILL
