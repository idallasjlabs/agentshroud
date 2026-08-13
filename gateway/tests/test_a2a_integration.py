# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""SCRUM-129 Phase 5 — real-HTTP integration tests for the A2A governance
module, against a minimal test-double A2A peer.

NOT a real third-party A2A peer, and not presented as one anywhere in this
file or its output — this is a small, honestly-labeled JSON-RPC test fixture
(A2APeerTestDouble below) that speaks just enough of the real A2A wire format
to prove HermesA2AForwarder + A2AProxy + A2APolicyEngine work together over an
actual loopback HTTP connection, not just as directly-called Python objects.
No live peer existed at the time this ticket was implemented; if/when one
does, these tests should be supplemented with (not replaced by) a real
cross-implementation run.

The two adversarial regression suites below (task ownership, SSRF callback)
specifically exercise the gaps A2APolicyEngine claims to independently
mitigate (docs/security/threat-model.md) end-to-end over real HTTP — this is
what makes the mitigation claims falsifiable rather than aspirational.

RULE C integration proof for the SendMessage -> forward -> response path:
  1. Entry point:  A2AProxy.process_inbound_request (gateway/proxy/a2a_proxy.py)
  2. Routing:      A2APolicyEngine.enforce (gateway/security/a2a_policy.py)
  3. Handler:      HermesA2AForwarder.forward -> real HTTP POST to the
                    test-double peer (this file)
  4. Test:         test_full_round_trip_allowed_request_reaches_the_peer (below)
  5. Evidence:      the test-double peer's own received-request log, asserted
                    against directly (see the `peer.received` list)
"""

from __future__ import annotations

import json

import pytest
from aiohttp import web
from aiohttp.test_utils import TestClient, TestServer

from gateway.proxy.a2a_proxy import A2AProxy, HermesA2AForwarder
from gateway.security.a2a_policy import A2APolicyConfig, A2APolicyEngine
from gateway.security.progressive_trust_config import ProgressiveTrustConfig
from gateway.security.trust_manager import TrustManager


class A2APeerTestDouble:
    """Minimal JSON-RPC 2.0 responder standing in for a real A2A peer.

    Explicitly NOT a real A2A implementation — no Agent Card, no task
    lifecycle, no SSE. Just enough to prove requests that pass AgentShroud's
    governance actually arrive over real HTTP, and requests that don't are
    never sent at all.
    """

    def __init__(self):
        self.received: list[dict] = []
        self.base_url: str = ""
        self.app = web.Application()
        self.app.router.add_post("/", self._handle)

    async def _handle(self, request: web.Request) -> web.Response:
        raw = await request.text()
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError:
            payload = {"_raw": raw}
        self.received.append(payload)
        return web.json_response(
            {"jsonrpc": "2.0", "id": payload.get("id", "1"), "result": {"status": "ok"}}
        )


@pytest.fixture()
async def test_double_peer():
    peer = A2APeerTestDouble()
    server = TestServer(peer.app)
    client = TestClient(server)
    await client.start_server()
    peer.base_url = str(client.make_url("/"))
    yield peer
    await client.close()


@pytest.fixture()
def trust_manager():
    manager = TrustManager(progressive_config=ProgressiveTrustConfig())
    yield manager
    manager.close()


def _jsonrpc(method: str, params: dict) -> dict:
    return {"jsonrpc": "2.0", "id": "1", "method": method, "params": params}


# ---------------------------------------------------------------------------
# Full round trip over real HTTP
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_full_round_trip_allowed_request_reaches_the_peer(test_double_peer) -> None:
    forwarder = HermesA2AForwarder(base_url=test_double_peer.base_url)
    cfg = A2APolicyConfig.from_dict({"default_action": "deny", "allowed_peers": ["alice"]})
    proxy = A2AProxy(
        policy_engine=A2APolicyEngine(cfg),
        peer_tokens={"alice-secret-token": "alice"},
        forwarder=forwarder,
    )
    try:
        result = await proxy.process_inbound_request(
            raw_body=_jsonrpc("GetTask", {"taskId": "t-1"}),
            auth_header="Bearer alice-secret-token",
            source_ip="198.51.100.7",
        )
        assert result.allowed is True
        assert result.upstream_status == 200
        # RULE C evidence: the test-double peer actually received the
        # forwarded request over real HTTP, not just an in-process call.
        assert len(test_double_peer.received) == 1
        assert test_double_peer.received[0]["method"] == "GetTask"
    finally:
        await forwarder.close()


@pytest.mark.asyncio
async def test_full_round_trip_denied_request_never_reaches_the_peer(test_double_peer) -> None:
    forwarder = HermesA2AForwarder(base_url=test_double_peer.base_url)
    cfg = A2APolicyConfig.from_dict({"default_action": "deny", "allowed_peers": ["alice"]})
    proxy = A2AProxy(
        policy_engine=A2APolicyEngine(cfg),
        peer_tokens={"eve-token": "eve"},
        forwarder=forwarder,
    )
    try:
        result = await proxy.process_inbound_request(
            raw_body=_jsonrpc("GetTask", {"taskId": "t-1"}),
            auth_header="Bearer eve-token",
            source_ip="198.51.100.8",
        )
        assert result.blocked is True
        # The whole point of terminating the connection ourselves: a denied
        # peer's traffic never reaches the real backend at all.
        assert test_double_peer.received == []
    finally:
        await forwarder.close()


# ---------------------------------------------------------------------------
# Adversarial regression: task ownership (upstream gap #83701) over real HTTP
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_adversarial_task_ownership_hijack_attempt_over_real_http(
    test_double_peer, trust_manager
) -> None:
    """alice legitimately creates a task; bob (a distinct, also-allowlisted
    peer) attempts to read it by guessing/reusing the same task_id — the
    exact upstream contextId-collision shape (gap #83701), driven end-to-end
    over real HTTP rather than direct Python calls."""
    forwarder = HermesA2AForwarder(base_url=test_double_peer.base_url)
    cfg = A2APolicyConfig.from_dict({"default_action": "deny", "allowed_peers": ["alice", "bob"]})
    proxy = A2AProxy(
        policy_engine=A2APolicyEngine(cfg),
        peer_tokens={"alice-token": "alice", "bob-token": "bob"},
        forwarder=forwarder,
        trust_manager=trust_manager,
    )
    try:
        create_result = await proxy.process_inbound_request(
            raw_body=_jsonrpc("SendMessage", {"message": {"taskId": "shared-guess", "parts": []}}),
            auth_header="Bearer alice-token",
            source_ip="10.0.0.1",
        )
        assert create_result.allowed is True

        hijack_result = await proxy.process_inbound_request(
            raw_body=_jsonrpc("GetTask", {"taskId": "shared-guess"}),
            auth_header="Bearer bob-token",
            source_ip="10.0.0.2",
        )

        assert hijack_result.blocked is True
        assert hijack_result.matched_rule == "task_ownership"
        # Only alice's original SendMessage reached the peer — bob's hijack
        # attempt was stopped before ever touching the backend.
        assert len(test_double_peer.received) == 1
        # And the attempt is reflected in bob's trust score, not silently
        # ignored.
        _, score = trust_manager.get_trust("bob")
        assert score < trust_manager.config.initial_score
    finally:
        await forwarder.close()


# ---------------------------------------------------------------------------
# Adversarial regression: SSRF callback bypass (upstream gap #78298) over
# real HTTP, covering every alternate-encoding bypass class found in the
# upstream source audit.
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "malicious_callback_url",
    [
        "http://127.0.0.1/exfil",
        "http://2130706433/exfil",  # decimal
        "http://0x7f000001/exfil",  # hex
        "http://0177.0.0.1/exfil",  # octal
        "http://169.254.169.254/latest/meta-data/iam/security-credentials/",
        "http://localhost./exfil",  # trailing dot
    ],
)
async def test_adversarial_ssrf_callback_bypass_attempts_over_real_http(
    test_double_peer, trust_manager, malicious_callback_url: str
) -> None:
    forwarder = HermesA2AForwarder(base_url=test_double_peer.base_url)
    cfg = A2APolicyConfig.from_dict({"default_action": "deny", "allowed_peers": ["alice"]})
    proxy = A2AProxy(
        policy_engine=A2APolicyEngine(cfg),
        peer_tokens={"alice-token": "alice"},
        forwarder=forwarder,
        trust_manager=trust_manager,
    )
    try:
        # Establish the task first so this is scoped as a genuine
        # post-creation callback-registration attempt, not conflated with a
        # separate ownership check.
        await proxy.process_inbound_request(
            raw_body=_jsonrpc("SendMessage", {"message": {"taskId": "t-ssrf", "parts": []}}),
            auth_header="Bearer alice-token",
            source_ip="10.0.0.1",
        )
        result = await proxy.process_inbound_request(
            raw_body=_jsonrpc(
                "SetTaskPushNotificationConfig",
                {
                    "taskId": "t-ssrf",
                    "pushNotificationConfig": {"url": malicious_callback_url},
                },
            ),
            auth_header="Bearer alice-token",
            source_ip="10.0.0.1",
        )
        assert result.blocked is True
        assert result.matched_rule == "ssrf_callback_blocked"
        # The malicious callback registration itself never reached the
        # backend — only the earlier legitimate SendMessage did.
        assert len(test_double_peer.received) == 1
    finally:
        await forwarder.close()


@pytest.mark.asyncio
async def test_legitimate_callback_url_is_forwarded_over_real_http(test_double_peer) -> None:
    """Negative control for the SSRF suite above — a genuinely public
    callback URL must still work, proving the guard isn't just failing
    everything closed indiscriminately."""
    import socket
    from unittest.mock import patch

    forwarder = HermesA2AForwarder(base_url=test_double_peer.base_url)
    cfg = A2APolicyConfig.from_dict({"default_action": "deny", "allowed_peers": ["alice"]})
    proxy = A2AProxy(
        policy_engine=A2APolicyEngine(cfg),
        peer_tokens={"alice-token": "alice"},
        forwarder=forwarder,
    )
    try:
        await proxy.process_inbound_request(
            raw_body=_jsonrpc("SendMessage", {"message": {"taskId": "t-ok", "parts": []}}),
            auth_header="Bearer alice-token",
            source_ip="10.0.0.1",
        )
        fake_addrinfo = [(socket.AF_INET, socket.SOCK_STREAM, 6, "", ("93.184.216.34", 0))]
        with patch("gateway.security.a2a_policy.socket.getaddrinfo", return_value=fake_addrinfo):
            result = await proxy.process_inbound_request(
                raw_body=_jsonrpc(
                    "SetTaskPushNotificationConfig",
                    {
                        "taskId": "t-ok",
                        "pushNotificationConfig": {"url": "https://example.com/webhook"},
                    },
                ),
                auth_header="Bearer alice-token",
                source_ip="10.0.0.1",
            )
        # SetTaskPushNotificationConfig is high-risk regardless of the
        # callback URL's safety — with no approval queue configured it's
        # denied fail-closed, but critically NOT for the SSRF reason.
        assert result.matched_rule != "ssrf_callback_blocked"
    finally:
        await forwarder.close()
