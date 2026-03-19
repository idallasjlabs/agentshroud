# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Application state container for the AgentShroud Gateway"""

from typing import Optional

from ..approval_queue.enhanced_queue import EnhancedApprovalQueue
from .config import GatewayConfig
from .event_bus import EventBus
from .ledger import DataLedger
from .router import MultiAgentRouter
from .sanitizer import PIISanitizer
from ..proxy.http_proxy import HTTPConnectProxy
from ..proxy.mcp_proxy import MCPProxy
from ..proxy.pipeline import SecurityPipeline
from ..security.egress_filter import EgressFilter
from ..security.prompt_guard import PromptGuard
from ..security.trust_manager import TrustManager
from gateway.security.session_manager import UserSessionManager


class AppState:
    """Container for application-wide state"""

    config: GatewayConfig
    sanitizer: PIISanitizer
    ledger: DataLedger
    router: MultiAgentRouter
    approval_queue: EnhancedApprovalQueue
    prompt_guard: PromptGuard
    trust_manager: TrustManager
    egress_filter: EgressFilter
    mcp_proxy: Optional[MCPProxy]
    pipeline: Optional[SecurityPipeline]
    session_manager: Optional[UserSessionManager]
    start_time: float
    event_bus: EventBus
    http_proxy: Optional[HTTPConnectProxy]
    llm_proxy: Optional[object]
    prompt_protection: Optional[object]
    heuristic_classifier: Optional[object]
    memory_integrity: Optional[object]
    memory_lifecycle: Optional[object]


# Global application state instance
app_state = AppState()
