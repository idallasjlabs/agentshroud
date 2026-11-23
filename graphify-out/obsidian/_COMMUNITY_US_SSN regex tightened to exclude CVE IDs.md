---
type: community
members: 1
---

# US_SSN regex tightened to exclude CVE IDs

**Members:** 1 nodes

## Members
- [[US_SSN regex tightened to exclude CVE IDs]] - rationale - gateway/tests/test_us_ssn_regex_tightened.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/US_SSN_regex_tightened_to_exclude_CVE_IDs
SORT file.name ASC
```
