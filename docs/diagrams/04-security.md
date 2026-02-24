# AgentShroud — Security & Access Diagrams

> AgentShroud™ is a trademark of Isaiah Jefferson · All rights reserved

---

## 11. Trust Boundary Diagram

```mermaid
graph TB
    subgraph TB0["Trust Zone 0 — Owner (Highest Trust)"]
        ISAIAH["Isaiah Jefferson\nFull control:\n- Approve/reject actions\n- Gateway admin\n- Container restart\n- Secret rotation"]
    end

    subgraph TB1["Trust Zone 1 — Gateway (Trusted Enforcer)"]
        GW["AgentShroud Gateway\n- Holds 1Password service account\n- Enforces all security policy\n- Signs all ledger entries\n- Controls approval queue\n- HMAC/JWT token validation"]
    end

    subgraph TB2["Trust Zone 2 — Bot (Supervised Agent)"]
        BOT["AgentShroud Bot\n- No direct credential access\n- No direct internet access\n- All secrets via op-proxy\n- All outbound via HTTP CONNECT proxy\n- All MCP calls via MCP inspector"]
    end

    subgraph TB3["Trust Zone 3 — External Services (Conditional)"]
        OAI["OpenAI API\nTrusted for inference\nAllowlisted domain"]
        ANTH["Anthropic API\nTrusted for inference\nAllowlisted domain"]
        TG["Telegram API\nTrusted for messaging\nAllowlisted domain"]
        GH["GitHub\nTrusted for code ops\nAllowlisted domain"]
        OP["1Password\nTrusted for secrets\nGateway-only access"]
    end

    subgraph TB4["Trust Zone 4 — Infrastructure Nodes (SSH-gated)"]
        PI["raspberrypi\nSSH: approved host\nUser: agentshroud-bot\nKey: id_ed25519"]
        MARVIN["marvin\nSSH: approved host"]
        TRILLIAN["trillian\nSSH: approved host"]
    end

    subgraph DENIED["Blocked / Untrusted"]
        LAN["LAN (RFC1918)\n10.x / 172.16.x / 192.168.x\nBlocked by gateway\nbot cannot reach host LAN"]
        UNLISTED["Unlisted domains\nBlocked by default-deny\nHTTP CONNECT proxy"]
    end

    ISAIAH -->|"Telegram approval\nDirect container access"| GW
    GW -->|"Enforces policy on"| BOT
    BOT -->|"All requests through"| GW
    GW -->|"Allowlisted HTTPS only"| TB3
    GW -->|"SSH proxy (approved hosts)"| TB4
    BOT -. "BLOCKED" .-> DENIED
```

---

## 12. Credential Flow Diagram

How secrets are managed and reach the bot.

```mermaid
sequenceDiagram
    participant OP as 1Password Cloud
    participant GW as Gateway Container<br/>(has service account)
    participant BOT as Bot Container<br/>(no service account)
    participant ENV as Bot Environment

    Note over GW: OP_SERVICE_ACCOUNT_TOKEN<br/>loaded from Docker secret<br/>/run/secrets/1password_service_account

    Note over BOT: Starts with ZERO 1Password access.<br/>Uses op-proxy endpoint on gateway.

    BOT->>GW: POST /credentials/op-proxy<br/>{"reference": "op://AgentShroud Bot Credentials/..."}
    Note over GW: Validates GATEWAY_AUTH_TOKEN<br/>Checks allowed_op_paths pattern<br/>"op://AgentShroud Bot Credentials/*"
    GW->>OP: op read "op://..." (service account)
    OP-->>GW: Secret value
    GW-->>BOT: {"value": "<secret>"}

    Note over BOT: op_proxy_read_with_retry()<br/>Cascading retries: 5s,10s,15s,30s,60s

    BOT->>ENV: export ANTHROPIC_OAUTH_TOKEN
    BOT->>ENV: export BRAVE_API_KEY
    BOT->>ENV: export ICLOUD_APP_PASSWORD
    BOT->>ENV: export ICLOUD_USERNAME
    BOT->>ENV: export ICLOUD_EMAIL

    Note over ENV: Secrets live only in container<br/>memory as env vars.<br/>Never written to disk.<br/>Never logged.
```

---

## 13. Network Security Diagram — Egress Controls

```mermaid
flowchart TD
    BOT_REQ["Bot makes outbound request\n(any HTTPS connection)"]

    CHECK1{"HTTP_PROXY set?\nhttp://gateway:8181"}
    DIRECT["Direct connection\n(would bypass all controls)\nNOT CONFIGURED"]
    CONNECT["HTTP CONNECT tunnel\nrequest to gateway:8181"]

    CHECK2{"Domain allowlisted?\n(agentshroud.yaml\nproxy.allowed_domains)"}

    ALLOWED["Allowlisted domains:\napi.openai.com\napi.anthropic.com\napi.telegram.org\noauth2.googleapis.com\nwww.googleapis.com\n*.github.com\n*.githubusercontent.com\nimap.mail.me.com\nsmtp.mail.me.com"]

    BLOCKED["Blocked (403 Forbidden)\nAll other domains\nAll RFC1918 addresses\n(10.x / 172.16.x / 192.168.x)"]

    TCP["TCP tunnel established\nGateway relays traffic"]

    LOG["Connection logged:\n- timestamp\n- target domain\n- allowed/blocked\n- connection count"]

    BOT_REQ --> CHECK1
    CHECK1 -->|"Yes (production)"| CONNECT
    CHECK1 -->|"No"| DIRECT
    CONNECT --> CHECK2
    CHECK2 -->|"Match"| ALLOWED
    CHECK2 -->|"No match"| BLOCKED
    ALLOWED --> TCP
    TCP --> LOG
    BLOCKED --> LOG
```
