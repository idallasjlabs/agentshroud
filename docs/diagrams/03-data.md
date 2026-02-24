# AgentShroud — Data Diagrams

> AgentShroud™ is a trademark of Isaiah Jefferson · All rights reserved

---

## 7. Data Flow Diagram — How Data Moves Through the System

```mermaid
flowchart TD
    subgraph Sources["Input Channels"]
        TG_IN["Telegram\n@agentshroud_bot"]
        IMSG["iMessage\n(imsg-ssh bridge)"]
        WEB["Web UI\nlocalhost:18790"]
        CRON["Cron Scheduler\n8 scheduled jobs"]
    end

    subgraph Bot["Bot Container (OpenClaw)"]
        BOT_RECV["Receive message\n/ cron trigger"]
        BOT_THINK["LLM inference\n(OpenAI / Anthropic)"]
        BOT_ACT["Execute action\n(tool call / reply)"]
    end

    subgraph Gateway["Gateway Container"]
        PII["PII Sanitizer\nPresidio · regex\nSSN · CC · Email · Phone"]
        AUDIT["Audit Ledger\nSHA-256 hash only\nNever stores raw content"]
        APPROVAL["Approval Queue\nHuman gate for\ndangerous actions"]
        MCP_GATE["MCP Inspector\nInjection scan\nPII leak · Sensitive op"]
        PROXY["HTTP CONNECT Proxy\nDomain allowlist\nDefault-deny egress"]
    end

    subgraph Stores["Persistent Storage"]
        LEDGER_DB[("ledger.db\nAudit trail · 90-day TTL")]
        APPROVAL_DB[("approval_queue.db\nPending approvals")]
        BOT_CONFIG[("agentshroud-config volume\nopenclaw.json · Sessions · Cron")]
    end

    subgraph Egress["External Services (Allowlisted)"]
        OAI["OpenAI API"]
        ANTH["Anthropic API"]
        TG_OUT["Telegram API"]
        GH["GitHub API"]
        OP["1Password\n(op-proxy)"]
    end

    TG_IN --> BOT_RECV
    IMSG --> BOT_RECV
    WEB --> BOT_RECV
    CRON --> BOT_RECV

    BOT_RECV --> BOT_THINK
    BOT_THINK -->|"Tool call"| MCP_GATE
    BOT_THINK -->|"HTTP request"| PROXY
    BOT_THINK --> BOT_ACT
    BOT_ACT -->|"POST /ingest"| PII

    PII -->|"Sanitized content (hash)"| AUDIT
    AUDIT --> LEDGER_DB
    PII -->|"Flagged action"| APPROVAL
    APPROVAL --> APPROVAL_DB
    APPROVAL -->|"Awaiting human decision"| TG_OUT

    MCP_GATE -->|"Approved"| PROXY
    MCP_GATE -->|"Blocked (HIGH threat)"| AUDIT

    PROXY -->|"HTTPS"| OAI
    PROXY -->|"HTTPS"| ANTH
    PROXY -->|"HTTPS"| TG_OUT
    PROXY -->|"HTTPS"| GH
    PROXY -->|"HTTPS"| OP

    BOT_CONFIG -.->|"read on startup"| Bot
```

---

## 8. Entity Relationship Diagram (ERD)

```mermaid
erDiagram
    LEDGER {
        TEXT id PK "UUID"
        TEXT timestamp "ISO 8601 UTC"
        TEXT source "shortcut | browser | telegram | etc"
        TEXT content_hash "SHA-256 of sanitized content"
        TEXT original_content_hash "SHA-256 of raw content"
        INTEGER sanitized "0 or 1"
        INTEGER size "byte length"
        INTEGER redaction_count
        TEXT redaction_types "JSON array of entity types"
        TEXT forwarded_to "target agent name"
        TEXT content_type "text | url | photo | file"
        TEXT metadata "JSON object"
        TEXT created_at "ISO 8601 UTC"
        TEXT expires_at "ISO 8601 UTC (90-day TTL)"
    }

    SCHEMA_VERSION {
        INTEGER version PK
        TEXT applied_at "ISO 8601 UTC"
    }

    APPROVAL_ITEMS {
        TEXT request_id PK "UUID"
        TEXT action_type "email_sending | file_deletion | etc"
        TEXT description "Human-readable description"
        TEXT details "JSON object — action parameters"
        TEXT agent_id "Requesting agent"
        TEXT submitted_at "ISO 8601 UTC"
        TEXT expires_at "ISO 8601 UTC (1-hour TTL)"
        TEXT status "pending | approved | rejected | expired"
        TEXT decided_at "ISO 8601 UTC — nullable"
        TEXT reason "Decision reason — nullable"
    }

    LEDGER ||--o{ APPROVAL_ITEMS : "action may generate"
```

---

## 9. Data Lineage Diagram

End-to-end traceability from source to consumption.

```mermaid
flowchart LR
    subgraph L1["Layer 1 — Source"]
        SRC1["Telegram message\n(raw user text)"]
        SRC2["iMessage\n(raw user text)"]
        SRC3["Cron trigger\n(no user content)"]
    end

    subgraph L2["Layer 2 — Ingestion (Gateway)"]
        HASH1["original_content_hash\nSHA-256(raw)"]
        REDACT["PII Redaction\n[PHONE] [EMAIL] [SSN]\n→ placeholders only"]
        HASH2["content_hash\nSHA-256(sanitized)"]
    end

    subgraph L3["Layer 3 — Persistence (ledger.db)"]
        LEDGER_ROW["ledger row\ncontent_hash · original_hash\nsanitized · redaction_count\nexpires_at = now+90d"]
    end

    subgraph L4["Layer 4 — Processing (Bot)"]
        LLM["LLM API call\n(sanitized text only)"]
        TOOL["Tool call\n(MCP-inspected)"]
    end

    subgraph L5["Layer 5 — Consumption"]
        RESP["Response to user\n(Telegram / iMessage)"]
        AUDIT_VIEW["Audit query\nGET /ledger\n(hashes only, never raw)"]
        RETENTION["Auto-delete\nat expires_at"]
    end

    SRC1 --> HASH1
    SRC2 --> HASH1
    SRC3 --> HASH2
    HASH1 --> REDACT
    REDACT --> HASH2
    HASH1 --> LEDGER_ROW
    HASH2 --> LEDGER_ROW
    REDACT --> LEDGER_ROW
    LEDGER_ROW --> LLM
    LLM --> TOOL
    LLM --> RESP
    LEDGER_ROW --> AUDIT_VIEW
    LEDGER_ROW --> RETENTION
```

---

## 10. Data Dictionary / Catalog Map

```mermaid
mindmap
  root((AgentShroud\nData Assets))
    SQLite DBs
      ledger.db
        ledger table
          SHA-256 hashes only
          90-day TTL
          Indexed on timestamp, source, forwarded_to
        schema_version table
      approval_queue.db
        approval_items table
          1-hour TTL for pending items
          States: pending, approved, rejected, expired
    OpenClaw Volume
      agentshroud-config
        openclaw.json
          agents.list
          bindings
          channels config
          compaction settings
        agents/main/sessions/
          Session JSONL files
          Auto-compacted at 196K tokens
        cron/jobs.json
          8 scheduled jobs
        workspace/
          BRAND.md
          IDENTITY.md
          AGENTS.md
    Ephemeral/Transient
      PII redaction result
        Never persisted raw
        Hash only in ledger
      MCP inspection result
        In-memory only
        Logged to gateway stdout
      Approval queue in-memory
        Backed by SQLite
    External Credentials
      1Password vault
        AgentShroud Bot Credentials
          OpenAI API key
          Anthropic OAuth token
          Brave Search API key
          iCloud app-specific password
          Gateway password
```
