# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for ReportStore (SCRUM-79) — gateway-managed multi-bot report store."""

from __future__ import annotations

import pytest

from gateway.security.report_store import ReportStore


@pytest.fixture
def store(tmp_path):
    return ReportStore(root=str(tmp_path / "reports"))


class TestSaveAndGet:
    def test_round_trip(self, store):
        rid = store.save(bot="hermes", title="Weekly Intel", content="market is up")
        rec = store.get(rid)
        assert rec is not None
        assert rec["bot"] == "hermes"
        assert rec["title"] == "Weekly Intel"
        assert rec["content"] == "market is up"
        assert rec["id"] == rid
        assert rec["content_sha256"]
        assert rec["created"]

    def test_list_returns_metadata_without_content(self, store):
        store.save(bot="hermes", title="A", content="body-a")
        store.save(bot="openclaw", title="B", content="body-b")
        items = store.list()
        assert len(items) == 2
        # Listing is metadata-only — no content bodies leak into the index.
        assert all("content" not in it for it in items)
        assert {it["bot"] for it in items} == {"hermes", "openclaw"}

    def test_list_filter_by_bot(self, store):
        store.save(bot="hermes", title="A", content="x")
        store.save(bot="openclaw", title="B", content="y")
        assert len(store.list(bot="hermes")) == 1

    def test_get_missing_returns_none(self, store):
        assert store.get("does-not-exist") is None

    def test_tags_preserved(self, store):
        rid = store.save(bot="hermes", title="T", content="c", tags=["intel", "weekly"])
        assert store.get(rid)["tags"] == ["intel", "weekly"]


class TestSecurity:
    def test_pii_redacted_on_save(self, tmp_path):
        def _redact(text: str) -> str:
            return text.replace("555-12-3456", "[SSN]")

        s = ReportStore(root=str(tmp_path / "r"), sanitize_fn=_redact)
        rid = s.save(bot="hermes", title="leak", content="SSN 555-12-3456 here")
        assert "555-12-3456" not in s.get(rid)["content"]
        assert "[SSN]" in s.get(rid)["content"]

    def test_report_id_is_path_safe(self, store):
        # The generated id must never contain path separators or traversal.
        rid = store.save(bot="../../etc", title="../../evil", content="x")
        assert "/" not in rid and ".." not in rid

    def test_get_rejects_path_traversal(self, store):
        store.save(bot="hermes", title="ok", content="x")
        # Crafted ids that try to escape the store root resolve to nothing.
        for evil in ["../secrets", "../../etc/passwd", "a/b", "..%2f..%2f", "/abs"]:
            assert store.get(evil) is None

    def test_bot_and_title_length_capped(self, store):
        rid = store.save(bot="B" * 500, title="T" * 5000, content="x")
        rec = store.get(rid)
        assert len(rec["bot"]) <= 64
        assert len(rec["title"]) <= 256

    def test_content_size_cap(self, tmp_path):
        s = ReportStore(root=str(tmp_path / "r"), max_content_bytes=1000)
        with pytest.raises(ValueError):
            s.save(bot="hermes", title="huge", content="A" * 2000)

    def test_corrupt_metadata_skipped_in_list(self, store, tmp_path):
        store.save(bot="hermes", title="good", content="x")
        # Drop a garbage file into the store — list() must tolerate it.
        (tmp_path / "reports" / "garbage.json").write_text("{not json")
        items = store.list()
        assert len(items) == 1


class TestPersistence:
    def test_survives_new_instance(self, tmp_path):
        root = str(tmp_path / "reports")
        rid = ReportStore(root=root).save(bot="hermes", title="T", content="persisted")
        # A fresh instance (e.g. gateway restart) sees prior reports.
        assert ReportStore(root=root).get(rid)["content"] == "persisted"

    def test_delete(self, store):
        rid = store.save(bot="hermes", title="T", content="x")
        assert store.delete(rid) is True
        assert store.get(rid) is None
        assert store.delete(rid) is False  # idempotent


class TestAsyncSave:
    @pytest.mark.asyncio
    async def test_save_async_with_async_sanitizer(self, tmp_path):
        async def _san(text: str) -> str:
            return text.replace("secret", "[X]")

        s = ReportStore(root=str(tmp_path / "r"), sanitize_fn=_san)
        rid = await s.save_async(bot="hermes", title="t", content="a secret value")
        assert "[X]" in s.get(rid)["content"]
        assert "secret" not in s.get(rid)["content"]

    @pytest.mark.asyncio
    async def test_save_async_with_sync_sanitizer(self, tmp_path):
        s = ReportStore(root=str(tmp_path / "r"), sanitize_fn=lambda t: t.upper())
        rid = await s.save_async(bot="hermes", title="t", content="lower")
        assert s.get(rid)["content"] == "LOWER"

    @pytest.mark.asyncio
    async def test_save_async_size_cap(self, tmp_path):
        s = ReportStore(root=str(tmp_path / "r"), max_content_bytes=100)
        with pytest.raises(ValueError):
            await s.save_async(bot="hermes", title="t", content="A" * 500)


class TestReportAPI:
    """Route-level: POST/GET /api/reports through the FastAPI app (SCRUM-79)."""

    @pytest.fixture
    def client(self, tmp_path, monkeypatch):
        from fastapi.testclient import TestClient

        from gateway.ingest_api import main as main_mod

        # Bypass auth for the route logic test.
        main_mod.app.dependency_overrides[main_mod.auth_dep] = lambda: None
        monkeypatch.setattr(
            main_mod.app_state,
            "report_store",
            ReportStore(root=str(tmp_path / "api-reports")),
            raising=False,
        )
        try:
            yield TestClient(main_mod.app)
        finally:
            main_mod.app.dependency_overrides.pop(main_mod.auth_dep, None)

    def test_create_list_get_roundtrip(self, client):
        r = client.post(
            "/api/reports",
            json={"bot": "hermes", "title": "Intel", "content": "market up", "tags": ["x"]},
        )
        assert r.status_code == 201, r.text
        rid = r.json()["id"]

        lst = client.get("/api/reports")
        assert lst.status_code == 200
        assert any(it["id"] == rid for it in lst.json()["reports"])
        assert all("content" not in it for it in lst.json()["reports"])

        got = client.get(f"/api/reports/{rid}")
        assert got.status_code == 200
        assert got.json()["content"] == "market up"

    def test_missing_content_422(self, client):
        assert client.post("/api/reports", json={"bot": "hermes"}).status_code == 422

    def test_unknown_report_404(self, client):
        assert client.get("/api/reports/" + "a" * 32).status_code == 404

    def test_traversal_id_rejected_not_500(self, client):
        # A crafted traversal id must be defensively rejected (normalized away
        # / 403 / 404 / 400) — never a 500 and never a file escape.
        code = client.get("/api/reports/..%2f..%2fetc").status_code
        assert code in (400, 403, 404), code
        assert code != 500

    def test_cross_bot_visibility(self, client):
        client.post("/api/reports", json={"bot": "hermes", "title": "H", "content": "h"})
        client.post("/api/reports", json={"bot": "openclaw", "title": "O", "content": "o"})
        bots = {it["bot"] for it in client.get("/api/reports").json()["reports"]}
        assert bots == {"hermes", "openclaw"}  # each bot sees the other's report
        assert len(client.get("/api/reports?bot=hermes").json()["reports"]) == 1


class TestReviewHardening:
    """SCRUM-79 adversarial-review follow-ups (2026-07-13)."""

    def test_title_and_tags_sanitized_sync(self, tmp_path):
        s = ReportStore(root=str(tmp_path / "r"), sanitize_fn=lambda t: t.replace("SECRET", "[X]"))
        rid = s.save(bot="hermes", title="SECRET plan", content="body", tags=["SECRET-tag", "ok"])
        rec = s.get(rid)
        assert "SECRET" not in rec["title"] and "[X]" in rec["title"]
        assert all("SECRET" not in t for t in rec["tags"])

    @pytest.mark.asyncio
    async def test_title_and_tags_sanitized_async(self, tmp_path):
        async def _san(t):
            return t.replace("SECRET", "[X]")

        s = ReportStore(root=str(tmp_path / "r"), sanitize_fn=_san)
        rid = await s.save_async(bot="hermes", title="SECRET", content="c", tags=["SECRET"])
        rec = s.get(rid)
        assert "SECRET" not in rec["title"]
        assert all("SECRET" not in t for t in rec["tags"])

    def test_async_sanitizer_refused_on_sync_save(self, tmp_path):
        async def _san(t):
            return t

        s = ReportStore(root=str(tmp_path / "r"), sanitize_fn=_san)
        with pytest.raises(RuntimeError):
            s.save(bot="hermes", title="t", content="c")

    def test_count_cap_prunes_oldest(self, tmp_path):
        import time

        s = ReportStore(root=str(tmp_path / "r"), max_reports=3)
        ids = []
        for i in range(5):
            ids.append(s.save(bot="hermes", title=f"t{i}", content=str(i)))
            time.sleep(0.001)  # distinct created timestamps for ordering
        remaining = {it["id"] for it in s.list()}
        assert len(remaining) == 3
        # oldest two pruned, newest three kept
        assert ids[0] not in remaining and ids[1] not in remaining
        assert ids[4] in remaining

    def test_content_cap_default_is_1mb(self, tmp_path):
        s = ReportStore(root=str(tmp_path / "r"))
        assert s._max_content_bytes == 1024 * 1024
