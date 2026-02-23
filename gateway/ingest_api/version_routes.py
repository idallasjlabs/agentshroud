# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Version Manager API Routes

All mutation operations (upgrade, downgrade, rollback) require
approval through the approval queue before execution.
"""
from __future__ import annotations


import logging
from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from ..tools.agentshroud_manager import (
    check_current_version,
    downgrade,
    list_available_versions,
    list_versions,
    mask_credentials,
    rollback,
    security_review,
    upgrade,
)

logger = logging.getLogger("agentshroud.version_routes")

router = APIRouter(prefix="/api/v1/versions", tags=["versions"])


class VersionRequest(BaseModel):
    """Request for version change operations."""

    target_version: str = Field(..., description="Target version (semver)")
    approval_id: str | None = Field(
        None, description="Approval queue ID (required for mutations)"
    )
    dry_run: bool = Field(False, description="Preview without executing")


class RollbackRequest(BaseModel):
    """Request for rollback operation."""

    approval_id: str | None = Field(None, description="Approval queue ID")


@router.get("/current")
async def get_current_version() -> dict[str, Any]:
    """Get the currently installed OpenClaw version."""
    return check_current_version()


@router.get("/history")
async def get_version_history() -> list[dict[str, Any]]:
    """Get version change history."""
    history = list_versions()
    # Mask credentials in any output
    for entry in history:
        if entry.get("security_review"):
            entry["security_review"] = mask_credentials(str(entry["security_review"]))
    return history


@router.get("/available")
async def get_available_versions() -> list[str]:
    """List available OpenClaw versions."""
    return list_available_versions()


@router.post("/review")
async def review_version(request: VersionRequest) -> dict[str, Any]:
    """Perform security review for a target version (no approval needed)."""
    return security_review(request.target_version)


@router.post("/upgrade")
async def upgrade_version(request: VersionRequest) -> dict[str, Any]:
    """Upgrade to a target version. Requires approval_id unless dry_run."""
    if not request.dry_run and not request.approval_id:
        raise HTTPException(
            status_code=400,
            detail="approval_id is required for non-dry-run upgrades. "
            "Submit an approval request first.",
        )
    result = upgrade(
        target_version=request.target_version,
        approval_id=request.approval_id,
        dry_run=request.dry_run,
    )
    if result["status"] == "blocked":
        raise HTTPException(status_code=422, detail=result["reason"])
    return result


@router.post("/downgrade")
async def downgrade_version(request: VersionRequest) -> dict[str, Any]:
    """Downgrade to a previous version. Requires approval_id unless dry_run."""
    if not request.dry_run and not request.approval_id:
        raise HTTPException(
            status_code=400,
            detail="approval_id is required for non-dry-run downgrades. "
            "Submit an approval request first.",
        )
    result = downgrade(
        target_version=request.target_version,
        approval_id=request.approval_id,
        dry_run=request.dry_run,
    )
    if result["status"] == "blocked":
        raise HTTPException(status_code=422, detail=result["reason"])
    return result


@router.post("/rollback")
async def rollback_version(request: RollbackRequest) -> dict[str, Any]:
    """Rollback to the previous version. Requires approval_id."""
    if not request.approval_id:
        raise HTTPException(
            status_code=400,
            detail="approval_id is required for rollback. Submit an approval request first.",
        )
    result = rollback(approval_id=request.approval_id)
    if result["status"] == "error":
        raise HTTPException(status_code=422, detail=result["reason"])
    return result
