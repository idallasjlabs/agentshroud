# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""BotConfig — per-bot protocol and container specification.

Defines the minimal contract any bot must implement to be encapsulated by
AgentShroud. Gateway code resolves all bot-specific values (hostnames,
ports, workspace paths, etc.) from this config rather than from hardcoded
OpenClaw-specific constants.
"""

from typing import Optional

from pydantic import BaseModel, Field


class BotConfig(BaseModel):
    """Declaration for a single bot encapsulated by AgentShroud.

    Required bot HTTP endpoints (must be implemented by every encapsulated bot):
      GET  {health_path}   — liveness probe; must return 200 {"status": "ok"}
      POST {chat_path}     — receive forwarded messages from the gateway
      POST {webhook_path}  — receive sanitized Telegram/channel webhooks

    Required env vars set by AgentShroud on the bot container:
      ANTHROPIC_BASE_URL          — LLM proxy (http://gateway:8080)
      HTTP_PROXY / HTTPS_PROXY    — egress proxy (http://gateway:8181)
      AGENTSHROUD_GATEWAY_PASSWORD — gateway auth token
      AGENTSHROUD_BOT_ID          — this bot's unique identifier
      AGENTSHROUD_WORKSPACE       — workspace directory inside the container
    """

    id: str = Field(..., description="Unique bot identifier, e.g. 'openclaw'")
    name: str = Field(..., description="Human-readable name, e.g. 'OpenClaw'")
    runtime: str = Field(default="node", description="Container runtime: node, python")
    hostname: str = Field(..., description="Docker service hostname on the isolated network")
    port: int = Field(..., description="Bot HTTP port inside the container")
    health_path: str = Field(default="/health", description="Health check endpoint path")
    chat_path: str = Field(default="/chat", description="Chat forwarding endpoint path")
    webhook_path: str = Field(default="/webhook", description="Webhook forwarding endpoint path")
    workspace_path: str = Field(..., description="Workspace directory inside the container")
    config_dir: str = Field(..., description="Bot config directory inside the container")
    dockerfile: str = Field(default="", description="Relative path to the bot Dockerfile")
    env_prefix: str = Field(
        default="", description="Env var prefix for bot-specific vars, e.g. 'OPENCLAW_'"
    )
    egress_domains: list[str] = Field(
        default_factory=list,
        description="Additional egress domains this bot requires beyond the global allowlist",
    )
    default: bool = Field(default=False, description="Whether this is the default bot for routing")

    @property
    def base_url(self) -> str:
        """Compute the bot's internal base URL from hostname and port."""
        return f"http://{self.hostname}:{self.port}"
