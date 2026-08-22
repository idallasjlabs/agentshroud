---
source_file: "gateway/tests/test_slack_proxy_coverage.py"
type: "rationale"
community: "Slack Proxy Coverage"
location: "L38"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Slack_Proxy_Coverage
---

# Unparseable JSON body → warning logged, empty payload forwarded (no crash).

## Connections
- [[.test_malformed_json_body_forwards_with_empty_payload()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Slack_Proxy_Coverage