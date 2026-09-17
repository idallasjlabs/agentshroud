---
type: community
cohesion: 0.10
members: 20
---

# TestPerAgentUpstreamChecks

**Cohesion:** 0.10 - loosely connected
**Members:** 20 nodes

## Members
- [[.test_agent_label_falls_back_when_source_missing()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_alert_send_failure_is_swallowed()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_all_agents_omitting_bot_tokens_preserves_default_behavior()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_all_agents_runs_each_independently_and_isolates_failure()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_all_agents_uses_per_agent_token_when_provided()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_check_scoped_to_agent_registry_and_repo()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_hermes_zero_stays_silent_via_all_agents()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_hermes_zero_still_reports_when_always_report_zero()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_openclaw_zero_stays_silent()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[.test_zero_report_send_failure_is_swallowed()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[2026-08-04 fix Hermes zero-CVE heartbeats confused the owner because         th]] - rationale - gateway/tests/test_daily_cve_report.py
- [[2026-08-04 each wrapped agent's alert must go out via ITS OWN bot         token]] - rationale - gateway/tests/test_daily_cve_report.py
- [[A Telegram failure on the new-CVE alert path never raises.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[A Telegram failure on the zero-report path never raises.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Backward compatibility no bot_tokens arg means every agent still         gets t]] - rationale - gateway/tests/test_daily_cve_report.py
- [[If the per-agent source config is missing, the label falls back gracefully.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[OpenClaw and Hermes are processed on fully separate paths; one failing         n]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Owner wants to SEE a Hermes report even with 0 new advisories.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[TestPerAgentUpstreamChecks_1]] - code - gateway/tests/test_daily_cve_report.py
- [[check_upstream_cves(agent_id=...) selects that agent's OWN repo + list.]] - rationale - gateway/tests/test_daily_cve_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestPerAgentUpstreamChecks
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_asyncio]]
- 1 edge to [[_COMMUNITY_test_daily_cve_report.py]]

## Top bridge nodes
- [[TestPerAgentUpstreamChecks_1]] - degree 11, connects to 1 community
- [[check_upstream_cves(agent_id=...) selects that agent's OWN repo + list.]] - degree 2, connects to 1 community
- [[Owner wants to SEE a Hermes report even with 0 new advisories.]] - degree 2, connects to 1 community
- [[If the per-agent source config is missing, the label falls back gracefully.]] - degree 2, connects to 1 community
- [[A Telegram failure on the zero-report path never raises.]] - degree 2, connects to 1 community