# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Tests for GatewayEmailService (SCRUM-77).

The transport is injected, so no test opens a real SMTP connection.
"""

from __future__ import annotations

import smtplib

import pytest

from gateway.ingest_api.email_service import GatewayEmailService

_SENDER = "agentshroud.ai@gmail.com"


class _FakeSmtp:
    """Records login/sendmail; usable as a context manager like SMTP_SSL."""

    def __init__(self, recorder: dict, raise_on: str | None = None) -> None:
        self._rec = recorder
        self._raise_on = raise_on

    def __enter__(self) -> "_FakeSmtp":
        self._rec["entered"] = True
        return self

    def __exit__(self, *exc) -> bool:
        self._rec["exited"] = True
        return False

    def login(self, user: str, password: str) -> None:
        self._rec["login"] = (user, password)
        if self._raise_on == "login":
            raise smtplib.SMTPAuthenticationError(535, b"bad creds")

    def sendmail(self, from_addr: str, to_addrs: list[str], msg: str) -> None:
        self._rec["sendmail"] = (from_addr, list(to_addrs), msg)
        if self._raise_on == "sendmail":
            raise smtplib.SMTPException("relay error")


def _service(recorder: dict, raise_on: str | None = None) -> GatewayEmailService:
    return GatewayEmailService(
        sender=_SENDER,
        host="smtp.example.com",
        port=465,
        transport_factory=lambda: _FakeSmtp(recorder, raise_on),
    )


# ---------------------------------------------------------------------------
# build_message
# ---------------------------------------------------------------------------


class TestBuildMessage:
    def test_plain_message_has_single_plain_part(self) -> None:
        svc = _service({})
        raw = svc.build_message("to@x.com", "Subj", "hello body", is_html=False)
        assert "Subject: Subj" in raw
        assert f"From: {_SENDER}" in raw
        assert "To: to@x.com" in raw
        assert "hello body" in raw
        assert "Content-Type: text/plain" in raw
        assert "text/html" not in raw

    def test_html_message_has_plain_fallback_then_html(self) -> None:
        svc = _service({})
        raw = svc.build_message("to@x.com", "S", "<b>hi</b>", is_html=True)
        # Both parts present; the plain fallback precedes the HTML part.
        assert "text/plain" in raw and "text/html" in raw
        assert raw.index("HTML-capable") < raw.index("<b>hi</b>")


# ---------------------------------------------------------------------------
# send
# ---------------------------------------------------------------------------


class TestSend:
    def test_send_logs_in_and_sendmails_over_injected_transport(self) -> None:
        rec: dict = {}
        _service(rec).send("to@x.com", "S", "body", is_html=False, app_password="pw")
        assert rec["entered"] and rec["exited"]
        assert rec["login"] == (_SENDER, "pw")
        from_addr, to_addrs, payload = rec["sendmail"]
        assert from_addr == _SENDER
        assert to_addrs == ["to@x.com"]
        assert "body" in payload

    def test_send_html_uses_html_payload(self) -> None:
        rec: dict = {}
        _service(rec).send("to@x.com", "S", "<i>x</i>", is_html=True, app_password="pw")
        assert "text/html" in rec["sendmail"][2]

    def test_send_propagates_auth_error(self) -> None:
        rec: dict = {}
        with pytest.raises(smtplib.SMTPAuthenticationError):
            _service(rec, raise_on="login").send(
                "to@x.com", "S", "b", is_html=False, app_password="bad"
            )
        # Never reached sendmail after an auth failure.
        assert "sendmail" not in rec

    def test_send_propagates_generic_smtp_error(self) -> None:
        rec: dict = {}
        with pytest.raises(smtplib.SMTPException):
            _service(rec, raise_on="sendmail").send(
                "to@x.com", "S", "b", is_html=False, app_password="pw"
            )

    def test_default_transport_is_smtp_ssl(self, monkeypatch) -> None:
        # Without an injected factory, production uses smtplib.SMTP_SSL(host, port).
        captured: dict = {}

        class _Dummy:
            def __init__(self, host, port):
                captured["args"] = (host, port)

            def __enter__(self):
                return self

            def __exit__(self, *a):
                return False

            def login(self, *a):
                pass

            def sendmail(self, *a):
                pass

        monkeypatch.setattr(smtplib, "SMTP_SSL", _Dummy)
        GatewayEmailService(_SENDER, "smtp.gmail.com", 465).send(
            "to@x.com", "S", "b", is_html=False, app_password="pw"
        )
        assert captured["args"] == ("smtp.gmail.com", 465)


def test_sender_property() -> None:
    assert GatewayEmailService(_SENDER, "h", 1).sender == _SENDER


# ---------------------------------------------------------------------------
# Endpoint wiring: /email/send uses the injectable service (SCRUM-77)
# ---------------------------------------------------------------------------


class TestEndpointUsesService:
    def test_email_send_routes_through_injectable_service(self, monkeypatch) -> None:
        """POST /email/send to the owner sends via forward._email_service — proving
        the transport is the injectable seam (no real SMTP, no module-level
        smtplib patching needed)."""
        from fastapi.testclient import TestClient

        import gateway.ingest_api.routes.forward as forward
        from gateway.ingest_api.main import app, auth_dep

        sent: dict = {}

        class _FakeService:
            sender = _SENDER

            def send(self, to, subject, body, is_html, app_password) -> None:
                sent.update(to=to, subject=subject, body=body, is_html=is_html, pw=app_password)

        monkeypatch.setattr(forward, "_email_service", _FakeService())
        monkeypatch.setattr(forward, "_get_gmail_app_password", lambda: "app-pw")

        app.dependency_overrides[auth_dep] = lambda: None
        app.dependency_overrides[forward.auth_dep] = lambda: None
        try:
            resp = TestClient(app).post(
                "/email/send",
                json={
                    "to": "idallasj@gmail.com",  # allowlisted owner
                    "subject": "Weekly",
                    "body": "report body",
                    "agent_id": "hermes",
                },
            )
        finally:
            app.dependency_overrides.pop(auth_dep, None)
            app.dependency_overrides.pop(forward.auth_dep, None)

        assert resp.status_code == 200
        assert resp.json()["status"] == "approved"
        # The endpoint handed the send to the injectable service — no real SMTP.
        assert sent["to"] == "idallasj@gmail.com"
        assert sent["subject"] == "Weekly"
        assert sent["body"] == "report body"
        assert sent["pw"] == "app-pw"
