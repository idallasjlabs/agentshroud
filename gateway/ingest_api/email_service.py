# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Gateway owner-comms email service (SCRUM-77).

Consolidates the SMTP transport for all gateway-originated owner email (the
/email/send + /email/send-owner endpoints, heartbeat, competitive-intel and
weekly-review crons) into one place with an **injectable transport**.

Why: the transport used to be inlined in the ``/email/send`` handler, so the
only way to exercise the send path in a test was to monkeypatch ``smtplib``
module-globals — brittle, and a missed patch would send real mail.  Here the
SMTP connection is created by an injected ``transport_factory``; production
uses ``smtplib.SMTP_SSL`` while tests inject a fake that records the calls, so
**no test can ever send real mail**.

The service owns only the transport (MIME build + login + sendmail).  Policy —
recipient allowlist, PII redaction, approval queue, credential retrieval —
stays in the endpoint, which is the correct trust boundary.
"""

from __future__ import annotations

import logging
import smtplib
from contextlib import AbstractContextManager
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Callable, Protocol

logger = logging.getLogger("agentshroud.ingest_api.email_service")


class SmtpLike(Protocol):
    """The subset of ``smtplib.SMTP_SSL`` the service uses."""

    def login(self, user: str, password: str) -> object: ...

    def sendmail(self, from_addr: str, to_addrs: list[str], msg: str) -> object: ...


# A transport factory returns a context-managed SMTP-like connection.  Injected
# so production uses SMTP_SSL and tests use a fake (no real network).
TransportFactory = Callable[[], AbstractContextManager[SmtpLike]]


class GatewayEmailService:
    """Sends owner-comms email over an injectable SMTP transport."""

    def __init__(
        self,
        sender: str,
        host: str,
        port: int,
        transport_factory: TransportFactory | None = None,
    ) -> None:
        self._sender = sender
        self._host = host
        self._port = port
        # Default production transport: TLS-wrapped SMTP to the configured host.
        self._transport_factory: TransportFactory = transport_factory or (
            lambda: smtplib.SMTP_SSL(self._host, self._port)
        )

    @property
    def sender(self) -> str:
        return self._sender

    def build_message(self, to: str, subject: str, body: str, is_html: bool) -> str:
        """Build the MIME message string (multipart/alternative).

        For HTML mail the plain fallback is attached first and the HTML part
        last (clients render the last-attached alternative) — preserving the
        prior endpoint behaviour exactly.
        """
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = self._sender
        msg["To"] = to
        if is_html:
            msg.attach(MIMEText("This email requires an HTML-capable email client.", "plain"))
            msg.attach(MIMEText(body, "html"))
        else:
            msg.attach(MIMEText(body, "plain"))
        return msg.as_string()

    def send(
        self,
        to: str,
        subject: str,
        body: str,
        is_html: bool,
        app_password: str,
    ) -> None:
        """Send one email synchronously.  Blocking — call in an executor.

        Raises the underlying ``smtplib`` exception on failure so the caller can
        map it to the right HTTP status (auth failure vs generic SMTP error).
        """
        payload = self.build_message(to, subject, body, is_html)
        with self._transport_factory() as smtp:
            smtp.login(self._sender, app_password)
            smtp.sendmail(self._sender, [to], payload)
        logger.info("email sent to %s subject=%r", to, subject)
