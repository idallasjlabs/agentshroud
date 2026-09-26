---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Outbound Infrastructure Content Filter (deny-lis"
location: "L2545"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Outbound_Infrastructure_Content_Filter_deny-lis
---

# Sensitive path probes should be blocked/quarantined for collaborators.

## Connections
- [[.test_collaborator_sensitive_path_probe_is_blocked_and_quarantined()]] - `rationale_for` [EXTRACTED]
- [[.test_collaborator_sensitive_path_probe_shell_style_is_blocked_and_quarantined()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Outbound_Infrastructure_Content_Filter_deny-lis