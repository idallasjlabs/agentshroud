---
source_file: "gateway/proxy/llm_quota_detector.py"
type: "code"
community: "Module Group 352"
location: "L142"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Module_Group_352
---

# is_overloaded()

## Connections
- [[.proxy_messages()]] - `calls` [EXTRACTED]
- [[.test_empty_and_garbage_bodies()]] - `calls` [EXTRACTED]
- [[.test_http_200_with_overloaded_body()]] - `calls` [EXTRACTED]
- [[.test_http_503_with_overloaded_body()]] - `calls` [EXTRACTED]
- [[.test_http_529_with_overloaded_body()]] - `calls` [EXTRACTED]
- [[.test_mention_in_content_not_flagged()]] - `calls` [EXTRACTED]
- [[.test_normal_200_message_body_not_flagged()]] - `calls` [EXTRACTED]
- [[.test_other_error_types_not_flagged()]] - `calls` [EXTRACTED]
- [[.test_quota_statuses_not_claimed()]] - `calls` [EXTRACTED]
- [[Return (True, anthropic_overloaded) for an overloaded_error envelope.      Onl]] - `rationale_for` [EXTRACTED]
- [[llm_proxy.py]] - `imports` [EXTRACTED]
- [[llm_quota_detector.py]] - `contains` [EXTRACTED]
- [[test_llm_quota_detector.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Module_Group_352
