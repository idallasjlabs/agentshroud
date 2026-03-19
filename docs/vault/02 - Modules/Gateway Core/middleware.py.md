---
title: middleware.py
type: module
file_path: gateway/ingest_api/middleware.py
tags: [middleware, security, p1-hardening, rbac, session-isolation, gateway-core]
related: [Gateway Core/main.py, Gateway Core/models.py, Architecture Overview]
status: documented
---

# middleware.py

## Purpose
Implements the P1 Security Hardening middleware layer for the AgentShroud gateway. Orchestrates over 30 security modules that inspect and optionally modify every inbound request before it reaches the core processing pipeline.

## Responsibilities
- Initialize and wire all P1 security modules on startup (fail-safe: each module failure is logged but does not stop startup)
- Enforce Role-Based Access Control (RBAC) on every request
- Enforce per-user session isolation to prevent cross-user data access
- Run memory security checks (integrity monitoring, lifecycle management)
- Scan for tool result injection attacks
- Filter XML leaks from content
- Strip markdown exfiltration patterns
- Provide a `MiddlewareResult` indicating whether the request is allowed, blocked, or modified
- Expose the `LogSanitizer` for wiring into Python's logging system

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `MiddlewareResult` | dataclass | Result of middleware processing: `allowed`, `reason`, `modified_request` |
| `MiddlewareManager` | class | Orchestrates all P1 security middleware modules |
| `MiddlewareManager.__init__` | method | Initializes every security module; each wrapped in try/except |
| `MiddlewareManager.process_request` | async method | Runs a request through the full middleware chain |
| `MiddlewareManager.set_config` | method | Post-init configuration (called after config is loaded in main.py) |
| `MiddlewareManager.get_log_sanitizer` | method | Returns the `LogSanitizer` instance for wiring into logging handlers |
| `MiddlewareManager._extract_user_id` | method | Extracts `user_id` from request data |
| `MiddlewareManager._check_rbac_permissions` | method | Verifies RBAC permissions for the requesting user |
| `MiddlewareManager._enforce_session_isolation` | method | Enforces per-user workspace isolation |

## Security Modules Initialized

### P1 Core Guards
| Module | Class | Purpose |
|--------|-------|---------|
| `context_guard` | `ContextGuard` | Validates conversation context integrity |
| `metadata_guard` | `MetadataGuard` | Sanitizes and validates request metadata |
| `log_sanitizer` | `LogSanitizer` | Redacts secrets from Python log output |
| `env_guard` | `EnvironmentGuard` | Prevents environment variable exfiltration |
| `git_guard` | `GitGuard` | Blocks git credential and repository access |
| `file_sandbox` | `FileSandbox` | Enforces read/write path restrictions (`/app`, `/tmp`, `/app/data`, `/app/logs`) |
| `resource_guard` | `ResourceGuard` | CPU/memory resource usage limits |
| `session_manager` | `SessionManager` | Session token security |
| `token_validator` | `TokenValidator` | JWT/token validation (audience: `agentshroud-gateway`, issuer: `agentshroud`) |
| `consent_framework` | `ConsentFramework` | User consent tracking for sensitive operations |
| `subagent_monitor` | `SubagentMonitor` | Monitors subagent spawning behavior |
| `agent_registry` | `AgentRegistry` | Tracks registered agent identities |

### Memory Security
| Module | Class | Purpose |
|--------|-------|---------|
| `memory_integrity_monitor` | `MemoryIntegrityMonitor` | Detects unauthorized memory file changes |
| `memory_lifecycle_manager` | `MemoryLifecycleManager` | Manages memory file retention and cleanup |

### Tool Security
| Module | Class | Purpose |
|--------|-------|---------|
| `tool_injection_scanner` | `ToolResultInjectionScanner` | Detects prompt injection in tool results |
| `xml_leak_filter` | `XMLLeakFilter` | Removes XML function call leaks |
| `tool_result_sanitizer` | `ToolResultSanitizer` | PII scanning of tool results (configured via `set_config`) |
| `enhanced_tool_sanitizer` | `EnhancedToolResultSanitizer` | Advanced tool result sanitization |

### Extended v0.8.0 Modules
| Module | Class | Purpose |
|--------|-------|---------|
| `alert_dispatcher` | `AlertDispatcher` | Routes security alerts to log file |
| `approval_hardening` | `ApprovalHardening` | Hardens the approval queue against bypass |
| `browser_security` | `BrowserSecurityGuard` | Browser-originated request security |
| `credential_injector` | `CredentialInjector` | Safe credential injection for agent use |
| `dns_filter` | `DNSFilter` | DNS resolution filtering |
| `drift_detector` | `DriftDetector` | Config drift detection |
| `egress_monitor` | `EgressMonitor` | Tracks outbound connection attempts |
| `key_rotation` | `KeyRotationManager` | Manages cryptographic key rotation |
| `killswitch_monitor` | `KillSwitchMonitor` | Kill switch heartbeat monitoring |
| `multi_turn_tracker` | `MultiTurnTracker` | Tracks multi-turn conversation anomalies |
| `network_validator` | `NetworkValidator` | Docker/container network security |
| `oauth_security` | `OAuthSecurityValidator` | OAuth redirect URI validation |
| `output_canary` | `OutputCanary` | Canary token detection in outputs |
| `path_isolation` | `PathIsolationManager` | File path access isolation |
| `tool_chain_analyzer` | `ToolChainAnalyzer` | Detects suspicious tool call sequences |

## process_request Flow
1. Extract `user_id` from request data — deny if missing
2. RBAC permission check via `_check_rbac_permissions`
3. Session isolation enforcement via `_enforce_session_isolation`
4. Apply session isolation modifications to request if returned
5. Memory integrity registration for write/edit operations
6. (Additional module checks handled by individual guard calls within the method)

**Returns:** `MiddlewareResult(allowed=True/False, reason=str, modified_request=dict|None)`

## FileSandbox Configuration (hardcoded in __init__)
```python
FileSandboxConfig(
    mode="enforce",
    allowed_read_paths=["/app", "/tmp", "/proc/meminfo", "/proc/cpuinfo"],
    allowed_write_paths=["/tmp", "/app/data", "/app/logs"],
)
```

## Environment Variables Used
- None directly — `MemorySecurityConfig.from_env()` may read environment variables for memory security configuration

## Config Keys Read
- None at middleware level directly — `set_config(config)` receives the full `GatewayConfig` and uses it to configure `ToolResultSanitizer`

## Imports From / Exports To
- Imports: 30+ modules from `gateway.security.*`
- Imported by: [[Gateway Core/main.py]] (`MiddlewareManager`)

## Known Issues / Notes
- All module initializations are wrapped in try/except — a failed module logs an error but startup continues. This is fail-open for individual modules; the system does not fail-closed at the middleware level if a security module fails to initialize.
- `owner_user_id = "8096968754"` is hard-coded in `__init__` (the Telegram owner user ID). This should come from configuration.
- `UserSessionManager` is instantiated in both `MiddlewareManager.__init__` and in `main.py`'s `lifespan` — there are two separate instances.
- The `process_request` method is marked async but many of the guard calls may be synchronous internally — verify thread-safety for CPU-bound guards.
- `TokenValidator` is initialized with hardcoded audience/issuer strings (`"agentshroud-gateway"`, `"agentshroud"`) — these are not configurable without a code change.
- The module count (30+) makes initialization order dependencies opaque. If a later module depends on an earlier one that failed silently, the behavior is undefined.

## Related
- [[Gateway Core/main.py]]
- [[Architecture Overview]]
