# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""SSH configuration models for AgentShroud Gateway"""


import os

from pydantic import BaseModel, Field, field_validator


class SSHHostConfig(BaseModel):
    """Configuration for a single SSH host"""

    host: str
    port: int = 22
    username: str = "root"
    key_path: str = ""
    known_hosts_file: str = Field(
        default="~/.ssh/known_hosts",
        description="Path to known_hosts file for host key verification",
    )
    allowed_commands: list[str] = Field(default_factory=list)
    denied_commands: list[str] = Field(default_factory=list)
    max_session_seconds: int = 60
    auto_approve_commands: list[str] = Field(default_factory=list)

    @field_validator("key_path", mode="after")
    @classmethod
    def expand_key_path(cls, v: str) -> str:
        return os.path.expanduser(v) if v else v

    @field_validator("known_hosts_file", mode="after")
    @classmethod
    def expand_known_hosts(cls, v: str) -> str:
        return os.path.expanduser(v) if v else v


class SSHConfig(BaseModel):
    """Top-level SSH proxy configuration"""

    enabled: bool = False
    hosts: dict[str, SSHHostConfig] = Field(default_factory=dict)
    global_denied_commands: list[str] = Field(default_factory=list)
    require_approval: bool = True
