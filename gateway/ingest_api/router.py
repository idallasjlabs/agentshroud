# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Multi-Agent Router for AgentShroud Gateway

Routes sanitized content to registered bot containers.
Handles graceful degradation when agents are offline.
"""


import logging
from datetime import datetime
from typing import Any

import httpx

from .config import RouterConfig
from .models import AgentTarget, ForwardRequest

logger = logging.getLogger("agentshroud.gateway.router")


class RouterError(Exception):
    """Raised when no valid routing target found"""

    pass


class ForwardError(Exception):
    """Raised when forwarding to agent fails"""

    pass


class MultiAgentRouter:
    """Routes content to appropriate agent containers

    Routing priority:
    1. Explicit route_to field in request
    2. Metadata tags matching agent tags
    3. Content type matching
    4. Default target from configuration
    """

    def __init__(self, config: RouterConfig):
        """Initialize router

        Args:
            config: Router configuration
        """
        self.config = config
        self.targets: dict[str, AgentTarget] = {}

        # Create default target from RouterConfig (URL computed from default BotConfig)
        self.targets[config.default_target] = AgentTarget(
            name=config.default_target,
            url=config.default_url,
            content_types=["text", "url", "photo", "file"],
            tags=[],
        )

        # Add any additional configured targets
        for name, url in config.targets.items():
            if name not in self.targets:
                self.targets[name] = AgentTarget(
                    name=name, url=url, content_types=[], tags=[]
                )

        logger.info(f"Router initialized with {len(self.targets)} target(s)")

    def register_bots(self, bots: dict) -> None:
        """Populate routing targets from the bots registry.

        Iterates all BotConfig entries and registers each as a named
        AgentTarget so they can be addressed by bot_id in forward requests.
        The default bot's target is already registered in __init__; this
        method adds the remaining bots and updates the default target URL
        to match the BotConfig-computed base_url.

        Args:
            bots: Mapping of bot_id → BotConfig from GatewayConfig.bots.
        """
        for bot_id, bot in bots.items():
            target = AgentTarget(
                name=bot_id,
                url=bot.base_url,
                content_types=["text", "url", "photo", "file"],
                tags=[],
                chat_path=bot.chat_path,
                health_path=bot.health_path,
            )
            self.targets[bot_id] = target
            logger.info("Router: registered bot target '%s' → %s", bot_id, bot.base_url)

        logger.info("Router: %d bot target(s) registered", len(self.targets))

    async def resolve_target(self, request: ForwardRequest) -> AgentTarget:
        """Determine which agent should receive this content

        Args:
            request: Forward request with routing hints

        Returns:
            AgentTarget to forward to

        Raises:
            RouterError: If no valid target found
        """
        # Priority 1: Explicit route_to
        if request.route_to:
            if request.route_to in self.targets:
                logger.debug(f"Explicit routing to {request.route_to}")
                return self.targets[request.route_to]
            else:
                logger.warning(
                    f"Explicit route_to '{request.route_to}' not found, "
                    "falling back to default"
                )

        # Priority 2: Metadata tags (future enhancement)
        # For now, skip to default

        # Priority 3: Content type matching (future enhancement)
        # For now, skip to default

        # Priority 4: Default target
        default_target = self.targets.get(self.config.default_target)
        if not default_target:
            raise RouterError(
                f"Default target '{self.config.default_target}' not found"
            )

        logger.debug(f"Routing to default target: {self.config.default_target}")
        return default_target

    async def forward_to_agent(
        self,
        target: AgentTarget,
        sanitized_content: str,
        ledger_id: str,
        metadata: dict[str, Any],
    ) -> dict:
        """Forward sanitized content to agent via HTTP POST

        Args:
            target: Agent target to forward to
            sanitized_content: PII-redacted content
            ledger_id: Ledger entry UUID for tracing
            metadata: Original request metadata

        Returns:
            Agent's response as dict

        Raises:
            ForwardError: If forwarding fails
        """
        payload = {
            "content": sanitized_content,
            "ledger_id": ledger_id,
            "source": metadata.get("source", "unknown"),
            "content_type": metadata.get("content_type", "text"),
            "metadata": metadata,
        }

        logger.info(
            f"Forwarding to {target.name} at {target.url} (ledger_id={ledger_id})"
        )

        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(
                    f"{target.url}{target.chat_path}",
                    json=payload,
                )
                response.raise_for_status()

                logger.info(
                    f"Successfully forwarded to {target.name} "
                    f"(status={response.status_code})"
                )

                return response.json()

        except httpx.ConnectError as e:
            # Agent is offline - this is expected in Phase 2
            logger.warning(
                f"Agent {target.name} offline at {target.url}: {e}. "
                "Content logged but not forwarded."
            )
            raise ForwardError(
                f"Agent {target.name} offline. Content saved to ledger."
            ) from e

        except httpx.TimeoutException as e:
            logger.error(f"Timeout forwarding to {target.name}: {e}")
            raise ForwardError(f"Timeout contacting agent {target.name}") from e

        except httpx.HTTPStatusError as e:
            logger.error(
                f"HTTP error forwarding to {target.name}: "
                f"{e.response.status_code} - {e.response.text}"
            )
            raise ForwardError(
                f"Agent {target.name} returned error: {e.response.status_code}"
            ) from e

        except Exception as e:
            logger.error(f"Unexpected error forwarding to {target.name}: {e}")
            raise ForwardError(f"Failed to forward to {target.name}") from e

    async def health_check(self, target: AgentTarget | None = None) -> dict[str, Any]:
        """Check health of one or all agent targets

        Args:
            target: Specific target to check, or None to check all

        Returns:
            Dictionary with health status
        """
        targets_to_check = [target] if target else list(self.targets.values())
        results = {}

        for t in targets_to_check:
            try:
                async with httpx.AsyncClient(timeout=5.0) as client:
                    from datetime import timezone

                    response = await client.get(f"{t.url}{t.health_path}")
                    t.healthy = response.status_code == 200
                    t.last_health_check = (
                        datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
                    )

                    results[t.name] = {
                        "healthy": t.healthy,
                        "status_code": response.status_code,
                        "last_check": t.last_health_check,
                    }

            except Exception as e:
                from datetime import timezone

                t.healthy = False
                t.last_health_check = (
                    datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
                )

                results[t.name] = {
                    "healthy": False,
                    "error": type(e).__name__,
                    "last_check": t.last_health_check,
                }

        return results

    def list_targets(self) -> list[AgentTarget]:
        """Return all configured agent targets

        Returns:
            List of AgentTarget objects
        """
        return list(self.targets.values())
