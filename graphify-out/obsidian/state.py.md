---
source_file: "gateway/ingest_api/state.py"
type: "code"
community: "PII Sanitizer Pipeline"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# state.py

## Connections
- [[AppState]] - `contains` [EXTRACTED]
- [[DataLedger]] - `imports` [EXTRACTED]
- [[EgressFilter_1]] - `imports` [EXTRACTED]
- [[EnhancedApprovalQueue]] - `imports` [EXTRACTED]
- [[EventBus]] - `imports` [EXTRACTED]
- [[GatewayConfig_1]] - `imports` [EXTRACTED]
- [[HTTPConnectProxy]] - `imports` [EXTRACTED]
- [[MCPProxy]] - `imports` [EXTRACTED]
- [[MultiAgentRouter]] - `imports` [EXTRACTED]
- [[PIISanitizer]] - `imports` [EXTRACTED]
- [[PromptGuard]] - `imports` [EXTRACTED]
- [[SSHProxy]] - `imports` [EXTRACTED]
- [[SecurityPipeline]] - `imports` [EXTRACTED]
- [[TrustManager_1]] - `imports` [EXTRACTED]
- [[UserSessionManager]] - `imports` [EXTRACTED]
- [[approval.py]] - `imports_from` [EXTRACTED]
- [[config.py]] - `imports_from` [EXTRACTED]
- [[dashboard.py]] - `imports_from` [EXTRACTED]
- [[egress_filter.py]] - `imports_from` [EXTRACTED]
- [[enhanced_queue.py]] - `imports_from` [EXTRACTED]
- [[event_bus.py]] - `imports_from` [EXTRACTED]
- [[forward.py]] - `imports_from` [EXTRACTED]
- [[health.py]] - `imports_from` [EXTRACTED]
- [[http_proxy.py]] - `imports_from` [EXTRACTED]
- [[ledger.py]] - `imports_from` [EXTRACTED]
- [[lifespan.py]] - `imports_from` [EXTRACTED]
- [[main.py_2]] - `imports_from` [EXTRACTED]
- [[mcp_proxy.py]] - `imports_from` [EXTRACTED]
- [[pipeline.py]] - `imports_from` [EXTRACTED]
- [[prompt_guard.py]] - `imports_from` [EXTRACTED]
- [[proxy.py]] - `imports_from` [EXTRACTED]
- [[router.py]] - `imports_from` [EXTRACTED]
- [[sanitizer.py]] - `imports_from` [EXTRACTED]
- [[test_telegram_proxy_inbound.py]] - `imports_from` [EXTRACTED]
- [[test_telegram_proxy_outbound.py]] - `imports_from` [EXTRACTED]
- [[trust_manager.py]] - `imports_from` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline