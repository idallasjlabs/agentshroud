---
type: community
cohesion: 0.10
members: 20
---

# iMessage Integration Fix - Using imsg + imessage

**Cohesion:** 0.10 - loosely connected
**Members:** 20 nodes

## Members
- [[APPLE-SERVICES-SETUP]] - document - docs/setup/APPLE-SERVICES-SETUP.md
- [[BOT_DEVELOPMENT_TEAM_RPI_SETUP]] - document - docs/setup/BOT_DEVELOPMENT_TEAM_RPI_SETUP.md
- [[Bot Identity Separation (Separate Accounts)]] - rationale - docs/security/SECURITY_ARCHITECTURE.md
- [[Current Setup (CORRECT)]] - document - docs/setup/IMESSAGE_FIX.md
- [[GOOGLE-CALENDAR-QUICK-SETUP]] - document - docs/setup/GOOGLE-CALENDAR-QUICK-SETUP.md
- [[GOOGLE-SERVICES-SETUP]] - document - docs/setup/GOOGLE-SERVICES-SETUP.md
- [[ICLOUD-SERVICES-SETUP]] - document - docs/setup/ICLOUD-SERVICES-SETUP.md
- [[IMESSAGE_FIX]] - document - docs/setup/IMESSAGE_FIX.md
- [[Next Steps_8]] - document - docs/setup/IMESSAGE_FIX.md
- [[Option 1 Grant Automation Permission (REQUIRED)]] - document - docs/setup/IMESSAGE_FIX.md
- [[Option 2 Check if Messages.app is Signed In]] - document - docs/setup/IMESSAGE_FIX.md
- [[Secret Management Hierarchy (1Password → Docker Secrets → Env)]] - rationale - docs/security/container-policy.md
- [[Status_5]] - document - docs/setup/IMESSAGE_FIX.md
- [[The Fix]] - document - docs/setup/IMESSAGE_FIX.md
- [[The Problem_1]] - document - docs/setup/IMESSAGE_FIX.md
- [[Verification_9]] - document - docs/setup/IMESSAGE_FIX.md
- [[Wazuh CVE-2025-24016 (CVSS 9.9)]] - concept - docs/security/security-supply-chain.md
- [[container-policy]] - document - docs/security/container-policy.md
- [[iMessage Integration Fix - Using imsg + imessage-exporter]] - document - docs/setup/IMESSAGE_FIX.md
- [[security-supply-chain]] - document - docs/security/security-supply-chain.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/iMessage_Integration_Fix_-_Using_imsg__imessage
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Apple Services Setup Guide]]
- 1 edge to [[_COMMUNITY_Google Calendar & Contacts - Quick Setup]]
- 1 edge to [[_COMMUNITY_Google Services Setup - Calendar, Contacts, Keep]]
- 1 edge to [[_COMMUNITY_iCloud Services Setup - Complete Guide]]
- 1 edge to [[_COMMUNITY_AgentShroud Security Architecture]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_Kill Switch]]
- 1 edge to [[_COMMUNITY_Container Security Policy — AgentShroud]]
- 1 edge to [[_COMMUNITY_AgentShroud Dev Environment — Raspberry Pi 4 (8G]]
- 1 edge to [[_COMMUNITY_Detailed Profiles]]
- 1 edge to [[_COMMUNITY_SECURITY_VALUE_PROPOSITION]]
- 1 edge to [[_COMMUNITY_Git History Purge Plan]]

## Top bridge nodes
- [[container-policy]] - degree 6, connects to 3 communities
- [[security-supply-chain]] - degree 4, connects to 2 communities
- [[APPLE-SERVICES-SETUP]] - degree 4, connects to 1 community
- [[BOT_DEVELOPMENT_TEAM_RPI_SETUP]] - degree 3, connects to 1 community
- [[GOOGLE-SERVICES-SETUP]] - degree 3, connects to 1 community