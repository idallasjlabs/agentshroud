---
source_file: "gateway/security/tool_acl.py"
type: "rationale"
community: "TelegramAPIProxy"
location: "L469"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TelegramAPIProxy
---

# Authorize a tool call, refusing owner elevation over an unverified origin.

## Connections
- [[.can_use_tool_from_origin()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TelegramAPIProxy