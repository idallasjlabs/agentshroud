---
type: community
members: 11
---

# VRAMHeadroomError

**Members:** 11 nodes

## Members
- [[dot-check_vram_headroom()]] - code - gateway/security/resource_guard.py
- [[dot-test_disabled_when_threshold_zero()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_passes_with_sufficient_headroom()]] - code - gateway/tests/test_resource_guard_limits.py
- [[dot-test_rejects_insufficient_headroom()]] - code - gateway/tests/test_resource_guard_limits.py
- [[Exception_4]] - code
- [[Pre-flight VRAM headroom check before dispatching a long-context local-model…]] - rationale - gateway/security/resource_guard.py
- [[Raised when a local-model call is rejected because estimated VRAM usage would…]] - rationale - gateway/security/resource_guard.py
- [[TestVramHeadroom]] - code - gateway/tests/test_resource_guard_limits.py
- [[VRAMHeadroomError]] - code - gateway/security/resource_guard.py
- [[VRAMHeadroomError must be a distinct exception, not a subclass of…]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[test_vram_headroom_error_is_not_resource_warning()]] - code - gateway/tests/test_llm_proxy_local_parity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/VRAMHeadroomError
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_ResourceGuard]]
- 2 edges to [[_COMMUNITY_LLMProxy]]

## Top bridge nodes
- [[VRAMHeadroomError]] - degree 10, connects to 2 communities
- [[TestVramHeadroom]] - degree 5, connects to 1 community
- [[dot-check_vram_headroom()]] - degree 3, connects to 1 community
- [[test_vram_headroom_error_is_not_resource_warning()]] - degree 3, connects to 1 community
