---
type: community
cohesion: 0.10
members: 27
---

# Module Group 176

**Cohesion:** 0.10 - loosely connected
**Members:** 27 nodes

## Members
- [[.test_returns_false_when_file_missing()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_false_when_sent_yesterday()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_returns_true_when_sent_today()]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_run_binary_not_found()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_image_scan_type()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_parse_error()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_success()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_timeout()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_trivy_binary_not_found()]] - code - gateway/tests/test_security_audit.py
- [[Background loop checks for new upstream agent CVEs once per day at report_hour]] - rationale - gateway/security/daily_cve_report.py
- [[Background loop sends one CVE report per day at ``report_hour`` UTC.      Runs]] - rationale - gateway/security/daily_cve_report.py
- [[Check if a Trivy report was already sent today (disk-based, secondary to _sent_d]] - rationale - gateway/security/daily_cve_report.py
- [[Check if the upstream CVE watch already ran today (disk-based).]] - rationale - gateway/security/daily_cve_report.py
- [[Generate a summary dict suitable for the health report.      Args         repor_1]] - rationale - gateway/security/trivy_report.py
- [[Run a Trivy scan and return parsed results.      Args         target Scan targ]] - rationale - gateway/security/trivy_report.py
- [[TestAlreadySentToday]] - code - gateway/tests/test_daily_cve_report.py
- [[TestTrivyRun]] - code - gateway/tests/test_security_toolchain.py
- [[_already_checked_upstream_today()]] - code - gateway/security/daily_cve_report.py
- [[_already_sent_today()]] - code - gateway/security/daily_cve_report.py
- [[cve_report_scheduler()]] - code - gateway/security/daily_cve_report.py
- [[daily_cve_report.py]] - code - gateway/security/daily_cve_report.py
- [[datetime]] - code - gateway/security/daily_cve_report.py
- [[generate_summary()_2]] - code - gateway/security/trivy_report.py
- [[run_trivy_scan()_1]] - code - gateway/security/trivy_report.py
- [[scan_type='image' is passed correctly to the trivy binary.]] - rationale - gateway/tests/test_security_toolchain.py
- [[trivy_report.py]] - code - gateway/security/trivy_report.py
- [[upstream_cve_check_scheduler()]] - code - gateway/security/daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_176
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Module Group 169]]
- 6 edges to [[_COMMUNITY_Module Group 153]]
- 4 edges to [[_COMMUNITY_Module Group 250]]
- 3 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 3 edges to [[_COMMUNITY_PII Sanitizer & Resource Guard]]
- 3 edges to [[_COMMUNITY_Module Group 141]]
- 1 edge to [[_COMMUNITY_Alert Dispatcher]]
- 1 edge to [[_COMMUNITY_Module Group 435]]
- 1 edge to [[_COMMUNITY_Module Group 333]]
- 1 edge to [[_COMMUNITY_Security Scanner Integration]]

## Top bridge nodes
- [[daily_cve_report.py]] - degree 17, connects to 5 communities
- [[run_trivy_scan()_1]] - degree 14, connects to 4 communities
- [[generate_summary()_2]] - degree 8, connects to 4 communities
- [[trivy_report.py]] - degree 7, connects to 3 communities
- [[TestTrivyRun]] - degree 7, connects to 2 communities
