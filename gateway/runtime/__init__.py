"""Multi-runtime container abstraction layer.

Supports Docker, Podman, and Apple Containers with automatic detection.
"""

import shutil
import logging
from typing import Optional

from .engine import ContainerEngine
from .docker_engine import DockerEngine
from .podman_engine import PodmanEngine
from .apple_engine import AppleContainerEngine

logger = logging.getLogger("agentshroud.runtime")

__all__ = [
    "ContainerEngine",
    "DockerEngine",
    "PodmanEngine",
    "AppleContainerEngine",
    "detect_runtime",
    "get_engine",
]


def detect_runtime() -> list[str]:
    """Auto-detect which container runtimes are available on this system."""
    available = []
    checks = [
        ("docker", "docker"),
        ("podman", "podman"),
        ("apple", "container"),
    ]
    for name, cli in checks:
        if shutil.which(cli):
            available.append(name)
            logger.info("Detected container runtime: %s (cli: %s)", name, cli)
    if not available:
        logger.warning("No container runtime detected")
    return available


def get_engine(preference: Optional[str] = None) -> ContainerEngine:
    """Return an appropriate container engine instance.

    Args:
        preference: Explicit runtime choice (docker/podman/apple).
                    If None, auto-detect with priority docker > podman > apple.

    Raises:
        RuntimeError: If no suitable runtime is found.
    """
    engines = {
        "docker": DockerEngine,
        "podman": PodmanEngine,
        "apple": AppleContainerEngine,
    }

    if preference:
        key = preference.lower()
        if key not in engines:
            raise ValueError(
                f"Unknown runtime: {preference!r}. Choose from: {list(engines)}"
            )
        return engines[key]()

    available = detect_runtime()
    priority = ["docker", "podman", "apple"]
    for rt in priority:
        if rt in available:
            logger.info("Selected runtime: %s", rt)
            return engines[rt]()

    raise RuntimeError(
        "No container runtime found. Install Docker, Podman, or Apple Containers."
    )
