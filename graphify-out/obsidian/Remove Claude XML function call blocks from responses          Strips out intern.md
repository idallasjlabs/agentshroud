---
source_file: "gateway/ingest_api/sanitizer.py"
type: "rationale"
community: "PII Sanitizer Pipeline"
location: "L518"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# Remove Claude XML function call blocks from responses          Strips out intern

## Connections
- [[.filter_xml_blocks()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline