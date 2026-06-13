# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Unit tests for the SOC CLI: gateway/cli/main.py + gateway/cli/client.py.

All network boundaries (urllib.urlopen, websockets) are mocked. Tests assert
behavior: emitted output, request shapes, exit codes, and error paths.
"""

from __future__ import annotations

import io
import json
import sys
import types
from unittest.mock import MagicMock
from urllib.error import HTTPError

import pytest
from click.testing import CliRunner

import gateway.cli.client as client_mod
import gateway.cli.main as main_mod
from gateway.cli.client import SCLClient, client_from_env
from gateway.cli.main import _default_format, _is_tty, _output, _print_table, _tail_ws, cli

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


class _FakeHTTPResponse:
    """Context-manager stand-in for the object urlopen() yields."""

    def __init__(self, payload: bytes):
        self._payload = payload

    def read(self) -> bytes:
        return self._payload

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


def _patch_urlopen(monkeypatch, payload: bytes = b'{"ok": true}', error: Exception = None):
    """Patch gateway.cli.client.urlopen; return list of captured Request objects."""
    captured = []

    def fake_urlopen(req, timeout=None):
        captured.append((req, timeout))
        if error is not None:
            raise error
        return _FakeHTTPResponse(payload)

    monkeypatch.setattr(client_mod, "urlopen", fake_urlopen)
    return captured


def _stub_client(monkeypatch, **returns) -> MagicMock:
    """Replace SCLClient in main with a MagicMock factory; return the instance."""
    stub = MagicMock(spec=SCLClient)
    stub.token = "stub-token"
    for name, value in returns.items():
        getattr(stub, name).return_value = value
    monkeypatch.setattr(main_mod, "SCLClient", MagicMock(return_value=stub))
    return stub


_BASE_ARGS = ["--url", "http://gw.test:8080", "--token", "tok-123", "--format", "json"]


def _invoke(args, **kwargs):
    runner = CliRunner()
    return runner.invoke(cli, _BASE_ARGS + args, **kwargs)


def _all_output(result) -> str:
    """stdout + stderr regardless of click version (mix_stderr removed in 8.2)."""
    try:
        return result.output + result.stderr
    except ValueError:
        return result.output


# ---------------------------------------------------------------------------
# SCLClient — request plumbing
# ---------------------------------------------------------------------------


class TestSCLClientRequest:
    def test_init_strips_trailing_slash_and_builds_soc_base(self):
        c = SCLClient("http://localhost:8080/", "tok")
        assert c.base_url == "http://localhost:8080"
        assert c._soc_base == "http://localhost:8080/soc/v1"
        assert c.timeout == 30

    def test_get_builds_url_headers_and_parses_json(self, monkeypatch):
        captured = _patch_urlopen(monkeypatch, payload=b'{"risk": 4}')
        c = SCLClient("http://gw:8080", "secret-tok", timeout=7)
        result = c.get("/security/risk")
        assert result == {"risk": 4}
        req, timeout = captured[0]
        assert req.full_url == "http://gw:8080/soc/v1/security/risk"
        assert req.get_method() == "GET"
        assert req.headers["Authorization"] == "Bearer secret-tok"
        assert req.headers["Content-type"] == "application/json"
        assert req.headers["Accept"] == "application/json"
        assert req.data is None
        assert timeout == 7

    def test_get_with_params_encodes_query_string(self, monkeypatch):
        captured = _patch_urlopen(monkeypatch, payload=b"[]")
        c = SCLClient("http://gw:8080", "t")
        assert c.get("security/events", {"limit": 5, "severity": "high"}) == []
        req, _ = captured[0]
        assert req.full_url == "http://gw:8080/soc/v1/security/events?limit=5&severity=high"

    def test_post_serializes_body(self, monkeypatch):
        captured = _patch_urlopen(monkeypatch)
        c = SCLClient("http://gw:8080", "t")
        assert c.post("/killswitch/freeze", {"confirm": True}) == {"ok": True}
        req, _ = captured[0]
        assert req.get_method() == "POST"
        assert json.loads(req.data.decode()) == {"confirm": True}

    def test_put_and_delete_methods(self, monkeypatch):
        captured = _patch_urlopen(monkeypatch)
        c = SCLClient("http://gw:8080", "t")
        c.put("/groups/g1/mode", {"collab_mode": "local_only"})
        c.delete("/users/u1")
        assert captured[0][0].get_method() == "PUT"
        assert json.loads(captured[0][0].data.decode()) == {"collab_mode": "local_only"}
        assert captured[1][0].get_method() == "DELETE"
        assert captured[1][0].data is None

    def test_empty_response_body_returns_empty_dict(self, monkeypatch):
        _patch_urlopen(monkeypatch, payload=b"")
        c = SCLClient("http://gw:8080", "t")
        assert c.get("/health") == {}

    def test_http_error_with_json_body_returns_parsed_payload(self, monkeypatch):
        err = HTTPError(
            "http://gw:8080/soc/v1/x",
            403,
            "Forbidden",
            None,
            io.BytesIO(b'{"error": true, "code": "CONFIRMATION_REQUIRED"}'),
        )
        try:
            _patch_urlopen(monkeypatch, error=err)
            c = SCLClient("http://gw:8080", "t")
            result = c.post("/services/gateway/restart", {"confirm": False})
            assert result == {"error": True, "code": "CONFIRMATION_REQUIRED"}
        finally:
            err.close()

    def test_http_error_with_non_json_body_returns_error_dict(self, monkeypatch):
        err = HTTPError(
            "http://gw:8080/soc/v1/x", 502, "Bad Gateway", None, io.BytesIO(b"<html>boom</html>")
        )
        try:
            _patch_urlopen(monkeypatch, error=err)
            c = SCLClient("http://gw:8080", "t")
            result = c.get("/services")
            assert result == {"error": True, "code": "502", "message": "Bad Gateway"}
        finally:
            err.close()


# ---------------------------------------------------------------------------
# SCLClient — convenience methods (URL/method/body contracts)
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "call,method,path,body",
    [
        (lambda c: c.get_services(), "GET", "/services", None),
        (
            lambda c: c.restart_service("gateway", confirm=True),
            "POST",
            "/services/gateway/restart",
            {"confirm": True},
        ),
        (
            lambda c: c.stop_service("hermes"),
            "POST",
            "/services/hermes/stop",
            {"confirm": False},
        ),
        (lambda c: c.get_logs("gateway", tail=10), "GET", "/services/gateway/logs?tail=10", None),
        (
            lambda c: c.get_events(severity="high", limit=5),
            "GET",
            "/security/events?limit=5&severity=high",
            None,
        ),
        (lambda c: c.get_events(), "GET", "/security/events?limit=50", None),
        (lambda c: c.get_risk(), "GET", "/security/risk", None),
        (lambda c: c.get_correlation(), "GET", "/security/correlation", None),
        (lambda c: c.get_users(), "GET", "/users", None),
        (
            lambda c: c.add_collaborator("12345"),
            "POST",
            "/users/collaborator",
            {"user_id": "12345"},
        ),
        (lambda c: c.get_egress_pending(), "GET", "/egress/pending", None),
        (lambda c: c.approve_egress("req-1"), "POST", "/egress/req-1/approve", None),
        (lambda c: c.deny_egress("req-2"), "POST", "/egress/req-2/deny", None),
        (
            lambda c: c.block_egress(),
            "POST",
            "/egress/emergency-block",
            {"reason": "CLI emergency block", "confirm": False},
        ),
        (lambda c: c.freeze(confirm=True), "POST", "/killswitch/freeze", {"confirm": True}),
        (lambda c: c.get_health(), "GET", "/health", None),
        (lambda c: c.get_groups(), "GET", "/groups", None),
        (
            lambda c: c.add_group_member("g1", "u9"),
            "POST",
            "/groups/g1/members",
            {"user_id": "u9"},
        ),
        (
            lambda c: c.set_group_mode("g1", "full_access"),
            "PUT",
            "/groups/g1/mode",
            {"collab_mode": "full_access"},
        ),
        (lambda c: c.run_scan("trivy"), "POST", "/scan/trivy", {"confirm": True}),
    ],
)
def test_convenience_methods_hit_expected_endpoints(monkeypatch, call, method, path, body):
    captured = _patch_urlopen(monkeypatch, payload=b'{"ok": true}')
    c = SCLClient("http://gw:8080", "t")
    result = call(c)
    assert result == {"ok": True}
    req, _ = captured[0]
    assert req.get_method() == method
    assert req.full_url == f"http://gw:8080/soc/v1{path}"
    if body is None:
        assert req.data is None
    else:
        assert json.loads(req.data.decode()) == body


# ---------------------------------------------------------------------------
# client_from_env
# ---------------------------------------------------------------------------


class TestClientFromEnv:
    def test_explicit_args_win(self, monkeypatch):
        monkeypatch.setenv("AGENTSHROUD_URL", "http://env:1")
        monkeypatch.setenv("AGENTSHROUD_TOKEN", "env-tok")
        c = client_from_env("http://arg:2", "arg-tok")
        assert c.base_url == "http://arg:2"
        assert c.token == "arg-tok"

    def test_env_token_and_url_used(self, monkeypatch):
        monkeypatch.setenv("AGENTSHROUD_URL", "http://env-host:9090")
        monkeypatch.setenv("AGENTSHROUD_TOKEN", "env-tok")
        monkeypatch.delenv("AGENTSHROUD_GATEWAY_PASSWORD", raising=False)
        c = client_from_env()
        assert c.base_url == "http://env-host:9090"
        assert c.token == "env-tok"

    def test_gateway_password_fallback(self, monkeypatch):
        monkeypatch.delenv("AGENTSHROUD_URL", raising=False)
        monkeypatch.delenv("AGENTSHROUD_TOKEN", raising=False)
        monkeypatch.setenv("AGENTSHROUD_GATEWAY_PASSWORD", "pw-tok")
        c = client_from_env()
        assert c.base_url == "http://localhost:8080"
        assert c.token == "pw-tok"

    def test_missing_token_raises_value_error(self, monkeypatch):
        monkeypatch.delenv("AGENTSHROUD_TOKEN", raising=False)
        monkeypatch.delenv("AGENTSHROUD_GATEWAY_PASSWORD", raising=False)
        with pytest.raises(ValueError, match="No token provided"):
            client_from_env()


# ---------------------------------------------------------------------------
# main.py — formatting helpers
# ---------------------------------------------------------------------------


class TestOutputHelpers:
    def test_is_tty_and_default_format_for_tty(self, monkeypatch):
        fake_stdout = MagicMock()
        fake_stdout.isatty.return_value = True
        monkeypatch.setattr(sys, "stdout", fake_stdout)
        assert _is_tty() is True
        assert _default_format() == "table"

    def test_default_format_for_pipe(self, monkeypatch):
        fake_stdout = MagicMock()
        fake_stdout.isatty.return_value = False
        monkeypatch.setattr(sys, "stdout", fake_stdout)
        assert _is_tty() is False
        assert _default_format() == "json"

    def test_output_json(self, capsys):
        _output({"a": 1}, "json")
        assert json.loads(capsys.readouterr().out) == {"a": 1}

    def test_output_yaml(self, capsys):
        _output({"a": 1, "b": "x"}, "yaml")
        out = capsys.readouterr().out
        assert "a: 1" in out
        assert "b: x" in out

    def test_output_yaml_falls_back_to_json_without_pyyaml(self, monkeypatch, capsys):
        # A None entry in sys.modules makes `import yaml` raise ImportError.
        monkeypatch.setitem(sys.modules, "yaml", None)
        _output({"a": 1}, "yaml")
        assert json.loads(capsys.readouterr().out) == {"a": 1}

    def test_output_table_empty_list(self, capsys):
        _output([], "table")
        assert capsys.readouterr().out.strip() == "(empty)"

    def test_output_table_list_of_dicts(self, capsys):
        rows = [
            {"name": "gateway", "status": "running"},
            {"name": "hermes", "status": "stopped"},
        ]
        _output(rows, "table")
        out = capsys.readouterr().out
        lines = out.splitlines()
        assert lines[0].startswith("NAME")
        assert "STATUS" in lines[0]
        assert set(lines[1]) <= {"-", " "}  # separator row
        assert "gateway" in out and "hermes" in out and "stopped" in out

    def test_output_table_caps_columns_at_eight(self, capsys):
        row = {f"k{i}": i for i in range(10)}
        _output([row], "table")
        header = capsys.readouterr().out.splitlines()[0]
        assert "K7" in header
        assert "K8" not in header and "K9" not in header

    def test_output_table_list_of_scalars(self, capsys):
        _output(["one", "two"], "table")
        assert capsys.readouterr().out.splitlines() == ["one", "two"]

    def test_output_table_dict(self, capsys):
        _output({"risk": "low", "score": 2}, "table")
        out = capsys.readouterr().out
        assert "  risk: low" in out
        assert "  score: 2" in out

    def test_output_table_scalar(self, capsys):
        _output(42, "table")
        assert capsys.readouterr().out.strip() == "42"

    def test_print_table_empty_rows_is_noop(self, capsys):
        _print_table([])
        assert capsys.readouterr().out == ""


# ---------------------------------------------------------------------------
# main.py — CLI commands (CliRunner + stubbed SCLClient)
# ---------------------------------------------------------------------------


class TestGetCommands:
    def test_get_services(self, monkeypatch):
        stub = _stub_client(monkeypatch, get_services=[{"name": "gateway", "status": "running"}])
        result = _invoke(["get", "services"])
        assert result.exit_code == 0
        assert json.loads(result.output) == [{"name": "gateway", "status": "running"}]
        # Client constructed with the URL/token passed on the command line
        factory = main_mod.SCLClient
        assert factory.call_args.args == ("http://gw.test:8080", "tok-123")
        stub.get_services.assert_called_once_with()

    def test_get_events_passes_severity_and_limit(self, monkeypatch):
        stub = _stub_client(monkeypatch, get_events=[{"id": "e1"}])
        result = _invoke(["get", "events", "--severity", "high", "--limit", "5"])
        assert result.exit_code == 0
        assert json.loads(result.output) == [{"id": "e1"}]
        stub.get_events.assert_called_once_with(severity="high", limit=5)

    @pytest.mark.parametrize(
        "subcmd,method,payload",
        [
            ("risk", "get_risk", {"score": 3, "level": "low"}),
            ("correlation", "get_correlation", {"clusters": 0}),
            ("health", "get_health", {"healthy": True}),
            ("users", "get_users", [{"user_id": "1"}]),
            ("groups", "get_groups", [{"group_id": "g1"}]),
            ("egress-pending", "get_egress_pending", [{"request_id": "r1"}]),
        ],
    )
    def test_simple_get_subcommands(self, monkeypatch, subcmd, method, payload):
        stub = _stub_client(monkeypatch, **{method: payload})
        result = _invoke(["get", subcmd])
        assert result.exit_code == 0
        assert json.loads(result.output) == payload
        getattr(stub, method).assert_called_once_with()

    def test_get_logs_echoes_lines(self, monkeypatch):
        stub = _stub_client(monkeypatch, get_logs={"lines": ["line-a", "line-b"]})
        result = _invoke(["get", "logs", "gateway", "--tail", "2"])
        assert result.exit_code == 0
        assert result.output.splitlines() == ["line-a", "line-b"]
        stub.get_logs.assert_called_once_with("gateway", tail=2)

    def test_get_logs_non_dict_result_prints_nothing(self, monkeypatch):
        _stub_client(monkeypatch, get_logs=["not", "a", "dict"])
        result = _invoke(["get", "logs", "gateway"])
        assert result.exit_code == 0
        assert result.output == ""

    def test_default_format_is_json_when_not_tty(self, monkeypatch):
        _stub_client(monkeypatch, get_risk={"score": 1})
        runner = CliRunner()
        result = runner.invoke(
            cli, ["--url", "http://gw.test:8080", "--token", "tok-123", "get", "risk"]
        )
        assert result.exit_code == 0
        assert json.loads(result.output) == {"score": 1}

    def test_token_falls_back_to_gateway_password_env(self, monkeypatch):
        _stub_client(monkeypatch, get_risk={"score": 1})
        runner = CliRunner()
        result = runner.invoke(
            cli,
            ["--url", "http://gw.test:8080", "get", "risk"],
            env={
                "AGENTSHROUD_TOKEN": None,
                "AGENTSHROUD_GATEWAY_PASSWORD": "fallback-pw",
            },
        )
        assert result.exit_code == 0
        assert main_mod.SCLClient.call_args.args == ("http://gw.test:8080", "fallback-pw")


class TestLifecycleCommands:
    def test_restart_service_success(self, monkeypatch):
        stub = _stub_client(monkeypatch, restart_service={"status": "restarted"})
        result = _invoke(["restart", "service", "gateway", "--confirm"])
        assert result.exit_code == 0
        assert json.loads(result.output) == {"status": "restarted"}
        stub.restart_service.assert_called_once_with("gateway", confirm=True)

    def test_restart_service_confirmation_required(self, monkeypatch):
        _stub_client(
            monkeypatch,
            restart_service={"code": "CONFIRMATION_REQUIRED", "message": "destructive op"},
        )
        result = _invoke(["restart", "service", "gateway"])
        assert result.exit_code == 0
        assert "Confirmation required: destructive op" in result.output
        assert "Re-run with --confirm to proceed." in result.output

    def test_stop_service_success(self, monkeypatch):
        stub = _stub_client(monkeypatch, stop_service={"status": "stopped"})
        result = _invoke(["stop", "service", "hermes", "--confirm"])
        assert result.exit_code == 0
        assert json.loads(result.output) == {"status": "stopped"}
        stub.stop_service.assert_called_once_with("hermes", confirm=True)

    def test_stop_service_confirmation_required(self, monkeypatch):
        _stub_client(monkeypatch, stop_service={"code": "CONFIRMATION_REQUIRED"})
        result = _invoke(["stop", "service", "hermes"])
        assert result.exit_code == 0
        assert "Confirmation required. Re-run with --confirm." in result.output

    def test_freeze_success(self, monkeypatch):
        stub = _stub_client(monkeypatch, freeze={"status": "frozen", "paused": 2})
        result = _invoke(["freeze", "--confirm"])
        assert result.exit_code == 0
        assert json.loads(result.output) == {"status": "frozen", "paused": 2}
        stub.freeze.assert_called_once_with(confirm=True)

    def test_freeze_confirmation_required(self, monkeypatch):
        _stub_client(monkeypatch, freeze={"code": "CONFIRMATION_REQUIRED"})
        result = _invoke(["freeze"])
        assert result.exit_code == 0
        assert "Confirmation required. Re-run with --confirm." in result.output


class TestEgressAndAdminCommands:
    def test_approve(self, monkeypatch):
        stub = _stub_client(monkeypatch, approve_egress={"approved": "req-1"})
        result = _invoke(["approve", "req-1"])
        assert result.exit_code == 0
        assert json.loads(result.output) == {"approved": "req-1"}
        stub.approve_egress.assert_called_once_with("req-1")

    def test_deny(self, monkeypatch):
        stub = _stub_client(monkeypatch, deny_egress={"denied": "req-2"})
        result = _invoke(["deny", "req-2"])
        assert result.exit_code == 0
        assert json.loads(result.output) == {"denied": "req-2"}
        stub.deny_egress.assert_called_once_with("req-2")

    def test_add_collaborator(self, monkeypatch):
        stub = _stub_client(monkeypatch, add_collaborator={"user_id": "8506022825"})
        result = _invoke(["add", "collaborator", "8506022825"])
        assert result.exit_code == 0
        assert json.loads(result.output) == {"user_id": "8506022825"}
        stub.add_collaborator.assert_called_once_with("8506022825")

    def test_add_group_member(self, monkeypatch):
        stub = _stub_client(monkeypatch, add_group_member={"group_id": "g1", "user_id": "u2"})
        result = _invoke(["add", "group-member", "g1", "u2"])
        assert result.exit_code == 0
        assert json.loads(result.output) == {"group_id": "g1", "user_id": "u2"}
        stub.add_group_member.assert_called_once_with("g1", "u2")

    def test_set_mode_valid_choice(self, monkeypatch):
        stub = _stub_client(monkeypatch, set_group_mode={"collab_mode": "project_scoped"})
        result = _invoke(["set", "mode", "g1", "project_scoped"])
        assert result.exit_code == 0
        assert json.loads(result.output) == {"collab_mode": "project_scoped"}
        stub.set_group_mode.assert_called_once_with("g1", "project_scoped")

    def test_set_mode_invalid_choice_rejected(self, monkeypatch):
        _stub_client(monkeypatch)
        result = _invoke(["set", "mode", "g1", "god_mode"])
        assert result.exit_code == 2
        assert "Invalid value" in _all_output(result)

    def test_scan(self, monkeypatch):
        stub = _stub_client(monkeypatch, run_scan={"scanner": "trivy", "status": "started"})
        result = _invoke(["scan", "trivy"])
        assert result.exit_code == 0
        assert json.loads(result.output) == {"scanner": "trivy", "status": "started"}
        stub.run_scan.assert_called_once_with("trivy")

    def test_scan_invalid_scanner_rejected(self, monkeypatch):
        _stub_client(monkeypatch)
        result = _invoke(["scan", "nmap"])
        assert result.exit_code == 2
        assert "Invalid value" in _all_output(result)


# ---------------------------------------------------------------------------
# tail command + _tail_ws
# ---------------------------------------------------------------------------


class TestTailCommand:
    def test_tail_runs_stream_and_uses_client_token(self, monkeypatch):
        _stub_client(monkeypatch)
        recorded = {}

        async def fake_tail_ws(url, token, stream, target, severity):
            recorded.update(url=url, token=token, stream=stream, target=target, severity=severity)

        monkeypatch.setattr(main_mod, "_tail_ws", fake_tail_ws)
        runner = CliRunner()
        result = runner.invoke(
            cli,
            [
                "--url",
                "http://gw.test:8080",
                "tail",
                "events",
                "--severity",
                "high",
                "--url",
                "http://gw.test:8080",
            ],
            env={"AGENTSHROUD_TOKEN": None},
        )
        assert result.exit_code == 0
        assert "Connecting to http://gw.test:8080/soc/v1/ws" in result.output
        # Falls back to the group-level client's token when --token is absent
        assert recorded == {
            "url": "http://gw.test:8080",
            "token": "stub-token",
            "stream": "events",
            "target": "",
            "severity": "high",
        }

    def test_tail_keyboard_interrupt_prints_disconnected(self, monkeypatch):
        _stub_client(monkeypatch)

        async def interrupted(*args):
            raise KeyboardInterrupt

        monkeypatch.setattr(main_mod, "_tail_ws", interrupted)
        result = _invoke(["tail", "logs", "gateway", "--token", "tok-123"])
        assert result.exit_code == 0
        assert "Disconnected." in result.output

    def test_tail_import_error_prints_message(self, monkeypatch):
        _stub_client(monkeypatch)

        def missing_dep(*args):
            raise ImportError("no streaming deps")

        monkeypatch.setattr(main_mod, "_tail_ws", missing_dep)
        result = _invoke(["tail", "events", "--token", "tok-123"])
        assert result.exit_code == 0
        assert "asyncio required for streaming." in result.output


class _FakeWS:
    """Async-iterable WebSocket double."""

    def __init__(self, messages):
        self._messages = list(messages)
        self.sent = []

    async def send(self, payload):
        self.sent.append(payload)

    def __aiter__(self):
        return self

    async def __anext__(self):
        if not self._messages:
            raise StopAsyncIteration
        return self._messages.pop(0)


class _FakeConnect:
    def __init__(self, ws):
        self.ws = ws
        self.url = None

    def __call__(self, url):
        self.url = url
        return self

    async def __aenter__(self):
        return self.ws

    async def __aexit__(self, *exc):
        return False


def _install_fake_websockets(monkeypatch, messages):
    ws = _FakeWS(messages)
    connect = _FakeConnect(ws)
    fake_module = types.ModuleType("websockets")
    fake_module.connect = connect
    monkeypatch.setitem(sys.modules, "websockets", fake_module)
    return ws, connect


class TestTailWS:
    async def test_tail_ws_events_stream(self, monkeypatch, capsys):
        ws, connect = _install_fake_websockets(
            monkeypatch,
            [
                json.dumps({"type": "keepalive"}),
                json.dumps(
                    {
                        "type": "security_event",
                        "summary": "PromptGuard blocked injection",
                        "severity": "high",
                        "timestamp": "2026-06-12T10:00:00.123456Z",
                    }
                ),
                "raw-non-json-payload",
            ],
        )
        await _tail_ws("http://gw:8080", "tok", "events", "", None)
        out = capsys.readouterr().out
        assert connect.url == "ws://gw:8080/soc/v1/ws?token=tok"
        assert ws.sent == [json.dumps({"subscribe": ["security_event"]})]
        assert "[2026-06-12T10:00:00] [HIGH    ] PromptGuard blocked injection" in out
        assert "raw-non-json-payload" in out
        assert "keepalive" not in out

    async def test_tail_ws_logs_stream_uses_wss_and_log_filter(self, monkeypatch, capsys):
        ws, connect = _install_fake_websockets(monkeypatch, [])
        await _tail_ws("https://gw:8443", "tok2", "logs", "gateway", "high")
        capsys.readouterr()
        assert connect.url == "wss://gw:8443/soc/v1/ws?token=tok2"
        assert ws.sent == [json.dumps({"subscribe": ["log_event"]})]

    async def test_tail_ws_missing_websockets_package(self, monkeypatch, capsys):
        # A None entry makes `import websockets` raise ImportError.
        monkeypatch.setitem(sys.modules, "websockets", None)
        await _tail_ws("http://gw:8080", "tok", "events", "", None)
        assert "websockets package required" in capsys.readouterr().out


# ---------------------------------------------------------------------------
# main() entrypoint
# ---------------------------------------------------------------------------


def test_main_entrypoint_runs_cli_group(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["agentshroud-soc"])
    with pytest.raises(SystemExit) as exc_info:
        main_mod.main()
    out = capsys.readouterr()
    combined = out.out + out.err
    assert "AgentShroud SOC CLI" in combined
    assert exc_info.value.code in (0, 2)
