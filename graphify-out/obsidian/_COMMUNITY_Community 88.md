---
type: community
cohesion: 0.04
members: 62
---

# Community 88

**Cohesion:** 0.04 - loosely connected
**Members:** 62 nodes

## Members
- [[.__del__()]] - code - gateway/security/resource_guard.py
- [[.__init__()_114]] - code - gateway/security/resource_guard.py
- [[._alert_high_usage()]] - code - gateway/security/resource_guard.py
- [[._check_system_resources()_1]] - code - gateway/security/resource_guard.py
- [[._cleanup_expired_usage()]] - code - gateway/security/resource_guard.py
- [[._get_disk_io_stats()]] - code - gateway/security/resource_guard.py
- [[._monitor_resources()]] - code - gateway/security/resource_guard.py
- [[._start_monitoring_task()]] - code - gateway/security/resource_guard.py
- [[.add_alert_callback()_1]] - code - gateway/security/resource_guard.py
- [[.check_cpu_limit()]] - code - gateway/security/resource_guard.py
- [[.check_disk_write_limit()]] - code - gateway/security/resource_guard.py
- [[.check_memory_limit()]] - code - gateway/security/resource_guard.py
- [[.check_resource()]] - code - gateway/security/resource_guard.py
- [[.check_vram_headroom()]] - code - gateway/security/resource_guard.py
- [[.cleanup_temp_files()]] - code - gateway/security/resource_guard.py
- [[.get_usage_stats()]] - code - gateway/security/resource_guard.py
- [[.register_temp_file()]] - code - gateway/security/resource_guard.py
- [[.start_request_tracking()]] - code - gateway/security/resource_guard.py
- [[.stop()_11]] - code - gateway/security/resource_guard.py
- [[.stop_monitoring()]] - code - gateway/security/resource_guard.py
- [[.test_check_cpu_limit_returns_false_on_exception()]] - code - gateway/tests/test_round2_hardening.py
- [[.test_check_disk_write_limit_returns_false_on_exception()]] - code - gateway/tests/test_round2_hardening.py
- [[.test_check_memory_limit_returns_false_on_exception()]] - code - gateway/tests/test_round2_hardening.py
- [[.test_cpu_limit_check()]] - code - gateway/tests/test_security_audit.py
- [[.test_disk_write_limit()]] - code - gateway/tests/test_security_audit.py
- [[.test_memory_limit_check()]] - code - gateway/tests/test_security_audit.py
- [[.test_resource_guard_init()]] - code - gateway/tests/test_security_audit.py
- [[.test_usage_stats()]] - code - gateway/tests/test_security_audit.py
- [[128k token request at 4 bytestoken KV cache triggers rejection at 4096 MB headr]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Add a callback function to be called when resource alerts are triggered.]] - rationale - gateway/security/resource_guard.py
- [[Any_57]] - code - gateway/security/resource_guard.py
- [[Background task to monitor resource usage and trigger alerts.]] - rationale - gateway/security/resource_guard.py
- [[Best-effort cleanup for test contexts that don't call stop().]] - rationale - gateway/security/resource_guard.py
- [[Check if agent has exceeded CPU time limit.]] - rationale - gateway/security/resource_guard.py
- [[Check if agent has exceeded disk write limit.]] - rationale - gateway/security/resource_guard.py
- [[Check if agent has exceeded memory limit.]] - rationale - gateway/security/resource_guard.py
- [[Check if resource usage is allowed for an agent.          Args             agen]] - rationale - gateway/security/resource_guard.py
- [[Check system-wide resource usage for anomalies (synchronous).]] - rationale - gateway/security/resource_guard.py
- [[Clean up old usage data (older than 5 minutes).]] - rationale - gateway/security/resource_guard.py
- [[Clean up temporary files for an agent.]] - rationale - gateway/security/resource_guard.py
- [[Current resource usage metrics.]] - rationale - gateway/security/resource_guard.py
- [[Get current disk IO statistics.]] - rationale - gateway/security/resource_guard.py
- [[Get current usage statistics.]] - rationale - gateway/security/resource_guard.py
- [[Monitor and limit resource usage per agentrequest.]] - rationale - gateway/security/resource_guard.py
- [[Pre-flight VRAM headroom check before dispatching a long-context local-model cal]] - rationale - gateway/security/resource_guard.py
- [[Register a temporary file for tracking.]] - rationale - gateway/security/resource_guard.py
- [[ResourceGuard]] - code - gateway/security/resource_guard.py
- [[ResourceUsage]] - code - gateway/security/resource_guard.py
- [[Small context request passes VRAM headroom check.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Start background monitoring task.]] - rationale - gateway/security/resource_guard.py
- [[Start tracking resources for a specific agentrequest.]] - rationale - gateway/security/resource_guard.py
- [[Stop background monitoring task cleanly.]] - rationale - gateway/security/resource_guard.py
- [[Stop background monitoring.]] - rationale - gateway/security/resource_guard.py
- [[TestResourceGuardFailClosed]] - code - gateway/tests/test_round2_hardening.py
- [[Trigger a resource usage alert synchronously.]] - rationale - gateway/security/resource_guard.py
- [[VRAM check is skipped when max_vram_headroom_mb=0 (disabled).]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[Verify resource check methods return False (deny) on exception.]] - rationale - gateway/tests/test_round2_hardening.py
- [[check_vram_headroom raises VRAMHeadroomError when estimated VRAM exceeds budget.]] - rationale - gateway/tests/test_llm_proxy_local_parity.py
- [[test_resource_guard_vram_estimate_128k_tokens_triggers_rejection()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_resource_guard_vram_headroom_check_allows_small_context()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_resource_guard_vram_headroom_check_disabled_when_threshold_zero()]] - code - gateway/tests/test_llm_proxy_local_parity.py
- [[test_resource_guard_vram_headroom_check_raises_on_insufficient_vram()]] - code - gateway/tests/test_llm_proxy_local_parity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_88
SORT file.name ASC
```

## Connections to other communities
- 23 edges to [[_COMMUNITY_Community 225]]
- 18 edges to [[_COMMUNITY_Security Audit & Drift Detection]]
- 13 edges to [[_COMMUNITY_Community 18]]
- 10 edges to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 6 edges to [[_COMMUNITY_Community 807]]
- 5 edges to [[_COMMUNITY_Community 54]]
- 3 edges to [[_COMMUNITY_Community 850]]
- 3 edges to [[_COMMUNITY_Community 351]]
- 1 edge to [[_COMMUNITY_Ingest API & Approval Routes]]
- 1 edge to [[_COMMUNITY_Middleware & Lifespan]]
- 1 edge to [[_COMMUNITY_Adversarial Injection Guards]]
- 1 edge to [[_COMMUNITY_Community 50]]
- 1 edge to [[_COMMUNITY_Community 918]]

## Top bridge nodes
- [[ResourceGuard]] - degree 93, connects to 11 communities
- [[TestResourceGuardFailClosed]] - degree 11, connects to 4 communities
- [[test_resource_guard_vram_estimate_128k_tokens_triggers_rejection()]] - degree 4, connects to 2 communities
- [[test_resource_guard_vram_headroom_check_allows_small_context()]] - degree 4, connects to 2 communities
- [[test_resource_guard_vram_headroom_check_disabled_when_threshold_zero()]] - degree 4, connects to 2 communities