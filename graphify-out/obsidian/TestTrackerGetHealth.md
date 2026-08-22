---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "code"
community: "Collaborator Tracker"
location: "L4943"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Collaborator_Tracker
---

# TestTrackerGetHealth

## Connections
- [[.test_failed_write_makes_unhealthy()]] - `method` [EXTRACTED]
- [[.test_initial_state_healthy()]] - `method` [EXTRACTED]
- [[CollaboratorActivityTracker]] - `uses` [INFERRED]
- [[CollaboratorActivityTracker.get_health() must return accurate counters.]] - `rationale_for` [EXTRACTED]
- [[PIIConfig]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[test_telegram_proxy_outbound.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Collaborator_Tracker