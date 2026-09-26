---
source_file: "gateway/tests/test_soc_auth.py"
type: "code"
community: ".analyze_tool_call()"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/analyze_tool_call
---

# test_soc_auth.py

## Connections
- [[TestSessionTokens]] - `contains` [EXTRACTED]
- [[TestWSTokens]] - `contains` [EXTRACTED]
- [[_verify_session_token()]] - `imports` [EXTRACTED]
- [[issue_session_token()]] - `imports` [EXTRACTED]
- [[issue_ws_token()]] - `imports` [EXTRACTED]
- [[redeem_ws_token()]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/analyze_tool_call