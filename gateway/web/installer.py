"""SecureClaw Web Installer — Step-by-step installation wizard."""

from __future__ import annotations

import logging
import platform
import shutil
import subprocess
from pathlib import Path
from typing import Optional

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from ..runtime import detect_runtime
from ..runtime.config import RuntimeConfig
from ..runtime.security import get_security_comparison

logger = logging.getLogger("secureclaw.web.installer")

router = APIRouter(prefix="/install", tags=["installer"])


class PrerequisiteCheck(BaseModel):
    name: str
    status: bool
    detail: str
    required: bool = True


class InstallConfig(BaseModel):
    runtime: str = "docker"
    rootless: bool = False
    telegram_token: Optional[str] = None
    model: str = "claude-sonnet-4-20250514"
    security_level: str = "recommended"  # minimal | recommended | paranoid
    gateway_password: Optional[str] = None
    allowed_users: list[str] = []
    enable_pii: bool = True
    enable_prompt_guard: bool = True
    enable_approval_queue: bool = True
    onepassword: bool = False
    email_smtp: Optional[str] = None
    icloud: bool = False


# --- Pages ------------------------------------------------------------------


@router.get("/", response_class=HTMLResponse)
async def installer_page(request: Request):
    """Serve the installer wizard HTML."""
    template = Path(__file__).parent / "templates" / "installer.html"
    return HTMLResponse(template.read_text())


# --- API for installer steps ------------------------------------------------


@router.get("/api/prerequisites")
async def check_prerequisites() -> dict:
    """Check system prerequisites for installation."""
    checks = []

    # OS
    os_name = platform.system()
    arch = platform.machine()
    checks.append(PrerequisiteCheck(
        name="Operating System",
        status=os_name in ("Linux", "Darwin"),
        detail=f"{os_name} {arch}",
    ))

    # Architecture
    checks.append(PrerequisiteCheck(
        name="Architecture",
        status=arch in ("x86_64", "aarch64", "arm64"),
        detail=arch,
    ))

    # Container runtime
    runtimes = detect_runtime()
    checks.append(PrerequisiteCheck(
        name="Container Runtime",
        status=len(runtimes) > 0,
        detail=f"Found: {', '.join(runtimes)}" if runtimes else "None found — install Docker, Podman, or Apple Containers",
    ))

    # Python
    py_version = platform.python_version()
    py_ok = tuple(int(x) for x in py_version.split(".")[:2]) >= (3, 11)
    checks.append(PrerequisiteCheck(
        name="Python 3.11+",
        status=py_ok,
        detail=f"Python {py_version}",
    ))

    # Git
    git_ok = shutil.which("git") is not None
    checks.append(PrerequisiteCheck(
        name="Git",
        status=git_ok,
        detail="Installed" if git_ok else "Not found",
    ))

    # Disk space
    disk = shutil.disk_usage("/")
    disk_gb = disk.free / (1024**3)
    checks.append(PrerequisiteCheck(
        name="Disk Space (>2GB free)",
        status=disk_gb > 2.0,
        detail=f"{disk_gb:.1f} GB free",
    ))

    # RAM (Linux only)
    try:
        with open("/proc/meminfo") as f:
            for line in f:
                if line.startswith("MemTotal"):
                    ram_kb = int(line.split()[1])
                    ram_gb = ram_kb / (1024**2)
                    checks.append(PrerequisiteCheck(
                        name="RAM (>1GB recommended)",
                        status=ram_gb > 1.0,
                        detail=f"{ram_gb:.1f} GB",
                        required=False,
                    ))
                    break
    except FileNotFoundError:
        # macOS — use sysctl
        try:
            result = subprocess.run(
                ["sysctl", "-n", "hw.memsize"],
                capture_output=True, text=True, timeout=5,
            )
            if result.returncode == 0:
                ram_gb = int(result.stdout.strip()) / (1024**3)
                checks.append(PrerequisiteCheck(
                    name="RAM (>1GB recommended)",
                    status=ram_gb > 1.0,
                    detail=f"{ram_gb:.1f} GB",
                    required=False,
                ))
        except Exception:
            pass

    all_required_ok = all(c.status for c in checks if c.required)

    return {
        "checks": [c.model_dump() for c in checks],
        "ready": all_required_ok,
        "platform": {"os": os_name, "arch": arch},
    }


@router.get("/api/runtimes")
async def get_runtimes() -> dict:
    """Get available runtimes with recommendations."""
    runtimes = detect_runtime()
    os_name = platform.system()
    arch = platform.machine()

    recommendations = {}
    if os_name == "Linux":
        recommendations = {
            "docker": "Most tested, widest ecosystem",
            "podman": "Rootless by default — more secure",
        }
    elif os_name == "Darwin":
        if arch in ("arm64", "aarch64"):
            recommendations = {
                "apple": "Native Apple Silicon, fastest, strongest isolation (VM per container)",
                "docker": "Docker Desktop — well-tested, full compose support",
            }
        else:
            recommendations = {
                "docker": "Docker Desktop — most compatible",
                "podman": "Rootless option via Podman Desktop",
            }

    return {
        "available": runtimes,
        "recommendations": recommendations,
        "security_comparison": get_security_comparison(),
    }


@router.post("/api/install")
async def start_install(config: InstallConfig) -> dict:
    """Start the installation process.

    This endpoint kicks off the install and returns immediately.
    Progress is streamed via WebSocket at /install/ws/progress.
    """
    # Validate
    if not config.telegram_token and config.telegram_token is not None:
        pass  # Optional for now

    # In production this would spawn a background task
    return {
        "status": "started",
        "config": config.model_dump(),
        "message": "Installation started. Monitor progress via WebSocket.",
    }
