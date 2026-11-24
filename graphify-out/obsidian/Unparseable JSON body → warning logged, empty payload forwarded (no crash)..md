---
source_file: "gateway/tests/test_slack_proxy_coverage.py"
type: "rationale"
community: "AsyncMock"
location: "L38"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/AsyncMock
---

# Unparseable JSON body → warning logged, empty payload forwarded (no crash).

## Connections
- [[dot-test_malformed_json_body_forwards_with_empty_payload()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/AsyncMock
