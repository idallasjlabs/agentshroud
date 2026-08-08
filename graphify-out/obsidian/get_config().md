---
source_file: "gateway/soc/router.py"
type: "code"
community: "Bot CVE Scorecard"
location: "L1890"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Bot_CVE_Scorecard
---

# get_config()

## Connections
- [[.test_bot_id_returns_per_bot_config()]] - `calls` [EXTRACTED]
- [[.test_config_none_returns_empty_dict()]] - `calls` [EXTRACTED]
- [[.test_no_bot_id_returns_global_config()]] - `calls` [EXTRACTED]
- [[.test_unknown_bot_id_returns_error()]] - `calls` [EXTRACTED]
- [[SCLCaller_1]] - `references` [EXTRACTED]
- [[SCLCaller_3]] - `references` [EXTRACTED]
- [[_app_state()]] - `calls` [EXTRACTED]
- [[router.py_1]] - `contains` [EXTRACTED]
- [[test_soc_bots.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Bot_CVE_Scorecard