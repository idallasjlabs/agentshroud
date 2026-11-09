# Inbound MCP Edge — Plan (awaiting owner approval)

Discovery: `00-discovery.md`. No feature code is written until this plan is approved.

## 1. Architecture decision: a thin edge in front of a gateway that enforces policy

The edge container is a protocol terminator only. Every policy decision and all state live in the gateway, behind a new internal router `/edge/v1/*`.

```
Vendor cloud ──HTTPS──► Tailscale Funnel :8443 ──► 127.0.0.1:8443 (host)
                                                     │  raw TCP forwarder in gateway
                                                     │  (same pattern as lifespan.py:2271)
                                                     ▼
                              agentshroud-mcp-edge  [agentshroud-dmz only, internal:true]
                                1. size cap (64 KB), single-message only, Origin check,
                                   MCP-Protocol-Version / Mcp-Method / Mcp-Name header-body match
                                2. JWT verify (ES256 public key only; exp/aud/iss/alg)
                                3. MCP protocol via official SDK (mcp 2.3.0)
                                4. relays every call to the gateway with a dedicated service token
                                                     │  agentshroud-dmz
                                                     ▼
                              gateway /edge/v1/*  (reuses app_state singletons)
                                authN (revocation, jti replay, kill) → profile + tool ACL →
                                schema → P0 → P3 (tool-chain, lockdown, rate/budget) →
                                approval (writes) → dispatch facade → P2 → DLP → audit
                                                     │  agentshroud-isolated
                                                     ▼
                              facades: searxng-local (via :8181), PKE status, Hermes edge-delegate (/forward)
```

**Why the gateway enforces instead of the edge (rule 5, reuse rather than fork)**
- PromptGuard, the approval queue, the audit chain, lockdown, canaries and DLP are all singletons on `app_state`.
- Rebuilding them inside the edge would fork the audit chain and the approval database.
- The internet-facing container then holds **no signing key and no policy state**. Compromising it gives an attacker the public key and a service token that only reaches `/edge/v1/*`.

**Network**
- The edge is on `agentshroud-dmz` only. It can reach nothing except the gateway.
- The gateway joins the DMZ. `PROXY_ALLOWED_NETWORKS` stays without 10.254.113/24, so the edge cannot use `/v1`, `/forward` or `/telegram-api`.
- An internal network can't publish a host port, so the host port goes through the gateway's existing raw TCP forwarder pattern.

**Edge identity.** Every request runs as principal `edge:<vendor>:<client_id>`. It is never the owner ID, because the pipeline exempts the owner (`pipeline.py:524`).

**Spec target**
- MCP **2026-07-28** (stateless; `server/discover`, `tools/list`, `tools/call`).
- Also serve **2025-11-25** (`initialize`) through the SDK's legacy support, because vendors may still speak it. Q1 asks you to confirm this.
- No `resources`, `prompts`, sampling, subscriptions, or the Tasks extension.

**Approval while a call is pending.** The Python SDK has no Tasks extension, and elicitation isn't proof of a human. So:
1. A write call returns a non-error result `{status:"awaiting_human_approval", approval_ticket, expires_at, args_sha256}`.
2. The agent repeats the same call with the same arguments plus `approval_ticket`.
3. The gateway checks that the args hash matches the approved hash, consumes the ticket atomically, and executes once.
4. If the arguments differ, the ticket is expired, or it was already used, the call is denied.

Once the SDK ships Tasks, a follow-up can switch to it.

## 2. Command Center (owner addendum 2026-11-09)

New SOC tabs live in `gateway/soc/`, served on gateway :8080, **tailnet-only** like the rest of the Command Center (`tailscale serve --https=8080`). The edge container never proxies `/soc`. A test pins the edge's route set to `/mcp`, `/.well-known/oauth-protected-resource*`, `/.well-known/oauth-authorization-server` and `/oauth/{authorize,token,register,revoke}`.

| Tab | Content |
|-----|---------|
| **Agents** | One registry covering local agents (Hermes, OpenClaw: health, route, last activity) and hosted agents (Poke, Gemini Spark, Claude Duet, OpenAI Dots: enabled/mode, last call, rate, denials, lockdown level, kill state). It has a mode selector, **Hosted only / Hosted + Local / Local only**. The default comes from what is actually configured. Backed by `GET /soc/v1/agents`. In hosted-only deployments, `delegate_to_hermes` is not listed to vendors. |
| **Inbound Edge** | Live calls (WebSocket `edge_event`), per-vendor rates, denials by reason, DLP and canary hits, pending edge approvals, and kill controls per vendor and per token (owner role required, `confirm` required). |
| **Approvals** | All pending approvals with approve/deny. This requires fixing F2, because the SOC decide endpoints are broken today. |

## 3. Prerequisite fixes the edge depends on (separate commits, RED first)

| Fix | Why the edge needs it |
|-----|-----------------------|
| **F1** The SOC killswitch actually kills (wire to the engine in `web/api.py:346`) | "Wire the edge kill into the existing killswitch" is meaningless while it is fake-green |
| **F2** SOC approve/deny call `decide` | Approvals tab, Command Center decisions |
| **F8** Lock around audit append; verify from an anchor | Concurrent edge calls would fork the chain |
| **F7** App-wide `ProgressiveLockdown` on `app_state`, keyed by principal, with `escalate_to(level)` and decay | Escalation ladder per token/vendor; canary hit → immediate lockdown. Also revives Falco escalation. |
| **F6** `PIISanitizer` honors `block` | Per-vendor `dlp_mode: block` |
| **F4** Benchmark harness measures P50/P99; checker fails on regression | "No P99 regression" is unprovable today |

Out of scope for this branch; I'll raise each as its own PR when you say so: **F3** (public Hermes `/api/status`), **F5** (gateway Trivy image gate), **F10** (test socket leak).

## 4. Modules and files

**New package `gateway/inbound_edge/`.** It lives under `gateway/` so it inherits CI pytest, coverage and Semgrep, which scan `gateway/` only.

| File | Runs in | Purpose |
|------|---------|---------|
| `server.py` | edge | ASGI app: SDK `MCPServer`, size/Origin/header guards, per-request timeout, route allowlist |
| `token_verify.py` | edge | SDK `TokenVerifier`: ES256, `aud`, `iss`, `exp`, `nbf`; the `alg` allowlist prevents `none`/HS confusion |
| `gateway_client.py` | edge | httpx client for `/edge/v1/*` with the service token |
| `routes.py` | gateway | `/edge/v1/*` internal router, guarded by the edge service token and the DMZ source subnet |
| `profiles.py` | gateway | Vendor YAML schema and loader; fails closed; enforces the DLP floor; monitor mode requires `monitor_ack` and logs a loud warning |
| `tokens.py` | gateway | Mint and verify ES256 JWTs (15 min, `jti`, `aud`=resource); refresh-token rotation; jti replay store; revocation and kill (SQLite in the gateway data directory) |
| `oauth_server.py` | gateway | RFC 8414 and RFC 9728 metadata, `/authorize` (owner consent, see Q2), `/token` (PKCE S256 and RFC 8707 `resource` required), allowlisted DCR, `/revoke`. Reuses `OAuthSecurityValidator` (PKCE, exact redirect match, state replay). |
| `descriptors.py` + `descriptors.manifest.json` + `.sig` | both | Versioned tool descriptors with strict schemas (`additionalProperties:false`, length limits, enums). Startup refuses to run on a hash mismatch or a bad signature. |
| `call_pipeline.py` | gateway | Ordered pipeline (section 5) and the audit record (FR9 fields, stored in `details` so they are hashed) |
| `approvals.py` | gateway | Edge tickets on top of `EnhancedApprovalQueue`: idempotency key, 10-min TTL, expired means denied, args-hash binding, single use. Card built from raw args (pretty JSON, 2 KB cap plus full SHA-256) with no agent prose. Inline buttons use the egress-notifier callback pattern. |
| `dlp.py` | gateway | Composes `PIISanitizer`, `block_credentials`, `KeyLeakDetector`, `OutboundInfoFilter`, `CanaryTripwire` and a per-tool byte cap, without flattening JSON |
| `escalation.py` | gateway | Ladder throttle → writes disabled → token revoked → vendor disabled, on top of the app-wide lockdown. Each step is audited and sent to Telegram. |
| `facades/lab_search.py` | gateway | Search `searxng-local` through the egress proxy :8181. Query string ≤256 characters, result count enum. |
| `facades/pke_status.py` | gateway | Read-only PKE feed status (data source: Q5) |
| `facades/hermes_delegate.py` | gateway | `delegate_to_hermes(task ≤2000, priority enum)` → `/forward` with `route_to=hermes` and profile `edge-delegate`, wrapped as untrusted. Links the edge request ID to the Hermes session ID. |

**Changed files**
- **Security modules:**
  - `security/instruction_envelope.py`: add `wrap_untrusted(content, source)` with delimiters and provenance. It is signed and also marked untrusted.
  - `security/progressive_lockdown.py`, `security/audit_store.py`, `ingest_api/sanitizer.py`.
- **Approvals and Telegram:**
  - `approval_queue/enhanced_queue.py`, `approval_queue/store.py`: idempotency key, per-item TTL, consume.
  - `proxy/telegram_proxy.py`: edge approval callback with an owner check.
- **App wiring:**
  - `ingest_api/lifespan.py`: wire the edge components and the DMZ TCP forwarder.
  - `ingest_api/main.py`: include the routers.
- **Command Center:** `soc/router.py`, `soc/templates/soc.html`, `soc/static/soc.js` (section 2, plus F1 and F2).
- **CLI:** `gateway/cli/main.py` adds an `edge kill --vendor|--token` group, and `scripts/asb` adds an `edge` wrapper (Q11).
- **Compose and configs:**
  - `docker/docker-compose.yml`: `agentshroud-mcp-edge` service with `read_only`, `user: 10001`, `cap_drop: ALL`, `no-new-privileges`, default seccomp, tmpfs `/tmp`, health check, profile `full`, no socket and no host mounts. The gateway gains `agentshroud-dmz`.
  - `docker-compose.agentshroud-bot.marvin.yml`: separate dev DMZ subnet and container name.
  - `docker/mcp-edge/Dockerfile` (new): slim Python 3.13, contains only `gateway/inbound_edge/{server,token_verify,gateway_client,descriptors}`.
  - Vendor profiles `config/inbound-edge/vendors/{poke,gemini-spark,claude-duet,openai-dots}.yaml` and `config/inbound-edge/schema.json` (all `enabled: false`).
  - `gateway/requirements.txt`: adds `mcp==2.3.0`, `PyJWT[crypto]`, `jsonschema`, and `hypothesis` (test-only). See Q8.
- **CI:**
  - `.github/workflows/security-scan.yml`: edge image build, Trivy **image** scan with `exit-code: 1` on fixable CRITICAL/HIGH, cosign sign on main, a `cosign verify` gate, and a descriptor-manifest signature check.
  - `.semgrep.yml`: new rules (JWT `verify=False` / `algorithms=None`; `json.loads` on request bodies without the size guard; subprocess anywhere in `inbound_edge/`; owner-ID literals in `inbound_edge/`).
- **Ops scripts:**
  - `scripts/tailscale-serve.sh`: add `edge-funnel {plan|on|off}`. `plan` (the default) only prints what would be exposed: `:8443 /mcp, /.well-known/*, /oauth/*`.
  - `scripts/sunday-upgrade-apply.sh`: `CONTAINERS`, `DEFAULT_SCAN_IMAGES`.
  - `scripts/asb` and `docker/setup-secrets.sh`: secrets `edge_signing_key`, `edge_gateway_token`.
- **Benchmarks:** `gateway/tests/test_benchmark_regression.py`, `scripts/check_benchmark_regression.py` (F4).
- **Docs:** `docs/inbound-mcp-edge/{02-design,03-threat-model,04-runbook,vendors}.md`, README feature list, CHANGELOG, and the `docs/` site architecture/feature pages.

## 5. Request pipeline order (FR5)

| # | Step | Implementation | Note |
|---|------|----------------|------|
| 0 | Transport guards | edge `server.py` | Rejects junk before any parsing cost; size cap before `json.loads` |
| 1 | AuthN | Edge: JWT signature/claims. Gateway: revocation, kill, vendor enabled, jti replay, nonce window. | Kill checked on every call at the gateway (no cache), so it takes effect within 1 s |
| 2 | Profile + tool ACL | `profiles.py` + `MCPPolicyEngine.evaluate` (server `edge:<vendor>`) | Default deny |
| 3 | Schema | `jsonschema` Draft 2020-12, strict | Unknown or extra args are rejected |
| 4 | P0 | `normalize_input`, `EncodingDetector`, `PromptGuard.scan` on every string leaf, `HeuristicClassifier` in the uncertain band | Score enters the audit record and the approval card |
| 5 | P3 | `ToolChainAnalyzer`, lockdown state, `RateLimitGuard` (token and vendor buckets), concurrency semaphore, daily budget | **Deviation:** rate and concurrency checks run before P0 when the bucket is empty, to avoid spending CPU on flood traffic. Rejections are audited either way. |
| 6 | Approval | `approvals.py` (writes only) | Raw args only |
| 7 | Dispatch | facade | Per-tool timeout |
| 8 | P2 | `CanaryTripwire`, `OutputCanary`, `OutputSchemaEnforcer`, `PromptGuard.scan_tool_result` | Canary hit → block and `escalate_to(SUSPENDED)` |
| 9 | DLP | `dlp.py` | `redact` or `block` per profile; the threshold can only go up from 0.9 |
| 10 | Audit + events | `AuditStore.log_event("edge_call", …)` + `event_bus.emit` | Every outcome, including denials |

## 6. Test plan (RED first; each threat has a test that fails when its control is removed)

| Threat | Test file (`gateway/tests/`) | Key tests |
|---|---|---|
| T1 | `test_edge_acl_injection.py` | unknown tool, tool not in profile, extra args, injection strings raise P0 score and block |
| T2 | `test_edge_dlp.py` | PII redact vs block, API keys scrubbed, canary hit blocks and suspends, oversize truncated or denied |
| T3 | `test_edge_approvals.py` | write without approval never dispatches, expired ticket denied, ticket replay denied, args mismatch denied, `../` and absolute paths rejected by schema |
| T4 | `test_edge_tokens.py` | expired, wrong `aud`, wrong `iss`, `alg:none`, HS256-with-public-key, unsigned, replayed `jti`, revoked token; kill takes effect within 1 s |
| T5 | `test_edge_approval_card.py` | snapshot: raw args, SHA-256, no agent prose |
| T6 | `test_edge_delegate.py` | task wrapped and marked untrusted; edge-delegate profile cannot write memory, skills or AGENTS.md (config assertion plus a live dev check) |
| T7 | `test_edge_descriptors.py` | changed descriptor or bad signature → startup refuses; CI job fails on an unsigned image |
| T8 | `test_edge_fuzz.py` (hypothesis) | every schema and the JSON-RPC parser against shell metacharacters, confusables, encodings and nesting depth |
| T9 | `test_edge_abuse.py` | per-token and per-vendor buckets, concurrency cap, ladder order and audit/Telegram per step |
| Isolation | `test_edge_network_isolation.py` (compose config, static) and `scripts/smoke.d/test-edge-isolation.sh` (dev, live) | edge cannot reach Hermes, OpenClaw, the docker socket or the internet; the route allowlist is pinned |
| Command Center | `test_soc_agents.py`, `test_soc_edge.py` | three mode filters, RBAC on kill, F1/F2 regressions |
| End to end | `test_edge_e2e_sdk.py` (in-process) plus a dev live run | SDK `OAuthClientProvider`: PKCE → token → `tools/list` → each tool, asserting `resource` is sent |

- **Mutation checks:** for each threat, I'll disable its control in a throwaway diff, show the test failing, then revert. The output goes in the phase report, not in a committed file.
- **Coverage:** the suite stays ≥ 93% (baseline). New modules aim for ≥ 94%, the CLAUDE.md floor, which is stricter than the 90% in the brief.

## 7. Commit sequence (branch `feat/inbound-mcp-edge`; no push or PR until you ask)

| # | Commit |
|---|--------|
| C0 | docs: discovery + plan |
| C1 | fix(soc): killswitch endpoints act (F1) |
| C2 | fix(soc): approvals decide + Approvals tab (F2) |
| C3 | fix(audit): serialized appends (F8) |
| C4 | feat(lockdown): app-wide, principal-keyed, escalate_to (F7) |
| C5 | fix(dlp): block mode (F6) |
| C6 | perf: P50/P99 harness + failing checker (F4) |
| C7 | feat(approval): idempotency, TTL, single-use, raw-args card, buttons |
| C8 | feat(envelope): `wrap_untrusted` |
| C9 | feat(edge): profiles + 4 disabled vendors |
| C10 | feat(edge): token service, revocation, kill CLI |
| C11 | feat(edge): OAuth AS + metadata |
| C12 | feat(edge): signed descriptors |
| C13 | feat(edge): gateway call pipeline + audit |
| C14 | feat(edge): `lab_search`, `pke_status` |
| C15 | feat(edge): `delegate_to_hermes` + edge-delegate profile |
| C16 | feat(edge): edge server container |
| C17 | feat(compose): service, DMZ, forwarder, dev subnet, isolation tests |
| C18 | feat(soc): Agents, Inbound Edge tabs |
| C19 | ci: edge image Trivy, cosign, Semgrep rules |
| C20 | ops: Funnel `plan/on/off`, Sunday upgrade, secrets |
| C21 | test: SDK e2e, fuzz |
| C22 | docs: design, threat model, runbook, vendors, README, CHANGELOG, site |

## 8. System-wide impact

| Component | Impact |
|-----------|--------|
| Gateway :8080 | New `/edge/v1` and `/soc/v1` routes; joins the DMZ; F1/F2/F4/F6/F7/F8 behavior fixes |
| Hermes | New `edge-delegate` profile only; main profile and memory untouched |
| OpenClaw | None (not exposed through the edge) |
| Voice path | None: no route or Funnel :443 change |
| Egress proxy :8181 | `lab_search` traffic goes through it; one allowlist entry for `searxng-local` if it is refused today |
| Weekly upgrade | One more built image, container and scan target |
| Command Center | Three tabs; F1 makes its kill buttons real |
| Telegram proxy | Edge approval callbacks; uses the shared lockdown instance |

## 9. Corrections to the brief's threat IDs (verified against ATLAS 2026.10 and OWASP ASI 2026)

| Threat | Change |
|---|---|
| T2 | **AML.T0057 no longer exists** (removed in ATLAS 2026.10, moved to AML.T0085.002). Use AML.T0086, and add AML.T0136 (Exfiltration via AI User Interface). |
| T4 | Add AML.T0091.000 (Application Access Token) |
| T5 | AML.T0051 is only the delivery vector; add AML.T0067 (Trusted Output Components Manipulation) |
| T6 | Drop ASI07 (no inter-agent channel); optionally add AML.T0080.001 |
| T7 | Add AML.T0109 (AI Supply Chain Rug Pull), which is an exact fit for descriptor drift |
| T8 | Add AML.T0050 (Command and Scripting Interpreter) |
| T9 | Replace ASI10 with ASI02 (which lists loop amplification); refine to AML.T0034.002 |

All other IDs verified as-is.

## 10. Open questions (decisions I need)

| # | Question | My recommendation |
|---|----------|-------------------|
| Q1 | The brief lists `initialize`, which the current spec (2026-07-28) removed. Serve both 2026-07-28 and legacy 2025-11-25? | Yes, both |
| Q2 | How do you consent when a vendor's OAuth sends your browser to `/oauth/authorize` on a public URL? | A one-time enrollment code from `asb edge enroll --vendor poke` (tailnet shell, 10-min TTL) entered on the page, **plus** a Telegram confirm. No passwords on the public page. |
| Q3 | Client registration: Poke and Gemini expect DCR (dynamic client registration); OpenAI prefers CIMD (client ID metadata document); the spec deprecates DCR | Pre-registered clients plus DCR allowed only for listed vendors and only during an open enrollment window; CIMD as a follow-up when Dots is confirmed |
| Q4 | **Telegram approval round-trip on dev.** Dev has no Telegram bot of its own. Inline-button callbacks from a dev card would be delivered to *prod's* poller. | Create a dev-only bot (you, via BotFather) and store it as a dev secret; until then, dev approvals go through the Command Center |
| Q5 | Where should `pke_status` read from? | The public GitHub Pages feed through the egress proxy (read-only, no new mounts), over a read-only mount of the Hermes outbox |
| Q6 | `edge-delegate` tool set | `web_search` (searxng) only. No terminal, file, browser, memory, skills, cron or MCP. I'll first test whether Hermes 0.23 profiles can enforce this; if not, I'll report back before building. |
| Q7 | Descriptor manifest signing | An ed25519 key you hold in Keychain/1Password signs the manifest; the public key is committed; CI and the edge verify it. Cosign keyless can't sign locally. |
| Q8 | New dependencies: `mcp==2.3.0`, `PyJWT[crypto]`, `jsonschema`, `hypothesis` (test-only) | Approve |
| Q9 | "No plaintext secrets on disk" conflicts with the existing pattern: `setup-secrets.sh` writes `docker/secrets/*.txt` | Edge secrets live only in Keychain/1Password and are written to a tmpfs-backed secrets directory by `asb` at start. If that is too invasive, accept the current pattern for now and track it. |
| Q10 | Fix F1, F2, F4, F6, F7, F8 on this branch (section 3)? | Yes: the edge's controls depend on them |
| Q11 | The brief's `agentshroud edge kill` CLI doesn't exist | `agentshroud-soc edge kill …` plus `asb edge kill …` |
| Q12 | Funnel port | 8443 (443 is already used by the Hermes dashboard and voice paths) |
| Q13 | Default limits per vendor | 30 calls/min per token, 60/min per vendor, concurrency 4, 500 calls/day, 20 delegations/day, 1 MB response cap (64 KB for `lab_search`) |
| Q14 | Hosted-agent IP allowlists (Anthropic publishes ranges; OpenAI publishes a JSON list) | An optional `source_cidrs` profile field, *if* a trial shows Funnel passes the client IP through. Not a substitute for OAuth. |
