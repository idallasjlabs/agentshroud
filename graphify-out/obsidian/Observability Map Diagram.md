---
source_file: "docs/diagrams/images/diagram-20-observability-map.png"
type: "image"
community: "1Password op-proxy (POST /credentials/op-proxy; validates GATEWAY_AUTH_TOKEN + allowed_op_paths; cascading retry 5s,10s,15s,30s,60s)"
tags:
  - graphify/image
  - graphify/EXTRACTED
  - community/1Password_op-proxy_POST_/credentials/op-proxy_validates_GATEWAY_AUTH_TOKEN__allowed_op_paths_cascading_retry_5s10s15s30s60s
---

# Observability Map Diagram

## Connections
- [[Alert Thresholds (health check 3x10s, 200K token hard limit196K compaction trigger, 1h approval timeout, 90-day ledger retention, op-proxy 6 cascading retries)]] - `conceptually_related_to` [EXTRACTED]
- [[Observability Gaps (future work) no centralised log aggregation (ELKLoki), no metrics export (Prometheus), no uptime monitor, Zabbix installed but not configured]] - `conceptually_related_to` [EXTRACTED]
- [[Phase 5 — Stability Context limit fix (Patch 4), MCP key crash fix (Patch 3), Documentation & Diagrams]] - `references` [EXTRACTED]
- [[What Is Instrumented (bot apihealth, gateway status and ledger, MCP audit log, HTTP CONNECT proxy stats)]] - `conceptually_related_to` [EXTRACTED]

#graphify/image #graphify/EXTRACTED #community/1Password_op-proxy_POST_/credentials/op-proxy_validates_GATEWAY_AUTH_TOKEN__allowed_op_paths_cascading_retry_5s10s15s30s60s
