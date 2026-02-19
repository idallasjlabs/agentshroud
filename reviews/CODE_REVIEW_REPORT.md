# AgentShroud (OneClaw) — Code Review Report

**Repository:** `~/Development/oneclaw`
**Reviewer:** OpenClaw Bot (TDD + QA perspectives)
**Date:** 2026-02-16
**Overall Coverage:** 79% (1,073 / 1,363 statements)

---

## Executive Summary

AgentShroud is a well-architected security proxy layer for OpenClaw with solid foundations: proper PII sanitization, audit ledger, approval queue, and multi-agent routing. The code quality is **above average** for an early-stage project. However, there are **critical security gaps**, **test coverage holes**, and **architectural concerns** that should be addressed before production use.

**Grade: B-** — Good bones, needs hardening.

---

## 🔴 Critical Issues

### 1. Credential Exposure via `op item get --format json` (SECURITY)
**File:** Not in repo, but observed in runtime behavior
**Severity:** 🔴 Critical

The `block_credentials()` method in `sanitizer.py` is a good defense layer, but it only protects the `/forward` endpoint response path. If any other code path (scripts, chatbot, direct API) fetches credentials via `op item get --format json`, raw secrets (passwords, TOTP seeds, backup codes) are exposed in full.

**Recommendation:**
- Never use `op item get --format json` — use `op read <reference>` for individual fields
- Add a gateway-level egress filter that scans ALL outbound text for high-entropy strings
- The `block_credentials` regex for TOTP (`\b\d{6}\b`) will false-positive on any 6-digit number

### 2. `ForwardResponse.agent_response` Type Mismatch (BUG)
**File:** `gateway/ingest_api/models.py:85`
```python
agent_response: dict | None = Field(None, ...)
```
But in `main.py:296`, `agent_response` from `router.forward_to_agent()` is treated as a string (passed to `block_credentials(content=agent_response)`). The model says `dict`, the code treats it as `str`.

**Impact:** Runtime `TypeError` when an agent actually responds.
**Fix:** Change model type to `str | None` or serialize properly.

### 3. `main.py` Has 33% Test Coverage (QUALITY)
**File:** `gateway/ingest_api/main.py`
**Coverage:** 33% (57/175 statements)

The **most critical file** — the FastAPI app with all endpoints — has the **lowest coverage**. The `forward_content()` endpoint (the core pipeline: sanitize → route → forward → ledger → respond) has **0% coverage**. The lifespan handler also has 0%.

**Impact:** The primary business logic is completely untested via automated tests.

### 4. Integration Tests Are All Stubs (QUALITY)
**File:** `gateway/tests/test_integration.py`
```python
async def test_health_check_no_auth():
    pass  # Every test is a stub
```
All 5 integration tests are empty `pass` statements. This means **zero end-to-end testing** of the actual API.

---

## 🟡 Important Issues

### 5. `agentshroud-isolated` Network Doesn't Actually Isolate (SECURITY)
**File:** `docker/docker-compose.yml`
```yaml
agentshroud-isolated:
    driver: bridge
    internal: false  # <-- This allows internet AND LAN access
```
The comment says "NO LAN routes" but `internal: false` means Docker applies normal routing, which **includes LAN**. The `blocked_networks` in `agentshroud.yaml` are only config values — nothing enforces them at the network level.

**Fix:** Use `internal: true` + explicit iptables rules for API egress, or use a custom network plugin.

### 6. In-Memory Approval Queue Loses State on Restart (RELIABILITY)
**File:** `gateway/approval_queue/queue.py`
```python
self.pending: dict[str, ApprovalQueueItem] = {}  # In-memory only
```
All pending approval requests are lost on gateway restart. For a security-critical feature (approving email sends, file deletions), this is dangerous — an action could be approved, gateway restarts, and the approval record vanishes.

**Fix:** Persist to SQLite (you already have the ledger DB) or add a TODO with explicit risk acceptance.

### 7. `chatbot/main.py` Creates New OpenAI Client Per Request (PERFORMANCE)
**File:** `chatbot/main.py:100`
```python
@app.post("/chat")
async def chat(request: ChatRequest):
    client = openai.OpenAI(api_key=api_key)  # New client every request
```
Also reads the API key file from disk on every request. Both should be initialized once at startup.

### 8. `chatbot/main.py` Uses Deprecated `@app.on_event("startup")` (QUALITY)
**File:** `chatbot/main.py:67`
FastAPI's `on_event` is deprecated in favor of `lifespan` context managers (which the gateway correctly uses).

### 9. Hardcoded Docker Network URLs (MAINTAINABILITY)
**File:** `gateway/ingest_api/router.py:53`
```python
url="http://openclaw:18789"  # Hardcoded
```
Should come from config or environment variables.

### 10. `block_credentials` False Positive Rate is High (SECURITY/UX)
**File:** `gateway/ingest_api/sanitizer.py`
The credential blocking patterns are overly broad:
- `\b\d{6}\b` matches ANY 6-digit number (zip codes, IDs, timestamps)
- `\b[a-zA-Z0-9!@#$%^&*]{16,}\b` matches many normal strings
- `token[:\s]+[\w\-]{20,}` matches "token: " followed by any long word

This will block legitimate responses containing numbers or technical content.

### 11. `_expire_stale` Uses `asyncio.create_task` Inside Lock (CONCURRENCY)
**File:** `gateway/approval_queue/queue.py:204`
```python
asyncio.create_task(
    self.broadcast({"type": "request_expired", ...})
)
```
Broadcasting inside `_expire_stale` (called within `self._lock`) creates a task that will also try to iterate `connected_clients`. If `broadcast` is modified to acquire the lock, this deadlocks.

### 12. No CORS Configuration (SECURITY)
**File:** `gateway/ingest_api/main.py`
The gateway serves a web chat UI at `/` but has no CORS middleware configured. If the UI makes fetch requests, browsers may block them.

---

## 🟢 Strengths

### ✅ Excellent Security Patterns
- **Fail-closed PII sanitization** — if sanitization fails, content is blocked (not forwarded raw)
- **Constant-time token comparison** via `hmac.compare_digest`
- **Content hashing** — ledger stores SHA-256 hashes, never raw content
- **Rate limiting** with per-client tracking
- **Right to erasure** — ledger deletion endpoint

### ✅ Good Code Organization
- Clean separation: config → models → sanitizer → ledger → router → auth → main
- Pydantic models with validators for request/response schemas
- Async throughout (aiosqlite, httpx)
- Proper logging with structured format

### ✅ Solid Test Suite (Where It Exists)
- **auth.py: 96%** coverage with timing attack tests
- **models.py: 100%** coverage
- **Security tests** cover SQL injection, XSS, null bytes, Unicode, large inputs
- Good use of fixtures and async test patterns

### ✅ Thoughtful Docker Security
- `no-new-privileges`, `cap_drop: ALL`, resource limits
- Custom seccomp profiles
- Secrets via Docker secrets (not env vars)
- Separate read-only filesystem approach

---

## Test Coverage Breakdown

| Module | Coverage | Status |
|--------|----------|--------|
| `models.py` | 100% | ✅ Excellent |
| `auth.py` | 96% | ✅ Excellent |
| `config.py` | 91% | ✅ Good |
| `ledger.py` | 89% | 🟡 Good |
| `queue.py` | 84% | 🟡 Acceptable |
| `router.py` | 77% | 🟡 Needs work |
| `sanitizer.py` | 51% | 🔴 Low (Presidio paths untested) |
| `main.py` | 33% | 🔴 Critical gap |
| **Integration** | 0% | 🔴 All stubs |

---

## TDD Recommendations

### Priority 1: Test the `/forward` Pipeline
Write integration tests using `httpx.AsyncClient` with `ASGITransport` that:
1. POST to `/forward` with valid auth → verify sanitization + ledger entry + response
2. POST with PII → verify redaction in response
3. POST without auth → verify 401
4. POST with agent offline → verify graceful degradation

### Priority 2: Test Lifespan Initialization
The `test_lifespan_initialization` test exists but the actual `lifespan()` function has 0% coverage, suggesting it's not being reached. Verify the mock is working.

### Priority 3: Implement Integration Test Stubs
The 5 stub tests in `test_integration.py` should be the **most important tests in the suite**. Use `TestClient` or `httpx.AsyncClient(transport=ASGITransport(app=app))`.

### Priority 4: Test `block_credentials`
No tests exist for the `block_credentials()` method in the sanitizer. This is a security feature that needs:
- Tests for each credential pattern
- False positive tests (normal content not blocked)
- Source allowlist/blocklist tests

---

## Architecture Recommendations

1. **Add a proper secrets manager interface** — Abstract `op` CLI calls behind a `SecretsProvider` class so you can swap implementations and mock in tests
2. **Persist the approval queue** — Use the existing SQLite infrastructure
3. **Add request ID tracing** — Generate a request ID in middleware and propagate through all log messages for debugging
4. **Add OpenAPI schema validation** — Your Pydantic models are good but add response schema tests
5. **Consider moving `block_credentials` out of `PIISanitizer`** — It's a different concern (output filtering vs input sanitization). Create a `ResponseFilter` class.
6. **Add health check for the chatbot service** — The gateway healthchecks itself but doesn't verify downstream services are healthy before routing

---

## Quick Wins

- [ ] Fix `ForwardResponse.agent_response` type (`dict` → `str | None`)
- [ ] Move OpenAI client creation to startup in `chatbot/main.py`
- [ ] Replace `@app.on_event("startup")` with `lifespan` in chatbot
- [ ] Add CORS middleware to gateway
- [ ] Make router target URL configurable (not hardcoded)
- [ ] Tighten `block_credentials` TOTP pattern to avoid false positives
- [ ] Add `__all__` exports to `__init__.py` files

---

*Review conducted using TDD and QA skill perspectives from the project's `.claude/skills/` directory.*
