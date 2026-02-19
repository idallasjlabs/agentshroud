"""Podman implementation of ContainerEngine.

Podman is largely CLI-compatible with Docker but differs in:
- Rootless by default (no daemon)
- Different socket path (/run/user/<uid>/podman/podman.sock)
- SELinux label support (:z / :Z volume flags)
- systemd service generation (podman generate systemd)
"""

from __future__ import annotations

import json
import logging
import shutil
from typing import Any, Optional

from .engine import ContainerEngine, ContainerInfo

logger = logging.getLogger("agentshroud.runtime.podman")


class PodmanEngine(ContainerEngine):
    """Container engine backed by the Podman CLI."""

    name = "podman"

    def __init__(self, cli: str = "podman"):
        self._cli = cli
        self._compose_cli = self._detect_compose()

    def _detect_compose(self) -> list[str]:
        """Detect podman compose or podman-compose."""
        # Try podman compose (plugin style)
        if shutil.which("podman-compose"):
            return ["podman-compose"]
        return [self._cli, "compose"]

    def _cmd(self, *args: str, **kwargs) -> str:
        result = self._run([self._cli, *args], **kwargs)
        return result.stdout.strip() if result.stdout else ""

    # -- image -----------------------------------------------------------

    def build(self, dockerfile: str, tag: str, context: str = ".", build_args: Optional[dict[str, str]] = None) -> str:
        cmd = [self._cli, "build", "-f", dockerfile, "-t", tag]
        for k, v in (build_args or {}).items():
            cmd += ["--build-arg", f"{k}={v}"]
        cmd.append(context)
        return self._run(cmd).stdout.strip()

    def pull(self, image: str) -> str:
        return self._cmd("pull", image)

    def push(self, image: str) -> str:
        return self._cmd("push", image)

    # -- container -------------------------------------------------------

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
        cmd = [self._cli, "run", "--name", name]
        if detach:
            cmd.append("-d")
        if privileged:
            cmd.append("--privileged")
        if read_only:
            cmd.append("--read-only")
        if no_new_privileges:
            cmd.append("--security-opt=no-new-privileges")
        if seccomp:
            cmd += ["--security-opt", f"seccomp={seccomp}"]
        for cap in caps or []:
            cmd += ["--cap-add", cap]
        for hp, cp in (ports or {}).items():
            cmd += ["-p", f"{hp}:{cp}"]
        for hv, cv in (volumes or {}).items():
            # Podman: use :z for SELinux shared label
            cmd += ["-v", f"{hv}:{cv}:z"]
        for net in networks or []:
            cmd += ["--network", net]
        for k, v in (env or {}).items():
            cmd += ["-e", f"{k}={v}"]
        cmd.append(image)
        return self._run(cmd).stdout.strip()

    def stop(self, name: str, timeout: int = 10) -> None:
        self._cmd("stop", "-t", str(timeout), name)

    def rm(self, name: str, force: bool = False) -> None:
        cmd = ["rm"]
        if force:
            cmd.append("-f")
        cmd.append(name)
        self._cmd(*cmd)

    def pause(self, name: str) -> None:
        self._cmd("pause", name)

    def unpause(self, name: str) -> None:
        self._cmd("unpause", name)

    def ps(self, all: bool = False) -> list[ContainerInfo]:
        cmd = [self._cli, "ps", "--format", "json"]
        if all:
            cmd.append("-a")
        result = self._run(cmd, check=False)
        containers = []
        raw = result.stdout.strip() if result.stdout else "[]"
        data = json.loads(raw) if raw else []
        if isinstance(data, dict):
            data = [data]
        for item in data:
            containers.append(
                ContainerInfo(
                    name=item.get("Names", [item.get("Name", "")])[0] if isinstance(item.get("Names"), list) else item.get("Names", item.get("Name", "")),
                    id=item.get("Id", item.get("ID", "")),
                    image=item.get("Image", ""),
                    status=item.get("Status", item.get("State", "")),
                    raw=item,
                )
            )
        return containers

    def logs(self, name: str, tail: int = 100) -> str:
        return self._cmd("logs", "--tail", str(tail), name)

    def exec(self, name: str, command: list[str]) -> str:
        return self._cmd("exec", name, *command)

    def inspect(self, name: str) -> dict[str, Any]:
        raw = self._cmd("inspect", name)
        data = json.loads(raw)
        return data[0] if isinstance(data, list) else data

    # -- networking & volumes --------------------------------------------

    def network_create(self, name: str, internal: bool = False) -> str:
        cmd = ["network", "create"]
        if internal:
            cmd.append("--internal")
        cmd.append(name)
        return self._cmd(*cmd)

    def network_rm(self, name: str) -> None:
        self._cmd("network", "rm", name)

    def volume_create(self, name: str) -> str:
        return self._cmd("volume", "create", name)

    def volume_rm(self, name: str) -> None:
        self._cmd("volume", "rm", name)

    # -- compose ---------------------------------------------------------

    def compose_up(self, file: str, detach: bool = True) -> str:
        cmd = [*self._compose_cli, "-f", file, "up"]
        if detach:
            cmd.append("-d")
        return self._run(cmd).stdout.strip()

    def compose_down(self, file: str) -> str:
        return self._run([*self._compose_cli, "-f", file, "down"]).stdout.strip()

    # -- podman-specific -------------------------------------------------

    def generate_systemd(self, name: str) -> str:
        """Generate a systemd unit file for a container."""
        return self._cmd("generate", "systemd", "--name", name)

    # -- health ----------------------------------------------------------

    def health_check(self) -> bool:
        try:
            self._cmd("info", timeout=10)
            return True
        except Exception:
            return False
