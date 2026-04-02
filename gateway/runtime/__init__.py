# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Multi-runtime container abstraction layer.

Supports Docker, Podman, and Apple Containers with automatic detection.
"""

import logging
import shutil
from typing import Optional

from .apple_engine import AppleContainerEngine
from .docker_engine import DockerEngine
from .engine import ContainerEngine
from .podman_engine import PodmanEngine

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
            raise ValueError(f"Unknown runtime: {preference!r}. Choose from: {list(engines)}")
        return engines[key]()

    available = detect_runtime()
    priority = ["docker", "podman", "apple"]
    for rt in priority:
        if rt in available:
            logger.info("Selected runtime: %s", rt)
            return engines[rt]()

    raise RuntimeError("No container runtime found. Install Docker, Podman, or Apple Containers.")
