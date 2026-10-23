---
source_file: "docs/papers/agentshroud-whitepaper.md"
type: "concept"
community: "1Password op-proxy (POST /credentials/op-proxy; validates GATEWAY_AUTH_TOKEN + allowed_op_paths; cascading retry 5s,10s,15s,30s,60s)"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/1Password_op-proxy_POST_/credentials/op-proxy_validates_GATEWAY_AUTH_TOKEN__allowed_op_paths_cascading_retry_5s10s15s30s60s
---

# Approval Queue (human-in-the-loop)

## Connections
- [[Agent Decision Logic Flowchart]] - `conceptually_related_to` [EXTRACTED]
- [[AgentShroud White Paper v1.1 (Feb 2026)]] - `references` [EXTRACTED]
- [[Alert Thresholds (health check 3x10s, 200K token hard limit196K compaction trigger, 1h approval timeout, 90-day ledger retention, op-proxy 6 cascading retries)]] - `references` [EXTRACTED]
- [[Approval Queue State Diagram (pending → approvedrejectedexpired)]] - `conceptually_related_to` [EXTRACTED]
- [[Approval queue data (in-memory, backed by SQLite)]] - `semantically_similar_to` [INFERRED]
- [[MCP Inspector (injection scan, PII scan, sensitive-op scan; ThreatLevel NONELOWMEDIUMHIGH)]] - `shares_data_with` [EXTRACTED]
- [[Phase 2 — Security Core HTTP CONNECT Proxy, MCP Proxy Inspector, Approval Queue, SSH Proxy]] - `references` [EXTRACTED]
- [[Severity matrix P1 Critical  P2 High  P3 Medium  P4 Low, with owners and response windows]] - `references` [EXTRACTED]
- [[enforcement-audit-script.py (P0P1P2 module smoke test)]] - `implements` [EXTRACTED]
- [[ledger.db — audit ledger (Layer 3 persistence; hash-only, 90-day retention, auto-purge at expires_at)]] - `shares_data_with` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/1Password_op-proxy_POST_/credentials/op-proxy_validates_GATEWAY_AUTH_TOKEN__allowed_op_paths_cascading_retry_5s10s15s30s60s
