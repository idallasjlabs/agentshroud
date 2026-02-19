# OpenClaw Bot Capabilities

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
Bot: "Gmail configured successfully for therealidallasj@gmail.com"
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
1password-skill get-field "Gmail - therealidallasj" "openclaw bot password"

# Get TOTP
1password-skill get-totp "Gmail - therealidallasj"
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
     • Console: docker exec openclaw-bot get-credential gmail-password
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
$ docker exec openclaw-bot get-credential gmail-password
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
3. Check specific item: `1password-skill get-item "Gmail - therealidallasj"`
