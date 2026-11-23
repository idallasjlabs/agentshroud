---
type: community
members: 52
---

# FalcoAlertWatcher

**Members:** 52 nodes

## Members
- [[dot-__init__()_4]] - code - gateway/security/falco_monitor.py
- [[dot-_handle_critical()]] - code - gateway/security/falco_monitor.py
- [[dot-_process_new_alerts()]] - code - gateway/security/falco_monitor.py
- [[dot-run()]] - code - gateway/security/falco_monitor.py
- [[dot-stop()]] - code - gateway/security/falco_monitor.py
- [[dot-test_categorize_empty()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_categorize_mixed()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_is_agentshroud_rule_false()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_is_agentshroud_rule_true()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_container_info()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_critical_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_empty_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_valid_alert()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_read_alerts_missing_dir()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_clean()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_top_rules()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_with_alerts()]] - code - gateway/tests/test_security_toolchain.py
- [[Any_3]] - code
- [[Categorize alerts by severity. Args alerts List of parsed alerts. Returns…]] - rationale - gateway/security/falco_monitor.py
- [[Check if a rule is AgentShroud-specific. Args rule_name Falco rule name.…]] - rationale - gateway/security/falco_monitor.py
- [[Extend AGENTSHROUD_RULES with bot-specific name prefixes. Called at gateway…]] - rationale - gateway/security/falco_monitor.py
- [[FalcoAlertWatcher]] - code - gateway/security/falco_monitor.py
- [[Generate a summary dict suitable for the health report. Args alerts List of…]] - rationale - gateway/security/falco_monitor.py
- [[Parse a single Falco alert. Args raw Raw Falco alert JSON. Returns Parsed…]] - rationale - gateway/security/falco_monitor.py
- [[Path]] - code
- [[Poll Falco alert files until stopped.]] - rationale - gateway/security/falco_monitor.py
- [[Read Falco alerts from the alert directory. Args alert_dir Directory…]] - rationale - gateway/security/falco_monitor.py
- [[Tail Falco alert files and trigger progressive lockdown on CRITICAL alerts.…]] - rationale - gateway/security/falco_monitor.py
- [[TestFalcoCategorize]] - code - gateway/tests/test_security_toolchain.py
- [[TestFalcoParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestFalcoSummary]] - code - gateway/tests/test_security_toolchain.py
- [[Tests for FalcoAlertWatcher — enforcement bridge from Falco alerts to…]] - rationale - gateway/tests/test_falco_watcher.py
- [[Watcher works without a lockdown module — only logs.]] - rationale - gateway/tests/test_falco_watcher.py
- [[_make_alert()]] - code - gateway/tests/test_falco_watcher.py
- [[asyncio_3]] - code
- [[categorize_alerts()]] - code - gateway/security/falco_monitor.py
- [[configure_rules()]] - code - gateway/security/falco_monitor.py
- [[counting_poll()]] - code - gateway/tests/test_falco_watcher.py
- [[datetime]] - code
- [[falco_monitor.py]] - code - gateway/security/falco_monitor.py
- [[generate_summary()]] - code - gateway/security/falco_monitor.py
- [[is_agentshroud_rule()]] - code - gateway/security/falco_monitor.py
- [[parse_alert()]] - code - gateway/security/falco_monitor.py
- [[read_alerts()]] - code - gateway/security/falco_monitor.py
- [[test_critical_alert_triggers_lockdown()]] - code - gateway/tests/test_falco_watcher.py
- [[test_deduplication_same_alert_twice()]] - code - gateway/tests/test_falco_watcher.py
- [[test_falco_watcher.py]] - code - gateway/tests/test_falco_watcher.py
- [[test_missing_alert_dir_noop()]] - code - gateway/tests/test_falco_watcher.py
- [[test_multiple_critical_alerts()]] - code - gateway/tests/test_falco_watcher.py
- [[test_no_progressive_lockdown_configured()]] - code - gateway/tests/test_falco_watcher.py
- [[test_stop_halts_run_loop()]] - code - gateway/tests/test_falco_watcher.py
- [[test_warning_alert_not_blocked()]] - code - gateway/tests/test_falco_watcher.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/FalcoAlertWatcher
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 3 edges to [[_COMMUNITY_test_progressive_lockdown.py]]
- 3 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_lifespan]]
- 2 edges to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_test_security_audit.py]]

## Top bridge nodes
- [[falco_monitor.py]] - degree 13, connects to 4 communities
- [[FalcoAlertWatcher]] - degree 20, connects to 3 communities
- [[read_alerts()]] - degree 11, connects to 3 communities
- [[generate_summary()]] - degree 8, connects to 3 communities
- [[TestFalcoParser]] - degree 7, connects to 1 community
