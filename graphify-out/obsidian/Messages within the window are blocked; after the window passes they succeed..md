---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "Unknown/unapproved users have stricter rate limits than collaborators. After…"
location: "L7867"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Unknown/unapproved_users_have_stricter_rate_limits_than_collaborators_After
---

# Messages within the window are blocked; after the window passes they succeed.

## Connections
- [[dot-test_collaborator_rate_limit_resets_after_window()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Unknown/unapproved_users_have_stricter_rate_limits_than_collaborators_After
