# One Shroud Over Every Wire: A Story About Trust, Isolation, and AI Assistants

## The Problem

In January 2026, security researchers discovered something terrifying: **42,900 AI assistants were exposed to the public internet**, waiting to be compromised. These weren't just chatbots—they were OpenClaw instances with full terminal access, complete email histories, API keys, and months of private conversations.

Within weeks:
- A critical vulnerability (CVE-2026-25253) enabled **one-click remote code execution** via malicious links
- Security audits found **512 vulnerabilities** in the platform, 8 classified as critical
- ClawHub, the official plugin repository, was **20% malicious** — 900 malicious skills deploying infostealers that harvested crypto exchange API keys, SSH credentials, and wallet private keys
- Researchers gained access to exposed instances and found **Anthropic API keys, Telegram bot tokens, and complete chat histories** sitting in the open

Palo Alto Networks called it **"the biggest insider threat of 2026."**

I wanted to use OpenClaw. The technology is incredible—an AI assistant that can manage your email, browse the web, execute terminal commands, remember conversations, and automate your digital life. But handing over my Gmail OAuth token, my iCloud credentials, my Telegram account? That felt like giving a stranger the keys to my entire digital existence.

What if the container got compromised? What if a malicious skill slipped through? What if a zero-day exploit emerged?

**I needed OpenClaw. But I didn't trust it.**

So I built a version with one shroud over every wire.

---

## The Philosophy: Separate Digital Environments

Here's the key insight: **Your AI assistant doesn't need access to your real life. It needs access to a staging area where you forward selected information.**

Think of it like this:

**Traditional OpenClaw Setup** (Dangerous):
```
Primary Gmail Account ──► OpenClaw Agent
• work@company.com          ├─ Full OAuth access
• personal@gmail.com        ├─ Reads ALL emails
                            ├─ Sends from your accounts
                            └─ If compromised = identity theft

Primary iCloud ─────────► OpenClaw Agent
• iMessages (all)           ├─ All conversations visible
• Notes, Photos             ├─ Private data exposed
• Contacts                  └─ If leaked = everyone's info stolen

Primary Telegram ───────► OpenClaw Agent
• @yourusername             ├─ Bot token access
                            └─ All chats compromised if breached
```

**One Shroud Over Every Wire** (Secure):
```
Your Real Digital Life          Information Valve          Agent's Isolated World
==================              ================           ======================

Primary Gmail                                              therealidallasj@gmail.com
work@company.com          ─────────────►                  (separate service account)
personal@gmail.com        You manually forward
                          selected emails only

Primary iCloud                                             therealidallasj@icloud.com
iMessages (main)          ─────────────►                  (separate Apple ID)
Photos, Notes             Via Apple Shortcuts             No access to your real data
                          (you choose what)

Primary Telegram                                           @therealidallasj
@realyou                  ─────────────►                  (dedicated bot)
                          Optional forwarding

Primary Bank                                               PayPal with $40 limit
Chase, Wells Fargo        ─────────────►                  You approve each transaction
```

**The agent only sees what you explicitly send to it.** If it gets compromised? You lose:
- A burner email account (revoke in 2 minutes)
- $40 in PayPal (spending limit enforced)
- The messages you forwarded (nothing you didn't choose to share)

You DON'T lose:
- ❌ Your primary email accounts
- ❌ Your iCloud data
- ❌ Your bank accounts
- ❌ Your real identity

---

## The Architecture: Internet-Only Isolation

Most OpenClaw setups have full network access: local network (your NAS, printers, smart home), VPN access (corporate resources), and internet. If compromised, an attacker can pivot to other devices.

Our setup? **Internet-only, no exceptions.**

```
┌─────────────────────────────────┐
│   Internet (ALLOWED)            │
│   • OpenAI API                  │
│   • Public websites             │
│   • Telegram                    │
└───────────────┬─────────────────┘
                │ ✅ Allowed
                │
┌───────────────┼─────────────────┐
│  Docker       │                 │
│  Container    │                 │
│               │                 │
│   AgentShroud     │                 │
│   Gateway     │                 │
│               │                 │
└───────────────┼─────────────────┘
                │ ❌ BLOCKED
                ↓
    ┌───────────────────────┐
    │  Local Network        │
    │  • 192.168.x.x        │
    │  • NAS devices        │
    │  • Printers           │
    │  • Smart home         │
    │  • VPN networks       │
    └───────────────────────┘
```

**How it works**:
- Custom Docker bridge network
- Gateway bound to `localhost:18789` only (not accessible from outside)
- All Linux capabilities dropped except essential ones
- Runs as non-root user (UID 1000)
- Resource limits: 2 CPUs, 4GB RAM max
- Read-only filesystem where possible
- No access to host files, Docker socket, or SSH keys

Even if an attacker achieves remote code execution inside the container:
- ✅ They can hit public internet (that's it)
- ❌ They CANNOT reach your local network
- ❌ They CANNOT access your Mac's filesystem
- ❌ They CANNOT access other Docker containers
- ❌ They CANNOT pivot to your VPN or corporate network

**Blast radius**: Limited to a service account you can revoke in 10 minutes.

---

## How You Actually Use It

### Daily Workflow

**Morning**:
```
You check your primary Gmail, see an important email.
Forward to: therealidallasj@gmail.com with subject "[ASK] Summarize this"
AgentShroud processes it, replies to your primary email with summary.
```

**Throughout the day**:
```
iPhone: Select article in Safari → Share → "Send to AgentShroud" Shortcut
        Auto-emails to agent with "TLDR this"

Mac: Select code in any editor → Keyboard shortcut ⌘⇧O
     Auto-sends to agent with "Explain this code"

Telegram: /remember "Bob prefers meetings after 2pm"
          Agent stores in long-term memory
```

**Evening**:
```
Email to agent: "What did I need to remember today?"
Agent: "You have 3 reminders:
       1. Call mom (her birthday next week)
       2. Bob prefers meetings after 2pm
       3. Amazon delivery arrives tomorrow"
```

### What You CAN'T Do (By Design)

❌ "Read my Gmail and find all receipts" — Agent doesn't have access to your primary Gmail
✅ "Here are my receipts [forwarded], find the Amazon ones" — You send data to agent

❌ "Check my bank balance" — No access to your bank
✅ "I just spent $500 on groceries, update my budget" — You tell agent what happened

❌ "Read all my iMessages" — No access to your Messages app
✅ [Forward specific message via Shortcut] "What does this mean?" — You choose what to share

**This is a feature, not a bug.** The inconvenience is the security.

---

## The Setup: From Zero to Running in 15 Minutes

1. Open `setup-wizard.html` in your browser
2. Follow the interactive checklist:
   - ✓ Install Docker (if not present)
   - ✓ Create new Gmail account using Google Voice number
   - ✓ Get OpenAI or Anthropic API key
   - ✓ (Optional) Create Telegram bot via @BotFather
3. Click "Deploy AgentShroud"
4. Done.

The wizard:
- Checks prerequisites (Docker, Python, Git)
- Generates secure gateway token (32-byte random hex)
- Builds Docker container from source (transparent, auditable)
- Configures network isolation
- Starts web interface on http://localhost:18791
- Optionally sets up Tailscale for secure remote access

**No cloud deployment. No third-party services. Everything local.**

---

## Real-World Security Comparison

| Aspect | Typical OpenClaw Setup | One Shroud Over Wire |
|--------|----------------------|---------------------|
| **Network Exposure** | Often 0.0.0.0:18789 (public) | 127.0.0.1:18789 (localhost-only) |
| **Internet Scan Visible?** | Yes (21,639 found by Censys) | No (not routable) |
| **Email Access** | OAuth to your primary Gmail | Separate burner account |
| **LAN Access** | Yes (can hit 192.168.x.x) | Blocked (internet-only) |
| **VPN Access** | Yes | Blocked |
| **If Compromised, Attacker Gets** | Your entire digital identity | A revocable service account |
| **Recovery Time** | Days (forensics, credential rotation) | 10 minutes (revoke key, rebuild) |
| **Exposed Credentials** | 40,000+ instances leaked real tokens | Dedicated keys (not your primary) |
| **Malicious Skills** | 900 found on ClawHub (20%) | Manual approval required |
| **Cost of Breach** | Identity theft, data loss | $40 PayPal + some messages |

---

## The Vision: What's Next?

This is **version 1.0**—a secure foundation. Here's where we're going:

### Near-Term (1-3 months)
- **Apple Shortcuts Integration**: One-tap forwarding from iPhone/Mac
  - "Send to AgentShroud" Share Sheet
  - Keyboard shortcuts for selected text
  - Voice command shortcuts

- **Smart Gmail Filters**: Auto-categorize forwarded emails
  - `[ASK]` → Immediate processing
  - `[REMEMBER]` → Add to memory
  - `[TASK]` → Create action item

- **Enhanced Telegram**: Quick commands
  - `/ask [question]`
  - `/remember [note]`
  - `/task [description]`

### Mid-Term (3-6 months)
- **Hardware Security Keys**: YubiKey required for dangerous operations
- **Calendar Integration**: Google Calendar for agent's account (not yours)
- **Task Management**: Todoist/Things/TickTick integration
- **PayPal Approval Workflow**: Agent requests payment, you approve via push notification

### Long-Term (6-12 months)
- **Mobile Apps** (iOS/Android): Native apps with push notifications
- **Desktop App** (Electron): System tray, global hotkeys, auto-start
- **Multi-Agent Orchestration**: Specialized agents (Research, Code, Personal, Finance)
- **Voice Interface**: "Hey AgentShroud, what's on my calendar?"

---

## Call for Collaborators

This is open source. I need help from:

**🍎 macOS/iOS Developers**:
- Build Apple Shortcuts gallery
- Test on different macOS/iOS versions
- Create Share Sheet extensions

**🔒 Security Engineers**:
- Audit Docker configuration
- Pen-test the isolation
- Implement SELinux/AppArmor profiles
- Add intrusion detection

**🎨 UI/UX Designers**:
- Improve Control UI
- Design mobile app interfaces
- Create onboarding flow

**📱 Mobile Developers**:
- Build iOS app
- Build Android app
- Implement push notifications via Tailscale

**📝 Technical Writers**:
- Create video tutorials
- Write troubleshooting guides
- Translate documentation

**🧪 Testers**:
- Test on different systems (M1/M2/Intel Macs, Windows via WSL2, Linux)
- Try to break the isolation
- Report bugs and edge cases

---

## The Philosophy: Trust Through Isolation

I don't trust OpenClaw. Not because it's malicious—it's open source, built by talented developers, and incredibly powerful. I don't trust it because:

1. **Software has bugs.** 512 vulnerabilities found in one audit. More will be discovered.
2. **Supply chains are compromised.** 20% of ClawHub was malicious. That's terrifying.
3. **Mistakes happen.** Even with good intentions, one wrong OAuth approval gives full account access.

But I **do trust isolation**.

I trust that:
- A container bound to localhost cannot be reached from the internet
- A custom Docker bridge with no LAN routes cannot hit 192.168.x.x
- A non-root user with dropped capabilities has limited damage potential
- A separate service account, even if stolen, doesn't expose my primary identity

**The only way to be safe is to assume you'll be breached, and limit what the attacker gets.**

That's what "One Shroud Over Every Wire" means. The agent is powerful, useful, and productive—but it can only touch what you explicitly hand to it. It cannot reach into your digital life and grab things on its own.

One shroud covers every wire. The agent is free to help you.

---

## Get Involved

**Repository**: https://github.com/idallasj/agentshroud

**Quick Start**:
```bash
git clone https://github.com/idallasj/agentshroud.git
cd agentshroud
open setup-wizard.html
```

**Contribute**:
1. Read `CONTRIBUTING.md`
2. Check `FUTURE-FEATURES.md` for ideas
3. Open an issue or pull request

**Security Concerns?**
Read `SECURITY-ANALYSIS.md` for our threat model and comparison with known OpenClaw vulnerabilities.

**Questions?**
Open a GitHub Discussion or issue.

---

## FAQ

**Q: Why not just use Claude Pro or ChatGPT Plus directly?**

**A**: Those are great for chat, but they can't:
- Execute terminal commands on your behalf
- Manage your email
- Browse the web with your cookies/sessions
- Remember long-term context across months
- Integrate with Telegram, iMessage, etc.
- Run on your local network (privacy)

OpenClaw is an **agent**, not just a chatbot. It acts autonomously with real-world integrations. That power requires isolation.

---

**Q: Is this more secure than just not using OpenClaw at all?**

**A**: Obviously not using any AI assistant is more secure. But if you want the productivity benefits of an AI agent without the identity theft risk, this is how.

---

**Q: Can I use Anthropic instead of OpenAI?**

**A**: Yes! The wizard supports both. I use OpenAI in examples, but Claude works great too.

---

**Q: What about the $40 PayPal limit? That seems low.**

**A**: It's intentionally low. This is for small recurring bills, one-time purchases, or reimbursements. For large transactions, use your primary accounts directly. Remember: **the agent is not you**. It's a separate entity you delegate small tasks to.

---

**Q: Couldn't an attacker exfiltrate data slowly over time via the internet connection?**

**A**: Yes, if they got in. That's why:
1. You only forward selected information (not your whole life)
2. Audit logging is enabled (review weekly)
3. Separate service accounts limit value
4. Spending limits prevent financial damage

No system is perfect. This reduces blast radius.

---

**Q: Why is this better than just using OpenClaw's built-in security features?**

**A**: OpenClaw's security is good, but:
- Default deployments are often misconfigured (42,900 exposed instances)
- Supply chain attacks via ClawHub are ongoing (900 malicious skills)
- Vulnerabilities keep being discovered (CVE-2026-25253)
- OAuth to your primary accounts = high-value target

Our approach: **defense in depth** + **separate identity** + **network isolation** + **manual information forwarding**.

Multiple overlapping protections, so when (not if) one fails, others hold.

---

## The Bottom Line

If you want an AI assistant that can act on your behalf—reading emails, executing commands, browsing the web, remembering context—you have two choices:

1. **Give it everything**: Full OAuth to your Gmail, access to your iCloud, your VPN, your network. When it gets compromised (not if—when), lose everything.

2. **Give it a staging area**: Separate accounts, isolated network, manual forwarding. When it gets compromised, lose a burner email and $40. Rebuild in 10 minutes.

I chose option 2.

**Join me. Let's build the most secure AI assistant together.**

🦞 **One Shroud Over Every Wire**

*Because the best security is the kind that assumes you'll be breached.*

---

**TL;DR**:
- OpenClaw had 40,000+ exposed instances, critical RCE vulnerability, and 900 malicious plugins
- This project isolates OpenClaw: internet-only access, separate service accounts, manual information forwarding
- If compromised, attacker gets a burner email and $40, not your digital identity
- Open source, auditable, runs locally
- Need developers, security engineers, and testers
- https://github.com/idallasj/agentshroud

**Let's make AI assistants actually safe to use.**
