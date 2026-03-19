---
title: log_sanitizer.py
type: module
file_path: gateway/security/log_sanitizer.py
tags: [security, logging, pii-redaction, credential-scrubbing, data-protection]
related: [[key_vault.py]], [[egress_monitor.py]], [[session_security.py]]
status: documented
---

# log_sanitizer.py

## Purpose
Implements a `logging.Filter` subclass that intercepts all Python log records and scrubs personally identifiable information (PII), API credentials, and internal path details before they are written to any log sink.

## Threat Model
Prevents sensitive data from being inadvertently persisted in log files or transmitted to log aggregation backends. Log exfiltration is a common secondary pivot after initial compromise; this module ensures that even if logs are accessed, they contain no actionable credentials, PII, or structural intelligence about the gateway internals.

## Responsibilities
- Compile regex patterns for a broad taxonomy of sensitive data types
- Hook into Python's logging system as a `logging.Filter`
- Sanitize log message text, format arguments, and exception info in every log record
- Apply to the root logger and all existing loggers at install time
- Monkey-patch `logging.getLogger` to automatically attach the sanitizer to future loggers
- Provide a stats function for inspection of active patterns

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `LogSanitizer` | Class | `logging.Filter` subclass; compiles patterns and sanitizes records |
| `LogSanitizer.filter` | Method | Called by the logging framework; sanitizes msg, args, and exc_text fields |
| `LogSanitizer._sanitize_text` | Method | Applies all compiled patterns to a string; returns the redacted string |
| `LogSanitizer._compile_patterns` | Method | Builds and returns the pattern dictionary |
| `install_log_sanitizer` | Function | Installs the sanitizer on all loggers and patches `logging.getLogger` |
| `get_sanitizer_stats` | Function | Returns metadata about the number and names of active patterns |

## Function Details

### LogSanitizer.filter(record)
**Purpose:** Intercepts log records. Sanitizes `record.msg`, each string element of `record.args`, and `record.exc_text`. Always returns `True` (records are emitted after scrubbing, never suppressed).
**Parameters:** `record` — `logging.LogRecord`
**Returns:** `bool` (always `True`)

### LogSanitizer._sanitize_text(text)
**Purpose:** Iterates over all compiled patterns, substituting matched content with a pattern-appropriate redaction token.
**Parameters:** `text` — `str`
**Returns:** Sanitized `str`

### install_log_sanitizer()
**Purpose:** Attaches a shared `LogSanitizer` instance to the root logger, all currently registered loggers, and patches `logging.getLogger` to auto-attach the sanitizer to any logger created after installation.
**Returns:** `None`

### get_sanitizer_stats()
**Purpose:** Returns a dict describing the current sanitizer configuration (pattern count, pattern names, installation status). Useful for health checks and debugging.
**Returns:** `dict`

## Pattern Taxonomy

| Pattern Name | Matches | Replacement |
|---|---|---|
| `ssn` | US SSNs (dashed and bare 9-digit) | `[REDACTED-SSN]` |
| `credit_card` | 16-digit card numbers | `[REDACTED-CC]` |
| `email` | Email addresses | `[REDACTED-EMAIL]` |
| `openai_key` | `sk-` prefixed 48-char keys | `[REDACTED-CREDENTIAL]` |
| `aws_access_key` | `AKIA` + 16 uppercase alphanum | `[REDACTED-CREDENTIAL]` |
| `github_token` | `ghp_` + 36 alphanum | `[REDACTED-CREDENTIAL]` |
| `jwt_token` | JWT `eyJ...eyJ...` three-part tokens | `[REDACTED-CREDENTIAL]` |
| `api_key_generic` | `api_key = <value>` patterns | `[REDACTED-CREDENTIAL]` |
| `password_assignment` | `password: <value>` or `password = <value>` | Preserves key, redacts value |
| `token_assignment` | `token: <value>` or `token = <value>` | Preserves key, redacts value |
| `secret_assignment` | `secret: <value>` or `secret = <value>` | Preserves key, redacts value |
| `user_paths` | `/home/<username>/` | `/home/[USER]/` |
| `windows_user_paths` | `C:\Users\<username>\` | `C:\Users\[USER]\` |
| `op_command_output` | `op <args>` (1Password CLI) | `[REDACTED-OP-COMMAND]` |
| `op_vault_content` | JSON-like `"key": "value"` (op output) | `[REDACTED-OP-DATA]` |
| `internal_paths` | `/opt/openclaw/*` | `[REDACTED-PATH]` |
| `docker_paths` | `/var/lib/docker/*` | `[REDACTED-PATH]` |
| `config_files` | `.env.*` or `config.*.json` | `[REDACTED-PATH]` |

## Configuration / Environment Variables
- No environment variables; installed programmatically via `install_log_sanitizer()`
- Installation is idempotent if called multiple times (multiple filters attached)

## Related
- [[key_vault.py]]
- [[egress_monitor.py]]
- [[session_security.py]]
