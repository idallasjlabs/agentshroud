# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Canvas reverse-proxy upstream wiring regression tests.

The v1.1.0 container rename (agentshroud-bot → agentshroud-openclaw) removed the
"bot" hostname from agentshroud-isolated. The proxy's default upstream silently
kept pointing at the dead name, so every Canvas request 502'd in production with
"[Errno -5] No address associated with hostname". These tests pin the default to
the live container name and verify the env override still works.
"""

from __future__ import annotations

import importlib

import gateway.proxy.canvas_proxy as canvas_proxy


def test_default_upstream_is_current_container_name(monkeypatch):
    monkeypatch.delenv("CANVAS_BOT_URL", raising=False)
    mod = importlib.reload(canvas_proxy)
    assert mod._BOT_CANVAS_URL == "http://agentshroud-openclaw:18789"
    assert "//bot:" not in mod._BOT_CANVAS_URL, (
        "Upstream default regressed to the pre-v1.1.0 'bot' hostname, which no "
        "longer resolves on agentshroud-isolated"
    )


def test_env_override_takes_precedence(monkeypatch):
    monkeypatch.setenv("CANVAS_BOT_URL", "http://example-bot:1234")
    mod = importlib.reload(canvas_proxy)
    assert mod._BOT_CANVAS_URL == "http://example-bot:1234"
    # Restore module state for other tests
    monkeypatch.delenv("CANVAS_BOT_URL", raising=False)
    importlib.reload(canvas_proxy)
