# AgentShroud — Security & Access Diagrams

> AgentShroud™ is a trademark of Isaiah Jefferson · All rights reserved

---

## 11. Trust Boundary Diagram

```mermaid
graph TB
    subgraph TB0["Trust Zone 0 — Owner (Highest Trust)"]
        ISAIAH["Isaiah Jefferson\nApprove actions · Gateway admin\nSecret rotation · Full control"]
    end

    subgraph TB1["Trust Zone 1 — Gateway (Trusted Enforcer)"]
        GW["AgentShroud Gateway\nHolds 1Password credentials\nEnforces all security policy"]
    end

    subgraph TB2["Trust Zone 2 — Bot (Supervised Agent)"]
        BOT["AgentShroud Bot\nNo direct credentials or internet\nAll access via gateway"]
    end

    subgraph TB3["Trust Zone 3 — External Services (Conditional)"]
        OAI["OpenAI API\nTrusted for inference\nAllowlisted domain"]
        ANTH["Anthropic API\nTrusted for inference\nAllowlisted domain"]
        TG["Telegram API\nTrusted for messaging\nAllowlisted domain"]
        GH["GitHub\nTrusted for code ops\nAllowlisted domain"]
        OP["1Password\nTrusted for secrets\nGateway-only access"]
    end

    subgraph TB4["Trust Zone 4 — Infrastructure Nodes (SSH-gated)"]
        PI["raspberrypi\nSSH: approved host\nagentshroud-bot user"]
        MARVIN["marvin\nSSH: approved host"]
        TRILLIAN["trillian\nSSH: approved host"]
    end

    subgraph DENIED["Blocked / Untrusted"]
        LAN["LAN (RFC1918)\n10.x / 172.16.x / 192.168.x\nBlocked by gateway"]
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

    Note over GW: Service account token<br/>loaded from Docker secret

    Note over BOT: No direct 1Password access<br/>All secrets via op-proxy

    BOT->>GW: POST /credentials/op-proxy<br/>{reference: "op://..."}
    Note over GW: Validates auth token<br/>Checks allowed_op_paths
    GW->>OP: op read "op://..." (service account)
    OP-->>GW: Secret value
    GW-->>BOT: {"value": "<secret>"}

    Note over BOT: op_proxy_read_with_retry()<br/>Cascading retries: 5s→10s→30s→60s

    BOT->>ENV: export ANTHROPIC_OAUTH_TOKEN
    BOT->>ENV: export BRAVE_API_KEY
    BOT->>ENV: export ICLOUD_APP_PASSWORD
    BOT->>ENV: export ICLOUD_USERNAME

    Note over ENV: Env vars only\nNever written to disk\nNever logged
```

---

## 13. Network Security Diagram — Egress Controls

```mermaid
flowchart TD
    BOT_REQ["Bot makes outbound request"]

    CHECK1{"HTTP_PROXY set?\nhttp://gateway:8181"}
    DIRECT["Direct connection\n(bypasses all controls)\nNOT CONFIGURED"]
    CONNECT["HTTP CONNECT tunnel\nto gateway:8181"]

    CHECK2{"Domain allowlisted?\n(agentshroud.yaml)"}

    ALLOWED["Allowlisted Domains\nOpenAI · Anthropic · Telegram\nGitHub · iCloud · googleapis"]

    BLOCKED["Blocked (403)\nAll unlisted domains\nAll RFC1918 addresses"]

    TCP["TCP tunnel established\nGateway relays traffic"]

    LOG["Connection logged\ntimestamp · domain\nallowed / blocked"]

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
