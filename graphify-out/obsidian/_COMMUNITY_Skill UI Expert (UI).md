---
type: community
cohesion: 0.12
members: 27
---

# Skill: UI Expert (UI)

**Cohesion:** 0.12 - loosely connected
**Members:** 27 nodes

## Members
- [[CVE-2026-34425 — Preflight Validation Bypass (Shell-Bleed)]] - rationale - docs/security/cve-mitigation-matrix.md
- [[LLMProxy._apply_filters]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._build_timeout_fallback_response]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._emit_failover_notice]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._enforce_tool_acl]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._failover_request]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._filter_outbound]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._filter_outbound_streaming]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._filter_streaming_event]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._forward_request]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._get_local_model]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._get_local_secondary_model]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._is_connect_error]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._is_local_oom]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._local_backend_headers]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._local_backend_unavailable_response]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._local_failover_base]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._local_secondary_failover_request]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._normalize_local_model]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._record_failover_event]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._scan_inbound]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._scan_request_data]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._suppress_qwen3_thinking]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy._widen_optional_tool_param_types]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy.proxy_messages]] - code - gateway/proxy/llm_proxy.py
- [[LLMProxy.proxy_messages_streaming]] - code - gateway/proxy/llm_proxy.py
- [[xml_leak_filter.py]] - code - gateway/security/xml_leak_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Skill_UI_Expert_UI
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_test_gemini_openai_translator.py]]
- 5 edges to [[_COMMUNITY_SecureBrowser]]
- 2 edges to [[_COMMUNITY_AgentShroud Security Hardening Plan]]
- 2 edges to [[_COMMUNITY_graphify Skill]]
- 2 edges to [[_COMMUNITY_AgentShroud Project Terminology]]
- 1 edge to [[_COMMUNITY_Oracle — Feedback Analyst]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_DockerEngine]]
- 1 edge to [[_COMMUNITY_test_jira_weekly_review.py]]
- 1 edge to [[_COMMUNITY_A2AProxyResult]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_URLAnalyzer]]
- 1 edge to [[_COMMUNITY_KeyRotationConfig]]

## Top bridge nodes
- [[LLMProxy.proxy_messages]] - degree 24, connects to 5 communities
- [[xml_leak_filter.py]] - degree 6, connects to 4 communities
- [[LLMProxy.proxy_messages_streaming]] - degree 11, connects to 3 communities
- [[LLMProxy._failover_request]] - degree 11, connects to 2 communities
- [[LLMProxy._local_secondary_failover_request]] - degree 7, connects to 1 community