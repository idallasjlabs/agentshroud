---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: ".test_collaborator_sensitive_path_probe_shell_st"
location: "L2576"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_collaborator_sensitive_path_probe_shell_st
---

# Shell-style sensitive path probes (e.g., ls ~/.ssh) should be blocked.

## Connections
- [[.test_collaborator_sensitive_path_probe_shell_style_is_blocked_and_quarantined()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_collaborator_sensitive_path_probe_shell_st