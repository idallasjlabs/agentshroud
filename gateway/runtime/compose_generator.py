# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Compose file generator for different container runtimes.

Generates docker-compose.yml / podman-compose.yml, or shell scripts for
Apple Containers which lacks compose support.
"""


import logging
from dataclasses import dataclass, field
from typing import Optional

import yaml

logger = logging.getLogger("agentshroud.runtime.compose")


@dataclass
class ServiceDef:
    """Definition of a single service for compose generation."""

    name: str
    image: str
    build: Optional[str] = None  # Dockerfile/Containerfile path
    build_context: str = "."
    ports: list[str] = field(default_factory=list)
    volumes: list[str] = field(default_factory=list)
    environment: dict[str, str] = field(default_factory=dict)
    env_file: Optional[str] = None
    networks: list[str] = field(default_factory=list)
    depends_on: list[str] = field(default_factory=list)
    restart: str = "unless-stopped"
    healthcheck: Optional[dict] = None
    security_opt: list[str] = field(default_factory=list)
    cap_drop: list[str] = field(default_factory=list)
    cap_add: list[str] = field(default_factory=list)
    read_only: bool = False
    privileged: bool = False


# Default AgentShroud services
DEFAULT_SERVICES = [
    ServiceDef(
        name="gateway",
        image="agentshroud-gateway:latest",
        build="gateway/Dockerfile",
        ports=["127.0.0.1:8080:8080"],
        volumes=[
            "gateway-data:/app/data",
            "./agentshroud.yaml:/app/agentshroud.yaml:ro",
        ],
        networks=["agentshroud-internal"],
        security_opt=["no-new-privileges"],
        cap_drop=["ALL"],
        cap_add=["NET_BIND_SERVICE"],
        read_only=True,
        healthcheck={
            "test": [
                "CMD",
                "python",
                "-c",
                "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/status')",
            ],
            "interval": "30s",
            "timeout": "5s",
            "retries": 3,
        },
    ),
    ServiceDef(
        name="openclaw",
        image="agentshroud-openclaw:latest",
        build="docker/Dockerfile.openclaw",
        ports=["127.0.0.1:18789:18789"],
        volumes=["openclaw-data:/home/node/.openclaw"],
        networks=["agentshroud-internal"],
        depends_on=["gateway"],
        healthcheck={
            "test": ["CMD", "curl", "-f", "http://localhost:18789/api/health"],
            "interval": "30s",
            "timeout": "10s",
            "retries": 3,
        },
    ),
]


def generate_compose(
    services: Optional[list[ServiceDef]] = None,
    runtime: str = "docker",
) -> str:
    """Generate a compose YAML file for Docker or Podman.

    Args:
        services: List of service definitions. Uses defaults if None.
        runtime: Target runtime (docker/podman). Affects volume labels etc.

    Returns:
        YAML string.
    """
    if services is None:
        services = DEFAULT_SERVICES

    compose: dict = {
        "version": "3.8",
        "services": {},
        "networks": {},
        "volumes": {},
    }

    all_networks: set[str] = set()
    all_volumes: set[str] = set()

    for svc in services:
        svc_dict: dict = {"image": svc.image}

        if svc.build:
            svc_dict["build"] = {
                "context": svc.build_context,
                "dockerfile": svc.build,
            }

        if svc.ports:
            svc_dict["ports"] = svc.ports
        if svc.environment:
            svc_dict["environment"] = svc.environment
        if svc.env_file:
            svc_dict["env_file"] = svc.env_file
        if svc.depends_on:
            svc_dict["depends_on"] = svc.depends_on
        if svc.restart:
            svc_dict["restart"] = svc.restart
        if svc.healthcheck:
            svc_dict["healthcheck"] = svc.healthcheck

        # Security options
        sec_opts = list(svc.security_opt)
        if sec_opts:
            svc_dict["security_opt"] = sec_opts
        if svc.cap_drop:
            svc_dict["cap_drop"] = svc.cap_drop
        if svc.cap_add:
            svc_dict["cap_add"] = svc.cap_add
        if svc.read_only:
            svc_dict["read_only"] = True

        # Volumes with runtime-specific labels
        if svc.volumes:
            vols = []
            for v in svc.volumes:
                if runtime == "podman" and ":" in v and not v.endswith(":z"):
                    v = v + ":z" if ":ro" not in v else v.replace(":ro", ":ro,z")
                vols.append(v)
            svc_dict["volumes"] = vols

        if svc.networks:
            svc_dict["networks"] = svc.networks
            all_networks.update(svc.networks)

        # Extract named volumes
        for v in svc.volumes:
            vol_name = v.split(":")[0]
            if not vol_name.startswith((".", "/", "~")):
                all_volumes.add(vol_name)

        compose["services"][svc.name] = svc_dict

    for net in all_networks:
        compose["networks"][net] = {"driver": "bridge"}
    for vol in all_volumes:
        compose["volumes"][vol] = None

    return yaml.dump(compose, default_flow_style=False, sort_keys=False)


def generate_apple_script(
    services: Optional[list[ServiceDef]] = None,
) -> str:
    """Generate a shell script to start services with Apple Containers.

    Apple Containers lacks compose, so we generate start/stop scripts.
    """
    if services is None:
        services = DEFAULT_SERVICES

    lines = [
        "#!/bin/zsh",
        "# AgentShroud — Apple Containers startup script",
        "# Generated by compose_generator.py",
        "set -euo pipefail",
        "",
        'ACTION="${1:-up}"',
        "",
        'if [[ "$ACTION" == "up" ]]; then',
        '  echo "Starting AgentShroud services..."',
    ]

    for svc in services:
        cmd_parts = [f"  container run -d --name {svc.name}"]
        for p in svc.ports:
            cmd_parts.append(f"    -p {p}")
        for v in svc.volumes:
            cmd_parts.append(f"    -v {v}")
        for k, val in svc.environment.items():
            cmd_parts.append(f"    -e {k}={val}")
        cmd_parts.append(f"    {svc.image}")
        lines.append(" \\\n".join(cmd_parts))
        lines.append(f'  echo "  ✅ {svc.name} started"')

    lines += [
        "",
        'elif [[ "$ACTION" == "down" ]]; then',
        '  echo "Stopping AgentShroud services..."',
    ]

    for svc in reversed(services):
        lines.append(f"  container stop {svc.name} 2>/dev/null || true")
        lines.append(f"  container rm {svc.name} 2>/dev/null || true")

    lines += [
        "",
        'elif [[ "$ACTION" == "status" ]]; then',
        "  container list",
        "",
        "else",
        '  echo "Usage: $0 [up|down|status]"',
        "fi",
    ]

    return "\n".join(lines) + "\n"
