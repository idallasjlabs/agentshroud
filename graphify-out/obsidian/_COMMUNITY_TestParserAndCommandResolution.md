---
type: community
cohesion: 0.50
members: 5
---

# TestParserAndCommandResolution

**Cohesion:** 0.50 - moderately connected
**Members:** 5 nodes

## Members
- [[.test_parser_defaults()]] - code - gateway/tests/test_multi_host_test.py
- [[.test_parser_hosts_and_command()]] - code - gateway/tests/test_multi_host_test.py
- [[ArgumentParser]] - code - gateway/tools/multi_host_test.py
- [[TestParserAndCommandResolution]] - code - gateway/tests/test_multi_host_test.py
- [[build_parser()]] - code - gateway/tools/multi_host_test.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestParserAndCommandResolution
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_test_multi_host_test.py]]
- 2 edges to [[_COMMUNITY_MultiHostResult]]
- 1 edge to [[_COMMUNITY_HostStatus]]
- 1 edge to [[_COMMUNITY_multi_host_test.py]]
- 1 edge to [[_COMMUNITY_main()]]

## Top bridge nodes
- [[TestParserAndCommandResolution]] - degree 6, connects to 3 communities
- [[build_parser()]] - degree 6, connects to 3 communities