# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""TDD — WS-E finding RT-11 (HIGH, deploy): MCP policy engine ships DORMANT.

Before this fix, the ``MCPPolicyEngine`` was instantiated only when the YAML
config contained an ``mcp_policy:`` section. The stock/example config shipped
no such section, so a fresh deployment ran MCP tool calls with the governance
gate DISABLED (``policy_engine=None`` in ``lifespan.py``) — unknown MCP servers
were invoked with no deny-by-default control.

The fix makes ``load_config`` synthesise a conservative, fail-closed default
``mcp_policy_data`` whenever the YAML omits the section:

  * ``default_action: deny`` — unknown servers are DENIED (default-deny).
  * ``allowed_servers`` = the servers actually configured under ``mcp_proxy``,
    so existing/known bots keep working (no breakage).

These tests prove the default config activates the engine fail-closed (unknown
server denied) while known-server calls still succeed.
"""

from __future__ import annotations

from pathlib import Path

from gateway.ingest_api.config import load_config
from gateway.security.mcp_policy import MCPPolicyAction, MCPPolicyConfig, MCPPolicyEngine

# A config with configured MCP servers but NO explicit mcp_policy: section —
# this is exactly the "stock deploy" shape from RT-11.
_YAML_NO_POLICY = """\
security:
  pii_min_confidence: 0.9
  pii_redaction: true
gateway:
  bind: "127.0.0.1"
  port: 8080
  auth_token: "test-token"
logging:
  level: "INFO"
mcp_proxy:
  servers:
    mac-messages:
      transport: http_sse
      url: "http://host.docker.internal:8200"
"""

# A config that DOES author an explicit mcp_policy: section — the operator's
# choice must be honoured verbatim (no silent override by our default).
_YAML_WITH_POLICY = """\
security:
  pii_min_confidence: 0.9
gateway:
  bind: "127.0.0.1"
  port: 8080
  auth_token: "test-token"
logging:
  level: "INFO"
mcp_proxy:
  servers:
    mac-messages:
      transport: http_sse
      url: "http://host.docker.internal:8200"
mcp_policy:
  default_action: allow
  allowed_servers:
    - custom-server
"""


def _write(path: Path, text: str) -> Path:
    path.write_text(text)
    return path


class TestDefaultMcpPolicyIsFailClosed:
    def test_missing_section_yields_deny_by_default_policy(self, tmp_path):
        """A stock config (no mcp_policy:) must produce a non-empty, deny-by-default policy."""
        cfg = load_config(_write(tmp_path / "cfg.yaml", _YAML_NO_POLICY))
        assert cfg.mcp_policy_data, "mcp_policy_data must NOT be empty (engine would stay dormant)"
        assert str(cfg.mcp_policy_data.get("default_action")).lower() == "deny"

    def test_configured_servers_are_allowlisted_by_default(self, tmp_path):
        """Known/configured MCP servers must be carried into the default allowlist
        so existing deployments do not break."""
        cfg = load_config(_write(tmp_path / "cfg.yaml", _YAML_NO_POLICY))
        assert "mac-messages" in cfg.mcp_policy_data.get("allowed_servers", [])

    def test_engine_denies_unknown_server_under_default(self, tmp_path):
        """The synthesised default, fed to the engine, DENIES an unknown server."""
        cfg = load_config(_write(tmp_path / "cfg.yaml", _YAML_NO_POLICY))
        engine = MCPPolicyEngine(MCPPolicyConfig.from_dict(cfg.mcp_policy_data))
        decision = engine.evaluate("evil-server", "tool_exfiltrate", agent_id="attacker")
        assert decision.action is MCPPolicyAction.DENY
        assert decision.allowed is False

    def test_engine_allows_known_server_under_default(self, tmp_path):
        """A known/allowlisted server's non-high-risk tool is still ALLOWED — no breakage."""
        cfg = load_config(_write(tmp_path / "cfg.yaml", _YAML_NO_POLICY))
        engine = MCPPolicyEngine(MCPPolicyConfig.from_dict(cfg.mcp_policy_data))
        decision = engine.evaluate("mac-messages", "tool_get_recent_messages", agent_id="owner")
        assert decision.action is MCPPolicyAction.ALLOW

    def test_engine_requires_approval_for_destructive_tool_on_known_server(self, tmp_path):
        """Fail-closed intent: even on a known server, an obviously destructive
        tool must route through approval (deny-by-default for high-risk)."""
        cfg = load_config(_write(tmp_path / "cfg.yaml", _YAML_NO_POLICY))
        engine = MCPPolicyEngine(MCPPolicyConfig.from_dict(cfg.mcp_policy_data))
        decision = engine.evaluate("mac-messages", "delete_all_chats", agent_id="attacker")
        assert decision.action is MCPPolicyAction.REQUIRE_APPROVAL

    def test_explicit_policy_section_is_not_overridden(self, tmp_path):
        """An operator-authored mcp_policy: section must be honoured verbatim."""
        cfg = load_config(_write(tmp_path / "cfg.yaml", _YAML_WITH_POLICY))
        assert str(cfg.mcp_policy_data.get("default_action")).lower() == "allow"
        assert cfg.mcp_policy_data.get("allowed_servers") == ["custom-server"]


class TestDefaultPolicyNoMcpServers:
    def test_no_mcp_section_still_deny_by_default(self, tmp_path):
        """A config with no mcp_proxy AND no mcp_policy still yields a fail-closed
        default (empty allowlist + deny) — a fresh deploy is locked down, not open."""
        yaml_bare = (
            "security:\n  pii_min_confidence: 0.9\n"
            'gateway:\n  bind: "127.0.0.1"\n  port: 8080\n  auth_token: "t"\n'
            'logging:\n  level: "INFO"\n'
        )
        cfg = load_config(_write(tmp_path / "cfg.yaml", yaml_bare))
        assert cfg.mcp_policy_data
        assert str(cfg.mcp_policy_data.get("default_action")).lower() == "deny"
        engine = MCPPolicyEngine(MCPPolicyConfig.from_dict(cfg.mcp_policy_data))
        assert engine.evaluate("anything", "any_tool").action is MCPPolicyAction.DENY
