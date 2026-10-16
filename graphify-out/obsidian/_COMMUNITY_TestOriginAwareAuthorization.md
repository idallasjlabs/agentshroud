---
type: community
cohesion: 0.13
members: 15
---

# TestOriginAwareAuthorization

**Cohesion:** 0.13 - loosely connected
**Members:** 15 nodes

## Members
- [[dot-test_applies_to_any_agent_not_just_openclaw()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_denial_is_counted_for_soc_correlation()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_non_owner_over_unverified_origin_is_unchanged()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_owner_claim_over_unverified_origin_is_refused_elevation()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_owner_over_verified_origin_keeps_full_authority()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_unknown_origin_defaults_to_unverified()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_unverified_origin_still_allows_public_tools()]] - code - gateway/tests/test_tool_acl.py
- [[A non-owner gains nothing and loses nothing from origin checking.]] - rationale - gateway/tests/test_tool_acl.py
- [[AgentShroud-side mitigation for the 'channel skips the check' CVE class.      Up]] - rationale - gateway/tests/test_tool_acl.py
- [[Fail closed an origin nobody vouched for is not trusted.          A caller that]] - rationale - gateway/tests/test_tool_acl.py
- [[Refusing ELEVATION is not the same as blanket denial — an unverified         ori]] - rationale - gateway/tests/test_tool_acl.py
- [[TestOriginAwareAuthorization]] - code - gateway/tests/test_tool_acl.py
- [[The control is agent-agnostic by construction it takes an origin and         an]] - rationale - gateway/tests/test_tool_acl.py
- [[The core of the CVE class a side channel claiming to be the owner.          ter]] - rationale - gateway/tests/test_tool_acl.py
- [[The legitimate path must not regress.]] - rationale - gateway/tests/test_tool_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestOriginAwareAuthorization
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Role]]
- 2 edges to [[_COMMUNITY_RBACConfig]]

## Top bridge nodes
- [[TestOriginAwareAuthorization]] - degree 14, connects to 2 communities
