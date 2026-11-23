---
source_file: "gateway/soc/router.py"
type: "code"
community: "test_soc_bots.py"
location: "L1968"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_soc_botspy
---

# list_bots()

## Connections
- [[dot-default()]] - `indirect_call` [INFERRED]
- [[dot-test_bot_dict_has_required_keys()]] - `calls` [EXTRACTED]
- [[dot-test_bots_backward_compat_no_bots_config()]] - `calls` [EXTRACTED]
- [[dot-test_bots_no_config_returns_synthetic_entry()]] - `calls` [EXTRACTED]
- [[dot-test_bots_returns_correct_structure()]] - `calls` [EXTRACTED]
- [[dot-test_bots_returns_default_true_on_default_bot()]] - `calls` [EXTRACTED]
- [[dot-test_returns_default_when_config_is_none()]] - `calls` [EXTRACTED]
- [[dot-test_returns_default_when_no_bots_config()]] - `calls` [EXTRACTED]
- [[dot-test_returns_registered_bots()]] - `calls` [EXTRACTED]
- [[dot-test_single_bot_returns_list_of_one()]] - `calls` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
- [[Return the list of registered bots. Falls back to backward-compat OpenClaw…]] - `rationale_for` [EXTRACTED]
- [[SCLCaller]] - `uses` [INFERRED]
- [[_app_state()]] - `calls` [EXTRACTED]
- [[get]] - `references` [EXTRACTED]
- [[socrouter.py]] - `contains` [EXTRACTED]
- [[test_soc_bots.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_soc_botspy
