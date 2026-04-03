# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Runtime configuration for multi-engine container support."""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger("agentshroud.runtime.config")


@dataclass
class RuntimeConfig:
    """Configuration for container runtime selection and behavior.

    Loaded from environment variables or a config dict.

    Environment variables:
        AGENTSHROUD_RUNTIME: docker | podman | apple (default: auto-detect)
        AGENTSHROUD_ROOTLESS: true | false (default: true for podman)
        AGENTSHROUD_COMPOSE_FILE: path to compose file
        AGENTSHROUD_RUNTIME_SOCKET: custom socket path
    """

    runtime: Optional[str] = None  # None = auto-detect
    rootless: Optional[bool] = None  # None = use runtime default
    compose_file: str = "docker-compose.secure.yml"
    socket_path: Optional[str] = None

    @classmethod
    def from_env(cls) -> "RuntimeConfig":
        """Load configuration from environment variables."""
        runtime = os.environ.get("AGENTSHROUD_RUNTIME")
        rootless_str = os.environ.get("AGENTSHROUD_ROOTLESS")
        compose_file = os.environ.get("AGENTSHROUD_COMPOSE_FILE", "docker-compose.secure.yml")
        socket_path = os.environ.get("AGENTSHROUD_RUNTIME_SOCKET")

        rootless = None
        if rootless_str is not None:
            rootless = rootless_str.lower() in ("true", "1", "yes")

        config = cls(
            runtime=runtime,
            rootless=rootless,
            compose_file=compose_file,
            socket_path=socket_path,
        )
        logger.info("Runtime config loaded: %s", config)
        return config

    @classmethod
    def from_dict(cls, data: dict) -> "RuntimeConfig":
        """Load from a config dictionary (e.g. from YAML)."""
        return cls(
            runtime=data.get("runtime"),
            rootless=data.get("rootless"),
            compose_file=data.get("compose_file", "docker-compose.secure.yml"),
            socket_path=data.get("socket_path"),
        )

    @property
    def effective_rootless(self) -> bool:
        """Resolve rootless setting based on runtime."""
        if self.rootless is not None:
            return self.rootless
        # Default: rootless for podman, not for docker/apple
        return self.runtime == "podman"
