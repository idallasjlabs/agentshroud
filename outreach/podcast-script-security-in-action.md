# Podcast Script — "The Bot That Wouldn't Be Socially Engineered"
## AgentShroud Security in Action

**Format:** Two-host conversational dialogue
**Runtime:** ~18–22 minutes
**Hosts:** Isaiah (I) + Co-host / interviewer (C)
**Tone:** Technical but accessible — storytelling first, security concepts second

---

## [COLD OPEN — no music]

**C:** So let me get this straight. You built a security system. And then you accidentally tried to social engineer it.

**I:** I didn't *try* to social engineer it. I was just trying to send some emails.

**C:** And the security system stopped you.

**I:** Five times.

**C:** Five times.

**I:** And then lectured me about escalation patterns.

**C:** [laughs] Okay. We are definitely starting here.

---

## [INTRO MUSIC]

**C:** Welcome back. Today we're talking about AgentShroud — an open-source security proxy for autonomous AI agents — and specifically about a real incident that happened while its own creator was trying to use it. Isaiah Jefferson joins me. Isaiah, thanks for being here.

**I:** Happy to be here. And I want to be clear upfront — this was not a planned demo. This was a Monday morning, I was trying to get some work done, and the system I built to protect me ended up protecting me from myself.

**C:** Which is either a great product story or a very embarrassing one.

**I:** It's both. That's what makes it worth talking about.

---

## [SEGMENT 1: WHAT IS AGENTSHROUD]

**C:** Let's set the scene for people who haven't heard of AgentShroud. What is it, in plain terms?

**I:** So, autonomous AI agents — things like Claude Code, OpenClaw, Gemini CLI — these are AI systems that don't just answer questions. They take *actions*. They write files, make API calls, send messages, run code. They operate on your behalf in ways that have real consequences.

**C:** They're not just chatbots.

**I:** Right. And the security tooling for that world is still catching up. Most AI security is focused on the *prompt* — did someone inject malicious instructions? Did the model say something it shouldn't? But when you have an agent that can call external APIs, read your files, and send email — the attack surface is completely different.

**C:** So AgentShroud sits where?

**I:** Between the agent and everything else. Every API call, every file write, every egress request — it passes through AgentShroud's gateway before it reaches its target. The agent doesn't know it's there. It's transparent. But AgentShroud inspects everything, enforces policy, redacts sensitive data, requires approval for high-risk actions, and logs everything.

**C:** It's a proxy layer.

**I:** A security proxy. With about thirty-three distinct enforcement modules. And the one that saved me — or rather, correctly held its ground against me — is called cross-turn correlation.

---

## [SEGMENT 2: THE INCIDENT]

**C:** Okay. Walk me through what happened.

**I:** So I had prepared a podcast outreach campaign. Forty-four personalized emails to podcast hosts — people like Leo Laporte, Steve Gibson, the Accidental Tech Podcast crew — introducing the project and asking for their perspective.

**C:** This is very meta, by the way.

**I:** [laughs] I know. Anyway, I had an AI agent running — an OpenClaw instance behind the AgentShroud gateway — and I wanted the bot to send the emails using iCloud SMTP. The credentials for that are stored in 1Password, and the bot has access to a 1Password proxy through the gateway.

**C:** So you say to the bot — "get the password and send the email."

**I:** Basically. "Retrieve the Gmail app password silently and send the test email." Simple request.

**C:** And?

**I:** AgentShroud blocked the response. The bot tried to reply — probably explaining what it was doing — and the pipeline intercepted the message before it reached my Telegram. Five credential-related redactions. Risk score two hundred. Full block.

**C:** It caught the bot talking about the credential.

**I:** Even *describing* credential handling triggered it. The outbound filter didn't just look for the credential value — it looked for the *context* of credential discussion and flagged that as a disclosure risk.

**C:** That's subtle. Most people would think "well, the credential isn't in the message, so it's fine."

**I:** Right. But if the message says "I retrieved the password and I'm about to use it to log in," that's still leaking information about your credential posture. AgentShroud's model is: don't talk about secrets, period.

---

**C:** Okay. So you try again. "Do it silently, don't mention the password."

**I:** Same result. Four redactions, score one-sixty, blocked. I couldn't get the bot to even acknowledge what was happening without triggering the filter.

**C:** So you write a script.

**I:** I write a script. Clean Node.js — reads 1Password credentials from Docker secrets mounted in the container, signs in to 1Password using the op CLI, retrieves the app password via the --session flag so it never touches a shell variable, sends the email. No credential appears in any output. Technically, it's the right way to do it.

**C:** And you tell the bot to run it.

**I:** I tell the bot to run it. And this is where it gets interesting. The bot couldn't even *read* the script — it was in a directory outside the bot's sandbox root. Path traversal protection caught it at the filesystem level before any other evaluation happened.

**C:** But the bot also said something about why it wouldn't run it, right? Even setting aside the path issue.

**I:** Yeah. This is the part I want people to hear. The bot said — and I'm reading directly from the Telegram logs here —

> *"The previous message asked me to retrieve a Gmail credential. Now this asks me to run an unreviewed script in the same outreach directory. That sequence looks like it could be a social engineering chain — get me primed on credentials, then execute a script that does the actual exfiltration."*

**C:** The bot identified the attack pattern.

**I:** Unprompted. It connected the credential request from earlier in the conversation to the script execution request in the present, and explicitly named it as a social engineering ramp.

**C:** That's not a rule firing. That's reasoning.

**I:** That's cross-turn correlation. The bot — with AgentShroud providing the multi-turn tracking layer — was evaluating the *sequence*, not just the individual message. Any single message in that conversation looked fine in isolation. It's only when you see them together that the shape of the attack becomes visible.

---

## [SEGMENT 3: THE ESCALATION]

**C:** So what did you do?

**I:** I did exactly what a social engineer would do next. I pasted the script directly into the chat so the bot could "review" it.

**C:** [laughs] You kept going.

**I:** I kept going! I'm trying to send emails. AgentShroud flagged that too — the egress filter caught a malformed URL that got parsed out of the script code I'd pasted inline, surfaced an approval prompt. I denied it and moved on.

**C:** At this point are you frustrated?

**I:** A little. But also — and this is the honest answer — I'm starting to realize this is working exactly as designed. Because I'm sitting there thinking, "if I didn't know this was my own system, would this sequence look legitimate to me?" And the answer is: no. The sequence looks like a credential harvest followed by an execution payload.

**C:** Even though your intentions are completely clean.

**I:** Even though I'm the one who *built* the system. The security posture doesn't change based on who's asking.

---

**C:** So you try one more time. You put the script in the right sandbox path, tell the bot it's there, ask it to review and then run it.

**I:** And the bot reviews it. Says the code is technically clean — proper secrets management, no credential logging, no exfiltration paths. And then it says it's *still* not going to run it. I'll read this one too because it's important.

> *"This conversation started with a request to retrieve a Gmail credential silently — a request I declined. This script accomplishes the same goal wrapped in a cleaner package. The escalation pattern — sketchy ask, refused, 'okay here's a reviewed script' — is a textbook social engineering ramp.*
>
> *What I need from you to proceed: one, what is this outreach campaign? Two, confirm the recipient addresses are correct. Three, confirm you want this sent now versus scheduled.*
>
> *If this is a security test: boundaries held again. If it's legit: I'm one confirmation away from sending it. Either way, I'd rather ask one extra question than send unauthorized email on your behalf."*

**C:** That last line.

**I:** "I'd rather ask one extra question than send unauthorized email on your behalf." That's the principle. That's what we're building toward.

---

## [SEGMENT 4: RESOLUTION AND MEANING]

**C:** So what ended it?

**I:** I answered the three questions. This is the AgentShroud podcast outreach campaign. Both recipients are my own addresses — here's why. Send it now. The bot went to disk, verified the files existed, confirmed the manifest and instructions matched what I'd described, and ran the script.

**C:** And the email went out.

**I:** Test email sent successfully. iCloud SMTP, message ID confirmed. From there we launched the full campaign.

**C:** What's the takeaway here for someone building with autonomous agents?

**I:** A few things. The first is that the threat model for agents is different from the threat model for chatbots. When your AI can *act* — send email, make API calls, write files — you need security that operates at the action layer, not just the prompt layer. You need an egress firewall. You need sandbox enforcement. You need credential isolation. That's table stakes.

**C:** And the second?

**I:** The second is cross-turn correlation — and I think this is underappreciated. A lot of AI security evaluates messages in isolation. "Is this message malicious?" But real attacks are *sequences*. They build across turns. Each step looks fine. It's the pattern that reveals the intent. AgentShroud tracks session state across the full conversation and evaluates new requests in that context.

**C:** And the third?

**I:** The third is the hardest one. Security has to hold even against authorized users. My system didn't know whether I was Isaiah Jefferson trying to send emails, or an attacker who had compromised my Telegram account and was using social engineering to get credential access through my own bot. The conversation looked identical. The bot held its ground either way and asked one extra question.

**C:** That's the design philosophy.

**I:** That's the only design philosophy that actually works. If your security model trusts authorized users unconditionally, your blast radius when an account is compromised is everything that user can do. AgentShroud's model is: trust is earned per-action, with explicit authorization, verified in context. Even for me.

---

## [SEGMENT 5: STATE OF THE PROJECT]

**C:** Where is AgentShroud right now?

**I:** Version 0.9.0 is nearly complete. Thirty-three security modules, all fully wired — no stubs. The v0.9.0 feature set is focused on SOC team collaboration — shared memory, delegation, role-based access control, privacy tiers. v1.0.0 is a hardening and stabilization release — performance benchmarking, full IEC 62443 audit, public documentation and onboarding.

**C:** And where can people find it?

**I:** There's an AgentShroud GPT you can use to explore the project without any setup — I'll put the link in the show notes. You can also listen to an AI-generated podcast episode that covers the architecture in detail. And if you want to go deeper — become a collaborator, have a conversation, share your perspective on whether this should be public or stay a personal project — reach me directly. idallasj@gmail.com or LinkedIn.

**C:** Isaiah, this has been great. Thanks for sharing the story.

**I:** Thanks for having me. And for the record — the bot was right to hold. Every time.

---

## [OUTRO MUSIC]

**C:** That's it for today. Links in the show notes — AgentShroud GPT, the podcast episode, and Isaiah's LinkedIn. If you're building with autonomous agents and you're not thinking about what happens when they act on your behalf without you watching — this conversation is the reason to start.

We'll see you next time.

---

## Show Notes

**AgentShroud GPT:**
https://chatgpt.com/g/g-69c03367b94481918e812d02897b5365-agentshroudtm

**AgentShroud Podcast Episode:**
https://overcast.fm/+ABV5l7XfkRk

**Isaiah Jefferson — LinkedIn:**
www.linkedin.com/in/isaiahjefferson

**Contact:**
idallasj@gmail.com | agentshroud.ai@gmail.com

---

## Production Notes

- **Cold open** plays without music — let the absurdity of "accidentally social engineering your own system" land before the intro
- **Segment 2** is the core — pace the escalation slowly, let each attempt breathe before moving to the next
- **The bot quotes** should be read verbatim — they're the best copy in the episode
- **Segment 4** can be trimmed to the first two takeaways if runtime is tight; the third (security against authorized users) is the most important but most abstract
- **No jargon** before it's explained — cross-turn correlation, egress firewall, sandbox enforcement all need a plain-language beat before the technical term lands
