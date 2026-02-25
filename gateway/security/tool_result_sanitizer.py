# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tool Result PII Sanitizer

Wraps the existing PIISanitizer for tool-result-specific scanning with:
- Per-tool configuration overrides
- Audit logging for redacted content
- Tool-specific risk thresholds
"""
from __future__ import annotations

import logging
from typing import Dict, Any, Optional

from gateway.ingest_api.sanitizer import PIISanitizer
from gateway.ingest_api.models import RedactionResult
from gateway.ingest_api.config import PIIConfig

logger = logging.getLogger("agentshroud.gateway.tool_result_sanitizer")


class ToolResultPIIConfig:
    """PII configuration with per-tool overrides"""
    
    def __init__(
        self,
        enabled: bool = True,
        default_config: Optional[PIIConfig] = None,
        tool_overrides: Optional[Dict[str, Dict[str, Any]]] = None
    ):
        self.enabled = enabled
        self.default_config = default_config or PIIConfig()
        self.tool_overrides = tool_overrides or {}
        
    def get_config_for_tool(self, tool_name: str) -> PIIConfig:
        """Get PII config for a specific tool, applying overrides if configured"""
        if tool_name not in self.tool_overrides:
            return self.default_config
            
        # Create a copy of default config and apply overrides
        config_dict = self.default_config.model_dump()
        overrides = self.tool_overrides[tool_name]
        
        # Apply overrides
        for key, value in overrides.items():
            if key in config_dict:
                config_dict[key] = value
                
        return PIIConfig(**config_dict)


class ToolResultSanitizer:
    """Tool result PII sanitizer with per-tool configuration"""
    
    def __init__(self, config: ToolResultPIIConfig):
        self.config = config
        self._sanitizers: Dict[str, PIISanitizer] = {}
        
    def _get_sanitizer_for_tool(self, tool_name: str) -> PIISanitizer:
        """Get or create a PIISanitizer instance for the specified tool"""
        if tool_name not in self._sanitizers:
            tool_config = self.config.get_config_for_tool(tool_name)
            self._sanitizers[tool_name] = PIISanitizer(
                config=tool_config,
                mode="enforce",
                action="redact"
            )
        return self._sanitizers[tool_name]
        
    async def sanitize_tool_result(
        self,
        tool_name: str,
        tool_result: Any,
        session_id: Optional[str] = None
    ) -> tuple[Any, RedactionResult]:
        """Sanitize a tool result for PII before it reaches the agent
        
        Args:
            tool_name: Name of the tool that produced the result
            tool_result: The raw tool result (could be string, dict, list, etc.)
            session_id: Optional session ID for audit logging
            
        Returns:
            Tuple of (sanitized_result, redaction_details)
        """
        if not self.config.enabled:
            return tool_result, RedactionResult(
                sanitized_content=str(tool_result),
                redactions=[],
                entity_types_found=[]
            )
            
        sanitizer = self._get_sanitizer_for_tool(tool_name)
        
        # Convert tool result to string for PII scanning
        content = self._extract_scannable_content(tool_result)
        
        if not content.strip():
            return tool_result, RedactionResult(
                sanitized_content=content,
                redactions=[],
                entity_types_found=[]
            )
            
        # Perform PII sanitization
        redaction_result = await sanitizer.sanitize(content)
        
        # Log redactions for audit trail (without logging the actual PII)
        if redaction_result.redactions:
            self._log_redaction_audit(
                tool_name=tool_name,
                session_id=session_id,
                entity_types=redaction_result.entity_types_found,
                redaction_count=len(redaction_result.redactions)
            )
            
        # Reconstruct the result with sanitized content
        sanitized_result = self._reconstruct_result(
            original_result=tool_result,
            original_content=content,
            sanitized_content=redaction_result.sanitized_content
        )
        
        return sanitized_result, redaction_result
        
    def _extract_scannable_content(self, tool_result: Any) -> str:
        """Extract text content from various tool result formats for PII scanning"""
        if isinstance(tool_result, str):
            return tool_result
        elif isinstance(tool_result, dict):
            # For dict results, scan all string values recursively
            return self._extract_dict_content(tool_result)
        elif isinstance(tool_result, (list, tuple)):
            # For list/tuple results, scan all items
            return "\n".join(self._extract_scannable_content(item) for item in tool_result)
        else:
            # Convert other types to string
            return str(tool_result)
            
    def _extract_dict_content(self, data: Dict[str, Any], prefix: str = "") -> str:
        """Recursively extract string content from dictionary"""
        content_parts = []
        
        for key, value in data.items():
            if isinstance(value, str):
                content_parts.append(value)
            elif isinstance(value, dict):
                nested_content = self._extract_dict_content(value, f"{prefix}{key}.")
                if nested_content:
                    content_parts.append(nested_content)
            elif isinstance(value, (list, tuple)):
                for item in value:
                    if isinstance(item, str):
                        content_parts.append(item)
                    elif isinstance(item, dict):
                        nested_content = self._extract_dict_content(item, f"{prefix}{key}[]." )
                        if nested_content:
                            content_parts.append(nested_content)
            else:
                str_value = str(value)
                if str_value and str_value != "None":
                    content_parts.append(str_value)
                    
        return "\n".join(content_parts)
        
    def _reconstruct_result(
        self,
        original_result: Any,
        original_content: str,
        sanitized_content: str
    ) -> Any:
        """Reconstruct the tool result with sanitized content"""
        # If content unchanged, return original
        if original_content == sanitized_content:
            return original_result
            
        # For simple string results, return sanitized content directly
        if isinstance(original_result, str):
            return sanitized_content
            
        # For complex structures, we need to be more careful
        # For now, return a simplified string representation with a note
        if isinstance(original_result, dict):
            return {
                "sanitized_result": sanitized_content,
                "original_type": "dict",
                "pii_redacted": True,
                "note": "Original structured data contained PII and has been sanitized"
            }
        elif isinstance(original_result, (list, tuple)):
            return {
                "sanitized_result": sanitized_content,
                "original_type": type(original_result).__name__,
                "pii_redacted": True,
                "note": "Original list/tuple data contained PII and has been sanitized"
            }
        else:
            return sanitized_content
            
    def _log_redaction_audit(
        self,
        tool_name: str,
        session_id: Optional[str],
        entity_types: list[str],
        redaction_count: int
    ):
        """Log PII redaction for audit trail without logging actual PII"""
        logger.info(
            f"PII redacted from tool result: tool={tool_name} session={session_id or 'unknown'} "
            f"entities=[{', '.join(entity_types)}] count={redaction_count}"
        )
        
    def get_supported_tools(self) -> list[str]:
        """Get list of tools with specific PII configurations"""
        return list(self.config.tool_overrides.keys())
        
    def get_tool_config(self, tool_name: str) -> PIIConfig:
        """Get the PII configuration for a specific tool"""
        return self.config.get_config_for_tool(tool_name)
