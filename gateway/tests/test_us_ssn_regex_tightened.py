# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Regression tests for the tightened US_SSN regex.

CVE-2024-NNNN identifiers (NNN-NN-NNNN digit pattern) were previously matched
by the US_SSN regex because XXX-XX-XXXX is structurally identical to the last
segments of a CVE ID.  The regex is now anchored to reject matches preceded by
an uppercase letter, which blocks CVE-style false-positives while preserving
detection of real Social Security Numbers.
"""

from __future__ import annotations

import pytest


@pytest.mark.asyncio
async def test_cve_pattern_not_flagged_as_ssn(sanitizer):
    """CVE identifiers must NOT be treated as US_SSN."""
    content = "CVE-2024-12345 affects multiple vendors."
    result = await sanitizer.sanitize(content)

    assert "US_SSN" not in result.entity_types_found
    assert "<US_SSN>" not in result.sanitized_content
    assert result.sanitized_content == content


@pytest.mark.asyncio
async def test_cve_with_five_digit_suffix_not_flagged(sanitizer):
    """CVE IDs with 5-digit suffix must also be excluded."""
    content = "See CVE-2023-44487 (HTTP/2 Rapid Reset) for details."
    result = await sanitizer.sanitize(content)

    assert "<US_SSN>" not in result.sanitized_content


@pytest.mark.asyncio
async def test_real_ssn_still_flagged(sanitizer):
    """Real SSNs (not preceded by uppercase) must still be detected."""
    content = "My SSN is 123-45-6789."
    result = await sanitizer.sanitize(content)

    assert "US_SSN" in result.entity_types_found
    assert "<US_SSN>" in result.sanitized_content
    assert "123-45-6789" not in result.sanitized_content


@pytest.mark.asyncio
async def test_ssn_at_start_of_string_still_flagged(sanitizer):
    """SSN at the very start of a string (no preceding character) is still flagged."""
    content = "123-45-6789 is the SSN in question."
    result = await sanitizer.sanitize(content)

    assert "US_SSN" in result.entity_types_found
    assert "<US_SSN>" in result.sanitized_content


@pytest.mark.asyncio
async def test_cve_dense_report_body_preserved(sanitizer):
    """A competitive-intel body with multiple CVEs is not collapsed into redaction tags."""
    content = (
        "<h2>Executive Summary</h2>"
        "<p>This week: CVE-2024-12345 (OpenAI), CVE-2023-44487 (Cloudflare), "
        "CVE-2024-99999 (Anthropic). No SSNs present.</p>"
    )
    result = await sanitizer.sanitize(content)

    assert "<US_SSN>" not in result.sanitized_content
    assert "Executive Summary" in result.sanitized_content
