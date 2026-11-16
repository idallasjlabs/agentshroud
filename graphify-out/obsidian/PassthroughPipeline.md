---
source_file: "gateway/tests/test_progressive_lockdown.py"
type: "code"
community: "Community 75"
location: "L59"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_75
---

# PassthroughPipeline

## Connections
- [[.process_inbound()_7]] - `method` [EXTRACTED]
- [[.test_attach_lockdown_replaces_instance()]] - `calls` [EXTRACTED]
- [[.test_falco_critical_escalates_instance_shared_with_telegram()]] - `calls` [EXTRACTED]
- [[.test_proxy_falls_back_to_private_instance_when_standalone()]] - `calls` [EXTRACTED]
- [[.test_proxy_uses_injected_instance()]] - `calls` [EXTRACTED]
- [[FalcoAlertWatcher]] - `uses` [INFERRED]
- [[LockdownLevel_1]] - `uses` [INFERRED]
- [[ProgressiveLockdown]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[_make_proxy()_1]] - `calls` [EXTRACTED]
- [[test_progressive_lockdown.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_75