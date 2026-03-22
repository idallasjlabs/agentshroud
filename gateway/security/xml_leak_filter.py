# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
XML Leak Filter — prevent sensitive XML and path information from leaking in responses.

This filter removes function call XML, file paths, and other sensitive information
that could expose system internals or enable further attacks.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class FilterResult:
    """Result from XML leak filtering."""
    filtered_content: str
    removed_items: List[str]
    filter_applied: bool


# C32: Command / code injection patterns for outbound text scanning
_COMMAND_INJECTION_PATTERNS: list[re.Pattern] = [
    # Shell metacharacters in execution context
    re.compile(r'(?:^|[^\\])[;&|`]\s*(?:rm|cp|mv|cat|chmod|wget|curl|bash|sh|python|node)\b', re.IGNORECASE | re.MULTILINE),
    # SQL injection signatures
    re.compile(r"(?:'\s*OR\s*'?1'?\s*=\s*'?1|UNION\s+(?:ALL\s+)?SELECT|DROP\s+TABLE\s+\w+|INSERT\s+INTO\s+\w+\s+VALUES)", re.IGNORECASE),
    # Python eval/exec/import injection
    re.compile(r'\b(?:eval|exec)\s*\(|__import__\s*\(', re.IGNORECASE),
    # Node.js child_process / require injection
    re.compile(r"""require\s*\(\s*['"]child_process['"]\s*\)|process\.exec\s*\("""),
]


class XMLLeakFilter:
    """Filter to remove sensitive XML and path information from outbound responses."""

    def __init__(self):
        """Initialize the filter with predefined patterns."""
        # Function call XML patterns
        func_calls = "function_calls"
        antml_func = "antml:function_calls"
        invoke_tag = "invoke"
        antml_invoke = "antml:invoke"
        param_tag = "parameter"
        antml_param = "antml:parameter"
        
        self.function_call_patterns = [
            re.compile(f"<{func_calls}>.*?</{func_calls}>", re.DOTALL | re.IGNORECASE),
            re.compile(f"<{antml_func}>.*?</{antml_func}>", re.DOTALL | re.IGNORECASE),
            re.compile(f"<{invoke_tag}[^>]*>.*?</{invoke_tag}>", re.DOTALL | re.IGNORECASE),
            re.compile(f"<{antml_invoke}[^>]*>.*?</{antml_invoke}>", re.DOTALL | re.IGNORECASE),
            re.compile(f"<{param_tag}[^>]*>.*?</{antml_param}>", re.DOTALL | re.IGNORECASE),
        ]
        
        # File path patterns to filter
        self.file_path_patterns = [
            re.compile(r"/Users/[^/\s]+(?:/[^/\s]+)*", re.IGNORECASE),  # macOS paths
            re.compile(r"/home/[^/\s]+(?:/[^/\s]+)*", re.IGNORECASE),   # Linux home paths
            re.compile(r"/app/[^/\s]+(?:/[^/\s]+)*", re.IGNORECASE),    # App paths
            re.compile(r"/tmp/[^/\s]+(?:/[^/\s]+)*", re.IGNORECASE),    # Temp paths
            re.compile(r"/workspace/[^/\s]+(?:/[^/\s]+)*", re.IGNORECASE),  # Workspace paths
        ]
        
        # Telegram ID patterns (in XML context)
        self.telegram_id_patterns = [
            re.compile(r'<target[^>]*>-?\d{8,12}</target>', re.IGNORECASE),
            re.compile(r'<user_id[^>]*>-?\d{8,12}</user_id>', re.IGNORECASE),
            re.compile(r'<chat_id[^>]*>-?\d{8,12}</chat_id>', re.IGNORECASE),
        ]
        
        # System information patterns
        self.system_patterns = [
            re.compile(r"session_id[\"']\s*:\s*[\"'][^\"']+[\"']", re.IGNORECASE),
            re.compile(r"api[_-]?key[\"']\s*:\s*[\"'][^\"']+[\"']", re.IGNORECASE),
            re.compile(r"token[\"']\s*:\s*[\"'][^\"']+[\"']", re.IGNORECASE),
        ]
    
    def filter_response(self, response_content: str) -> FilterResult:
        """
        Filter outbound response content to remove sensitive information.
        
        Args:
            response_content: The response content to filter
            
        Returns:
            FilterResult with filtered content and list of removed items
        """
        if not response_content:
            return FilterResult(
                filtered_content=response_content or "",
                removed_items=[],
                filter_applied=False
            )
        
        filtered_content = response_content
        removed_items = []
        
        # Remove function call XML
        for pattern in self.function_call_patterns:
            matches = pattern.findall(filtered_content)
            if matches:
                removed_items.extend([f"function_call_xml:{len(matches)} instances"])
                filtered_content = pattern.sub("[FUNCTION_CALL_FILTERED]", filtered_content)
        
        # Remove file paths
        for pattern in self.file_path_patterns:
            matches = pattern.findall(filtered_content)
            if matches:
                for match in matches:
                    removed_items.append(f"file_path:{match}")
                filtered_content = pattern.sub("[PATH_FILTERED]", filtered_content)
        
        # Remove Telegram IDs in XML context
        for pattern in self.telegram_id_patterns:
            matches = pattern.findall(filtered_content)
            if matches:
                for match in matches:
                    removed_items.append(f"telegram_id:{match}")
                filtered_content = pattern.sub("[ID_FILTERED]", filtered_content)
        
        # Remove system information
        for pattern in self.system_patterns:
            matches = pattern.findall(filtered_content)
            if matches:
                for match in matches:
                    removed_items.append(f"system_info:{match}")
                filtered_content = pattern.sub("[SYSTEM_INFO_FILTERED]", filtered_content)
        
        return FilterResult(
            filtered_content=filtered_content,
            removed_items=removed_items,
            filter_applied=len(removed_items) > 0
        )
    
    # ── C32: Command Injection Scan ───────────────────────────────────────────

    def scan_command_injection(self, text: str) -> FilterResult:
        """Scan outbound text for command / code injection patterns.

        Does NOT modify the text — returns a FilterResult with removed_items
        populated for each matched pattern.  Callers decide whether to block.
        """
        if not text:
            return FilterResult(filtered_content=text or "", removed_items=[], filter_applied=False)

        removed: List[str] = []
        for pat in _COMMAND_INJECTION_PATTERNS:
            matches = pat.findall(text)
            if matches:
                removed.append(f"command_injection:{pat.pattern[:60]}")

        return FilterResult(
            filtered_content=text,
            removed_items=removed,
            filter_applied=bool(removed),
        )

    # ─────────────────────────────────────────────────────────────────────────

    def filter_function_calls_only(self, response_content: str) -> str:
        """
        Quick filter that only removes function call XML (for performance).
        
        Args:
            response_content: The response content to filter
            
        Returns:
            Content with function calls removed
        """
        if not response_content:
            return response_content or ""
        
        filtered_content = response_content
        
        for pattern in self.function_call_patterns:
            filtered_content = pattern.sub("[FUNCTION_CALL_FILTERED]", filtered_content)
        
        return filtered_content
