# SecureClaw Data Flow Diagrams

This document illustrates the flow of data through the SecureClaw system at three levels of detail.

## Level 0: Context Diagram

The highest level view shows SecureClaw as a transparent security gateway between users and OpenClaw AI agents.

```
┌─────────────┐    ┌─────────────────────┐    ┌─────────────┐
│             │    │                     │    │             │
│   External  │───▶│   SecureClaw        │───▶│  OpenClaw   │
│   Users/    │    │   Gateway           │    │  Container  │
│   APIs      │◀───│   (FastAPI)         │◀───│             │
│             │    │                     │    │             │
└─────────────┘    └─────────────────────┘    └─────────────┘
                             │
                             ▼
                   ┌─────────────────────┐
                   │                     │
                   │   External          │
                   │   Resources:        │
                   │   • MCP Servers     │
                   │   • Web/HTTP        │
                   │   • SSH Hosts       │
                   │   • File Systems    │
                   │                     │
                   └─────────────────────┘
```

**Key Components:**
- **External Users/APIs**: HTTP clients, chat interfaces, automation systems
- **SecureClaw Gateway**: Security proxy with audit, filtering, and control
- **OpenClaw Container**: AI agent runtime environment
- **External Resources**: Systems the AI agent needs to access

## Level 1: Security Components

This level shows the key security components within SecureClaw that process and monitor traffic.

```
User Request
     │
     ▼
┌─────────────────────────────────────────────────────────────┐
│  SecureClaw Gateway                                         │
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │
│  │             │  │             │  │             │          │
│  │ PII         │  │ Kill        │  │ Trust       │          │
│  │ Sanitizer   │  │ Switch      │  │ Manager     │          │
│  │             │  │             │  │             │          │
│  └─────────────┘  └─────────────┘  └─────────────┘          │
│         │                 │                 │               │
│         ▼                 ▼                 ▼               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │             Audit Ledger                           │    │
│  │         (Blockchain-style chain)                   │    │
│  └─────────────────────────────────────────────────────┘    │
│         │                                                   │
│         ▼                                                   │
│  ┌─────────────┐                                            │
│  │             │                                            │
│  │ Approval    │                                            │
│  │ Queue       │                                            │
│  │             │                                            │
│  └─────────────┘                                            │
│         │                                                   │
│         ▼                                                   │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │
│  │             │  │             │  │             │          │
│  │ MCP Proxy   │  │ Web Proxy   │  │ DNS Filter  │          │
│  │             │  │             │  │             │          │
│  └─────────────┘  └─────────────┘  └─────────────┘          │
│         │                 │                 │               │
└─────────┼─────────────────┼─────────────────┼───────────────┘
          │                 │                 │
          ▼                 ▼                 ▼
    ┌───────────┐     ┌───────────┐     ┌───────────┐
    │           │     │           │     │           │
    │ MCP       │     │ Web/HTTP  │     │ DNS       │
    │ Servers   │     │ Resources │     │ Resolution│
    │           │     │           │     │           │
    └───────────┘     └───────────┘     └───────────┘
                                              │
                                              ▼
                                    ┌─────────────────┐
                                    │  OpenClaw       │
                                    │  Container      │
                                    └─────────────────┘
```

**Data Flow:**
1. User requests enter the PII Sanitizer first
2. Kill Switch can block all traffic immediately
3. Trust Manager evaluates agent permissions
4. All actions are logged to the Audit Ledger
5. High-risk actions go to Approval Queue
6. Specific proxies handle different resource types
7. DNS Filter prevents malicious domain access

## Level 2: MCP Proxy Detail

This diagram details the flow through the MCP (Model Context Protocol) proxy, which handles AI agent tool calls.

```
Agent Tool Call
     │
     ▼
┌─────────────────────────────────────────────────────────────┐
│  MCP Proxy Detailed Flow                                   │
│                                                             │
│  ┌─────────────┐                                            │
│  │  Tool Call  │  ◀── JSON-RPC request from agent          │
│  │ Inspection  │                                            │
│  └─────────────┘                                            │
│         │                                                   │
│         ▼                                                   │
│  ┌─────────────┐     ┌─────────────────────────────────┐    │
│  │             │────▶│  Parameter Analysis:            │    │
│  │ Permission  │     │  • Check for path traversal    │    │
│  │ Check       │     │  • Validate file paths         │    │
│  │             │     │  • Sanitize shell commands     │    │
│  └─────────────┘     │  • Check URL safety            │    │
│         │             └─────────────────────────────────┘    │
│         ▼                                                   │
│  ┌─────────────┐                                            │
│  │             │  ◀── Per-agent, per-tool limits           │
│  │ Rate Limit  │                                            │
│  │ Check       │                                            │
│  └─────────────┘                                            │
│         │                                                   │
│    ┌────┴────┐                                              │
│    │ BLOCK?  │                                              │
│    └────┬────┘                                              │
│         │                                                   │
│    ┌────▼────┐                                              │
│    │   NO    │                                              │
│    └────┬────┘                                              │
│         ▼                                                   │
│  ┌─────────────┐     ┌─────────────────────────────────┐    │
│  │             │────▶│  Forward to MCP Server:        │    │
│  │ Forward     │     │  • Proxy JSON-RPC call         │    │
│  │ Request     │     │  • Monitor response time       │    │
│  │             │     │  • Handle errors gracefully    │    │
│  └─────────────┘     └─────────────────────────────────┘    │
│         │                                                   │
│         ▼                                                   │
│  ┌─────────────┐     ┌─────────────────────────────────┐    │
│  │             │────▶│  Response Analysis:             │    │
│  │ Result      │     │  • Scan for PII in results     │    │
│  │ Inspection  │     │  • Check for error patterns    │    │
│  │             │     │  • Validate file content       │    │
│  └─────────────┘     │  • Monitor performance         │    │
│         │             └─────────────────────────────────┘    │
│         ▼                                                   │
│  ┌─────────────┐                                            │
│  │             │  ◀── Write to immutable audit chain       │
│  │ Audit Log   │                                            │
│  │ Entry       │                                            │
│  └─────────────┘                                            │
│         │                                                   │
│         ▼                                                   │
│  ┌─────────────┐                                            │
│  │             │  ◀── Send sanitized response to agent     │
│  │ Return      │                                            │
│  │ Response    │                                            │
│  └─────────────┘                                            │
└─────────────────────────────────────────────────────────────┘
         │
         ▼
   Agent receives
   cleaned response
```

**Key Security Checkpoints:**
- **Tool Call Inspection**: Deep analysis of requested operations
- **Permission Check**: Role-based access control per agent
- **Rate Limiting**: Prevents abuse and resource exhaustion
- **Result Inspection**: Ensures safe data return to agent
- **Audit Logging**: Immutable record of all MCP interactions

**Blocked Actions Flow:**
```
   Blocked Action
         │
         ▼
   ┌─────────────┐     ┌─────────────────────────────────┐
   │             │────▶│  Block Reasons:                 │
   │ Generate    │     │  • Permission denied            │
   │ Block       │     │  • Rate limit exceeded         │
   │ Response    │     │  • Malicious pattern detected  │
   │             │     │  • Trust level insufficient    │
   └─────────────┘     └─────────────────────────────────┘
         │
         ▼
   ┌─────────────┐
   │             │
   │ Audit &     │  ◀── Log block with full context
   │ Alert       │
   │             │
   └─────────────┘
         │
         ▼
   Return sanitized
   error to agent
```

This multi-layered approach ensures that every MCP tool call is thoroughly vetted before execution and all results are sanitized before returning to the AI agent.