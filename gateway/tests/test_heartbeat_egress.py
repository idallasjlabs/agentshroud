# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Verify hc-ping.com (Healthchecks.io) is on the egress allowlist.

Without this CI gate, every Hermes heartbeat ping would silently 403 and the
dead-man's-switch would fire permanently.
"""
from gateway.proxy.web_config import WebProxyConfig


def test_hc_ping_allowed():
    cfg = WebProxyConfig()
    assert cfg.is_domain_allowed("hc-ping.com"), (
        "hc-ping.com must be in WebProxyConfig.allowed_domains so the "
        "Hermes heartbeat can reach Healthchecks.io through the gateway egress proxy"
    )


def test_hc_ping_subdomain_not_blocked():
    cfg = WebProxyConfig()
    # hc-ping.com is an exact-match entry (no wildcard), so subdomains are not
    # auto-allowed — but the domain itself must not appear on the denylist.
    assert not cfg.is_domain_denied("hc-ping.com")
