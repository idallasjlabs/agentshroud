---
type: community
cohesion: 0.08
members: 26
---

# Data flow (01 - Architecture)

**Cohesion:** 0.08 - loosely connected
**Members:** 26 nodes

## Members
- [[1. MCP Proxy Wrapper (Bot Side)]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[11. Ledger Recording]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[2. Authentication (Gateway Entry)]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[3. Middleware Manager]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[4. Input Normalization]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[5. PII Sanitization]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[6. Prompt Injection Defense]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[7-Layer Defense Architecture]] - document - docs/architecture/agentic-os.md
- [[9. Proxy Routing]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Data Flow_1]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Key Classes_1]] - document - docs/vault/02 - Modules/Proxy Layer/pipeline.py.md
- [[Layer Reference]] - document - docs/vault/09 - Diagrams/Security Pipeline Flow.md
- [[Layer-by-Layer Breakdown]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Module Count by Layer]] - document - docs/architecture/agentic-os.md
- [[Monitor Mode]] - document - docs/vault/09 - Diagrams/Security Pipeline Flow.md
- [[Overview_19]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Overview_24]] - document - docs/vault/09 - Diagrams/Security Pipeline Flow.md
- [[Proxy Layer]] - document - docs/architecture/agentic-os.md
- [[Related Notes_3]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Related Notes_73]] - document - docs/vault/09 - Diagrams/Security Pipeline Flow.md
- [[Request Flow Diagram]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Response Path]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[`AuditChain`]] - document - docs/vault/02 - Modules/Proxy Layer/pipeline.py.md
- [[`PipelineAction` (Enum)]] - document - docs/vault/02 - Modules/Proxy Layer/pipeline.py.md
- [[`PipelineResult` (Dataclass)]] - document - docs/vault/02 - Modules/Proxy Layer/pipeline.py.md
- [[`SecurityPipeline`]] - document - docs/vault/02 - Modules/Proxy Layer/pipeline.py.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Data_flow_01_-_Architecture
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Agentic Os (architecture)]]
- 1 edge to [[_COMMUNITY_System overview (00 - START HERE)]]
- 1 edge to [[_COMMUNITY_Egress Filter.py (Security Modules)]]
- 1 edge to [[_COMMUNITY_Shutdown & recovery (01 - Architecture)]]
- 1 edge to [[_COMMUNITY_Pipeline.py (Proxy Layer)]]
- 1 edge to [[_COMMUNITY_Network topology (09 - Diagrams)]]

## Top bridge nodes
- [[Layer-by-Layer Breakdown]] - degree 12, connects to 2 communities
- [[`SecurityPipeline`]] - degree 11, connects to 2 communities
- [[Data Flow_1]] - degree 6, connects to 1 community
- [[Key Classes_1]] - degree 5, connects to 1 community