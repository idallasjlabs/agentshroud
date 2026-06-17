---
source_file: "gateway/ingest_api/config.py"
type: "code"
community: "Enhanced Approval Queue"
location: "L201"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Enhanced_Approval_Queue
---

# ToolRiskConfig

## Connections
- [[Any]] - `uses` [INFERRED]
- [[ApprovalQueueConfig]] - `uses` [INFERRED]
- [[ApprovalQueueItem]] - `uses` [INFERRED]
- [[ApprovalRequest]] - `uses` [INFERRED]
- [[ApprovalStore]] - `uses` [INFERRED]
- [[BaseModel]] - `inherits` [EXTRACTED]
- [[BotConfig]] - `uses` [INFERRED]
- [[EnhancedApprovalQueue]] - `uses` [INFERRED]
- [[SSHConfig]] - `uses` [INFERRED]
- [[TestApprovalWorkflow]] - `uses` [INFERRED]
- [[TestMCPProxyIntegration]] - `uses` [INFERRED]
- [[TestPersistence]] - `uses` [INFERRED]
- [[TestToolRiskClassification]] - `uses` [INFERRED]
- [[Tool risk tier configuration]] - `rationale_for` [EXTRACTED]
- [[ToolRiskConfig]] - `uses` [INFERRED]
- [[ToolRiskPolicy]] - `uses` [INFERRED]
- [[WebSocket]] - `uses` [INFERRED]
- [[config.py]] - `contains` [EXTRACTED]
- [[enhanced_queue.py]] - `imports` [EXTRACTED]
- [[load_config()]] - `calls` [EXTRACTED]
- [[test_enhanced_approval.py]] - `imports` [EXTRACTED]
- [[test_websocket_notifications()]] - `calls` [EXTRACTED]
- [[tool_risk_config()]] - `calls` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Enhanced_Approval_Queue