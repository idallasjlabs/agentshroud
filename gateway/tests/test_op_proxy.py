# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for POST /credentials/op-proxy endpoint (P2: credential isolation)."""

from unittest.mock import patch, MagicMock

import pytest
from fastapi.testclient import TestClient

from gateway.ingest_api.main import _is_op_reference_allowed, app as gateway_app, auth_dep


# ============================================================
# Unit tests for reference validation helpers
# ============================================================


class TestIsOpReferenceAllowed:

    def test_allowed_path_passes(self):
        assert _is_op_reference_allowed("op://AgentShroud Bot Credentials/API Keys/openai") is True

    def test_allowed_path_different_item(self):
        assert _is_op_reference_allowed("op://AgentShroud Bot Credentials/Email/password") is True

    def test_disallowed_vault_blocked(self):
        assert _is_op_reference_allowed("op://Personal/Logins/bank") is False

    def test_path_traversal_blocked(self):
        assert _is_op_reference_allowed("op://AgentShroud Bot Credentials/../../../etc/passwd") is False

    def test_missing_op_prefix_blocked(self):
        assert _is_op_reference_allowed("http://evil.com") is False

    def test_empty_reference_blocked(self):
        assert _is_op_reference_allowed("") is False


# ============================================================
# Endpoint integration tests
# ============================================================


@pytest.fixture
def client():
    gateway_app.dependency_overrides[auth_dep] = lambda: None
    yield TestClient(gateway_app)
    gateway_app.dependency_overrides.pop(auth_dep, None)


class TestOpProxyEndpoint:

    def test_malformed_reference_returns_422(self, client):
        resp = client.post(
            "/credentials/op-proxy",
            json={"reference": "not-an-op-reference"},
        )
        assert resp.status_code == 422

    def test_disallowed_vault_returns_403(self, client):
        resp = client.post(
            "/credentials/op-proxy",
            json={"reference": "op://Personal/Logins/bank"},
        )
        assert resp.status_code == 403

    def test_path_traversal_returns_403(self, client):
        resp = client.post(
            "/credentials/op-proxy",
            json={"reference": "op://AgentShroud Bot Credentials/../../../etc/passwd"},
        )
        assert resp.status_code == 403

    def test_valid_reference_returns_value(self, client):
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_result.stdout = "sk-secret-key-abc123\n"

        with patch("gateway.ingest_api.main.subprocess.run", return_value=mock_result):
            resp = client.post(
                "/credentials/op-proxy",
                json={"reference": "op://AgentShroud Bot Credentials/API Keys/openai"},
            )

        assert resp.status_code == 200
        data = resp.json()
        assert data["value"] == "sk-secret-key-abc123"

    def test_op_subprocess_failure_returns_502(self, client):
        mock_result = MagicMock()
        mock_result.returncode = 1
        mock_result.stderr = "no such item"

        with patch("gateway.ingest_api.main.subprocess.run", return_value=mock_result):
            resp = client.post(
                "/credentials/op-proxy",
                json={"reference": "op://AgentShroud Bot Credentials/API Keys/openai"},
            )

        assert resp.status_code == 502

    def test_requires_auth(self):
        """Endpoint returns 401 without auth override."""
        from gateway.ingest_api.main import app as real_app
        saved = real_app.dependency_overrides.pop(auth_dep, None)
        try:
            tc = TestClient(real_app, raise_server_exceptions=False)
            resp = tc.post(
                "/credentials/op-proxy",
                json={"reference": "op://AgentShroud Bot Credentials/API Keys/openai"},
            )
            assert resp.status_code in (401, 403)
        finally:
            if saved is not None:
                real_app.dependency_overrides[auth_dep] = saved
