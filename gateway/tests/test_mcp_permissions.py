"""Tests for MCP permission system."""

import pytest

from gateway.proxy.mcp_config import (
    MCPProxyConfig,
    MCPServerConfig,
    MCPToolConfig,
    MCPTransport,
    PermissionLevel,
)
from gateway.proxy.mcp_permissions import (
    MCPPermissionManager,
    TRUST_PERMISSION_MAP,
)


# === PermissionLevel ordering ===

class TestPermissionLevel:
    def test_read_lt_write(self):
        assert PermissionLevel.READ < PermissionLevel.WRITE

    def test_write_lt_execute(self):
        assert PermissionLevel.WRITE < PermissionLevel.EXECUTE

    def test_execute_lt_admin(self):
        assert PermissionLevel.EXECUTE < PermissionLevel.ADMIN

    def test_admin_ge_read(self):
        assert PermissionLevel.ADMIN >= PermissionLevel.READ

    def test_read_le_read(self):
        assert PermissionLevel.READ <= PermissionLevel.READ

    def test_level_values(self):
        assert PermissionLevel.level_value(PermissionLevel.READ) == 0
        assert PermissionLevel.level_value(PermissionLevel.ADMIN) == 3


# === Trust level mapping ===

class TestTrustMapping:
    def test_trust_0_read_only(self):
        assert TRUST_PERMISSION_MAP[0] == PermissionLevel.READ

    def test_trust_1_write(self):
        assert TRUST_PERMISSION_MAP[1] == PermissionLevel.WRITE

    def test_trust_2_execute(self):
        assert TRUST_PERMISSION_MAP[2] == PermissionLevel.EXECUTE

    def test_trust_3_admin(self):
        assert TRUST_PERMISSION_MAP[3] == PermissionLevel.ADMIN


# === MCPPermissionManager ===

@pytest.fixture
def config():
    return MCPProxyConfig(
        servers={
            "test-server": MCPServerConfig(
                name="test-server",
                min_trust_level=0,
                tools={
                    "read_data": MCPToolConfig(name="read_data", permission_level=PermissionLevel.READ),
                    "write_data": MCPToolConfig(name="write_data", permission_level=PermissionLevel.WRITE),
                    "exec_cmd": MCPToolConfig(name="exec_cmd", permission_level=PermissionLevel.EXECUTE),
                    "admin_op": MCPToolConfig(name="admin_op", permission_level=PermissionLevel.ADMIN),
                    "limited": MCPToolConfig(name="limited", permission_level=PermissionLevel.READ, rate_limit=3),
                },
                allowed_agents=["agent-a", "agent-b"],
                denied_agents=["agent-x"],
            ),
            "restricted": MCPServerConfig(
                name="restricted",
                min_trust_level=2,
                enabled=True,
            ),
            "disabled-server": MCPServerConfig(
                name="disabled-server",
                enabled=False,
            ),
        },
        global_rate_limit=0,
    )


@pytest.fixture
def mgr(config):
    m = MCPPermissionManager(config)
    m.set_trust_level("agent-a", 1)
    m.set_trust_level("agent-b", 3)
    m.set_trust_level("agent-low", 0)
    m.set_trust_level("agent-x", 2)
    return m


class TestTrustLevels:
    def test_set_and_get(self, mgr):
        mgr.set_trust_level("new-agent", 2)
        assert mgr.get_trust_level("new-agent") == 2

    def test_default_trust_is_1(self, mgr):
        assert mgr.get_trust_level("unknown-agent") == 1

    def test_clamp_high(self, mgr):
        mgr.set_trust_level("a", 99)
        assert mgr.get_trust_level("a") == 3

    def test_clamp_low(self, mgr):
        mgr.set_trust_level("a", -5)
        assert mgr.get_trust_level("a") == 0


class TestServerAccess:
    def test_allowed_agent(self, mgr):
        result = mgr.check_agent_server_access("agent-a", "test-server")
        assert result.allowed

    def test_denied_agent(self, mgr):
        result = mgr.check_agent_server_access("agent-x", "test-server")
        assert not result.allowed
        assert "denied" in result.reason.lower()

    def test_not_in_allowlist(self, mgr):
        result = mgr.check_agent_server_access("agent-low", "test-server")
        assert not result.allowed
        assert "allowlist" in result.reason.lower()

    def test_disabled_server(self, mgr):
        result = mgr.check_agent_server_access("agent-a", "disabled-server")
        assert not result.allowed
        assert "disabled" in result.reason.lower()

    def test_unknown_server_default_allow(self, mgr):
        result = mgr.check_agent_server_access("agent-a", "nonexistent")
        assert result.allowed
        assert result.logged_only

    def test_trust_too_low_for_server(self, mgr):
        mgr.set_trust_level("low-agent", 0)
        result = mgr.check_agent_server_access("low-agent", "restricted")
        assert not result.allowed
        assert "trust level" in result.reason.lower()

    def test_trust_sufficient_for_server(self, mgr):
        mgr.set_trust_level("high-agent", 3)
        result = mgr.check_agent_server_access("high-agent", "restricted")
        assert result.allowed


class TestToolPermission:
    def test_read_tool_at_trust_0(self, mgr):
        result = mgr.check_tool_permission("agent-low", "test-server", "read_data")
        assert result.allowed

    def test_write_tool_denied_at_trust_0(self, mgr):
        result = mgr.check_tool_permission("agent-low", "test-server", "write_data")
        assert not result.allowed

    def test_write_tool_allowed_at_trust_1(self, mgr):
        result = mgr.check_tool_permission("agent-a", "test-server", "write_data")
        assert result.allowed

    def test_exec_denied_at_trust_1(self, mgr):
        result = mgr.check_tool_permission("agent-a", "test-server", "exec_cmd")
        assert not result.allowed

    def test_admin_allowed_at_trust_3(self, mgr):
        result = mgr.check_tool_permission("agent-b", "test-server", "admin_op")
        assert result.allowed

    def test_admin_denied_at_trust_2(self, mgr):
        mgr.set_trust_level("agent-mid", 2)
        result = mgr.check_tool_permission("agent-mid", "test-server", "admin_op")
        assert not result.allowed


class TestInferPermission:
    def test_explicit_config(self, mgr, config):
        sc = config.servers["test-server"]
        assert mgr.infer_permission_level("read_data", sc) == PermissionLevel.READ

    def test_pattern_sensitive(self, mgr):
        assert mgr.infer_permission_level("run_shell_command") == PermissionLevel.EXECUTE

    def test_pattern_read(self, mgr):
        assert mgr.infer_permission_level("get_users") == PermissionLevel.READ

    def test_pattern_list(self, mgr):
        assert mgr.infer_permission_level("list_files") == PermissionLevel.READ

    def test_pattern_delete(self, mgr):
        assert mgr.infer_permission_level("delete_record") == PermissionLevel.EXECUTE

    def test_default_write(self, mgr):
        assert mgr.infer_permission_level("do_something_custom") == PermissionLevel.WRITE


class TestRateLimiting:
    def test_no_limit_always_allowed(self, mgr):
        for _ in range(100):
            result = mgr.check_rate_limit("agent-a", "test-server", "read_data")
            assert result.allowed

    def test_rate_limit_enforced(self, mgr):
        # "limited" has rate_limit=3
        for i in range(3):
            result = mgr.check_rate_limit("agent-a", "test-server", "limited")
            assert result.allowed, f"Call {i+1} should be allowed"

        result = mgr.check_rate_limit("agent-a", "test-server", "limited")
        assert not result.allowed
        assert result.rate_limited

    def test_rate_limit_per_agent(self, mgr):
        # Each agent has separate counter
        for _ in range(3):
            mgr.check_rate_limit("agent-a", "test-server", "limited")

        result = mgr.check_rate_limit("agent-b", "test-server", "limited")
        assert result.allowed  # Different agent, fresh counter


class TestCheckAll:
    def test_all_pass(self, mgr):
        result = mgr.check_all("agent-a", "test-server", "read_data")
        assert result.allowed

    def test_server_denied_stops_early(self, mgr):
        result = mgr.check_all("agent-x", "test-server", "read_data")
        assert not result.allowed
        assert "denied" in result.reason.lower()

    def test_permission_denied(self, mgr):
        result = mgr.check_all("agent-a", "test-server", "exec_cmd")
        assert not result.allowed
        assert "trust level" in result.reason.lower()

    def test_full_access(self, mgr):
        result = mgr.check_all("agent-b", "test-server", "admin_op")
        assert result.allowed
