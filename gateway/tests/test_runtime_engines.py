# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for multi-runtime container abstraction layer.

Covers all three engines (Docker, Podman, Apple Containers),
detection logic, compose generation, security feature mapping,
runtime config, and web API endpoints.
"""
from __future__ import annotations


import os
from unittest.mock import MagicMock, patch

import pytest

# ============================================================
# Runtime detection
# ============================================================


class TestDetectRuntime:
    @patch("shutil.which")
    def test_detect_docker(self, mock_which):
        mock_which.side_effect = lambda x: "/usr/bin/docker" if x == "docker" else None
        from gateway.runtime import detect_runtime

        result = detect_runtime()
        assert "docker" in result
        assert "podman" not in result

    @patch("shutil.which")
    def test_detect_podman(self, mock_which):
        mock_which.side_effect = lambda x: "/usr/bin/podman" if x == "podman" else None
        from gateway.runtime import detect_runtime

        result = detect_runtime()
        assert "podman" in result

    @patch("shutil.which")
    def test_detect_apple(self, mock_which):
        mock_which.side_effect = lambda x: (
            "/usr/bin/container" if x == "container" else None
        )
        from gateway.runtime import detect_runtime

        result = detect_runtime()
        assert "apple" in result

    @patch("shutil.which")
    def test_detect_multiple(self, mock_which):
        mock_which.return_value = "/usr/bin/whatever"
        from gateway.runtime import detect_runtime

        result = detect_runtime()
        assert len(result) == 3

    @patch("shutil.which")
    def test_detect_none(self, mock_which):
        mock_which.return_value = None
        from gateway.runtime import detect_runtime

        result = detect_runtime()
        assert result == []


class TestGetEngine:
    @patch("shutil.which")
    def test_explicit_docker(self, mock_which):
        mock_which.return_value = "/usr/bin/docker"
        from gateway.runtime import get_engine
        from gateway.runtime.docker_engine import DockerEngine

        engine = get_engine("docker")
        assert isinstance(engine, DockerEngine)

    @patch("shutil.which")
    def test_explicit_podman(self, mock_which):
        mock_which.return_value = "/usr/bin/podman"
        from gateway.runtime import get_engine
        from gateway.runtime.podman_engine import PodmanEngine

        engine = get_engine("podman")
        assert isinstance(engine, PodmanEngine)

    @patch("shutil.which")
    def test_explicit_apple(self, mock_which):
        mock_which.return_value = "/usr/bin/container"
        from gateway.runtime import get_engine
        from gateway.runtime.apple_engine import AppleContainerEngine

        engine = get_engine("apple")
        assert isinstance(engine, AppleContainerEngine)

    def test_invalid_runtime(self):
        from gateway.runtime import get_engine

        with pytest.raises(ValueError, match="Unknown runtime"):
            get_engine("kubernetes")

    @patch("shutil.which")
    def test_auto_detect_priority(self, mock_which):
        # All available — should pick docker (highest priority)
        mock_which.return_value = "/usr/bin/whatever"
        from gateway.runtime import get_engine
        from gateway.runtime.docker_engine import DockerEngine

        engine = get_engine()
        assert isinstance(engine, DockerEngine)

    @patch("shutil.which")
    def test_no_runtime_available(self, mock_which):
        mock_which.return_value = None
        from gateway.runtime import get_engine

        with pytest.raises(RuntimeError, match="No container runtime"):
            get_engine()


# ============================================================
# Docker Engine
# ============================================================


class TestDockerEngine:
    def setup_method(self):
        from gateway.runtime.docker_engine import DockerEngine

        self.engine = DockerEngine()

    @patch("subprocess.run")
    def test_build(self, mock_run):
        mock_run.return_value = MagicMock(stdout="sha256:abc123\n", returncode=0)
        self.engine.build("Dockerfile", "myimage:latest", ".")
        assert mock_run.called
        args = mock_run.call_args[0][0]
        assert "build" in args
        assert "-t" in args
        assert "myimage:latest" in args

    @patch("subprocess.run")
    def test_build_with_args(self, mock_run):
        mock_run.return_value = MagicMock(stdout="ok\n", returncode=0)
        self.engine.build("Dockerfile", "img:v1", ".", build_args={"FOO": "bar"})
        args = mock_run.call_args[0][0]
        assert "--build-arg" in args
        assert "FOO=bar" in args

    @patch("subprocess.run")
    def test_pull(self, mock_run):
        mock_run.return_value = MagicMock(stdout="pulled\n", returncode=0)
        self.engine.pull("nginx:latest")
        args = mock_run.call_args[0][0]
        assert args == ["docker", "pull", "nginx:latest"]

    @patch("subprocess.run")
    def test_push(self, mock_run):
        mock_run.return_value = MagicMock(stdout="pushed\n", returncode=0)
        self.engine.push("myimg:latest")
        args = mock_run.call_args[0][0]
        assert "push" in args

    @patch("subprocess.run")
    def test_run_basic(self, mock_run):
        mock_run.return_value = MagicMock(stdout="container123\n", returncode=0)
        self.engine.run("nginx:latest", "web")
        args = mock_run.call_args[0][0]
        assert "run" in args
        assert "--name" in args
        assert "web" in args
        assert "-d" in args
        assert "--security-opt=no-new-privileges" in args

    @patch("subprocess.run")
    def test_run_with_options(self, mock_run):
        mock_run.return_value = MagicMock(stdout="c1\n", returncode=0)
        self.engine.run(
            "img",
            "c1",
            ports={"8080": "80"},
            volumes={"/data": "/app/data"},
            env={"KEY": "val"},
            read_only=True,
            seccomp="/path/to/seccomp.json",
        )
        args = mock_run.call_args[0][0]
        assert "--read-only" in args
        assert any("seccomp=" in a for a in args)
        assert "-p" in args
        assert "-v" in args
        assert "-e" in args

    @patch("subprocess.run")
    def test_stop(self, mock_run):
        mock_run.return_value = MagicMock(stdout="", returncode=0)
        self.engine.stop("web", timeout=15)
        args = mock_run.call_args[0][0]
        assert "stop" in args
        assert "15" in args

    @patch("subprocess.run")
    def test_rm(self, mock_run):
        mock_run.return_value = MagicMock(stdout="", returncode=0)
        self.engine.rm("web")
        args = mock_run.call_args[0][0]
        assert "rm" in args
        assert "-f" not in args

    @patch("subprocess.run")
    def test_rm_force(self, mock_run):
        mock_run.return_value = MagicMock(stdout="", returncode=0)
        self.engine.rm("web", force=True)
        args = mock_run.call_args[0][0]
        assert "-f" in args

    @patch("subprocess.run")
    def test_pause_unpause(self, mock_run):
        mock_run.return_value = MagicMock(stdout="", returncode=0)
        self.engine.pause("web")
        assert "pause" in mock_run.call_args[0][0]
        self.engine.unpause("web")
        assert "unpause" in mock_run.call_args[0][0]

    @patch("subprocess.run")
    def test_ps(self, mock_run):
        mock_run.return_value = MagicMock(
            stdout='{"Names":"web","ID":"abc","Image":"nginx","Status":"Up 2h"}\n',
            returncode=0,
        )
        containers = self.engine.ps()
        assert len(containers) == 1
        assert containers[0].name == "web"
        assert containers[0].image == "nginx"

    @patch("subprocess.run")
    def test_ps_empty(self, mock_run):
        mock_run.return_value = MagicMock(stdout="", returncode=0)
        containers = self.engine.ps()
        assert containers == []

    @patch("subprocess.run")
    def test_logs(self, mock_run):
        mock_run.return_value = MagicMock(
            stdout="log line 1\nlog line 2\n", returncode=0
        )
        logs = self.engine.logs("web", tail=50)
        assert "log line" in logs
        args = mock_run.call_args[0][0]
        assert "50" in args

    @patch("subprocess.run")
    def test_exec(self, mock_run):
        mock_run.return_value = MagicMock(stdout="output\n", returncode=0)
        result = self.engine.exec("web", ["ls", "-la"])
        assert "output" in result

    @patch("subprocess.run")
    def test_inspect(self, mock_run):
        mock_run.return_value = MagicMock(
            stdout='[{"Id":"abc","Name":"web"}]', returncode=0
        )
        info = self.engine.inspect("web")
        assert info["Id"] == "abc"

    @patch("subprocess.run")
    def test_network_create(self, mock_run):
        mock_run.return_value = MagicMock(stdout="net123\n", returncode=0)
        self.engine.network_create("mynet")
        args = mock_run.call_args[0][0]
        assert "network" in args
        assert "create" in args

    @patch("subprocess.run")
    def test_network_create_internal(self, mock_run):
        mock_run.return_value = MagicMock(stdout="net123\n", returncode=0)
        self.engine.network_create("mynet", internal=True)
        args = mock_run.call_args[0][0]
        assert "--internal" in args

    @patch("subprocess.run")
    def test_volume_create(self, mock_run):
        mock_run.return_value = MagicMock(stdout="vol\n", returncode=0)
        self.engine.volume_create("data")
        args = mock_run.call_args[0][0]
        assert "volume" in args
        assert "create" in args

    @patch("subprocess.run")
    def test_compose_up(self, mock_run):
        mock_run.return_value = MagicMock(stdout="", returncode=0)
        self.engine.compose_up("docker-compose.yml")
        args = mock_run.call_args[0][0]
        assert "compose" in args
        assert "up" in args
        assert "-d" in args

    @patch("subprocess.run")
    def test_compose_down(self, mock_run):
        mock_run.return_value = MagicMock(stdout="", returncode=0)
        self.engine.compose_down("docker-compose.yml")
        args = mock_run.call_args[0][0]
        assert "down" in args

    @patch("subprocess.run")
    def test_health_check_ok(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0, stdout="")
        assert self.engine.health_check() is True

    @patch("subprocess.run")
    def test_health_check_fail(self, mock_run):
        mock_run.side_effect = Exception("not found")
        assert self.engine.health_check() is False


# ============================================================
# Podman Engine
# ============================================================


class TestPodmanEngine:
    def setup_method(self):
        with patch("shutil.which", return_value=None):
            from gateway.runtime.podman_engine import PodmanEngine

            self.engine = PodmanEngine()

    @patch("subprocess.run")
    def test_run_selinux_volumes(self, mock_run):
        mock_run.return_value = MagicMock(stdout="c1\n", returncode=0)
        self.engine.run("img", "c1", volumes={"/data": "/app"})
        args = mock_run.call_args[0][0]
        # Podman should add :z for SELinux
        joined = " ".join(args)
        assert ":z" in joined

    @patch("subprocess.run")
    def test_ps_json(self, mock_run):
        mock_run.return_value = MagicMock(
            stdout='[{"Names":["web"],"Id":"abc","Image":"nginx","State":"running"}]',
            returncode=0,
        )
        containers = self.engine.ps()
        assert len(containers) == 1
        assert containers[0].name == "web"

    @patch("subprocess.run")
    def test_generate_systemd(self, mock_run):
        mock_run.return_value = MagicMock(
            stdout="[Unit]\nDescription=...", returncode=0
        )
        result = self.engine.generate_systemd("web")
        assert "[Unit]" in result

    @patch("subprocess.run")
    def test_health_check(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0, stdout="")
        assert self.engine.health_check() is True


# ============================================================
# Apple Container Engine
# ============================================================


class TestAppleContainerEngine:
    def setup_method(self):
        from gateway.runtime.apple_engine import AppleContainerEngine

        self.engine = AppleContainerEngine()

    @patch("subprocess.run")
    def test_run_ignores_seccomp(self, mock_run):
        mock_run.return_value = MagicMock(stdout="c1\n", returncode=0)
        self.engine.run(
            "img", "c1", seccomp="/path", caps=["NET_ADMIN"], privileged=True
        )
        args = mock_run.call_args[0][0]
        # Apple should NOT pass seccomp, caps, or privileged
        assert "seccomp" not in " ".join(args)
        assert "--privileged" not in args
        assert "--cap-add" not in args

    @patch("subprocess.run")
    def test_ps_text_parse(self, mock_run):
        mock_run.return_value = MagicMock(
            stdout="ID      NAME    IMAGE     STATUS\nabc123  web     nginx     running\n",
            returncode=0,
        )
        containers = self.engine.ps()
        assert len(containers) == 1
        assert containers[0].id == "abc123"

    @patch("subprocess.run")
    def test_pause_fallback(self, mock_run):
        mock_run.side_effect = [
            Exception("not supported"),
            MagicMock(stdout="", returncode=0),
        ]
        # Should not raise — falls back to stop
        self.engine.pause("web")

    def test_compose_not_supported(self):
        with pytest.raises(NotImplementedError):
            self.engine.compose_up("docker-compose.yml")
        with pytest.raises(NotImplementedError):
            self.engine.compose_down("docker-compose.yml")

    @patch("subprocess.run")
    def test_health_check(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0, stdout="1.0.0")
        assert self.engine.health_check() is True

    @patch("subprocess.run")
    def test_inspect_non_json(self, mock_run):
        mock_run.return_value = MagicMock(stdout="not json", returncode=0)
        result = self.engine.inspect("web")
        assert "raw" in result

    @patch("subprocess.run")
    def test_network_graceful_fail(self, mock_run):
        mock_run.side_effect = [
            Exception("not supported"),
            MagicMock(stdout="", returncode=0),
        ]
        # Should not raise
        self.engine.network_create("mynet")
        self.engine.network_rm("mynet")
        self.engine.volume_create("myvol")
        self.engine.volume_rm("myvol")


# ============================================================
# Runtime Config
# ============================================================


class TestRuntimeConfig:
    def test_from_env_defaults(self):
        from gateway.runtime.config import RuntimeConfig

        with patch.dict(os.environ, {}, clear=True):
            config = RuntimeConfig.from_env()
            assert config.runtime is None
            assert config.rootless is None
            assert config.compose_file == "docker-compose.secure.yml"

    def test_from_env_set(self):
        from gateway.runtime.config import RuntimeConfig

        with patch.dict(
            os.environ,
            {
                "AGENTSHROUD_RUNTIME": "podman",
                "AGENTSHROUD_ROOTLESS": "true",
                "AGENTSHROUD_COMPOSE_FILE": "custom.yml",
            },
        ):
            config = RuntimeConfig.from_env()
            assert config.runtime == "podman"
            assert config.rootless is True
            assert config.compose_file == "custom.yml"

    def test_from_dict(self):
        from gateway.runtime.config import RuntimeConfig

        config = RuntimeConfig.from_dict({"runtime": "apple", "rootless": False})
        assert config.runtime == "apple"
        assert config.rootless is False

    def test_effective_rootless_podman(self):
        from gateway.runtime.config import RuntimeConfig

        config = RuntimeConfig(runtime="podman")
        assert config.effective_rootless is True

    def test_effective_rootless_docker(self):
        from gateway.runtime.config import RuntimeConfig

        config = RuntimeConfig(runtime="docker")
        assert config.effective_rootless is False

    def test_effective_rootless_override(self):
        from gateway.runtime.config import RuntimeConfig

        config = RuntimeConfig(runtime="podman", rootless=False)
        assert config.effective_rootless is False


# ============================================================
# Security Features
# ============================================================


class TestSecurityFeatures:
    def test_get_features_docker(self):
        from gateway.runtime.security import get_features_for_runtime

        features = get_features_for_runtime("docker")
        names = [f.name for f in features]
        assert "seccomp" in names
        assert "cap_drop" in names
        assert "vm_isolation" not in names

    def test_get_features_podman(self):
        from gateway.runtime.security import get_features_for_runtime

        features = get_features_for_runtime("podman")
        names = [f.name for f in features]
        assert "rootless" in names
        assert "selinux" in names

    def test_get_features_apple(self):
        from gateway.runtime.security import get_features_for_runtime

        features = get_features_for_runtime("apple")
        names = [f.name for f in features]
        assert "vm_isolation" in names
        assert "rootless" in names

    def test_missing_features(self):
        from gateway.runtime.security import get_missing_features

        missing = get_missing_features("docker")
        names = [f.name for f in missing]
        assert "vm_isolation" in names
        assert "rootless" in names

    def test_security_comparison(self):
        from gateway.runtime.security import get_security_comparison

        comp = get_security_comparison()
        assert "seccomp" in comp
        assert comp["seccomp"]["docker"] is True
        assert comp["seccomp"]["apple"] is False
        assert comp["vm_isolation"]["apple"] is True

    def test_warn_missing(self):
        from gateway.runtime.security import warn_missing_features

        warnings = warn_missing_features("docker")
        assert len(warnings) > 0
        assert any("vm_isolation" in w for w in warnings)

    def test_security_options_docker(self):
        from gateway.runtime.security import get_security_options

        opts = get_security_options("docker")
        assert "security_opt" in opts
        assert "cap_drop" in opts

    def test_security_options_podman(self):
        from gateway.runtime.security import get_security_options

        opts = get_security_options("podman")
        assert "userns" in opts

    def test_security_options_apple(self):
        from gateway.runtime.security import get_security_options

        opts = get_security_options("apple")
        assert "notes" in opts

    def test_security_options_unknown(self):
        import pytest
        from gateway.runtime.security import get_security_options

        with pytest.raises(ValueError, match="Invalid runtime"):
            get_security_options("lxc")


# ============================================================
# Compose Generator
# ============================================================


class TestComposeGenerator:
    def test_generate_docker_compose(self):
        from gateway.runtime.compose_generator import generate_compose

        result = generate_compose(runtime="docker")
        assert "services:" in result
        assert "gateway:" in result
        assert "openclaw:" in result
        assert "networks:" in result
        assert "volumes:" in result

    def test_generate_podman_compose(self):
        from gateway.runtime.compose_generator import generate_compose

        result = generate_compose(runtime="podman")
        assert ":z" in result  # SELinux labels

    def test_generate_custom_services(self):
        from gateway.runtime.compose_generator import generate_compose, ServiceDef

        services = [ServiceDef(name="test", image="test:latest", ports=["8080:80"])]
        result = generate_compose(services=services, runtime="docker")
        assert "test:" in result
        assert "8080:80" in result

    def test_generate_apple_script(self):
        from gateway.runtime.compose_generator import generate_apple_script

        result = generate_apple_script()
        assert "#!/bin/zsh" in result
        assert "container run" in result
        assert "up" in result
        assert "down" in result

    def test_apple_script_custom_services(self):
        from gateway.runtime.compose_generator import generate_apple_script, ServiceDef

        services = [ServiceDef(name="myapp", image="app:v1", ports=["3000:3000"])]
        result = generate_apple_script(services=services)
        assert "myapp" in result
        assert "3000:3000" in result

    def test_compose_has_security_opts(self):
        from gateway.runtime.compose_generator import generate_compose

        result = generate_compose(runtime="docker")
        assert "no-new-privileges" in result
        assert "cap_drop" in result
        assert "read_only" in result

    def test_compose_depends_on(self):
        from gateway.runtime.compose_generator import generate_compose

        result = generate_compose(runtime="docker")
        assert "depends_on" in result

    def test_compose_healthcheck(self):
        from gateway.runtime.compose_generator import generate_compose

        result = generate_compose(runtime="docker")
        assert "healthcheck" in result


# ============================================================
# ContainerInfo dataclass
# ============================================================


class TestContainerInfo:
    def test_defaults(self):
        from gateway.runtime.engine import ContainerInfo

        info = ContainerInfo(name="test")
        assert info.name == "test"
        assert info.id == ""
        assert info.ports == {}
        assert info.labels == {}

    def test_with_data(self):
        from gateway.runtime.engine import ContainerInfo

        info = ContainerInfo(name="web", id="abc123", image="nginx", status="running")
        assert info.image == "nginx"
        assert info.status == "running"


# ============================================================
# Web API (using TestClient)
# ============================================================


class TestWebAPI:
    """Test the management API endpoints with mocked runtime."""

    @pytest.fixture
    def client(self):
        from fastapi import FastAPI
        from fastapi.testclient import TestClient
        from gateway.web.api import router, require_auth

        app = FastAPI()
        app.include_router(router)
        app.dependency_overrides[require_auth] = lambda: "test-token"
        return TestClient(app)

    @patch("gateway.web.api._get_engine")
    @patch("gateway.web.api.RuntimeConfig")
    @patch("gateway.web.api.detect_runtime")
    def test_status(self, mock_detect, mock_config, mock_engine, client):
        mock_detect.return_value = ["docker"]
        mock_config_inst = MagicMock()
        mock_config_inst.runtime = "docker"
        mock_config_inst.effective_rootless = False
        mock_config.from_env.return_value = mock_config_inst
        eng = MagicMock()
        eng.name = "docker"
        eng.health_check.return_value = True
        eng.ps.return_value = []
        mock_engine.return_value = eng
        resp = client.get("/api/status")
        assert resp.status_code == 200
        data = resp.json()
        assert "services" in data
        assert "runtime" in data
        assert "system" in data

    @patch("gateway.web.api._get_engine")
    def test_stop_service(self, mock_engine, client):
        eng = MagicMock()
        mock_engine.return_value = eng
        resp = client.post("/api/services/agentshroud-gateway/stop")
        assert resp.status_code == 200

    @patch("gateway.web.api._get_engine")
    def test_killswitch_no_confirm(self, mock_engine, client):
        resp = client.post("/api/killswitch/freeze", json={"confirm": False})
        assert resp.status_code == 400

    @patch("gateway.web.api._get_engine")
    def test_killswitch_invalid_mode(self, mock_engine, client):
        resp = client.post("/api/killswitch/explode", json={"confirm": True})
        assert resp.status_code == 400

    @patch("gateway.web.api._get_engine")
    def test_killswitch_freeze(self, mock_engine, client):
        eng = MagicMock()
        mock_engine.return_value = eng
        resp = client.post("/api/killswitch/freeze", json={"confirm": True})
        assert resp.status_code == 200
        assert resp.json()["status"] == "frozen"

    def test_get_config(self, client):
        resp = client.get("/api/config")
        assert resp.status_code == 200

    def test_export_config(self, client):
        resp = client.get("/api/config/export")
        assert resp.status_code == 200

    @patch("gateway.web.api._get_engine")
    def test_get_logs(self, mock_engine, client):
        eng = MagicMock()
        eng.logs.return_value = "line1\nline2"
        mock_engine.return_value = eng
        resp = client.get("/api/logs?service=agentshroud-gateway&tail=10")
        assert resp.status_code == 200
        assert "logs" in resp.json()

    @patch("subprocess.run")
    def test_check_openclaw_updates(self, mock_run, client):
        mock_run.return_value = MagicMock(stdout="1.2.3\n", returncode=0)
        with patch("gateway.web.api._get_engine") as mock_engine:
            eng = MagicMock()
            eng.exec.return_value = "1.2.2"
            mock_engine.return_value = eng
            resp = client.get("/api/updates/openclaw")
            assert resp.status_code == 200
            data = resp.json()
            assert "current" in data
            assert "latest" in data

    @patch("subprocess.run")
    def test_check_agentshroud_updates(self, mock_run, client):
        mock_run.return_value = MagicMock(stdout="abc1234\n", returncode=0)
        resp = client.get("/api/updates/agentshroud")
        assert resp.status_code == 200

    def test_update_history(self, client):
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(stdout="abc Fix\ndef Add\n", returncode=0)
            resp = client.get("/api/updates/history")
            assert resp.status_code == 200
            assert "history" in resp.json()

    def test_security_report(self, client):
        with patch("gateway.web.api._get_engine") as mock_engine:
            eng = MagicMock()
            eng.name = "docker"
            eng.health_check.return_value = True
            mock_engine.return_value = eng
            resp = client.get("/api/security/report")
            assert resp.status_code == 200


# ============================================================
# Installer API
# ============================================================


class TestInstallerAPI:
    @pytest.fixture
    def client(self):
        from fastapi import FastAPI
        from fastapi.testclient import TestClient
        from gateway.web.installer import router

        app = FastAPI()
        app.include_router(router)
        return TestClient(app)

    def test_prerequisites(self, client):
        resp = client.get("/install/api/prerequisites")
        assert resp.status_code == 200
        data = resp.json()
        assert "checks" in data
        assert "ready" in data

    @patch("gateway.web.installer.detect_runtime")
    def test_runtimes(self, mock_detect, client):
        mock_detect.return_value = ["docker", "podman"]
        resp = client.get("/install/api/runtimes")
        assert resp.status_code == 200
        data = resp.json()
        assert "available" in data
        assert "security_comparison" in data

    def test_install(self, client):
        resp = client.post(
            "/install/api/install",
            json={
                "runtime": "docker",
                "model": "claude-sonnet-4-20250514",
                "security_level": "recommended",
            },
        )
        assert resp.status_code == 200
        assert resp.json()["status"] == "started"

    def test_installer_page(self, client):
        resp = client.get("/install/")
        assert resp.status_code == 200
        assert "AgentShroud" in resp.text


class TestManagementPage:
    @pytest.fixture
    def client(self):
        from fastapi import FastAPI
        from fastapi.testclient import TestClient
        from gateway.web.management import router

        app = FastAPI()
        app.include_router(router)
        return TestClient(app)

    def test_dashboard_page(self, client):
        resp = client.get("/manage/")
        assert resp.status_code == 200
        assert "AgentShroud" in resp.text
        assert "Dashboard" in resp.text


# ============================================================
# Config import/export round-trip
# ============================================================


class TestConfigRoundTrip:
    @pytest.fixture
    def client(self):
        from fastapi import FastAPI
        from fastapi.testclient import TestClient
        from gateway.web.api import router, require_auth

        app = FastAPI()
        app.include_router(router)
        app.dependency_overrides[require_auth] = lambda: "test-token"
        return TestClient(app)

    def test_put_then_get(self, client, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        config_data = {"gateway": {"port": 8080}, "security": {"level": "paranoid"}}
        resp = client.put("/api/config", json={"config": config_data})
        assert resp.status_code == 200
        resp2 = client.get("/api/config")
        assert resp2.status_code == 200
        assert resp2.json()["config"]["gateway"]["port"] == 8080
