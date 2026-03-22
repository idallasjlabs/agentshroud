# Accidental Tech Podcast — Marco Arment, Casey Liss, John Siracusa
**To:** atp@marco.org
**Subject:** Long-time listener — AgentShroud: a security proxy for AI coding agents

---

Hi Marco, Casey, and John,

I'm Isaiah Jefferson — systems architect, long-time ATP listener, and someone who has spent a lot of time thinking about the same kinds of design tradeoffs you three discuss every week.

I'm reaching out as a listener, not a PR pitch. I've been building **AgentShroud** — an open-source security proxy for autonomous AI coding agents. Given how much of the show lately touches on AI tools and their integration into development workflows, I thought you might find the architecture interesting.

The core problem: tools like Claude Code, Copilot, and Cursor now have real write access to codebases, file systems, and APIs. AgentShroud sits between those agents and the target system, enforcing policy on every tool call and keeping a full audit trail. It's the infrastructure question that almost nobody is asking yet.

I'm not pitching it as a show topic — just sharing it in case it's interesting, the way you'd share something cool with fellow developers. The codebase is open, 33 security modules, ≥94% test coverage.

**v0.9.0 is nearly complete.** Try the GPT to explore it:
https://chatgpt.com/g/g-69c03367b94481918e812d02897b5365-agentshroudtm

Also listen to the AI-generated AgentShroud podcast episode:
https://overcast.fm/+ABV5l7XfkRk

I'm approaching a go/no-go decision on whether to make AgentShroud fully public or keep it for personal use. I'd genuinely value an outside perspective. If you have a few minutes to explore the GPT, listen to the podcast, or consider becoming a collaborator, I'd love to hear your honest opinion. Reach me directly: idallasj@gmail.com, agentshroud.ai@gmail.com, or via LinkedIn.

If you'd like to follow along or collaborate:
- **Telegram:** @agentshroud_bot → /start
- **Slack:** Send me your Slack user ID and I'll add you

More about me: www.linkedin.com/in/isaiahjefferson

Thanks for a decade-plus of thoughtful technical conversation.

Isaiah Jefferson

*P.S. I know you don't do regular guest segments — this isn't that. Just a listener who thought you might find it interesting.*
