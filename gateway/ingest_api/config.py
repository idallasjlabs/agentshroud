# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Configuration loader for AgentShroud Gateway


Loads configuration from agentshroud.yaml and provides typed access via Pydantic models.
"""


import logging
import os
import secrets
from pathlib import Path
from typing import Optional
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
    min_confidence: float = 0.8


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
    db_path: str = ""  # Set dynamically in __init__ if empty


class ChannelsConfig(BaseModel):
    """Channel ownership configuration (P3: Telegram + email oversight, P5: iMessage)"""

    email_enabled: bool = True
    email_allowed_recipients: list[str] = Field(default_factory=list)
    email_rate_limit_per_hour: int = 10
    email_require_approval_for_new: bool = True
    telegram_enabled: bool = True
    imessage_enabled: bool = True
    imessage_allowed_recipients: list[str] = Field(default_factory=list)
    imessage_rate_limit_per_hour: int = 30
    imessage_require_approval_for_new: bool = True




class SecurityModuleConfig(BaseModel):
    """Security module configuration"""

    mode: str = "enforce"  # enforce, monitor
    action: Optional[str] = None  # For PII: redact, block


class SecurityConfig(BaseModel):
    """Complete security configuration"""

    pii_sanitizer: SecurityModuleConfig = Field(default_factory=lambda: SecurityModuleConfig(action="redact"))
    prompt_guard: SecurityModuleConfig = Field(default_factory=SecurityModuleConfig)
    egress_filter: SecurityModuleConfig = Field(default_factory=SecurityModuleConfig)
    mcp_proxy: SecurityModuleConfig = Field(default_factory=SecurityModuleConfig)


def get_module_mode(config: "GatewayConfig", module_name: str) -> str:
    """Return module mode, respecting the global permissive override."""
    import os
    
    # Check for global override
    permissive = os.getenv("AGENTSHROUD_MODE", "enforce") == "monitor"
    if permissive:
        return "monitor"
    
    # Get module-specific config
    module_config = getattr(config.security, module_name, None)
    if module_config:
        return module_config.mode
    
    # Default to enforce
    return "enforce"


def check_monitor_mode_warnings(config: "GatewayConfig", logger):
    """Log warnings for any core modules running in monitor mode."""
    core_modules = ["pii_sanitizer", "prompt_guard", "egress_filter", "mcp_proxy"]
    
    for module_name in core_modules:
        mode = get_module_mode(config, module_name)
        if mode == "monitor":
            logger.warning(
                f"SECURITY: Module {module_name} is in MONITOR mode. "
                f"Threats will be logged but NOT blocked. "
                f"Set mode: enforce or remove AGENTSHROUD_MODE=monitor for production."
            )
class ToolRiskPolicy(BaseModel):
    """Risk policy configuration for a tool tier"""
    require_approval: bool = False
    timeout_seconds: int = 300  # 5 minutes default
    timeout_action: str = "deny"  # deny or allow
    notify_channels: list[str] = Field(default_factory=lambda: ["websocket"])
    owner_bypass: bool = False


class ToolRiskConfig(BaseModel):
    """Tool risk tier configuration"""
    
    critical: ToolRiskPolicy = Field(default_factory=lambda: ToolRiskPolicy(
        require_approval=True,
        timeout_seconds=300,
        timeout_action="deny",
        notify_channels=["websocket", "telegram_admin"],
        owner_bypass=False
    ))
    
    high: ToolRiskPolicy = Field(default_factory=lambda: ToolRiskPolicy(
        require_approval=True, 
        timeout_seconds=300,
        timeout_action="deny",
        notify_channels=["websocket"],
        owner_bypass=True
    ))
    
    medium: ToolRiskPolicy = Field(default_factory=lambda: ToolRiskPolicy(
        require_approval=False,
        timeout_seconds=300,
        timeout_action="deny",
        notify_channels=["websocket"],
        owner_bypass=True
    ))
    
    low: ToolRiskPolicy = Field(default_factory=lambda: ToolRiskPolicy(
        require_approval=False,
        timeout_seconds=300,
        timeout_action="deny",
        notify_channels=["websocket"],
        owner_bypass=True
    ))
    
    # Tool classifications
    tool_classifications: dict[str, str] = Field(default_factory=lambda: {
        # Critical: irreversible external impact
        "exec": "critical",
        "cron": "critical", 
        "sessions_send": "critical",
        
        # High: sensitive resource access
        "nodes": "high",
        "browser": "high",
        "apply_patch": "high", 
        "subagents": "high",
        
        # Medium: read potentially sensitive data
        "grep": "medium",
        "find": "medium",
        "sessions_list": "medium",
        "sessions_history": "medium", 
        "session_status": "medium",
        
        # Low: safe read-only operations
        "ls": "low",
        "canvas": "low", 
        "process": "low",
    })
    
    # Global enforcement settings
    enforce_mode: bool = True
    monitor_only_mode: bool = False
    owner_user_id: str = ""  # Telegram user ID for owner bypass


class AuditExportConfig(BaseModel):
    """Configuration for compliance audit export functionality."""

    enabled: bool = True
    default_format: str = "json"
    cef_vendor: str = "AgentShroud"
    cef_product: str = "Gateway"
    cef_version: str = "0.7.0"
    include_hash_verification: bool = True
    db_path: str = ""  # Set dynamically if empty
    max_export_records: int = 10000

    def model_post_init(self, __context):
        if not self.db_path:
            import tempfile
            data_dir = Path(os.environ.get("AGENTSHROUD_DATA_DIR", tempfile.gettempdir()))
            data_dir.mkdir(parents=True, exist_ok=True)
            self.db_path = str(data_dir / "agentshroud_audit.db")

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
    channels: ChannelsConfig = Field(default_factory=ChannelsConfig)
    ssh: SSHConfig = Field(default_factory=SSHConfig)
    # Domains permitted through the HTTP CONNECT proxy (proxy.allowed_domains in YAML)
    proxy_allowed_domains: list[str] = Field(default_factory=list)
    # Raw mcp_proxy section from YAML — passed to MCPProxyConfig.from_dict() at startup
    mcp_proxy_data: dict = Field(default_factory=dict)
    # Security modules configuration
    security: SecurityConfig = Field(default_factory=SecurityConfig)
    # Tool result PII configuration
    tool_result_pii: dict = Field(default_factory=lambda: {"enabled": True, "tool_overrides": {"icloud": {"entities": ["US_SSN", "CREDIT_CARD", "PHONE_NUMBER", "EMAIL_ADDRESS", "LOCATION"], "min_confidence": 0.7}, "email": {"entities": ["US_SSN", "CREDIT_CARD", "PHONE_NUMBER", "EMAIL_ADDRESS"], "min_confidence": 0.7}, "contacts": {"entities": ["PHONE_NUMBER", "EMAIL_ADDRESS", "LOCATION"], "min_confidence": 0.8}, "web_search": {"entities": ["US_SSN", "CREDIT_CARD", "PHONE_NUMBER"], "min_confidence": 0.8}, "web_fetch": {"entities": ["US_SSN", "CREDIT_CARD", "PHONE_NUMBER", "EMAIL_ADDRESS"], "min_confidence": 0.8}, "browser": {"entities": ["US_SSN", "CREDIT_CARD"], "min_confidence": 0.9}}})
    # Tool risk tier configuration
    tool_risk: ToolRiskConfig = Field(default_factory=ToolRiskConfig)
    # Compliance audit export configuration
    audit_export: AuditExportConfig = Field(default_factory=AuditExportConfig)



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


def load_config(config_path: Optional[Path] = None) -> GatewayConfig:
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
    pii_min_confidence = security.get("pii_min_confidence", 0.8)
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
        min_confidence=pii_min_confidence,
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

    # Map channels configuration
    channels_raw = raw_config.get("channels", {})
    email_raw = channels_raw.get("email", {}) if isinstance(channels_raw, dict) else {}
    telegram_raw = channels_raw.get("telegram", {}) if isinstance(channels_raw, dict) else {}
    imessage_raw = channels_raw.get("imessage", {}) if isinstance(channels_raw, dict) else {}
    channels_config = ChannelsConfig(
        email_enabled=email_raw.get("enabled", True),
        email_allowed_recipients=email_raw.get("allowed_recipients", []),
        email_rate_limit_per_hour=email_raw.get("rate_limit_per_hour", 10),
        email_require_approval_for_new=email_raw.get("require_approval_for_new", True),
        telegram_enabled=telegram_raw.get("enabled", True),
        imessage_enabled=imessage_raw.get("enabled", True),
        imessage_allowed_recipients=imessage_raw.get("allowed_recipients", []),
        imessage_rate_limit_per_hour=imessage_raw.get("rate_limit_per_hour", 30),
        imessage_require_approval_for_new=imessage_raw.get("require_approval_for_new", True),
    )

    # Build final config
    # Map SSH configuration — use Pydantic model parsing directly
    ssh_section = raw_config.get("ssh", {})
    ssh_config = SSHConfig(**ssh_section) if ssh_section else SSHConfig()

    # HTTP CONNECT proxy domain allowlist (proxy.allowed_domains in YAML)
    proxy_section = raw_config.get("proxy", {})
    proxy_allowed_domains = proxy_section.get("allowed_domains", [])

    # MCP proxy config (raw dict — converted to MCPProxyConfig in main.py at startup)
    mcp_proxy_data = raw_config.get("mcp_proxy", {})

    
    # Map security configuration
    security_raw = raw_config.get("security_modules", {})
    security_config = SecurityConfig()
    
    # Override defaults with YAML values if present
    for module in ["pii_sanitizer", "prompt_guard", "egress_filter", "mcp_proxy"]:
        if module in security_raw:
            module_data = security_raw[module]
            if hasattr(security_config, module):
                current_config = getattr(security_config, module)
                if "mode" in module_data:
                    current_config.mode = module_data["mode"]
                if "action" in module_data:
                    current_config.action = module_data["action"]
    # Tool risk tier config
    tool_risk_section = raw_config.get("tool_risk", {})
    # Audit export configuration
    audit_export_section = raw_config.get("audit_export", {})
    audit_export_config = AuditExportConfig(**audit_export_section) if audit_export_section else AuditExportConfig()

    tool_risk_config = ToolRiskConfig(**tool_risk_section) if tool_risk_section else ToolRiskConfig()

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
        channels=channels_config,
        ssh=ssh_config,
        security=security_config,
        proxy_allowed_domains=proxy_allowed_domains,
        audit_export=audit_export_config,

        mcp_proxy_data=mcp_proxy_data,
        tool_risk=tool_risk_config,
    )

    logger.info(
        f"Configuration loaded: bind={config.bind}:{config.port}, "
        f"PII engine={config.pii.engine}, "
        f"ledger={config.ledger.path}, "
        f"router_enabled={config.router.enabled}"
    )

    return config


