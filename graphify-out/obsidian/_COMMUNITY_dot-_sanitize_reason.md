---
type: community
members: 8
---

# ._sanitize_reason

**Members:** 8 nodes

## Members
- [[dot-_sanitize_reason()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-test_sanitize_reason_hides_internal_paths()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_sanitize_reason_preserves_simple_text()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_sanitize_reason_strips_file_paths()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_sanitize_reason_strips_module_paths()]] - code - gateway/tests/test_round2_hardening.py
- [[Strip internal paths and module names from block reasons before user display.]] - rationale - gateway/proxy/telegram_proxy.py
- [[TestNotifyUserBlockedSanitization]] - code - gateway/tests/test_round2_hardening.py
- [[User-facing block reasons should not expose modules or file paths.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_sanitize_reason
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_GitGuard]]
- 1 edge to [[_COMMUNITY_TestOutboundPipelineIntegration]]

## Top bridge nodes
- [[TestNotifyUserBlockedSanitization]] - degree 5, connects to 2 communities
- [[dot-_sanitize_reason()]] - degree 7, connects to 1 community
- [[dot-test_sanitize_reason_hides_internal_paths()]] - degree 3, connects to 1 community
