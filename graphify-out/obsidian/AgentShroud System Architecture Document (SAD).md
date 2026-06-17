---
source_file: "docs/architecture/system-architecture.md"
type: "document"
community: "Module Group 238"
location: "line 1"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Module_Group_238
---

# AgentShroud System Architecture Document (SAD)

## Connections
- [[AgentShroud Deployment Architecture Document]] - `references` [INFERRED]
- [[Approval Queue (SQLite-based, human-in-the-loop, risk-based queuing)]] - `describes` [EXTRACTED]
- [[Audit Ledger (SHA-256 Hash Chain, blockchain-inspired, tamper-evident)]] - `describes` [EXTRACTED]
- [[Gateway Component (FastAPI, asyncio, uvicorn ASGI, WebSocket support)]] - `describes` [EXTRACTED]
- [[Kill Switch (3 Modes Monitor, Block, Isolate)]] - `describes` [EXTRACTED]
- [[MCP Proxy (Model Context Protocol, Tool Authorization, Parameter Validation, Capability Sandboxing)]] - `describes` [EXTRACTED]
- [[PII Sanitizer (Microsoft Presidio + custom regex, spaCy models)]] - `describes` [EXTRACTED]
- [[SSH Proxy (Protocol Inspection, Session Recording, Key Management, Privilege Escalation Detection)]] - `describes` [EXTRACTED]
- [[Transparent Proxy - Zero modification for existing OpenClaw deployments]] - `describes` [EXTRACTED]
- [[Two-Network Docker Architecture (agentshroud_external + agentshroud_internal)]] - `describes` [EXTRACTED]

#graphify/document #graphify/EXTRACTED #community/Module_Group_238