# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Skills manifest — build, deploy, and validate the canonical skills/agents/MCP tree.

Single source of truth: ``~/.llm_settings/``
Deployed into: ``docker/config/openclaw/`` and ``docker/config/hermes/``

Usage::

    from gateway.skills.manifest import SkillsManifest, deploy_manifest, validate_manifest

    manifest = SkillsManifest.from_source(Path("~/.llm_settings").expanduser())
    deploy_manifest(manifest, source, [dest_openclaw, dest_hermes])
    drifted = validate_manifest(manifest, dest_openclaw)
"""

from __future__ import annotations

import hashlib
import json
import shutil
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Sequence

__all__ = [
    "ManifestEntry",
    "SkillsManifest",
    "deploy_manifest",
    "validate_manifest",
]

# Files that must never appear in the manifest even if present in source.
_EXCLUDED_NAMES = frozenset({"manifest.json"})

# Subdirectory names that are valid skill/agent/MCP source trees.
# Any file inside these directories (recursively) is eligible for syncing.
_VALID_SUBDIRS = frozenset({"skills", "mcp", "agents"})

_MANIFEST_VERSION = "1"


# ---------------------------------------------------------------------------
# ManifestEntry
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ManifestEntry:
    """A single item in the skills manifest."""

    name: str  # relative path from source root, e.g. "skills/graphify/SKILL.md"
    hash: str  # SHA-256 hex digest of file contents
    size: int  # byte size of file

    @classmethod
    def from_file(cls, name: str, path: Path) -> "ManifestEntry":
        """Build a ManifestEntry by reading *path* from disk."""
        data = path.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        return cls(name=name, hash=digest, size=len(data))

    def to_dict(self) -> dict:
        return {"name": self.name, "hash": self.hash, "size": self.size}


# ---------------------------------------------------------------------------
# SkillsManifest
# ---------------------------------------------------------------------------


@dataclass
class SkillsManifest:
    """In-memory representation of the skills/agents/MCP manifest."""

    entries: list[ManifestEntry] = field(default_factory=list)
    generated_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    version: str = _MANIFEST_VERSION

    # ------------------------------------------------------------------
    # Construction
    # ------------------------------------------------------------------

    @classmethod
    def from_source(cls, source: Path) -> "SkillsManifest":
        """Build a manifest by walking *source* (``~/.llm_settings/``).

        Raises:
            FileNotFoundError: if *source* does not exist.
            ValueError: if *source* is empty (no eligible files found).
        """
        if not source.exists():
            raise FileNotFoundError(f"Source directory not found: {source}")

        entries: list[ManifestEntry] = []
        for subdir in sorted(_VALID_SUBDIRS):
            subdir_path = source / subdir
            if not subdir_path.exists():
                continue
            for file_path in sorted(subdir_path.rglob("*")):
                if not file_path.is_file():
                    continue
                rel = file_path.relative_to(source).as_posix()
                if rel in _EXCLUDED_NAMES:
                    continue
                entries.append(ManifestEntry.from_file(rel, file_path))

        if not entries:
            raise ValueError(
                f"Source directory is empty — no eligible files found in {source}. "
                "Expected subdirectories: skills/, mcp/, agents/"
            )

        return cls(entries=entries)

    # ------------------------------------------------------------------
    # Serialisation
    # ------------------------------------------------------------------

    def to_dict(self) -> dict:
        return {
            "version": self.version,
            "generated_at": self.generated_at,
            "entries": [e.to_dict() for e in self.entries],
        }

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent)

    # ------------------------------------------------------------------
    # Lookup
    # ------------------------------------------------------------------

    def by_name(self) -> dict[str, ManifestEntry]:
        return {e.name: e for e in self.entries}


# ---------------------------------------------------------------------------
# deploy_manifest
# ---------------------------------------------------------------------------


def deploy_manifest(
    manifest: SkillsManifest,
    source: Path,
    destinations: Sequence[Path],
) -> None:
    """Copy all files in *manifest* from *source* to each path in *destinations*.

    Behaviour:
    - Creates destination subdirectories as needed.
    - Skips files whose SHA-256 already matches (idempotent for unchanged files).
    - Always (re-)writes ``manifest.json`` at the destination root so the timestamp
      reflects the last deploy, but file contents only change when hashes differ.
    - Exits cleanly when called a second time with the same manifest and source.
    """
    for dest in destinations:
        dest.mkdir(parents=True, exist_ok=True)
        for entry in manifest.entries:
            src_path = source / entry.name
            dst_path = dest / entry.name
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            # Only write if content has changed (idempotency gate)
            if dst_path.exists():
                existing_hash = hashlib.sha256(dst_path.read_bytes()).hexdigest()
                if existing_hash == entry.hash:
                    continue
            shutil.copy2(str(src_path), str(dst_path))

        # Always write manifest.json so CI gate can compare timestamps
        manifest_path = dest / "manifest.json"
        manifest_path.write_text(manifest.to_json())


# ---------------------------------------------------------------------------
# validate_manifest
# ---------------------------------------------------------------------------


def validate_manifest(manifest: SkillsManifest, dest: Path) -> list[str]:
    """Return names of entries that are missing or hash-mismatched in *dest*.

    Returns an empty list when the deployment is in sync with *manifest*.
    """
    drifted: list[str] = []
    for entry in manifest.entries:
        deployed = dest / entry.name
        if not deployed.exists():
            drifted.append(entry.name)
            continue
        actual_hash = hashlib.sha256(deployed.read_bytes()).hexdigest()
        if actual_hash != entry.hash:
            drifted.append(entry.name)
    return drifted
