---
type: community
members: 2
---

# Docker sidecar integrity — falco/clamav/fluent-bit in-process, wazuh-agent standalone sidecar

**Members:** 2 nodes

## Members
- [[dot-test_runtime_profile_memory_error_text_is_rewritten_generic()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Previously emitted runtime-profile memory text should be normalized to generic g]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Docker_sidecar_integrity__falco/clamav/fluent-bit_in-process_wazuh-agent_standalone_sidecar
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY__req]]
- 1 edge to [[_COMMUNITY_CronStateMonitor]]
- 1 edge to [[_COMMUNITY_UserSessionManager (2)]]

## Top bridge nodes
- [[dot-test_runtime_profile_memory_error_text_is_rewritten_generic()]] - degree 4, connects to 3 communities
