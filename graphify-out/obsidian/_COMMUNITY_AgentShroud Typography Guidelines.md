---
type: community
cohesion: 0.16
members: 18
---

# AgentShroud Typography Guidelines

**Cohesion:** 0.16 - loosely connected
**Members:** 18 nodes

## Members
- [[AgentShroud Security Inventory v0.8.0 (58 Modules)]] - document - docs/security/security-inventory.md
- [[Competitive Security Matrix (28 Modules vs 11 Platforms)]] - document - docs/security/competitive-security-matrix.md
- [[ESP32-S3-BOX-3 Hermes Voice Terminal Planning Doc]] - document - docs/planning/v1.3/esp32-s3-hermes-voice-terminal.md
- [[KeyVault Zero-Exposure In-Memory Secret Storage]] - concept - docs/security/security-inventory.md
- [[Kokoro TTS Engine]] - concept - voice_gateway/requirements.txt
- [[MicroLink Native Tailscale Client for ESP32 (Requires PSRAM)]] - concept - docs/planning/v1.3/esp32-s3-hermes-voice-terminal.md
- [[PromptGuard Prompt Injection Defense (49 Patterns, 35+ Languages)]] - concept - docs/security/security-inventory.md
- [[RT-MB2 Cross-Bot Shared Memory Leak (Fixed in PR)]] - concept - docs/planning/v1.2/red-team-assessment-v1.2.0.md
- [[RT-MB4 Hermes Cron Job Injection via jobs.yaml (Accepted Risk)]] - concept - docs/planning/v1.2/red-team-assessment-v1.2.0.md
- [[Red Team Assessment v1.2.0]] - document - docs/planning/v1.2/red-team-assessment-v1.2.0.md
- [[Security Module 27 Cross-Bot Trust Ledger (v1.2.0)]] - concept - docs/security/competitive-security-matrix.md
- [[Security Module 28 Differential PII Detector on Tool Results 0.7-floor (v1.2.0)]] - concept - docs/security/competitive-security-matrix.md
- [[SecurityPipeline Central InboundOutbound Module Orchestrator]] - concept - docs/security/security-inventory.md
- [[SharedMemoryManager Per-User Per-Bot Memory Isolation]] - concept - docs/planning/v1.2/red-team-assessment-v1.2.0.md
- [[TrustManager Progressive Trust Scoring (5 Levels)]] - concept - docs/security/security-inventory.md
- [[Voice Gateway Python Requirements (faster-whisper, kokoro)]] - code - voice_gateway/requirements.txt
- [[Voice Gateway Service (STTTTS WebSocket Bridge to Governed Path)]] - concept - docs/planning/v1.3/esp32-s3-hermes-voice-terminal.md
- [[faster-whisper STT Engine (Local, CPU-friendly)]] - concept - voice_gateway/requirements.txt

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_Typography_Guidelines
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Any]]
- 1 edge to [[_COMMUNITY_TestLogSanitizer]]
- 1 edge to [[_COMMUNITY_agent_isolation.py]]

## Top bridge nodes
- [[Red Team Assessment v1.2.0]] - degree 7, connects to 1 community
- [[AgentShroud Security Inventory v0.8.0 (58 Modules)]] - degree 6, connects to 1 community
- [[PromptGuard Prompt Injection Defense (49 Patterns, 35+ Languages)]] - degree 5, connects to 1 community
- [[SecurityPipeline Central InboundOutbound Module Orchestrator]] - degree 4, connects to 1 community
- [[Competitive Security Matrix (28 Modules vs 11 Platforms)]] - degree 4, connects to 1 community