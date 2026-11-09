# Inbound MCP Edge — Threat Model

Scope: hosted personal AI agents (Claude Duet, Poke, Gemini Spark, OpenAI Dots)
reaching the owner's home lab through the Inbound MCP Edge. IEC 62443 references
describe **alignment**, not certification.

**Taxonomies used**
- OWASP Top 10 for Agentic Applications 2026 (ASI01–ASI10, published 2025-12-09).
- MITRE ATLAS 2026.10 (released 2026-10-28).

Both were checked against the live sources on 2026-11-09. The changes from the brief are listed in section 3.

## 1. Trust boundaries

| Zone | Trust | Crosses into |
|---|---|---|
| Vendor cloud (hosted agent, its model, its connectors) | **Untrusted** | Tailscale Funnel :8443 |
| `agentshroud-mcp-edge` (internal network `agentshroud-dmz`) | Untrusted input, minimal privilege | gateway `POST /edge/v1/rpc` only |
| Gateway (policy and state) | Trusted enforcement point | Facades → SearXNG via :8181, public feeds, Hermes `edge-delegate` |
| Hermes `edge-delegate` profile | Restricted | Its own memory and tools only |
| Owner (Telegram, tailnet Command Center) | Trusted | Approvals, enrollment, kill |

## 2. Threats, controls, tests and residual risk

Each threat has at least one test that fails when its control is removed. The mutation evidence comes from a throwaway edit per control, run on 2026-11-09 (section 4).

| ID | Threat | OWASP ASI | MITRE ATLAS | Controls (code) | Tests | IEC 62443 FR | Residual risk |
|---|---|---|---|---|---|---|---|
| T1 | Injected content steers the agent into tool calls | ASI01 | AML.T0051.001, AML.T0053 | Per-vendor tool allowlist; local-agent tools hidden in hosted-only deployments; closed JSON Schemas; PromptGuard over raw, normalised and decoded string leaves, plus the heuristic band (`call_pipeline.py`) | `test_edge_pipeline.py::TestT1ToolAbuse` (8) | FR2, FR3 | A benign-looking but harmful read query passes P0. Read tools only return data and are size-capped. |
| T2 | Data exfiltration via tool results | ASI02 | AML.T0086, AML.T0136 | Per-install canaries (CanaryTripwire); per-leaf Presidio at ≥0.9 in redact or block mode; credential scrubber (now catches `sk-ant-`/`sk-proj-` keys); per-tool and per-vendor byte caps | `TestT2Exfiltration` (5), `test_hyphenated_sk_keys_are_blocked` | FR4, FR5 | PII Presidio does not recognise, below 0.9, or paraphrased. |
| T3 | Destructive writes | ASI02 | AML.T0101 | Every write needs owner approval. Tickets are bound to principal, tool and args SHA-256, single use (atomic consume), with a 10-minute TTL where expiry means deny. The daily delegation budget is enforced. | `test_edge_approvals.py` (24), `TestT3Writes` (4) | FR2 | The owner approves a harmful but readable request. Mitigated by showing the raw args and their hash. |
| T4 | Stolen or forged token | ASI03 | AML.T0012, AML.T0091.000 | ES256 pinned; `aud`/`iss`/`exp`/`iat`/lifetime/`sub` checks; issued-`jti` registry; vendor/client/`jti` kill checked on every call; refresh-family reuse revocation; single-use codes; DCR only inside an owner enrollment window | `test_edge_jwt.py` (29), `test_edge_oauth.py` (16), `TestT4AuthN` | FR1 | A stolen token is valid for up to 15 minutes, or until a kill. |
| T5 | Approval manipulation | ASI09 | AML.T0051, AML.T0067 | The card is built from structured fields only; no prose parameter exists; args are shown only as JSON with their hash; plain-text card | `TestApprovalCard` (snapshot and shape tests) | FR2 | Long args are truncated at 2 KB. The SHA-256 lets the owner verify them in the Command Center. |
| T6 | Memory or config poisoning of Hermes | ASI06 | AML.T0080.000, AML.T0081 | `wrap_untrusted` (signed delimiters, defanged look-alikes); restricted `edge-delegate` Hermes profile (no memory, no skill writes, web tool only, separate home) | `test_untrusted_envelope.py` (4), `test_edge_facades.py::test_delegate_wraps…` | FR3 | Depends on Hermes honouring the profile's memory and skill switches. To be verified live on dev. |
| T7 | Supply chain / descriptor drift | ASI04 | AML.T0010.005, AML.T0109, AML.T0110 | SHA-256 per descriptor; Ed25519-signed manifest; verified at gateway and edge start-up; CI step; image signing and Trivy gate in CI | `test_edge_descriptors.py` (19) | FR3 | The signing key must stay offline with the owner. |
| T8 | Code execution via args | ASI05 | AML.T0053, AML.T0050 | No path, URL, command or free-form target in any schema; control characters rejected (trailing-newline bypass fixed); facades never spawn processes | `test_edge_fuzz.py` (13, Hypothesis) | FR3 | None identified. Facades pass text to SearXNG and Hermes as data. |
| T9 | Loops, DoS, cost | ASI02, ASI08 | AML.T0029, AML.T0034.002 | Per-client and per-vendor windows, daily call and delegation budgets, per-vendor concurrency cap. Ladder: ALERT throttle → ESCALATED writes disabled → SUSPENDED client revoked → vendor disabled. Each step is audited and alerted. | `TestT9Abuse` (7) | FR7, FR6 | Counters are in memory and reset on gateway restart. Kills persist. |
| T10 | Vendor-side connector misuse | ASI02, ASI03 | AML.T0086, AML.T0085 | **Accepted residual risk.** AgentShroud cannot see a vendor's own Gmail or Slack connectors. Mitigations are scope minimisation (expose few tools), separate least-privilege vendor accounts, and the host egress watch (SCRUM-219). | none (by design) | — | High for agents with broad native connectors (Grok Bot, Instinct, Manus Cue: no hook at all). |
| ISO | Edge reaches internal services directly | — | — | Edge on internal `agentshroud-dmz` only; route allowlist; the only gateway door is a service-token RPC; `PROXY_ALLOWED_NETWORKS` excludes the DMZ | `test_edge_e2e_sdk.py::test_edge_guard`, `test_edge_fuzz.py::test_edge_guard_allowlist…`, `test_edge_network_isolation.py` | FR5 | A compromise of the gateway itself is out of scope for the edge. |

## 3. Taxonomy corrections versus the brief

| Threat | Brief | Corrected | Why |
|---|---|---|---|
| T2 | AML.T0057 | AML.T0086 + AML.T0136 | T0057 was removed in ATLAS 2026.10 (moved to AML.T0085.002, a collection technique) |
| T4 | AML.T0012 | + AML.T0091.000 | Application Access Token is the exact technique |
| T5 | AML.T0051 | + AML.T0067 | T0051 is only the delivery vector |
| T6 | ASI06, ASI07 | ASI06 | There is no inter-agent channel |
| T7 | T0010.005, T0110 | + AML.T0109 | AI Supply Chain Rug Pull matches descriptor drift |
| T8 | AML.T0053 | + AML.T0050 | Command and Scripting Interpreter |
| T9 | ASI08, ASI10 | ASI02, ASI08 | ASI02 names loop amplification; ASI10 (Rogue Agents) does not fit |

## 4. Mutation evidence (2026-11-09)

| Control removed | Result |
|---|---|
| T1 tool ACL | 2 failed |
| T1 schema | 1 failed |
| T1 P0 | 3 failed |
| T2 canary | 1 failed |
| T2 DLP | 3 failed |
| T3 approval status | 1 failed |
| T3 atomic consume | 4 failed |
| T4 jti registry | 1 failed |
| T4 kill check | 4 failed |
| T5 JSON card | 2 failed |
| T6 untrusted wrap | 1 failed |
| T7 drift check | 1 failed |
| T8 closed schema | 2 failed |
| T9 client rate limit | 2 failed |
| Edge route allowlist (guard alone) | 1 failed |
| `/mcp` bearer verifier | 1 failed |

Two controls first survived mutation because a second layer covered them: the single-use pre-check (the atomic consume still held) and the route allowlist (the SDK router also returns 404). Each was then proven separately: the atomic consume through its own mutation above, and the allowlist through a new guard-alone test.

## 5. Defects found while building

- **MCP SDK 2.3.0 low-level `streamable_http_app`.** It guards `/mcp` only when a `token_verifier` is passed. With just an `auth_server_provider` it served `/mcp` unauthenticated, and an end-to-end test saw a 200. The edge now passes `ProviderTokenVerifier`.
- **Single-line schema pattern.** `^…+$` accepted a trailing `\n` under Python `re`. Fixed with `(?![\s\S])`. Found by Hypothesis.
- **Credential scrubber.** It missed hyphenated `sk-` keys on every untrusted path.
- **Pre-existing control failures.** F1–F8 (`00-discovery.md` §6) are fixed on this branch: SOC killswitch, SOC approvals, DLP block mode, lockdown, audit-chain race, benchmark gate.
