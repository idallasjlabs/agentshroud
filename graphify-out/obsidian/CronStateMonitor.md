---
source_file: "gateway/security/cron_state_monitor.py"
type: "code"
community: "Gateway Test Suite"
location: "L66"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# CronStateMonitor

## Connections
- [[.__init__()_64]] - `method` [EXTRACTED]
- [[._dispatch_aggregate()]] - `method` [EXTRACTED]
- [[._episode_id()]] - `method` [EXTRACTED]
- [[._evaluate()]] - `method` [EXTRACTED]
- [[._run()_1]] - `method` [EXTRACTED]
- [[._safe_dispatch()]] - `method` [EXTRACTED]
- [[.check()_3]] - `method` [EXTRACTED]
- [[.parse_store()]] - `method` [EXTRACTED]
- [[.start()_2]] - `method` [EXTRACTED]
- [[.stop()_9]] - `method` [EXTRACTED]
- [[.test_alert_ids_stable_per_job_episode()]] - `calls` [EXTRACTED]
- [[.test_dispatch_failure_does_not_raise()]] - `calls` [EXTRACTED]
- [[.test_first_sight_failing_alerts_once()]] - `calls` [EXTRACTED]
- [[.test_flood_capped_with_aggregate_alert()]] - `calls` [EXTRACTED]
- [[.test_hermes_jobs_reach_critical_via_observed_runs()]] - `calls` [EXTRACTED]
- [[.test_job_name_capped_in_alert()]] - `calls` [EXTRACTED]
- [[.test_malformed_consecutive_errors_does_not_blind_store()]] - `calls` [EXTRACTED]
- [[.test_multiple_stores_checked()]] - `calls` [EXTRACTED]
- [[.test_ok_to_fail_dispatches_high_alert()]] - `calls` [EXTRACTED]
- [[.test_oversized_store_skipped()]] - `calls` [EXTRACTED]
- [[.test_recovery_refail_realerts_through_real_dedup()]] - `calls` [EXTRACTED]
- [[.test_recovery_resets_alerting()]] - `calls` [EXTRACTED]
- [[.test_repeated_failure_escalates_to_critical()]] - `calls` [EXTRACTED]
- [[.test_start_is_idempotent()]] - `calls` [EXTRACTED]
- [[AlertDispatcher]] - `calls` [INFERRED]
- [[Poll bot cron stores; dispatch AlertDispatcher alerts on failures.]] - `rationale_for` [EXTRACTED]
- [[TestAdversarial]] - `uses` [INFERRED]
- [[TestParsing]] - `uses` [INFERRED]
- [[TestTransitions]] - `uses` [INFERRED]
- [[_DedupDispatchFake]] - `uses` [INFERRED]
- [[_DispatchSpy]] - `uses` [INFERRED]
- [[cron_state_monitor.py]] - `contains` [EXTRACTED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_cron_state_monitor.py]] - `imports` [EXTRACTED]
- [[test_poll_loop_runs_and_stops()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite