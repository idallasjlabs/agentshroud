# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""A2A Proxy — inbound interceptor for Hermes's A2A (Agent-to-Agent) surface
(SCRUM-129).

Unlike MCP tool calls (mcp_proxy.py), where the bot calls AgentShroud's own
pre-flight hook before making its own outbound request, A2A's inbound
direction is the opposite: an external peer calls Hermes's HTTP server
directly. AgentShroud must terminate that connection itself, not wait to be
called — the correct template is webhook_receiver.py ("sit in front of the
configured bot, ensure inbound traffic passes through the SecurityPipeline
before forwarding"), not mcp_proxy.py's "callee calls me first" pattern.

Pipeline per request:
  1. Resolve peer identity from the Authorization: Bearer token, via a
     peer-alias mapping — never from socket address / X-Forwarded-For.
     Independent mitigation for upstream Hermes gap #80534 (identity
     collapses to one shared identity behind a reverse proxy).
  2. Parse the JSON-RPC 2.0 envelope into (method, task_id, callback_url).
  3. Run it through A2APolicyEngine.enforce() (gateway/security/a2a_policy.py)
     — peer allow/deny, task ownership, SSRF-callback check, risk-tier
     approval gate.
  4. On ALLOW: extract text from Message.parts, PII-scan it (binary parts are
     flagged, never silently scanned or dropped), forward the (possibly
     redacted) request to Hermes's real A2A listener.
  5. PII-scan Hermes's response text before it goes back to the peer.

GET /.well-known/agent-card.json is a deliberate exception: passed through
unconditionally (the A2A spec requires open discovery) but still audited, so
reconnaissance against the endpoint is visible even though it's never blocked.

Docker networking note: this proxy is meant to be the actual published
surface peers reach, with Hermes's own A2A adapter bound to an internal-only
address — but that topology change ships alongside actually enabling A2A in
production (Hermes's adapter is disabled by default today), not with this
module. See docs/security/threat-model.md, "A2A (Agent-to-Agent) Protocol
Threat Analysis".
"""

import hmac
import json
import logging
import time
from dataclasses import dataclass, field
from typing import Any, Dict, Optional, Tuple

from gateway.security.a2a_policy import A2AMethod, A2APolicyEngine

logger = logging.getLogger("agentshroud.proxy.a2a_proxy")

# Pre-1.0 A2A peers sent lowercase, path-style method names. Hermes itself
# accepts both (per the upstream DESIGN.md); AgentShroud's parser must too, or
# a legitimate older peer is spuriously denied at the parser, before policy
# ever sees it.
_LEGACY_METHOD_ALIASES: Dict[str, A2AMethod] = {
    "message/send": A2AMethod.SEND_MESSAGE,
    "message/stream": A2AMethod.SEND_STREAMING_MESSAGE,
    "tasks/get": A2AMethod.GET_TASK,
    "tasks/list": A2AMethod.LIST_TASKS,
    "tasks/cancel": A2AMethod.CANCEL_TASK,
    "tasks/subscribe": A2AMethod.SUBSCRIBE_TO_TASK,
    "tasks/pushNotificationConfig/get": A2AMethod.GET_PUSH_NOTIFICATION_CONFIG,
    "tasks/pushNotificationConfig/create": A2AMethod.SET_PUSH_NOTIFICATION_CONFIG,
    "tasks/pushNotificationConfig/set": A2AMethod.SET_PUSH_NOTIFICATION_CONFIG,
    "tasks/pushNotificationConfig/delete": A2AMethod.DELETE_PUSH_NOTIFICATION_CONFIG,
}


# ---------------------------------------------------------------------------
# Result type — mirrors mcp_proxy.py::ProxyResult's shape and fail-closed
# default (allowed=False), so a code path that forgets to explicitly set the
# result fails closed by construction, never open.
# ---------------------------------------------------------------------------


@dataclass
class A2AProxyResult:
    """Result of proxying a single inbound A2A request."""

    allowed: bool = False
    blocked: bool = True
    block_reason: str = ""
    peer_id: str = ""
    method: str = ""
    matched_rule: str = ""
    # PII scanning
    pii_redaction_count: int = 0
    pii_scan_skipped_binary: bool = False
    # What actually got forwarded (redacted if PII was found)
    forwarded_body: Optional[str] = None
    upstream_status: Optional[int] = None
    upstream_body: Optional[str] = None
    # Audit
    audit_entry_id: str = ""
    processing_time_ms: float = 0.0


# ---------------------------------------------------------------------------
# Parsed JSON-RPC request
# ---------------------------------------------------------------------------


@dataclass
class ParsedA2ARequest:
    method: A2AMethod
    params: Dict[str, Any] = field(default_factory=dict)
    task_id: Optional[str] = None
    callback_url: Optional[str] = None
    request_id: Optional[str] = None


# ---------------------------------------------------------------------------
# Proxy
# ---------------------------------------------------------------------------


class A2AProxy:
    """Terminates inbound A2A HTTP requests, enforces policy, forwards.

    Usage::

        proxy = A2AProxy(
            policy_engine=engine,
            peer_tokens={"partner-token-abc": "partner-agent"},
            forwarder=hermes_a2a_forwarder,
            pii_detector=differential_pii_detector,
        )
        result = await proxy.process_inbound_request(raw_body, auth_header, source_ip)
    """

    def __init__(
        self,
        policy_engine: A2APolicyEngine,
        peer_tokens: Optional[Dict[str, str]] = None,
        forwarder: Optional[Any] = None,
        pii_detector: Optional[Any] = None,
        audit_store: Optional[Any] = None,
        bot_id: str = "hermes",
    ):
        self._policy_engine = policy_engine
        # token -> peer_id. A real deployment loads this from the same
        # A2A_PEER_TOKENS-shaped config Hermes itself would use, but resolved
        # and owned by AgentShroud, not trusted from Hermes.
        self._peer_tokens = dict(peer_tokens or {})
        self._forwarder = forwarder
        self._pii_detector = pii_detector
        self._audit_store = audit_store
        self._bot_id = bot_id

    # ---- peer identity resolution ------------------------------------

    def resolve_peer_id(self, auth_header: Optional[str]) -> Optional[str]:
        """Resolve peer identity from the Authorization: Bearer token.

        Never falls back to socket address or X-Forwarded-For — that fallback
        is exactly the upstream Hermes bug (gap #80534) that collapses every
        peer behind a shared reverse proxy into one identity. An unresolvable
        token means an unauthenticated caller, full stop.

        Uses hmac.compare_digest for constant-time token comparison, the same
        timing-attack resistance Hermes's own security.py uses.
        """
        if not auth_header:
            return None
        prefix = "Bearer "
        if not auth_header.startswith(prefix):
            return None
        token = auth_header[len(prefix) :].strip()
        if not token:
            return None
        for known_token, peer_id in self._peer_tokens.items():
            if hmac.compare_digest(known_token, token):
                return peer_id
        return None

    # ---- JSON-RPC parsing ----------------------------------------------

    @staticmethod
    def parse_jsonrpc_request(raw_body: Any) -> ParsedA2ARequest:
        """Parse a JSON-RPC 2.0 A2A request body into method/task_id/
        callback_url. Raises ValueError on anything unparseable or using an
        unrecognized method — callers should treat that as a hard reject,
        not attempt best-effort recovery.
        """
        if not isinstance(raw_body, dict):
            raise ValueError("A2A request body must be a JSON object")

        raw_method = raw_body.get("method")
        if not raw_method or not isinstance(raw_method, str):
            raise ValueError("A2A request missing a 'method' field")

        method = _LEGACY_METHOD_ALIASES.get(raw_method)
        if method is None:
            try:
                method = A2AMethod(raw_method)
            except ValueError:
                raise ValueError(f"Unrecognized A2A method: {raw_method!r}") from None

        params = raw_body.get("params") or {}
        if not isinstance(params, dict):
            params = {}

        task_id = params.get("taskId") or params.get("id")
        if not task_id:
            message = params.get("message")
            if isinstance(message, dict):
                task_id = message.get("taskId")

        callback_url = None
        push_config = params.get("pushNotificationConfig")
        if isinstance(push_config, dict):
            callback_url = push_config.get("url")

        return ParsedA2ARequest(
            method=method,
            params=params,
            task_id=task_id,
            callback_url=callback_url,
            request_id=raw_body.get("id"),
        )

    # ---- PII extraction --------------------------------------------------

    @staticmethod
    def extract_text_for_pii_scan(message: Dict[str, Any]) -> Tuple[str, bool]:
        """Flatten an A2A Message's `parts` array to plain text for PII
        scanning.

        Returns (text, skipped_binary). Binary/file/data Parts are never
        scanned as if they were text (that would either produce noisy false
        positives on base64 syntax, or silently miss real PII embedded in a
        file) — they're explicitly flagged as skipped instead, so nothing
        downstream can claim PII coverage this function didn't actually
        provide.
        """
        parts = message.get("parts")
        if not isinstance(parts, list):
            return "", False

        text_chunks = []
        skipped_binary = False
        for part in parts:
            if not isinstance(part, dict):
                continue
            if "text" in part and isinstance(part["text"], str):
                text_chunks.append(part["text"])
            elif "file" in part or "data" in part:
                skipped_binary = True
        return "".join(text_chunks), skipped_binary

    # ---- inbound request ---------------------------------------------

    async def process_inbound_request(
        self,
        raw_body: Any,
        auth_header: Optional[str],
        source_ip: str,
    ) -> A2AProxyResult:
        start = time.monotonic()
        result = A2AProxyResult()

        peer_id = self.resolve_peer_id(auth_header)
        if peer_id is None:
            result.block_reason = "missing or invalid A2A auth token"
            await self._audit(result, source_ip, severity="warning")
            return result
        result.peer_id = peer_id

        try:
            parsed = self.parse_jsonrpc_request(raw_body)
        except ValueError as exc:
            result.block_reason = f"malformed A2A request: {exc}"
            await self._audit(result, source_ip, severity="warning")
            return result
        result.method = parsed.method.value

        decision = await self._policy_engine.enforce(
            peer_id,
            parsed.method,
            task_id=parsed.task_id,
            callback_url=parsed.callback_url,
        )
        result.matched_rule = decision.matched_rule
        if not decision.allowed:
            result.block_reason = decision.reason
            await self._audit(result, source_ip, severity="warning")
            return result

        result.allowed = True
        result.blocked = False

        # PII scan + redact the outgoing body before it ever reaches Hermes.
        forward_body = raw_body
        message = parsed.params.get("message")
        if self._pii_detector is not None and isinstance(message, dict):
            text, skipped_binary = self.extract_text_for_pii_scan(message)
            result.pii_scan_skipped_binary = skipped_binary
            if text:
                report = self._pii_detector.scan_tool_result(
                    tool_name=f"a2a:{peer_id}", content=text
                )
                if report.has_pii:
                    result.pii_redaction_count = len(report.hits)
                    forward_body = _redact_message_text(raw_body, report.redacted_content)

        forwarded_json = json.dumps(forward_body)
        result.forwarded_body = forwarded_json

        if self._forwarder is not None:
            status, body = await self._forwarder.forward(body=forwarded_json)
            result.upstream_status = status
            result.upstream_body = body

        result.processing_time_ms = (time.monotonic() - start) * 1000
        await self._audit(result, source_ip, severity="info")
        return result

    # ---- agent-card discovery -----------------------------------------

    async def process_agent_card_request(self, source_ip: str) -> A2AProxyResult:
        """GET /.well-known/agent-card.json — never policy-gated (the A2A
        spec requires open discovery) but always audited, since it's the
        reconnaissance step before an attacker picks an attack method."""
        result = A2AProxyResult(
            allowed=True,
            blocked=False,
            matched_rule="discovery_passthrough",
        )
        if self._forwarder is not None:
            status, body = await self._forwarder.forward(body="")
            result.upstream_status = status
            result.upstream_body = body
        await self._audit(result, source_ip, severity="info")
        return result

    # ---- audit -----------------------------------------------------------

    async def _audit(self, result: A2AProxyResult, source_ip: str, severity: str) -> None:
        try:
            from gateway.security.module_stats import record_decision

            record_decision("a2a_proxy", result.allowed)
        except Exception:  # pragma: no cover - telemetry must never raise
            pass

        if self._audit_store is None:
            return
        try:
            event = await self._audit_store.log_event(
                event_type="a2a_request",
                severity=severity,
                details={
                    "peer_id": result.peer_id,
                    "method": result.method,
                    "allowed": result.allowed,
                    "matched_rule": result.matched_rule,
                    "block_reason": result.block_reason,
                    "source_ip": source_ip,
                    "pii_redaction_count": result.pii_redaction_count,
                },
                source_module="a2a_proxy",
                bot_id=self._bot_id,
            )
            result.audit_entry_id = getattr(event, "event_id", "") or ""
        except Exception:  # pragma: no cover - audit failure must never block
            logger.error("A2A proxy audit logging failed (non-fatal)", exc_info=True)


def _redact_message_text(raw_body: Dict[str, Any], redacted_text: str) -> Dict[str, Any]:
    """Return a copy of raw_body with the first text Part's content replaced
    by the PII-redacted version. Deliberately conservative: only touches the
    single concatenated text blob produced by extract_text_for_pii_scan,
    consistent with how it was scanned.
    """
    body = json.loads(json.dumps(raw_body))  # cheap deep copy, JSON-safe by construction
    params = body.get("params") or {}
    message = params.get("message")
    if isinstance(message, dict) and isinstance(message.get("parts"), list):
        replaced = False
        for part in message["parts"]:
            if isinstance(part, dict) and "text" in part and not replaced:
                part["text"] = redacted_text
                replaced = True
            elif isinstance(part, dict) and "text" in part:
                part["text"] = ""
    return body
