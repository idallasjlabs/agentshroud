---
source_file: "gateway/tests/test_egress_filter.py"
type: "code"
community: "EgressAction"
location: "L367"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/EgressAction
---

# .test_allowlisted_domain_still_prompts_when_approval_all_enabled()

## Connections
- [[EgressFilterConfig]] - `calls` [EXTRACTED]
- [[FakeApprovalQueue]] - `calls` [INFERRED]
- [[TestInteractiveApproval]] - `method` [EXTRACTED]
- [[__init__()_16]] - `contains` [EXTRACTED]
- [[asyncio_63]] - `references` [EXTRACTED]
- [[get_pending_requests()_1]] - `contains` [EXTRACTED]
- [[request_approval()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/EgressAction
