# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Docker Compose Validation Tests — parse and validate compose files."""
from __future__ import annotations


from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).parent.parent.parent


def _load_compose(filename: str) -> dict:
    """Load a docker-compose YAML file."""
    path = REPO_ROOT / filename
    if not path.exists():
        pytest.skip(f"{filename} not found")
    with open(path) as f:
        return yaml.safe_load(f)


def _load_compose_raw(filename: str) -> str:
    """Load raw text of a compose file."""
    path = REPO_ROOT / filename
    if not path.exists():
        pytest.skip(f"{filename} not found")
    return path.read_text()


# --- Example Compose Files ---


class TestMinimalCompose:
    """Validate examples/docker-compose.minimal.yml."""

    @pytest.fixture
    def compose(self):
        return _load_compose("examples/docker-compose.minimal.yml")

    def test_has_gateway_service(self, compose):
        assert "gateway" in compose.get("services", {}), "Must have gateway service"

    def test_has_volumes(self, compose):
        assert "volumes" in compose, "Must define volumes"

    def test_gateway_has_ports(self, compose):
        gateway = compose["services"]["gateway"]
        assert "ports" in gateway, "Minimal gateway should expose ports"


class TestProductionCompose:
    """Validate examples/docker-compose.production.yml."""

    @pytest.fixture
    def compose(self):
        return _load_compose("examples/docker-compose.production.yml")

    def test_has_gateway_service(self, compose):
        assert "gateway" in compose.get("services", {})

    def test_gateway_read_only(self, compose):
        gateway = compose["services"]["gateway"]
        assert (
            gateway.get("read_only") is True
        ), "Production gateway should have read_only rootfs"

    def test_gateway_no_new_privileges(self, compose):
        gateway = compose["services"]["gateway"]
        security_opts = gateway.get("security_opt", [])
        assert any(
            "no-new-privileges" in str(opt) for opt in security_opts
        ), "Production gateway should set no-new-privileges"

    def test_gateway_has_healthcheck(self, compose):
        gateway = compose["services"]["gateway"]
        assert "healthcheck" in gateway, "Production gateway should have healthcheck"

    def test_gateway_has_resource_limits(self, compose):
        gateway = compose["services"]["gateway"]
        deploy = gateway.get("deploy", {})
        limits = deploy.get("resources", {}).get("limits", {})
        assert "memory" in limits, "Should have memory limit"

    def test_gateway_has_pids_limit(self, compose):
        gateway = compose["services"]["gateway"]
        assert "pids_limit" in gateway, "Should have PID limit"

    def test_gateway_ports_bound_to_localhost(self, compose):
        gateway = compose["services"]["gateway"]
        for port in gateway.get("ports", []):
            port_str = str(port)
            assert (
                "127.0.0.1" in port_str
            ), f"Production ports should bind to localhost, got: {port_str}"

    def test_gateway_has_tmpfs(self, compose):
        gateway = compose["services"]["gateway"]
        assert "tmpfs" in gateway, "Production should use tmpfs for temp dirs"

    def test_gateway_has_logging_config(self, compose):
        gateway = compose["services"]["gateway"]
        assert "logging" in gateway, "Production should configure logging driver"

    def test_healthcheck_has_interval(self, compose):
        hc = compose["services"]["gateway"]["healthcheck"]
        assert "interval" in hc
        assert "timeout" in hc
        assert "retries" in hc

    def test_has_volume_definitions(self, compose):
        assert "volumes" in compose
        volumes = compose["volumes"]
        assert "gateway-data" in volumes or len(volumes) > 0


class TestDockerComposeMain:
    """Validate docker/docker-compose.yml (main compose)."""

    @pytest.fixture
    def compose(self):
        return _load_compose("docker/docker-compose.yml")

    def test_file_exists_and_parses(self, compose):
        assert isinstance(compose, dict)
        assert "services" in compose

    def test_has_at_least_one_service(self, compose):
        assert len(compose["services"]) >= 1


class TestAllComposeFilesValid:
    """All compose files should be valid YAML."""

    COMPOSE_FILES = [
        "docker/docker-compose.yml",
        "examples/docker-compose.minimal.yml",
        "examples/docker-compose.production.yml",
    ]

    @pytest.mark.parametrize("compose_file", COMPOSE_FILES)
    def test_valid_yaml(self, compose_file):
        path = REPO_ROOT / compose_file
        if not path.exists():
            pytest.skip(f"{compose_file} not found")
        with open(path) as f:
            data = yaml.safe_load(f)
        assert isinstance(data, dict), f"{compose_file} should parse to a dict"

    @pytest.mark.parametrize("compose_file", COMPOSE_FILES)
    def test_has_services_key(self, compose_file):
        path = REPO_ROOT / compose_file
        if not path.exists():
            pytest.skip(f"{compose_file} not found")
        with open(path) as f:
            data = yaml.safe_load(f)
        assert "services" in data, f"{compose_file} must have 'services' key"
