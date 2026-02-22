# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Configuration loader for AgentShroud Gateway

Loads configuration from agentshroud.yaml and provides typed access via Pydantic models.
"""

import logging
import secrets
from pathlib import Path
from urllib.parse import urlparse

import yaml
from pydantic import BaseModel, Field, field_validator
from .ssh_config import SSHConfig

logger = logging.getLogger("agentshroud.gateway.config")


class PIIConfig(BaseModel):
    """PII detection and redaction configuration"""

    engine: str = "presidio"
    entities: list[str] = Field(default_factory=list)
    enabled: bool = True
    min_confidence: float = 0.7


class LedgerConfig(BaseModel):
    """Data ledger configuration"""

    backend: str = "sqlite"
    path: Path = Field(default=Path("./gateway/data/ledger.db"))
    retention_days: int = 90


class RouterConfig(BaseModel):
    """Multi-agent router configuration"""

    enabled: bool = True
    default_target: str = "general"
    default_url: str = "http://openclaw:18789"
    targets: dict[str, str] = Field(default_factory=dict)

    @field_validator("default_url")
    @classmethod
    def validate_default_url(cls, v: str) -> str:
        """Validate that default_url uses http/https and points to localhost or openclaw"""
        if not v.startswith(("http://", "https://")):
            raise ValueError("default_url must start with http:// or https://")

        parsed = urlparse(v)
        allowed_hosts = ["localhost", "127.0.0.1", "openclaw"]

        if parsed.hostname not in allowed_hosts:
            raise ValueError(
                f"default_url host must be one of {allowed_hosts}, got: {parsed.hostname}"
            )

        return v

    @field_validator("targets")
    @classmethod
    def validate_targets(cls, v: dict[str, str]) -> dict[str, str]:
        """Validate that each target URL uses http/https and points to localhost or openclaw"""
        allowed_hosts = ["localhost", "127.0.0.1", "openclaw"]

        for name, url in v.items():
            if not url.startswith(("http://", "https://")):
                raise ValueError(
                    f"Target '{name}' URL must start with http:// or https://"
                )

            parsed = urlparse(url)
            if parsed.hostname not in allowed_hosts:
                raise ValueError(
                    f"Target '{name}' URL host must be one of {allowed_hosts}, got: {parsed.hostname}"
                )

        return v


class ApprovalQueueConfig(BaseModel):
    """Approval queue configuration"""

    enabled: bool = True
    actions: list[str] = Field(default_factory=list)
    timeout_seconds: int = 3600  # 1 hour


class GatewayConfig(BaseModel):
    """Complete gateway configuration"""

    bind: str = "127.0.0.1"
    port: int = 8080
    auth_method: str = "shared_secret"
    auth_token: str = ""
    cors_origins: list[str] = Field(
        default_factory=lambda: [
            "http://localhost:8080",
            "http://localhost:18790",
            "http://127.0.0.1:8080",
            "http://127.0.0.1:18790",
        ]
    )
    ledger: LedgerConfig = Field(default_factory=LedgerConfig)
    router: RouterConfig = Field(default_factory=RouterConfig)
    pii: PIIConfig = Field(default_factory=PIIConfig)
    approval_queue: ApprovalQueueConfig = Field(default_factory=ApprovalQueueConfig)
    log_level: str = "INFO"
    ssh: SSHConfig = Field(default_factory=SSHConfig)


def _entity_type_mapping(yaml_type: str) -> str:
    """Map agentshroud.yaml entity names to Presidio/internal entity names"""
    mapping = {
        "SSN": "US_SSN",
        "CREDIT_CARD": "CREDIT_CARD",
        "PHONE_NUMBER": "PHONE_NUMBER",
        "EMAIL_ADDRESS": "EMAIL_ADDRESS",
        "STREET_ADDRESS": "LOCATION",
    }
    return mapping.get(yaml_type, yaml_type)


def load_config(config_path: Path | None = None) -> GatewayConfig:
    """Load and validate configuration from agentshroud.yaml

    Search order:
    1. Explicit path argument
    2. AGENTSHROUD_CONFIG environment variable
    3. ./agentshroud.yaml (relative to CWD)
    4. ../agentshroud.yaml (for when running from gateway/)

    If auth_token is empty, generates a cryptographically random 32-byte
    hex token and logs it to stdout (once) so the user can configure their
    shortcuts and browser extension.

    Args:
        config_path: Optional explicit path to config file

    Returns:
        GatewayConfig: Validated configuration

    Raises:
        FileNotFoundError: If no config file found
        ValueError: If YAML is malformed or missing required fields
    """
    import os

    # Determine config file path
    if config_path:
        path = config_path
    elif env_path := os.getenv("AGENTSHROUD_CONFIG"):
        path = Path(env_path)
    elif Path("agentshroud.yaml").exists():
        path = Path("agentshroud.yaml")
    elif Path("../agentshroud.yaml").exists():
        path = Path("../agentshroud.yaml")
    else:
        raise FileNotFoundError(
            "No agentshroud.yaml found. Searched: "
            "./agentshroud.yaml, ../agentshroud.yaml, $AGENTSHROUD_CONFIG"
        )

    logger.info(f"Loading configuration from {path.absolute()}")

    # Load YAML
    with open(path, "r") as f:
        raw_config = yaml.safe_load(f)

    if not isinstance(raw_config, dict):
        raise ValueError(f"Invalid YAML structure in {path}")

    # Extract sections
    security = raw_config.get("security", {})
    gateway = raw_config.get("gateway", {})

    # Map PII configuration
    pii_enabled = security.get("pii_redaction", True)
    pii_engine = security.get("pii_detection_engine", "presidio")
    redaction_rules = security.get("redaction_rules", [])

    # Filter to enabled entities and map names
    enabled_entities = [
        _entity_type_mapping(rule["type"])
        for rule in redaction_rules
        if rule.get("enabled", True)
    ]

    pii_config = PIIConfig(
        engine=pii_engine,
        entities=enabled_entities,
        enabled=pii_enabled,
    )

    # Map ledger configuration
    ledger_db = gateway.get("ledger_database", "sqlite:///data/ledger.db")
    # Strip sqlite:/// prefix if present
    if ledger_db.startswith("sqlite:///"):
        ledger_path = Path(ledger_db.replace("sqlite:///", ""))
    else:
        ledger_path = Path(ledger_db)

    ledger_config = LedgerConfig(
        backend="sqlite",
        path=ledger_path,
        retention_days=gateway.get("retention_days", 90),
    )

    # Map router configuration
    router_config = RouterConfig(
        enabled=gateway.get("router_enabled", True),
        default_target=gateway.get("default_agent", "general"),
        targets={},  # Future: parse from config if needed
    )

    # Map approval queue configuration
    approval_config = ApprovalQueueConfig(
        enabled=security.get("approval_queue", True),
        actions=security.get("require_approval_for", []),
        timeout_seconds=3600,  # Not in current YAML, using default
    )

    # Get or generate auth token
    # Priority: 1) Docker secret file, 2) YAML config, 3) generate random
    auth_token = ""
    secret_file = os.environ.get("GATEWAY_AUTH_TOKEN_FILE", "")
    if secret_file:
        try:
            with open(secret_file) as f:
                auth_token = f.read().strip()
            logger.info("Loaded auth_token from secret file.")
        except OSError as e:
            logger.warning(f"Could not read GATEWAY_AUTH_TOKEN_FILE ({secret_file}): {e}")
    if not auth_token:
        auth_token = gateway.get("auth_token", "")
    if not auth_token:
        auth_token = secrets.token_hex(32)
        logger.warning(
            "\n" + "=" * 80 + "\n"
            "No auth_token found in secret file or agentshroud.yaml. Generated new token:\n\n"
            f"    {auth_token}\n\n"
            "Set GATEWAY_AUTH_TOKEN_FILE env var or add auth_token to agentshroud.yaml.\n"
            + "=" * 80
        )

    # Build final config
    # Map SSH configuration — use Pydantic model parsing directly
    ssh_section = raw_config.get("ssh", {})
    ssh_config = SSHConfig(**ssh_section) if ssh_section else SSHConfig()

    config = GatewayConfig(
        bind=gateway.get("bind", "127.0.0.1"),
        port=gateway.get("port", 8080),
        auth_method=gateway.get("auth_method", "shared_secret"),
        auth_token=auth_token,
        ledger=ledger_config,
        router=router_config,
        pii=pii_config,
        approval_queue=approval_config,
        log_level=raw_config.get("logging", {}).get("level", "INFO"),
        ssh=ssh_config,
    )

    logger.info(
        f"Configuration loaded: bind={config.bind}:{config.port}, "
        f"PII engine={config.pii.engine}, "
        f"ledger={config.ledger.path}, "
        f"router_enabled={config.router.enabled}"
    )

    return config
