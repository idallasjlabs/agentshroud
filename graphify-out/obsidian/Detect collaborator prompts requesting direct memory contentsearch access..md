---
source_file: "gateway/proxy/telegram_proxy.py"
type: "rationale"
community: "Collaborator Prompt Classifiers"
location: "L1599"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Collaborator_Prompt_Classifiers
---

# Detect collaborator prompts requesting direct memory content/search access.

## Connections
- [[._looks_like_cross_user_messaging_request()]] - `rationale_for` [EXTRACTED]
- [[._looks_like_memory_access_request()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Collaborator_Prompt_Classifiers