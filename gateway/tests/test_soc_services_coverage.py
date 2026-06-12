# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Coverage tests for gateway/soc/services.py — ServiceManager, socket fallbacks, sidecar probes."""

from __future__ import annotations

import builtins
import errno
import http.client
import io
import json
import os
import shutil
import socket
import struct
from datetime import datetime, timedelta, timezone
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

import gateway.soc.services as services
from gateway.soc.models import HealthStatus, ServiceStatus
from gateway.soc.services import ServiceManager

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


class _FakeResponse:
    def __init__(self, status: int, body: bytes = b""):
        self.status = status
        self._body = body

    def read(self) -> bytes:
        return self._body


class _FakeUnixSocket:
    """Stand-in for socket.socket — records calls, never opens a real fd."""

    def __init__(self, *args, **kwargs):
        self.connected_to = None

    def settimeout(self, timeout):
        self.timeout = timeout

    def connect(self, address):
        self.connected_to = address

    def close(self):
        pass


def _patch_http_connection(monkeypatch, response, raise_on_request=None):
    """Replace http.client.HTTPConnection so the in-function _UnixHTTP subclass
    exercises its connect() override against a fake AF_UNIX socket instead of
    the real Docker daemon socket."""
    requests = []
    monkeypatch.setattr(socket, "socket", _FakeUnixSocket)

    class _FakeConn:
        sock = None

        def __init__(self, host, *args, **kwargs):
            self.host = host

        def request(self, method, path):
            self.connect()  # runs the _UnixHTTP.connect override (fake socket)
            if raise_on_request is not None:
                raise raise_on_request
            requests.append((method, path))

        def getresponse(self):
            return response

    monkeypatch.setattr(http.client, "HTTPConnection", _FakeConn)
    return requests


def _patch_open(monkeypatch, mapping):
    """Intercept builtins.open for specific paths; delegate everything else."""
    real_open = builtins.open

    def _open(path, *args, **kwargs):
        key = str(path)
        if key in mapping:
            val = mapping[key]
            if isinstance(val, BaseException):
                raise val
            return io.StringIO(val)
        return real_open(path, *args, **kwargs)

    monkeypatch.setattr(builtins, "open", _open)


def _patch_exists(monkeypatch, mapping):
    """os.path.exists override for specific paths only."""
    real_exists = os.path.exists

    def _exists(path):
        key = str(path)
        if key in mapping:
            return mapping[key]
        return real_exists(path)

    monkeypatch.setattr(os.path, "exists", _exists)


def _frame(payload: bytes) -> bytes:
    """Build one Docker multiplexed-log frame (stdout)."""
    return b"\x01\x00\x00\x00" + struct.pack(">I", len(payload)) + payload


# ---------------------------------------------------------------------------
# _inspect_via_socket
# ---------------------------------------------------------------------------


class TestInspectViaSocket:
    def test_200_returns_parsed_json(self, monkeypatch):
        body = json.dumps({"Id": "abc123", "State": {"Status": "running"}}).encode()
        reqs = _patch_http_connection(monkeypatch, _FakeResponse(200, body))
        info = services._inspect_via_socket("agentshroud-gateway")
        assert info == {"Id": "abc123", "State": {"Status": "running"}}
        assert reqs == [("GET", "/containers/agentshroud-gateway/json")]

    def test_404_returns_empty_dict(self, monkeypatch):
        _patch_http_connection(monkeypatch, _FakeResponse(404, b"no such container"))
        assert services._inspect_via_socket("gone") == {}

    def test_500_returns_none(self, monkeypatch):
        _patch_http_connection(monkeypatch, _FakeResponse(500, b"daemon error"))
        assert services._inspect_via_socket("broken") is None

    def test_exception_returns_none(self, monkeypatch):
        _patch_http_connection(
            monkeypatch, _FakeResponse(200, b"{}"), raise_on_request=ConnectionError("no sock")
        )
        assert services._inspect_via_socket("agentshroud-gateway") is None


# ---------------------------------------------------------------------------
# Sidecar probes — _check_clamd / _check_fluent_bit / _check_wazuh_agent / _check_openscap
# ---------------------------------------------------------------------------


class TestCheckClamd:
    def test_not_installed(self, monkeypatch):
        monkeypatch.setattr(shutil, "which", lambda *a, **k: None)
        _patch_exists(monkeypatch, {"/usr/sbin/clamd": False})
        assert services._check_clamd() == "not_installed"

    def test_running_via_socket(self, monkeypatch):
        monkeypatch.setattr(shutil, "which", lambda *a, **k: "/usr/sbin/clamd")

        class _OkSock:
            def __init__(self, *a, **k):
                pass

            def settimeout(self, t):
                pass

            def connect(self, addr):
                pass

            def close(self):
                pass

        monkeypatch.setattr(socket, "socket", _OkSock)
        assert services._check_clamd() == "running"

    def test_running_via_proc_scan(self, monkeypatch):
        monkeypatch.setattr(shutil, "which", lambda *a, **k: "/usr/sbin/clamd")

        class _FailSock:
            def __init__(self, *a, **k):
                pass

            def settimeout(self, t):
                pass

            def connect(self, addr):
                raise ConnectionRefusedError("socket not ready")

        monkeypatch.setattr(socket, "socket", _FailSock)
        monkeypatch.setattr(os, "listdir", lambda p: ["1", "notpid", "2"])
        _patch_open(
            monkeypatch,
            {
                "/proc/1/comm": PermissionError("denied"),
                "/proc/2/comm": "clamd\n",
            },
        )
        assert services._check_clamd() == "running"

    def test_standby_when_no_socket_and_no_process(self, monkeypatch):
        monkeypatch.setattr(shutil, "which", lambda *a, **k: "/usr/sbin/clamd")

        class _FailSock:
            def __init__(self, *a, **k):
                pass

            def settimeout(self, t):
                pass

            def connect(self, addr):
                raise ConnectionRefusedError("socket not ready")

        monkeypatch.setattr(socket, "socket", _FailSock)
        monkeypatch.setattr(os, "listdir", lambda p: (_ for _ in ()).throw(OSError("no /proc")))
        assert services._check_clamd() == "standby"


class TestCheckFluentBit:
    def test_not_installed(self, monkeypatch):
        monkeypatch.setattr(shutil, "which", lambda *a, **k: None)
        _patch_exists(monkeypatch, {"/opt/fluent-bit/bin/fluent-bit": False})
        assert services._check_fluent_bit() == "not_installed"

    def test_running_via_pid_file(self, monkeypatch):
        monkeypatch.setattr(shutil, "which", lambda *a, **k: "/usr/bin/fluent-bit")
        _patch_open(monkeypatch, {"/tmp/fluent-bit.pid": "4242\n"})
        monkeypatch.setattr(os, "kill", lambda pid, sig: None)
        assert services._check_fluent_bit() == "running"

    def test_running_via_proc_scan(self, monkeypatch):
        monkeypatch.setattr(shutil, "which", lambda *a, **k: "/usr/bin/fluent-bit")
        monkeypatch.setattr(os, "listdir", lambda p: ["9", "xyz", "10"])
        _patch_open(
            monkeypatch,
            {
                "/tmp/fluent-bit.pid": FileNotFoundError("no pid file"),
                "/proc/9/comm": PermissionError("denied"),
                "/proc/10/comm": "fluent-bit\n",
            },
        )
        assert services._check_fluent_bit() == "running"

    def test_stopped_when_no_pid_and_no_process(self, monkeypatch):
        monkeypatch.setattr(shutil, "which", lambda *a, **k: "/usr/bin/fluent-bit")
        _patch_open(monkeypatch, {"/tmp/fluent-bit.pid": FileNotFoundError("no pid file")})
        monkeypatch.setattr(os, "listdir", lambda p: (_ for _ in ()).throw(OSError("no /proc")))
        assert services._check_fluent_bit() == "stopped"


class TestCheckWazuhAgent:
    def test_not_installed(self, monkeypatch):
        monkeypatch.setattr(shutil, "which", lambda *a, **k: None)
        _patch_exists(monkeypatch, {"/var/ossec/bin/wazuh-agentd": False})
        assert services._check_wazuh_agent() == "not_installed"

    def test_running_via_pid_file(self, monkeypatch):
        monkeypatch.setattr(shutil, "which", lambda *a, **k: "/var/ossec/bin/wazuh-agentd")
        _patch_open(monkeypatch, {"/var/ossec/var/run/wazuh-agentd.pid": "999\n"})
        monkeypatch.setattr(os, "kill", lambda pid, sig: None)
        assert services._check_wazuh_agent() == "running"

    def test_running_when_kill_raises_eperm(self, monkeypatch):
        """EPERM means the process exists but is owned by another user."""
        monkeypatch.setattr(shutil, "which", lambda *a, **k: "/var/ossec/bin/wazuh-agentd")
        _patch_open(monkeypatch, {"/var/ossec/var/run/wazuh-agentd.pid": "999\n"})

        def _kill(pid, sig):
            raise OSError(errno.EPERM, "Operation not permitted")

        monkeypatch.setattr(os, "kill", _kill)
        assert services._check_wazuh_agent() == "running"

    def test_esrch_falls_through_to_proc_scan(self, monkeypatch):
        """Stale PID (ESRCH) is not EPERM — falls through to /proc scan, then standby."""
        monkeypatch.setattr(shutil, "which", lambda *a, **k: "/var/ossec/bin/wazuh-agentd")
        _patch_open(monkeypatch, {"/var/ossec/var/run/wazuh-agentd.pid": "999\n"})

        def _kill(pid, sig):
            raise OSError(errno.ESRCH, "No such process")

        monkeypatch.setattr(os, "kill", _kill)
        monkeypatch.setattr(os, "listdir", lambda p: (_ for _ in ()).throw(OSError("no /proc")))
        assert services._check_wazuh_agent() == "standby"

    def test_running_via_proc_scan(self, monkeypatch):
        monkeypatch.setattr(shutil, "which", lambda *a, **k: "/var/ossec/bin/wazuh-agentd")
        monkeypatch.setattr(os, "listdir", lambda p: ["5", "abc", "6"])
        _patch_open(
            monkeypatch,
            {
                "/var/ossec/var/run/wazuh-agentd.pid": FileNotFoundError("no pid file"),
                "/proc/5/comm": PermissionError("denied"),
                "/proc/6/comm": "wazuh-agentd\n",
            },
        )
        assert services._check_wazuh_agent() == "running"

    def test_standby_when_no_pid_and_no_process(self, monkeypatch):
        monkeypatch.setattr(shutil, "which", lambda *a, **k: "/var/ossec/bin/wazuh-agentd")
        _patch_open(
            monkeypatch,
            {"/var/ossec/var/run/wazuh-agentd.pid": FileNotFoundError("no pid file")},
        )
        monkeypatch.setattr(os, "listdir", lambda p: (_ for _ in ()).throw(OSError("no /proc")))
        assert services._check_wazuh_agent() == "standby"


class TestCheckOpenscap:
    def test_not_installed(self, monkeypatch):
        monkeypatch.setattr(shutil, "which", lambda *a, **k: None)
        assert services._check_openscap() == "not_installed"

    def test_running_when_content_present(self, monkeypatch):
        monkeypatch.setattr(shutil, "which", lambda *a, **k: "/usr/bin/oscap")
        _patch_exists(monkeypatch, {"/usr/share/xml/scap/ssg/content/ssg-debian12-ds.xml": True})
        assert services._check_openscap() == "running"

    def test_stopped_when_content_missing(self, monkeypatch):
        monkeypatch.setattr(shutil, "which", lambda *a, **k: "/usr/bin/oscap")
        _patch_exists(monkeypatch, {"/usr/share/xml/scap/ssg/content/ssg-debian12-ds.xml": False})
        assert services._check_openscap() == "stopped"


# ---------------------------------------------------------------------------
# Status / health mapping
# ---------------------------------------------------------------------------


class TestStatusMappings:
    @pytest.mark.parametrize(
        "raw,expected",
        [
            ("running", ServiceStatus.RUNNING),
            ("RUNNING", ServiceStatus.RUNNING),
            ("stopped", ServiceStatus.STOPPED),
            ("paused", ServiceStatus.PAUSED),
            ("restarting", ServiceStatus.RESTARTING),
            ("exited", ServiceStatus.STOPPED),
            ("dead", ServiceStatus.STOPPED),
            ("created", ServiceStatus.STOPPED),
            ("removing", ServiceStatus.STOPPED),
            ("warp-drive", ServiceStatus.UNKNOWN),
        ],
    )
    def test_engine_status_mapping(self, raw, expected):
        assert services._engine_status_to_service_status(raw) == expected

    @pytest.mark.parametrize(
        "raw,expected",
        [
            ("healthy", HealthStatus.HEALTHY),
            ("Unhealthy", HealthStatus.UNHEALTHY),
            ("starting", HealthStatus.STARTING),
            ("none", HealthStatus.UNKNOWN),
            ("", HealthStatus.UNKNOWN),
            ("bizarre", HealthStatus.UNKNOWN),
        ],
    )
    def test_engine_health_mapping(self, raw, expected):
        assert services._engine_health_to_health(raw) == expected


# ---------------------------------------------------------------------------
# ServiceManager._get_engine
# ---------------------------------------------------------------------------


class TestGetEngine:
    def test_injected_engine_returned(self):
        engine = MagicMock()
        assert ServiceManager(engine=engine)._get_engine() is engine

    def test_resolved_from_runtime_module(self, monkeypatch):
        import gateway.runtime.engine as engine_mod

        sentinel = object()
        monkeypatch.setattr(engine_mod, "get_engine", lambda: sentinel, raising=False)
        assert ServiceManager()._get_engine() is sentinel

    def test_resolution_failure_returns_none(self, monkeypatch):
        import gateway.runtime.engine as engine_mod

        def _boom():
            raise RuntimeError("no container runtime")

        monkeypatch.setattr(engine_mod, "get_engine", _boom, raising=False)
        assert ServiceManager()._get_engine() is None


# ---------------------------------------------------------------------------
# _describe_service / get_service
# ---------------------------------------------------------------------------


def _full_inspect_info(started_at: str) -> dict:
    return {
        "Id": "abcdef1234567890ffff",
        "State": {
            "Status": "running",
            "Health": {"Status": "healthy"},
            "StartedAt": started_at,
            "RestartCount": 2,
        },
        "Image": "sha256:" + "x" * 100,
        "Config": {"Labels": {"org.opencontainers.image.version": "1.2.3"}},
        "NetworkSettings": {
            "Ports": {"8080/tcp": [{"HostPort": "18080"}], "9090/tcp": None},
            "Networks": {"agentshroud-internal": {}, "agentshroud-isolated": {}},
        },
    }


class TestDescribeService:
    def test_full_running_descriptor(self):
        started = (
            (datetime.now(timezone.utc) - timedelta(seconds=120)).isoformat().replace("+00:00", "Z")
        )
        engine = MagicMock()
        engine.inspect.return_value = _full_inspect_info(started)
        sd = ServiceManager(engine=engine).get_service("agentshroud-gateway")
        assert sd.name == "agentshroud-gateway"
        assert sd.status == ServiceStatus.RUNNING
        assert sd.health == HealthStatus.HEALTHY
        assert sd.container_id == "abcdef123456"
        assert sd.restart_count == 2
        assert len(sd.image) == 64
        assert sd.version == "1.2.3"
        assert sd.ports == ["8080/tcp:18080"]  # empty port bindings are skipped
        assert sorted(sd.networks) == ["agentshroud-internal", "agentshroud-isolated"]
        assert sd.uptime_seconds is not None and sd.uptime_seconds >= 100

    def test_zero_started_at_skips_uptime(self):
        engine = MagicMock()
        engine.inspect.return_value = _full_inspect_info("0001-01-01T00:00:00Z")
        sd = ServiceManager(engine=engine).get_service("agentshroud-gateway")
        assert sd.uptime_seconds is None
        assert sd.status == ServiceStatus.RUNNING

    def test_unparseable_started_at_yields_no_uptime(self):
        engine = MagicMock()
        engine.inspect.return_value = _full_inspect_info("not-a-timestamp")
        sd = ServiceManager(engine=engine).get_service("agentshroud-gateway")
        assert sd.uptime_seconds is None
        assert sd.status == ServiceStatus.RUNNING

    def test_malformed_sections_fall_back_to_defaults(self):
        engine = MagicMock()
        engine.inspect.return_value = {
            "Id": "1234567890abcd",
            "State": {"Status": "exited", "Health": "garbage", "StartedAt": ""},
            "Image": "",
            "Config": "not-a-dict",
            "NetworkSettings": "not-a-dict",
        }
        sd = ServiceManager(engine=engine).get_service("agentshroud-gateway")
        assert sd.status == ServiceStatus.STOPPED  # exited → stopped
        assert sd.health == HealthStatus.UNKNOWN  # Health not a dict
        assert sd.version is None  # Config not a dict
        assert sd.ports == [] and sd.networks == []  # NetworkSettings not a dict
        assert sd.image == ""

    def test_empty_info_means_container_not_found(self):
        engine = MagicMock()
        engine.inspect.return_value = {}
        sd = ServiceManager(engine=engine).get_service("agentshroud-openclaw")
        assert sd.status == ServiceStatus.STOPPED

    def test_engine_failure_falls_back_to_socket_then_unknown(self, monkeypatch):
        engine = MagicMock()
        engine.inspect.side_effect = RuntimeError("engine down")
        monkeypatch.setattr(services, "_inspect_via_socket", lambda name: None)
        sd = ServiceManager(engine=engine).get_service("agentshroud-hermes")
        assert sd.status == ServiceStatus.UNKNOWN

    def test_engine_failure_falls_back_to_socket_data(self, monkeypatch):
        engine = MagicMock()
        engine.inspect.side_effect = RuntimeError("engine down")
        monkeypatch.setattr(
            services,
            "_inspect_via_socket",
            lambda name: {"Id": "feedfacecafebeef", "State": {"Status": "paused"}},
        )
        sd = ServiceManager(engine=engine).get_service("agentshroud-hermes")
        assert sd.status == ServiceStatus.PAUSED
        assert sd.container_id == "feedfacecafe"

    def test_parse_exception_returns_unknown(self):
        engine = MagicMock()
        # Id as int makes the [:12] slice raise TypeError → outer except branch
        engine.inspect.return_value = {"Id": 12345, "State": {"Status": "running"}}
        sd = ServiceManager(engine=engine).get_service("agentshroud-gateway")
        assert sd.status == ServiceStatus.UNKNOWN


# ---------------------------------------------------------------------------
# list_services — known containers + internal gateway services
# ---------------------------------------------------------------------------


class TestListServices:
    def test_internal_services_status_mapping(self, monkeypatch):
        from gateway.ingest_api.state import app_state

        engine = MagicMock()
        engine.inspect.return_value = {}  # all containers "not found" → stopped
        monkeypatch.setattr(app_state, "soc_test_up_attr", object(), raising=False)
        monkeypatch.setattr(
            services,
            "_INTERNAL_SERVICE_ATTRS",
            [
                ("svc-attr-up", "soc_test_up_attr", "Up", 1234, None),
                ("svc-attr-down", "soc_test_missing_attr", "Down", 99, None),
                ("svc-fn-not-installed", None, "NI", None, lambda: "not_installed"),
                ("svc-fn-standby", None, "SB", 5678, lambda: "standby"),
                ("svc-fn-weird", None, "W", None, lambda: "bizarre"),
            ],
        )
        result = {d.name: d for d in ServiceManager(engine=engine).list_services()}
        assert len(result) == len(services._KNOWN_SERVICES) + 5

        for known in services._KNOWN_SERVICES:
            assert result[known].status == ServiceStatus.STOPPED
            assert result[known].is_internal is False

        up = result["svc-attr-up"]
        assert up.status == ServiceStatus.RUNNING
        assert up.health == HealthStatus.HEALTHY
        assert up.ports == ["1234/tcp"]
        assert up.is_internal is True
        assert up.uptime_seconds is not None and up.uptime_seconds >= 0
        assert up.networks == ["agentshroud-internal"]

        down = result["svc-attr-down"]
        assert down.status == ServiceStatus.STOPPED
        assert down.health == HealthStatus.UNKNOWN
        assert down.ports == []  # not running → port hidden
        assert down.uptime_seconds is None

        assert result["svc-fn-not-installed"].status == ServiceStatus.NOT_INSTALLED

        standby = result["svc-fn-standby"]
        assert standby.status == ServiceStatus.STANDBY
        assert standby.health == HealthStatus.HEALTHY  # standby counts as healthy
        assert standby.ports == ["5678/tcp"]

        assert result["svc-fn-weird"].status == ServiceStatus.UNKNOWN

    def test_internal_probe_failure_keeps_container_descriptors(self, monkeypatch):
        engine = MagicMock()
        engine.inspect.return_value = {}

        def _boom():
            raise RuntimeError("probe exploded")

        monkeypatch.setattr(
            services,
            "_INTERNAL_SERVICE_ATTRS",
            [("svc-boom", None, "Boom", None, _boom)],
        )
        descriptors = ServiceManager(engine=engine).list_services()
        # Internal probe failure is swallowed; container descriptors still returned.
        assert [d.name for d in descriptors] == list(services._KNOWN_SERVICES)


# ---------------------------------------------------------------------------
# start / stop / restart / update
# ---------------------------------------------------------------------------


class TestLifecycleActions:
    async def test_all_actions_false_without_engine(self):
        mgr = ServiceManager(engine=None)
        # _get_engine resolution is forced to fail
        mgr._get_engine = lambda: None  # type: ignore[method-assign]
        assert await mgr.start_service("x") is False
        assert await mgr.stop_service("x") is False
        assert await mgr.restart_service("x") is False
        assert await mgr.update_service("x") is False

    async def test_start_success_and_failure(self):
        engine = MagicMock()
        mgr = ServiceManager(engine=engine)
        assert await mgr.start_service("agentshroud-openclaw") is True
        engine.start.assert_called_once_with("agentshroud-openclaw")
        engine.start.side_effect = RuntimeError("docker down")
        assert await mgr.start_service("agentshroud-openclaw") is False

    async def test_stop_success_and_failure(self):
        engine = MagicMock()
        mgr = ServiceManager(engine=engine)
        assert await mgr.stop_service("agentshroud-hermes") is True
        engine.stop.assert_called_once_with("agentshroud-hermes")
        engine.stop.side_effect = RuntimeError("docker down")
        assert await mgr.stop_service("agentshroud-hermes") is False

    async def test_restart_success_and_failure(self):
        engine = MagicMock()
        mgr = ServiceManager(engine=engine)
        assert await mgr.restart_service("agentshroud-gateway") is True
        engine.restart.assert_called_once_with("agentshroud-gateway")
        engine.restart.side_effect = RuntimeError("docker down")
        assert await mgr.restart_service("agentshroud-gateway") is False

    async def test_update_pull_then_restart(self):
        engine = MagicMock()
        mgr = ServiceManager(engine=engine)
        assert await mgr.update_service("agentshroud-openclaw") is True
        engine.pull.assert_called_once_with("agentshroud-openclaw")
        engine.restart.assert_called_once_with("agentshroud-openclaw")

    async def test_update_pull_failure_still_restarts(self):
        engine = MagicMock()
        engine.pull.side_effect = RuntimeError("registry unreachable")
        mgr = ServiceManager(engine=engine)
        assert await mgr.update_service("agentshroud-openclaw") is True
        engine.restart.assert_called_once_with("agentshroud-openclaw")

    async def test_update_engine_without_pull_support(self):
        restart = MagicMock()
        engine = SimpleNamespace(restart=restart)  # no .pull attribute
        mgr = ServiceManager(engine=engine)
        assert await mgr.update_service("agentshroud-hermes") is True
        restart.assert_called_once_with("agentshroud-hermes")

    async def test_update_restart_failure_returns_false(self):
        engine = MagicMock()
        engine.restart.side_effect = RuntimeError("cannot restart")
        mgr = ServiceManager(engine=engine)
        assert await mgr.update_service("agentshroud-hermes") is False


# ---------------------------------------------------------------------------
# get_logs + _logs_via_socket
# ---------------------------------------------------------------------------


class TestGetLogs:
    async def test_bytes_payload_is_decoded(self):
        engine = MagicMock()
        engine.logs.return_value = b"alpha\nbeta\ngamma"
        lines = await ServiceManager(engine=engine).get_logs("agentshroud-gateway", tail=2)
        assert lines == ["beta", "gamma"]

    async def test_engine_error_falls_back_to_socket(self, monkeypatch):
        engine = MagicMock()
        engine.logs.side_effect = RuntimeError("engine gone")
        captured = {}

        def _fake_socket_logs(self, name, tail=50):
            captured["tail"] = tail
            return ["module=egress deny", "module=http allow", "module=egress allow"]

        monkeypatch.setattr(ServiceManager, "_logs_via_socket", _fake_socket_logs)
        _patch_exists(monkeypatch, {services._DOCKER_SOCK: True})
        lines = await ServiceManager(engine=engine).get_logs(
            "agentshroud-gateway", tail=3, module_filter="egress"
        )
        assert lines == ["module=egress deny", "module=egress allow"]
        # Filtered fetches widen the pool: min(tail*20, 2000)
        assert captured["tail"] == 60

    async def test_socket_fallback_empty_lines(self, monkeypatch):
        monkeypatch.setattr(ServiceManager, "_logs_via_socket", lambda self, n, tail=50: [])
        _patch_exists(monkeypatch, {services._DOCKER_SOCK: True})
        lines = await ServiceManager(engine=None).get_logs("agentshroud-gateway", tail=5)
        assert lines == []

    async def test_no_engine_no_socket(self, monkeypatch):
        _patch_exists(monkeypatch, {services._DOCKER_SOCK: False})
        mgr = ServiceManager(engine=None)
        mgr._get_engine = lambda: None  # type: ignore[method-assign]
        assert await mgr.get_logs("agentshroud-gateway", tail=5) == []


class TestLogsViaSocket:
    def test_parses_multiplexed_frames(self, monkeypatch):
        body = (
            _frame(b"line1\n")
            + _frame(b"")  # zero-size frame → skipped
            + _frame(b"line2\nline3\n")
            + b"\x01\x00\x00\x00"
            + struct.pack(">I", 100)
            + b"short"  # truncated → break
        )
        _patch_http_connection(monkeypatch, _FakeResponse(200, body))
        lines = ServiceManager(engine=None)._logs_via_socket("agentshroud-gateway", tail=50)
        assert lines == ["line1", "line2", "line3"]

    def test_tail_limit_applied(self, monkeypatch):
        body = b"".join(_frame(f"line{i}\n".encode()) for i in range(10))
        _patch_http_connection(monkeypatch, _FakeResponse(200, body))
        lines = ServiceManager(engine=None)._logs_via_socket("agentshroud-gateway", tail=3)
        assert lines == ["line7", "line8", "line9"]

    def test_non_200_returns_empty(self, monkeypatch):
        _patch_http_connection(monkeypatch, _FakeResponse(404, b"no such container"))
        assert ServiceManager(engine=None)._logs_via_socket("gone") == []

    def test_exception_returns_empty(self, monkeypatch):
        _patch_http_connection(
            monkeypatch, _FakeResponse(200, b""), raise_on_request=ConnectionError("no sock")
        )
        assert ServiceManager(engine=None)._logs_via_socket("agentshroud-gateway") == []
