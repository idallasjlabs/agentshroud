# AgentShroud Recovery Plan v0.4.0

**Created:** 2026-02-21 15:00 PST
**Status:** ACTIVE
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
- ❌ Function call exposure (security issue - Phase 1)
- ❌ iMessage integration (permission error - Phase 2)
- ❌ Anthropic API credits (user action required - Phase 2)

---

## PHASE 1: SECURITY FIX (CURRENT PRIORITY)

**Goal:** Stop exposing function call internals to users

### 1.1 The Problem

**Issue:** When OpenClaw (Claude) responds via Telegram/iMessage, users see raw XML blocks exposing:
- System commands executed
- File paths accessed
- Infrastructure details
- Internal operations

**Example of what users currently see:**
```
<function_calls>
<invoke name="Bash">
<parameter name="command">cat /Users/agentshroud-bot/.env</parameter>
</invoke>
</function_calls>

This is confidential system information!
```

**Impact:**
- Security risk (exposes internal paths, commands, architecture)
- Poor user experience (technical noise in conversational interface)
- Unprofessional (looks like a bug or debug mode)

### 1.2 Root Cause Analysis

**Where it happens:**
- `services/gateway/router.py` - routes requests to OpenClaw
- OpenClaw returns `agent_response` field containing full Claude response
- Gateway passes this directly to message platforms without filtering

**Why it happens:**
- Claude's tool use responses include XML blocks by design (MCP protocol)
- Gateway currently treats `agent_response` as opaque text
- No post-processing or sanitization layer exists

### 1.3 Solution Options

**Option A: Filter XML Blocks (RECOMMENDED)**
- Strip `<function_calls>`, `<invoke>`, and similar tags from responses
- Preserve actual text content Claude meant for users
- Minimal code change, backward compatible

**Option B: Configure Claude to Suppress XML**
- Modify system prompt to instruct Claude not to include tool call blocks
- Risk: May not be reliable (Claude's format is part of MCP spec)
- Not recommended: Fighting against designed behavior

**Option C: Document as "Transparency Feature"**
- Accept current behavior
- Market as "see what the AI is doing"
- Not acceptable: Security and UX concerns outweigh any transparency benefit

**Decision: Option A (Response Filter)**

### 1.4 Implementation Plan

**File to modify:** `services/gateway/router.py`

**Changes needed:**
1. Create `filter_xml_blocks()` function
2. Apply to `agent_response` before returning to platforms
3. Add unit tests for edge cases

**Pseudocode:**
```python
import re

def filter_xml_blocks(text: str) -> str:
    """Remove XML function call blocks from agent responses."""
    # Remove <function_calls>...</function_calls> blocks
    text = re.sub(r'<function_calls>.*?</function_calls>', '', text, flags=re.DOTALL)
    # Remove standalone <...> blocks
    text = re.sub(r'<.*?</.*?>', '', text, flags=re.DOTALL)
    # Clean up excessive whitespace
    text = re.sub(r'\n\n\n+', '\n\n', text)
    return text.strip()

# Apply in /chat endpoint
response_text = filter_xml_blocks(agent_response)
```

### 1.5 Testing Strategy

**Test cases:**
1. Response with single function call block
2. Response with multiple function call blocks
3. Response with no function calls (ensure unchanged)
4. Response with mixed text and function calls
5. Edge case: Function call at start, middle, end of response

**Validation:**
```bash
# Unit tests
pytest tests/test_response_filter.py -v

# Integration test via chat console
./scripts/chat-console
> "What's my IP address?"
# Should see only answer, not function call blocks

# End-to-end via Telegram
# Send message to @agentshroud_bot
# Verify clean response
```

### 1.6 Success Criteria

**Done when:**
- ✅ Users see only conversational text responses
- ✅ No XML blocks visible in Telegram/iMessage/console
- ✅ Unit tests pass with 100% coverage on filter function
- ✅ Integration tests confirm end-to-end filtering
- ✅ No impact on actual functionality (commands still execute)

---

## PHASE 2: USER ACTIONS REQUIRED

**Goal:** Enable features blocked by external dependencies

### 2.1 Top Up Anthropic API Credits

**Issue:** Anthropic account has $0 balance, Claude API calls fail

**Evidence:**
```
AnthropicError: 429 Too Many Requests
Your account has exceeded its API rate limit
```

**Action Required:**
1. Visit https://console.anthropic.com/settings/billing
2. Add payment method if not already configured
3. Purchase credits (minimum $20 recommended)
4. Wait 2-5 minutes for credit activation

**Verification:**
```bash
# Test via chat console
./scripts/chat-console
> "Hello"
# Should get response, not rate limit error
```

**Dependencies:**
- User must have access to Anthropic Console
- Valid payment method required
- Cannot be automated (requires human decision/payment)

### 2.2 Grant iMessage Automation Permission

**Issue:** macOS Security & Privacy blocks automation access to Messages.app

**Error:**
```
osascript: Not authorized to send Apple events to Messages
```

**Action Required:**
Follow instructions in `IMESSAGE_PERMISSION_FIX.md`:
1. Open System Settings > Privacy & Security > Automation
2. Find Terminal (or Docker, if running from container)
3. Enable checkbox for Messages
4. Restart container if necessary

**Alternative approach (if container needs permission):**
```bash
# Grant Docker Desktop automation permission
# System Settings > Privacy & Security > Automation > Docker > Messages
```

**Verification:**
```bash
# Test manual send from host
osascript -e 'tell application "Messages" to send "test" to buddy "YOUR_NUMBER"'

# Should send successfully, no permission error
```

**Dependencies:**
- User has admin access to macOS
- User has physical access to the Mac
- Cannot be automated (requires GUI interaction)

### 2.3 Verify Both Working

**Once both actions complete:**
```bash
# 1. Check Anthropic credits
curl -H "x-api-key: $ANTHROPIC_API_KEY" https://api.anthropic.com/v1/messages \
  -d '{"model":"claude-sonnet-4-5","max_tokens":10,"messages":[{"role":"user","content":"hi"}]}'
# Should return response, not 429 error

# 2. Check iMessage permission
osascript -e 'tell application "Messages" to send "AgentShroud test" to buddy "YOUR_NUMBER"'
# Should send message successfully

# 3. Test via AgentShroud chat
./scripts/chat-console
> "Send an iMessage to MY_NUMBER saying 'test successful'"
# Should work end-to-end
```

---

## PHASE 3: iMESSAGE INTEGRATION TEST

**Goal:** Verify full iMessage workflow functions correctly

**Prerequisites:**
- Phase 1 complete (response filter deployed)
- Phase 2 complete (API credits + permissions granted)

### 3.1 Test Manual Send from Host

**Purpose:** Confirm macOS Messages.app is functional

```bash
# From host terminal (not container)
osascript -e 'tell application "Messages" to send "Manual test from host" to buddy "+1234567890"'
```

**Expected:** Message appears in Messages.app and sends to recipient

### 3.2 Test from Container

**Purpose:** Confirm container can access host Messages.app

```bash
# From inside agentshroud-bot container
docker exec -it agentshroud-bot bash
osascript -e 'tell application "Messages" to send "Test from container" to buddy "+1234567890"'
```

**Expected:** Message sends successfully (proves automation permission is set correctly)

### 3.3 Test via OpenClaw /chat Endpoint

**Purpose:** Verify gateway routes to bot and bot executes iMessage tool

```bash
# From host
curl -X POST http://localhost:8080/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Send an iMessage to +1234567890 saying \"test via API\""}'
```

**Expected:**
- Gateway returns success
- Claude processes request
- iMessage sends
- Response includes confirmation (but no XML blocks, thanks to Phase 1)

### 3.4 Verify End-to-End Message Flow

**Purpose:** Test real-world usage pattern

**Steps:**
1. Send message to AgentShroud via Telegram: `"Send an iMessage to +1234567890 with the current time"`
2. Verify Telegram response is clean (no XML)
3. Verify iMessage was sent to recipient
4. Verify iMessage content is correct

**Success criteria:**
- ✅ Message received in Telegram
- ✅ No XML blocks in Telegram response
- ✅ iMessage sent successfully
- ✅ iMessage content matches request
- ✅ No errors in gateway/bot logs

---

## PHASE 4: CLEANUP & v0.4.0 RELEASE

**Goal:** Stabilize codebase and tag first production-ready release

### 4.1 Remove Obsolete Code/Docs

**Files to remove/consolidate:**
```bash
# Duplicate or outdated docs
rm -f docs/old_architecture.md
rm -f docker/deprecated_configs/

# Obsolete scripts
rm -f scripts/legacy-*.sh

# Test artifacts
rm -rf .pytest_cache __pycache__

# Old development notes (keep in git history)
rm -f NOTES_2025.md
```

**Keep:**
- All core functionality code
- Current architecture docs
- Working scripts
- RECOVERY_PLAN.md (this document, for reference)
- IMESSAGE_PERMISSION_FIX.md

### 4.2 Update README

**File:** `/Users/ijefferson.admin/Development/agentshroud/README.md`

**Required updates:**
- ✅ Accurate feature list (remove unimplemented features)
- ✅ Prerequisites (Anthropic API key, iMessage permissions)
- ✅ Quick start guide (working commands only)
- ✅ Troubleshooting section (common permission errors)
- ✅ Remove outdated sections (old architecture, deprecated features)

**Template:**
```markdown
# AgentShroud v0.4.0

AI-powered messaging gateway with iMessage and Telegram integration.

## Features
- Claude AI integration (Anthropic API)
- Telegram bot interface
- iMessage send capabilities (macOS only)
- Docker containerized deployment

## Prerequisites
- Docker Desktop (macOS/Linux)
- Anthropic API key (with credits)
- macOS Automation permissions for Messages.app

## Quick Start
1. `./scripts/start-agentshroud`
2. `./scripts/chat-console`

## Troubleshooting
See IMESSAGE_PERMISSION_FIX.md for permission issues.
```

### 4.3 Create CHANGELOG

**File:** `/Users/ijefferson.admin/Development/agentshroud/CHANGELOG.md`

**Content:**
```markdown
# Changelog

## [0.4.0] - 2026-02-21

### Added
- Response filtering to remove XML function call blocks
- Comprehensive permission documentation (IMESSAGE_PERMISSION_FIX.md)
- Recovery plan for systematic debugging (RECOVERY_PLAN.md)
- Improved error handling for API rate limits

### Fixed
- Security issue: Raw function call blocks exposed to users
- iMessage automation permission documentation
- Container health check reliability

### Changed
- Standardized script naming (start-agentshroud.sh)
- Updated README to reflect actual working features

### Removed
- Obsolete legacy scripts
- Unimplemented feature documentation
- Development debug artifacts
```

### 4.4 Tag v0.4.0

**Process:**
```bash
cd /Users/ijefferson.admin/Development/agentshroud

# Ensure clean working directory
git status
# If clean, proceed. If not, commit outstanding changes first.

# Create annotated tag
git tag -a v0.4.0 -m "Release v0.4.0 - Stabilization and Security Fixes

- Fixed function call exposure vulnerability
- Documented iMessage permission requirements
- Cleaned up codebase and documentation
- Established systematic recovery workflow

See CHANGELOG.md for full details."

# Push tag to remote
git push origin v0.4.0

# Verify
git tag -l -n9 v0.4.0
```

### 4.5 Deploy to Production

**Definition:** "Production" = Local Mac running 24/7 with stable containers

**Deployment steps:**
```bash
# 1. Stop existing containers
docker-compose down

# 2. Pull latest code (if using git deployment)
git checkout v0.4.0

# 3. Rebuild containers with updated code
docker-compose build

# 4. Start with production config
docker-compose up -d

# 5. Verify health
./scripts/health-check

# 6. Test critical paths
./scripts/chat-console
> "Send iMessage test to MY_NUMBER"
> "What's the current time?"

# 7. Monitor logs for 10 minutes
docker-compose logs -f --tail=50
```

**Rollback plan (if issues):**
```bash
# Stop broken version
docker-compose down

# Revert to previous tag
git checkout v0.3.x  # or last known good version

# Rebuild and restart
docker-compose build
docker-compose up -d
```

---

## NEXT STEPS

**Immediate actions (in order):**

1. **Complete Phase 1** (in progress)
   - [ ] Implement `filter_xml_blocks()` in `router.py`
   - [ ] Write unit tests for response filter
   - [ ] Deploy and test via chat console
   - [ ] Verify via Telegram bot

2. **Execute Phase 2** (user actions)
   - [ ] Top up Anthropic API credits ($20 minimum)
   - [ ] Grant iMessage Automation permission (System Settings)
   - [ ] Verify both working

3. **Run Phase 3** (integration tests)
   - [ ] Test manual iMessage send
   - [ ] Test container iMessage send
   - [ ] Test via OpenClaw API
   - [ ] Test end-to-end via Telegram

4. **Complete Phase 4** (release prep)
   - [ ] Clean up obsolete files
   - [ ] Update README.md
   - [ ] Create CHANGELOG.md
   - [ ] Tag v0.4.0
   - [ ] Deploy to production

**Success checkpoint:**
After completing all phases, you should have:
- ✅ Secure responses (no XML exposure)
- ✅ Working iMessage integration
- ✅ Working Claude API integration
- ✅ Clean, documented codebase
- ✅ Stable v0.4.0 release

**Document location:** `/Users/ijefferson.admin/Development/agentshroud/RECOVERY_PLAN.md`

---

*This recovery plan was created systematically to escape development chaos and establish a stable foundation. Follow phases in order. Test thoroughly. Ship v0.4.0 when all phases complete.*