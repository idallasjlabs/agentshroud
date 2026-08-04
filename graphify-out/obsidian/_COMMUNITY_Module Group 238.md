---
type: community
cohesion: 0.12
members: 19
---

# Module Group 238

**Cohesion:** 0.12 - loosely connected
**Members:** 19 nodes

## Members
- [[AgentShroud Data Flow Diagrams (Level 0 Context, Level 1 Security Components, Level 2 MCP Proxy Detail)]] - document - docs/flows/data-flow-diagram.md
- [[AgentShroud Sequence Diagrams (Normal Message, MCP Tool Call, Kill Switch, SSH Command, Web Fetch)]] - document - docs/flows/sequence-diagrams.md
- [[AgentShroud System Architecture Document (SAD)]] - document - docs/architecture/system-architecture.md
- [[Approval Queue (SQLite-based, human-in-the-loop, risk-based queuing)]] - concept - docs/architecture/system-architecture.md
- [[Audit Ledger (SHA-256 Hash Chain, blockchain-inspired, tamper-evident)]] - concept - docs/architecture/system-architecture.md
- [[Data Flow Diagram (TelegramiMessageWebCron → Bot → Gateway PIIAuditApproval → Egress)]] - document - docs/diagrams/03-data.md
- [[Gateway Component (FastAPI, asyncio, uvicorn ASGI, WebSocket support)]] - concept - docs/architecture/system-architecture.md
- [[Incident Response Severity Flow (P1 breachcanary, P2 crashgateway, P3 context reset, P4 minor)]] - document - docs/diagrams/06-operations.md
- [[Kill Switch (3 Modes Monitor, Block, Isolate)]] - concept - docs/architecture/system-architecture.md
- [[Kill Switch Activation Flow (Admin → Dashboard → KillSw → Gateway → all proxies stop → audit → notify)]] - concept - docs/flows/sequence-diagrams.md
- [[MCP Proxy (Model Context Protocol, Tool Authorization, Parameter Validation, Capability Sandboxing)]] - concept - docs/architecture/system-architecture.md
- [[MCP Proxy Detailed Flow (Tool Call Inspection → Permission Check → Rate Limit → Forward → Result Inspection → Audit Log)]] - concept - docs/flows/data-flow-diagram.md
- [[PII Sanitizer (Microsoft Presidio + custom regex, spaCy models)]] - concept - docs/architecture/system-architecture.md
- [[Request Execution Flowchart (User Message → LLM → Tool Call → MCP Inspector → Threat Level → Approval Queue → Execute)]] - document - docs/diagrams/05-behavior.md
- [[SSH Command Flow (Agent → SSHProxy → Injection Check → Approval Queue → Execute → Audit)]] - concept - docs/flows/sequence-diagrams.md
- [[SSH Proxy (Protocol Inspection, Session Recording, Key Management, Privilege Escalation Detection)]] - concept - docs/architecture/system-architecture.md
- [[Transparent Proxy - Zero modification for existing OpenClaw deployments]] - concept - docs/architecture/system-architecture.md
- [[Two-Network Docker Architecture (agentshroud_external + agentshroud_internal)]] - concept - docs/architecture/system-architecture.md
- [[Web Fetch Flow (Agent → WebProxy → URL Analyzer → DNS Check → WebFetch → ContentScan → Agent)]] - concept - docs/flows/sequence-diagrams.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_238
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Module Group 398]]
- 1 edge to [[_COMMUNITY_Module Group 455]]

## Top bridge nodes
- [[AgentShroud System Architecture Document (SAD)]] - degree 10, connects to 1 community
- [[Approval Queue (SQLite-based, human-in-the-loop, risk-based queuing)]] - degree 4, connects to 1 community
- [[Audit Ledger (SHA-256 Hash Chain, blockchain-inspired, tamper-evident)]] - degree 3, connects to 1 community
- [[PII Sanitizer (Microsoft Presidio + custom regex, spaCy models)]] - degree 3, connects to 1 community
