---
type: community
members: 6
---

# Community 2073

**Members:** 6 nodes

## Members
- [[._is_valid_domain_name()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_filename_reference()]] - code - gateway/proxy/telegram_proxy.py
- [[._trigger_web_fetch_approval()]] - code - gateway/proxy/telegram_proxy.py
- [[Best-effort check to avoid treating local file names as egress domains.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Queue an interactive egress approval when raw web_fetch JSON leaks.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Validate normalized domain labels to avoid malformed allowlist entries.]] - rationale - gateway/proxy/telegram_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_2073
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Community 14]]
- 2 edges to [[_COMMUNITY_Community 187]]
- 2 edges to [[_COMMUNITY_Community 96]]

## Top bridge nodes
- [[._trigger_web_fetch_approval()]] - degree 8, connects to 3 communities
- [[._looks_like_filename_reference()]] - degree 4, connects to 2 communities
- [[._is_valid_domain_name()]] - degree 3, connects to 1 community