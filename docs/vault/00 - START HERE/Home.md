---
type: home
created: 2026-03-03
tags: [index, navigation]
---

# AgentShroud — Vault Home

AgentShroud is a security gateway proxy for autonomous AI agents. Every message, tool call, API request, and outbound connection passes through this gateway before reaching the network or LLM provider. The gateway enforces PII redaction, prompt injection defense, egress filtering, MCP permission enforcement, and human-in-the-loop approval.

---

## Navigate This Vault

| Section | Description |
|---------|-------------|
| [[System Overview]] | What AgentShroud is, architecture summary, key design decisions |
| [[Quick Reference]] | Start / stop / health / emergency cheat sheet |
| [[Architecture Overview]] | Full component map with Mermaid diagram |
| [[Startup Sequence]] | Cold boot to operational (numbered steps) |
| [[Shutdown & Recovery]] | Graceful shutdown and crash recovery |
| [[Data Flow]] | Request flow through every security layer |

---

## Module Index

| Subsystem | Notes |
|-----------|-------|
| [[Gateway Core/main.py\|main.py]] | FastAPI entry point — 3,209 lines |
| [[Gateway Core/config.py\|config.py]] | Configuration loader and Pydantic models |
| [[Gateway Core/sanitizer.py\|sanitizer.py]] | PII detection and redaction (Presidio/spaCy) |
| [[Gateway Core/middleware.py\|middleware.py]] | Security middleware orchestration |
| [[Gateway Core/ledger.py\|ledger.py]] | SQLite audit ledger |
| [[Gateway Core/auth.py\|auth.py]] | Shared-secret authentication |
| [[Gateway Core/models.py\|models.py]] | Pydantic request/response models |
| [[Gateway Core/router.py\|router.py]] | Multi-agent routing |
| [[Gateway Core/event_bus.py\|event_bus.py]] | Event pub/sub |
| [[Gateway Core/version_routes.py\|version_routes.py]] | API version endpoints |
| [[Gateway Core/ssh_config.py\|ssh_config.py]] | SSH host configuration |
| [[Security Modules/prompt_guard.py\|prompt_guard.py]] | Prompt injection detection |
| [[Security Modules/egress_filter.py\|egress_filter.py]] | Outbound domain/IP allowlist |
| [[Security Modules/trust_manager.py\|trust_manager.py]] | Trust scoring and progressive trust |
| [[Security Modules/agent_isolation.py\|agent_isolation.py]] | Agent-level isolation enforcement |
| [[Security Modules/input_normalizer.py\|input_normalizer.py]] | Input normalization |
| [[Security Modules/alert_dispatcher.py\|alert_dispatcher.py]] | Alert routing |
| [[Security Modules/canary.py\|canary.py]] | Canary trap detection |
| [[Security Modules/clamav_scanner.py\|clamav_scanner.py]] | ClamAV malware scanning |
| [[Security Modules/dns_filter.py\|dns_filter.py]] | DNS filtering |
| [[Security Modules/drift_detector.py\|drift_detector.py]] | Configuration drift detection |
| [[Security Modules/encrypted_store.py\|encrypted_store.py]] | AES-256 encrypted storage |
| [[Security Modules/env_guard.py\|env_guard.py]] | Environment variable sandboxing |
| [[Security Modules/falco_monitor.py\|falco_monitor.py]] | Falco SIEM integration |
| [[Security Modules/health_report.py\|health_report.py]] | System health reporting |
| [[Security Modules/key_vault.py\|key_vault.py]] | Key storage and retrieval |
| [[Security Modules/log_sanitizer.py\|log_sanitizer.py]] | Log content sanitization |
| [[Security Modules/oauth_security.py\|oauth_security.py]] | OAuth security hardening |
| [[Security Modules/resource_guard.py\|resource_guard.py]] | Resource quota enforcement |
| [[Security Modules/session_security.py\|session_security.py]] | Session security hardening |
| [[Security Modules/subagent_monitor.py\|subagent_monitor.py]] | Subagent behavior monitoring |
| [[Security Modules/token_validation.py\|token_validation.py]] | Token validation |
| [[Security Modules/trivy_report.py\|trivy_report.py]] | Trivy vulnerability scanning |
| [[Security Modules/wazuh_client.py\|wazuh_client.py]] | Wazuh security monitoring |
| [[Proxy Layer/pipeline.py\|pipeline.py]] | Security pipeline orchestration |
| [[Proxy Layer/mcp_proxy.py\|mcp_proxy.py]] | MCP stdio proxy with gateway inspection |
| [[Proxy Layer/mcp_permissions.py\|mcp_permissions.py]] | MCP permission enforcement |
| [[Proxy Layer/mcp_inspector.py\|mcp_inspector.py]] | MCP message inspection |
| [[Proxy Layer/mcp_audit.py\|mcp_audit.py]] | MCP audit trail |
| [[Proxy Layer/mcp_config.py\|mcp_config.py]] | MCP configuration |
| [[Proxy Layer/telegram_proxy.py\|telegram_proxy.py]] | Telegram API proxy |
| [[Proxy Layer/llm_proxy.py\|llm_proxy.py]] | LLM API proxy |
| [[Proxy Layer/http_proxy.py\|http_proxy.py]] | HTTP CONNECT proxy |
| [[Proxy Layer/forwarder.py\|forwarder.py]] | Protocol forwarding |
| [[Proxy Layer/web_proxy.py\|web_proxy.py]] | Web content proxy with CSP |
| [[Proxy Layer/url_analyzer.py\|url_analyzer.py]] | URL pattern analysis |
| [[Runtime/engine.py\|engine.py]] | Abstract container engine |
| [[Runtime/docker_engine.py\|docker_engine.py]] | Docker integration |
| [[Runtime/podman_engine.py\|podman_engine.py]] | Podman integration |
| [[Runtime/compose_generator.py\|compose_generator.py]] | Docker Compose YAML generation |
| [[Web & Dashboard/api.py\|api.py]] | REST management API |
| [[JavaScript/mcp-proxy-wrapper.js\|mcp-proxy-wrapper.js]] | Node.js MCP stdio proxy |
| [[JavaScript/apply-patches.js\|apply-patches.js]] | OpenClaw config patching |

---

## Configuration & Infrastructure

| Section | Notes |
|---------|-------|
| [[Configuration/agentshroud.yaml\|agentshroud.yaml]] | Master config with annotated breakdown |
| [[Configuration/docker-compose.yml\|docker-compose.yml]] | Primary Docker Compose |
| [[Configuration/Dockerfile.gateway\|Dockerfile.gateway]] | Gateway image (Python 3.13) |
| [[Configuration/Dockerfile.bot\|Dockerfile.bot]] | OpenClaw bot image (Node.js 22) |
| [[Configuration/All Environment Variables\|All Environment Variables]] | Master env var index |
| [[Containers & Services/agentshroud-gateway\|agentshroud-gateway]] | Gateway container details |
| [[Containers & Services/agentshroud-bot\|agentshroud-bot]] | Bot container details |

---

## Operations

| Section | Notes |
|---------|-------|
| [[Runbooks/First Time Setup\|First Time Setup]] | End-to-end initial deployment |
| [[Runbooks/Restart Procedure\|Restart Procedure]] | How to restart safely |
| [[Runbooks/Crash Recovery\|Crash Recovery]] | What to do when the gateway crashes |
| [[Runbooks/Health Checks\|Health Checks]] | Health endpoints and verification |
| [[Runbooks/Kill Switch Procedure\|Kill Switch Procedure]] | Emergency shutdown |
| [[Errors & Troubleshooting/Error Index\|Error Index]] | All known error codes |
| [[Errors & Troubleshooting/Troubleshooting Matrix\|Troubleshooting Matrix]] | Symptom → cause → fix |

---

## Diagrams

| Diagram | Description |
|---------|-------------|
| [[Diagrams/Full System Flowchart\|Full System Flowchart]] | Complete Mermaid system diagram |
| [[Diagrams/Security Pipeline Flow\|Security Pipeline Flow]] | Security layer sequence |
| [[Diagrams/Startup Flow Diagram\|Startup Flow Diagram]] | Boot sequence diagram |
| [[Diagrams/Network Topology\|Network Topology]] | Container network layout |
| [[Diagrams/Dependency Graph\|Dependency Graph]] | Module dependency map |
