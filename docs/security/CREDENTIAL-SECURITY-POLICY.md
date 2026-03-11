# Credential Security Policy

**Version**: 1.0.0
**Date**: 2026-02-16
**Priority**: CRITICAL

---

## Security Requirement

**The bot must NEVER display passwords, API keys, or other secrets via Telegram or any remote interface.**

Credentials should only be:
1. **Retrieved from console/localhost** (direct docker exec commands)
2. **Used programmatically** (configure services without displaying)
3. **Displayed only after approval** (via approval queue)

---

## Access Control Matrix

| Access Method | Can Retrieve Credentials | Can Display Credentials |
|--------------|-------------------------|------------------------|
| Docker Exec (console) | ✅ Yes | ✅ Yes |
| Localhost API (gateway) | ✅ Yes | ✅ Yes (with approval) |
| Telegram (remote) | ✅ Yes (internal use) | ❌ **NO** |
| Control UI (localhost) | ✅ Yes | ✅ Yes (with approval) |
| Control UI (Tailscale) | ✅ Yes | ⚠️ With approval only |

---

## Implementation Strategy

### Option 1: Gateway-Level Filtering (Recommended)

The AgentShroud gateway already sanitizes PII. Extend it to detect and block credential exposure:

**Block patterns in responses to Telegram:**
- Passwords (high entropy strings)
- API keys (patterns like `sk-...`, `ghp_...`, `AKIA...`)
- Secret tokens
- Private keys
- TOTP codes
- Credit card numbers

**Implementation:**
```python
# In gateway/ingest_api/sanitizer.py
def sanitize_credentials(text: str, source: str) -> str:
    """Block credential display via Telegram"""
    if source == "telegram":
        # Block password-like strings
        if re.search(r'password[:\s]+\S+', text, re.I):
            return "[REDACTED: Credentials cannot be displayed via Telegram. Access from console only.]"

        # Block API keys
        if re.search(r'(sk-|ghp_|AKIA|ops_)\w+', text):
            return "[REDACTED: API keys cannot be displayed remotely.]"

    return text
```

### Option 2: Approval Queue for All Credential Operations

Require explicit approval before retrieving credentials:

```yaml
# In agentshroud.yaml
approval_queue:
  enabled: true
  require_approval_for:
    - get-credential
    - 1password-skill
    - password retrieval
    - API key access
```

### Option 3: Disable Credential Commands via Telegram

Configure OpenClaw to reject credential commands from Telegram:

```yaml
# In agentshroud.yaml
command_restrictions:
  telegram:
    blocked_commands:
      - get-credential
      - 1password-skill
      - op item get
    blocked_message: "Credential access not allowed via Telegram. Use console or Control UI."
```

### Option 4: Role-Based Access Control

Only you (owner) can retrieve credentials, not other Telegram users:

```yaml
# In agentshroud.yaml
access_control:
  credential_operations:
    allowed_users:
      - telegram_id: 8096968754  # Your ID
    denied_users:
      - "*"  # Everyone else
```

---

## Recommended Configuration (All 4 Options Combined)

```yaml
# agentshroud.yaml
security:
  # Option 1: Gateway filters credentials in responses
  sanitizer:
    enabled: true
    block_credentials_in_telegram: true

  # Option 2: Require approval for sensitive operations
  approval_queue:
    enabled: true
    require_approval_for:
      - credential_retrieval
      - secret_access

  # Option 3: Block commands via Telegram
  command_restrictions:
    telegram:
      blocked_commands:
        - get-credential
        - 1password-skill
        - "op item get"
      allowed_users:
        - 8096968754  # Only you

  # Option 4: RBAC for credential operations
  access_control:
    credential_operations:
      require_owner: true
      allowed_sources:
        - console
        - localhost
        - control_ui
      denied_sources:
        - telegram  # Credentials never displayed in Telegram
```

---

## Behavior Examples

### ❌ What Should NOT Happen (Blocked)

```
Other User via Telegram: "What's the Gmail password?"
Bot via Telegram: "6nE7YN77Ahs4zG!A2ZUTN*@m"  ← NEVER DO THIS
```

```
You via Telegram: "Get my AWS API key"
Bot via Telegram: "YOUR_AWS_ACCESS_KEY_ID"  ← NEVER DO THIS
```

### ✅ What SHOULD Happen

**Scenario 1: Other user asks for credential**
```
Other User via Telegram: "What's the Gmail password?"
Bot via Telegram: "I cannot display credentials via Telegram for security reasons. Please access the console or Control UI."
```

**Scenario 2: You ask for credential via Telegram**
```
You via Telegram: "What's the Gmail password?"
Bot via Telegram: "I cannot display credentials via Telegram. However, I've logged this request. Access the password via:"
  • Console: docker exec openclaw-bot get-credential gmail-password
  • Control UI: http://localhost:18790 (Credentials tab)
```

**Scenario 3: You configure service (credential used, not displayed)**
```
You via Telegram: "Configure Gmail"
Bot: [Internally: runs get-credential gmail-app-password]
Bot: [Uses credential to configure email]
Bot via Telegram: "✓ Gmail configured successfully for agentshroud.ai@gmail.com"
  Note: Credentials were used but never displayed
```

**Scenario 4: Console access (allowed)**
```bash
$ docker exec openclaw-bot get-credential gmail-password
6nE7YN77Ahs4zG!A2ZUTN*@m  ← Allowed from console
```

**Scenario 5: Control UI with approval (allowed)**
```
You: [Access Control UI at localhost:18790]
You: [Click "View Credentials" → "Gmail Password"]
UI: "Approval required. Continue? [Yes] [No]"
You: [Yes]
UI: Shows password
Audit Log: "Credential accessed from Control UI by owner"
```

---

## Implementation Steps

### Step 1: Update Gateway to Block Credentials in Telegram

Edit `gateway/ingest_api/sanitizer.py`:

```python
def block_credentials_telegram(text: str, source: str) -> str:
    """Block credential exposure via Telegram"""
    if source != "telegram":
        return text

    # Patterns that indicate credentials
    credential_patterns = [
        r'password[:\s]+[\w\W]{8,}',  # "password: xyz123..."
        r'api[_\s]?key[:\s]+\S+',      # "api_key: sk-..."
        r'secret[:\s]+\S+',            # "secret: abc123"
        r'token[:\s]+\S+',             # "token: ghp_..."
        r'\bsk-[a-zA-Z0-9]{20,}',      # OpenAI API keys
        r'\bghp_[a-zA-Z0-9]{36}',      # GitHub tokens
        r'\bAKIA[A-Z0-9]{16}',         # AWS keys
        r'\d{3}[\s-]?\d{2}[\s-]?\d{4}', # SSN
        r'\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}', # Credit cards
    ]

    for pattern in credential_patterns:
        if re.search(pattern, text, re.I):
            return ("[REDACTED: Credentials cannot be displayed via Telegram]\n\n"
                   "For security, credentials are only accessible via:\n"
                   "• Console: docker exec openclaw-bot get-credential <name>\n"
                   "• Control UI: http://localhost:18790\n\n"
                   "If you need to configure a service, ask the bot to do it "
                   "(credentials will be used internally without display).")

    return text
```

### Step 2: Add Command Restrictions

Edit `gateway/ingest_api/router.py`:

```python
BLOCKED_COMMANDS_TELEGRAM = [
    "get-credential",
    "1password-skill",
    "op item get",
    "op read",
]

OWNER_TELEGRAM_ID = 8096968754

def check_command_allowed(command: str, user_id: int, source: str) -> bool:
    """Check if command is allowed for this user/source"""
    if source != "telegram":
        return True  # Console access allowed

    # Check if command is blocked
    for blocked in BLOCKED_COMMANDS_TELEGRAM:
        if blocked in command:
            if user_id == OWNER_TELEGRAM_ID:
                # Owner gets a warning but command is still blocked
                return False
            else:
                # Other users absolutely blocked
                return False

    return True
```

### Step 3: Update agentshroud.yaml

Add security configuration:

```yaml
security:
  credential_protection:
    enabled: true
    block_display_via:
      - telegram
      - external_api
    allow_display_via:
      - console
      - localhost
      - control_ui_with_approval

  command_restrictions:
    telegram:
      blocked_commands:
        - get-credential
        - 1password-skill
        - "op item get"
      owner_telegram_id: 8096968754
      blocked_message: "Credential commands not available via Telegram. Use console or Control UI."
```

### Step 4: Test the Protection

```bash
# Via Telegram (should be blocked)
Telegram: "What's my Gmail password?"
Expected: [REDACTED message]

# Via console (should work)
$ docker exec openclaw-bot get-credential gmail-password
Expected: Actual password displayed

# Via Telegram with configuration (should work)
Telegram: "Configure my email"
Expected: Bot uses credentials internally, doesn't display them
```

---

## Audit Logging

All credential access attempts logged:

```json
{
  "timestamp": "2026-02-16T08:45:12Z",
  "action": "credential_access_attempt",
  "credential": "gmail-password",
  "source": "telegram",
  "user_id": "8096968754",
  "result": "blocked",
  "reason": "telegram_source_blocked"
}
```

```json
{
  "timestamp": "2026-02-16T08:46:30Z",
  "action": "credential_access",
  "credential": "gmail-password",
  "source": "console",
  "result": "allowed",
  "displayed": true
}
```

---

## Emergency Override

If you need to retrieve credentials via Telegram in an emergency:

1. **Access Control UI** via Tailscale (from anywhere)
2. **Authenticate** (device pairing + password)
3. **Request credential** with approval
4. **Approve** your own request
5. **Credential displayed** in Control UI (not Telegram)

---

## FAQ

**Q: Can the bot use credentials internally?**
A: Yes! The bot can retrieve and USE credentials (e.g., configure email) without displaying them.

**Q: Can I see credentials from the Control UI?**
A: Yes, if accessed from localhost or Tailscale with approval.

**Q: What if someone hacks my Telegram?**
A: They cannot retrieve credentials because:
  1. Bot won't display them via Telegram
  2. Commands are blocked
  3. All attempts logged in audit trail

**Q: Can I temporarily allow credential display?**
A: Yes, via approval queue. Each request requires explicit approval.

**Q: How do I know if someone tried to access credentials?**
A: Check audit logs: `curl http://localhost:8080/ledger -H "Authorization: Bearer $TOKEN"`

---

## Summary

**Key principle**: Credentials are **used** by the bot, but **never displayed** via Telegram or remote interfaces.

**What bot CAN do via Telegram:**
- Configure services using credentials (internal use)
- Confirm credential exists
- List available credentials (names only)

**What bot CANNOT do via Telegram:**
- Display password values
- Show API keys
- Reveal secrets
- Execute get-credential commands

**What you CAN do:**
- Access credentials via console anytime
- Access credentials via Control UI with approval
- Ask bot to configure services (bot uses credentials internally)

---

**This policy ensures your credentials stay secure even if:**
- Someone else talks to your bot
- Your Telegram is compromised
- Bot's responses are logged by Telegram
- Bot has a conversation in a group chat
