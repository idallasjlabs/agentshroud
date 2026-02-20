# AgentShroud System Architecture Document (SAD)

## Executive Overview

AgentShroud is a transparent security proxy layer designed to provide comprehensive protection for OpenClaw AI agents without requiring modifications to the agent codebase. Operating as a FastAPI gateway, AgentShroud intercepts all external communications, applies security controls, and maintains detailed audit trails while preserving the agent's functionality and user experience.

The system implements a defense-in-depth strategy with 26 security modules operating across 7 distinct layers, from network isolation to application-level content filtering. AgentShroud's design philosophy centers on "default-allow with comprehensive logging" - enabling agent functionality while capturing threats for analysis and progressive enforcement.

Key capabilities include:
- **Transparent Proxy**: Zero modification required for existing OpenClaw deployments
- **Multi-Protocol Security**: HTTP/HTTPS, SSH, MCP, DNS filtering with protocol-aware inspection
- **Advanced PII Detection**: Microsoft Presidio integration with custom regex patterns
- **Immutable Audit Trail**: SHA-256 hash chain ensuring tamper-evident logging
- **Progressive Trust Model**: Dynamic security controls based on agent behavior and trust levels
- **Zero-Config Deployment**: `docker-compose up` achieves full security posture

## System Context

AgentShroud serves as a security enforcement point positioned between external networks and OpenClaw agent containers. The system architecture follows a two-network isolation model where external traffic flows through AgentShroud's security controls before reaching the protected OpenClaw environment.

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   External      │    │   AgentShroud    │    │    OpenClaw     │
│   Networks      │◄──►│   Security      │◄──►│    Agent        │
│                 │    │   Gateway       │    │   Container     │
│ • Users/APIs    │    │                 │    │                 │
│ • Third Parties │    │ • Authentication│    │ • Agent Core    │
│ • Service Mesh  │    │ • PII Filtering │    │ • Tools/Skills  │
│                 │    │ • Audit Trail   │    │ • Memory Store  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
        │                        │                        │
        └─ External Network ─────┴─ Internal Network ─────┘
        (agentshroud_external)        (agentshroud_internal)
```

## Component Architecture

### Core Components

#### 1. Gateway (FastAPI)
**Location**: `agentshroud/gateway/`  
**Purpose**: Primary ingress point handling HTTP/HTTPS traffic routing

The Gateway component serves as the main entry point for all HTTP-based communications. Built on FastAPI, it provides:
- Asynchronous request processing with uvicorn ASGI server
- OpenAPI specification generation for API documentation
- WebSocket support for real-time dashboard connections
- Request/response middleware integration for security modules

#### 2. PII Sanitizer (Presidio + Regex)
**Location**: `agentshroud/pii/`  
**Purpose**: Detection and redaction of personally identifiable information

Combines Microsoft Presidio's ML-based entity recognition with custom regex patterns:
- **Presidio Integration**: Detects names, addresses, phone numbers, emails using spaCy models
- **Custom Patterns**: Credit cards, SSNs, API keys, cryptocurrency addresses
- **Contextual Analysis**: Reduces false positives through context-aware scoring
- **Redaction Modes**: Replace, mask, hash, or log-only based on sensitivity levels

#### 3. Audit Ledger (SHA-256 Hash Chain)
**Location**: `agentshroud/audit/`  
**Purpose**: Tamper-evident logging with cryptographic integrity

Implements blockchain-inspired hash chaining for audit integrity:
```
Genesis Block: hash(timestamp + "GENESIS" + initial_seed)
Block N: hash(prev_hash + timestamp + event_data + nonce)
Chain Verification: Validate each block's hash against predecessor
```

Key features:
- **Immutable History**: Each entry cryptographically linked to previous
- **Integrity Verification**: Detect tampering attempts through chain validation
- **Event Correlation**: Link related security events across time
- **Compliance Support**: Structured logging for IEC 62443 and NIST frameworks

#### 4. Approval Queue (SQLite)
**Location**: `agentshroud/approval/`  
**Purpose**: Human-in-the-loop security decision management

SQLite-based workflow engine supporting:
- **Risk-Based Queuing**: Automatic escalation based on threat scores
- **Multi-Stage Approval**: Sequential approval workflows for high-risk operations
- **Time-Bound Decisions**: Automatic approval/denial after configurable timeouts
- **Approval Context**: Full request context preservation for informed decisions

#### 5. Kill Switch (3 Modes)
**Location**: `agentshroud/killswitch/`  
**Purpose**: Emergency response and threat containment

Three operational modes:
- **Monitor**: Log threats without blocking (default behavior)
- **Block**: Prevent specific threat patterns from reaching agents
- **Isolate**: Complete network isolation, emergency stop of agent operations

Mode transitions support automated threat response and manual intervention.

#### 6. SSH Proxy
**Location**: `agentshroud/ssh/`  
**Purpose**: Secure shell connection proxying with session recording

Features:
- **Protocol Inspection**: Command logging and pattern analysis
- **Session Recording**: Full terminal session capture for audit
- **Key Management**: SSH key rotation and certificate-based authentication
- **Privilege Escalation Detection**: Monitor for suspicious privilege changes

#### 7. MCP Proxy (Model Context Protocol)
**Location**: `agentshroud/mcp/`  
**Purpose**: Tool and skill invocation security with capability-based access control

MCP-specific security controls:
- **Tool Authorization**: Per-tool permission matrix based on agent trust levels
- **Parameter Validation**: Input sanitization for tool parameters
- **Capability Sandboxing**: Restrict tool execution scope based on security policies
- **Tool Chain Analysis**: Detect suspicious tool usage patterns

#### 8. Web Proxy
**Location**: `agentshroud/web/`  
**Purpose**: HTTP/HTTPS traffic inspection and filtering

Advanced web security features:
- **URL Analysis**: Machine learning-based malicious URL detection
- **Content Filtering**: Response body inspection for data exfiltration attempts
- **Certificate Validation**: TLS certificate pinning and validation
- **Rate Limiting**: Adaptive rate limiting based on request patterns

#### 9. DNS Filter
**Location**: `agentshroud/dns/`  
**Purpose**: DNS-based threat prevention and data exfiltration detection

DNS security capabilities:
- **Threat Intelligence**: Real-time DNS threat feed integration
- **Exfiltration Detection**: Statistical analysis of DNS query patterns
- **Custom Blocklists**: Domain and subdomain filtering rules
- **DNS-over-HTTPS**: Secure DNS resolution with logging

#### 10. Dashboard (WebSocket)
**Location**: `agentshroud/dashboard/`  
**Purpose**: Real-time security monitoring and control interface

Web-based dashboard providing:
- **Real-Time Monitoring**: Live security event streams via WebSocket
- **Threat Visualization**: Security metrics and trend analysis
- **Control Interface**: Kill switch controls and approval queue management
- **Agent Status**: Trust level progression and agent health monitoring

#### 11. Trust Manager
**Location**: `agentshroud/trust/`  
**Purpose**: Dynamic trust level calculation and policy enforcement

Trust-based security model:
- **Behavioral Analysis**: Agent action patterns and anomaly detection
- **Trust Scoring**: Mathematical model for trust level calculation
- **Policy Enforcement**: Dynamic security control adjustment based on trust
- **Trust Persistence**: Long-term trust relationship management

#### 12. Egress Monitor
**Location**: `agentshroud/egress/`  
**Purpose**: Outbound traffic analysis and data loss prevention

Egress security controls:
- **Data Classification**: Automatic classification of outbound data
- **Exfiltration Detection**: Pattern matching for sensitive data egress
- **Bandwidth Analysis**: Unusual traffic volume detection
- **Destination Analysis**: Reputation and risk assessment of target hosts

## Two-Network Docker Architecture

AgentShroud implements strict network isolation using Docker's custom bridge networks:

```
┌─────────────────────────────────────────────────────────────────┐
│                     Docker Host                                 │
│                                                                 │
│  ┌─ External Network (agentshroud_external) ─┐                  │
│  │                                          │                  │
│  │  ┌─────────────────┐    ┌──────────────┐ │                  │
│  │  │  AgentShroud     │    │   Ingress    │ │                  │
│  │  │   Gateway       │◄──►│   Proxy      │ │                  │
│  │  │  (Port 8080)    │    │ (Port 80/443)│ │                  │
│  │  └─────────────────┘    └──────────────┘ │                  │
│  └─────────────────┬────────────────────────┘                  │
│                    │                                            │
│  ┌─ Internal Network (agentshroud_internal) ─┐                  │
│  │                 │                        │                  │
│  │  ┌─────────────────┐    ┌──────────────┐ │                  │
│  │  │  AgentShroud     │    │   OpenClaw   │ │                  │
│  │  │   Gateway       │◄──►│    Agent     │ │                  │
│  │  │ (Internal Only) │    │   Container  │ │                  │
│  │  └─────────────────┘    └──────────────┘ │                  │
│  └─────────────────────────────────────────┘                  │
└─────────────────────────────────────────────────────────────────┘
```

### Network Isolation Benefits:

1. **Attack Surface Reduction**: OpenClaw containers have no direct external exposure
2. **Traffic Inspection**: All communication flows through AgentShroud security controls
3. **Lateral Movement Prevention**: Compromised containers cannot access external networks
4. **Policy Enforcement**: Network-level controls complement application-layer security

## Technology Stack

### Core Technologies
- **Runtime**: Python 3.11 with asyncio for high-performance concurrent processing
- **Web Framework**: FastAPI with automatic OpenAPI documentation generation
- **Database**: SQLite with WAL mode for audit persistence and approval queues
- **Containerization**: Multi-runtime support (Docker, Podman, Apple Containers)
- **Networking**: Docker Compose custom bridge networks for isolation

### Security Technologies
- **NLP Processing**: spaCy 3.7+ with transformer models for entity recognition
- **PII Detection**: Microsoft Presidio 2.2+ with custom analyzer extensions
- **Cryptography**: Python cryptography library with AES-256-GCM and SHA-256
- **Protocol Handling**: asyncssh for SSH proxying, aiohttp for HTTP client operations

### Monitoring and Observability
- **Metrics**: Prometheus-compatible metrics export
- **Logging**: Structured JSON logging with correlation IDs
- **Tracing**: OpenTelemetry integration for distributed tracing
- **Health Checks**: Docker HEALTHCHECK and liveness probes

## System Traffic Flow

```
External Request Flow:

   ┌─────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
   │  User/  │───►│   Ingress   │───►│  Security   │───►│  OpenClaw   │
   │   API   │    │   Proxy     │    │  Gateway    │    │   Agent     │
   └─────────┘    └─────────────┘    └─────────────┘    └─────────────┘
        │                │                 │                 │
        │        ┌───────▼───────┐ ┌───────▼───────┐         │
        │        │  TLS Termination│ │ Authentication│         │
        │        │  Rate Limiting  │ │ Authorization │         │
        │        └─────────────────┘ └─────────────────┘       │
        │                               │                     │
        │        ┌─────────────────────────▼─────────────┐     │
        │        │        Security Module Chain           │     │
        │        │                                       │     │
        │        │  ┌─────────┐  ┌─────────┐  ┌─────────┐│     │
        │        │  │   PII   │  │  Audit  │  │  Trust  ││     │
        │        │  │Sanitizer│─►│ Logger  │─►│Manager ││     │
        │        │  └─────────┘  └─────────┘  └─────────┘│     │
        │        │                                       │     │
        │        │  ┌─────────┐  ┌─────────┐  ┌─────────┐│     │
        │        │  │ Threat  │  │Approval │  │  Kill   ││     │
        │        │  │Detector │─►│ Queue   │─►│ Switch  ││     │
        │        │  └─────────┘  └─────────┘  └─────────┘│     │
        │        └─────────────────────────────────────────┘     │
        │                               │                     │
        └─── Response Path ◄────────────┴────── Request ──────┘
                     │                           Forward
              ┌──────▼──────┐
              │   Response  │
              │ Post-Process│
              │ • Sanitize  │
              │ • Audit Log │
              │ • Metrics   │
              └─────────────┘
```

This architecture ensures comprehensive security coverage while maintaining transparency to both users and OpenClaw agents, enabling robust threat detection and prevention without impacting agent functionality.