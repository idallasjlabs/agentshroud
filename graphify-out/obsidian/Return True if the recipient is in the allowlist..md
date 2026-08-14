---
source_file: "gateway/ingest_api/main.py"
type: "rationale"
community: "PII Sanitizer Pipeline"
location: "L138"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# Return True if the recipient is in the allowlist.

## Connections
- [[OpProxyRequest]] - `rationale_for` [EXTRACTED]
- [[_is_imessage_recipient_allowed()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline