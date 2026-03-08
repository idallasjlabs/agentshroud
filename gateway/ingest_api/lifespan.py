# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Application lifespan management for the AgentShroud Gateway"""

import logging
import time
import os
import subprocess
import threading
from contextlib import asynccontextmanager
from pathlib import Path
from typing import TYPE_CHECKING

from fastapi import FastAPI

from .config import load_config, get_module_mode, check_monitor_mode_warnings
from ..security.agent_isolation import AgentRegistry, ContainerConfig, IsolationVerifier
from .state import app_state
from .sanitizer import PIISanitizer
from .ledger import DataLedger
from .router import MultiAgentRouter
from ..approval_queue.enhanced_queue import EnhancedApprovalQueue
from ..security.prompt_guard import PromptGuard
from ..security.trust_manager import TrustManager, TrustLevel
from ..security.egress_filter import EgressFilter, EgressPolicy
from ..security.outbound_filter import OutboundInfoFilter
from .middleware import MiddlewareManager
from .event_bus import EventBus
from ..proxy.pipeline import SecurityPipeline
from gateway.security.session_manager import UserSessionManager
from ..proxy.mcp_proxy import MCPProxy
from ..proxy.mcp_config import MCPProxyConfig
from ..proxy.web_config import WebProxyConfig
from ..proxy.web_proxy import WebProxy
from ..proxy.http_proxy import ALLOWED_DOMAINS, HTTPConnectProxy
from ..proxy.dns_forwarder import start_dns_forwarder
from ..proxy.dns_blocklist import DNSBlocklist
from ..ssh_proxy.proxy import SSHProxy
from ..security.killswitch_monitor import KillSwitchMonitor
from ..web.dashboard_endpoints import install_log_handler

if TYPE_CHECKING:
    pass

logger = logging.getLogger(__name__)


def _read_secret(env_key: str) -> str:
    """Read secret from env var or _FILE variant (Docker secrets)."""
    value = os.environ.get(env_key, "")
    if not value:
        file_path = os.environ.get(f"{env_key}_FILE", "")
        if file_path:
            try:
                with open(file_path, "r") as f:
                    value = f.read().strip()
            except Exception as e:
                logger.warning("Failed to read %s from %s: %s", env_key, file_path, e)
    return value


@asynccontextmanager
async def lifespan(app: FastAPI):
    """FastAPI lifespan - startup and shutdown"""

    # === STARTUP ===
    # Make app_state accessible via request.app.state for route files
    app.state.app_state = app_state
    logger.info("=" * 80)
    logger.info("AgentShroud Gateway starting up...")

    # Authenticate with 1Password using personal credentials.
    # Service accounts require a Teams/Enterprise plan; personal/family accounts
    # use email + master password + secret key instead.
    _OP_SECRETS = "/run/secrets"
    _op_email_file = os.path.join(_OP_SECRETS, "1password_bot_email")
    _op_pass_file  = os.path.join(_OP_SECRETS, "1password_bot_master_password")
    _op_key_file   = os.path.join(_OP_SECRETS, "1password_bot_secret_key")

    def _op_authenticate() -> "str | None":
        """Sign in to 1Password with personal credentials; return session token or None."""
        try:
            email    = Path(_op_email_file).read_text().strip()
            password = Path(_op_pass_file).read_text().strip()
            key      = Path(_op_key_file).read_text().strip() if Path(_op_key_file).exists() else ""
        except OSError as e:
            logger.warning(f"1Password credentials not found: {e}")
            return None
        if not email or not password:
            return None

        # Tier 1: op account add --signin --raw (first boot / account not yet registered)
        if key:
            r = subprocess.run(
                ["op", "account", "add",
                 "--address", "my.1password.com",
                 "--email", email,
                 "--secret-key", key,
                 "--signin", "--raw"],
                input=password, capture_output=True, text=True, timeout=120,
            )
            if r.returncode == 0 and r.stdout.strip():
                return r.stdout.strip()

        # Tier 2: op signin --raw (account already registered on this host)
        r = subprocess.run(
            ["op", "signin", "--raw"],
            input=password, capture_output=True, text=True, timeout=60,
        )
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.strip()

        logger.warning(f"1Password sign-in failed: {r.stderr.strip()[:200]}")
        return None

    if Path(_op_email_file).exists() and Path(_op_email_file).stat().st_size > 0:
        def _prewarm_op():
            session = _op_authenticate()
            if session:
                os.environ["OP_SESSION"] = session
                logger.info("1Password authenticated (personal credentials)")
            else:
                logger.warning("1Password authentication failed — op-proxy will be unavailable")

        threading.Thread(target=_prewarm_op, daemon=True).start()
        logger.info("1Password sign-in started (background)")

    # Load configuration
    try:
        app_state.config = load_config()
        logger.info("Configuration loaded successfully")
        # Check for monitor mode warnings
        check_monitor_mode_warnings(app_state.config, logger)
    except Exception as e:
        logger.critical(f"Failed to load configuration: {e}")
        raise

    # Set log level from config
    logging.getLogger().setLevel(app_state.config.log_level)
    logger.info(f"CORS configured with origins: {app_state.config.cors_origins}")

    # Initialize PII sanitizer
    try:
        sanitizer_mode = get_module_mode(app_state.config, "pii_sanitizer")
        sanitizer_action = app_state.config.security.pii_sanitizer.action or "redact"
        app_state.sanitizer = PIISanitizer(app_state.config.pii, mode=sanitizer_mode, action=sanitizer_action)
        logger.info(
            f"PII sanitizer initialized (mode: {app_state.sanitizer.get_mode()}, action: {sanitizer_action})"
        )
    except Exception as e:
        logger.critical(f"Failed to initialize PII sanitizer: {e}")
        raise

    # Initialize data ledger
    try:
        app_state.ledger = DataLedger(app_state.config.ledger)
        await app_state.ledger.initialize()
        logger.info("Data ledger initialized")
    except Exception as e:
        logger.critical(f"Failed to initialize data ledger: {e}")
        raise

    # Initialize router
    try:
        app_state.router = MultiAgentRouter(app_state.config.router)
        app_state.router.register_bots(app_state.config.bots)
        logger.info("Multi-agent router initialized")
    except Exception as e:
        logger.critical(f"Failed to initialize router: {e}")
        raise

    # Initialize AgentRegistry — wire all bots from config
    try:
        app_state.agent_registry = AgentRegistry()
        for bot_id, bot in app_state.config.bots.items():
            container_cfg = ContainerConfig(
                agent_id=bot_id,
                container_name=f"agentshroud-{bot_id}",
                network=f"agentshroud-{bot_id}-net",
                volume=f"agentshroud-{bot_id}-workspace",
                image=f"agentshroud/{bot_id}:latest",
            )
            app_state.agent_registry.register(container_cfg)
            logger.info("AgentRegistry: registered bot '%s'", bot_id)
        # Verify shared-nothing isolation across all registered bots
        verifier = IsolationVerifier(app_state.agent_registry)
        checks = verifier.verify_shared_nothing()
        violations = [c for c in checks if c.issues]
        if violations:
            for v in violations:
                logger.warning("Isolation check violation for '%s': %s", v.agent_id, v.issues)
        else:
            logger.info("AgentRegistry: shared-nothing isolation verified (%d bot(s))", len(checks))
    except Exception as e:
        logger.error(f"Failed to initialize AgentRegistry: {e}")
        app_state.agent_registry = None

    # Initialize approval queue
    try:
        from ..security.rbac_config import RBACConfig
        from ..approval_queue.store import ApprovalStore
        import tempfile
        _data_dir = os.environ.get("AGENTSHROUD_DATA_DIR", tempfile.gettempdir())
        _approval_db = os.path.join(_data_dir, "agentshroud_approvals.db")
        store = ApprovalStore(_approval_db)
        _tg_token = _read_secret("TELEGRAM_BOT_TOKEN")
        app_state.approval_queue = EnhancedApprovalQueue(
            app_state.config.approval_queue,
            app_state.config.tool_risk,
            store,
            bot_token=_tg_token or None,
            admin_chat_id=RBACConfig().owner_user_id if _tg_token else None,
        )
        await app_state.approval_queue.initialize()
        logger.info(f"Enhanced approval queue initialized (enforce_mode={app_state.config.tool_risk.enforce_mode})")
    except Exception as e:
        logger.critical(f"Failed to initialize approval queue: {e}")
        raise

    # Initialize security components
    try:
        prompt_guard_mode = get_module_mode(app_state.config, "prompt_guard")
        # Set thresholds based on mode - in monitor mode, set very high threshold so nothing blocks
        block_threshold = 999.0 if prompt_guard_mode == "monitor" else 0.8
        warn_threshold = 999.0 if prompt_guard_mode == "monitor" else 0.4
        app_state.prompt_guard = PromptGuard(block_threshold=block_threshold, warn_threshold=warn_threshold)
        logger.info("PromptGuard initialized")
    except Exception as e:
        logger.critical(f"Failed to initialize PromptGuard: {e}")
        raise

    try:
        app_state.trust_manager = TrustManager()
        app_state.trust_manager.register_agent("default")
        # Elevate default agent to STANDARD so internal API calls work
        app_state.trust_manager._conn.execute(
            "UPDATE trust_scores SET score = 200, level = ? WHERE agent_id = ?",
            (int(TrustLevel.STANDARD), "default")
        )
        app_state.trust_manager._conn.commit()
        logger.info("TrustManager initialized")
    except Exception as e:
        logger.critical(f"Failed to initialize TrustManager: {e}")
        raise

    try:
        egress_mode = get_module_mode(app_state.config, "egress_filter")
        # Create default policy with required domains for AgentShroud operation
        from ..security.egress_filter import EgressPolicy
        default_policy = EgressPolicy(
            allowed_domains=[
                "api.anthropic.com",
                "api.openai.com",
                "imap.gmail.com",
                "smtp.gmail.com",
                "*.googleapis.com",
                "api.telegram.org"
            ] + app_state.config.proxy_allowed_domains,
            deny_all=(egress_mode == "enforce")
        )
        app_state.egress_filter = EgressFilter(default_policy=default_policy)
        logger.info(f"EgressFilter initialized (mode: {egress_mode}, deny_all: {default_policy.deny_all})")

        # Wire per-bot egress policies from BotConfig.egress_domains
        for bot_id, bot in app_state.config.bots.items():
            if bot.egress_domains:
                bot_policy = EgressPolicy(
                    allowed_domains=list(default_policy.allowed_domains) + bot.egress_domains,
                    deny_all=default_policy.deny_all,
                )
                app_state.egress_filter.set_agent_policy(bot_id, bot_policy)
                logger.info(
                    "EgressFilter: bot '%s' policy set (%d extra domains)",
                    bot_id, len(bot.egress_domains),
                )
    except Exception as e:
        logger.critical(f"Failed to initialize EgressFilter: {e}")
        raise

    # Wire EgressTelegramNotifier into EgressFilter
    try:
        from ..proxy.telegram_egress_notify import EgressTelegramNotifier
        _tg_token_egress = _read_secret("TELEGRAM_BOT_TOKEN")
        if _tg_token_egress:
            app_state.egress_notifier = EgressTelegramNotifier(
                bot_token=_tg_token_egress,
                owner_chat_id=RBACConfig().owner_user_id,
            )
            app_state.egress_filter.set_notifier(app_state.egress_notifier)
            logger.info("EgressTelegramNotifier wired")
        else:
            app_state.egress_notifier = None
            logger.warning("EgressTelegramNotifier skipped — TELEGRAM_BOT_TOKEN not set")
    except Exception as e:
        logger.error(f"EgressTelegramNotifier failed: {e}")
        app_state.egress_notifier = None

    # Initialize P1 middleware manager
    try:
        app_state.middleware_manager = MiddlewareManager()
        logger.info("P1 MiddlewareManager initialized")
    except Exception as e:
        logger.critical(f"Failed to initialize MiddlewareManager: {e}")
        raise

    # Configure middleware with tool result PII scanning
    try:
        app_state.middleware_manager.set_config(app_state.config)
        logger.info("Middleware configured with tool result PII scanning")
    except Exception as e:
        logger.error(f"Failed to configure middleware: {e}")
    # Wire log sanitizer into Python logging
    try:
        log_sanitizer = app_state.middleware_manager.get_log_sanitizer()
        if log_sanitizer:
            # Add the log sanitizer filter to all handlers
            for handler in logging.getLogger().handlers:
                handler.addFilter(log_sanitizer)
            logger.info("Log sanitizer wired into logging system")
        else:
            logger.warning("Log sanitizer not available - logging may contain sensitive data")
    except Exception as e:
        logger.warning(f"Failed to wire log sanitizer: {e}")


    # Initialize outbound information filter
    try:
        app_state.outbound_filter = OutboundInfoFilter(getattr(app_state.config, "outbound_filter", None))
        logger.info(f"Outbound information filter initialized (mode: {app_state.outbound_filter.mode})")
    except Exception as e:
        logger.critical(f"Failed to initialize outbound information filter: {e}")
        raise

    # Initialize AuditStore (prerequisite for Pipeline, EgressFilter, AuditExporter)
    try:
        from ..security.audit_store import AuditStore
        _audit_db = os.path.join(
            os.environ.get("AGENTSHROUD_DATA_DIR", "/app/data"), "audit.db"
        )
        app_state.audit_store = AuditStore(db_path=_audit_db)
        await app_state.audit_store.initialize()
        logger.info("AuditStore initialized (%s)", _audit_db)
    except Exception as e:
        logger.error("AuditStore failed: %s", e)
        app_state.audit_store = None

    # GAP-1: Wire audit_store into EgressFilter now that AuditStore is initialized
    if getattr(app_state, "egress_filter", None) and app_state.audit_store:
        app_state.egress_filter._audit_store = app_state.audit_store
        logger.info("EgressFilter: audit_store wired (egress events will persist)")

    # Initialize security pipeline — wire all available guards
    try:
        from ..security.canary_tripwire import CanaryTripwire
        from ..security.encoding_detector import EncodingDetector
        _canary_tripwire = CanaryTripwire()
        _encoding_detector = EncodingDetector()
    except Exception as e:
        logger.warning(f"Optional pipeline guards failed to load: {e}")
        _canary_tripwire = None
        _encoding_detector = None

    app_state.pipeline = SecurityPipeline(
        prompt_guard=app_state.prompt_guard,
        pii_sanitizer=app_state.sanitizer,
        trust_manager=app_state.trust_manager,
        egress_filter=app_state.egress_filter,
        approval_queue=app_state.approval_queue,
        outbound_filter=app_state.outbound_filter,
        context_guard=app_state.middleware_manager.context_guard if app_state.middleware_manager else None,
        canary_tripwire=_canary_tripwire,
        encoding_detector=_encoding_detector,
        output_canary=app_state.middleware_manager.get_output_canary() if app_state.middleware_manager else None,
        enhanced_tool_sanitizer=app_state.middleware_manager.get_enhanced_tool_sanitizer() if app_state.middleware_manager else None,
        audit_store=app_state.audit_store,
    )
    logger.info("Security pipeline initialized")

    # Initialize per-user session manager for session isolation
    try:
        # Resolve workspace path from the default bot config.
        _bots = getattr(app_state.config, "bots", {})
        _default_bot = next(
            (b for b in _bots.values() if b.default),
            next(iter(_bots.values()), None),
        )
        _workspace_path = (
            _default_bot.workspace_path if _default_bot else "/app/workspace"
        )
        base_workspace = Path("/app/data/sessions")
        from gateway.security.rbac_config import RBACConfig as _RBACConfig
        _rbac = _RBACConfig()
        owner_user_id = _rbac.owner_user_id
        app_state.session_manager = UserSessionManager(
            base_workspace=base_workspace,
            owner_user_id=owner_user_id
        )
        logger.info("UserSessionManager initialized (workspace: /app/data/sessions)")
    except Exception as e:
        logger.error(f"Failed to initialize UserSessionManager: {e}")
        app_state.session_manager = None
        _rbac = None

    # Initialize gateway-level collaborator activity tracker
    try:
        from ..security.collaborator_tracker import CollaboratorActivityTracker
        from gateway.security.rbac_config import RBACConfig as _RBACCfg
        _rbac_cfg = _RBACCfg()
        app_state.collaborator_tracker = CollaboratorActivityTracker(
            log_path=Path("/app/data/collaborator_activity.jsonl"),
            owner_user_id=_rbac_cfg.owner_user_id,
            collaborator_ids=_rbac_cfg.collaborator_user_ids,
        )
        logger.info("CollaboratorActivityTracker initialized")
    except Exception as e:
        logger.error(f"Failed to initialize CollaboratorActivityTracker: {e}")
        app_state.collaborator_tracker = None

    # ══════════════════════════════════════════════════════════════════
    # P3 — Background & Infrastructure Security Modules
    # All modules fully configured with real binaries and data paths.
    # ══════════════════════════════════════════════════════════════════
    import shutil
    from pathlib import Path as _Path

    # Create required directories (tmpfs in containers, /tmp fallback in tests)
    _security_dirs = [
        "/tmp/security/alerts", "/tmp/security/clamav",
        "/tmp/security/trivy", "/tmp/security/falco",
        "/tmp/security/wazuh", "/tmp/security/canary",
        "/tmp/security/drift",
    ]
    for _d in _security_dirs:
        try:
            _Path(_d).mkdir(parents=True, exist_ok=True)
        except OSError:
            pass

    # Data directories — /app/data in container, /tmp/agentshroud-data in tests
    _data_dir = _Path("/app/data")
    try:
        _data_dir.mkdir(parents=True, exist_ok=True)
    except OSError:
        _data_dir = _Path("/tmp/agentshroud-data")
        _data_dir.mkdir(parents=True, exist_ok=True)
    (_data_dir / "baselines").mkdir(parents=True, exist_ok=True)

    # -- AlertDispatcher: routes security findings to logging --
    try:
        from ..security.alert_dispatcher import AlertDispatcher
        app_state.alert_dispatcher = AlertDispatcher(
            alert_log=_Path("/tmp/security/alerts/alerts.jsonl")
        )
        logger.info("✓ AlertDispatcher → /tmp/security/alerts/alerts.jsonl")
    except Exception as e:
        logger.error(f"✗ AlertDispatcher: {e}")
        app_state.alert_dispatcher = None

    # -- KillSwitchMonitor: automated kill switch verification and heartbeat monitoring --
    try:
        app_state.killswitch_monitor = KillSwitchMonitor(
            alert_dispatcher=app_state.alert_dispatcher
        )
        logger.info("✓ KillSwitchMonitor → kill switch verification and anomaly detection enabled")
    except Exception as e:
        logger.error(f"✗ KillSwitchMonitor: {e}")
        app_state.killswitch_monitor = None

    # -- DriftDetector: detects config changes from baseline --
    try:
        from ..security.drift_detector import DriftDetector
        app_state.drift_detector = DriftDetector(
            db_path=str(_data_dir / "drift.db"),
        )
        logger.info("✓ DriftDetector → %s/drift.db", _data_dir)
    except Exception as e:
        logger.error(f"✗ DriftDetector: {e}")
        app_state.drift_detector = None

    # -- HealthReport: aggregates security posture from all modules --
    try:
        from ..security import health_report as _health_mod
        app_state.health_report = _health_mod
        logger.info("✓ HealthReport module loaded")
    except Exception as e:
        logger.error(f"✗ HealthReport: {e}")
        app_state.health_report = None

    # -- EncryptedStore: AES-256-GCM encryption for ledger entries --
    try:
        from ..security.encrypted_store import EncryptedStore
        _master = (
            os.getenv("AGENTSHROUD_GATEWAY_PASSWORD", "")
            or os.getenv("OPENCLAW_GATEWAY_PASSWORD", "")
            or os.getenv("GATEWAY_AUTH_TOKEN", "")
        )
        if not _master:
            try:
                _master = open("/run/secrets/gateway_password").read().strip()
            except OSError:
                pass
        if _master:
            app_state.encrypted_store = EncryptedStore(master_secret=_master)
            logger.info("✓ EncryptedStore (AES-256-GCM)")
        else:
            app_state.encrypted_store = None
            logger.warning("✗ EncryptedStore: no master secret")
    except Exception as e:
        logger.error(f"✗ EncryptedStore: {e}")
        app_state.encrypted_store = None

    # KeyVault removed — was instantiated but never wired to any consumer.
    # Re-add when a consumer (e.g. credential injector) needs it.

    # -- Canary: integrity checks on critical files --
    try:
        from ..security.canary import run_canary
        app_state.canary_runner = run_canary
        app_state.canary_targets = [
            "/app/agentshroud.yaml",
            "/usr/local/bin/trivy",
            "/run/secrets/gateway_password",
        ]
        logger.info("✓ Canary (3 integrity targets registered)")
    except Exception as e:
        logger.error(f"✗ Canary: {e}")
        app_state.canary_runner = None

    # -- ClamAV: antivirus file scanning --
    try:
        from ..security import clamav_scanner as _clamav_mod
        _clam_bin = shutil.which("clamscan")
        app_state.clamav_scanner = _clamav_mod
        if _clam_bin:
            logger.info("✓ ClamAV scanner (%s)", _clam_bin)
        else:
            logger.warning("⚠ ClamAV module loaded but clamscan not in PATH")
    except Exception as e:
        logger.error(f"✗ ClamAV: {e}")
        app_state.clamav_scanner = None

    # -- Trivy: container/image vulnerability scanning --
    try:
        from ..security import trivy_report as _trivy_mod
        _trivy_bin = shutil.which("trivy")
        app_state.trivy_scanner = _trivy_mod
        if _trivy_bin:
            logger.info("✓ Trivy scanner (%s)", _trivy_bin)
        else:
            logger.warning("⚠ Trivy module loaded but trivy not in PATH")
    except Exception as e:
        logger.error(f"✗ Trivy: {e}")
        app_state.trivy_scanner = None

    # -- Falco: runtime security monitoring (reads JSON alert files) --
    try:
        from ..security import falco_monitor as _falco_mod
        app_state.falco_monitor = _falco_mod
        # Register bot names as Falco rule prefixes so bot-specific rules are captured
        _bot_names = [b.name for b in app_state.config.bots.values() if b.name]
        _falco_mod.configure_rules(_bot_names)
        logger.info("✓ Falco monitor (alerts: /tmp/security/falco, bots: %s)", _bot_names)
    except Exception as e:
        logger.error(f"✗ Falco monitor: {e}")
        app_state.falco_monitor = None

    # -- Wazuh: host intrusion detection (reads alert files) --
    try:
        from ..security import wazuh_client as _wazuh_mod
        app_state.wazuh_client = _wazuh_mod
        logger.info("✓ Wazuh client (alerts: /tmp/security/wazuh)")
    except Exception as e:
        logger.error(f"✗ Wazuh client: {e}")
        app_state.wazuh_client = None

    # -- NetworkValidator: Docker/container network security --
    try:
        from ..security.network_validator import NetworkValidator
        app_state.network_validator = NetworkValidator()
        logger.info("✓ NetworkValidator")
    except Exception as e:
        logger.info("✓ NetworkValidator (static mode — Docker socket not available)")
        app_state.network_validator = None

    # Initialize MCP proxy — load server registry from agentshroud.yaml mcp_proxy section
    mcp_mode = get_module_mode(app_state.config, "mcp_proxy")
    mcp_proxy_config = (
        MCPProxyConfig.from_dict(app_state.config.mcp_proxy_data)
        if app_state.config.mcp_proxy_data
        else MCPProxyConfig()
    )
    # In enforce mode, enable all security scanning
    if mcp_mode == "enforce":
        mcp_proxy_config.pii_scan_enabled = True
        mcp_proxy_config.injection_scan_enabled = True
        mcp_proxy_config.audit_enabled = True
    app_state.mcp_proxy = MCPProxy(config=mcp_proxy_config, approval_queue=app_state.approval_queue)
    logger.info(
        f"MCP proxy initialized (mode: {mcp_mode}): {len(mcp_proxy_config.servers)} server(s) registered"
    )

    # Initialize SSH proxy
    if app_state.config.ssh.enabled:
        app_state.ssh_proxy = SSHProxy(app_state.config.ssh)
        logger.info("SSH proxy initialized")
    else:
        app_state.ssh_proxy = None

    # Initialize event bus
    app_state.event_bus = EventBus()
    logger.info("Event bus initialized")

    # Initialize HTTP CONNECT proxy (port 8181)
    # Activated in the FINAL PR by setting HTTP_PROXY on the bot container.
    # Running it now adds zero risk — the bot doesn't use it until then.
    try:
        # Use allowed_domains from agentshroud.yaml (proxy.allowed_domains),
        # falling back to the hardcoded default if the YAML section is absent.
        _proxy_domains = app_state.config.proxy_allowed_domains or ALLOWED_DOMAINS
        _web_proxy = WebProxy(config=WebProxyConfig(mode="allowlist", allowed_domains=_proxy_domains))
        app_state.http_proxy = HTTPConnectProxy(web_proxy=_web_proxy)
        await app_state.http_proxy.start()
        logger.info("HTTP CONNECT proxy started on port 8181")
    except Exception as e:
        logger.warning(f"HTTP CONNECT proxy failed to start: {e} (continuing)")
        app_state.http_proxy = None

    # Start DNS forwarder with Pi-hole-style blocklist filtering
    # Replaces the separate Pi-hole container — all DNS filtering in gateway.
    try:
        # Initialize blocklist (downloads adlists on first run)
        app_state.dns_blocklist = DNSBlocklist()
        await app_state.dns_blocklist.update()
        await app_state.dns_blocklist.start_periodic_updates()
        logger.info(
            f"DNS blocklist loaded: {len(app_state.dns_blocklist.blocked_domains)} blocked domains"
        )

        app_state.dns_transport = await start_dns_forwarder(
            host="0.0.0.0", port=5353, blocklist=app_state.dns_blocklist
        )
        logger.info("DNS forwarder started on port 5353 (with blocklist filtering)")
    except Exception as e:
        logger.warning(f"DNS forwarder failed to start: {e} (continuing)")
        app_state.dns_transport = None

    # Record start time
    app_state.start_time = time.time()

    install_log_handler()
    logger.info(
        f"AgentShroud Gateway ready at {app_state.config.bind}:{app_state.config.port}"
    )
    logger.info("=" * 80)

    yield

    # === SHUTDOWN ===
    logger.info("AgentShroud Gateway shutting down...")

    # Stop HTTP CONNECT proxy
    if getattr(app_state, "http_proxy", None):
        await app_state.http_proxy.stop()

    # Close ledger

    # Close approval queue
    if hasattr(app_state, "approval_queue") and app_state.approval_queue:
        await app_state.approval_queue.close()
        logger.info("Approval queue closed")

    # GAP-2: Close AuditStore to flush WAL before exit
    if getattr(app_state, "audit_store", None):
        await app_state.audit_store.close()
        logger.info("AuditStore closed")

    # GAP-6: Cancel DNSBlocklist periodic update task
    if getattr(app_state, "dns_blocklist", None):
        app_state.dns_blocklist.stop()
        logger.info("DNSBlocklist periodic updates stopped")

    await app_state.ledger.close()

    logger.info("Shutdown complete")


