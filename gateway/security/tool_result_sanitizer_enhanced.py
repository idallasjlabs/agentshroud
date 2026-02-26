# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™
from __future__ import annotations

"""
Enhanced Tool Result Sanitizer with Domain Allowlist
Strips markdown images and links pointing to non-allowlisted domains while preserving legitimate content.
"""

import re
import logging
from dataclasses import dataclass, field
from typing import List, Set, Optional, Tuple
from urllib.parse import urlparse

logger = logging.getLogger("agentshroud.security.tool_result_sanitizer")


@dataclass
class ToolResultSanitizerConfig:
    """Configuration for tool result markdown sanitization."""
    
    # Operating mode: "enforce" (strip non-allowlisted) or "warn" (mark but preserve)
    mode: str = "enforce"
    
    # Default domain allowlist for markdown links and images
    allowed_domains: List[str] = field(default_factory=lambda: [
        # Documentation and reference sites
        "github.com",
        "*.github.com",
        "docs.python.org",
        "*.python.org",
        "stackoverflow.com",
        "*.stackoverflow.com",
        "wikipedia.org",
        "*.wikipedia.org",
        "w3.org",
        "*.w3.org",
        
        # Common safe domains for technical content
        "developer.mozilla.org",
        "docs.microsoft.com",
        "cloud.google.com",
        "aws.amazon.com",
        "docs.aws.amazon.com",
        
        # Package registries and dev tools
        "pypi.org",
        "npmjs.com",
        "*.npmjs.com",
        "registry.npmjs.org",
        
        # Media hosting (for legitimate images in documentation)
        "i.imgur.com",
        "raw.githubusercontent.com",
    ])
    
    # Additional patterns that should always be blocked regardless of domain
    blocked_patterns: List[str] = field(default_factory=lambda: [
        r"exfil",
        r"leak",
        r"steal", 
        r"callback",
        r"webhook",
        r"collect",
        r"log", 
        r"track",
        r"ping",
        r"beacon",
        # Template injection patterns
        r"\{\{.*\}\}",
        r"\$\{.*\}",
        r"%7[Bb].*%7[Dd]",  # URL encoded {{ }}
        r"SYSTEM",
        r"SECRET",
        r"KEY",
        r"TOKEN", 
        r"PASSWORD",
        r"API_KEY",
        r"BEARER",
    ])
    
    # Preserve code blocks and other structured content
    preserve_code_blocks: bool = True
    preserve_internal_links: bool = True  # Links that start with # or /


class ToolResultSanitizer:
    """Enhanced markdown sanitizer with configurable domain allowlist."""
    
    def __init__(self, config: ToolResultSanitizerConfig):
        self.config = config
        
        # Compile regex patterns for performance
        self._md_image_re = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
        self._md_link_re = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')
        self._code_block_re = re.compile(r'```[\s\S]*?```|`[^`]+`')
        
        # Compile blocked patterns
        self._blocked_pattern_res = [
            re.compile(pattern, re.IGNORECASE) for pattern in self.config.blocked_patterns
        ]
    
    def _is_domain_allowed(self, url: str) -> bool:
        """Check if a URL's domain is in the allowlist."""
        try:
            parsed = urlparse(url)
            domain = parsed.netloc.lower()
            
            if not domain:
                return False
            
            # Check against allowlist patterns
            for allowed in self.config.allowed_domains:
                if self._domain_matches_pattern(domain, allowed.lower()):
                    return True
            
            return False
            
        except Exception:
            return False
    
    def _domain_matches_pattern(self, domain: str, pattern: str) -> bool:
        """Check if domain matches pattern (supports wildcards)."""
        if pattern.startswith("*."):
            # Wildcard subdomain match
            base_domain = pattern[2:]
            return domain == base_domain or domain.endswith("." + base_domain)
        else:
            return domain == pattern
    
    def _url_has_blocked_patterns(self, url: str) -> bool:
        """Check if URL contains any blocked patterns."""
        for pattern_re in self._blocked_pattern_res:
            if pattern_re.search(url):
                return True
        return False
    
    def _is_internal_link(self, url: str) -> bool:
        """Check if this is an internal link (relative, anchor, etc.)."""
        return url.startswith("#") or url.startswith("/") or not ("://" in url)
    
    def _extract_code_blocks(self, text: str) -> Tuple[str, List[str]]:
        """Extract code blocks to preserve them during sanitization."""
        if not self.config.preserve_code_blocks:
            return text, []
        
        code_blocks = []
        placeholders = []
        
        def replace_code_block(match):
            placeholder = f"__CODE_BLOCK_{len(code_blocks)}__"
            code_blocks.append(match.group(0))
            placeholders.append(placeholder)
            return placeholder
        
        text_without_code = self._code_block_re.sub(replace_code_block, text)
        return text_without_code, list(zip(placeholders, code_blocks))
    
    def _restore_code_blocks(self, text: str, code_blocks: List[Tuple[str, str]]) -> str:
        """Restore code blocks after sanitization."""
        for placeholder, original_code in code_blocks:
            text = text.replace(placeholder, original_code)
        return text
    
    def sanitize_images(self, text: str) -> str:
        """Remove or warn about markdown images pointing to non-allowlisted domains."""
        
        def replace_image(match):
            alt_text = match.group(1)
            url = match.group(2)
            
            # Preserve internal/relative images
            if self.config.preserve_internal_links and self._is_internal_link(url):
                return match.group(0)
            
            # Check for blocked patterns first
            if self._url_has_blocked_patterns(url):
                logger.warning(f"Blocked markdown image with suspicious pattern: {url[:100]}")
                return f"[Image removed: suspicious URL pattern]"
            
            # Check domain allowlist
            if not self._is_domain_allowed(url):
                if self.config.mode == "enforce":
                    logger.info(f"Stripped markdown image from non-allowlisted domain: {url[:100]}")
                    return f"[Image: {alt_text}]" if alt_text else "[Image removed: external domain]"
                elif self.config.mode == "warn":
                    logger.warning(f"External image detected: {url[:100]}")
                    return f"![{alt_text}]({url}) [⚠️ EXTERNAL IMAGE]"
            
            return match.group(0)  # Keep allowed images
        
        return self._md_image_re.sub(replace_image, text)
    
    def sanitize_links(self, text: str) -> str:
        """Remove or warn about markdown links pointing to non-allowlisted domains."""
        
        def replace_link(match):
            link_text = match.group(1) 
            url = match.group(2)
            
            # Preserve internal/relative links
            if self.config.preserve_internal_links and self._is_internal_link(url):
                return match.group(0)
            
            # Check for blocked patterns first
            if self._url_has_blocked_patterns(url):
                logger.warning(f"Blocked markdown link with suspicious pattern: {url[:100]}")
                return f"[Link removed: suspicious URL pattern]"
            
            # Check domain allowlist
            if not self._is_domain_allowed(url):
                if self.config.mode == "enforce":
                    logger.info(f"Stripped markdown link to non-allowlisted domain: {url[:100]}")
                    return link_text if link_text else "[Link removed: external domain]"
                elif self.config.mode == "warn":
                    logger.warning(f"External link detected: {url[:100]}")
                    return f"[{link_text}]({url}) [⚠️ EXTERNAL LINK]"
            
            return match.group(0)  # Keep allowed links
        
        return self._md_link_re.sub(replace_link, text)
    
    def sanitize(self, content: str) -> str:
        """
        Sanitize tool result content by filtering markdown links and images.
        
        Args:
            content: Raw tool result content
            
        Returns:
            Sanitized content with non-allowlisted markdown links/images filtered
        """
        if not content or not isinstance(content, str):
            return content or ""
        
        # Extract and preserve code blocks
        content_no_code, code_blocks = self._extract_code_blocks(content)
        
        # Sanitize images and links
        content_no_code = self.sanitize_images(content_no_code)
        content_no_code = self.sanitize_links(content_no_code)
        
        # Restore code blocks
        sanitized_content = self._restore_code_blocks(content_no_code, code_blocks)
        
        return sanitized_content


# Default instance for easy import
default_sanitizer = ToolResultSanitizer(ToolResultSanitizerConfig())


def sanitize_tool_result(content: str, config: Optional[ToolResultSanitizerConfig] = None) -> str:
    """
    Convenience function to sanitize tool result content.
    
    Args:
        content: Content to sanitize
        config: Optional custom configuration
        
    Returns:
        Sanitized content
    """
    if config is not None:
        sanitizer = ToolResultSanitizer(config)
    else:
        sanitizer = default_sanitizer
        
    return sanitizer.sanitize(content)