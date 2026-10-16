---
type: community
cohesion: 0.06
members: 63
---

# ProxyDashboard

**Cohesion:** 0.06 - loosely connected
**Members:** 63 nodes

## Members
- [[dot-__init__()_49]] - code - gateway/dashboard/proxy_status.py
- [[dot-get_display()]] - code - gateway/dashboard/proxy_status.py
- [[dot-get_report()]] - code - gateway/dashboard/proxy_status.py
- [[dot-record_message_proxied()]] - code - gateway/dashboard/proxy_status.py
- [[dot-record_pii_redaction()]] - code - gateway/dashboard/proxy_status.py
- [[dot-set_mode()]] - code - gateway/dashboard/proxy_status.py
- [[dot-to_display()]] - code - gateway/dashboard/proxy_status.py
- [[dot-update_audit_status()]] - code - gateway/dashboard/proxy_status.py
- [[dot-update_canary()]] - code - gateway/dashboard/proxy_status.py
- [[dot-update_direct_access()]] - code - gateway/dashboard/proxy_status.py
- [[Collects status from all security components and generates reports.]] - rationale - gateway/dashboard/proxy_status.py
- [[Complete proxy status report for the dashboard.]] - rationale - gateway/dashboard/proxy_status.py
- [[Dashboard display should include all required fields.]] - rationale - gateway/tests/test_proxy_dashboard.py
- [[Dashboard should count PII redactions.]] - rationale - gateway/tests/test_proxy_dashboard.py
- [[Dashboard should default to unprotected mode.]] - rationale - gateway/tests/test_proxy_dashboard.py
- [[Dashboard should reflect proxy mode.]] - rationale - gateway/tests/test_proxy_dashboard.py
- [[Dashboard should reflect sidecar mode with warning.]] - rationale - gateway/tests/test_proxy_dashboard.py
- [[Dashboard should show audit chain status.]] - rationale - gateway/tests/test_proxy_dashboard.py
- [[Dashboard should show broken audit chain.]] - rationale - gateway/tests/test_proxy_dashboard.py
- [[Dashboard should show failed canary.]] - rationale - gateway/tests/test_proxy_dashboard.py
- [[Dashboard should track canary results.]] - rationale - gateway/tests/test_proxy_dashboard.py
- [[Dashboard should track direct access status.]] - rationale - gateway/tests/test_proxy_dashboard.py
- [[Dashboard should track proxied messages.]] - rationale - gateway/tests/test_proxy_dashboard.py
- [[Dashboard should track uptime.]] - rationale - gateway/tests/test_proxy_dashboard.py
- [[ProxyDashboard]] - code - gateway/dashboard/proxy_status.py
- [[ProxyStatusReport]] - code - gateway/dashboard/proxy_status.py
- [[ProxyStatusReport.to_display should produce readable strings.]] - rationale - gateway/tests/test_proxy_dashboard.py
- [[Return human-readable dashboard strings.]] - rationale - gateway/dashboard/proxy_status.py
- [[check()_7]] - code - scripts/preflight-check.sh
- [[fail()_1]] - code - scripts/tailscale-check.sh
- [[fail()_2]] - code - scripts/verify-proxy.sh
- [[info()_1]] - code - scripts/verify-proxy.sh
- [[infra-check.sh]] - code - scripts/infra-check.sh
- [[infra-check.sh script]] - code - scripts/infra-check.sh
- [[ok()]] - code - scripts/tailscale-check.sh
- [[pass()_1]] - code - scripts/verify-proxy.sh
- [[preflight-check.sh]] - code - scripts/preflight-check.sh
- [[preflight-check.sh script]] - code - scripts/preflight-check.sh
- [[proxy_status.py]] - code - gateway/dashboard/proxy_status.py
- [[run_bypass()]] - code - scripts/verify-proxy.sh
- [[run_canary()_1]] - code - scripts/verify-proxy.sh
- [[run_chain()]] - code - scripts/verify-proxy.sh
- [[run_full()]] - code - scripts/verify-proxy.sh
- [[run_quick()]] - code - scripts/verify-proxy.sh
- [[tailscale-check.sh]] - code - scripts/tailscale-check.sh
- [[tailscale-check.sh script]] - code - scripts/tailscale-check.sh
- [[test_dashboard_audit_broken()]] - code - gateway/tests/test_proxy_dashboard.py
- [[test_dashboard_audit_status()]] - code - gateway/tests/test_proxy_dashboard.py
- [[test_dashboard_canary_failed()]] - code - gateway/tests/test_proxy_dashboard.py
- [[test_dashboard_canary_status()]] - code - gateway/tests/test_proxy_dashboard.py
- [[test_dashboard_default_unprotected()]] - code - gateway/tests/test_proxy_dashboard.py
- [[test_dashboard_direct_access()]] - code - gateway/tests/test_proxy_dashboard.py
- [[test_dashboard_display_all_fields()]] - code - gateway/tests/test_proxy_dashboard.py
- [[test_dashboard_message_tracking()]] - code - gateway/tests/test_proxy_dashboard.py
- [[test_dashboard_pii_counting()]] - code - gateway/tests/test_proxy_dashboard.py
- [[test_dashboard_set_proxy_mode()]] - code - gateway/tests/test_proxy_dashboard.py
- [[test_dashboard_set_sidecar_mode()]] - code - gateway/tests/test_proxy_dashboard.py
- [[test_dashboard_uptime()]] - code - gateway/tests/test_proxy_dashboard.py
- [[test_proxy_dashboard.py]] - code - gateway/tests/test_proxy_dashboard.py
- [[test_status_report_to_display()]] - code - gateway/tests/test_proxy_dashboard.py
- [[verify-proxy.sh]] - code - scripts/verify-proxy.sh
- [[verify-proxy.sh script]] - code - scripts/verify-proxy.sh
- [[warn()_3]] - code - scripts/tailscale-check.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ProxyDashboard
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 1 edge to [[_COMMUNITY_api.py]]
- 1 edge to [[_COMMUNITY_test_security_toolchain.py]]
- 1 edge to [[_COMMUNITY_test_e2e_proxy.py]]

## Top bridge nodes
- [[proxy_status.py]] - degree 4, connects to 2 communities
- [[ProxyDashboard]] - degree 27, connects to 1 community
- [[run_canary()_1]] - degree 11, connects to 1 community
- [[run_full()]] - degree 10, connects to 1 community
- [[run_quick()]] - degree 9, connects to 1 community
