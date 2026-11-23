---
type: community
members: 30
---

# Architecture Overview.md

**Members:** 30 nodes

## Members
- [[dot-agentsagentssav]] - document - .agents/agents/sav.md
- [[dot-cursoragentssav]] - document - .cursor/agents/sav.md
- [[dot-ompagentssav]] - document - .omp/agents/sav.md
- [[dot-opencodeagentssav]] - document - .opencode/agents/sav.md
- [[Architecture Overview]] - document - docs/vault/01 - Architecture/Architecture Overview.md
- [[Complete System Diagram]] - document - docs/vault/09 - Diagrams/Full System Flowchart.md
- [[Crash Recovery_1]] - document - docs/vault/08 - Runbooks/Crash Recovery.md
- [[Data Flow]] - document - docs/vault/01 - Architecture/Data Flow.md
- [[Error Index]] - document - docs/vault/07 - Errors & Troubleshooting/Error Index.md
- [[First Time Setup_1]] - document - docs/vault/08 - Runbooks/First Time Setup.md
- [[Full System Flowchart_1]] - document - docs/vault/09 - Diagrams/Full System Flowchart.md
- [[Full System Flowchart]] - document - docs/vault/09 - Diagrams/Full System Flowchart.md
- [[Home]] - document - docs/vault/00 - START HERE/Home.md
- [[Kill Switch Procedure_1]] - document - docs/vault/08 - Runbooks/Kill Switch Procedure.md
- [[Legend]] - document - docs/vault/09 - Diagrams/Full System Flowchart.md
- [[Quick Reference]] - document - docs/vault/00 - START HERE/Quick Reference.md
- [[Related Notes_23]] - document - docs/vault/09 - Diagrams/Full System Flowchart.md
- [[Restart Procedure]] - document - docs/vault/08 - Runbooks/Restart Procedure.md
- [[Shutdown & Recovery_1]] - document - docs/vault/01 - Architecture/Shutdown & Recovery.md
- [[Startup Flow Diagram (vault note)]] - document - docs/vault/09 - Diagrams/Startup Flow Diagram.md
- [[Startup Sequence_1]] - document - docs/vault/01 - Architecture/Startup Sequence.md
- [[i-sav README (System Audit Vault)]] - document - docker/config/hermes/skills/i-sav/README.md
- [[i-sav SKILL (System Audit Vault, Obsidian)]] - document - docker/config/hermes/skills/i-sav/SKILL.md
- [[i-sav.agent]] - document - .github/agents/i-sav.agent.md
- [[main.py]] - document - docs/vault/02 - Modules/Gateway Core/main.py.md
- [[mcp_proxy.py_1]] - document - docs/vault/02 - Modules/Proxy Layer/mcp_proxy.py.md
- [[openclawskillsi-savSKILL]] - document - docker/config/openclaw/skills/i-sav/SKILL.md
- [[pipeline.py]] - document - docs/vault/02 - Modules/Proxy Layer/pipeline.py.md
- [[router.py_1]] - document - docs/vault/02 - Modules/Gateway Core/router.py.md
- [[savSKILL]] - document - .agents/skills/sav/SKILL.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Architecture_Overviewmd
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_middleware.py_1]]
- 1 edge to [[_COMMUNITY_clamav_scanner.py]]
- 1 edge to [[_COMMUNITY_prompt_guard.py_1]]
- 1 edge to [[_COMMUNITY_Gateway Python Dependencies (`gatewayrequirements.txt`)]]
- 1 edge to [[_COMMUNITY_auth.py]]
- 1 edge to [[_COMMUNITY_ledger.py]]
- 1 edge to [[_COMMUNITY_sanitizer.py]]
- 1 edge to [[_COMMUNITY_version_routes.py_1]]
- 1 edge to [[_COMMUNITY_agent_isolation.py]]
- 1 edge to [[_COMMUNITY_dns_filter.py]]
- 1 edge to [[_COMMUNITY_ANTHROPIC_BASE_URL]]
- 1 edge to [[_COMMUNITY_agentshroud-bot]]
- 1 edge to [[_COMMUNITY_agentshroud-gateway]]
- 1 edge to [[_COMMUNITY_Shutdown & Recovery]]
- 1 edge to [[_COMMUNITY_egress_filter.py]]
- 1 edge to [[_COMMUNITY_input_normalizer.py]]
- 1 edge to [[_COMMUNITY_event_bus.py]]
- 1 edge to [[_COMMUNITY_mcp-proxy-wrapper.js_1]]
- 1 edge to [[_COMMUNITY_Function Details_4]]
- 1 edge to [[_COMMUNITY_canary.py]]
- 1 edge to [[_COMMUNITY_Gateway Container Startup Failures]]
- 1 edge to [[_COMMUNITY_router.py]]
- 1 edge to [[_COMMUNITY_Troubleshooting Matrix]]
- 1 edge to [[_COMMUNITY_Health Checks]]
- 1 edge to [[_COMMUNITY_Kill Switch Procedure]]
- 1 edge to [[_COMMUNITY_Startup Sequence]]
- 1 edge to [[_COMMUNITY_ssh_config.py]]
- 1 edge to [[_COMMUNITY_apply-patches.js_1]]
- 1 edge to [[_COMMUNITY_First Time Setup]]
- 1 edge to [[_COMMUNITY_Quick Reference — AgentShroud]]
- 1 edge to [[_COMMUNITY_Dockerfile — Bot (OpenClaw)]]
- 1 edge to [[_COMMUNITY_pipeline.py — Security Pipeline]]
- 1 edge to [[_COMMUNITY_Layer-by-Layer Breakdown]]
- 1 edge to [[_COMMUNITY_alert_dispatcher.py]]
- 1 edge to [[_COMMUNITY_drift_detector.py]]
- 1 edge to [[_COMMUNITY_encrypted_store.py]]
- 1 edge to [[_COMMUNITY_env_guard.py]]
- 1 edge to [[_COMMUNITY_trust_manager.py]]
- 1 edge to [[_COMMUNITY_Prompt Injection Blocks]]
- 1 edge to [[_COMMUNITY_All Environment Variables]]
- 1 edge to [[_COMMUNITY_SSH Config]]
- 1 edge to [[_COMMUNITY_Container Errors]]
- 1 edge to [[_COMMUNITY_Architecture Overview_1]]
- 1 edge to [[_COMMUNITY_port_manager.py]]
- 1 edge to [[_COMMUNITY_api.py_1]]
- 1 edge to [[_COMMUNITY_falco-rules.yaml]]
- 1 edge to [[_COMMUNITY_Seccomp Profiles]]
- 1 edge to [[_COMMUNITY_Docker Networks]]
- 1 edge to [[_COMMUNITY_AgentShroud — Vault Home]]
- 1 edge to [[_COMMUNITY_REQUIRED NOTES — PRODUCE EVERY ONE OF THESE_7]]
- 1 edge to [[_COMMUNITY_REQUIRED NOTES — PRODUCE EVERY ONE OF THESE_1]]
- 1 edge to [[_COMMUNITY_REQUIRED NOTES — PRODUCE EVERY ONE OF THESE_3]]
- 1 edge to [[_COMMUNITY_REQUIRED NOTES — PRODUCE EVERY ONE OF THESE_5]]
- 1 edge to [[_COMMUNITY_REQUIRED NOTES — PRODUCE EVERY ONE OF THESE_2]]
- 1 edge to [[_COMMUNITY_REQUIRED NOTES — PRODUCE EVERY ONE OF THESE_4]]
- 1 edge to [[_COMMUNITY_REQUIRED NOTES — PRODUCE EVERY ONE OF THESE_6]]
- 1 edge to [[_COMMUNITY_main.py]]
- 1 edge to [[_COMMUNITY_Error Index]]
- 1 edge to [[_COMMUNITY_Crash Recovery]]
- 1 edge to [[_COMMUNITY_Restart Procedure]]

## Top bridge nodes
- [[Data Flow]] - degree 31, connects to 16 communities
- [[Architecture Overview]] - degree 31, connects to 15 communities
- [[Startup Sequence_1]] - degree 21, connects to 7 communities
- [[Quick Reference]] - degree 8, connects to 3 communities
- [[Shutdown & Recovery_1]] - degree 8, connects to 2 communities
