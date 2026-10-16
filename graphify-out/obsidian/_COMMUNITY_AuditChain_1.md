---
type: community
cohesion: 0.05
members: 48
---

# AuditChain

**Cohesion:** 0.05 - loosely connected
**Members:** 48 nodes

## Members
- [[Add a domain to the local denylist. Authentication required.]] - rationale - gateway/ingest_api/main.py
- [[Add an egress allowdeny rule.]] - rationale - gateway/ingest_api/main.py
- [[Approve an egress request (oncesessionpermanent).]] - rationale - gateway/ingest_api/main.py
- [[Build normalized scanner summary for SOCdashboard telemetry.]] - rationale - gateway/ingest_api/main.py
- [[CIS Docker Benchmark checks for this container.]] - rationale - gateway/ingest_api/main.py
- [[Deny an egress request (oncesessionpermanent).]] - rationale - gateway/ingest_api/main.py
- [[Discard (keep quarantined) a blocked message after admin review.]] - rationale - gateway/ingest_api/main.py
- [[Discard a blocked outbound message after admin review.]] - rationale - gateway/ingest_api/main.py
- [[Enabledisable emergency block-all for outbound egress.]] - rationale - gateway/ingest_api/main.py
- [[Execute SSH command with validation and approval]] - rationale - gateway/ingest_api/main.py
- [[Persist last scanner result and emit live event-bus telemetry.]] - rationale - gateway/ingest_api/main.py
- [[Release a blocked outbound message for adminmanual resend flow.]] - rationale - gateway/ingest_api/main.py
- [[Release a quarantined message for admin workflow follow-up.]] - rationale - gateway/ingest_api/main.py
- [[Return normalized scanner state + latest results for SOCdashboard views.]] - rationale - gateway/ingest_api/main.py
- [[Run ClamAV antivirus scan. Tries clamdscan (daemon) first, falls back to…]] - rationale - gateway/ingest_api/main.py
- [[Run OpenSCAP XCCDF evaluation against the running container.]] - rationale - gateway/ingest_api/main.py
- [[Run Trivy vulnerability scan.]] - rationale - gateway/ingest_api/main.py
- [[Run all locally available security scanners and return consolidated results.]] - rationale - gateway/ingest_api/main.py
- [[Run canary integrity checks.]] - rationale - gateway/ingest_api/main.py
- [[Run kill switch verification test. Args dry_run If True (default), only…]] - rationale - gateway/ingest_api/main.py
- [[SSHExecRequest]] - code
- [[SSHWriteFileRequest_1]] - code
- [[Trigger an immediate blocklist refresh from upstream adlists. Authentication…]] - rationale - gateway/ingest_api/main.py
- [[Write file content to an allowlisted SSH host via structured transport. Unlike…]] - rationale - gateway/ingest_api/main.py
- [[_execute_and_record()]] - code - gateway/ingest_api/main.py
- [[_record_scanner_result()]] - code - gateway/ingest_api/main.py
- [[_scanner_summary()]] - code - gateway/ingest_api/main.py
- [[add()]] - code - gateway/ingest_api/main.py
- [[add_blocked_domain()]] - code - gateway/ingest_api/main.py
- [[discard_blocked_message()]] - code - gateway/ingest_api/main.py
- [[discard_blocked_outbound()]] - code - gateway/ingest_api/main.py
- [[egress_add_rule()]] - code - gateway/ingest_api/main.py
- [[egress_approve()]] - code - gateway/ingest_api/main.py
- [[egress_deny()]] - code - gateway/ingest_api/main.py
- [[egress_emergency_block()]] - code - gateway/ingest_api/main.py
- [[post_1]] - code
- [[refresh_dns_blocklist()]] - code - gateway/ingest_api/main.py
- [[release_blocked_message()]] - code - gateway/ingest_api/main.py
- [[release_blocked_outbound()]] - code - gateway/ingest_api/main.py
- [[run_all_scanners()]] - code - gateway/ingest_api/main.py
- [[run_canary_checks()]] - code - gateway/ingest_api/main.py
- [[run_cis_benchmark()]] - code - gateway/ingest_api/main.py
- [[run_clamav_scan()]] - code - gateway/ingest_api/main.py
- [[run_openscap_scan()]] - code - gateway/ingest_api/main.py
- [[run_trivy_scan()]] - code - gateway/ingest_api/main.py
- [[ssh_exec()]] - code - gateway/ingest_api/main.py
- [[ssh_write_file()]] - code - gateway/ingest_api/main.py
- [[verify_killswitch()]] - code - gateway/ingest_api/main.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AuditChain
SORT file.name ASC
```

## Connections to other communities
- 42 edges to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 2 edges to [[_COMMUNITY_test_prompt_guard.py_2]]
- 1 edge to [[_COMMUNITY__is_op_reference_allowed]]
- 1 edge to [[_COMMUNITY_deep_security_test]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL_4]]
- 1 edge to [[_COMMUNITY_test_main_endpoints.py]]

## Top bridge nodes
- [[post_1]] - degree 25, connects to 5 communities
- [[_record_scanner_result()]] - degree 7, connects to 1 community
- [[_scanner_summary()]] - degree 7, connects to 1 community
- [[run_all_scanners()]] - degree 6, connects to 1 community
- [[ssh_exec()]] - degree 6, connects to 1 community
