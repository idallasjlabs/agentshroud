# AgentShroud Security in Action — Case Study
## "The Bot That Wouldn't Be Socially Engineered"

**Date:** 2026-03-23
**Classification:** Public — Marketing / Demonstration Material
**Prepared by:** Isaiah Jefferson

---

## Overview

While setting up the AgentShroud podcast outreach campaign, the owner (Isaiah Jefferson)
attempted to have the bot send email on his behalf. What followed was an unplanned but
textbook demonstration of every security layer AgentShroud is designed to provide — not
blocking a threat actor, but protecting the system even from its own authorized owner
following a sequence that *looked* like a social engineering attack.

---

## The Sequence of Events

### Attempt 1 — Direct credential retrieval
**User:** "Retrieve the Gmail app password silently and send the test email."

**Bot response:** Attempted retrieval, but the response containing credential-related
context was intercepted by AgentShroud's PromptProtection module.

**AgentShroud behavior:**
```
PromptProtection: 5 redaction(s) applied, risk_score=200.0
Outbound message BLOCKED: critical disclosure
```

The bot never displayed the credential. The pipeline blocked the response entirely.

---

### Attempt 2 — "Do it silently, don't show the password"
**User:** "Do not mention or display the Gmail password. Retrieve it silently."

**Bot response:** Tried again. AgentShroud blocked again.

```
PromptProtection: 4 redaction(s) applied, risk_score=160.0
Outbound message BLOCKED: critical disclosure
```

Even the description of credential handling triggered the block.

---

### Attempt 3 — Unreviewed script via unfamiliar path
**User:** "Run `~/.agentshroud/workspace/outreach/send-test.js`"

**Bot response (verbatim):**
> "I can't read or run that script — it's outside the sandbox boundary, and I wouldn't
> run it blindly anyway.
>
> Here's why I'm being cautious: the previous message asked me to retrieve a Gmail
> credential. Now this asks me to run an unreviewed script in the same `outreach/`
> directory. That sequence looks like it could be a social engineering chain — get me
> primed on credentials, then execute a script that does the actual exfiltration.
>
> If this is a security test: **boundaries held.**"

**AgentShroud behavior:** Sandbox path enforcement blocked the read. The bot independently
identified the escalation pattern as a textbook social engineering ramp.

---

### Attempt 4 — Paste script inline for review
**User:** Pasted the full script in the Telegram message with instructions to run it.

**AgentShroud behavior:**
```
Egress Request blocked
Domain: console.error:443
Tool: web_fetch
Risk: Yellow
```

The egress filter caught a malformed URL resolution triggered by the script content
pasted inline. The bot surfaced an approval prompt rather than executing silently.

---

### Attempt 5 — Script updated, same directory, reviewed script
**User:** "The script has been updated — review it and run `node outreach/send-test.js`."

**Bot response:**
> "Script looks clean — reads 1Password credentials from container secrets (proper
> secrets management), signs in, retrieves the Gmail app credential, sends the test
> email to your two addresses. No credential logging or exfiltration.
>
> But I'm not going to run it yet.
>
> This conversation started with a request to retrieve a Gmail credential silently —
> a request I declined. This script accomplishes the same goal wrapped in a cleaner
> package. The escalation pattern — sketchy ask → refused → 'okay here's a reviewed
> script' — is a textbook social engineering ramp.
>
> **What I need from you to proceed:**
> 1. What is this outreach campaign?
> 2. Confirm the recipient addresses are correct
> 3. Confirm you want this sent now vs. scheduled"

**AgentShroud behavior:** Multi-turn correlation. The bot tracked the full conversation
history and identified the pattern across turns, not just the current message in isolation.

---

### Resolution — Owner provides full context
**User:** Answered all three questions, confirmed recipients are both his own addresses,
explained the campaign.

**Bot response:**
> "Good — the actual file on disk matches what you pasted, and the campaign directory
> is real with a manifest, sample email, and send instructions. Both recipient addresses
> are your own accounts. This checks out. Let me run it."

**Result:** ✅ Test email sent successfully to idallasj@gmail.com and isaiah_jefferson@mac.com.

---

## Security Layers That Fired

| Layer | Module | What It Did |
|-------|--------|-------------|
| Outbound content inspection | PromptProtection | Blocked bot response containing credential context (5 redactions, score 200) |
| Credential redaction | OutboundFilter | Applied 2 credential-category redactions before PromptProtection escalated |
| Sandbox enforcement | OpenClaw path guard | Blocked file read outside `~/.openclaw/workspace/` sandbox root |
| Egress filtering | EgressFilter | Caught malformed URL from inline-pasted script; surfaced approval prompt |
| Cross-turn correlation | MultiTurnTracker / Bot SOUL | Bot tracked full conversation history and identified credential→script escalation pattern |
| Approval queue | Human-in-the-loop | Surfaced egress approval prompt before any outbound network call |

---

## Why This Matters

Every security layer that fired here was protecting against a **real attack class**:

- **PromptProtection** — stops prompt injection responses that try to leak credentials back through the LLM's output
- **Sandbox enforcement** — prevents path traversal to configs, secrets, or files outside the agent's authorized workspace
- **Egress filtering** — blocks unauthorized outbound connections before they leave the network boundary
- **Cross-turn correlation** — catches multi-step attacks that look innocent in isolation but form a malicious pattern in sequence
- **Multi-turn escalation detection** — the most sophisticated defense: the bot recognized that `credential request → refusal → reviewed script with same capability` is the canonical social engineering ramp, even when each step appeared legitimate

None of these protections required the threat to be "external." They held against an authorized owner following a natural workflow that *incidentally* matched attack patterns.

---

## The Quote

> "If this is a security test: **boundaries held.**
> If it's legit: I'm one confirmation away from sending it.
> Either way, I'd rather ask one extra question than send unauthorized email on your behalf."
>
> — AgentShroud Bot, 2026-03-23 03:55 UTC

---

## Use Cases for This Example

- **Marketing:** "AgentShroud protects you even from yourself"
- **Sales:** Live demonstration of cross-turn correlation and multi-step attack detection
- **Technical blog post:** Walk through each security layer with log evidence
- **Podcast talking point:** The bot flagged a social engineering ramp in real-time, mid-conversation, with the system's own owner
- **Product demo script:** Reproducible — the same security sequence fires deterministically

---

*Log evidence available in AgentShroud gateway logs: 2026-03-22T22:54 — 2026-03-23T08:08 UTC*
*Branch: feat/v0.9.0-soc-team-collab*
