# Inbound MCP Edge — Agent Coverage and Vendor Onboarding

Researched 2026-11-09 against vendor documentation. **UNCONFIRMED** means the vendor's official documentation does not state the capability.

## How each personal agent is covered

| Agent | Mechanism | Status |
|---|---|---|
| **Claude Duet** (owner's agent) | Claude custom connector → Inbound MCP Edge | First live pilot (SCRUM-218) |
| **Poke** | Custom MCP integration → Edge | Supported; redirect URI to be captured during its pilot |
| **Gemini Spark** | Gemini custom app (MCP) → Edge; host egress watch of the macOS app | Edge supported; egress watch is SCRUM-219 |
| **OpenAI Dots** | Slack/Teams bridge to Hermes (SCRUM-220); host egress watch if it runs on the owner's Mac | Custom MCP from Dots is UNCONFIRMED |
| **Perplexity Personal Computer** | Host egress watch | SCRUM-219 |
| **Meta Muse** | Host egress watch of the Mac app (no MCP support listed) | SCRUM-219 |
| **Grok Bot, Instinct, Manus Cue** | None. They act as the user, with their own identity, inside the vendor cloud. | Documented residual risk (threat model T10) |

## Claude Duet

- **Attach:**
  - Claude → Customize → Connectors → Custom → Web → URL `https://<node>.ts.net:8443/mcp` ([Anthropic help](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)).
  - Duet "works with the connectors you've connected in Claude" ([Duet help](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)). Whether it uses *custom* ones is **UNCONFIRMED** officially, and the pilot will confirm it.
- **Auth:** OAuth with automatic registration (DCR) or your own client. The callback is `https://claude.ai/api/mcp/auth_callback`, and Anthropic says it may move to `https://claude.com/api/mcp/auth_callback` ([help](https://support.anthropic.com/en/articles/11503834-building-custom-connectors-via-remote-mcp-servers)). Both are in the profile.
- **Transport:** Streamable HTTP.
- **Egress addresses:** Anthropic publishes `160.79.104.0/21` and `153.61.208.0/20` for MCP tool calls ([IP addresses](https://platform.claude.com/docs/en/api/ip-addresses)). They are recorded in `source_cidrs` and not yet enforced.
- **Profile:** `config/inbound-edge/vendors/claude-duet.yaml`.

## Poke

- **Attach:** poke.com/integrations/new → Name, MCP Server URL, optional API key ([Poke docs](https://poke.com/docs/managing-integrations)).
- **Auth:**
  - OAuth with DCR "works automatically" ([Poke MCP docs](https://poke.com/docs/mcp-servers)).
  - API key as Bearer is also offered, but the edge's static bearer is not implemented, so use OAuth.
  - Poke sends `X-Poke-User-Id`, which is useful for audit and is not authentication.
- **Transport:** the official template uses Streamable HTTP at `/mcp` ([template](https://github.com/InteractionCo/mcp-server-template)).
- **Profile:** `poke.yaml`. Its `redirect_uris` are empty, so registration fails closed until they are captured from Poke's first registration in an enrollment window.

## Gemini Spark

- **Attach:** gemini.google.com → Settings → Connected Apps → Custom apps → Add a custom app → MCP URL. Web only; US, 18+, personal accounts ([Google help](https://support.google.com/gemini/answer/17209137)). That page doesn't name Spark; MCP support for Spark comes from [9to5Google](https://9to5google.com/2026/06/30/gemini-spark-apps-more/).
- **Auth:** OAuth with DCR by default, or manual client credentials under Advanced. Transport is UNCONFIRMED.
- **Profile:** `gemini-spark.yaml`. Its `redirect_uris` are empty; they must be filled in during the pilot.
- **Desktop app:** the egress watch is tracked in SCRUM-219.

## OpenAI Dots

- **Custom MCP:** Dots "can use supported plugins installed and enabled for your account" ([learn.chatgpt.com](https://learn.chatgpt.com/codex/dots/computers-and-apps)). Whether it can use a custom MCP server is **UNCONFIRMED**.
- **ChatGPT's own MCP support:** ChatGPT accepts remote MCP over Streamable HTTP with OAuth 2.1 + PKCE. It prefers CIMD (Client ID Metadata Documents), falls back to DCR, and never sends static API keys ([OpenAI auth](https://developers.openai.com/plugins/build/auth)).
  - The edge accepts DCR today; CIMD support is a follow-up.
  - OpenAI publishes `chatgpt-connectors.json` egress ranges.
- **Path chosen:** the Slack/Teams bridge to Hermes (SCRUM-220). `openai-dots.yaml` has `dynamic_registration: false` until custom MCP is confirmed.

## Enabling a vendor

See [04-runbook.md](04-runbook.md) §1. Keep each vendor's tool list minimal. Writes always need approval.
