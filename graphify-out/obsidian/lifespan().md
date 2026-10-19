---
source_file: "gateway/ingest_api/lifespan.py"
type: "code"
community: "lifespan()"
location: "L108"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/lifespan
---

# lifespan()

## Connections
- [[DataLedger]] - `calls` [EXTRACTED]
- [[EgressFilter_2]] - `calls` [EXTRACTED]
- [[FastAPI]] - `references` [EXTRACTED]
- [[FastAPI lifespan - startup and shutdown]] - `rationale_for` [EXTRACTED]
- [[MiddlewareManager]] - `calls` [EXTRACTED]
- [[PromptGuard_1]] - `calls` [EXTRACTED]
- [[SecurityPipeline_1]] - `calls` [EXTRACTED]
- [[_alert_sanitize()]] - `indirect_call` [INFERRED]
- [[_audit_chain_heartbeat()]] - `contains` [EXTRACTED]
- [[_build_per_bot_telegram_tokens()]] - `calls` [EXTRACTED]
- [[_check_trivy_report()]] - `contains` [EXTRACTED]
- [[_install_uvicorn_warning_filter()]] - `calls` [EXTRACTED]
- [[_on_config_reload()]] - `indirect_call` [INFERRED]
- [[_op_authenticate()]] - `contains` [EXTRACTED]
- [[_prewarm_op()]] - `indirect_call` [INFERRED]
- [[_report_sanitize()]] - `indirect_call` [INFERRED]
- [[_resource_alert_bridge()]] - `indirect_call` [INFERRED]
- [[_run_canvas_proxy()]] - `contains` [EXTRACTED]
- [[_run_hermes_api_forwarder()]] - `contains` [EXTRACTED]
- [[_run_hermes_dashboard_forwarder()]] - `contains` [EXTRACTED]
- [[_run_initial_scan_if_needed()]] - `contains` [EXTRACTED]
- [[_run_security_scheduler()]] - `contains` [EXTRACTED]
- [[_startup_scanner()]] - `contains` [EXTRACTED]
- [[_verify_bot_image()]] - `contains` [EXTRACTED]
- [[_wazuh_periodic()]] - `contains` [EXTRACTED]
- [[ingest_apimain.py]] - `imports` [EXTRACTED]
- [[lifespan.py]] - `contains` [EXTRACTED]
- [[main.py]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/lifespan
