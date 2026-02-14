"""Configuration loader for SecureClaw Gateway

Loads configuration from secureclaw.yaml and provides typed access via Pydantic models.
"""

import logging
import secrets
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings

logger = logging.getLogger("secureclaw.gateway.config")


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
    targets: dict[str, str] = Field(default_factory=dict)


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
    ledger: LedgerConfig = Field(default_factory=LedgerConfig)
    router: RouterConfig = Field(default_factory=RouterConfig)
    pii: PIIConfig = Field(default_factory=PIIConfig)
    approval_queue: ApprovalQueueConfig = Field(default_factory=ApprovalQueueConfig)
    log_level: str = "INFO"


def _entity_type_mapping(yaml_type: str) -> str:
    """Map secureclaw.yaml entity names to Presidio/internal entity names"""
    mapping = {
        "SSN": "US_SSN",
        "CREDIT_CARD": "CREDIT_CARD",
        "PHONE_NUMBER": "PHONE_NUMBER",
        "EMAIL_ADDRESS": "EMAIL_ADDRESS",
        "STREET_ADDRESS": "LOCATION",
    }
    return mapping.get(yaml_type, yaml_type)


def load_config(config_path: Path | None = None) -> GatewayConfig:
    """Load and validate configuration from secureclaw.yaml

    Search order:
    1. Explicit path argument
    2. SECURECLAW_CONFIG environment variable
    3. ./secureclaw.yaml (relative to CWD)
    4. ../secureclaw.yaml (for when running from gateway/)

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
    elif env_path := os.getenv("SECURECLAW_CONFIG"):
        path = Path(env_path)
    elif Path("secureclaw.yaml").exists():
        path = Path("secureclaw.yaml")
    elif Path("../secureclaw.yaml").exists():
        path = Path("../secureclaw.yaml")
    else:
        raise FileNotFoundError(
            "No secureclaw.yaml found. Searched: "
            "./secureclaw.yaml, ../secureclaw.yaml, $SECURECLAW_CONFIG"
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
    auth_token = gateway.get("auth_token", "")
    if not auth_token:
        auth_token = secrets.token_hex(32)
        logger.warning(
            "\n" + "=" * 80 + "\n"
            "No auth_token found in secureclaw.yaml. Generated new token:\n\n"
            f"    {auth_token}\n\n"
            "Add this to secureclaw.yaml under gateway.auth_token or use it for this session.\n"
            "Save this token for your iOS Shortcuts and browser extension.\n"
            + "=" * 80
        )

    # Build final config
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
    )

    logger.info(
        f"Configuration loaded: bind={config.bind}:{config.port}, "
        f"PII engine={config.pii.engine}, "
        f"ledger={config.ledger.path}, "
        f"router_enabled={config.router.enabled}"
    )

    return config
