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
    "PlannedAction",
    "SkillsManifest",
    "deploy_manifest",
    "plan_deploy",
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
# PlannedAction / plan_deploy
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class PlannedAction:
    """One unit of work in a deploy plan (canonical entry -> per-bot path).

    ``action`` is one of:
    - ``"create"`` — destination file does not exist yet.
    - ``"update"`` — destination exists but its SHA-256 differs from the source.
    - ``"skip"``   — destination already matches the source hash (idempotent).
    """

    action: str  # "create" | "update" | "skip"
    name: str  # relative manifest name, e.g. "skills/graphify/SKILL.md"
    dest_root: Path  # the per-bot destination root (openclaw / hermes)
    dest_path: Path  # concrete target path = dest_root / name


def plan_deploy(
    manifest: SkillsManifest,
    source: Path,
    destinations: Sequence[Path],
) -> list[PlannedAction]:
    """Compute the deploy plan without mutating the filesystem.

    Pure with respect to *destinations*: it reads existing destination files to
    classify each action but never creates directories or writes files. The plan
    maps every canonical entry to its concrete path under each per-bot
    destination root, in deterministic order (destinations outer, entries inner).

    This is the testable core the CLI/dry-run and the real deploy both build on.
    """
    plan: list[PlannedAction] = []
    for dest in destinations:
        for entry in manifest.entries:
            dst_path = dest / entry.name
            if not dst_path.exists():
                action = "create"
            elif hashlib.sha256(dst_path.read_bytes()).hexdigest() == entry.hash:
                action = "skip"
            else:
                action = "update"
            plan.append(
                PlannedAction(
                    action=action,
                    name=entry.name,
                    dest_root=dest,
                    dest_path=dst_path,
                )
            )
    return plan


# ---------------------------------------------------------------------------
# deploy_manifest
# ---------------------------------------------------------------------------


def deploy_manifest(
    manifest: SkillsManifest,
    source: Path,
    destinations: Sequence[Path],
    dry_run: bool = False,
) -> list[PlannedAction]:
    """Copy all files in *manifest* from *source* to each per-bot destination.

    Behaviour:
    - Computes the plan via :func:`plan_deploy` (canonical -> per-bot mapping).
    - Creates destination subdirectories as needed.
    - Skips files whose SHA-256 already matches (idempotent for unchanged files).
    - Always (re-)writes ``manifest.json`` at the destination root so the timestamp
      reflects the last deploy, but file contents only change when hashes differ.
    - Exits cleanly when called a second time with the same manifest and source.

    When *dry_run* is True the filesystem is not touched at all (no directories
    created, no files or ``manifest.json`` written); the computed plan is still
    returned so callers can report exactly what would change.

    Returns the deploy plan (one :class:`PlannedAction` per entry per destination).
    """
    plan = plan_deploy(manifest, source, destinations)
    if dry_run:
        return plan

    for dest in destinations:
        dest.mkdir(parents=True, exist_ok=True)

    for act in plan:
        if act.action == "skip":
            continue
        src_path = source / act.name
        act.dest_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(src_path), str(act.dest_path))

    # Always write manifest.json so CI gate can compare timestamps
    for dest in destinations:
        (dest / "manifest.json").write_text(manifest.to_json())

    return plan


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
