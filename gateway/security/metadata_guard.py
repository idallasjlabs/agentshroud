# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Metadata Channel Guard - Security Hardening Module
Sanitize HTTP headers, image metadata, and filenames to prevent information disclosure.
"""

from __future__ import annotations

import hashlib
import logging
import re
import time
import unicodedata
from dataclasses import dataclass
from typing import Dict, Optional

logger = logging.getLogger(__name__)


# C18: Document File Tagging
@dataclass
class DocumentTag:
    """Provenance record for a document ingested into the agent context."""

    filename: str
    content_hash: str  # SHA-256 of raw content bytes
    source: str  # upload / tool_fetch / web_fetch
    trust_level: str  # TRUSTED / UNTRUSTED
    tagged_at: float
    size_bytes: int


class MetadataGuard:
    """Guards against metadata channel attacks and information disclosure."""

    def __init__(self):
        # C18: document tag store keyed by content_hash
        self._document_tags: Dict[str, DocumentTag] = {}

        # Headers to strip entirely
        self.strip_headers = {"Server", "X-Powered-By"}

        # Headers to sanitize (remove internal IPs)
        self.sanitizable_headers = {"Via", "X-Forwarded-For", "X-Real-IP"}

        # Internal IP patterns (RFC 1918 + loopback + link-local)
        self.internal_ip_pattern = re.compile(
            r"(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2[0-9]|3[0-1])\.\d{1,3}\.\d{1,3}|127\.\d{1,3}\.\d{1,3}\.\d{1,3}|169\.254\.\d{1,3}\.\d{1,3}|::1|fc00::|fe80::)"
        )

        # EXIF magic bytes
        self.exif_magic = b"Exif\x00\x00"

        # Unicode control characters to strip
        self.control_chars = [
            "\u200b",  # Zero width space
            "\u200c",  # Zero width non-joiner
            "\u200d",  # Zero width joiner
            "\u200e",  # Left-to-right mark
            "\u200f",  # Right-to-left mark
            "\u202a",  # Left-to-right embedding
            "\u202b",  # Right-to-left embedding
            "\u202c",  # Pop directional formatting
            "\u202d",  # Left-to-right override
            "\u202e",  # Right-to-left override
        ]

        # Max header size (8KB)
        self.max_header_size = 8192

    def sanitize_headers(self, headers: Dict[str, str]) -> Dict[str, str]:
        """Sanitize HTTP headers by removing sensitive information."""
        sanitized = {}
        total_size = 0

        for key, value in headers.items():
            # Calculate size
            header_size = len(key.encode("utf-8")) + len(str(value).encode("utf-8"))
            total_size += header_size

            # Skip if total headers exceed limit
            if total_size > self.max_header_size:
                logger.warning(f"Headers exceed size limit ({self.max_header_size}B), truncating")
                break

            # Strip sensitive headers entirely
            if key in self.strip_headers:
                continue

            # Sanitize headers that might contain internal IPs
            if key in self.sanitizable_headers:
                value = self.internal_ip_pattern.sub("[REDACTED]", str(value))

            sanitized[key] = value

        return sanitized

    def sanitize_filename(self, filename: str) -> str:
        """Sanitize filename by removing unicode control characters and normalizing."""
        if not filename:
            return filename

        # Strip unicode control characters
        for char in self.control_chars:
            filename = filename.replace(char, "")

        # Normalize using NFKC (canonical decomposition + canonical composition)
        filename = unicodedata.normalize("NFKC", filename)

        # Strip path traversal sequences
        # Remove .. components and absolute path prefixes
        filename = filename.replace("\\", "/")  # Normalize backslash
        parts = filename.split("/")
        safe_parts = [p for p in parts if p and p != ".."]
        filename = (
            "/".join(safe_parts)
            if len(safe_parts) > 1
            else (safe_parts[0] if safe_parts else "unnamed")
        )

        # Strip leading slashes (prevent absolute paths)
        filename = filename.lstrip("/")

        # Strip null bytes
        filename = filename.replace("\x00", "")

        return filename or "unnamed"

    def check_for_exif(self, data: bytes) -> bool:
        """Check if binary data contains EXIF metadata."""
        if not data:
            return False

        # Look for EXIF magic bytes
        return self.exif_magic in data

    def sanitize_image_metadata(self, data: bytes) -> bytes:
        """Remove EXIF metadata from image data if present."""
        if not self.check_for_exif(data):
            return data

        # Find EXIF section and remove it
        # This is a simplified implementation - in production you'd want a proper EXIF parser
        exif_start = data.find(self.exif_magic)
        if exif_start == -1:
            return data

        # Find the end of the EXIF section
        # EXIF sections are typically small, so we'll remove a reasonable chunk
        exif_end = exif_start + 1024  # Remove up to 1KB of EXIF data
        if exif_end > len(data):
            exif_end = len(data)

        # Remove the EXIF section
        return data[:exif_start] + data[exif_end:]

    # ── C18: Document File Tagging ────────────────────────────────────────────

    def tag_document(
        self,
        filename: str,
        content: bytes,
        source: str = "upload",
        trust_level: str = "UNTRUSTED",
    ) -> DocumentTag:
        """Create and store a provenance tag for a document."""
        content_hash = hashlib.sha256(content).hexdigest()
        tag = DocumentTag(
            filename=filename,
            content_hash=content_hash,
            source=source,
            trust_level=trust_level,
            tagged_at=time.time(),
            size_bytes=len(content),
        )
        self._document_tags[content_hash] = tag
        return tag

    def get_document_tag(self, content_hash: str) -> Optional[DocumentTag]:
        """Look up a document tag by its SHA-256 content hash."""
        return self._document_tags.get(content_hash)

    # ─────────────────────────────────────────────────────────────────────────

    def check_oversized_headers(self, headers: Dict[str, str]) -> Optional[str]:
        """Check if headers exceed size limits."""
        total_size = sum(
            len(k.encode("utf-8")) + len(str(v).encode("utf-8")) for k, v in headers.items()
        )

        if total_size > self.max_header_size:
            return f"Headers size ({total_size}B) exceeds limit ({self.max_header_size}B)"

        return None
