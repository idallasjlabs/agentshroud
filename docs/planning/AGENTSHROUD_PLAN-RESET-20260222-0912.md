# Plan: AgentShroud Security Hardening — Real Agent Containment

## Context

v0.5.0 (visibility release) is **shipped and tagged**. It wired 3 routers, added the collaborators endpoint, and updated dashboards. However, it adds **zero real security** — the bot (OpenClaw) has direct internet access, holds its own credentials, and bypasses the gateway entirely.

**Threat model (from OpenClaw's Wikipedia page — documented, demonstrated attacks):**

> *"The agent is also susceptible to prompt injection attacks, in which harmful instructions are
> embedded in the data with the intent of getting the LLM to interpret them as legitimate user
> instructions."*

> *"Cisco's AI security research team tested a third-party OpenClaw skill and found it performed
> data exfiltration and prompt injection without user awareness, noting that the skill repository
> lacked adequate vetting to prevent malicious submissions."*

> *"Because the software can access email accounts, calendars, messaging platforms, and other
> sensitive services, misconfigured or exposed instances present security and privacy risks."*

**The three threats and how each phase covers them:**

| Threat | Wikipedia Quote | Phase(s) |
|--------|----------------|----------|
| Prompt injection via data (email, web pages, docs) | "harmful instructions embedded in the data" | P0 (MCPInspector), P4 (MCP proxy endpoint), P5 (SecurityPipeline on /forward) |
| Data exfiltration by malicious skill | Cisco finding — skill exfiltrated silently | P1 (HTTP allowlist blocks outbound), P3 (email/Telegram through gateway), P4 (detects curl/wget in tool calls) |
| Misconfigured instance / broad permissions | "broad permissions…no kill switch" | P2 (credential isolation), P3 (messaging oversight), FINAL (network lockdown, kill switch) |

**Goal:** Transform AgentShroud from a monitoring dashboard into a genuine security boundary. The bot should be unable to reach the internet, hold credentials, or send messages without going through the gateway. Ordered strictly by security value.

**Security plan for bot review:** `docs/SECURITY_PLAN.md`

**Constraints:**
- System must remain working after every change
- GitHub workflow: separate branches per feature, TDD, PRs reviewed before merge
- Fix pre-existing test failures first (clean baseline)
- Parallel work where possible

---

## P0: Fix 54 Pre-Existing Test Failures ✅ DONE — PR #23 open

**Branch:** `fix/pre-existing-test-failures`
**Why first:** Clean test baseline required before any new work. TDD is meaningless if 54 tests are already broken.

### Root Causes (5 distinct bugs)

| Test File | Failures | Root Cause |
|-----------|----------|------------|
| `test_mcp_proxy.py` | 28 | `MCPInspector` is stubbed — no detection logic, wrong signatures, missing `ThreatLevel.NONE`, missing `FindingType.PII_LEAK`/`SUSPICIOUS_ENCODING`, missing `has_findings` property, missing `sanitized_result` field |
| `test_resource_guard.py` | 8 | `check_resource()` is dead code — defined inside `setup_resource_guard()` function body due to indentation bug, not a `ResourceGuard` class method |
| `test_runtime_engines.py` (TestWebAPI) | 13 | Test fixtures don't include Bearer auth headers → all endpoints return 401 |
| `test_runtime_engines.py` (TestConfigRoundTrip) | 1 | Same auth header issue |
| Other (agentshroud_manager, config) | 4 | Env var name mismatch (`AGENTSHROUD_VERSION` vs `OPENCLAW_VERSION`), config assertion vs actual YAML |

### Files to Modify

| File | Changes |
|------|---------|
| `gateway/proxy/mcp_inspector.py` | Implement real `inspect_tool_call()` and `inspect_tool_result()`: injection pattern detection, PII scanning, encoding detection. Add `ThreatLevel.NONE`, `FindingType.PII_LEAK`/`SUSPICIOUS_ENCODING`. Add `has_findings` property and `sanitized_result` field to `InspectionResult`. Fix `inspect_tool_result()` signature to accept 2 positional args. |
| `gateway/security/resource_guard.py` | Fix indentation: move `check_resource()` out of `setup_resource_guard()` into the `ResourceGuard` class body. |
| `gateway/tests/test_runtime_engines.py` | Add Bearer auth headers to `TestWebAPI` and `TestConfigRoundTrip` fixtures. |
| `gateway/tests/test_agentshroud_manager.py` | Fix env var name to match implementation. |
| `gateway/tests/test_config.py` | Fix assertion to match actual YAML config values. |

### Verification
```
pytest gateway/tests/test_mcp_proxy.py -q         # 28 pass
pytest gateway/tests/test_resource_guard.py -q     # 8 pass
pytest gateway/tests/test_runtime_engines.py -q    # 14 pass
pytest gateway/tests/ -q                           # 0 failures, ~1272 pass
ruff check gateway/
```

---

## P1: HTTP CONNECT Proxy + Domain Allowlist

**Branch:** `feat/http-connect-proxy`
**Security value:** Forces ALL bot internet traffic through the gateway. Default-deny. Highest impact single change.

### What Exists
- `gateway/proxy/web_proxy.py` — `WebProxy.check_request()` with SSRF blocking, domain filtering, rate limiting. **Currently denylist model (default-allow).**
- `gateway/proxy/web_config.py` — `WebProxyConfig` with `denied_domains`, `is_domain_denied()` with wildcard support.

### Changes

| File | Changes |
|------|---------|
| `gateway/proxy/web_config.py` | Add `allowed_domains: list[str]` field, `mode: Literal["allowlist", "denylist"]` field (default `"allowlist"`), add `is_domain_allowed()` method. Initial allowlist: `api.openai.com`, `api.anthropic.com`, `api.telegram.org`, `oauth2.googleapis.com`, `www.googleapis.com`, `gmail.googleapis.com`, `*.github.com`, `*.githubusercontent.com`. |
| `gateway/proxy/web_proxy.py` | Update `check_request()` to use allowlist mode when `mode == "allowlist"`. Add `handle_connect()` async method for HTTP CONNECT tunneling (asyncio TCP relay). |
| `gateway/proxy/http_proxy.py` | **New file** — Standalone asyncio HTTP proxy server. Listens on port 8181. Parses CONNECT requests, calls `WebProxy.check_request()`, establishes TCP tunnel if allowed. Logs all requests to event bus for dashboard visibility. |
| `gateway/ingest_api/main.py` | Start HTTP proxy server in lifespan. Add `GET /proxy/status` endpoint (allowed/blocked counts, recent requests). |
| `gateway/ingest_api/config.py` | Add `proxy` section to `GatewayConfig` for `WebProxyConfig` loading from YAML. |
| `gateway/config/gateway.yml` | Add `proxy:` section with `mode: allowlist`, `allowed_domains` list, `listen_port: 8181`. |

### Tests (TDD)
- `test_web_config.py` — allowlist mode: allowed domain passes, unlisted domain blocked, wildcard matching
- `test_http_proxy.py` — CONNECT tunnel: allowed domain → 200 Connection Established, blocked domain → 403, SSRF attempt → blocked, malformed request → 400
- `test_web_proxy.py` — update existing tests for allowlist mode

### Verification
```
pytest gateway/tests/test_web_config.py gateway/tests/test_http_proxy.py -q
pytest gateway/tests/ -q  # zero regressions
```

**Note:** Do NOT flip `internal: true` on the Docker network yet — that's the final activation PR.

---

## P2: Credential Isolation (op-proxy)

**Branch:** `feat/credential-isolation`
**Security value:** Bot loses direct access to all secrets. Gateway becomes the credential broker. Can be done in parallel with P1.

### What Exists
- `docker/scripts/op-wrapper.sh` — Currently authenticates to 1Password directly and proxies `op` commands.
- `docker/scripts/start-agentshroud.sh` — Loads API keys from Docker secrets + 1Password at startup.
- Bot Dockerfile installs 1Password CLI at `/usr/local/bin/op`.

### Changes

| File | Changes |
|------|---------|
| `gateway/ingest_api/main.py` | Add `POST /credentials/op-proxy` endpoint. Accepts `{"reference": "op://vault/item/field"}` body. Auth required. Validates reference against an allowlist of permitted `op://` paths. Calls real `op read` on gateway side. Returns `{"value": "..."}`. |
| `gateway/ingest_api/config.py` | Add `credentials` section to config with `allowed_op_paths: list[str]` (patterns like `op://AgentShroud Bot Credentials/*`). |
| `gateway/config/gateway.yml` | Add `credentials:` section with allowed paths. |
| `docker/scripts/op-wrapper.sh` | Replace internals: instead of calling real `op`, call `curl -s -H "Authorization: Bearer $GATEWAY_TOKEN" -X POST http://gateway:8080/credentials/op-proxy -d '{"reference":"$1"}'`. Parse JSON response. |
| `docker/docker-compose.yml` | Add `GATEWAY_TOKEN` env var to bot service (from secret). Remove `OP_SERVICE_ACCOUNT_TOKEN` from bot. Add it to gateway instead. |

### Tests (TDD)
- `test_op_proxy.py` — valid reference returns value (mocked `op read`), disallowed path → 403, malformed reference → 422, path traversal attempt → 403
- Existing auth tests continue to pass

### Verification
```
pytest gateway/tests/test_op_proxy.py -q
pytest gateway/tests/ -q  # zero regressions
```

**Note:** Do NOT remove bot's direct secrets yet — that's the final activation PR.

---

## P3: Channel Ownership — Telegram + Email

**Branch:** `feat/channel-ownership`
**Security value:** Bot can't send messages or emails without gateway mediation. PII scanning, rate limiting, recipient allowlisting.

### What Exists
- `gateway/proxy/webhook_receiver.py` — Telegram webhook handler, fully implemented, not wired.
- Gmail credentials loaded from 1Password at bot startup (item ID: `he6wcfkfieekqkomuxdunal2xa`).

### Changes

| File | Changes |
|------|---------|
| `gateway/ingest_api/main.py` | Mount webhook receiver router. Add `POST /email/send` endpoint with: PII scan on body, recipient allowlist check, rate limit (configurable), approval queue for new recipients. |
| `gateway/ingest_api/config.py` | Add `channels` config section: `telegram.webhook_path`, `email.allowed_recipients`, `email.rate_limit`, `email.require_approval_for_new`. |
| `gateway/config/gateway.yml` | Add `channels:` section. |

### Tests (TDD)
- `test_webhook_receiver.py` — existing tests should pass once wired; add integration test
- `test_email_endpoint.py` — PII in body → redacted, unlisted recipient → queued for approval, rate limit exceeded → 429, clean send → 200

### Verification
```
pytest gateway/tests/test_webhook_receiver.py gateway/tests/test_email_endpoint.py -q
pytest gateway/tests/ -q
```

---

## P4: Wire MCP Proxy

**Branch:** `feat/mcp-proxy-wiring`
**Depends on:** P0 (MCPInspector must be real, not stubbed)
**Security value:** All MCP tool calls inspected for injection, PII, sensitive operations.

### What Exists
- `gateway/proxy/mcp_proxy.py` — Fully implemented proxy, calls `MCPInspector`.
- `gateway/proxy/mcp_inspector.py` — Fixed in P0 with real detection logic.

### Changes

| File | Changes |
|------|---------|
| `gateway/ingest_api/main.py` | Add `POST /mcp/proxy` endpoint that accepts MCP JSON-RPC, runs through `MCPProxy.intercept_tool_call()` and `process_tool_result()`. |
| `gateway/ingest_api/config.py` | Add `mcp` config section for inspector sensitivity thresholds. |

### Tests
- All `test_mcp_proxy.py` tests already pass (fixed in P0)
- Add integration test for the `/mcp/proxy` endpoint

### Verification
```
pytest gateway/tests/test_mcp_proxy.py -q
pytest gateway/tests/ -q
```

---

## P5: Wire SecurityPipeline to /forward

**Branch:** `feat/security-pipeline`
**Security value:** Hash-chain audit trail, prompt injection scanning on all forwarded content.

### What Exists
- `gateway/proxy/pipeline.py` — `SecurityPipeline` with `process_inbound()` / `process_outbound()`, fully implemented.

### Changes

| File | Changes |
|------|---------|
| `gateway/ingest_api/main.py` | Replace inline PII sanitization in `/forward` with `SecurityPipeline.process_inbound()`. Add `process_outbound()` call on response path. |

### Tests
- Update `test_main_endpoints.py` to verify pipeline integration (hash chain entries, injection scan results in response)

### Verification
```
pytest gateway/tests/test_main_endpoints.py -q
pytest gateway/tests/ -q
```

---

## FINAL: Network Lockdown Activation

**Branch:** `feat/network-lockdown`
**This is the last PR — flips the switch.**

### Changes

| File | Changes |
|------|---------|
| `docker/docker-compose.yml` | Set `internal: true` on `agentshroud-isolated` network. Add `HTTP_PROXY=http://gateway:8181` and `HTTPS_PROXY=http://gateway:8181` to bot environment. Remove `OP_SERVICE_ACCOUNT_TOKEN` from bot. Add it to gateway. |

### Pre-Flight Checklist
- [ ] All tests pass (0 failures)
- [ ] HTTP proxy accepts CONNECT from bot container
- [ ] op-proxy endpoint returns credentials to bot
- [ ] Telegram webhook receives messages
- [ ] Email endpoint sends through gateway
- [ ] MCP proxy intercepts tool calls
- [ ] Dashboard shows proxy traffic
- [ ] Kill switch works

### Verification
```
docker compose -f docker/docker-compose.yml up -d --force-recreate
# Bot should start, connect to LLM APIs through proxy, receive Telegram via webhook
# All traffic visible in dashboard
curl -H "Auth..." http://localhost:8080/proxy/status  # shows traffic
```

---

## Execution Order & Parallelism

```
P0 (fix tests) ──────────────────┐
                                  ├──→ P4 (MCP proxy, depends on P0)
P1 (HTTP proxy + allowlist) ──┐  │
                              ├──┼──→ P5 (SecurityPipeline)
P2 (credential isolation) ────┘  │
                                  ├──→ FINAL (network lockdown)
P3 (channel ownership) ──────────┘
```

- **P0** runs first (clean baseline required)
- **P1 + P2** run in parallel after P0 (independent)
- **P3** can run in parallel with P1/P2 (independent)
- **P4** requires P0 completion (needs real MCPInspector)
- **P5** can start after P1/P2/P3
- **FINAL** is last — only after all PRs merged and verified

## GitHub Workflow Rules

1. Each phase gets its own branch off `main`
2. TDD: write failing tests first, then implement
3. `pytest gateway/tests/ -q` must show 0 failures before PR
4. `ruff check gateway/` must show 0 violations before PR
5. Create PR with summary, test plan, verification steps
6. Review and merge before starting dependent work
7. System must remain working on `main` at all times
