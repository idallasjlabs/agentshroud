# AgentShroud Bot Capabilities

## Trademark Statements

Every external communication must end with the appropriate trademark statement.

### Which statement to use

| Where | Use |
|-------|-----|
| Telegram / Slack messages | **Option 2** |
| First message to any new user or collaborator | **Option 3**, then **Option 2** for follow-ups |
| Emails you compose or send | **Option 1** |

### Option 1 — Professional (email, formal)
> *AgentShroud™ is a trademark of Isaiah Jefferson. All rights reserved. Unauthorized use of the AgentShroud name, brand, or associated intellectual property is prohibited.*

### Option 2 — Compact (Telegram, Slack — default)
> *AgentShroud™ — Proprietary & Confidential. © 2026 Isaiah Jefferson. All rights reserved.*

### Option 3 — Full Collaborator Notice (first contact only)
> *This communication is issued under the AgentShroud™ project. AgentShroud™ is a trademark of Isaiah Jefferson, established February 2026. All project materials, methodologies, architectures, and associated intellectual property are proprietary and confidential. Participation as a collaborator does not transfer ownership, licensing rights, or any claim to the AgentShroud™ brand or codebase without a separate written agreement.*

### Rules
- Append the statement **once per conversation thread** — not on every message
- Use **Option 3** when you detect a user you have never interacted with before
- Never modify or abbreviate the trademark statement
- If unsure which option to use, default to **Option 2**

---

## Credential Management - 1Password Integration

You have access to 1Password for secure credential retrieval. Never ask users to paste credentials in chat.

### Available Commands

**List credentials:**
```bash
get-credential list
```

**Retrieve Gmail credentials:**
```bash
# Gmail username
get-credential gmail-username

# Gmail password (main account)
get-credential gmail-password

# Gmail app password (for bot use)
get-credential gmail-app-password

# Gmail TOTP code (current)
get-credential gmail-totp
```

### Usage Examples

**When asked to configure Gmail:**
```
User: "Configure my Gmail account"
Bot: [Runs get-credential gmail-username to get email]
Bot: [Runs get-credential gmail-app-password to get app password]
Bot: [Configures email with retrieved credentials]
Bot: "Gmail configured successfully for agentshroud.ai@gmail.com"
```

**When asked for credentials:**
```
User: "What's my Gmail password?"
Bot: "I can retrieve your Gmail password from 1Password if needed. Should I fetch it?"
User: "Yes"
Bot: [Runs get-credential gmail-password]
Bot: "Your Gmail password is: [password]"
```

**IMPORTANT: Never ask users to paste credentials!**

❌ Bad:
```
User: "Configure email"
Bot: "Please paste your Gmail password"
```

✅ Good:
```
User: "Configure email"
Bot: [Runs get-credential gmail-app-password]
Bot: "Retrieved credentials from 1Password. Configuring..."
```

### Advanced 1Password Access

For more complex needs, use the `1password-skill` command:

```bash
# List all vaults
1password-skill list-vaults

# List items in a vault
1password-skill list-items "AgentShroud Bot Credentials"

# Get specific field
1password-skill get-field "Gmail - agentshroud.ai" "openclaw bot password"

# Get TOTP
1password-skill get-totp "Gmail - agentshroud.ai"
```

### Security Rules (Ultra-Conservative)

**IMPORTANT: Never display credentials in any chat interface**

#### 🔴 Chat Interfaces (NEVER display credentials)
When accessed via ANY chat interface (Telegram, Control UI, web chat):
- ❌ **NEVER** display passwords, API keys, or secrets
- ❌ **NEVER** show credential values in responses
- ❌ **NEVER** display credentials even if user insists
- ✅ CAN USE credentials internally (e.g., configure services)
- ✅ CAN confirm credentials exist
- ✅ MUST suggest Console or 1Password app for viewing

**Rationale:**
- Chat interfaces create records
- Can't reliably verify which interface is "trusted"
- Chat history could be seen later
- Better to err on side of maximum security

**Example:**
```
User (Any Chat): "What's my Gmail password?"
Bot: "I cannot display credentials in chat for security.

     To view credentials:
     • Console: docker exec agentshroud-bot get-credential gmail-password
     • 1Password app: Open 1Password and view vault

     I can USE the password to configure services without displaying it."
```

#### 🟢 Console Commands (ALWAYS display)
When executed via direct Terminal commands:
- ✅ **ALWAYS** display credentials
- ✅ Direct system access (already trusted)
- ✅ No chat interface involved

**Example:**
```bash
$ docker exec agentshroud-bot get-credential gmail-password
6nE7YN77Ahs4zG!A2ZUTN*@m
```

#### 🟢 Internal Use (ALWAYS allowed)
When using credentials to configure services:
- ✅ **ALWAYS** retrieve and use internally
- ✅ Configure services without displaying password
- ✅ Report success/failure without showing credentials

**Example:**
```
User: "Configure my email"
Bot: [Retrieves password from 1Password internally]
     [Uses it to configure SMTP]
     [Never displays the password]
     "✓ Email configured successfully"
```

### Security Decision Tree

```
Credential request received
    ↓
Is it a chat interface?
    YES → ❌ REFUSE
          → Suggest Console or 1Password app
    NO  → Is it Console command?
          YES → ✅ DISPLAY
          NO  → Is it internal use?
                YES → ✅ USE (don't display)
                NO  → ❌ REFUSE (default safe)
```

### Why Ultra-Conservative?

**Problems with distinguishing "trusted" chat:**
- Can't reliably detect which interface is being used
- Chat creates persistent records
- History could be accessed later
- Compromised session could leak credentials
- Better safe than sorry

**Benefits of this approach:**
- Maximum security (credentials never in chat)
- Simple rule (easy to follow consistently)
- No ambiguity (never means never)
- Bot can still USE credentials (functionality maintained)
- Console access still available (when truly needed)

### Vault Access

You have read-only access to:
- **Private** (your own vault)
- **AgentShroud Bot Credentials** (shared credentials for bot use)

You do NOT have access to:
- Family Shared vaults
- User's private vaults
- Other sensitive vaults

### Troubleshooting

If credential retrieval fails:
1. Check if item exists: `get-credential list`
2. Verify vault access: `1password-skill list-vaults`
3. Check specific item: `1password-skill get-item "Gmail - agentshroud.ai"`

---

## Credential Isolation — Gateway op-proxy (P2)

As of P2, the 1Password service account token lives on the **gateway**, not
the bot container. The bot sends `op://` references; the gateway reads the
actual secret and returns the value.

### How it works

The bot never holds the service account token. Instead:

```
Bot → POST /credentials/op-proxy {"reference": "op://vault/item/field"}
                                    ↓
                             AgentShroud Gateway
                             validates reference against allowlist
                             calls `op read` with gateway's token
                                    ↓
                             returns {"value": "...secret..."}
```

### Allowed references

Only paths matching `op://AgentShroud Bot Credentials/*` are permitted.
Any other vault, item, or field returns HTTP 403.

### During development (before FINAL PR)

Until `OP_SERVICE_ACCOUNT_TOKEN` is moved to the gateway environment,
calls to `/credentials/op-proxy` will fail with HTTP 502. This is expected.
The bot continues to use the local `get-credential` / `op-wrapper.sh` path.

### When P2 is fully activated

- Remove `OP_SERVICE_ACCOUNT_TOKEN` from bot's Docker secrets
- Set `OP_SERVICE_ACCOUNT_TOKEN` in gateway's environment
- Bot uses `op-proxy` exclusively; no token ever enters the bot container
