---
type: community
members: 6
---

# .verify_export_integrity

**Members:** 6 nodes

## Members
- [[dot-_parse_cef_for_verification()]] - code - gateway/security/audit_export.py
- [[dot-test_conversion_error_path()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-verify_export_integrity()]] - code - gateway/security/audit_export.py
- [[Parse CEF lines and extract entryHashpreviousHash for chain verification.…]] - rationale - gateway/security/audit_export.py
- [[Verify the integrity of an exported audit log. Args export_content The…]] - rationale - gateway/security/audit_export.py
- [[timestamp()]] - code - gateway/tests/test_soc_realtime_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/verify_export_integrity
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_AuditExporter]]
- 1 edge to [[_COMMUNITY__audit_entry]]
- 1 edge to [[_COMMUNITY_socmodels.py]]

## Top bridge nodes
- [[dot-verify_export_integrity()]] - degree 4, connects to 1 community
- [[dot-_parse_cef_for_verification()]] - degree 3, connects to 1 community
- [[timestamp()]] - degree 3, connects to 1 community
- [[dot-test_conversion_error_path()]] - degree 2, connects to 1 community
