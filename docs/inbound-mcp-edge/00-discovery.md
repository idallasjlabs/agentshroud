# Inbound MCP Edge — Phase 0 Discovery

Branch `feat/inbound-mcp-edge` @ `5cf50ed189` (= `origin/main`), 2026-11-09.
Graphify graph was built 2026-11-01 and predates the 2026-11-08 commits, so this
discovery was done by reading source directly. Line numbers are against `5cf50ed189`.

## 1. Repo layout, build and test

| Area | Path | Language |
|------|------|----------|
| Gateway (FastAPI app, all security modules) | `gateway/` (`ingest_api/`, `security/`, `proxy/`, `approval_queue/`, `soc/`, `web/`) | Python 3.11 (CI also 3.13) |
| Command Center (SOC SPA) | `gateway/soc/` (`router.py`, `templates/soc.html`, `static/soc.js`) | Python + vanilla JS |
| SOC CLIs | `gateway/cli/` (click, `agentshroud-soc`), `cli/` (Rust clap, same name) | Python, Rust |
| Operator CLI | `scripts/asb` (bash `case`, `asb:599-746`) | bash |
| Containers | `docker/docker-compose.yml` + `docker/docker-compose.agentshroud-bot.*.yml` overrides | YAML |
| Hermes wrapper | `docker/bots/hermes/` (`run-standalone.sh`, `init-config.sh`) | bash |
| Voice | `voice_gateway/` | Python |

**Commands**
- Tests: `python -m pytest gateway/tests/ --cov=gateway --cov-fail-under=84` (`.github/workflows/ci.yml:69-73`). `pytest.ini` sets `timeout=60` and turns `ResourceWarning`/unraisable warnings into errors.
- Lint in CI: black 26.5.1, isort, flake8 (`ci.yml:195-218`). Ruff is only in `Makefile:12-13` and pre-commit. **mypy is not in CI.**
- Coverage thresholds disagree: CI 84, `gateway/pyproject.toml:58-64` 85, `Makefile:10` 94, CLAUDE.md 94.

**CI workflows** (`.github/workflows/`)

| Workflow | What it runs |
|----------|--------------|
| `ci.yml` | Test matrix; pip-audit; gitleaks; smoke-static; lint; benchmark; dast (manual); docs-drift |
| `security-scan.yml` | Cosign keyless signing + SBOM attestation of the **gateway image only** (14-58, push to main); Trivy **filesystem** scan with `exit-code: 0` (71-79); Semgrep 1.177.0 on `gateway/`, new findings only (119-134); pip-audit |
| `release.yml` | On `v*` tags: tests, builds gateway and openclaw images (push commented out) |

## 2. Baseline measurements (run now)

```
$ .venv/bin/python -m pytest gateway/tests/ -q -n auto --cov=gateway --cov-report=term
TOTAL                                                  90795   6227    93%
1 failed, 7848 passed, 3 skipped, 24 warnings in 135.09s (0:02:15)
```

- **Coverage baseline is 93%.**
- **The single failure already exists on main.** `test_security_audit.py::TestContainerSecurity::test_security_toolchain_trivy` passes alone (`1 passed in 0.02s`) but errors when its whole file runs (`133 passed, 1 error`). A test that runs earlier leaves a socket open, and the `ResourceWarning` it raises surfaces in this test. That is a baseline defect, not a regression. The new work must not add to it.

**Latency harness**
- `gateway/tests/test_benchmark_regression.py` measures the **mean over 1000 iterations** with `perf_counter`; there is **no P99**.
- Baseline `.benchmarks/baseline-v1.0.0.json`: `single_inbound_ms: 0.44`.
- **The CI checker cannot fail.** `scripts/check_benchmark_regression.py:16-21` expects pytest-benchmark keys the tests never emit, so every metric SKIPs, and `ci.yml:233-237` runs the test step with `|| true`.

## 3. Defense layers and reusable interfaces

**Layering definitions disagree.**
- The P0–P6 model exists only in `docs/index.html:385-414`.
- `CLAUDE.md` and `README.md:93-96` use an older 4-tier model.
- The canonical module sets are in code: `MiddlewareManager.ALL_MODULE_ATTRS` (`gateway/ingest_api/middleware.py:119-157`) and `SecurityPipeline.ALL_MODULE_ATTRS` (`gateway/proxy/pipeline.py:333-346`).

**Runtime model.**
- One FastAPI app (`gateway/ingest_api/main.py:178`).
- Every module is built once in `lifespan.py:340-900` and held on the singleton `app_state` (`gateway/ingest_api/state.py:23-67`).
- An in-process caller can reuse the full chain through `app_state.pipeline` and `app_state.middleware_manager`. A separate process would have to rebuild it and would fork state.

**Governed inbound path.** `POST /forward` (`routes/forward.py:586`) → `_process_inbound` (:386), which runs three stages:
1. `middleware_manager.process_request` (:469)
2. `pipeline.process_inbound` (:504; order at `pipeline.py:527-1024`)
3. `pipeline.process_outbound` (:706; order at `pipeline.py:1072-1570`)

| Layer (docs/index.html) | Module | Interface to reuse |
|---|---|---|
| P0 | PromptGuard | `PromptGuard.scan(text) -> ScanResult(blocked, score, patterns, …)` `security/prompt_guard.py:705`. Default thresholds are block 0.8 / warn 0.4 (`lifespan.py:347`); monitor mode sets them to 999. |
| P0 | Heuristic second opinion | `HeuristicClassifier.classify` `heuristic_classifier.py:164`. Its ML path is a stub (:112-127, :215-220). |
| P0 | Encoding / normalization | `EncodingDetector.analyze` `encoding_detector.py:145`; `normalize_input` `input_normalizer.py:33` |
| P0 | Trust | `TrustManager.is_action_allowed` / `is_tool_allowed` / `record_violation` `trust_manager.py:204,289,221` |
| P2 | Output | `CanaryTripwire.scan_response` `canary_tripwire.py:127`; `OutputCanary.check_response` `output_canary.py:204`; `OutboundInfoFilter.filter_response` `outbound_filter.py:351`; `OutputSchemaEnforcer.validate` `output_schema.py:89` |
| P3 | MCP policy | `MCPPolicyEngine.evaluate(server, tool, agent_id, args)` `mcp_policy.py:263` (pure, default-deny) and `enforce` :401 |
| P3 | ACL / RBAC | `ToolACLEnforcer.can_use_tool` `tool_acl.py:233`; `RBACManager.check_permission` `rbac.py:187` |
| P3 | Lockdown | `ProgressiveLockdown.record_block` `progressive_lockdown.py:77`. States: NORMAL, ALERT ≥3, ESCALATED ≥5, SUSPENDED ≥10. |
| P3 | Rate limit | `RateLimitGuard.check(agent_id, tool)` `rate_limit_guard.py:108`. Off unless `AGENTSHROUD_RATE_LIMIT_ENABLED=1` (`lifespan.py:728`). |
| P3 | Approval | `EnhancedApprovalQueue` (section 4) |

**`gateway/proxy/mcp_proxy.py` is an outbound MCP client inspector, not an MCP server.**
- `POST /mcp/proxy` (`main.py:704`) only inspects (`execute=False`).
- No `/mcp` server route exists. The Hermes entry `agentshroud-gateway → http://gateway:8080/mcp` is `"enabled": false` in `docker/config/hermes/mcp/servers.json`.

**Owner bypass hazard.**
- `pipeline.process_inbound` audits the owner but never blocks them (`pipeline.py:524-525`).
- Owner identity comes from `metadata["user_id"]` and the trusted header `X-AgentShroud-User-Id` (`forward.py:409-425`).
- **Any edge request that resolves to the owner's ID would skip enforcement.** The edge principal must be a distinct, non-owner identity.

## 4. Mechanisms the edge depends on

| Mechanism | Where | State today | Gap for the edge |
|---|---|---|---|
| Approval queue | `EnhancedApprovalQueue` `approval_queue/enhanced_queue.py:35`; SQLite `agentshroud_approvals.db` | `submit` :215, `decide` :357 (MFA, single decide via popped future), `wait_for_decision` :341 | Telegram card is plain text with no buttons and is sent only for the `critical` tier (:462-494, `config.py:204-212`). `ApprovalHardening.format_hardened_message` (`approval_hardening.py:413`) is never called. No idempotency key (new uuid on every submit, :221). Default timeout 86400 s. `timeout_action: allow` resolves as deny (:320). |
| SOC approvals | `soc/router.py:1667-1700` | Calls `aq.approve` / `aq.deny`, which don't exist (only `decide`). | **Always returns `ok: false`.** There is no approvals tab in the Command Center. |
| Telegram buttons | `proxy/telegram_egress_notify.py:137-205` (`callback_data`), dispatched in `telegram_proxy.py:4208-4240` with an owner check | Egress approvals only | Pattern to copy for tool approvals. |
| DLP | `PIISanitizer.sanitize` `ingest_api/sanitizer.py:171`. `min_confidence=0.9` at `ingest_api/config.py:39-40`; entities SSN / card / phone / email. | Redacts only | `enforcement_action="block"` is stored but **never read** (`sanitizer.py:39-40`). `ToolResultSanitizer` flattens JSON when it finds PII (`tool_result_sanitizer.py:160-189`). |
| Credential scrub | `PIISanitizer.block_credentials` `sanitizer.py:417` (includes literal `/run/secrets` values); `KeyLeakDetector.scan_outbound` `key_vault.py:169`; `OutboundInfoFilter` | Spread across several functions | No single `scrub()`; the edge must compose them. |
| Audit chain | `AuditStore.log_event(event_type, severity, details, source_module, …)` `security/audit_store.py:169`; `verify_hash_chain` :301 | `details` is part of the hashed content, so new fields need no migration | No lock between reading the previous hash and the INSERT (:198-219), so concurrent appends can fork the chain. `verify_hash_chain(start_id)` fails mid-chain (:338). SOC verify checks only the in-memory chain (`router.py:295`). |
| Lockdown | `progressive_lockdown.py:63` | One private instance, inside the Telegram proxy only (`telegram_proxy.py:501`) | Not on `app_state`, so Falco escalation is dead (`lifespan.py:1735`). In memory only, with no decay. No direct escalate-to-level call. |
| Killswitch | `web/api.py:346-403` (real: pause, `compose_down`, rm), `docker/scripts/killswitch.sh` | Global only | **The SOC killswitch endpoints do nothing and return `ok: true`.** `router.py:748-754` guards on `hasattr(monitor, "trigger_freeze")`, and `KillSwitchMonitor` (`security/killswitch_monitor.py:37-623`) defines no `trigger_*` methods. Both CLIs call this path (`gateway/cli/client.py:114`, `cli/src/main.rs:856-866`). There is no per-principal kill. |
| Canaries | `CanaryTripwire` (`lifespan.py:614`; blocks plus CRITICAL audit at `pipeline.py:1201-1235`) | Static default values only | `register_canary` is never called in production. `OutputCanary.generate_canary` is never called. Alerts go to the log and audit only. |
| Command Center | SPA `/soc/v1/` (`router.py:2715`); tabs at `soc.html:53-64`; `_registerTab` in `soc.js:204-217`; WebSocket `/soc/v1/ws` fed by `event_bus.emit(make_event(...))` (`event_bus.py:64,110`) | 10 tabs | `/soc/v1/bots` (`router.py:1899`) lists configured local bots only, with no idea of hosted agents. |
| Alerts / metrics | `AlertDispatcher.dispatch` `alert_dispatcher.py:58` → `/api/alerts` → `AlertTelegramRelay` | JSONL plus Telegram for CRITICAL/HIGH | **No Prometheus or `/metrics`.** The only counters are `module_stats.record_decision` (`module_stats.py:86`). |
| Secrets | `read_secret(name)` `gateway/utils/secrets.py:29` (`/run/secrets`); host side `docker/setup-secrets.sh` (Keychain → secret-tool → `op` → file) | | `setup-secrets.sh extract` writes `docker/secrets/<name>.txt`, so **plaintext secret files on disk are the existing pattern**. |
| JWT / OAuth | `TokenValidator` `security/token_validation.py:51`; `OAuthSecurityValidator` `security/oauth_security.py` | | **`TokenValidator` never checks a signature** (it only base64-decodes the payload, :64-77). No JWT library is in `gateway/` (`cryptography>=50.0.1` is present). It is never called on live requests. `OAuthSecurityValidator` has usable PKCE S256, exact redirect-URI match and state-replay checks. |
| Instruction envelope | `security/instruction_envelope.py:51-88` | HMAC attestation only | **It does not wrap or mark content as untrusted.** No untrusted-content wrapper exists anywhere in `gateway/`. |

## 5. Hermes, local agents and networking

**Networks** (`docker/docker-compose.yml:1024-1074`)

| Network | Range | Purpose |
|---|---|---|
| `agentshroud-internal` | 10.254.110/24 | Edge and internet tier |
| `agentshroud-isolated` | 10.254.111/24, internal | Bots |
| `agentshroud-dmz` | 10.254.113/24, internal | Declared "reserved for a future edge broker" (:1055-1065) and attached to nothing |

- The gateway must stay on both internal and isolated (:1036-1039).
- The dev override does **not** override the DMZ subnet, so dev and prod would both claim 10.254.113/24.

**Hermes access**
- The API on :8642 is a raw TCP forwarder in the gateway (`lifespan.py:2271-2283`) that **deliberately bypasses PromptGuard**. Its only auth is Hermes' `API_SERVER_KEY`.
- The governed path is `/forward` and `/forward/stream` with `route_to=hermes`, behind `AuthRequired` (`routes/forward.py:586,854`).
- The edge must use the governed path.

**Hermes personas**
- The only persona is `SOUL.md`, seeded by `init-config.sh:68-131`.
- **There is no restricted profile with memory writes or skill install disabled.**
- Hermes 0.23 reports `profiles` and `parked_profiles` in `/api/status`, so a native profile mechanism exists upstream. Whether it can switch off memory and skills must be confirmed with a short trial.

**Hermes MCP governance**
- A GitHub MCP is added directly (`init-config.sh:469-497`). It reaches GitHub through the egress allowlist only, not through the approval queue.

**Other services**
- **searxng-local** is not in this repo. It runs from `~/Development/local-llms` and is attached to the isolated network by `run-standalone.sh:358-372`. That attachment is lost whenever searxng is recreated.
- **PKE** is host-side (`~/Development/pke`, launchd job at 04:35). Its status lives in the Hermes outbox (`/opt/data/podcasts/outbox/daily/<date>/READY`), `~/Library/Logs/daily-brief-publish.log`, and the public GitHub Pages feed. **There is no in-repo status API.**

**Command Center exposure.** It is served on gateway :8080, published tailnet-only by `scripts/tailscale-serve.sh:85` (`tailscale serve --https=8080`).

**Funnel on :443 is already public:** `/voice`, `/hermes`, `/` (→ Hermes dashboard) and `/health` (`tailscale-serve.sh:103-120`). Confirmed live with `tailscale serve status`.

## 6. Pre-existing findings (not caused by this work)

Items marked ✓ were re-checked in the code by me. The others come from the discovery agents and still need checking.

| # | Finding | Evidence | Severity |
|---|---|---|---|
| F1 | SOC killswitch (UI, Python CLI, Rust CLI) reports success and kills nothing ✓ | `soc/router.py:748-754`; `killswitch_monitor.py` has no `trigger_*` | **High**: a CLAUDE.md §0.0 fake-green |
| F2 | SOC approve/deny always fails ✓ | `soc/router.py:1677,1696` call methods that don't exist | Medium |
| F3 | Hermes `/api/status` is readable from the public internet without a login | `curl https://marvin.tail240ea8.ts.net/api/status` → 200 JSON with `version`, `install_id`, `profiles`, gateway state. `/api/sessions`, `/api/config` and `/api/memory` correctly return 401. | Medium (fingerprinting) |
| F4 | Benchmark regression checker can never fail | `check_benchmark_regression.py:16-21`, `ci.yml:233-237` | Medium: fake-green |
| F5 | CI Trivy is a filesystem scan with `exit-code: 0`; there is no image scan | `security-scan.yml:71-79` | Medium |
| F6 | DLP block mode is ignored | `sanitizer.py:39-40` | Medium |
| F7 | Falco lockdown path is dead; `OutputCanary` is never seeded | `lifespan.py:1735`; `output_canary.py:92` | Medium |
| F8 | Audit chain append race; mid-chain verify broken | `audit_store.py:198-219,338` | Medium |
| F9 | `TokenValidator` has no signature check (unused) ✓ (no JWT library present) | `token_validation.py:64-77` | Low while unused |
| F10 | Order-dependent `ResourceWarning` makes one test error | section 2 | Low |

## 7. External specs verified (2026-11-09)

| Item | Finding | Source |
|---|---|---|
| MCP spec | Current version **2026-07-28**. It is **stateless**: `initialize`, sessions (`Mcp-Session-Id`), GET streams and `ping` are removed. `server/discover` is mandatory. POST only, one message per request (no batching). `MCP-Protocol-Version`, `Mcp-Method` and `Mcp-Name` headers are required and must match the body. Origin must be validated (403). | modelcontextprotocol.io/specification/2026-07-28 (transports, changelog) |
| MCP authorization | OAuth 2.1 with PKCE S256 required. Protected Resource Metadata (RFC 9728) required. Authorization-server discovery via RFC 8414 or OIDC (OpenID Connect). Client registration: Client ID Metadata Documents **SHOULD**, Dynamic Client Registration **MAY and deprecated**, pre-registration allowed. RFC 8707 `resource` required, audience must be validated. Token passthrough forbidden. | …/2026-07-28/basic/authorization |
| Long-running calls | Tasks moved out of core into the extension `io.modelcontextprotocol/tasks` (`tasks/get`, `tasks/update`, `tasks/cancel`; lists "human approvals" as a use case). Elicitation is not proof of human approval: a hosted agent can answer it itself. | modelcontextprotocol.io/extensions/tasks/overview |
| Python SDK | `mcp` **2.3.0** (2026-10-02). Serves 2026-07-28 plus earlier revisions. Resource-server auth helpers, but `validate_token_resource` is off by default. **No Tasks extension.** Not an authorization server. Python 3.11+. | pypi.org/pypi/mcp/json, py.sdk.modelcontextprotocol.io |
| Tailscale Funnel | Ports 443, 8443 and 10000 only. TLS ends at the local `tailscaled`. **Funnel traffic carries no identity headers.** `--set-path` is supported (whether it isolates other paths is unverified). A port is either Serve or Funnel, whichever command ran last. | tailscale.com/kb/1223/funnel, /kb/1311/tailscale-funnel |

## 8. Gaps this feature needs filled

1. An MCP server endpoint, an OAuth authorization server and a JWT library (none exist).
2. An edge principal model: a non-owner identity for each vendor and client.
3. An untrusted-content wrapper for delegated tasks (the envelope only signs).
4. Approval items with idempotency keys, per-item TTL, a raw-args card with inline buttons, single-use execution, and working SOC decide endpoints.
5. An app-wide lockdown keyed by edge principal, with escalate-to-level.
6. A per-vendor and per-token revocation list plus kill, shared by the edge and the gateway.
7. A DLP block mode and seeded canaries.
8. A restricted Hermes `edge-delegate` profile.
9. A PKE status data source.
10. P99 measurement in the benchmark harness.
11. CI image build, Trivy image scan and cosign for a second image.
12. A multi-class agent registry for the Command Center (hosted and local).

## 9. Risks to existing services

| Risk | Affected | Mitigation in plan |
|---|---|---|
| A new public port on the node prod shares | Prod Funnel, Hermes dashboard | Separate Funnel port (8443). Script defaults to off and is never run without owner approval. |
| Gateway joins `agentshroud-dmz` | Gateway, all bots | DMZ stays `internal: true`; `PROXY_ALLOWED_NETWORKS` stays without 10.254.113/24 so `/v1` and `/forward` remain unreachable from the edge. Network-isolation tests. |
| DMZ subnet clash between dev and prod | Both stacks | Dev override gets its own DMZ subnet. |
| Edge principal mis-resolved as owner | Whole pipeline | Principal is namespaced `edge:<vendor>:<client>`; a test asserts it is never the owner. |
| Approval-queue changes | Telegram proxy, MCP proxy, egress | Additive fields only; existing callers unchanged; their existing tests must stay green. |
| Audit lock and lockdown moved to `app_state` | Telegram proxy | The Telegram proxy keeps using the same instance; regression tests. |
| Weekly upgrade must know the new container | Sunday job | Add to `CONTAINERS` (`sunday-upgrade-apply.sh:185-189`), `DEFAULT_SCAN_IMAGES` (:129-130), compose profile `full`, and `asb` secrets. |
| Voice gateway, OpenClaw, egress proxy :8181 | Unchanged paths | No route or network changes for them; existing tests must stay green. |
