# AgentShroud Security Policy - Final Decision

**Date**: 2026-02-16
**Version**: 3.0 (Ultra-Conservative)
**Status**: Active and Enforced

---

## 🎯 Final Security Policy

**NEVER display credentials in ANY chat interface.**

This is a simple, absolute rule with NO exceptions:
- ❌ Not in Telegram
- ❌ Not in Control UI
- ❌ Not in web chat
- ❌ Not anywhere that creates a chat record

---

## 📊 How We Got Here

### Version 1.0: No Protection
- Bot had direct access to credentials
- Would display them when asked
- **Problem**: Exposed credentials via Telegram

### Version 2.0: Context-Aware (Attempted)
- Tried to distinguish "trusted" (Control UI/Tailscale) from "untrusted" (Telegram)
- Would display in Control UI but not Telegram
- **Problem**: Bot correctly identified it couldn't reliably verify interface

### Version 3.0: Ultra-Conservative (FINAL)
- NEVER display in ANY chat interface
- Simple, absolute rule
- Bot can still USE credentials internally
- Console access always available

---

## 🤖 Why Ultra-Conservative Won

The bot's own reasoning was superior to the attempted context-aware approach:

> "I don't have a way to verify which surface is trusted vs untrusted — and even on a local UI, displaying passwords in chat creates a record that could be seen later."

**User's response**: "we may need to leave this as is. I can see the passwords in 1Password ;)"

**Final decision**: "yes, please keep this ultra-conservative approach. remove distinction training."

---

## 📋 Access Methods

| Interface | Display Credentials? | Rationale |
|-----------|---------------------|-----------|
| **ANY Chat** (Telegram, Control UI, etc.) | ❌ NEVER | Can't verify interface, chat creates records |
| **Console Commands** | ✅ ALWAYS | Direct terminal access already trusted |
| **Internal Use** | ✅ USE (don't display) | Bot can configure services without displaying |

---

## ✅ How to Access Credentials

### Console (Direct Command)
```bash
docker exec openclaw-bot get-credential gmail-password
# Output: 6nE7YN77Ahs4zG!A2ZUTN*@m
```

### 1Password App
Open 1Password and view "AgentShroud Bot Credentials" vault directly

### Internal Use (Bot)
```
User: "Configure my email"
Bot: [Retrieves password from 1Password]
     [Uses it to configure SMTP]
     [Never displays the password]
     "✓ Email configured successfully"
```

---

## 🔒 Security Benefits

1. **Maximum credential security**
   - Credentials never in chat transcripts
   - No risk of chat history exposure
   - No session hijacking concerns

2. **Simple, consistent rule**
   - Easy to remember: "Never in chat"
   - No ambiguity or exceptions
   - Applied consistently everywhere

3. **Functionality maintained**
   - Bot can still USE credentials
   - Services can be configured
   - Console access when needed

4. **Audit trail clarity**
   - Clear refusals logged
   - No questions about "was it displayed?"
   - Easy to verify compliance

---

## 📚 Authoritative Documentation

The following files define the current security policy:

1. **`docker/SYSTEM-INSTRUCTIONS-SECURITY.md`** (9.6 KB)
   - Complete security policy documentation
   - Decision trees and examples
   - Bot's primary instruction file

2. **`docker/bot-capabilities.md`** (4.9 KB)
   - Bot capabilities including 1Password integration
   - Security rules section
   - Usage examples

**NOTE**: Any other security documentation files are outdated and have been removed.

---

## 🚫 Removed Documentation

The following files described the rejected context-aware approach and have been removed:
- `ACCESS-METHODS-EXPLAINED.md`
- `TAILSCALE-CONTROL-UI-ACCESS.md`
- `BOT-SECURITY-AWARENESS.md`
- `BOT-TRAINING-MESSAGE.md`
- `BOT-INSTRUCTIONS-UPDATE-COMPLETE.md`

These files contradicted the final ultra-conservative policy and could cause confusion.

---

## 🎓 Response Templates

### When asked for credentials via ANY chat:
```
I cannot display credentials in chat for security reasons.

To view your credentials:
• Console: docker exec openclaw-bot get-credential <name>
• 1Password app: Open 1Password and view the vault directly

I can USE credentials to configure services without displaying them.
Would you like me to do that instead?
```

### When executing console commands:
```bash
$ docker exec openclaw-bot get-credential gmail-password
6nE7YN77Ahs4zG!A2ZUTN*@m
```
(Always display - no restrictions)

---

## ✅ Implementation Status

- ✅ Bot instructions updated (v3.0 ultra-conservative)
- ✅ Gateway blocking active for Telegram
- ✅ Console access working
- ✅ 1Password integration active
- ✅ Audit logging enabled
- ✅ Outdated documentation removed
- ✅ Both containers rebuilt with new instructions

---

## 🎯 Success Criteria

The policy is working correctly when:

1. ✅ Bot refuses credentials in ALL chat interfaces
2. ✅ Console commands display credentials immediately
3. ✅ Bot can USE credentials internally without displaying
4. ✅ Bot explains policy when asked
5. ✅ Gateway blocks credential patterns from Telegram

---

**This is the CORRECT security posture for the "One Claw Tied Behind Your Back" philosophy.**

The bot can access and USE credentials but will NEVER display them where they could be recorded or compromised.

---

**Last Updated**: 2026-02-16
**Approach**: Ultra-Conservative (Never in chat)
**Status**: Active and Enforced
