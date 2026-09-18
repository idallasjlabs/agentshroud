---
type: community
cohesion: 0.10
members: 27
---

# EgressFilterConfig

**Cohesion:** 0.10 - loosely connected
**Members:** 27 nodes

## Members
- [[._matches_any_pattern()]] - code - gateway/security/egress_config.py
- [[._matches_any_pattern()_1]] - code - gateway/security/egress_config.py
- [[.from_environment()]] - code - gateway/security/egress_config.py
- [[.from_environment()_1]] - code - gateway/security/egress_config.py
- [[.get_effective_allowlist()]] - code - gateway/security/egress_config.py
- [[.get_effective_allowlist()_1]] - code - gateway/security/egress_config.py
- [[.is_denylisted()]] - code - gateway/security/egress_config.py
- [[.is_denylisted()_1]] - code - gateway/security/egress_config.py
- [[.matches_allowlist()]] - code - gateway/security/egress_config.py
- [[.matches_allowlist()_1]] - code - gateway/security/egress_config.py
- [[Check if a domain matches the denylist.]] - rationale - gateway/security/egress_config.py
- [[Check if domain matches any pattern in the list (supports wildcards).]] - rationale - gateway/security/egress_config.py
- [[Configuration for egress filtering enforcement.]] - rationale - gateway/security/egress_config.py
- [[Create config from environment variables and AGENTSHROUD_MODE.]] - rationale - gateway/security/egress_config.py
- [[EgressFilterConfig_2]] - code - gateway/security/egress_config.py
- [[FEED_HOSTS]] - code - gateway/security/feed_hosts.py
- [[GENERATED FILE — do not hand-edit. Feed-source hostnames derived from…]] - rationale - gateway/security/feed_hosts.py
- [[Get the effective allowlist for a specific agent.]] - rationale - gateway/security/egress_config.py
- [[Get the global egress filter configuration.]] - rationale - gateway/security/egress_config.py
- [[PERMANENT_EGRESS_DOMAINS]] - code - gateway/security/egress_config.py
- [[Public does domain match any pattern in the effective default allowlist]] - rationale - gateway/security/egress_config.py
- [[Return True if domain matches any pattern (exact or ``.`` wildcard).      Sin]] - rationale - gateway/security/egress_config.py
- [[domain_matches()]] - code - gateway/security/egress_config.py
- [[egress_config.py_3]] - code - gateway/security/egress_config.py
- [[feed_hosts.py]] - code - gateway/security/feed_hosts.py
- [[get_egress_config()]] - code - gateway/security/egress_config.py
- [[set_egress_config()_1]] - code - gateway/security/egress_config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressFilterConfig
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_EgressFilterConfig]]
- 2 edges to [[_COMMUNITY_DraftEntry]]

## Top bridge nodes
- [[._matches_any_pattern()]] - degree 5, connects to 2 communities
- [[.matches_allowlist()]] - degree 3, connects to 2 communities
- [[Get the global egress filter configuration.]] - degree 4, connects to 1 community
- [[.get_effective_allowlist()]] - degree 3, connects to 1 community
- [[.is_denylisted()]] - degree 3, connects to 1 community