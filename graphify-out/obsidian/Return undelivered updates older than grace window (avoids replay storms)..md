---
source_file: "gateway/proxy/telegram_replay.py"
type: "rationale"
community: ".test_collaborator_web_access_imperative_with_url_queues_owner_approval()"
location: "L119"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_collaborator_web_access_imperative_with_url_queues_owner_approval
---

# Return undelivered updates older than grace window (avoids replay storms).

## Connections
- [[dot-pull_undelivered()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_collaborator_web_access_imperative_with_url_queues_owner_approval
