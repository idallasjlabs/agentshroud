"""Abstract base class for container engines."""

from __future__ import annotations

import subprocess
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class ContainerInfo:
    """Lightweight container metadata returned by ps/inspect."""
    name: str
    id: str = ""
    image: str = ""
    status: str = ""
    ports: dict[str, str] = field(default_factory=dict)
    labels: dict[str, str] = field(default_factory=dict)
    raw: dict[str, Any] = field(default_factory=dict)


class ContainerEngine(ABC):
    """Unified interface for container runtimes (Docker / Podman / Apple Containers)."""

    name: str = "base"

    # --- helpers --------------------------------------------------------

    def _run(
        self,
        cmd: list[str],
        *,
        check: bool = True,
        capture: bool = True,
        timeout: int = 300,
    ) -> subprocess.CompletedProcess:
        """Run a CLI command and return the result."""
        return subprocess.run(
            cmd,
            check=check,
            capture_output=capture,
            text=True,
            timeout=timeout,
        )

    # --- image lifecycle ------------------------------------------------

    @abstractmethod
    def build(
        self,
        dockerfile: str,
        tag: str,
        context: str = ".",
        build_args: Optional[dict[str, str]] = None,
    ) -> str:
        """Build an image. Returns the image id/tag."""

    @abstractmethod
    def pull(self, image: str) -> str:
        """Pull an image from a registry."""

    @abstractmethod
    def push(self, image: str) -> str:
        """Push an image to a registry."""

    # --- container lifecycle --------------------------------------------

    @abstractmethod
    def run(
        self,
        image: str,
        name: str,
        *,
        ports: Optional[dict[str, str]] = None,
        volumes: Optional[dict[str, str]] = None,
        networks: Optional[list[str]] = None,
        env: Optional[dict[str, str]] = None,
        privileged: bool = False,
        caps: Optional[list[str]] = None,
        seccomp: Optional[str] = None,
        detach: bool = True,
        read_only: bool = False,
        no_new_privileges: bool = True,
    ) -> str:
        """Start a container. Returns container id."""

    @abstractmethod
    def stop(self, name: str, timeout: int = 10) -> None:
        """Stop a running container."""

    @abstractmethod
    def rm(self, name: str, force: bool = False) -> None:
        """Remove a container."""

    @abstractmethod
    def pause(self, name: str) -> None:
        """Pause a container."""

    @abstractmethod
    def unpause(self, name: str) -> None:
        """Unpause a container."""

    @abstractmethod
    def ps(self, all: bool = False) -> list[ContainerInfo]:
        """List containers."""

    @abstractmethod
    def logs(self, name: str, tail: int = 100) -> str:
        """Retrieve container logs."""

    @abstractmethod
    def exec(self, name: str, command: list[str]) -> str:
        """Execute a command inside a running container."""

    @abstractmethod
    def inspect(self, name: str) -> dict[str, Any]:
        """Return detailed container metadata."""

    # --- networking & volumes -------------------------------------------

    @abstractmethod
    def network_create(self, name: str, internal: bool = False) -> str:
        """Create a network."""

    @abstractmethod
    def network_rm(self, name: str) -> None:
        """Remove a network."""

    @abstractmethod
    def volume_create(self, name: str) -> str:
        """Create a volume."""

    @abstractmethod
    def volume_rm(self, name: str) -> None:
        """Remove a volume."""

    # --- compose --------------------------------------------------------

    @abstractmethod
    def compose_up(self, file: str, detach: bool = True) -> str:
        """Bring up services from a compose file."""

    @abstractmethod
    def compose_down(self, file: str) -> str:
        """Tear down services from a compose file."""

    # --- health ---------------------------------------------------------

    @abstractmethod
    def health_check(self) -> bool:
        """Return True if the runtime is available and responsive."""
