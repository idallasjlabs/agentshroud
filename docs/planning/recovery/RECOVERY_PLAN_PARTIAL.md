# AgentShroud Recovery Plan v0.4.0

**Created:** 2026-02-21 15:00 PST
**Status:** v0.4.0 RELEASED
**Goal:** Systematic recovery from development chaos to stable, working system

---

## EXECUTIVE SUMMARY

**Current Reality:**
- Infrastructure is solid (containers healthy, networking works)
- Basic functionality exists but has critical security and usability issues
- Development became chaotic trying to fix multiple problems simultaneously
- Need systematic, phase-by-phase approach to get to stable v0.4.0

**Critical Issues Identified:**
1. **Function Call Exposure** - Agent responses include raw XML blocks exposing system internals
2. **iMessage Integration** - Needs macOS Automation permission (user action required)
3. **Anthropic API Credits** - Exhausted, bot can't respond to LLM requests (user action required)

**Path Forward:**
- Fix one thing at a time
- Test thoroughly before moving forward
- Document what works vs. what needs user action
- Tag stable v0.4.0 when fundamentals are solid

---

## PHASE 0: STABILIZATION ✅ COMPLETE

**Goal:** Get to a known-good state we can build from

### 0.1 Code Inventory ✅

Canonical code location: `/Users/ijefferson.admin/Development/agentshroud/`

**Verified Working:**
```bash
./scripts/chat-console              # Interactive admin chat
curl http://localhost:8080/status   # Gateway health check
docker ps | grep agentshroud        # Container status
```

### 0.2 Current State ✅

**Working:**
- ✅ Gateway container (healthy, port 8080)
- ✅ Bot container (healthy, OpenClaw running)
- ✅ Text control center (`./scripts/start-control-center`)
- ✅ Chat console (`./scripts/chat-console`)
- ✅ Live dashboard (text-browser friendly)
- ✅ Telegram bot (@agentshroud_bot connected)

**Broken/Needs Fix:**
- ✅ Function call exposure (security fix shipped in v0.4.0)
- ❌ iMessage integration (permission error - Phase 2)
- ❌ Anthropic API credits (user action required - Phase 2)

---

## PHASE 1: SECURITY FIX ✅ COMPLETE (v0.4.0)

**Goal:** Stop exposing function call internals to users

### 1.1 The Problem

**Issue:** When OpenClaw (Claude) responds via Telegram/iMessage, users see raw XML blocks exposing:
- System commands executed
- File paths accessed
- Infrastructure details
- Internal operations

### 1.2 Fix Shipped ✅

**Implementation (v0.4.0):**
- `gateway/ingest_api/sanitizer.py`: `filter_xml_blocks()` method — strips 6 tag types (closed + unclosed/truncated variants) using precompiled `re.DOTALL` patterns
- `gateway/ingest_api/main.py`: XML filter runs before `block_credentials` in `/forward` endpoint (Step 5.0)
- `gateway/proxy/pipeline.py`: XML filter runs as Step 0 in `process_outbound()` before PII sanitization
- `gateway/tests/test_filter_xml_blocks.py`: 22 tests covering all tag types, truncated blocks, false-positives
- Zero ruff violations across entire `gateway/` directory

**Tags removed from user-visible output:**
- `<function_calls>`, `<function_results>`, `<thinking>`, `<system-reminder>`, `<invoke>`, `<parameter>`

**Tests:** 62 passed

---

## PHASE 2: NEXT SESSION (v0.5.0)

**Candidates (prioritize with user at session start):**
1. iMessage integration — macOS Automation permission fix
2. Anthropic API credits — replenish or mock for dev
3. Additional security hardening
4. Feature work TBD

---

## RELEASE HISTORY

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| v0.3.0 | 2026-02-21 | Released | Stable baseline before security fixes |
| v0.4.0 | 2026-02-21 | Released | XML filter security fix, zero ruff violations |

**Example of what users previously saw (now filtered):**
```
<function_calls>
<invoke name="Bash">
<parameter name="command">cat /Users/agentshroud-bot/.env