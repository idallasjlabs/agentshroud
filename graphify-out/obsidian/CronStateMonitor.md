---
source_file: "gateway/security/cron_state_monitor.py"
type: "code"
community: "Community 90"
location: "L66"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_90
---

# CronStateMonitor

## Connections
- [[dot-__init__()_194]] - `method` [EXTRACTED]
- [[dot-_dispatch_aggregate()]] - `method` [EXTRACTED]
- [[dot-_episode_id()]] - `method` [EXTRACTED]
- [[dot-_evaluate()]] - `method` [EXTRACTED]
- [[dot-_run()_1]] - `method` [EXTRACTED]
- [[dot-_safe_dispatch()]] - `method` [EXTRACTED]
- [[dot-check()_5]] - `method` [EXTRACTED]
- [[dot-parse_store()]] - `method` [EXTRACTED]
- [[dot-start()_2]] - `method` [EXTRACTED]
- [[dot-stop()_11]] - `method` [EXTRACTED]
- [[dot-test_alert_ids_stable_per_job_episode()]] - `calls` [EXTRACTED]
- [[dot-test_dispatch_failure_does_not_raise()]] - `calls` [EXTRACTED]
- [[dot-test_first_sight_failing_alerts_once()]] - `calls` [EXTRACTED]
- [[dot-test_flood_capped_with_aggregate_alert()]] - `calls` [EXTRACTED]
- [[dot-test_hermes_jobs_reach_critical_via_observed_runs()]] - `calls` [EXTRACTED]
- [[dot-test_job_name_capped_in_alert()]] - `calls` [EXTRACTED]
- [[dot-test_malformed_consecutive_errors_does_not_blind_store()]] - `calls` [EXTRACTED]
- [[dot-test_multiple_stores_checked()]] - `calls` [EXTRACTED]
- [[dot-test_ok_to_fail_dispatches_high_alert()]] - `calls` [EXTRACTED]
- [[dot-test_oversized_store_skipped()]] - `calls` [EXTRACTED]
- [[dot-test_recovery_refail_realerts_through_real_dedup()]] - `calls` [EXTRACTED]
- [[dot-test_recovery_resets_alerting()]] - `calls` [EXTRACTED]
- [[dot-test_repeated_failure_escalates_to_critical()]] - `calls` [EXTRACTED]
- [[dot-test_start_is_idempotent()]] - `calls` [EXTRACTED]
- [[AlertDispatcher]] - `calls` [INFERRED]
- [[Poll bot cron stores; dispatch AlertDispatcher alerts on failures.]] - `rationale_for` [EXTRACTED]
- [[TestAdversarial]] - `uses` [INFERRED]
- [[TestParsing]] - `uses` [INFERRED]
- [[TestTransitions]] - `uses` [INFERRED]
- [[_DedupDispatchFake]] - `uses` [INFERRED]
- [[_DispatchSpy]] - `uses` [INFERRED]
- [[cron_state_monitor.py]] - `contains` [EXTRACTED]
- [[lifespan()]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_cron_state_monitor.py]] - `imports` [EXTRACTED]
- [[test_poll_loop_runs_and_stops()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_90