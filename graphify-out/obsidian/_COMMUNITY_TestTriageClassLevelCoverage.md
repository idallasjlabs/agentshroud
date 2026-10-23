---
type: community
cohesion: 0.36
members: 8
---

# TestTriageClassLevelCoverage

**Cohesion:** 0.36 - loosely connected
**Members:** 8 nodes

## Members
- [[dot-_triage()]] - code - gateway/tests/test_xml_dtd_control.py
- [[dot-test_libxml2_dtd_uaf_classifies_as_xxe_not_dos()]] - code - gateway/tests/test_xml_dtd_control.py
- [[dot-test_unrelated_classes_unchanged()]] - code - gateway/tests/test_xml_dtd_control.py
- [[dot-test_xxe_class_is_covered_by_the_gateway_control()]] - code - gateway/tests/test_xml_dtd_control.py
- [[It calls itself DoS; the generic DOS profile is containment-only. Left as DOS…]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[TestTriageClassLevelCoverage]] - code - gateway/tests/test_xml_dtd_control.py
- [[The durable statement is at the CLASS level, not per-CVE. A register entry…]] - rationale - gateway/tests/test_xml_dtd_control.py
- [[The new rule runs first, so prove it does not swallow neighbours.]] - rationale - gateway/tests/test_xml_dtd_control.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestTriageClassLevelCoverage
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_main_endpoints.py]]

## Top bridge nodes
- [[TestTriageClassLevelCoverage]] - degree 6, connects to 1 community
