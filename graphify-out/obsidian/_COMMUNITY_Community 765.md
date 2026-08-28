---
type: community
cohesion: 0.18
members: 12
---

# Community 765

**Cohesion:** 0.18 - loosely connected
**Members:** 12 nodes

## Members
- [[A competitive-intel body with multiple CVEs is not collapsed into redaction tags]] - rationale - gateway/tests/test_us_ssn_regex_tightened.py
- [[CVE IDs with 5-digit suffix must also be excluded.]] - rationale - gateway/tests/test_us_ssn_regex_tightened.py
- [[CVE identifiers must NOT be treated as US_SSN.]] - rationale - gateway/tests/test_us_ssn_regex_tightened.py
- [[Real SSNs (not preceded by uppercase) must still be detected.]] - rationale - gateway/tests/test_us_ssn_regex_tightened.py
- [[SSN at the very start of a string (no preceding character) is still flagged.]] - rationale - gateway/tests/test_us_ssn_regex_tightened.py
- [[US_SSN regex tightened to exclude CVE IDs]] - rationale - gateway/tests/test_us_ssn_regex_tightened.py
- [[test_cve_dense_report_body_preserved()]] - code - gateway/tests/test_us_ssn_regex_tightened.py
- [[test_cve_pattern_not_flagged_as_ssn()]] - code - gateway/tests/test_us_ssn_regex_tightened.py
- [[test_cve_with_five_digit_suffix_not_flagged()]] - code - gateway/tests/test_us_ssn_regex_tightened.py
- [[test_real_ssn_still_flagged()]] - code - gateway/tests/test_us_ssn_regex_tightened.py
- [[test_ssn_at_start_of_string_still_flagged()]] - code - gateway/tests/test_us_ssn_regex_tightened.py
- [[test_us_ssn_regex_tightened.py]] - code - gateway/tests/test_us_ssn_regex_tightened.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_765
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Community 55]]

## Top bridge nodes
- [[US_SSN regex tightened to exclude CVE IDs]] - degree 3, connects to 1 community