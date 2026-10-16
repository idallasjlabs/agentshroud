---
source_file: "docs/diagrams/04-security.md"
type: "concept"
community: "AgentShroud Gateway (Trust Zone 1): holds 1Password service account, enforces policy, signs ledger entries, controls approval queue, HMAC/JWT validation"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/AgentShroud_Gateway_Trust_Zone_1_holds_1Password_service_account_enforces_policy_signs_ledger_entries_controls_approval_queue_HMAC/JWT_validation
---

# Trust Boundary Diagram

## Connections
- [[04-security]] - `conceptually_related_to` [EXTRACTED]
- [[AgentShroud Gateway (Trust Zone 1) holds 1Password service account, enforces policy, signs ledger entries, controls approval queue, HMACJWT validation]] - `conceptually_related_to` [EXTRACTED]
- [[BlockedUntrusted (LAN RFC1918, unlisted domains)]] - `conceptually_related_to` [EXTRACTED]
- [[Shared-Nothing Isolation Design Principle]] - `semantically_similar_to` [INFERRED]
- [[Trust Zone 0 — Owner (Isaiah Jefferson approvereject, gateway admin, container restart, secret rotation)]] - `conceptually_related_to` [EXTRACTED]
- [[Trust Zone 2 — Bot (Supervised Agent no direct credentialinternet access)]] - `conceptually_related_to` [EXTRACTED]
- [[Trust Zone 3 — External Services (OpenAI, Anthropic, Telegram, GitHub, 1Password; allowlisted HTTPS only)]] - `conceptually_related_to` [EXTRACTED]
- [[Trust Zone 4 — Infrastructure Nodes (raspberrypi, marvin, trillian; SSH-gated)]] - `conceptually_related_to` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/AgentShroud_Gateway_Trust_Zone_1_holds_1Password_service_account_enforces_policy_signs_ledger_entries_controls_approval_queue_HMAC/JWT_validation
