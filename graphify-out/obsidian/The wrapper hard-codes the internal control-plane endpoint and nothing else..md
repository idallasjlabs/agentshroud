---
source_file: "gateway/tests/test_bots_ssh_exec_wrapper.py"
type: "rationale"
community: "test_bots_ssh_exec_wrapper.py"
location: "L52"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_bots_ssh_exec_wrapperpy
---

# The wrapper hard-codes the internal control-plane endpoint and nothing else.

## Connections
- [[test_wrapper_targets_only_internal_gateway_endpoint()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_bots_ssh_exec_wrapperpy