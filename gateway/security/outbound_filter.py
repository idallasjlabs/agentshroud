# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Outbound Information Filter for AgentShroud Gateway

Prevents disclosure of system architecture, infrastructure details,
security configurations, and operational information to users.

This is a hard enforcement layer that runs after the agent generates
a response but before delivery to the user. It complements system
prompt restrictions with deterministic regex-based filtering.
"""
from __future__ import annotations

import logging
import re
import time
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple

logger = logging.getLogger("agentshroud.security.outbound_filter")


class InfoCategory(Enum):
    """Categories of information that may need filtering."""
    INFRASTRUCTURE = "infrastructure"      # hostnames, IPs, URLs, ports
    TOOL_INVENTORY = "tool_inventory"       # MCP tool names, capabilities
    USER_IDENTITY = "user_identity"         # user IDs, usernames, email addresses
    SECURITY_ARCH = "security_architecture" # module names, modes, thresholds
    CREDENTIAL = "credential"              # paths to secrets, token names
    OPERATIONAL = "operational"            # bugs, versions, internal processes
    CODE_BLOCKS = "code_blocks"            # function_calls XML, raw tool invocations
    SAFE = "safe"                          # general knowledge, functional descriptions


@dataclass
class FilterMatch:
    """A single match found by the outbound filter."""
    category: InfoCategory
    pattern_name: str
    matched_text: str
    replacement: str
    start: int
    end: int
    confidence: float = 1.0


@dataclass
class FilterResult:
    """Result of filtering agent response content."""
    original_text: str
    filtered_text: str
    matches: List[FilterMatch]
    risk_level: str  # "clean", "low", "medium", "high"
    redaction_count: int
    categories_found: List[str]
    processing_time_ms: float


class OutboundInfoFilter:
    """Main outbound information filtering engine.
    
    Uses compiled regex patterns to detect and redact sensitive
    system information before delivering agent responses to users.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initialize the outbound information filter.
        
        Args:
            config: Configuration dictionary with:
                - mode: "enforce" (redact) or "monitor" (log only)
                - trust_overrides: per-trust-level disclosure rules
                - additional_patterns: custom patterns to add
        """
        self.config = config or {}
        self.mode = self.config.get("mode", "enforce")
        self.trust_overrides = self.config.get("trust_overrides", {})
        
        # Compile all filter patterns
        self.patterns = self._compile_patterns()
        
        # Add any additional patterns from config
        additional = self.config.get("additional_patterns", [])
        for pattern_def in additional:
            try:
                compiled_pattern = {
                    "name": pattern_def["name"],
                    "regex": re.compile(pattern_def["pattern"], pattern_def.get("flags", 0)),
                    "category": InfoCategory(pattern_def["category"]),
                    "replacement": pattern_def["replacement"]
                }
                self.patterns.append(compiled_pattern)
                logger.info(f"Added custom pattern: {pattern_def['name']}")
            except Exception as e:
                logger.warning(f"Failed to add custom pattern {pattern_def.get('name', '?')}: {e}")
        
        logger.info(f"OutboundInfoFilter initialized: {len(self.patterns)} patterns, mode={self.mode}")

    def _compile_patterns(self) -> List[Dict[str, Any]]:
        """Compile all filter patterns into regex objects."""
        # Base patterns from the remediation specification
        patterns = [
            # Infrastructure patterns
            {
                "name": "tailscale_hostname",
                "pattern": r"\b[a-zA-Z0-9_-]+\.tail[a-f0-9]+\.ts\.net\b",
                "category": InfoCategory.INFRASTRUCTURE,
                "replacement": "[INTERNAL_HOST]",
            },
            {
                "name": "tailnet_id", 
                "pattern": r"\btail[a-f0-9]{6,}\b",
                "category": InfoCategory.INFRASTRUCTURE,
                "replacement": "[TAILNET]",
            },
            {
                "name": "internal_url",
                "pattern": r"https?://(?:raspberrypi|trillian|host\.docker\.internal|localhost|127\.0\.0\.1)[:\d/\w.-]*",
                "category": InfoCategory.INFRASTRUCTURE,
                "replacement": "[INTERNAL_URL]",
            },
            {
                "name": "docker_internal",
                "pattern": r"\bhost\.docker\.internal\b",
                "category": InfoCategory.INFRASTRUCTURE,
                "replacement": "[INTERNAL_HOST]",
            },
            {
                "name": "private_ip",
                "pattern": r"\b(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3})\b",
                "category": InfoCategory.INFRASTRUCTURE,
                "replacement": "[PRIVATE_IP]",
            },
            {
                "name": "port_number_in_url",
                "pattern": r":(8080|8443|3000|5000|9090|6379|5432|3306|27017)\b",
                "category": InfoCategory.INFRASTRUCTURE,
                "replacement": ":[PORT]",
            },

            # Tool inventory patterns - only security-sensitive tools
            {
                "name": "mcp_tool_name",
                "pattern": r"\b(?:exec|cron|sessions_send|subagents|nodes|apply_patch|sessions_list|sessions_history|session_status)\b",
                "category": InfoCategory.TOOL_INVENTORY,
                "replacement": "[TOOL]",
            },
            
            # User identity patterns - Fixed pattern
            {
                "name": "telegram_user_id",
                "pattern": r"(?:user|owner|admin|authorized|telegram)\s+(?:ID\s+)?\d{9,12}\b",
                "category": InfoCategory.USER_IDENTITY,
                "replacement": r"\g<1>[USER_ID]",
                "flags": re.IGNORECASE,
            },

            # Security architecture patterns
            {
                "name": "module_reference",
                "pattern": r"(?:module\s*#?\d{1,2}|(?:PII\s+Sanitizer|Prompt\s+Injection\s+Defense|Egress\s+Filtering|MCP\s+Proxy|Approval\s+Queue|Kill\s+Switch|Progressive\s+Trust|API\s+Key\s+Vault|File\s+I/O\s+Sandboxing))",
                "category": InfoCategory.SECURITY_ARCH,
                "replacement": "[SECURITY_MODULE]",
                "flags": re.IGNORECASE,
            },
            {
                "name": "agentshroud_reference",
                "pattern": r"\bAgentShroud\b",
                "category": InfoCategory.SECURITY_ARCH,
                "replacement": "[SECURITY_SYSTEM]",
            },

            # Credential patterns
            {
                "name": "secret_path",
                "pattern": r"/run/secrets/[a-zA-Z0-9_-]+",
                "category": InfoCategory.CREDENTIAL,
                "replacement": "[SECRET_PATH]",
            },
            {
                "name": "env_var_credential", 
                "pattern": r"\b(?:OP_SERVICE_ACCOUNT_TOKEN|ANTHROPIC_API_KEY|OPENAI_API_KEY|API_KEY|SECRET_KEY|ACCESS_TOKEN)\b",
                "category": InfoCategory.CREDENTIAL,
                "replacement": "[CREDENTIAL_VAR]",
            },

            # Operational patterns
            {
                "name": "source_file_path",
                "pattern": r"(?:/app/agentshroud|/home/[^/]+/\.[^/]+)/[\w/._-]+\.(?:py|js|ts|yaml|yml|json|md)",
                "category": InfoCategory.OPERATIONAL,
                "replacement": "[INTERNAL_PATH]",
            },
            
            # Code block patterns - function_calls XML, tool invocations
            {
                "name": "function_calls_xml",
                "pattern": r"<function_calls>.*?</function_calls>",
                "category": InfoCategory.CODE_BLOCKS,
                "replacement": "[REDACTED_TOOL_CALL]",
                "flags": re.DOTALL,
            },
            {
                "name": "tool_invocation_partial",
                "pattern": r"<invoke[^>]*>.*?</invoke>",
                "category": InfoCategory.CODE_BLOCKS,
                "replacement": "[REDACTED_TOOL_CALL]",
                "flags": re.DOTALL,
            },
        ]
        
        # Compile all patterns
        compiled = []
        for p in patterns:
            try:
                flags = p.get("flags", 0)
                compiled.append({
                    "name": p["name"],
                    "regex": re.compile(p["pattern"], flags),
                    "category": p["category"],
                    "replacement": p["replacement"],
                })
            except re.error as e:
                logger.error(f"Failed to compile pattern {p['name']}: {e}")
                continue
        
        return compiled

    def filter_response(
        self,
        response_text: str,
        user_trust_level: str = "UNTRUSTED",
        source: str = "unknown"
    ) -> FilterResult:
        """Filter agent response for sensitive information disclosure.
        
        Args:
            response_text: The agent's response text to filter
            user_trust_level: Trust level of the requesting user
            source: Source of the request (for logging context)
            
        Returns:
            FilterResult with filtered text and match details
        """
        start_time = time.time()
        
        matches = []
        
        # Find all pattern matches
        for pattern in self.patterns:
            for match in pattern["regex"].finditer(response_text):
                # Check if this category is allowed for the user's trust level
                if self._is_allowed_for_trust(pattern["category"], user_trust_level):
                    continue
                    
                # Special handling for user ID pattern (capture group replacement)
                replacement = pattern["replacement"]
                if pattern["name"] == "telegram_user_id":
                    # Use a simpler replacement for user IDs
                    replacement = re.sub(r"(?:user|owner|admin|authorized|telegram)\s+(?:ID\s+)?", "", match.group(), flags=re.IGNORECASE) 
                    replacement = "[USER_ID]"
                    
                matches.append(FilterMatch(
                    category=pattern["category"],
                    pattern_name=pattern["name"],
                    matched_text=match.group(),
                    replacement=replacement,
                    start=match.start(),
                    end=match.end(),
                ))
        
        # Apply redactions if in enforce mode
        filtered_text = response_text
        if self.mode == "enforce":
            # Apply replacements in reverse order to preserve offsets
            for match in sorted(matches, key=lambda m: m.start, reverse=True):
                filtered_text = (
                    filtered_text[:match.start] + 
                    match.replacement + 
                    filtered_text[match.end:]
                )
        
        # Classify risk level based on match density
        risk_level = self._classify_response_risk(matches)
        
        # Get unique categories found
        categories_found = list({match.category.value for match in matches})
        
        processing_time = (time.time() - start_time) * 1000
        
        result = FilterResult(
            original_text=response_text,
            filtered_text=filtered_text,
            matches=matches,
            risk_level=risk_level,
            redaction_count=len(matches),
            categories_found=categories_found,
            processing_time_ms=processing_time
        )
        
        # Log results
        if matches:
            if self.mode == "enforce":
                logger.warning(
                    f"Outbound filter: {len(matches)} redactions applied "
                    f"(trust={user_trust_level}, risk={risk_level}, source={source})"
                )
            else:
                logger.info(
                    f"Outbound filter: {len(matches)} matches found "
                    f"(monitor mode, trust={user_trust_level}, risk={risk_level}, source={source})"
                )
            
            # Log category breakdown
            category_counts = {}
            for match in matches:
                cat = match.category.value
                category_counts[cat] = category_counts.get(cat, 0) + 1
            
            logger.info(f"Categories: {category_counts}")
        
        return result

    def _is_allowed_for_trust(
        self,
        category: InfoCategory,
        trust_level: str,
    ) -> bool:
        """Check if a disclosure category is permitted for the user's trust level.
        
        Default policy: FULL trust can see security architecture and operational
        details. All other categories are always filtered regardless of trust.
        """
        overrides = self.trust_overrides.get(trust_level, {})
        return overrides.get(category.value, False)

    def _classify_response_risk(self, matches: List[FilterMatch]) -> str:
        """Classify the risk level of a response based on info disclosure density."""
        if len(matches) == 0:
            return "clean"
        if len(matches) <= 2:
            return "low"    # incidental mention
        if len(matches) <= 5:
            return "medium" # possible probing response
        return "high"       # likely architecture disclosure attempt

    def get_stats(self) -> Dict[str, Any]:
        """Get filter statistics."""
        return {
            "mode": self.mode,
            "patterns_loaded": len(self.patterns),
            "trust_overrides": len(self.trust_overrides),
        }