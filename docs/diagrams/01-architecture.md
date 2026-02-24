# AgentShroud — Architecture Diagrams

> AgentShroud™ is a trademark of Isaiah Jefferson · All rights reserved

---

## 1. C4 Level 0 — Context Diagram (Executive View)

Single-page view of the system as a black box with all external actors.

```mermaid
C4Context
    title AgentShroud — System Context

    Person(isaiah, "Isaiah Jefferson", "Architect / Owner\nSends messages, approves actions,\nreviews audit logs")
    Person_Ext(collaborator, "External Collaborators", "Future: third-party agents\nor human reviewers")

    System(agentshroud, "AgentShroud", "Transparent proxy framework.\nIntercepts, inspects, logs, and\nenforces policy on every AI\nagent action.")

    System_Ext(openai, "OpenAI API", "GPT-4o model inference")
    System_Ext(anthropic, "Anthropic API", "Claude Opus 4 model inference")
    System_Ext(telegram, "Telegram", "Primary messaging channel\n@agentshroud_bot")
    System_Ext(github, "GitHub", "Source control, PRs, CI/CD")
    System_Ext(onepassword, "1Password", "Credential vault\n(service account)")
    System_Ext(brave, "Brave Search API", "Web search for the bot")
    System_Ext(tailscale, "Tailscale", "Encrypted overlay network\nfor remote node access")

    Rel(isaiah, agentshroud, "Sends messages via", "Telegram / iMessage / Web UI")
    Rel(agentshroud, isaiah, "Sends responses & alerts via", "Telegram")
    Rel(agentshroud, openai, "Forwards prompts to", "HTTPS")
    Rel(agentshroud, anthropic, "Forwards prompts to", "HTTPS")
    Rel(agentshroud, telegram, "Sends & receives messages via", "HTTPS")
    Rel(agentshroud, github, "Reads/writes code via", "HTTPS / MCP")
    Rel(agentshroud, onepassword, "Reads secrets from", "HTTPS (op-proxy)")
    Rel(agentshroud, brave, "Searches web via", "HTTPS")
    Rel(agentshroud, tailscale, "SSHes into nodes via", "Tailscale tunnel")
    Rel(collaborator, agentshroud, "Future: submits tasks to", "API")
```

---

## 2. C4 Level 1 — Container Diagram

Internal containers and how they communicate.

```mermaid
C4Container
    title AgentShroud — Container View

    Person(isaiah, "Isaiah Jefferson", "Owner / Operator")

    System_Boundary(agentshroud, "AgentShroud (Docker Compose — macOS host)") {
        Container(gateway, "Gateway", "Python 3.11 / FastAPI", "REST API :8080\nHTTP CONNECT proxy :8181\nOp-proxy endpoint\nAudit ledger\nApproval queue\nPII sanitizer\nSSH proxy\nMCP inspector")

        Container(bot, "AgentShroud Bot", "Node.js 22 / OpenClaw", "Autonomous AI agent :18789\nTelegram channel\niMessage channel\nEmail channel (iCloud)\nCron scheduler\nBrowser control\nMCP server integration")

        ContainerDb(ledger_db, "Ledger DB", "SQLite (aiosqlite)", "Audit trail — SHA-256 hashes only\n90-day retention\nData: ledger.db")

        ContainerDb(approval_db, "Approval DB", "SQLite (aiosqlite)", "Pending human-approval items\nData: approval_queue.db")
    }

    System_Ext(openai, "OpenAI API", "api.openai.com")
    System_Ext(anthropic, "Anthropic API", "api.anthropic.com")
    System_Ext(telegram_api, "Telegram API", "api.telegram.org")
    System_Ext(op, "1Password", "Credential vault")

    Rel(isaiah, bot, "Messages via", "Telegram / iMessage / WebUI")
    Rel(bot, gateway, "All outbound traffic via", "HTTP CONNECT proxy :8181")
    Rel(bot, gateway, "MCP tool calls via", "HTTP :8080/proxy/mcp")
    Rel(bot, gateway, "Reads secrets via", "HTTP :8080/credentials/op-proxy")
    Rel(gateway, ledger_db, "Writes audit entries to", "aiosqlite")
    Rel(gateway, approval_db, "Reads/writes approvals to", "aiosqlite")
    Rel(gateway, op, "Reads secrets from", "HTTPS (service account)")
    Rel(gateway, openai, "Proxies prompts to", "HTTPS via allowlist")
    Rel(gateway, anthropic, "Proxies prompts to", "HTTPS via allowlist")
    Rel(gateway, telegram_api, "Proxies messages to", "HTTPS via allowlist")
```

---

## 3. Architecture Component Diagram — Gateway internals

```mermaid
graph TB
    subgraph Gateway["Gateway Container (FastAPI :8080)"]
        direction TB

        subgraph IngestAPI["Ingest API"]
            AUTH[auth.py\nHMAC/JWT validation]
            ROUTER[router.py\nMulti-agent router]
            SANITIZER[sanitizer.py\nPII redaction\nPresidio / regex]
            LEDGER[ledger.py\nAudit trail\nSHA-256 hashing]
            EVENTBUS[event_bus.py\nAsync event dispatch]
        end

        subgraph ProxyLayer["Proxy Layer"]
            HTTP_PROXY[http_proxy.py\nHTTP CONNECT :8181\nDomain allowlist]
            MCP_PROXY[mcp_proxy.py\nMCP tool call gate]
            MCP_INSPECT[mcp_inspector.py\nInjection + PII scan]
            MCP_AUDIT[mcp_audit.py\nTool call audit log]
            MCP_PERMS[mcp_permissions.py\nPer-tool ACL]
            WEB_PROXY[web_proxy.py\nDomain allowlist engine]
            PIPELINE[pipeline.py\nRequest pipeline orchestrator]
        end

        subgraph ApprovalQ["Approval Queue"]
            QUEUE[queue.py\nIn-memory queue]
            STORE[store.py\nSQLite persistence]
        end

        subgraph SecurityModules["Security Modules (30+)"]
            PROMPT_GUARD[prompt_guard\nPrompt injection]
            EGRESS[egress_filter\negress_monitor]
            DNS[dns_filter\nDNS sinkhole]
            GIT_GUARD[git_guard\nGit op safety]
            FILE_SANDBOX[file_sandbox\nPath traversal]
            TRUST[trust_manager\nTrust levels]
            KEY_VAULT[key_vault\nSecret isolation]
            CANARY[canary\nHoneytokens]
            SUBAGENT[subagent_monitor\nChild agent oversight]
            MORE["...17 more modules"]
        end

        subgraph SSHProxy["SSH Proxy"]
            SSH[ssh_proxy\nApproved hosts only]
        end

        subgraph OpProxy["Op-Proxy (Credential Gateway)"]
            OP[Reads 1Password on\nbehalf of bot container]
        end
    end

    BOT["Bot Container"] -->|"POST /ingest"| AUTH
    BOT -->|"CONNECT host:port"| HTTP_PROXY
    BOT -->|"POST /proxy/mcp/call"| MCP_PROXY
    BOT -->|"POST /credentials/op-proxy"| OP
    BOT -->|"POST /ssh/exec"| SSH

    AUTH --> ROUTER
    ROUTER --> SANITIZER
    SANITIZER --> LEDGER
    SANITIZER --> PIPELINE
    PIPELINE --> QUEUE
    MCP_PROXY --> MCP_INSPECT
    MCP_INSPECT --> MCP_AUDIT
    MCP_AUDIT --> MCP_PERMS
    HTTP_PROXY --> WEB_PROXY
```
