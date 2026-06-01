# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests that owner-bound email bypasses PII sanitisation.

Root cause of the OpenClaw email truncation bug (2026-05-26 PM): the Presidio +
regex PII sanitiser ran on every email body before the recipient allowlist check.
Competitive-intel bodies dense with CVE IDs, company names, and ISO dates were
collapsed into redaction tags, producing an empty body.

The fix (forward.py:184-199): perform the allowlist check first; skip PII for
allowlisted recipients (the trust boundary is the allowlist, not the body content).
Unknown recipients still get the full Presidio+regex scrub before the approval queue.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from gateway.ingest_api.main import app, auth_dep
from gateway.ingest_api.routes.forward import auth_dep as forward_auth_dep


@pytest.fixture(autouse=True)
def bypass_auth():
    app.dependency_overrides[auth_dep] = lambda: None
    app.dependency_overrides[forward_auth_dep] = lambda: None
    yield
    app.dependency_overrides.pop(auth_dep, None)
    app.dependency_overrides.pop(forward_auth_dep, None)


@pytest.fixture
def client():
    return TestClient(app)


class TestOwnerEmailBypassesPii:

    def test_owner_recipient_body_preserved(self, client):
        """Owner-allowlisted recipient receives body verbatim; pii_redacted=False."""
        mock_sanitizer = MagicMock()
        mock_sanitizer.sanitize = AsyncMock()

        body = (
            "<h2>Executive Summary</h2>"
            "<p>CVE-2024-12345 affects OpenAI and Anthropic. "
            "Report date: 2026-05-26. Contact: research@openai.com.</p>"
        )

        with (
            patch(
                "gateway.ingest_api.routes.forward._get_gmail_app_password",
                return_value="fake-app-pw",
            ),
            patch("gateway.ingest_api.routes.forward.smtplib.SMTP_SSL") as mock_smtp,
            patch("gateway.ingest_api.routes.forward.app_state") as mock_state,
        ):
            mock_smtp.return_value.__enter__ = MagicMock(return_value=MagicMock())
            mock_smtp.return_value.__exit__ = MagicMock(return_value=False)
            mock_state.sanitizer = mock_sanitizer
            mock_state.approval_queue = None
            resp = client.post(
                "/email/send",
                json={
                    "to": "idallasj@gmail.com",
                    "subject": "AgentShroud Competitive Intelligence PM 2026-05-26",
                    "body": body,
                    "is_html": True,
                },
            )

        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "approved"
        assert data["pii_redacted"] is False
        mock_sanitizer.sanitize.assert_not_awaited()

    def test_send_owner_endpoint_also_bypasses_pii(self, client):
        """/email/send-owner delegates to email_send and also skips PII for the owner."""
        mock_sanitizer = MagicMock()
        mock_sanitizer.sanitize = AsyncMock()

        with (
            patch(
                "gateway.ingest_api.routes.forward._get_gmail_app_password",
                return_value="fake-app-pw",
            ),
            patch("gateway.ingest_api.routes.forward.smtplib.SMTP_SSL") as mock_smtp,
            patch("gateway.ingest_api.routes.forward.app_state") as mock_state,
        ):
            mock_smtp.return_value.__enter__ = MagicMock(return_value=MagicMock())
            mock_smtp.return_value.__exit__ = MagicMock(return_value=False)
            mock_state.sanitizer = mock_sanitizer
            mock_state.approval_queue = None
            resp = client.post(
                "/email/send-owner",
                json={
                    "subject": "Hermes smoke test",
                    "body": "CVE-2024-12345 and CVE-2023-44487 noted.",
                },
            )

        assert resp.status_code == 200
        data = resp.json()
        assert data["pii_redacted"] is False
        mock_sanitizer.sanitize.assert_not_awaited()

    def test_unknown_recipient_body_still_scrubbed(self, client):
        """Unknown recipient's body is PII-scrubbed before approval queue submission."""
        mock_scan = MagicMock()
        mock_scan.sanitized_content = "My SSN is <US_SSN>"
        mock_scan.redactions = [MagicMock()]

        mock_sanitizer = MagicMock()
        mock_sanitizer.sanitize = AsyncMock(return_value=mock_scan)

        mock_item = MagicMock()
        mock_item.request_id = "approval-001"
        mock_queue = MagicMock()
        mock_queue.submit = AsyncMock(return_value=mock_item)

        with (
            patch("gateway.ingest_api.routes.forward.app_state") as mock_state,
        ):
            mock_state.sanitizer = mock_sanitizer
            mock_state.approval_queue = mock_queue
            resp = client.post(
                "/email/send",
                json={
                    "to": "stranger@example.com",
                    "subject": "Test",
                    "body": "My SSN is 123-45-6789",
                },
            )

        assert resp.status_code == 202
        data = resp.json()
        assert data["status"] == "queued"
        mock_sanitizer.sanitize.assert_awaited_once()
