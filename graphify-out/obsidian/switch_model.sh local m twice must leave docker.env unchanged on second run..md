---
source_file: "gateway/tests/test_switch_model_idempotent.py"
type: "rationale"
community: "._run_and_read()"
location: "L78"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_run_and_read
---

# switch_model.sh local <m> twice must leave docker/.env unchanged on second run.

## Connections
- [[TestSwitchModelIdempotent]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_run_and_read