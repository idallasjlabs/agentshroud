---
source_file: "gateway/ingest_api/config.py"
type: "code"
community: "Slack API Proxy"
location: "L745"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Slack_API_Proxy
---

# reload_config()

## Connections
- [[GatewayConfig_1]] - `references` [EXTRACTED]
- [[Path_1]] - `references` [EXTRACTED]
- [[Re-parse and validate ``config_path``; atomically swap in reloadable fields.]] - `rationale_for` [EXTRACTED]
- [[apply_reloadable_config()]] - `calls` [EXTRACTED]
- [[config.py]] - `contains` [EXTRACTED]
- [[config_watcher()]] - `calls` [EXTRACTED]
- [[load_config()]] - `calls` [EXTRACTED]
- [[test_config_hot_reload.py]] - `imports` [EXTRACTED]
- [[test_reload_applies_valid_change()]] - `calls` [EXTRACTED]
- [[test_reload_missing_file_keeps_last_good()]] - `calls` [EXTRACTED]
- [[test_reload_no_reloadable_field_changed()]] - `calls` [EXTRACTED]
- [[test_reload_rejects_invalid_and_keeps_last_good()]] - `calls` [EXTRACTED]
- [[test_reload_rejects_schema_violation_and_keeps_last_good()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Slack_API_Proxy