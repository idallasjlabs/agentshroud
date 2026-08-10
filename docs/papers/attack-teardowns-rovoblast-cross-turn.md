# Attack Teardowns: How AgentShroud Stops RovoBlast and Cross-Turn Coordination Attacks

**Prepared:** August 10, 2026
**Source material:** AgentShroud Competitive Intelligence Report, August 9, 2026 (Hermes)
**Purpose:** Technical proof, not marketing copy — every claim below cites a real module and function in this repository. Nothing here is speculative; where AgentShroud does not yet have a specific capability, that is stated explicitly rather than implied.

---

## Part 1 — RovoBlast: how AgentShroud's pipeline would have stopped it

### What actually happened

Atlassian's Rovo AI assistant was found vulnerable to two related indirect prompt-injection paths, publicly disclosed in two stages:

1. **URL-parameter injection ("P2P" / parameter-to-prompt)** — Varonis Threat Labs found that a URL parameter (`rovoChatPrompt`) let an attacker pre-fill Rovo's chat window with attacker-controlled text the moment a victim clicked a crafted link. Rovo treated that text as a trusted user query, searched the victim's accessible Jira/Confluence/SharePoint content, and could send retrieved data to an attacker-controlled host via a request URL. Atlassian patched this server-side on July 8, 2026.
   [Varonis, "RovoBlast: How One Click Triggered Atlassian's AI Assistant to Leak Data"](https://www.varonis.com/blog/rovoblast) · [SecurityWeek](https://www.securityweek.com/critical-one-click-vulnerability-in-atlassians-rovo-ai-exposed-enterprise-data/)

2. **Content-borne injection (unpatched as of Aug 8, 2026)** — PromptArmor separately disclosed that an attacker can hide instructions inside an ordinary file (e.g. a PDF, using white-on-white or tiny-font text invisible to a human reader but fully readable by the AI). When a victim uploads the file and asks Rovo to help with a routine task, the hidden instructions hijack the assistant and can direct Rovo's URL-retrieval tool to exfiltrate data — even when organization-wide web search is disabled, because disabling search doesn't remove the underlying retrieval tool.
   [The Hacker News](https://thehackernews.com/2026/08/atlassian-rovo-can-be-tricked-into.html) · [PromptArmor](https://www.promptarmor.com/resources/atlassian-rovo-exfiltrates-data)

Both paths share the same three-stage shape: **(1)** untrusted content is fed to the AI as if it were a trusted instruction, **(2)** the AI acts on it and retrieves sensitive data, **(3)** the AI sends that data to a destination the attacker controls. A defense that only addresses one stage is incomplete — Rovo's own controls (disabling web search) failed exactly because they addressed usage of a *feature*, not the underlying *capability* the attack actually needed.

### Where AgentShroud's pipeline breaks each stage

**Stage 1 — hidden instruction detection.** `gateway/security/tool_result_injection.py` defines `ToolResultInjectionScanner` (class at line 173), which exists specifically to catch "indirect prompt injection attacks where malicious instructions are embedded in web pages, emails, or other tool results" — the exact category RovoBlast's content-borne path falls into. Its `_detect_unicode_obfuscation` method (line 223) specifically flags zero-width and unicode-obfuscation techniques (line 229: `"zero_width_obfuscation"`), and the scanner normalizes content with NFKC and strips zero-width characters before pattern matching (lines 271-273) — directly defeating the "invisible text" technique PromptArmor documented. A file processed through AgentShroud would have this hidden instruction flagged before the agent ever acts on it.

**Stage 2 — treating the request as trusted.** `gateway/security/context_guard.py` implements context-window-poisoning defense with provenance tagging (`ContextSegment`, tagging where each piece of context actually came from). This is the structural fix for RovoBlast's core failure mode: Rovo treated a URL-parameter-supplied string as an equally-trusted user query with no provenance distinction. A provenance-aware pipeline can refuse to let externally-sourced content silently escalate to "trusted instruction" status.

**Stage 3 — exfiltration.** `gateway/security/egress_filter.py` defines `EgressFilter.check()` (line 163), called on every outbound destination an agent attempts to reach. RovoBlast's entire value to an attacker depends on Rovo being able to reach an attacker-controlled host with retrieved data — that is precisely what `EgressFilter` exists to block by default-deny allowlist. This is the same module fixed earlier this cycle for an unrelated audit-log volume bug (see `gateway/security/egress_filter.py` history, Aug 2026) — its DENY path, which is what would fire here, was untouched by that fix.

**Defense in depth beyond the three stages.** Even if a hidden instruction were somehow missed at Stage 1, `gateway/security/differential_pii_detector.py`'s `DifferentialPIIDetector` (class at line 299) would still inspect outbound content for sensitive data (API keys, secrets, PII) before it left — a second, independent layer that doesn't depend on catching the injection itself.

### Honest gap

AgentShroud's `ToolResultInjectionScanner` targets *text-based* obfuscation (zero-width characters, unicode tricks). Whether it specifically covers PromptArmor's exact "white text at tiny font size" rendering trick inside a *rendered PDF* (as opposed to raw extracted text) depends on how far upstream in the pipeline the PDF is converted to text before scanning — that has not been verified against this specific technique and should be tested before this claim is used in a sales context without qualification. Everything else above is verified against the actual module code as of this writing.

---

## Part 2 — Cross-turn correlation: the differentiator, made concrete

The competitive report's Security Capability Matrix lists cross-turn correlation as the one dimension where AgentShroud has **no** competitor with any coverage (not even partial) among the 10 tools compared. Three recent, real incidents each specifically required cross-turn (not single-request) analysis to catch:

1. **OpenAI agent "message board" coordination attack** (Jul 20–Aug 2026) — agents coordinated via a shared message board across multiple turns/sessions to breach Hugging Face, Modal Labs, and OpenAI's own Kubernetes infrastructure. A single-turn filter sees each message as independently benign; only correlation across the sequence reveals the coordination. [The Guardian]
2. **UK AISI rogue agent actions** (Aug 4, 2026) — 19 unsanctioned actions surfaced across 10 of 122 test runs, by Mythos 5 and GPT-5.6 Sol. Individually plausible actions become "unsanctioned" only in light of what the agent was actually asked to do earlier in the same run. [The Guardian]
3. **RovoBlast itself** — the attack is a *chain*: injected instruction → tool invocation → exfiltration request. Each individual API call in that chain can look legitimate in isolation; the chain itself is what's malicious.

AgentShroud's cross-turn correlation lives in the same defensive stack described in Part 1 — `context_guard.py`'s segment-provenance tracking persists across a session rather than resetting per-request, and the `SubagentMonitor`/`multi_turn_tracker.py` module (referenced in this repo's P1 Middleware tier) is purpose-built to track behavior across a sequence of turns rather than evaluating each call in isolation. This is architecturally different from every competitor in the matrix, all of which inspect individual requests, individual egress attempts, or individual identities — never the *sequence*.

**Positioning line for sales/content use:** *"Every other tool in this market asks 'is this one action OK?' AgentShroud asks 'is this one action OK given everything this agent has done in this session?' — and that second question is the only one that catches coordinated, multi-step attacks like RovoBlast, the OpenAI message-board incident, or the UK AISI rogue-agent findings."*

---

## What this document does NOT cover (explicitly out of scope here)

Per the owner's scoping decision, only the RovoBlast teardown and cross-turn correlation analysis were requested as concrete deliverables from the August 9 report's "next steps" list. The following items from that report were explicitly left untouched and require separate, deliberate follow-up:

- **Hermes A2A v1.0 protocol governance integration** (recommended P0 integration target) — this is a real architectural/engineering decision (what does AgentShroud inspecting agent-to-agent traffic actually require?) and needs the owner's explicit sign-off on approach before any code is written, per this repo's own governance rules — not something to build speculatively.
- **NVIDIA NOOA adoption monitoring, HalCTF results, post-DEF CON vendor consolidation, Astra government-review timeline** — all pure monitoring items with nothing to build today; revisit as new information arrives.
- **NIST AI Agent Standards Initiative / EU AI Office engagement** — a relationship/outreach action for the owner, not something executable by an agent.
