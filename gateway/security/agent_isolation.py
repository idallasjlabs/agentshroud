"""
Per-Agent Container Isolation — agent registry and isolation verification.

Maps agent IDs to container configurations and validates
network namespace separation and shared-nothing constraints.
"""

import json
import subprocess
from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Optional


class IsolationStatus(str, Enum):
    ISOLATED = "isolated"
    SHARED = "shared"
    UNKNOWN = "unknown"
    VIOLATION = "violation"


@dataclass
class ContainerConfig:
    agent_id: str
    container_name: str
    network: str
    volume: str
    image: str = "secureclaw/agent:latest"
    cpu_limit: str = "1.0"
    memory_limit: str = "512m"
    read_only_root: bool = True
    no_new_privileges: bool = True
    seccomp_profile: str = "default"
    capabilities_drop: list[str] = field(default_factory=lambda: ["ALL"])
    capabilities_add: list[str] = field(default_factory=list)
    env_vars: dict[str, str] = field(default_factory=dict)


@dataclass
class IsolationCheck:
    agent_id: str
    status: IsolationStatus
    issues: list[str]
    details: dict = field(default_factory=dict)


class AgentRegistry:
    """Registry mapping agent IDs to container configurations."""

    def __init__(self):
        self._agents: dict[str, ContainerConfig] = {}

    def register(self, config: ContainerConfig) -> None:
        """Register an agent with its container configuration."""
        self._agents[config.agent_id] = config

    def unregister(self, agent_id: str) -> Optional[ContainerConfig]:
        """Remove an agent from the registry."""
        return self._agents.pop(agent_id, None)

    def get(self, agent_id: str) -> Optional[ContainerConfig]:
        """Get container config for an agent."""
        return self._agents.get(agent_id)

    def list_agents(self) -> list[str]:
        """List all registered agent IDs."""
        return list(self._agents.keys())

    def to_dict(self) -> dict:
        """Serialize registry to dict."""
        return {aid: asdict(cfg) for aid, cfg in self._agents.items()}

    @classmethod
    def from_dict(cls, data: dict) -> "AgentRegistry":
        """Deserialize registry from dict."""
        reg = cls()
        for aid, cfg_data in data.items():
            reg.register(ContainerConfig(**cfg_data))
        return reg


class IsolationVerifier:
    """Verify container isolation properties."""

    def __init__(self, registry: AgentRegistry):
        self.registry = registry

    def verify_network_isolation(self) -> list[IsolationCheck]:
        """Verify that each agent has its own network namespace."""
        results = []
        networks_seen: dict[str, str] = {}

        for agent_id in self.registry.list_agents():
            config = self.registry.get(agent_id)
            issues = []

            if config.network in networks_seen:
                issues.append(
                    f"Network '{config.network}' shared with agent "
                    f"'{networks_seen[config.network]}'"
                )
                status = IsolationStatus.VIOLATION
            else:
                networks_seen[config.network] = agent_id
                status = IsolationStatus.ISOLATED

            results.append(
                IsolationCheck(
                    agent_id=agent_id,
                    status=status,
                    issues=issues,
                    details={"network": config.network},
                )
            )
        return results

    def verify_volume_isolation(self) -> list[IsolationCheck]:
        """Verify that each agent has its own volume (no shared filesystems)."""
        results = []
        volumes_seen: dict[str, str] = {}

        for agent_id in self.registry.list_agents():
            config = self.registry.get(agent_id)
            issues = []

            if config.volume in volumes_seen:
                issues.append(
                    f"Volume '{config.volume}' shared with agent "
                    f"'{volumes_seen[config.volume]}'"
                )
                status = IsolationStatus.VIOLATION
            else:
                volumes_seen[config.volume] = agent_id
                status = IsolationStatus.ISOLATED

            results.append(
                IsolationCheck(
                    agent_id=agent_id,
                    status=status,
                    issues=issues,
                    details={"volume": config.volume},
                )
            )
        return results

    def verify_shared_nothing(self) -> list[IsolationCheck]:
        """Full shared-nothing verification: network + volume + security settings."""
        results = []
        network_checks = {c.agent_id: c for c in self.verify_network_isolation()}
        volume_checks = {c.agent_id: c for c in self.verify_volume_isolation()}

        for agent_id in self.registry.list_agents():
            config = self.registry.get(agent_id)
            issues = []

            # Merge network/volume issues
            if agent_id in network_checks:
                issues.extend(network_checks[agent_id].issues)
            if agent_id in volume_checks:
                issues.extend(volume_checks[agent_id].issues)

            # Security checks
            if not config.read_only_root:
                issues.append("Root filesystem is not read-only")
            if not config.no_new_privileges:
                issues.append("no_new_privileges is not set")
            if "ALL" not in config.capabilities_drop:
                issues.append("Not all capabilities are dropped")

            status = IsolationStatus.VIOLATION if issues else IsolationStatus.ISOLATED
            results.append(
                IsolationCheck(agent_id=agent_id, status=status, issues=issues)
            )
        return results

    def generate_compose(self) -> dict:
        """Generate Docker Compose config for all registered agents."""
        services = {}
        networks = {}
        volumes = {}

        for agent_id in self.registry.list_agents():
            config = self.registry.get(agent_id)
            svc_name = f"agent-{agent_id}"

            services[svc_name] = {
                "image": config.image,
                "container_name": config.container_name,
                "networks": [config.network],
                "volumes": [f"{config.volume}:/data"],
                "deploy": {
                    "resources": {
                        "limits": {
                            "cpus": config.cpu_limit,
                            "memory": config.memory_limit,
                        }
                    }
                },
                "read_only": config.read_only_root,
                "security_opt": [
                    "no-new-privileges:true",
                    f"seccomp:{config.seccomp_profile}",
                ],
                "cap_drop": config.capabilities_drop,
                "environment": config.env_vars,
            }
            if config.capabilities_add:
                services[svc_name]["cap_add"] = config.capabilities_add

            networks[config.network] = {"driver": "bridge", "internal": True}
            volumes[config.volume] = {"driver": "local"}

        return {
            "version": "3.8",
            "services": services,
            "networks": networks,
            "volumes": volumes,
        }
