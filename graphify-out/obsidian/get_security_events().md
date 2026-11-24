---
source_file: "gateway/soc/router.py"
type: "code"
community: "test_soc_bots.py"
location: "L145"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_soc_botspy
---

# get_security_events()

## Connections
- [[dot-test_filters_events_by_exact_bot_id()]] - `calls` [EXTRACTED]
- [[dot-test_no_bot_id_returns_all_events()]] - `calls` [EXTRACTED]
- [[dot-test_security_events_filters_by_bot_id()]] - `calls` [EXTRACTED]
- [[dot-test_security_events_nonexistent_bot_returns_empty_not_404()]] - `calls` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
- [[SCLCaller]] - `uses` [INFERRED]
- [[_app_state()]] - `calls` [EXTRACTED]
- [[collect_recent_events()]] - `calls` [EXTRACTED]
- [[get]] - `references` [EXTRACTED]
- [[socrouter.py]] - `contains` [EXTRACTED]
- [[test_soc_bots.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_soc_botspy
