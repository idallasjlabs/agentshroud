# Inbound MCP Edge — Agent Coverage and Vendor Onboarding

Researched 2026-11-09 against vendor documentation. **UNCONFIRMED** means the vendor's official documentation does not state the capability.

## How each personal agent is covered

| Agent | Mechanism | Status |
|---|---|---|
| **Claude Duet** (owner's agent) | Claude custom connector → Inbound MCP Edge. Profile `claude-duet` covers Duet, chat and Cowork (one account, one client identity) | First live pilot (SCRUM-218); runbook §1a |
| **Poke** | Custom MCP integration → Edge | Supported; redirect URI to be captured during its pilot |
| **Gemini Spark** | Gemini custom app (MCP) → Edge; host egress watch of the macOS app | Edge supported; egress watch is SCRUM-219 |
| **OpenAI Dots** | Slack/Teams bridge to Hermes (SCRUM-220); host egress watch if it runs on the owner's Mac | Custom MCP from Dots is UNCONFIRMED |
| **Perplexity Personal Computer** | Host egress watch | SCRUM-219 |
| **Meta Muse** | Edge profile `meta-muse` (custom MCP UNCONFIRMED); host egress watch of a local app (`meta-muse-local`) | Profile ships disabled, read-only, no redirect URI; egress watch is SCRUM-219 |
| **xAI Grok Bot** | Edge profile `xai-grok-bot` (custom MCP UNCONFIRMED) | Profile ships disabled, read-only, no redirect URI |
| **Instinct, Manus Cue** | None. They act as the user, with their own identity, inside the vendor cloud. | Documented residual risk (threat model T10) |

Every profile declares `connection` (`mcp` or `chat-bridge`), `support` (`documented` or `unconfirmed`) and the `docs` it was written from; the Command Center's Agents page shows all three. An **unconfirmed** vendor ships with no redirect URI (OAuth cannot complete) and read-only tools; an enabled `chat-bridge` vendor refuses to load until the Slack/Teams bridge (SCRUM-220) exists.

## Claude Duet

- **Attach:**
  - Claude → Customize → Connectors → Custom → Web → URL `https://<node>.ts.net:8443/mcp` ([Anthropic help](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)).
  - Duet "works with the connectors you've connected in Claude" ([Duet help](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)). Whether it uses *custom* ones is **UNCONFIRMED** officially, and the pilot will confirm it.
- **Auth:** OAuth with automatic registration (DCR) or your own client. The callback is `https://claude.ai/api/mcp/auth_callback`, and Anthropic says it may move to `https://claude.com/api/mcp/auth_callback` ([help](https://support.anthropic.com/en/articles/11503834-building-custom-connectors-via-remote-mcp-servers)). Both are in the profile.
  - **CIMD ("Use Claude's published identity") is not supported yet** (checked 2026-11-11 against [Claude connector authentication](https://claude.com/docs/connectors/building/authentication.md)). Claude selects CIMD only when the server advertises `client_id_metadata_document_supported: true`, and otherwise falls back to DCR, so choose **Register automatically**. The docs publish Claude Code's client-ID URL but not the hosted apps' one, and an allowlist that guesses it is not a control. Follow-up once Anthropic publishes it.
  - Claude always sends S256 PKCE, refreshes on 401 and up to five minutes before expiry, and expects rotated refresh tokens for public clients; the edge rotates them with reuse detection.
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
- **Path chosen:** the Slack/Teams bridge to Hermes (SCRUM-220). `openai-dots.yaml` is `connection: chat-bridge`, read-only, with `dynamic_registration: false` until custom MCP is confirmed.

## Meta Muse

- **Custom MCP: UNCONFIRMED** (checked 2026-11-11). Meta documents built-in connectors and "Custom Connectors" for services with APIs, but no user-facing flow for adding an MCP server URL. A third-party walkthrough reports a Custom Connector accepting a remote MCP gateway with OAuth on some accounts ([Arcade](https://www.arcade.dev/blog/connect-meta-muse-mcp-gateway/)); others report no such field ([AI Agents Library](https://www.aiagentslibrary.com/blog/meta-muse-mcp/)). Muse Code, Meta's coding agent, is the product with documented MCP.
- **Profile:** `meta-muse.yaml`, disabled, read-only, no redirect URI. Capture the callback during a pilot window before adding it.

## xAI Grok Bot

- **Custom MCP: UNCONFIRMED** (checked 2026-11-11). xAI says a Bot "can interact with any MCP or API" ([xAI docs](https://docs.x.ai/grok-bot/overview)). Third-party guides describe adding a remote HTTPS MCP server under Plugins with OAuth, and say local (stdio) servers are not supported ([Composio](https://composio.dev/content/guide-to-frok-bot)).
- **Profile:** `xai-grok-bot.yaml`, disabled, read-only, no redirect URI.

## Enabling a vendor

See [04-runbook.md](04-runbook.md) §1. Keep each vendor's tool list minimal. Writes always need approval.
