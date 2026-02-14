# Future Features & Roadmap

## Overview

This document tracks planned enhancements for "One Claw Tied Behind Your Back" - a secure, isolated OpenClaw deployment that serves as a separate digital environment for AI assistance.

## Core Philosophy

The agent operates in a **separate digital environment** from your primary online life. You manually forward selected information to it via:
- Email to dedicated Gmail account
- Apple Shortcuts (iOS/macOS)
- Telegram messages
- Web interface

**The agent has NO access to your primary**:
- Email accounts
- iCloud/Apple ID
- Calendar (unless you forward events)
- Files (unless you send them)
- Messages (unless you forward them)
- Financial accounts (except dedicated PayPal with limits)

---

## Priority 1: Information Forwarding Integrations

### 1.1 Apple Shortcuts Integration (iOS & macOS)

**Status**: Planned
**Complexity**: Medium
**ETA**: 4-6 weeks

**Description**: Create iOS and macOS Shortcuts that allow you to quickly forward information to your OneClaw agent without opening apps or typing commands.

**Use Cases**:
- Forward current web page to agent with note
- Send screenshot to agent for analysis
- Forward selected text from any app
- Send current location for context
- Forward photos with questions
- Send calendar events selectively
- Forward specific iMessages (not all messages)
- Quick voice memo transcription → agent

**Implementation**:

**iOS Shortcuts**:
```
Shortcut: "Send to OneClaw"
├─ Receive: Text, URLs, Images, Files
├─ Show prompt: "What do you want to ask about this?"
├─ Send email to: therealidallasj@gmail.com
    ├─ Subject: [From iPhone] {timestamp}
    ├─ Body: {user question}
    └─ Attachments: {selected content}
```

**macOS Shortcuts**:
```
Shortcut: "Forward to Agent"
├─ Get selected text/files from current app
├─ Show dialog: "Add context or question?"
├─ Compose email to therealidallasj@gmail.com
├─ Send with attachment/quote
└─ Notify: "Sent to OneClaw"
```

**Example Workflows**:

1. **"Summarize This Article"**:
   - Select text in Safari
   - Right-click → Services → "Send to OneClaw"
   - Shortcut emails article + "Please summarize" to agent
   - Agent processes via Gmail integration
   - Reply arrives in dedicated inbox

2. **"Explain This Code"**:
   - Select code in any editor
   - Keyboard shortcut (⌘⇧O)
   - Auto-sends to agent with "Explain this code"

3. **"Remember This"**:
   - Take screenshot
   - Share → "Send to OneClaw"
   - Add note: "Remember this for later"
   - Agent stores in memory

**Security Considerations**:
- ✅ User explicitly selects what to send (not automatic)
- ✅ Preview before sending
- ✅ Uses separate email account (therealidallasj@gmail.com)
- ✅ No background access to other apps
- ✅ Shortcuts permissions limited to selected content only

**Installation**:
- Provide `.shortcut` files users can import
- Step-by-step gallery in README with screenshots
- Test on iPhone, iPad, Mac

### 1.2 Gmail Integration with Smart Filtering

**Status**: Partially Implemented (can receive), Enhancement Planned
**Complexity**: Low
**ETA**: 2 weeks

**Current State**:
- Agent can receive emails at therealidallasj@gmail.com
- No automatic processing yet

**Enhancement**:
Create Gmail filters and labels for intelligent processing:

```
Gmail Filter Rules:
├─ From: your-primary-email@gmail.com
│   ├─ Subject contains: [ASK]
│   │   → Label: "OneClaw/Questions"
│   │   → Star
│   │   → Mark as unread
│   │
│   ├─ Subject contains: [REMEMBER]
│   │   → Label: "OneClaw/Memory"
│   │   → Archive
│   │
│   └─ Subject contains: [TASK]
│       → Label: "OneClaw/Tasks"
│       → Star
│
└─ From: trusted-sender@domain.com
    → Label: "OneClaw/Approved"
    → Process automatically
```

**Workflow**:
```
You:  Forward email with subject "[ASK] What's the deadline?"
      ↓
      Gmail receives at therealidallasj@gmail.com
      ↓
      Filter applies label + star
      ↓
      OneClaw's Gmail watcher detects new labeled email
      ↓
      Agent processes question
      ↓
      Reply sent to your primary email
```

**Privacy Enhancement**:
- You control which emails get forwarded
- Can use `+filters` in email address for categorization
- Example: `therealidallasj+ask@gmail.com`, `therealidallasj+remember@gmail.com`
- Filter by `+ask` → auto-process, `+review` → wait for approval

### 1.3 Telegram Quick Forwarding

**Status**: Partially Implemented
**Complexity**: Low
**ETA**: 1 week

**Current State**:
- Can create dedicated Telegram bot (@therealidallasj)
- Manual setup required

**Enhancement**:
Make Telegram the fastest way to interact with agent:

**Features**:
- `/ask [question]` - Quick question
- `/remember [note]` - Add to memory
- `/task [description]` - Create task
- `/summarize [URL]` - Summarize webpage
- Forward any message → agent analyzes
- Send photo → agent describes/analyzes
- Send voice message → transcribe + process

**Example**:
```
You: /ask What's the weather like in Tokyo?
Bot: Let me check... Currently 15°C (59°F) and partly cloudy in Tokyo.

You: [Forward message from friend]
Bot: This is an invitation to dinner on Friday at 7pm. Would you like me to:
     1. Add to calendar
     2. Draft a reply
     3. Just remember it
```

**Security**:
- Dedicated bot account (not connected to your primary Telegram)
- Can revoke bot token anytime
- Messages stored only in agent's memory (not Telegram servers permanently)

---

## Priority 2: Enhanced Security Features

### 2.1 Hardware Security Key Support

**Status**: Planned
**Complexity**: High
**ETA**: 8-10 weeks

**Description**: Require physical YubiKey or similar for gateway authentication.

**Implementation**:
- WebAuthn support in Control UI
- YubiKey required for:
  - Initial gateway pairing
  - Approving dangerous operations
  - Accessing audit logs
  - Changing security settings

**Use Case**:
Even if someone steals your gateway token, they can't connect without your physical YubiKey.

### 2.2 Automatic Security Updates

**Status**: Planned
**Complexity**: Medium
**ETA**: 6 weeks

**Description**: Auto-rebuild container weekly with latest security patches.

**Implementation**:
```bash
# Cron job (runs weekly)
0 3 * * 0 /Users/you/Development/oneclaw/auto-update.sh

# auto-update.sh
#!/bin/bash
# Pull latest OpenClaw from GitHub
# Rebuild Docker image
# Test in isolated environment
# If tests pass → swap containers
# If tests fail → alert user, keep old version
```

**Safety**:
- Blue-green deployment (keep old container until new one verified)
- Automatic rollback if new version fails health checks
- Email notification of updates

### 2.3 Intrusion Detection & Honeypots

**Status**: Planned
**Complexity**: High
**ETA**: 10-12 weeks

**Description**: Detect if container has been compromised.

**Features**:
- Honeypot files in container (fake SSH keys, API tokens)
- If accessed → immediate alert
- Monitor for suspicious syscalls
- Detect lateral movement attempts
- Auto-isolate if breach detected

**Example**:
```
Honeypot: /app/.ssh/id_rsa (fake SSH key)
If accessed:
1. Immediately email: "ALERT: Possible breach detected"
2. Stop container
3. Export logs
4. Lock gateway authentication
```

---

## Priority 3: User Experience Improvements

### 3.1 One-Click Setup Wizard (Web-Based)

**Status**: **COMPLETED** ✅
**File**: `setup-wizard.html`

Interactive web wizard that guides users through:
- ✅ Prerequisite checking (Docker, Python, Git)
- ✅ Creating Gmail account with Google Voice
- ✅ Setting up OpenAI/Anthropic API keys
- ✅ Optional Telegram bot creation
- ✅ Deploying with one button press
- ✅ Optional Tailscale configuration

### 3.2 Mobile App (iOS/Android)

**Status**: Concept Phase
**Complexity**: Very High
**ETA**: 6+ months

**Description**: Native mobile apps for iOS and Android that connect securely to your OneClaw instance.

**Features**:
- Push notifications for agent replies
- Voice input via Siri/Google Assistant
- Share sheet integration (share anything to OneClaw)
- Background sync
- Offline queue (messages sent when back online)
- Tailscale VPN integration for secure remote access

**Security**:
- mTLS certificate pinning
- Biometric authentication (Face ID / fingerprint)
- Zero data stored on device (all in container)

### 3.3 Desktop App (Electron)

**Status**: Concept Phase
**Complexity**: Medium
**ETA**: 3-4 months

**Description**: Standalone desktop app (Mac, Windows, Linux) instead of web browser.

**Advantages**:
- System tray icon (always accessible)
- Global keyboard shortcuts
- Native notifications
- Better performance than browser
- Auto-start on boot (optional)

---

## Priority 4: Advanced Agent Capabilities

### 4.1 Multi-Agent Orchestration

**Status**: Concept Phase
**Complexity**: High
**ETA**: 4-6 months

**Description**: Run multiple specialized agents in same container:
- Research Agent (web searching, summarization)
- Code Agent (programming help, debugging)
- Personal Agent (email, calendar, reminders)
- Finance Agent (budget tracking, bill reminders)

**Isolation**:
Each agent has:
- Separate workspace
- Different API key allowances
- Independent memory
- Specific skill permissions

**Workflow**:
```
You: "Research best practices for Docker security"
     ↓
Research Agent:
- Searches web
- Reads documentation
- Summarizes findings
     ↓
Returns: "Here are the top 10 Docker security best practices..."
```

### 4.2 Scheduled Actions & Automation

**Status**: Concept Phase
**Complexity**: Medium
**ETA**: 8 weeks

**Description**: Agent can perform scheduled tasks.

**Examples**:
- Daily digest: "Send me a summary of my emails at 9am"
- Weekly reports: "Every Monday, analyze my spending"
- Reminders: "Remind me to call mom on her birthday"
- Monitoring: "Alert me if Bitcoin drops below $50k"

**Implementation**:
- Cron-like scheduling inside container
- OpenClaw's built-in cron service
- User approves scheduled actions via web UI
- Can disable/modify anytime

### 4.3 Voice Interface

**Status**: Concept Phase
**Complexity**: High
**ETA**: 5-6 months

**Description**: Talk to your agent via voice.

**Features**:
- Voice input (speech-to-text)
- Voice output (text-to-speech)
- Wake word ("Hey OneClaw")
- Natural conversation flow
- Integration with ElevenLabs or OpenAI TTS

**Use Case**:
```
You: "Hey OneClaw, what's on my calendar today?"
Agent: [Speaks] "You have three items: Meeting at 10am, lunch with Sarah at noon..."
```

---

## Priority 5: Integration Expansions

### 5.1 Calendar Integration (Google Calendar)

**Status**: Planned
**Complexity**: Medium
**ETA**: 4 weeks

**Implementation**:
- OAuth to therealidallasj@gmail.com's Google Calendar
- Agent can:
  - Read events you forward
  - Create events on command
  - Send reminders
  - Check availability

**Workflow**:
```
You email: "Schedule coffee with John next Tuesday at 3pm"
Agent:
1. Checks calendar for conflicts
2. Creates event
3. Optionally sends invite to John
4. Confirms via email
```

**Privacy**:
- Uses separate Google Calendar (not your primary one)
- You manually forward important events from primary calendar
- Or: Agent only has read access, you approve writes

### 5.2 Task Management (Todoist, Things, TickTick)

**Status**: Planned
**Complexity**: Low
**ETA**: 3 weeks

**Integration**:
- Connect to Todoist/Things/TickTick
- Agent can:
  - Add tasks via voice/email/Telegram
  - Mark tasks complete
  - Send reminders
  - Prioritize tasks

**Example**:
```
You: "Remind me to buy milk tomorrow"
Agent: ✓ Added to Todoist: "Buy milk" due tomorrow 9am
```

### 5.3 Browser Automation (Puppeteer)

**Status**: Partially Available (OpenClaw has built-in browser control)
**Complexity**: High
**ETA**: 6-8 weeks for custom workflows

**Use Cases**:
- Fill out forms automatically
- Monitor websites for changes
- Screenshot and summarize pages
- Extract data from sites without APIs

**Example**:
```
You: "Check if concert tickets are available for next Friday"
Agent:
1. Opens Ticketmaster in headless browser
2. Searches for event
3. Checks availability
4. Screenshots results
5. Reports back: "Yes, tickets available from $89"
```

### 5.4 PayPal Integration with Approval Workflow

**Status**: Planned
**Complexity**: Medium
**ETA**: 5 weeks

**Description**: Agent can make PayPal payments but requires your approval for each transaction.

**Workflow**:
```
You: "Pay my electric bill"
Agent:
1. Finds bill in email (forwarded to therealidallasj@gmail.com)
2. Identifies amount and payee
3. Sends approval request via Telegram:
   "💰 Payment Request:
    To: City Electric Company
    Amount: $127.45
    Reason: Monthly bill for Jan 2026
    [Approve] [Deny]"
4. You tap [Approve]
5. Payment sent via PayPal API
6. Confirmation sent back
```

**Security**:
- $40/month spending limit enforced in PayPal account settings
- Requires approval for EVERY transaction
- 2FA on PayPal account
- Separate PayPal account (not your primary one)
- Can revoke OAuth access anytime

---

## Priority 6: Data & Memory Enhancements

### 6.1 Long-Term Memory with Vector Search

**Status**: Built-in to OpenClaw, needs configuration
**Complexity**: Medium
**ETA**: 2 weeks

**Description**: Agent remembers everything you tell it and can search memories semantically.

**Features**:
- Automatic embedding of conversations
- Vector similarity search
- Temporal awareness (remembers when things happened)
- Memory categories (personal, work, reference)

**Example**:
```
You (in January): "Remember that my sister's birthday is May 15th"
Agent: ✓ Stored in memory

You (in April): "When is my sister's birthday?"
Agent: "Your sister's birthday is May 15th. Would you like me to remind you a week before?"
```

### 6.2 Structured Knowledge Base

**Status**: Planned
**Complexity**: High
**ETA**: 8-10 weeks

**Description**: Personal wiki managed by agent.

**Structure**:
```
Knowledge Base/
├─ People/
│   ├─ Family/
│   │   └─ Sister.md (birthday, preferences, past conversations)
│   └─ Friends/
├─ Projects/
│   ├─ OneClaw Setup/ (technical details, decisions made)
│   └─ Home Renovation/
├─ Reference/
│   ├─ Recipes/
│   ├─ Travel Info/
│   └─ Product Recommendations/
└─ Work/
    ├─ Meeting Notes/
    └─ Project Plans/
```

**Interaction**:
```
You: "Add to my knowledge base: John likes spicy food"
Agent: ✓ Added under People/Friends/John.md

You: "What did I learn about Docker security?"
Agent: "On Feb 14, 2026, you researched Docker security and noted:
        • Use non-root users
        • Drop capabilities
        • Isolate networks
        [View full article]"
```

### 6.3 Conversation Exports & Analytics

**Status**: Planned
**Complexity**: Low
**ETA**: 2 weeks

**Features**:
- Export all conversations as JSON, Markdown, or PDF
- Search full conversation history
- Analytics dashboard:
  - Most asked questions
  - Topics discussed
  - API usage stats
  - Response time trends

---

## Priority 7: Collaboration & Sharing

### 7.1 Multi-User Support

**Status**: Concept Phase
**Complexity**: Very High
**ETA**: 6+ months

**Description**: Family/team can share one OneClaw instance with role-based permissions.

**Use Case**: Family assistant shared by household members.

**Permissions**:
```
User: Dad (admin)
- Can access all features
- Can approve payments
- Can modify settings

User: Mom (admin)
- Same as Dad

User: Kids (limited)
- Can ask questions
- Can set reminders
- CANNOT make payments or access email
```

### 7.2 Agent Marketplace

**Status**: Future Vision
**Complexity**: Very High
**ETA**: 12+ months

**Description**: Share your custom agent configurations, shortcuts, and workflows with the community.

**Examples**:
- "Travel Planning Agent" (pre-configured with travel sites, APIs)
- "Fitness Tracker Agent" (integrates with health apps)
- "Home Automation Agent" (controls smart devices)

**Distribution**:
- GitHub repository of configs
- One-click import
- Community ratings and reviews
- Security audits for shared configs

---

## Implementation Priority Matrix

| Feature | Impact | Complexity | Priority | ETA |
|---------|--------|-----------|----------|-----|
| Apple Shortcuts (iOS/macOS) | High | Medium | **P0** | 4-6 weeks |
| Gmail Smart Filtering | High | Low | **P0** | 2 weeks |
| Telegram Quick Forwarding | High | Low | **P0** | 1 week |
| Calendar Integration | Medium | Medium | P1 | 4 weeks |
| Task Management | Medium | Low | P1 | 3 weeks |
| Hardware Security Keys | Medium | High | P2 | 8-10 weeks |
| Voice Interface | Medium | High | P2 | 5-6 months |
| PayPal with Approval | Low | Medium | P2 | 5 weeks |
| Desktop App | Medium | Medium | P3 | 3-4 months |
| Mobile App | High | Very High | P3 | 6+ months |
| Multi-Agent Orchestration | Low | High | P4 | 4-6 months |

---

## How to Contribute

Want to help build these features? See [CONTRIBUTING.md](./CONTRIBUTING.md) for:
- Development setup
- Code style guide
- Pull request process
- Feature proposal template

**High-impact contributions welcome**:
- 🍎 macOS/iOS developers (Shortcuts integration)
- 🔒 Security engineers (hardening, audits)
- 🎨 UI/UX designers (Control UI improvements)
- 📱 Mobile developers (iOS/Android apps)
- 📝 Technical writers (documentation, tutorials)

---

## Feedback & Feature Requests

Have ideas? Open an issue on GitHub:
- **Feature Request**: Describe the use case and expected behavior
- **Bug Report**: Include logs, steps to reproduce
- **Security Concern**: Email privately (see SECURITY.md)

**Let's build the most secure, private AI assistant together!** 🦞

---

**Last Updated**: February 14, 2026
**Version**: 1.0
