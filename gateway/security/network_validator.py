"""
Container Network Isolation Validator - Security Hardening Module
Validate docker-compose network configuration and detect security issues.
"""

import yaml
import json
import logging
import docker
import time
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class NetworkSecurityFinding:
    """A network security finding."""

    category: str
    severity: str  # critical, high, medium, low
    service_name: str
    description: str
    details: Dict[str, Any]
    remediation: str


@dataclass
class NetworkConfiguration:
    """Container network configuration."""

    service_name: str
    networks: List[str]
    exposed_ports: List[str]
    published_ports: List[str]
    network_mode: Optional[str] = None
    dns_servers: Optional[List[str]] = None
    links: Optional[List[str]] = None
    privileged: bool = False


class NetworkValidator:
    """Validate container network isolation and security."""

    def __init__(self):
        self.docker_client = None
        self.findings: List[NetworkSecurityFinding] = []
        self.expected_networks = {
            "openclaw_internal",  # Internal network for AgentShroud components
            "openclaw_external",  # External network for internet access
            "default",  # Docker default network
        }
        self.gateway_service = "gateway"  # Service that should bridge networks

        try:
            self.docker_client = docker.from_env()
        except Exception as e:
            logger.error(f"Failed to connect to Docker: {e}")

    def validate_docker_compose_config(
        self, compose_file_path: str
    ) -> List[NetworkSecurityFinding]:
        """
        Validate docker-compose network configuration.

        Args:
            compose_file_path: Path to docker-compose.yml file

        Returns:
            List of network security findings
        """
        findings = []

        try:
            with open(compose_file_path, "r") as f:
                compose_config = yaml.safe_load(f)

            services = compose_config.get("services", {})
            networks = compose_config.get("networks", {})

            # Parse service configurations
            service_configs = {}
            for service_name, service_config in services.items():
                service_configs[service_name] = self._parse_service_network_config(
                    service_name, service_config
                )

            # Validate network configurations
            findings.extend(self._validate_network_definitions(networks))
            findings.extend(self._validate_service_network_isolation(service_configs))
            findings.extend(self._validate_port_exposure(service_configs))
            findings.extend(self._validate_dns_configuration(service_configs))
            findings.extend(self._validate_network_modes(service_configs))
            findings.extend(self._validate_privileged_containers(service_configs))

        except Exception as e:
            logger.error(f"Error validating docker-compose config: {e}")
            findings.append(
                NetworkSecurityFinding(
                    category="config_error",
                    severity="high",
                    service_name="unknown",
                    description="Failed to parse docker-compose configuration",
                    details={"error": str(e)},
                    remediation="Fix docker-compose.yml syntax errors",
                )
            )

        self.findings.extend(findings)
        return findings

    def _parse_service_network_config(
        self, service_name: str, service_config: Dict[str, Any]
    ) -> NetworkConfiguration:
        """Parse network configuration for a service."""
        networks = []
        exposed_ports = []
        published_ports = []
        network_mode = service_config.get("network_mode")
        dns_servers = service_config.get("dns")
        links = service_config.get("links")

        # Parse networks
        service_networks = service_config.get("networks", [])
        if isinstance(service_networks, list):
            networks = service_networks
        elif isinstance(service_networks, dict):
            networks = list(service_networks.keys())

        # Parse ports
        service_ports = service_config.get("ports", [])
        for port in service_ports:
            if isinstance(port, str):
                if ":" in port:
                    published_ports.append(port)
                else:
                    exposed_ports.append(port)
            elif isinstance(port, dict):
                target = port.get("target")
                published = port.get("published")
                if published:
                    published_ports.append(f"{published}:{target}")
                else:
                    exposed_ports.append(str(target))

        # Parse expose directive
        expose_ports = service_config.get("expose", [])
        exposed_ports.extend([str(p) for p in expose_ports])

        # Parse privileged flag
        privileged = service_config.get("privileged", False)

        return NetworkConfiguration(
            service_name=service_name,
            networks=networks,
            exposed_ports=exposed_ports,
            published_ports=published_ports,
            network_mode=network_mode,
            dns_servers=dns_servers,
            links=links,
            privileged=privileged,
        )

    def _validate_network_definitions(
        self, networks: Dict[str, Any]
    ) -> List[NetworkSecurityFinding]:
        """Validate network definitions in compose file."""
        findings = []

        # Check for required networks
        if "openclaw_internal" not in networks:
            findings.append(
                NetworkSecurityFinding(
                    category="missing_network",
                    severity="high",
                    service_name="infrastructure",
                    description="Missing internal network definition",
                    details={"missing_network": "openclaw_internal"},
                    remediation="Add openclaw_internal network for internal communication",
                )
            )

        # Validate network configurations
        for network_name, network_config in networks.items():
            if network_config is None:
                continue

            # Check for external networks
            if network_config.get("external", False):
                findings.append(
                    NetworkSecurityFinding(
                        category="external_network",
                        severity="medium",
                        service_name="infrastructure",
                        description="External network detected",
                        details={"network": network_name},
                        remediation="Verify external network is properly secured",
                    )
                )

            # Check for bridge driver configuration
            driver = network_config.get("driver", "bridge")
            if driver == "host":
                findings.append(
                    NetworkSecurityFinding(
                        category="insecure_driver",
                        severity="critical",
                        service_name="infrastructure",
                        description="Host network driver detected - breaks container isolation",
                        details={"network": network_name, "driver": driver},
                        remediation="Use bridge driver instead of host driver",
                    )
                )

        return findings

    def _validate_service_network_isolation(
        self, service_configs: Dict[str, NetworkConfiguration]
    ) -> List[NetworkSecurityFinding]:
        """Validate service network isolation."""
        findings = []

        for service_name, config in service_configs.items():
            # Check if OpenClaw container is on internal network only
            if (
                service_name.startswith("openclaw")
                and service_name != self.gateway_service
            ):
                if "openclaw_external" in config.networks:
                    findings.append(
                        NetworkSecurityFinding(
                            category="network_isolation_breach",
                            severity="critical",
                            service_name=service_name,
                            description="Internal service has external network access",
                            details={"networks": config.networks},
                            remediation=f"Remove {service_name} from openclaw_external network",
                        )
                    )

                if "openclaw_internal" not in config.networks:
                    findings.append(
                        NetworkSecurityFinding(
                            category="missing_internal_network",
                            severity="high",
                            service_name=service_name,
                            description="Service missing from internal network",
                            details={"networks": config.networks},
                            remediation=f"Add {service_name} to openclaw_internal network",
                        )
                    )

            # Check if gateway bridges internal and external
            elif service_name == self.gateway_service:
                if "openclaw_internal" not in config.networks:
                    findings.append(
                        NetworkSecurityFinding(
                            category="gateway_misconfiguration",
                            severity="critical",
                            service_name=service_name,
                            description="Gateway missing from internal network",
                            details={"networks": config.networks},
                            remediation="Add gateway to openclaw_internal network",
                        )
                    )

                if "openclaw_external" not in config.networks:
                    findings.append(
                        NetworkSecurityFinding(
                            category="gateway_misconfiguration",
                            severity="high",
                            service_name=service_name,
                            description="Gateway missing from external network",
                            details={"networks": config.networks},
                            remediation="Add gateway to openclaw_external network",
                        )
                    )

        return findings

    def _validate_port_exposure(
        self, service_configs: Dict[str, NetworkConfiguration]
    ) -> List[NetworkSecurityFinding]:
        """Validate port exposure configuration."""
        findings = []

        # Known dangerous ports
        dangerous_ports = {
            "22": "SSH",
            "23": "Telnet",
            "25": "SMTP",
            "53": "DNS",
            "80": "HTTP (should use reverse proxy)",
            "443": "HTTPS (should use reverse proxy)",
            "3389": "RDP",
            "5432": "PostgreSQL",
            "3306": "MySQL",
            "27017": "MongoDB",
            "6379": "Redis",
            "9200": "Elasticsearch",
        }

        for service_name, config in service_configs.items():
            # Check published ports
            for port_mapping in config.published_ports:
                if ":" in port_mapping:
                    host_port = port_mapping.split(":")[0]
                    if host_port in dangerous_ports:
                        findings.append(
                            NetworkSecurityFinding(
                                category="dangerous_port_exposure",
                                severity=(
                                    "high"
                                    if host_port in ["22", "3389", "5432", "3306"]
                                    else "medium"
                                ),
                                service_name=service_name,
                                description=f"Dangerous port {host_port} ({dangerous_ports[host_port]}) exposed",
                                details={
                                    "port_mapping": port_mapping,
                                    "service": dangerous_ports[host_port],
                                },
                                remediation=f"Remove port {host_port} exposure or use reverse proxy",
                            )
                        )

            # Check for services that shouldn't expose ports
            if (
                service_name.startswith("openclaw")
                and service_name != self.gateway_service
            ):
                if config.published_ports:
                    findings.append(
                        NetworkSecurityFinding(
                            category="unnecessary_port_exposure",
                            severity="medium",
                            service_name=service_name,
                            description="Internal service exposes ports unnecessarily",
                            details={"published_ports": config.published_ports},
                            remediation="Remove port publishing for internal services",
                        )
                    )

        return findings

    def _validate_dns_configuration(
        self, service_configs: Dict[str, NetworkConfiguration]
    ) -> List[NetworkSecurityFinding]:
        """Validate DNS configuration for security."""
        findings = []

        for service_name, config in service_configs.items():
            if config.dns_servers:
                # Check for public DNS servers (potential DNS exfiltration)
                public_dns_servers = ["8.8.8.8", "8.8.4.4", "1.1.1.1", "1.0.0.1"]
                for dns_server in config.dns_servers:
                    if dns_server in public_dns_servers:
                        findings.append(
                            NetworkSecurityFinding(
                                category="public_dns_usage",
                                severity="medium",
                                service_name=service_name,
                                description="Service uses public DNS servers",
                                details={
                                    "dns_servers": config.dns_servers,
                                    "public_server": dns_server,
                                },
                                remediation="Configure DNS to point to gateway for filtering",
                            )
                        )

        return findings

    def _validate_network_modes(
        self, service_configs: Dict[str, NetworkConfiguration]
    ) -> List[NetworkSecurityFinding]:
        """Validate network mode configurations."""
        findings = []

        for service_name, config in service_configs.items():
            if config.network_mode == "host":
                findings.append(
                    NetworkSecurityFinding(
                        category="host_network_mode",
                        severity="critical",
                        service_name=service_name,
                        description="Service uses host network mode - breaks container isolation",
                        details={"network_mode": config.network_mode},
                        remediation="Remove network_mode: host and use proper networks",
                    )
                )
            elif config.network_mode and config.network_mode.startswith("container:"):
                findings.append(
                    NetworkSecurityFinding(
                        category="container_network_mode",
                        severity="medium",
                        service_name=service_name,
                        description="Service shares network with another container",
                        details={"network_mode": config.network_mode},
                        remediation="Verify network sharing is intentional and secure",
                    )
                )

        return findings

    def _validate_privileged_containers(
        self, service_configs: Dict[str, NetworkConfiguration]
    ) -> List[NetworkSecurityFinding]:
        """Validate that no containers are running in privileged mode."""
        findings = []

        for service_name, config in service_configs.items():
            if config.privileged:
                findings.append(
                    NetworkSecurityFinding(
                        category="privileged_container",
                        severity="critical",
                        service_name=service_name,
                        description="Service runs with privileged flag - full host access",
                        details={"privileged": config.privileged},
                        remediation="Remove privileged: true and use specific capabilities instead",
                    )
                )

        return findings

    def validate_runtime_configuration(self) -> List[NetworkSecurityFinding]:
        """Validate runtime network configuration using Docker API."""
        findings = []

        if not self.docker_client:
            findings.append(
                NetworkSecurityFinding(
                    category="runtime_check_failed",
                    severity="medium",
                    service_name="infrastructure",
                    description="Cannot validate runtime configuration - Docker client unavailable",
                    details={},
                    remediation="Ensure Docker is running and accessible",
                )
            )
            return findings

        try:
            # Check networks
            networks = self.docker_client.networks.list()
            network_names = {network.name for network in networks}

            if "openclaw_internal" not in network_names:
                findings.append(
                    NetworkSecurityFinding(
                        category="missing_runtime_network",
                        severity="high",
                        service_name="infrastructure",
                        description="Internal network not found in runtime",
                        details={"available_networks": list(network_names)},
                        remediation="Create openclaw_internal network",
                    )
                )

            # Check containers
            containers = self.docker_client.containers.list()
            for container in containers:
                findings.extend(self._validate_container_runtime_config(container))

        except Exception as e:
            logger.error(f"Error validating runtime configuration: {e}")
            findings.append(
                NetworkSecurityFinding(
                    category="runtime_validation_error",
                    severity="medium",
                    service_name="infrastructure",
                    description="Failed to validate runtime configuration",
                    details={"error": str(e)},
                    remediation="Check Docker daemon and permissions",
                )
            )

        return findings

    def _validate_container_runtime_config(
        self, container
    ) -> List[NetworkSecurityFinding]:
        """Validate a single container's runtime network configuration."""
        findings = []

        try:
            container_name = container.name
            network_settings = container.attrs["NetworkSettings"]

            # Check network modes
            if network_settings.get("NetworkMode") == "host":
                findings.append(
                    NetworkSecurityFinding(
                        category="runtime_host_mode",
                        severity="critical",
                        service_name=container_name,
                        description="Container running in host network mode",
                        details={"network_mode": "host"},
                        remediation=f"Restart {container_name} without host networking",
                    )
                )

            # Check port bindings
            port_bindings = network_settings.get("Ports", {})
            exposed_ports = []
            for container_port, host_bindings in port_bindings.items():
                if host_bindings:
                    for binding in host_bindings:
                        host_port = binding.get("HostPort")
                        if host_port:
                            exposed_ports.append(f"{host_port}:{container_port}")

            if (
                exposed_ports
                and container_name.startswith("openclaw")
                and "gateway" not in container_name
            ):
                findings.append(
                    NetworkSecurityFinding(
                        category="runtime_unnecessary_exposure",
                        severity="medium",
                        service_name=container_name,
                        description="Internal container has exposed ports at runtime",
                        details={"exposed_ports": exposed_ports},
                        remediation=f"Remove port exposure from {container_name}",
                    )
                )

        except Exception as e:
            logger.error(f"Error validating container {container.name}: {e}")

        return findings

    def detect_configuration_drift(
        self, compose_file_path: str
    ) -> List[NetworkSecurityFinding]:
        """Detect drift between compose file and runtime configuration."""
        findings = []

        # This would compare the compose file configuration with actual runtime state
        # and detect any differences that might indicate tampering or misconfiguration

        try:
            compose_findings = self.validate_docker_compose_config(compose_file_path)
            runtime_findings = self.validate_runtime_configuration()

            # Compare findings to detect drift
            compose_issues = {(f.service_name, f.category) for f in compose_findings}
            runtime_issues = {(f.service_name, f.category) for f in runtime_findings}

            # Issues that appear in runtime but not in compose file analysis
            drift_issues = runtime_issues - compose_issues
            for service_name, category in drift_issues:
                findings.append(
                    NetworkSecurityFinding(
                        category="configuration_drift",
                        severity="medium",
                        service_name=service_name,
                        description=f"Runtime configuration differs from compose file: {category}",
                        details={"drift_category": category},
                        remediation="Investigate configuration changes and update compose file",
                    )
                )

        except Exception as e:
            logger.error(f"Error detecting configuration drift: {e}")

        return findings

    def get_security_report(self) -> Dict[str, Any]:
        """Get comprehensive network security report."""
        return {
            "total_findings": len(self.findings),
            "by_severity": {
                "critical": len([f for f in self.findings if f.severity == "critical"]),
                "high": len([f for f in self.findings if f.severity == "high"]),
                "medium": len([f for f in self.findings if f.severity == "medium"]),
                "low": len([f for f in self.findings if f.severity == "low"]),
            },
            "by_category": {},
            "services_with_issues": list(set(f.service_name for f in self.findings)),
            "critical_findings": [
                {
                    "service": f.service_name,
                    "description": f.description,
                    "remediation": f.remediation,
                }
                for f in self.findings
                if f.severity == "critical"
            ],
        }

    def export_report(self, output_path: str):
        """Export network security report to file."""
        report = {
            "timestamp": time.time(),
            "summary": self.get_security_report(),
            "findings": [
                {
                    "category": f.category,
                    "severity": f.severity,
                    "service_name": f.service_name,
                    "description": f.description,
                    "details": f.details,
                    "remediation": f.remediation,
                }
                for f in self.findings
            ],
        }

        with open(output_path, "w") as file:
            json.dump(report, file, indent=2)

        logger.info(f"Network security report exported to {output_path}")


def validate_network_security(compose_file_path: str) -> NetworkValidator:
    """Convenience function to validate network security."""
    validator = NetworkValidator()
    validator.validate_docker_compose_config(compose_file_path)
    validator.validate_runtime_configuration()
    return validator
