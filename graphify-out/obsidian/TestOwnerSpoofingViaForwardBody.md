---
source_file: "gateway/tests/test_forward_routing.py"
type: "code"
community: "Slack API Proxy"
location: "L225"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Slack_API_Proxy
---

# TestOwnerSpoofingViaForwardBody

## Connections
- [[._post()]] - `method` [EXTRACTED]
- [[.test_body_owner_id_with_matching_trusted_header_is_honored()]] - `method` [EXTRACTED]
- [[.test_body_owner_id_without_trusted_header_is_stripped()]] - `method` [EXTRACTED]
- [[.test_non_owner_body_user_id_passes_through()]] - `method` [EXTRACTED]
- [[AgentTarget]] - `uses` [INFERRED]
- [[ForwardRequest]] - `uses` [INFERRED]
- [[WS-E SCRUM-7374 a body-supplied user_id must NOT grant owner identity     to t]] - `rationale_for` [EXTRACTED]
- [[test_forward_routing.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Slack_API_Proxy