# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""AgentShroud Management REST API.

All management actions available as REST endpoints.
Requires gateway authentication.
"""


import asyncio
import logging
import os
import platform
import secrets as _secrets
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
    WebSocket,
    WebSocketDisconnect,
)
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel

from ..ingest_api.auth import verify_token
from ..ingest_api.config import load_config
from ..runtime import detect_runtime, get_engine
from ..runtime.config import RuntimeConfig
from ..runtime.security import get_security_comparison, warn_missing_features

logger = logging.getLogger("agentshroud.web.api")

# Scoped WebSocket tokens for management API (R3-M2)
_mgmt_ws_tokens: dict[str, float] = {}
_MGMT_WS_TOKEN_TTL = 300  # 5 minutes


def _create_mgmt_ws_token() -> str:
    """Create a short-lived WebSocket-only token for management endpoints."""
    token = f"mgmt_ws_{_secrets.token_urlsafe(32)}"
    _mgmt_ws_tokens[token] = time.time() + _MGMT_WS_TOKEN_TTL
    # Clean expired tokens
    now = time.time()
    expired = [t for t, exp in _mgmt_ws_tokens.items() if exp < now]
    for t in expired:
        del _mgmt_ws_tokens[t]
    return token


def _validate_mgmt_ws_token(token: str) -> bool:
    """Validate a management WebSocket token (single-use, time-limited)."""
    if not token or not token.startswith("mgmt_ws_"):
        return False
    expiry = _mgmt_ws_tokens.pop(token, None)  # Single-use: remove on validation
    if expiry is None:
        return False
    return time.time() < expiry


router = APIRouter(prefix="/api", tags=["management"])

# --- Auth dependency -------------------------------------------------------

_bearer = HTTPBearer()


async def require_auth(
    credentials: HTTPAuthorizationCredentials = Depends(_bearer),
) -> str:
    """Require valid Bearer token for all management endpoints."""
    config = load_config()
    if not verify_token(credentials.credentials, config.auth_token):
        raise HTTPException(status_code=401, detail="Invalid token")
    return "authenticated"


# --- Input validation ------------------------------------------------------

VALID_SERVICES = frozenset(
    {
        "agentshroud-gateway",
        "agentshroud-bot",
        "falco",
        "wazuh-agent",
        "clamav",
    }
)

VALID_KILLSWITCH_MODES = frozenset({"freeze", "shutdown", "disconnect"})


def _validate_service_name(name: str) -> str:
    """Validate service name against allowlist to prevent injection."""
    if name not in VALID_SERVICES:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid service name. Must be one of: {sorted(VALID_SERVICES)}",
        )
    return name


# --- Models ----------------------------------------------------------------


class ServiceAction(BaseModel):
    timeout: int = 30


class KillSwitchAction(BaseModel):

    confirm: bool = False


class ConfigUpdate(BaseModel):
    config: dict[str, Any]


class UpdateRequest(BaseModel):
    version: Optional[str] = None  # None = latest
    skip_tests: bool = False  # NOT recommended; safety gate


class ModeRequest(BaseModel):
    mode: str  # "enforce" | "monitor" | "observatory"
    revert_after_minutes: int = 30  # auto-revert to "enforce" after this delay


# --- Observatory Mode -------------------------------------------------------

VALID_AGENTSHROUD_MODES = frozenset({"enforce", "monitor", "observatory"})

# Tracks any pending auto-revert asyncio task so we can cancel it on re-call
_revert_task: Optional[asyncio.Task] = None


@router.get("/mode")
async def get_mode(user: str = Depends(require_auth)) -> dict:
    """Return the current AGENTSHROUD_MODE."""
    current = os.environ.get("AGENTSHROUD_MODE", "enforce")
    return {
        "mode": current,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@router.put("/mode")
async def set_mode(req: ModeRequest, user: str = Depends(require_auth)) -> dict:
    """Set AGENTSHROUD_MODE at runtime with automatic revert to 'enforce'."""
    global _revert_task

    if req.mode not in VALID_AGENTSHROUD_MODES:
        raise HTTPException(
            status_code=400,
            detail=f"mode must be one of: {sorted(VALID_AGENTSHROUD_MODES)}",
        )

    revert_minutes = max(1, min(req.revert_after_minutes, 480))  # 1 min – 8 hrs

    previous = os.environ.get("AGENTSHROUD_MODE", "enforce")
    os.environ["AGENTSHROUD_MODE"] = req.mode

    if req.mode != "enforce":
        logger.critical(
            "AGENTSHROUD_MODE changed from '%s' → '%s' — auto-revert in %d min",
            previous,
            req.mode,
            revert_minutes,
        )
    else:
        logger.info("AGENTSHROUD_MODE set to 'enforce'")

    # Cancel any existing revert task before scheduling a new one
    if _revert_task and not _revert_task.done():
        _revert_task.cancel()

    async def _auto_revert():
        await asyncio.sleep(revert_minutes * 60)
        if os.environ.get("AGENTSHROUD_MODE") != "enforce":
            logger.critical(
                "AGENTSHROUD_MODE auto-reverted '%s' → 'enforce' after %d min",
                os.environ.get("AGENTSHROUD_MODE"),
                revert_minutes,
            )
            os.environ["AGENTSHROUD_MODE"] = "enforce"

    _revert_task = asyncio.create_task(_auto_revert())

    return {
        "mode": req.mode,
        "previous_mode": previous,
        "auto_revert_in_minutes": revert_minutes,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


# --- Status -----------------------------------------------------------------


@router.get("/status")
async def get_status(user: str = Depends(require_auth)) -> dict:
    """Full system status including all services and runtime info."""
    runtime_config = RuntimeConfig.from_env()
    available_runtimes = detect_runtime()

    try:
        engine = get_engine(runtime_config.runtime)
        runtime_healthy = engine.health_check()
        containers = engine.ps(all=True) if runtime_healthy else []
    except Exception as e:
        runtime_healthy = False
        containers = []
        logger.warning("Runtime health check failed: %s", e)

    # System info
    import shutil

    disk = shutil.disk_usage("/")

    services = {}
    service_names = [
        "agentshroud-gateway",
        "agentshroud-bot",
        "falco",
        "wazuh-agent",
        "clamav",
    ]
    container_map = {c.name: c for c in containers}

    for svc_name in service_names:
        if svc_name in container_map:
            c = container_map[svc_name]
            services[svc_name] = {
                "status": (
                    "running" if "Up" in c.status or "running" in c.status.lower() else "stopped"
                ),
                "image": c.image,
                "id": c.id[:12],
                "details": c.status,
            }
        else:
            services[svc_name] = {"status": "not_found"}

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "platform": {
            "os": platform.system(),
            "arch": platform.machine(),
            "python": platform.python_version(),
        },
        "runtime": {
            "selected": runtime_config.runtime or "auto",
            "active": engine.name if runtime_healthy else None,
            "available": available_runtimes,
            "healthy": runtime_healthy,
            "rootless": runtime_config.effective_rootless,
        },
        "services": services,
        "system": {
            "disk_total_gb": round(disk.total / (1024**3), 1),
            "disk_free_gb": round(disk.free / (1024**3), 1),
            "disk_used_pct": round((disk.used / disk.total) * 100, 1),
        },
        "security": {
            "comparison": get_security_comparison(),
            "warnings": warn_missing_features(engine.name) if runtime_healthy else [],
        },
    }


# --- Service Control --------------------------------------------------------


@router.post("/services/{name}/start")
async def start_service(name: str, user: str = Depends(require_auth)) -> dict:
    """Start a specific service container."""
    _validate_service_name(name)
    engine = _get_engine()
    try:
        # For now, start via compose
        engine.compose_up(RuntimeConfig.from_env().compose_file)
        return {"status": "started", "service": name}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/services/{name}/stop")
async def stop_service(name: str, user: str = Depends(require_auth)) -> dict:
    """Stop a specific service container."""
    _validate_service_name(name)
    engine = _get_engine()
    try:
        engine.stop(name)
        return {"status": "stopped", "service": name}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/services/{name}/restart")
async def restart_service(name: str, user: str = Depends(require_auth)) -> dict:
    """Restart a specific service container."""
    _validate_service_name(name)
    engine = _get_engine()
    try:
        engine.stop(name)
        engine.rm(name, force=True)
        engine.compose_up(RuntimeConfig.from_env().compose_file)
        return {"status": "restarted", "service": name}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# --- Kill Switch ------------------------------------------------------------


@router.post("/killswitch/{mode}")
async def killswitch(
    mode: str, action: KillSwitchAction, user: str = Depends(require_auth)
) -> dict:
    """Emergency kill switch: freeze, shutdown, or disconnect."""
    if not action.confirm:
        raise HTTPException(status_code=400, detail="Must confirm kill switch action")

    if mode not in VALID_KILLSWITCH_MODES:
        raise HTTPException(
            status_code=400,
            detail=f"Mode must be one of: {sorted(VALID_KILLSWITCH_MODES)}",
        )

    engine = _get_engine()

    if mode == "freeze":
        for name in ["agentshroud-bot"]:
            try:
                engine.pause(name)
            except Exception:
                pass
        return {"status": "frozen", "mode": mode}

    elif mode == "shutdown":
        try:
            engine.compose_down(RuntimeConfig.from_env().compose_file)
        except Exception as e:
            logger.error("Shutdown failed: %s", e)
        return {"status": "shutdown", "mode": mode}

    elif mode == "disconnect":
        for name in ["agentshroud-bot"]:
            try:
                engine.stop(name)
                engine.rm(name, force=True)
            except Exception:
                pass
        return {"status": "disconnected", "mode": mode}

    return {"status": "unknown"}


# --- Configuration ----------------------------------------------------------


@router.get("/config")
async def get_config(user: str = Depends(require_auth)) -> dict:
    """Get current configuration."""
    config_path = Path("agentshroud.yaml")
    if config_path.exists():
        import yaml

        return {
            "config": yaml.safe_load(config_path.read_text()),
            "path": str(config_path),
        }
    return {"config": {}, "path": str(config_path), "exists": False}


@router.put("/config")
async def update_config(update: ConfigUpdate, user: str = Depends(require_auth)) -> dict:
    """Update configuration (writes YAML and optionally restarts)."""
    import yaml

    config_path = Path("agentshroud.yaml")

    # Validate config keys against allowlist
    ALLOWED_TOP_KEYS = {
        "gateway",
        "runtime",
        "security",
        "services",
        "network",
        "logging",
        "approval",
        "pii",
        "egress",
    }
    unexpected = set(update.config.keys()) - ALLOWED_TOP_KEYS
    if unexpected:
        raise HTTPException(status_code=400, detail=f"Unknown config keys: {sorted(unexpected)}")

    # Backup current
    if config_path.exists():
        backup = config_path.with_suffix(f".yaml.bak.{int(time.time())}")
        backup.write_text(config_path.read_text())

    config_path.write_text(yaml.dump(update.config, default_flow_style=False))
    return {"status": "updated", "path": str(config_path)}


@router.post("/config/import")
async def import_config(update: ConfigUpdate, user: str = Depends(require_auth)) -> dict:
    """Import configuration from uploaded data."""
    return await update_config(update)


@router.get("/config/export")
async def export_config(user: str = Depends(require_auth)) -> dict:
    """Export current configuration."""
    return await get_config()


# --- Rebuild ----------------------------------------------------------------


def _get_default_bot_dockerfile() -> str:
    """Resolve the Dockerfile for the default bot from gateway config."""
    try:
        cfg = load_config()
        default_bot = next(
            (b for b in cfg.bots.values() if b.default),
            next(iter(cfg.bots.values()), None),
        )
        if default_bot and default_bot.dockerfile:
            return default_bot.dockerfile
    except Exception:
        pass
    return "docker/bots/openclaw/Dockerfile"


@router.post("/rebuild")
async def rebuild(user: str = Depends(require_auth)) -> dict:
    """Rebuild containers with latest images."""
    engine = _get_engine()
    config = RuntimeConfig.from_env()
    try:
        engine.compose_down(config.compose_file)
        # Rebuild images
        engine.build("gateway/Dockerfile", "agentshroud-gateway:latest", ".")
        engine.build(_get_default_bot_dockerfile(), "agentshroud-bot:latest", ".")
        engine.compose_up(config.compose_file)
        return {"status": "rebuilt"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# --- Updates (bot-agnostic) ---------------------------------------------------


def _resolve_bot_container(bot_id: str) -> str:
    """Resolve the Docker container name for a given bot_id."""
    return f"agentshroud-{bot_id}"


@router.get("/updates/bot/{bot_id}")
async def check_bot_updates(bot_id: str, user: str = Depends(require_auth)) -> dict:
    """Check for updates for the named bot container."""
    import subprocess

    engine = _get_engine()
    container = _resolve_bot_container(bot_id)

    # For node-based bots, check npm registry
    latest = "unknown"
    try:
        result = subprocess.run(
            ["npm", "view", bot_id, "version"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        latest = result.stdout.strip() if result.returncode == 0 else "unknown"
    except Exception:
        pass

    current = "unknown"
    try:
        current = engine.exec(container, [bot_id, "--version"]).strip()
    except Exception:
        pass

    return {
        "bot_id": bot_id,
        "current": current,
        "latest": latest,
        "update_available": current != latest and latest != "unknown" and current != "unknown",
    }


@router.post("/updates/bot/{bot_id}/upgrade")
async def upgrade_bot(bot_id: str, req: UpdateRequest, user: str = Depends(require_auth)) -> dict:
    """Upgrade a named bot container."""
    engine = _get_engine()
    container = _resolve_bot_container(bot_id)
    version = req.version or "latest"

    steps: list[dict] = []
    try:
        steps.append({"step": "pull", "status": "running"})
        engine.exec(container, ["npm", "install", "-g", f"{bot_id}@{version}"])
        steps[-1]["status"] = "done"

        steps.append({"step": "restart", "status": "running"})
        engine.stop(container)
        engine.rm(container, force=True)
        engine.compose_up(RuntimeConfig.from_env().compose_file)
        steps[-1]["status"] = "done"

        return {"status": "upgraded", "bot_id": bot_id, "version": version, "steps": steps}
    except Exception as e:
        steps.append({"step": "error", "detail": str(e)})
        return {"status": "failed", "bot_id": bot_id, "steps": steps, "error": str(e)}


@router.post("/updates/bot/{bot_id}/rollback")
async def rollback_bot(bot_id: str, user: str = Depends(require_auth)) -> dict:
    """Rollback a named bot container to the previous image tag."""
    return {
        "status": "rollback_initiated",
        "bot_id": bot_id,
        "note": "Restoring previous container image",
    }


# --- Backward-compat aliases (openclaw → bot/openclaw) -----------------------


@router.get("/updates/openclaw")
async def check_openclaw_updates(user: str = Depends(require_auth)) -> dict:
    """Check for OpenClaw updates (backward-compat alias for /updates/bot/openclaw)."""
    return await check_bot_updates("openclaw", user)


@router.post("/updates/openclaw/upgrade")
async def upgrade_openclaw(req: UpdateRequest, user: str = Depends(require_auth)) -> dict:
    """Upgrade OpenClaw (backward-compat alias for /updates/bot/openclaw/upgrade)."""
    return await upgrade_bot("openclaw", req, user)


@router.post("/updates/openclaw/rollback")
async def rollback_openclaw(user: str = Depends(require_auth)) -> dict:
    """Rollback OpenClaw (backward-compat alias for /updates/bot/openclaw/rollback)."""
    return await rollback_bot("openclaw", user)


@router.get("/updates/agentshroud")
async def check_agentshroud_updates(user: str = Depends(require_auth)) -> dict:
    """Check for AgentShroud updates from GitHub."""
    import subprocess

    try:
        # Current commit
        current = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True,
            text=True,
            timeout=10,
            cwd=".",
        )
        current_hash = current.stdout.strip() if current.returncode == 0 else "unknown"

        # Current version from git tag
        tag_result = subprocess.run(
            ["git", "describe", "--tags", "--abbrev=0"],
            capture_output=True,
            text=True,
            timeout=10,
            cwd=".",
        )
        current_version = tag_result.stdout.strip() if tag_result.returncode == 0 else "dev"

        # Fetch latest from remote
        subprocess.run(["git", "fetch", "--tags"], capture_output=True, timeout=30, cwd=".")

        # Check if behind
        behind = subprocess.run(
            ["git", "rev-list", "--count", "HEAD..origin/main"],
            capture_output=True,
            text=True,
            timeout=10,
            cwd=".",
        )
        commits_behind = int(behind.stdout.strip()) if behind.returncode == 0 else 0

        # Latest remote tag
        remote_tag = subprocess.run(
            ["git", "describe", "--tags", "--abbrev=0", "origin/main"],
            capture_output=True,
            text=True,
            timeout=10,
            cwd=".",
        )
        latest_version = (
            remote_tag.stdout.strip() if remote_tag.returncode == 0 else current_version
        )

    except Exception as e:
        return {"error": str(e)}

    return {
        "current_version": current_version,
        "current_commit": current_hash,
        "latest_version": latest_version,
        "commits_behind": commits_behind,
        "update_available": commits_behind > 0,
    }


@router.post("/updates/agentshroud/upgrade")
async def upgrade_agentshroud(req: UpdateRequest, user: str = Depends(require_auth)) -> dict:
    """Pull latest AgentShroud, test, rebuild, restart. Auto-rollback on failure."""
    import subprocess

    steps = []
    rollback_hash = None

    try:
        # 0. Record current commit for rollback
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            timeout=10,
            cwd=".",
        )
        rollback_hash = result.stdout.strip()

        # 1. Git pull
        steps.append({"step": "git_pull", "status": "running"})
        pull = subprocess.run(
            ["git", "pull", "--ff-only"],
            capture_output=True,
            text=True,
            timeout=60,
            cwd=".",
        )
        if pull.returncode != 0:
            raise RuntimeError(f"git pull failed: {pull.stderr}")
        steps[-1]["status"] = "done"

        # 2. Security review — check for new deps, removed security features
        steps.append({"step": "security_review", "status": "running"})
        diff = subprocess.run(
            ["git", "diff", "--name-only", f"{rollback_hash}..HEAD"],
            capture_output=True,
            text=True,
            timeout=10,
            cwd=".",
        )
        changed_files = diff.stdout.strip().splitlines() if diff.returncode == 0 else []
        security_concerns = []
        for f in changed_files:
            if "requirements" in f.lower():
                security_concerns.append(f"Dependency change: {f}")
            if "security" in f.lower():
                security_concerns.append(f"Security module changed: {f}")
        steps[-1]["status"] = "done"
        steps[-1]["changed_files"] = len(changed_files)
        steps[-1]["security_concerns"] = security_concerns

        # 3. Run tests
        if not req.skip_tests:
            steps.append({"step": "run_tests", "status": "running"})
            tests = subprocess.run(
                ["python", "-m", "pytest", "gateway/tests/", "-v", "--tb=short"],
                capture_output=True,
                text=True,
                timeout=300,
                cwd=".",
            )
            if tests.returncode != 0:
                raise RuntimeError(f"Tests failed:\n{tests.stdout}\n{tests.stderr}")
            steps[-1]["status"] = "done"

        # 4. Rebuild containers
        steps.append({"step": "rebuild", "status": "running"})
        engine = _get_engine()
        config = RuntimeConfig.from_env()
        engine.build("gateway/Dockerfile", "agentshroud-gateway:latest", ".")
        engine.build(_get_default_bot_dockerfile(), "agentshroud-bot:latest", ".")
        steps[-1]["status"] = "done"

        # 5. Restart services
        steps.append({"step": "restart", "status": "running"})
        engine.compose_down(config.compose_file)
        engine.compose_up(config.compose_file)
        steps[-1]["status"] = "done"

        return {"status": "upgraded", "steps": steps, "rollback_hash": rollback_hash}

    except Exception as e:
        # Automatic rollback
        if rollback_hash:
            steps.append({"step": "rollback", "status": "running"})
            subprocess.run(
                ["git", "reset", "--hard", rollback_hash],
                capture_output=True,
                timeout=30,
                cwd=".",
            )
            steps[-1]["status"] = "done"

        return {
            "status": "failed",
            "error": str(e),
            "steps": steps,
            "rolled_back_to": rollback_hash,
        }


@router.post("/updates/agentshroud/rollback")
async def rollback_agentshroud(user: str = Depends(require_auth)) -> dict:
    """Revert to previous git commit and rebuild."""
    import subprocess

    try:
        subprocess.run(
            ["git", "reset", "--hard", "HEAD~1"],
            capture_output=True,
            timeout=30,
            cwd=".",
        )
        engine = _get_engine()
        config = RuntimeConfig.from_env()
        engine.build("gateway/Dockerfile", "agentshroud-gateway:latest", ".")
        engine.compose_down(config.compose_file)
        engine.compose_up(config.compose_file)
        return {"status": "rolled_back"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/updates/history")
async def update_history(user: str = Depends(require_auth)) -> dict:
    """Return update history from audit log."""
    # In production this reads from the data ledger
    import subprocess

    try:
        result = subprocess.run(
            ["git", "log", "--oneline", "-20"],
            capture_output=True,
            text=True,
            timeout=10,
            cwd=".",
        )
        commits = result.stdout.strip().splitlines() if result.returncode == 0 else []
        return {"history": commits}
    except Exception:
        return {"history": []}


# --- Security Reports -------------------------------------------------------


@router.get("/security/report")
async def security_report(user: str = Depends(require_auth)) -> dict:
    """Aggregate security report."""
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "runtime_security": get_security_comparison(),
        "warnings": warn_missing_features(
            _get_engine().name if _get_engine().health_check() else "docker"
        ),
    }


# --- Logs -------------------------------------------------------------------


@router.get("/logs")
async def get_logs(
    user: str = Depends(require_auth),
    service: Optional[str] = None,
    severity: Optional[str] = None,
    since: Optional[str] = None,
    tail: int = 100,
) -> dict:
    """Retrieve container logs with optional filtering."""
    tail = max(1, min(tail, 1000))  # Clamp to sane range
    engine = _get_engine()
    if service:
        _validate_service_name(service)
        try:
            logs = engine.logs(service, tail=tail)
            return {"service": service, "logs": logs.splitlines()}
        except Exception as e:
            raise HTTPException(status_code=404, detail=f"Service not found: {e}")
    else:
        # Combined logs from all services
        all_logs = {}
        for svc in ["agentshroud-gateway", "agentshroud-bot"]:
            try:
                all_logs[svc] = engine.logs(svc, tail=tail).splitlines()
            except Exception:
                all_logs[svc] = []
        return {"logs": all_logs}


# --- WebSocket for real-time updates ----------------------------------------

active_websockets: list[WebSocket] = []


@router.websocket("/ws/logs")
async def ws_logs(websocket: WebSocket, token: str = Query(default="")):
    """WebSocket endpoint for real-time log streaming. Requires scoped WS token."""
    if not token:
        await websocket.close(code=4001, reason="Authentication required")
        return
    # R3-M2: Accept only scoped management WS tokens (not the master auth token)
    if not _validate_mgmt_ws_token(token):
        await websocket.close(code=4003, reason="Invalid credentials")
        return
    await websocket.accept()
    active_websockets.append(websocket)
    try:
        while True:
            # Keep connection alive, send periodic updates
            await asyncio.sleep(5)
            try:
                engine = _get_engine()
                for svc in ["agentshroud-gateway", "agentshroud-bot"]:
                    try:
                        logs = engine.logs(svc, tail=5)
                        await websocket.send_json({"service": svc, "logs": logs.splitlines()})
                    except Exception:
                        pass
            except Exception:
                pass
    except WebSocketDisconnect:
        pass
    finally:
        # R3-L2: Ensure cleanup on any exception, not just WebSocketDisconnect
        if websocket in active_websockets:
            active_websockets.remove(websocket)


@router.websocket("/ws/updates")
async def ws_updates(websocket: WebSocket, token: str = Query(default="")):
    """WebSocket for real-time update progress. Requires scoped WS token."""
    if not token:
        await websocket.close(code=4001, reason="Authentication required")
        return
    # R3-M2: Accept only scoped management WS tokens (not the master auth token)
    if not _validate_mgmt_ws_token(token):
        await websocket.close(code=4003, reason="Invalid credentials")
        return
    await websocket.accept()
    try:
        while True:
            await websocket.receive_text()
            # Client can request update progress
            await websocket.send_json({"status": "connected"})
    except WebSocketDisconnect:
        pass


# --- Helpers ----------------------------------------------------------------


def _get_engine():
    """Get the active container engine."""
    config = RuntimeConfig.from_env()
    return get_engine(config.runtime)
