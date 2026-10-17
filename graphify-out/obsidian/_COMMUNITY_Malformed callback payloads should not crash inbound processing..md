---
type: community
members: 6
---

# Malformed callback payloads should not crash inbound processing.

**Members:** 6 nodes

## Members
- [[dot-test_egress_callback_non_dict_result_is_handled()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Malformed callback payloads should not crash inbound processing.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[answer_callback()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[approve()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[deny()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[handle_callback()]] - code - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Malformed_callback_payloads_should_not_crash_inbound_processing
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_FakeRBAC]]
- 1 edge to [[_COMMUNITY_test_llm_proxy_local_parity.py]]

## Top bridge nodes
- [[dot-test_egress_callback_non_dict_result_is_handled()]] - degree 8, connects to 2 communities
