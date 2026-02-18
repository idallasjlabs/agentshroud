"""Docker implementation of ContainerEngine."""

from __future__ import annotations

import json
import logging
from typing import Any, Optional

from .engine import ContainerEngine, ContainerInfo

logger = logging.getLogger("secureclaw.runtime.docker")


class DockerEngine(ContainerEngine):
    """Container engine backed by the Docker CLI."""

    name = "docker"

    def __init__(self, cli: str = "docker"):
        self._cli = cli

    # -- helpers ---------------------------------------------------------

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
            cmd += ["-v", f"{hv}:{cv}"]
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
        cmd = [self._cli, "ps", "--format", "{{json .}}"]
        if all:
            cmd.append("-a")
        result = self._run(cmd, check=False)
        containers = []
        for line in (result.stdout or "").strip().splitlines():
            if not line.strip():
                continue
            data = json.loads(line)
            containers.append(
                ContainerInfo(
                    name=data.get("Names", ""),
                    id=data.get("ID", ""),
                    image=data.get("Image", ""),
                    status=data.get("Status", ""),
                    raw=data,
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
        cmd = [self._cli, "compose", "-f", file, "up"]
        if detach:
            cmd.append("-d")
        return self._run(cmd).stdout.strip()

    def compose_down(self, file: str) -> str:
        return self._run([self._cli, "compose", "-f", file, "down"]).stdout.strip()

    # -- health ----------------------------------------------------------

    def health_check(self) -> bool:
        try:
            self._cmd("info", timeout=10)
            return True
        except Exception:
            return False
