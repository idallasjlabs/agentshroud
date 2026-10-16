---
source_file: "gateway/security/egress_filter.py"
type: "code"
community: "EgressAttempt"
location: "L180"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/EgressAttempt
---

# ._check_impl()

## Connections
- [[dot-_is_ipv6()]] - `calls` [EXTRACTED]
- [[dot-_is_private_ip()]] - `calls` [EXTRACTED]
- [[dot-_matches_allowlist_domain()]] - `calls` [EXTRACTED]
- [[dot-_matches_ip_list()]] - `calls` [EXTRACTED]
- [[dot-_record()_1]] - `calls` [EXTRACTED]
- [[dot-check()_3]] - `calls` [EXTRACTED]
- [[dot-get_policy()_1]] - `calls` [EXTRACTED]
- [[dot-matches_domain()]] - `calls` [EXTRACTED]
- [[dot-matches_ip()]] - `calls` [EXTRACTED]
- [[dot-matches_port()]] - `calls` [EXTRACTED]
- [[Check if an outbound connection is allowed.          Args             agent_id]] - `rationale_for` [EXTRACTED]
- [[EgressAttempt]] - `references` [EXTRACTED]
- [[EgressFilter_2]] - `method` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/EgressAttempt
