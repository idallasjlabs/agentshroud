# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for skills manifest sync (Workstream D).

TDD: these tests were written before the implementation.

Covers:
- SkillsManifest: build from source, hash stability, serialisation
- deploy_manifest: copies files to dest dirs, writes manifest.json per dest
- validate_manifest: drift detection (hash mismatch, missing item)
- IdempotencyProperty: second deploy produces no file changes
- Endpoint: POST /api/skills/reload returns correct JSON shape
"""

from __future__ import annotations

import hashlib
import json
import shutil
import time
from pathlib import Path
from types import SimpleNamespace
from typing import Any
from unittest.mock import MagicMock, patch

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

# ---------------------------------------------------------------------------
# Unit under test
# ---------------------------------------------------------------------------
from gateway.skills.manifest import (
    ManifestEntry,
    SkillsManifest,
    deploy_manifest,
    validate_manifest,
)
from gateway.web.api import require_auth, router


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def _write_tree(root: Path, files: dict[str, str]) -> None:
    """Write {relative_path: content} under *root*."""
    for rel, content in files.items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)


# ---------------------------------------------------------------------------
# ManifestEntry
# ---------------------------------------------------------------------------

class TestManifestEntry:
    def test_hash_is_sha256_of_content(self, tmp_path: Path) -> None:
        f = tmp_path / "skill.md"
        f.write_text("hello world")
        entry = ManifestEntry.from_file("skills/skill.md", f)
        assert entry.hash == _sha256("hello world")

    def test_serialise_roundtrip(self, tmp_path: Path) -> None:
        f = tmp_path / "x.md"
        f.write_text("content")
        entry = ManifestEntry.from_file("skills/x.md", f)
        data = entry.to_dict()
        assert data["name"] == "skills/x.md"
        assert data["hash"] == _sha256("content")
        assert "size" in data

    def test_hash_changes_when_content_changes(self, tmp_path: Path) -> None:
        f = tmp_path / "mcp.json"
        f.write_text('{"a": 1}')
        e1 = ManifestEntry.from_file("mcp/mcp.json", f)
        f.write_text('{"a": 2}')
        e2 = ManifestEntry.from_file("mcp/mcp.json", f)
        assert e1.hash != e2.hash


# ---------------------------------------------------------------------------
# SkillsManifest — build from source directory
# ---------------------------------------------------------------------------

class TestSkillsManifest:
    def test_build_includes_all_files(self, tmp_path: Path) -> None:
        _write_tree(tmp_path, {
            "skills/graphify/SKILL.md": "# graphify",
            "mcp/servers.json": '{"servers": {}}',
            "agents/hermes-soul.md": "# hermes",
        })
        manifest = SkillsManifest.from_source(tmp_path)
        names = {e.name for e in manifest.entries}
        assert "skills/graphify/SKILL.md" in names
        assert "mcp/servers.json" in names
        assert "agents/hermes-soul.md" in names

    def test_build_excludes_manifest_json_itself(self, tmp_path: Path) -> None:
        _write_tree(tmp_path, {
            "skills/a.md": "content",
            "manifest.json": '{"entries": []}',
        })
        manifest = SkillsManifest.from_source(tmp_path)
        names = {e.name for e in manifest.entries}
        assert "manifest.json" not in names

    def test_build_is_sorted_deterministically(self, tmp_path: Path) -> None:
        _write_tree(tmp_path, {
            "skills/z.md": "z",
            "agents/a.md": "a",
            "mcp/b.json": "b",
        })
        m1 = SkillsManifest.from_source(tmp_path)
        m2 = SkillsManifest.from_source(tmp_path)
        assert [e.name for e in m1.entries] == [e.name for e in m2.entries]

    def test_serialise_contains_version_and_timestamp(self, tmp_path: Path) -> None:
        _write_tree(tmp_path, {"skills/x.md": "x"})
        manifest = SkillsManifest.from_source(tmp_path)
        data = manifest.to_dict()
        assert "version" in data
        assert "generated_at" in data
        assert "entries" in data

    def test_from_empty_source_raises(self, tmp_path: Path) -> None:
        """An empty source directory must raise ValueError."""
        with pytest.raises(ValueError, match="empty"):
            SkillsManifest.from_source(tmp_path)

    def test_missing_source_raises(self, tmp_path: Path) -> None:
        absent = tmp_path / "nonexistent"
        with pytest.raises(FileNotFoundError):
            SkillsManifest.from_source(absent)

    def test_manifest_json_in_source_is_excluded(self, tmp_path: Path) -> None:
        """manifest.json must never appear as an entry even when present in source."""
        _write_tree(tmp_path, {
            "skills/x.md": "x",
            "manifest.json": '{"entries":[]}',
        })
        manifest = SkillsManifest.from_source(tmp_path)
        names = {e.name for e in manifest.entries}
        assert "manifest.json" not in names
        # The continue branch was hit — we still got the skill entry
        assert "skills/x.md" in names

    def test_by_name_lookup(self, tmp_path: Path) -> None:
        _write_tree(tmp_path, {"skills/tool.md": "tool content"})
        manifest = SkillsManifest.from_source(tmp_path)
        lookup = manifest.by_name()
        assert "skills/tool.md" in lookup
        assert lookup["skills/tool.md"].hash == _sha256("tool content")


# ---------------------------------------------------------------------------
# deploy_manifest
# ---------------------------------------------------------------------------

class TestDeployManifest:
    def test_deploy_copies_files_to_dest(self, tmp_path: Path) -> None:
        src = tmp_path / "src"
        dest = tmp_path / "dest"
        _write_tree(src, {
            "skills/graphify/SKILL.md": "# graphify skill",
            "mcp/servers.json": '{"servers": {}}',
        })
        manifest = SkillsManifest.from_source(src)
        deploy_manifest(manifest, src, [dest])
        assert (dest / "skills/graphify/SKILL.md").exists()
        assert (dest / "mcp/servers.json").exists()

    def test_deploy_writes_manifest_json(self, tmp_path: Path) -> None:
        src = tmp_path / "src"
        dest = tmp_path / "dest"
        _write_tree(src, {"agents/hermes-soul.md": "# hermes"})
        manifest = SkillsManifest.from_source(src)
        deploy_manifest(manifest, src, [dest])
        manifest_path = dest / "manifest.json"
        assert manifest_path.exists()
        data = json.loads(manifest_path.read_text())
        assert "entries" in data

    def test_deploy_is_idempotent(self, tmp_path: Path) -> None:
        src = tmp_path / "src"
        dest = tmp_path / "dest"
        _write_tree(src, {
            "skills/graphify/SKILL.md": "# graphify",
            "agents/openclaw-identity.md": "identity",
        })
        manifest = SkillsManifest.from_source(src)
        deploy_manifest(manifest, src, [dest])
        # Record mtimes after first deploy
        mtimes_1 = {
            p: p.stat().st_mtime
            for p in dest.rglob("*")
            if p.is_file()
        }
        # Wait a tick then deploy again — idempotent: only changed files get re-written
        time.sleep(0.05)
        deploy_manifest(manifest, src, [dest])
        mtimes_2 = {
            p: p.stat().st_mtime
            for p in dest.rglob("*")
            if p.is_file()
        }
        # manifest.json is always refreshed (timestamp changes); all other files unchanged
        changed = {
            p for p in mtimes_1
            if p.name != "manifest.json" and mtimes_2.get(p, 0) != mtimes_1[p]
        }
        assert changed == set(), f"Idempotency violated: {changed}"

    def test_deploy_to_multiple_destinations(self, tmp_path: Path) -> None:
        src = tmp_path / "src"
        dest_a = tmp_path / "dest_a"
        dest_b = tmp_path / "dest_b"
        _write_tree(src, {"skills/tool.md": "tool"})
        manifest = SkillsManifest.from_source(src)
        deploy_manifest(manifest, src, [dest_a, dest_b])
        assert (dest_a / "skills/tool.md").exists()
        assert (dest_b / "skills/tool.md").exists()
        assert (dest_a / "manifest.json").exists()
        assert (dest_b / "manifest.json").exists()

    def test_deploy_overwrites_changed_content(self, tmp_path: Path) -> None:
        src = tmp_path / "src"
        dest = tmp_path / "dest"
        _write_tree(src, {"skills/tool.md": "v1"})
        m1 = SkillsManifest.from_source(src)
        deploy_manifest(m1, src, [dest])

        # Update source
        (src / "skills/tool.md").write_text("v2")
        m2 = SkillsManifest.from_source(src)
        deploy_manifest(m2, src, [dest])

        assert (dest / "skills/tool.md").read_text() == "v2"


# ---------------------------------------------------------------------------
# validate_manifest — drift detection
# ---------------------------------------------------------------------------

class TestValidateManifest:
    def test_no_drift_returns_empty_list(self, tmp_path: Path) -> None:
        src = tmp_path / "src"
        dest = tmp_path / "dest"
        _write_tree(src, {"skills/x.md": "content"})
        manifest = SkillsManifest.from_source(src)
        deploy_manifest(manifest, src, [dest])
        drifted = validate_manifest(manifest, dest)
        assert drifted == []

    def test_drift_detected_on_hash_mismatch(self, tmp_path: Path) -> None:
        src = tmp_path / "src"
        dest = tmp_path / "dest"
        _write_tree(src, {"skills/x.md": "original"})
        manifest = SkillsManifest.from_source(src)
        deploy_manifest(manifest, src, [dest])
        # Tamper with deployed file
        (dest / "skills/x.md").write_text("tampered")
        drifted = validate_manifest(manifest, dest)
        assert "skills/x.md" in drifted

    def test_drift_detected_on_missing_file(self, tmp_path: Path) -> None:
        src = tmp_path / "src"
        dest = tmp_path / "dest"
        _write_tree(src, {
            "skills/a.md": "a",
            "skills/b.md": "b",
        })
        manifest = SkillsManifest.from_source(src)
        deploy_manifest(manifest, src, [dest])
        # Delete a deployed file
        (dest / "skills/b.md").unlink()
        drifted = validate_manifest(manifest, dest)
        assert "skills/b.md" in drifted

    def test_returns_all_drifted_items(self, tmp_path: Path) -> None:
        src = tmp_path / "src"
        dest = tmp_path / "dest"
        _write_tree(src, {
            "skills/a.md": "a",
            "skills/b.md": "b",
            "agents/persona.md": "p",
        })
        manifest = SkillsManifest.from_source(src)
        deploy_manifest(manifest, src, [dest])
        (dest / "skills/a.md").write_text("X")
        (dest / "agents/persona.md").unlink()
        drifted = validate_manifest(manifest, dest)
        assert set(drifted) == {"skills/a.md", "agents/persona.md"}


# ---------------------------------------------------------------------------
# /api/skills/reload endpoint
# ---------------------------------------------------------------------------

class TestSkillsReloadEndpoint:
    @pytest.fixture
    def client(self, tmp_path: Path) -> TestClient:
        app = FastAPI()
        app.dependency_overrides[require_auth] = lambda: "test-user"
        app.include_router(router)
        with TestClient(app, raise_server_exceptions=False) as c:
            yield c

    def test_reload_returns_200_with_skills_list(
        self, client: TestClient, tmp_path: Path
    ) -> None:
        src = tmp_path / "src"
        dest_oc = tmp_path / "openclaw"
        dest_h = tmp_path / "hermes"
        _write_tree(src, {
            "skills/graphify/SKILL.md": "# graphify",
            "mcp/servers.json": '{"servers":{}}',
        })
        manifest = SkillsManifest.from_source(src)
        deploy_manifest(manifest, src, [dest_oc, dest_h])

        with patch(
            "gateway.web.api._skills_reload_impl",
            return_value={"reloaded": True, "skills": ["graphify"]},
        ):
            resp = client.post("/api/skills/reload")
        assert resp.status_code == 200
        body = resp.json()
        assert body["reloaded"] is True
        assert isinstance(body["skills"], list)

    def test_reload_requires_auth(self) -> None:
        app = FastAPI()
        app.include_router(router)
        with TestClient(app, raise_server_exceptions=False) as c:
            resp = c.post("/api/skills/reload")
        assert resp.status_code in (401, 403)

    def test_reload_returns_500_on_source_missing(
        self, client: TestClient
    ) -> None:
        with patch(
            "gateway.web.api._skills_reload_impl",
            side_effect=FileNotFoundError("~/.llm_settings not found"),
        ):
            resp = client.post("/api/skills/reload")
        assert resp.status_code == 500
