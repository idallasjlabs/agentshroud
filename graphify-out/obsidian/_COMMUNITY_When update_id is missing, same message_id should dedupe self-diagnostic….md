---
type: community
members: 5
---

# When update_id is missing, same message_id should dedupe self-diagnostic…

**Members:** 5 nodes

## Members
- [[dot-test_self_diagnose_dedupe_handles_missing_update_id_same_message()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_self_diagnostic_dedupe_handles_missing_update_id_same_message()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[When update_id is missing, same message_id should dedupe self-diagnostic…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_urlopen()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_urlopen()_1]] - code - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/When_update_id_is_missing_same_message_id_should_dedupe_self-diagnostic
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_FakeRBAC]]
- 4 edges to [[_COMMUNITY_test_llm_proxy_local_parity.py]]
- 2 edges to [[_COMMUNITY_test_telegram_proxy_inbound.py]]

## Top bridge nodes
- [[dot-test_self_diagnose_dedupe_handles_missing_update_id_same_message()]] - degree 9, connects to 3 communities
- [[dot-test_self_diagnostic_dedupe_handles_missing_update_id_same_message()]] - degree 9, connects to 3 communities
