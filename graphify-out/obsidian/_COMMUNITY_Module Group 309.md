---
type: community
cohesion: 0.14
members: 14
---

# Module Group 309

**Cohesion:** 0.14 - loosely connected
**Members:** 14 nodes

## Members
- [[.test_false_on_empty_string()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_false_on_non_string()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_no_false_positive_on_domain_mention()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_no_false_positive_on_generic_llm_response()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_true_on_callback_token()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_true_on_deny_token()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_true_on_real_egress_banner_header()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Common LLM prose with 'risk', 'tool', 'id' must NOT trigger the matcher.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Generic 'domain' mention without the egress emoji must not trigger.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Inline-keyboard callback tokens must always match (egress_allow_always_uuid).]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TestInternalBannerMatcher]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[The canonical 🌐 Egress Request header from TelegramEgressNotifier must match.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_contains_internal_approval_banner must only fire on real egress banners.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[egress_deny_ callback token must match.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_309
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Tool Result Sanitizer]]
- 1 edge to [[_COMMUNITY_Telegram Proxy Core]]
- 1 edge to [[_COMMUNITY_Module Group 140]]

## Top bridge nodes
- [[TestInternalBannerMatcher]] - degree 13, connects to 3 communities