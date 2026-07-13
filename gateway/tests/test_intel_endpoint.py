# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Tests for POST /api/intel/reports — verified competitive-intel submission (SCRUM-75 PR2).

The endpoint runs the CitationVerifier over a submitted draft; only claims backed
by a re-fetched, allowlisted, live source survive.  All fetching is stubbed (no
real network): endpoint tests inject a fake verifier, and the production
httpx fetcher is tested against a mocked httpx.get.
"""

from __future__ import annotations

from unittest.mock import patch

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

import gateway.web.api as api_module
from gateway.security.citation_verifier import CitationVerifier, FetchOutcome, make_httpx_fetcher
from gateway.web.api import require_auth, router

_SHA = "a" * 64
_ALLOW = {"lakera.ai", "www.lakera.ai"}


class _FakeFetcher:
    def __init__(self, table):
        self._table = table

    def __call__(self, url):
        status, sha = self._table.get(url, (599, None))
        return FetchOutcome(url=url, status=status, content_sha256=sha, fetched_at=1000.0)


@pytest.fixture
def client(tmp_path, monkeypatch):
    # Persist to a temp store, not the real gateway-data volume.
    monkeypatch.setenv("AGENTSHROUD_INTEL_REPORT_PATH", str(tmp_path / "intel"))
    app = FastAPI()
    app.dependency_overrides[require_auth] = lambda: "test-user"
    app.include_router(router)
    with TestClient(app) as c:
        yield c


def _inject_fetcher(monkeypatch, table):
    """Point the endpoint's verifier at a deterministic fake fetcher."""
    monkeypatch.setattr(
        api_module,
        "_intel_verifier",
        lambda: CitationVerifier(fetcher=_FakeFetcher(table), allowed_domains=_ALLOW),
    )


def _draft(**over):
    body = {
        "report_id": "r-1",
        "source": "hermes-cron",
        "summary": "weekly landscape",
        "agentshroud_score": 76,
        "lead_delta": 30,
        "entries": [
            {
                "name": "Lakera",
                "security_score": 40,
                "module_count": 40,
                "notes": "guardrails",
                "candidate_urls": ["https://lakera.ai/pricing"],
            },
            {
                "name": "Ghost",
                "security_score": 1,
                "module_count": 1,
                "candidate_urls": ["https://evil.com/x"],
            },
        ],
    }
    body.update(over)
    return body


# ---------------------------------------------------------------------------
# Endpoint behaviour
# ---------------------------------------------------------------------------


class TestSubmitEndpoint:
    def test_keeps_verified_drops_unverified(self, client, monkeypatch) -> None:
        _inject_fetcher(
            monkeypatch,
            {"https://lakera.ai/pricing": (200, _SHA), "https://evil.com/x": (200, _SHA)},
        )
        resp = client.post("/api/intel/reports", json=_draft())
        assert resp.status_code == 200
        data = resp.json()
        assert data["verified_claims"] == 1
        assert data["dropped_unverified"] == 1
        names = [c["name"] for c in data["report"]["competitors"]]
        assert names == ["Lakera"]
        assert data["report"]["competitors"][0]["sources"][0]["domain"] == "lakera.ai"
        assert len(data["content_hash"]) == 64

    def test_persisted_report_is_retrievable_and_chain_valid(self, client, monkeypatch) -> None:
        _inject_fetcher(monkeypatch, {"https://lakera.ai/pricing": (200, _SHA)})
        post = client.post(
            "/api/intel/reports",
            json=_draft(
                entries=[
                    {
                        "name": "Lakera",
                        "security_score": 40,
                        "module_count": 40,
                        "candidate_urls": ["https://lakera.ai/pricing"],
                    }
                ]
            ),
        )
        assert post.status_code == 200
        # The persisted, verified report is served by the existing GET endpoint.
        got = client.get("/api/intel/competitive")
        assert got.status_code == 200
        body = got.json()
        assert body["chain_valid"] is True
        assert body["report"]["competitors"][0]["sources"][0]["content_sha256"] == _SHA

    def test_all_unverified_yields_empty_report(self, client, monkeypatch) -> None:
        _inject_fetcher(monkeypatch, {})  # every URL -> 599/None (unreachable)
        resp = client.post("/api/intel/reports", json=_draft())
        assert resp.status_code == 200
        data = resp.json()
        assert data["verified_claims"] == 0
        assert data["dropped_unverified"] == 2
        assert data["report"]["competitors"] == []

    def test_missing_required_field_returns_422(self, client, monkeypatch) -> None:
        _inject_fetcher(monkeypatch, {})
        bad = _draft()
        del bad["report_id"]
        resp = client.post("/api/intel/reports", json=bad)
        assert resp.status_code == 422

    def test_too_many_candidate_urls_rejected(self, client, monkeypatch) -> None:
        # Bounded fan-out: >20 URLs on one claim is rejected before any fetch.
        _inject_fetcher(monkeypatch, {})
        bad = _draft(
            entries=[
                {
                    "name": "Flood",
                    "security_score": 1,
                    "module_count": 1,
                    "candidate_urls": [f"https://lakera.ai/{i}" for i in range(21)],
                }
            ]
        )
        resp = client.post("/api/intel/reports", json=bad)
        assert resp.status_code == 422

    def test_too_many_entries_rejected(self, client, monkeypatch) -> None:
        _inject_fetcher(monkeypatch, {})
        bad = _draft(
            entries=[
                {"name": f"c{i}", "security_score": 1, "module_count": 1, "candidate_urls": []}
                for i in range(51)
            ]
        )
        resp = client.post("/api/intel/reports", json=bad)
        assert resp.status_code == 422


class TestSubmitAuth:
    def test_requires_auth(self, tmp_path, monkeypatch) -> None:
        # No require_auth override → the bearer dependency rejects an anonymous call.
        monkeypatch.setenv("AGENTSHROUD_INTEL_REPORT_PATH", str(tmp_path / "intel"))
        app = FastAPI()
        app.include_router(router)
        with TestClient(app) as c:
            resp = c.post("/api/intel/reports", json=_draft())
        assert resp.status_code in (401, 403)


# ---------------------------------------------------------------------------
# Production httpx fetcher
# ---------------------------------------------------------------------------


class _StreamResp:
    """Fake httpx.stream context manager yielding a body in chunks."""

    def __init__(self, status: int, chunks: list[bytes]) -> None:
        self.status_code = status
        self._chunks = chunks

    def __enter__(self):
        return self

    def __exit__(self, *a) -> bool:
        return False

    def iter_bytes(self):
        yield from self._chunks


class TestHttpxFetcher:
    def test_2xx_with_body_is_proven(self) -> None:
        with patch("httpx.stream", return_value=_StreamResp(200, [b"hello ", b"world"])):
            outcome = make_httpx_fetcher()("https://lakera.ai/x")
        assert outcome.status == 200
        assert outcome.ok
        assert outcome.content_sha256 is not None and len(outcome.content_sha256) == 64

    def test_redirect_is_not_proven(self) -> None:
        # follow_redirects=False → a 3xx is a non-2xx → citation rejected (SSRF guard).
        with patch("httpx.stream", return_value=_StreamResp(302, [])) as mock_stream:
            outcome = make_httpx_fetcher()("https://lakera.ai/x")
        assert mock_stream.call_args.kwargs.get("follow_redirects") is False
        assert mock_stream.call_args.kwargs.get("trust_env") is False
        assert not outcome.ok

    def test_empty_body_is_not_proven(self) -> None:
        with patch("httpx.stream", return_value=_StreamResp(200, [])):
            outcome = make_httpx_fetcher()("https://lakera.ai/x")
        assert outcome.content_sha256 is None
        assert not outcome.ok

    def test_oversize_body_is_capped(self) -> None:
        # A huge body must be truncated at the byte budget (memory-DoS guard):
        # the hash is over the capped prefix, not the full stream.
        big = [b"x" * 1024] * 100  # 100 KB of chunks
        with patch("httpx.stream", return_value=_StreamResp(200, big)):
            outcome = make_httpx_fetcher(max_bytes=4096)("https://lakera.ai/x")
        assert outcome.ok  # still proven-live, just capped
        assert outcome.content_sha256 is not None

    def test_network_error_maps_to_599(self) -> None:
        with patch("httpx.stream", side_effect=RuntimeError("boom")):
            outcome = make_httpx_fetcher()("https://lakera.ai/x")
        assert outcome.status == 599
        assert outcome.content_sha256 is None
        assert not outcome.ok
