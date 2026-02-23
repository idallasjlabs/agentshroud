# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Runtime-specific security feature mapping.

Maps security capabilities per container runtime and warns about gaps.
"""


import logging
from dataclasses import dataclass

logger = logging.getLogger("agentshroud.runtime.security")


@dataclass
class SecurityFeature:
    """A security feature with runtime support info."""

    name: str
    description: str
    docker: bool = False
    podman: bool = False
    apple: bool = False
    docker_notes: str = ""
    podman_notes: str = ""
    apple_notes: str = ""


# Master registry of security features
SECURITY_FEATURES: list[SecurityFeature] = [
    SecurityFeature(
        name="seccomp",
        description="Syscall filtering via seccomp profiles",
        docker=True,
        podman=True,
        apple=False,
        docker_notes="Custom profiles via --security-opt seccomp=<profile>",
        podman_notes="Custom profiles via --security-opt seccomp=<profile>",
        apple_notes="Not needed — VM isolation provides stronger boundary",
    ),
    SecurityFeature(
        name="cap_drop",
        description="Drop Linux capabilities for least-privilege",
        docker=True,
        podman=True,
        apple=False,
        docker_notes="--cap-drop ALL --cap-add <needed>",
        podman_notes="--cap-drop ALL --cap-add <needed>; rootless drops more by default",
        apple_notes="Not applicable — VM isolation",
    ),
    SecurityFeature(
        name="read_only_rootfs",
        description="Read-only root filesystem",
        docker=True,
        podman=True,
        apple=False,
        docker_notes="--read-only flag",
        podman_notes="--read-only flag",
        apple_notes="VM filesystem management differs",
    ),
    SecurityFeature(
        name="no_new_privileges",
        description="Prevent privilege escalation",
        docker=True,
        podman=True,
        apple=False,
        docker_notes="--security-opt=no-new-privileges",
        podman_notes="--security-opt=no-new-privileges; default in rootless",
        apple_notes="VM isolation prevents host privilege escalation",
    ),
    SecurityFeature(
        name="rootless",
        description="Run without root/daemon",
        docker=False,
        podman=True,
        apple=True,
        docker_notes="Requires rootless Docker setup (not default)",
        podman_notes="Default mode — no daemon, no root",
        apple_notes="No daemon; runs as user",
    ),
    SecurityFeature(
        name="selinux",
        description="SELinux label enforcement on volumes",
        docker=False,
        podman=True,
        apple=False,
        docker_notes="Requires manual setup",
        podman_notes=":z/:Z volume labels for automatic SELinux context",
        apple_notes="Not applicable on macOS",
    ),
    SecurityFeature(
        name="vm_isolation",
        description="Hardware-level VM isolation per container",
        docker=False,
        podman=False,
        apple=True,
        docker_notes="Not available (namespace isolation only)",
        podman_notes="Not available (namespace isolation only)",
        apple_notes="Each container runs in its own lightweight VM",
    ),
    SecurityFeature(
        name="user_namespace",
        description="User namespace remapping",
        docker=True,
        podman=True,
        apple=True,
        docker_notes="--userns-remap flag",
        podman_notes="Automatic in rootless mode",
        apple_notes="VM provides user isolation",
    ),
]


VALID_RUNTIMES = frozenset({"docker", "podman", "apple"})


def _validate_runtime(runtime: str) -> str:
    """Validate runtime name to prevent attribute access injection."""
    if runtime not in VALID_RUNTIMES:
        raise ValueError(
            f"Invalid runtime: {runtime!r}. Must be one of: {sorted(VALID_RUNTIMES)}"
        )
    return runtime


def get_features_for_runtime(runtime: str) -> list[SecurityFeature]:
    """Return features available for a given runtime."""
    _validate_runtime(runtime)
    return [f for f in SECURITY_FEATURES if getattr(f, runtime, False)]


def get_missing_features(runtime: str) -> list[SecurityFeature]:
    """Return features NOT available for a given runtime."""
    _validate_runtime(runtime)
    return [f for f in SECURITY_FEATURES if not getattr(f, runtime, False)]


def get_security_comparison() -> dict[str, dict[str, bool]]:
    """Return a comparison dict: {feature_name: {runtime: supported}}."""
    return {
        f.name: {"docker": f.docker, "podman": f.podman, "apple": f.apple}
        for f in SECURITY_FEATURES
    }


def warn_missing_features(runtime: str) -> list[str]:
    """Return warning messages for missing security features."""
    _validate_runtime(runtime)
    warnings = []
    for feat in get_missing_features(runtime):
        notes = getattr(feat, f"{runtime}_notes", "")
        msg = f"[{runtime}] Missing: {feat.name} — {feat.description}"
        if notes:
            msg += f" ({notes})"
        warnings.append(msg)
        logger.warning(msg)
    return warnings


def get_security_options(runtime: str) -> dict:
    """Return recommended security CLI options for a runtime."""
    _validate_runtime(runtime)
    if runtime == "docker":
        return {
            "security_opt": [
                "no-new-privileges",
                "seccomp=docker/seccomp/agentshroud-seccomp.json",
            ],
            "cap_drop": ["ALL"],
            "cap_add": ["NET_BIND_SERVICE"],
            "read_only": True,
        }
    elif runtime == "podman":
        return {
            "security_opt": ["no-new-privileges"],
            "cap_drop": ["ALL"],
            "cap_add": ["NET_BIND_SERVICE"],
            "read_only": True,
            "userns": "auto",
        }
    elif runtime == "apple":
        return {
            "notes": "VM isolation provides hardware-level security boundary",
        }
    return {}
