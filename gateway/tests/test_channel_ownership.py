# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for P3: Channel Ownership — Telegram webhook + email send.

TDD red phase: these tests define the required behaviour for:
  POST /webhook/telegram  — inbound Telegram messages through the gateway
  POST /email/send        — bot email requests mediated by the gateway
"""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from gateway.ingest_api.main import app, auth_dep
from gateway.ingest_api.routes.forward import auth_dep as forward_auth_dep

# ============================================================
# Auth bypass fixture (autouse keeps every test isolated)
# ============================================================


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


# ============================================================
# Telegram webhook tests
# ============================================================


class TestTelegramWebhook:

    def test_valid_payload_returns_200(self, client):
        """Standard Telegram message payload is accepted."""
        resp = client.post(
            "/webhook/telegram",
            json={"message": {"text": "Hello from Telegram", "chat": {"id": 12345}}},
        )
        assert resp.status_code == 200

    def test_empty_payload_returns_200(self, client):
        """Empty payload is handled gracefully (skipped, not error)."""
        resp = client.post("/webhook/telegram", json={})
        assert resp.status_code == 200

    def test_response_has_status_field(self, client):
        """Response always includes a 'status' field."""
        resp = client.post(
            "/webhook/telegram",
            json={"message": {"text": "Test"}},
        )
        assert resp.status_code == 200
        assert "status" in resp.json()

    def test_passthrough_status_without_pipeline(self, client):
        """Without a pipeline configured, status is passthrough (not error)."""
        resp = client.post(
            "/webhook/telegram",
            json={"message": {"text": "Test"}},
        )
        data = resp.json()
        assert data["status"] in ("passthrough", "processed", "forwarded", "skipped")

    def test_requires_auth(self):
        """Endpoint returns 401 without auth override."""
        app.dependency_overrides.pop(auth_dep, None)
        app.dependency_overrides.pop(forward_auth_dep, None)
        try:
            tc = TestClient(app, raise_server_exceptions=False)
            resp = tc.post(
                "/webhook/telegram",
                json={"message": {"text": "Hello"}},
            )
            assert resp.status_code in (401, 403)
        finally:
            app.dependency_overrides[auth_dep] = lambda: None

    def test_non_json_body_returns_200(self, client):
        """Malformed body is handled defensively (empty dict fallback)."""
        resp = client.post(
            "/webhook/telegram",
            content=b"not json",
            headers={"Content-Type": "application/json"},
        )
        # Should not 500 — endpoint handles JSON parse errors gracefully
        assert resp.status_code in (200, 422)


# ============================================================
# Email send tests
# ============================================================


class TestEmailSend:

    def test_missing_required_fields_returns_422(self, client):
        """Missing 'subject' or 'body' returns 422."""
        resp = client.post("/email/send", json={"to": "test@example.com"})
        assert resp.status_code == 422

    def test_missing_to_returns_422(self, client):
        """Missing 'to' field returns 422."""
        resp = client.post("/email/send", json={"subject": "Hi", "body": "Hello"})
        assert resp.status_code == 422

    def test_requires_auth(self):
        """Endpoint returns 401 without auth override."""
        app.dependency_overrides.pop(auth_dep, None)
        app.dependency_overrides.pop(forward_auth_dep, None)
        try:
            tc = TestClient(app, raise_server_exceptions=False)
            resp = tc.post(
                "/email/send",
                json={"to": "a@b.com", "subject": "x", "body": "x"},
            )
            assert resp.status_code in (401, 403)
        finally:
            app.dependency_overrides[auth_dep] = lambda: None

    def test_allowed_recipient_returns_200(self, client):
        """Email to an allowed recipient returns 200 with status=approved."""
        with patch(
            "gateway.ingest_api.routes.forward._is_email_recipient_allowed", return_value=True
        ):
            resp = client.post(
                "/email/send",
                json={
                    "to": "trusted@example.com",
                    "subject": "Test",
                    "body": "Hello world",
                },
            )
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "approved"

    def test_allowed_recipient_response_has_sanitized_body(self, client):
        """Approved response includes sanitized_body field."""
        with patch(
            "gateway.ingest_api.routes.forward._is_email_recipient_allowed", return_value=True
        ):
            resp = client.post(
                "/email/send",
                json={"to": "trusted@example.com", "subject": "Test", "body": "Hi"},
            )
        assert resp.status_code == 200
        data = resp.json()
        assert "sanitized_body" in data
        assert "pii_redacted" in data

    def test_pii_in_body_is_redacted(self, client):
        """PII in email body is flagged when sanitizer is active."""
        mock_scan = MagicMock()
        mock_scan.sanitized_content = "My SSN is [REDACTED]"
        mock_scan.redactions = [MagicMock()]  # non-empty = redaction happened

        mock_sanitizer = MagicMock()
        mock_sanitizer.sanitize = AsyncMock(return_value=mock_scan)

        with (
            patch(
                "gateway.ingest_api.routes.forward._is_email_recipient_allowed", return_value=True
            ),
            patch("gateway.ingest_api.routes.forward.app_state") as mock_state,
        ):
            mock_state.sanitizer = mock_sanitizer
            mock_state.approval_queue = None
            resp = client.post(
                "/email/send",
                json={
                    "to": "trusted@example.com",
                    "subject": "Test",
                    "body": "My SSN is 123-45-6789",
                },
            )
        assert resp.status_code == 200
        data = resp.json()
        assert data["pii_redacted"] is True
        assert "123-45-6789" not in data["sanitized_body"]
        mock_sanitizer.sanitize.assert_awaited_once()

    def test_unknown_recipient_queued_for_approval(self, client):
        """Unknown recipient triggers approval queue and returns 202."""
        mock_item = MagicMock()
        mock_item.request_id = "approval-abc-123"
        mock_queue = MagicMock()
        mock_queue.submit = AsyncMock(return_value=mock_item)

        with (
            patch(
                "gateway.ingest_api.routes.forward._is_email_recipient_allowed", return_value=False
            ),
            patch("gateway.ingest_api.routes.forward.app_state") as mock_state,
        ):
            mock_state.sanitizer = None
            mock_state.approval_queue = mock_queue
            resp = client.post(
                "/email/send",
                json={
                    "to": "unknown@random.com",
                    "subject": "Test",
                    "body": "Hello",
                },
            )
        assert resp.status_code == 202
        data = resp.json()
        assert data["status"] == "queued"
        assert data["approval_id"] == "approval-abc-123"

    def test_unknown_recipient_no_queue_returns_403(self, client):
        """Unknown recipient with no approval queue configured returns 403."""
        with (
            patch(
                "gateway.ingest_api.routes.forward._is_email_recipient_allowed", return_value=False
            ),
            patch("gateway.ingest_api.routes.forward.app_state") as mock_state,
        ):
            mock_state.sanitizer = None
            mock_state.approval_queue = None
            resp = client.post(
                "/email/send",
                json={
                    "to": "unknown@random.com",
                    "subject": "Test",
                    "body": "Hello",
                },
            )
        assert resp.status_code == 403

    def test_response_has_timestamp(self, client):
        """All responses include an ISO 8601 timestamp."""
        with patch(
            "gateway.ingest_api.routes.forward._is_email_recipient_allowed", return_value=True
        ):
            resp = client.post(
                "/email/send",
                json={"to": "trusted@example.com", "subject": "Test", "body": "Hi"},
            )
        assert resp.status_code == 200
        data = resp.json()
        assert "timestamp" in data
        assert "T" in data["timestamp"]  # ISO 8601 format
