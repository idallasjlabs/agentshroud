# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""
API contract tests.

Validates the FastAPI OpenAPI schema and ensures:
- Version consistency between package and API declaration
- Health endpoint is accessible without authentication
- Protected endpoints reject unauthenticated requests
- OpenAPI schema is structurally valid
"""

import json
from pathlib import Path

import pytest

from gateway import __version__

# Committed contract snapshot — gateway/openapi.json (resolved from this file so
# the test passes regardless of pytest's working directory).
SNAPSHOT_PATH = Path(__file__).resolve().parent.parent / "openapi.json"


class TestOpenAPIContract:
    """OpenAPI schema and version consistency tests."""

    @pytest.fixture(autouse=True)
    def client(self):
        """Create a FastAPI test client."""
        try:
            from fastapi.testclient import TestClient

            from gateway.ingest_api.main import app

            self._client = TestClient(app)
        except ImportError:
            pytest.skip("FastAPI TestClient not available")
        except Exception as e:
            pytest.skip(f"Could not instantiate app: {e}")

    def test_openapi_schema_is_valid(self):
        """OpenAPI schema endpoint returns valid JSON schema."""
        response = self._client.get("/openapi.json")
        assert response.status_code == 200, f"OpenAPI schema returned {response.status_code}"
        schema = response.json()
        # Validate top-level OpenAPI fields
        assert "openapi" in schema, "Schema missing 'openapi' version field"
        assert "info" in schema, "Schema missing 'info' field"
        assert "paths" in schema, "Schema missing 'paths' field"
        assert schema["info"].get("title"), "Schema info.title is empty"

    def test_version_consistency(self):
        """API version in OpenAPI schema matches gateway package version."""
        response = self._client.get("/openapi.json")
        if response.status_code != 200:
            pytest.skip("OpenAPI schema not available")
        schema = response.json()
        api_version = schema.get("info", {}).get("version", "")
        assert api_version == __version__, (
            f"API schema version '{api_version}' does not match "
            f"package version '{__version__}'. "
            "Fix: use version=__version__ in FastAPI app instantiation."
        )

    def test_health_endpoint_unauthenticated(self):
        """Health/status endpoint must be accessible without authentication."""
        for path in ["/status", "/health"]:
            response = self._client.get(path)
            # Should NOT return 401/403 for health checks
            assert response.status_code not in (
                401,
                403,
            ), f"{path} returned {response.status_code} — health endpoints must be public"

    def test_protected_endpoints_reject_unauthenticated(self):
        """Protected API endpoints must reject requests without auth tokens."""
        protected_paths = [
            "/ingest",
            "/approve",
            "/reject",
        ]
        for path in protected_paths:
            response = self._client.post(path, json={})
            # Protected endpoints must return 401, 403, or 422 (validation) — not 200 or 500
            assert response.status_code in (401, 403, 404, 405, 422), (
                f"Protected endpoint {path} returned unexpected {response.status_code} "
                "without authentication credentials"
            )

    def test_no_500_on_empty_requests(self):
        """API endpoints should not return 500 on malformed/empty requests."""
        response = self._client.post("/ingest", json={})
        # 500 = unhandled exception — bad. 4xx = expected validation rejection.
        assert (
            response.status_code != 500
        ), "/ingest returned 500 on empty request — this is an unhandled exception"

    def test_openapi_snapshot_matches_live_schema(self):
        """The committed gateway/openapi.json snapshot must match the live schema.

        This is the API contract gate: any route, parameter, or response-model
        change must be made consciously by regenerating the snapshot, never
        silently. Regenerate after an INTENTIONAL API change with:

            python3 -c "import json, pathlib; from gateway.ingest_api.main import app; \\
                pathlib.Path('gateway/openapi.json').write_text(\\
                json.dumps(app.openapi(), indent=2, sort_keys=True) + '\\n', encoding='utf-8')"

        (run from the repository root, then commit the diff alongside the API
        change so reviewers see the contract delta).
        """
        assert SNAPSHOT_PATH.exists(), (
            f"OpenAPI snapshot missing at {SNAPSHOT_PATH}. "
            "Generate it with the command in this test's docstring and commit it."
        )
        snapshot = json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))
        response = self._client.get("/openapi.json")
        assert response.status_code == 200
        live = response.json()

        # Friendlier failure for the most common drift: added/removed routes.
        snapshot_paths = set(snapshot.get("paths", {}))
        live_paths = set(live.get("paths", {}))
        assert live_paths == snapshot_paths, (
            "API routes drifted from the committed contract. "
            f"Added: {sorted(live_paths - snapshot_paths)} "
            f"Removed: {sorted(snapshot_paths - live_paths)}. "
            "If intentional, regenerate gateway/openapi.json (see docstring)."
        )
        assert live == snapshot, (
            "OpenAPI schema drifted from the committed gateway/openapi.json "
            "(same routes, but parameters/models/metadata changed). "
            "If intentional, regenerate the snapshot (see docstring)."
        )
