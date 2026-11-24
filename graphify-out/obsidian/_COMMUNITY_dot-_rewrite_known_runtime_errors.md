---
type: community
members: 14
---

# ._rewrite_known_runtime_errors

**Members:** 14 nodes

## Members
- [[dot-_rewrite_known_runtime_errors()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-test_rewrite_known_runtime_errors_accepts_hyphen_delimiter()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_accepts_underscore_delimiter()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_handles_non_string_input()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_matches_cannot_to_access_variant()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_matches_healthcheck_skill_sandbox_error()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_matches_http_status_without_body()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_matches_memory_embedding_provider_error()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_matches_no_response_generated_phrase()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_requires_skill_marker_for_healthcheck_branch()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_returns_none_for_unrelated_text()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Map recurring runtimeprovider failures to deterministic operator guidance.]] - rationale - gateway/proxy/telegram_proxy.py
- [[TestRuntimeRewriteHelpers]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Unit tests for deterministic runtime error rewrite helper behavior.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_rewrite_known_runtime_errors
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_dot-_filter_outbound]]

## Top bridge nodes
- [[TestRuntimeRewriteHelpers]] - degree 13, connects to 2 communities
- [[dot-_rewrite_known_runtime_errors()]] - degree 13, connects to 2 communities
