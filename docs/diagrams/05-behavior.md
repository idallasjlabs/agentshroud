# AgentShroud — System Behavior Diagrams

> AgentShroud™ is a trademark of Isaiah Jefferson · All rights reserved

---

## 14. Logic Flow / Flowchart — Request Execution

```mermaid
flowchart TD
    START(["User sends message\nor cron fires"])

    RECV["Bot receives event\n(Telegram / iMessage / Web / Cron)"]

    ROUTE{"Route to agent?\n(bindings config)"}
    MAIN["Main agent\n(agentshroud_bot)"]

    LLM_CALL["LLM inference\n(OpenAI GPT-4o\nor Anthropic Claude)"]

    DECIDE{"Agent decides\nnext action"}

    REPLY_ONLY["Send reply to user"]

    TOOL_CALL["Issue tool call\n(MCP server)"]

    MCP_INSPECT["MCP Inspector\ninjection scan\nPII scan\nsensitive op scan"]

    THREAT{"Threat level?"}
    NONE_LOW["NONE / LOW\nAllow + log"]
    MEDIUM["MEDIUM\nAllow + audit flag"]
    HIGH_THREAT["HIGH\nBlock + alert Isaiah"]

    APPROVAL_CHECK{"Action type\nrequires approval?\n(email_sending\nfile_deletion\nexternal_api_calls\nskill_installation)"]

    QUEUE_ITEM["Add to approval queue\nNotify Isaiah via Telegram\nWait up to 1 hour"]

    DECISION{"Isaiah decides"}
    APPROVED["Approved\nExecute action"]
    REJECTED["Rejected\nLog + notify bot"]
    EXPIRED["Expired (1h timeout)\nAuto-reject"]

    EXECUTE["Execute action\nvia HTTP CONNECT proxy"]

    LEDGER["Write audit entry\nto ledger.db\n(SHA-256 hash only)"]

    END(["Response delivered\nto user"])

    START --> RECV
    RECV --> ROUTE
    ROUTE -->|"Telegram ID 8096968754 → main"| MAIN
    MAIN --> LLM_CALL
    LLM_CALL --> DECIDE

    DECIDE -->|"Direct reply"| REPLY_ONLY
    DECIDE -->|"Tool call"| TOOL_CALL

    TOOL_CALL --> MCP_INSPECT
    MCP_INSPECT --> THREAT

    THREAT -->|"NONE/LOW"| NONE_LOW
    THREAT -->|"MEDIUM"| MEDIUM
    THREAT -->|"HIGH"| HIGH_THREAT

    NONE_LOW --> APPROVAL_CHECK
    MEDIUM --> APPROVAL_CHECK
    HIGH_THREAT --> LEDGER

    APPROVAL_CHECK -->|"No approval needed"| EXECUTE
    APPROVAL_CHECK -->|"Approval needed"| QUEUE_ITEM

    QUEUE_ITEM --> DECISION
    DECISION -->|"✅ Approved"| APPROVED
    DECISION -->|"❌ Rejected"| REJECTED
    DECISION -->|"⏱️ Timeout"| EXPIRED

    APPROVED --> EXECUTE
    REJECTED --> LEDGER
    EXPIRED --> LEDGER
    EXECUTE --> LEDGER
    REPLY_ONLY --> LEDGER
    LEDGER --> END
```

---

## 15. Sequence Diagram — Telegram Message to Response

Time-ordered interactions with exact message passing.

```mermaid
sequenceDiagram
    participant Isaiah as Isaiah (Telegram)
    participant TG as Telegram API
    participant Bot as Bot Container<br/>(OpenClaw :18789)
    participant GW as Gateway<br/>(:8080/:8181)
    participant OAI as OpenAI API
    participant Ledger as ledger.db

    Isaiah->>TG: Sends message
    TG->>Bot: Webhook / long-poll delivery
    Note over Bot: Binding: peer 8096968754 → agent:main

    Bot->>GW: POST /credentials/op-proxy<br/>(if fresh secret needed)
    GW-->>Bot: Secret value

    Bot->>OAI: POST /v1/chat/completions<br/>(via HTTP CONNECT proxy :8181)
    Note over GW: Domain check: api.openai.com ✓
    GW->>OAI: TCP tunnel relay
    OAI-->>GW: Streaming response
    GW-->>Bot: Relay response

    Note over Bot: Agent decides: reply + tool call

    Bot->>GW: POST /proxy/mcp/call<br/>{"server": "github", "tool": "get_file_contents", ...}
    Note over GW: MCP inspection:<br/>injection scan → NONE<br/>PII scan → NONE<br/>sensitive op → NONE
    GW->>GW: Audit log (mcp_audit.py)
    GW-->>Bot: {"result": ...}

    Bot->>GW: POST /ingest<br/>{"source": "telegram", "content": "reply text"}
    Note over GW: HMAC auth check\nPII redaction (Presidio)\nRoute to agent
    GW->>Ledger: INSERT INTO ledger<br/>(SHA-256 hash only)
    GW-->>Bot: 200 OK

    Bot->>TG: sendMessage (via HTTP CONNECT proxy)
    TG-->>Isaiah: Message delivered
```

---

## 16. State Machine Diagram — Approval Queue Item Lifecycle

```mermaid
stateDiagram-v2
    [*] --> pending : Bot submits action\nrequiring approval

    pending --> approved : Isaiah sends ✅ approve\nvia Telegram
    pending --> rejected : Isaiah sends ❌ reject\nvia Telegram
    pending --> expired : 1-hour TTL exceeded\n(auto-transition on load)

    approved --> [*] : Action executed\nLedger entry written
    rejected --> [*] : Action blocked\nBot notified
    expired --> [*] : Action blocked\nBot notified

    note right of pending
        Stored in approval_queue.db
        Isaiah receives Telegram notification
        Decision window: 1 hour
    end note

    note right of approved
        Gateway executes the action
        on behalf of bot
    end note
```

---

## 17. State Machine — Bot Session / Context Lifecycle

```mermaid
stateDiagram-v2
    [*] --> fresh : Container starts\nNew session created

    fresh --> active : First message received

    active --> compacting : Token count approaches\nreserveTokensFloor (196K of 200K)

    compacting --> active : Compaction successful\nHistory summarised

    compacting --> reset : Compaction failed\n3 retries exhausted

    active --> reset : Hard context overflow\n(>200K tokens,\nall recovery failed)

    reset --> fresh : New session UUID created\nPrevious session archived\nin agents/main/sessions/

    active --> idle : No messages\n(health monitor active\n300s interval)

    idle --> active : New message received

    note right of compacting
        openclaw auto-compaction
        reserveTokensFloor = 4000
        triggers at ~196K tokens
        leaving 4K buffer for summary
    end note

    note right of reset
        Session JSONL archived
        Bot sends Telegram notification
        Critical jobs may be interrupted
    end note
```
