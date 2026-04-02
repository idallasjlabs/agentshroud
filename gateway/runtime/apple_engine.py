# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Apple Containers implementation of ContainerEngine.

Apple Containers (macOS 26+) uses the `container` CLI. Each container runs
in a lightweight VM with hardware-level isolation. Key differences:
- No compose (yet) — containers managed individually
- Optimised for Apple Silicon
- Strongest isolation model (per-container VM)
"""


import json
import logging
from typing import Any, Optional

from .engine import ContainerEngine, ContainerInfo

logger = logging.getLogger("agentshroud.runtime.apple")


class AppleContainerEngine(ContainerEngine):
    """Container engine backed by Apple's `container` CLI."""

    name = "apple"

    def __init__(self, cli: str = "container"):
        self._cli = cli

    def _cmd(self, *args: str, **kwargs) -> str:
        result = self._run([self._cli, *args], **kwargs)
        return result.stdout.strip() if result.stdout else ""

    # -- image -----------------------------------------------------------

    def build(
        self,
        dockerfile: str,
        tag: str,
        context: str = ".",
        build_args: Optional[dict[str, str]] = None,
    ) -> str:
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
        # Apple Containers: VM isolation means seccomp/caps are less relevant
        # but we pass what we can
        for hp, cp in (ports or {}).items():
            cmd += ["-p", f"{hp}:{cp}"]
        for hv, cv in (volumes or {}).items():
            cmd += ["-v", f"{hv}:{cv}"]
        for k, v in (env or {}).items():
            cmd += ["-e", f"{k}={v}"]
        if privileged:
            logger.warning("Apple Containers: --privileged flag not applicable (VM isolation)")
        if seccomp:
            logger.info("Apple Containers: seccomp profiles not needed (VM isolation)")
        if caps:
            logger.info("Apple Containers: capability flags not applicable (VM isolation)")
        cmd.append(image)
        return self._run(cmd).stdout.strip()

    def stop(self, name: str, timeout: int = 10) -> None:
        self._cmd("stop", name)

    def rm(self, name: str, force: bool = False) -> None:
        cmd = ["rm"]
        if force:
            cmd.append("-f")
        cmd.append(name)
        self._cmd(*cmd)

    def pause(self, name: str) -> None:
        # Apple Containers may not support pause — graceful degradation
        try:
            self._cmd("pause", name)
        except Exception:
            logger.warning("Apple Containers: pause not supported, stopping instead")
            self.stop(name)

    def unpause(self, name: str) -> None:
        try:
            self._cmd("unpause", name)
        except Exception:
            logger.warning("Apple Containers: unpause not supported")

    def ps(self, all: bool = False) -> list[ContainerInfo]:
        cmd = [self._cli, "list"]
        if all:
            cmd.append("--all")
        result = self._run(cmd, check=False)
        containers = []
        # Parse text output (Apple container list format)
        lines = (result.stdout or "").strip().splitlines()
        for line in lines[1:]:  # skip header
            parts = line.split()
            if len(parts) >= 3:
                containers.append(
                    ContainerInfo(
                        name=parts[1] if len(parts) > 1 else "",
                        id=parts[0],
                        image=parts[2] if len(parts) > 2 else "",
                        status=parts[3] if len(parts) > 3 else "",
                        raw={"line": line},
                    )
                )
        return containers

    def logs(self, name: str, tail: int = 100) -> str:
        return self._cmd("logs", "--tail", str(tail), name)

    def exec(self, name: str, command: list[str]) -> str:
        return self._cmd("exec", name, *command)

    def inspect(self, name: str) -> dict[str, Any]:
        raw = self._cmd("inspect", name)
        try:
            data = json.loads(raw)
            return data[0] if isinstance(data, list) else data
        except json.JSONDecodeError:
            return {"raw": raw}

    # -- networking & volumes --------------------------------------------

    def network_create(self, name: str, internal: bool = False) -> str:
        try:
            return self._cmd("network", "create", name)
        except Exception:
            logger.warning("Apple Containers: network management may be limited")
            return ""

    def network_rm(self, name: str) -> None:
        try:
            self._cmd("network", "rm", name)
        except Exception:
            logger.warning("Apple Containers: network removal not supported")

    def volume_create(self, name: str) -> str:
        try:
            return self._cmd("volume", "create", name)
        except Exception:
            logger.warning("Apple Containers: volume management may be limited")
            return ""

    def volume_rm(self, name: str) -> None:
        try:
            self._cmd("volume", "rm", name)
        except Exception:
            logger.warning("Apple Containers: volume removal not supported")

    # -- compose ---------------------------------------------------------

    def compose_up(self, file: str, detach: bool = True) -> str:
        # Apple Containers has no compose — handled by compose_generator shell scripts
        raise NotImplementedError(
            "Apple Containers does not support compose. "
            "Use compose_generator.py to create a startup script."
        )

    def compose_down(self, file: str) -> str:
        raise NotImplementedError(
            "Apple Containers does not support compose. " "Use the generated shutdown script."
        )

    # -- health ----------------------------------------------------------

    def health_check(self) -> bool:
        try:
            self._cmd("--version", timeout=10)
            return True
        except Exception:
            return False
