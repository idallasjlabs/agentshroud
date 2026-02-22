"""
Log Sanitizer - Security Hardening Module
Scrubs PII, credentials, and sensitive data from ALL log output.
"""

import logging
import re
from typing import Any, Dict, Pattern


class LogSanitizer(logging.Filter):
    """Custom logging filter that sanitizes sensitive data from log records."""

    def __init__(self):
        super().__init__()
        self.patterns = self._compile_patterns()

    def _compile_patterns(self) -> Dict[str, Pattern[str]]:
        """Compile regex patterns for sensitive data detection."""
        return {
            # PII Patterns
            "ssn": re.compile(r"\b\d{3}-\d{2}-\d{4}\b|\b\d{9}\b"),
            "credit_card": re.compile(r"\b(?:\d{4}[-\s]?){3}\d{4}\b"),
            "email": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"),
            # API Keys and Tokens
            "openai_key": re.compile(r"\bsk-[A-Za-z0-9]{48}\b"),
            "aws_access_key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
            "github_token": re.compile(r"\bghp_[A-Za-z0-9]{36}\b"),
            "jwt_token": re.compile(
                r"\beyJ[A-Za-z0-9_-]+\.eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+"
            ),
            "api_key_generic": re.compile(
                r'\b[Aa]pi[_-]?[Kk]ey["\s:=]+[A-Za-z0-9+/]{20,}\b'
            ),
            # Credential Patterns in Code/Configs
            "password_assignment": re.compile(
                r'password\s*[:=]\s*["\']?[^"\'\s]{3,}["\']?', re.IGNORECASE
            ),
            "token_assignment": re.compile(
                r'token\s*[:=]\s*["\']?[^"\'\s]{3,}["\']?', re.IGNORECASE
            ),
            "key_assignment": re.compile(
                r'[^_]key\s*[:=]\s*["\']?[^"\'\s]{3,}["\']?', re.IGNORECASE
            ),
            "secret_assignment": re.compile(
                r'secret\s*[:=]\s*["\']?[^"\'\s]{3,}["\']?', re.IGNORECASE
            ),
            # File Paths with Usernames
            "user_paths": re.compile(r"/home/[^/\s]+/", re.IGNORECASE),
            "windows_user_paths": re.compile(r"C:\\Users\\[^\\s]+\\", re.IGNORECASE),
            # 1Password CLI output (op command)
            "op_command_output": re.compile(r"op\s+[^|;\n&]+"),
            "op_vault_content": re.compile(
                r'"[^"]*":\s*"[^"]*"'
            ),  # JSON-like op output
            # Internal structure leakage
            "internal_paths": re.compile(r"/opt/openclaw/[^\s]*"),
            "docker_paths": re.compile(r"/var/lib/docker/[^\s]*"),
            "config_files": re.compile(r"\.env\.[^\s]*|config\.[^\s]*\.json"),
        }

    def filter(self, record: logging.LogRecord) -> bool:
        """Filter log record, sanitizing sensitive content."""
        try:
            # Sanitize the main message
            if hasattr(record, "msg") and record.msg:
                record.msg = self._sanitize_text(str(record.msg))

            # Sanitize arguments if present
            if hasattr(record, "args") and record.args:
                sanitized_args = []
                for arg in record.args:
                    if isinstance(arg, str):
                        sanitized_args.append(self._sanitize_text(arg))
                    else:
                        sanitized_args.append(arg)
                record.args = tuple(sanitized_args)

            # Sanitize exception info if present
            if hasattr(record, "exc_text") and record.exc_text:
                record.exc_text = self._sanitize_text(record.exc_text)

            return True  # Always allow the record through (after sanitization)

        except Exception:
            # If sanitization fails, allow the record through unchanged
            # to avoid breaking logging entirely
            return True

    def _sanitize_text(self, text: str) -> str:
        """Sanitize sensitive data in text."""
        if not text:
            return text

        sanitized = text

        # Apply each pattern
        for pattern_name, pattern in self.patterns.items():
            if pattern_name == "ssn":
                sanitized = pattern.sub("[REDACTED-SSN]", sanitized)
            elif pattern_name == "credit_card":
                sanitized = pattern.sub("[REDACTED-CC]", sanitized)
            elif pattern_name == "email":
                sanitized = pattern.sub("[REDACTED-EMAIL]", sanitized)
            elif "key" in pattern_name or "token" in pattern_name:
                sanitized = pattern.sub("[REDACTED-CREDENTIAL]", sanitized)
            elif pattern_name in ["password_assignment", "secret_assignment"]:
                sanitized = pattern.sub(
                    lambda m: (
                        m.group(0).split(":")[0] + ":[REDACTED]"
                        if ":" in m.group(0)
                        else m.group(0).split("=")[0] + "=[REDACTED]"
                    ),
                    sanitized,
                )
            elif pattern_name == "user_paths":
                sanitized = pattern.sub("/home/[USER]/", sanitized)
            elif pattern_name == "windows_user_paths":
                sanitized = pattern.sub(r"C:\\Users\\[USER]\\", sanitized)
            elif pattern_name == "op_command_output":
                sanitized = pattern.sub("[REDACTED-OP-COMMAND]", sanitized)
            elif pattern_name == "op_vault_content":
                sanitized = pattern.sub("[REDACTED-OP-DATA]", sanitized)
            elif pattern_name in ["internal_paths", "docker_paths", "config_files"]:
                sanitized = pattern.sub("[REDACTED-PATH]", sanitized)

        return sanitized


def install_log_sanitizer():
    """Install the log sanitizer on all existing loggers."""
    sanitizer = LogSanitizer()

    # Add to root logger
    root_logger = logging.getLogger()
    root_logger.addFilter(sanitizer)

    # Add to all existing loggers
    for logger_name in logging.Logger.manager.loggerDict:
        logger = logging.getLogger(logger_name)
        logger.addFilter(sanitizer)

    # Add to any future loggers by patching getLogger
    original_getLogger = logging.getLogger

    def sanitized_getLogger(name=None):
        logger = original_getLogger(name)
        logger.addFilter(sanitizer)
        return logger

    logging.getLogger = sanitized_getLogger


def get_sanitizer_stats() -> Dict[str, Any]:
    """Get statistics about sanitization patterns."""
    return {
        "patterns_count": len(LogSanitizer()._compile_patterns()),
        "pattern_types": list(LogSanitizer()._compile_patterns().keys()),
        "installed": True,
    }
