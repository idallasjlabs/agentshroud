---
type: community
members: 6
---

# ._sanitize_reason

**Members:** 6 nodes

## Members
- [[dot-_sanitize_reason()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-test_sanitize_reason_preserves_simple_text()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_sanitize_reason_strips_file_paths()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_sanitize_reason_strips_module_paths()]] - code - gateway/tests/test_round2_hardening.py
- [[Strip internal paths and module names from block reasons before user display.]] - rationale - gateway/proxy/telegram_proxy.py
- [[TestNotifyUserBlockedSanitization]] - code - gateway/tests/test_round2_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_sanitize_reason
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_FileSandbox]]
- 1 edge to [[_COMMUNITY__make_sanitizer]]

## Top bridge nodes
- [[dot-_sanitize_reason()]] - degree 7, connects to 2 communities
- [[TestNotifyUserBlockedSanitization]] - degree 5, connects to 2 communities
