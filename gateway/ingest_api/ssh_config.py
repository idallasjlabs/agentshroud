"""SSH configuration models for SecureClaw Gateway"""

from pydantic import BaseModel, Field


class SSHHostConfig(BaseModel):
    """Configuration for a single SSH host"""
    host: str
    port: int = 22
    username: str = "root"
    key_path: str = ""
    allowed_commands: list[str] = Field(default_factory=list)
    denied_commands: list[str] = Field(default_factory=list)
    max_session_seconds: int = 60
    auto_approve_commands: list[str] = Field(default_factory=list)


class SSHConfig(BaseModel):
    """Top-level SSH proxy configuration"""
    enabled: bool = False
    hosts: dict[str, SSHHostConfig] = Field(default_factory=dict)
    global_denied_commands: list[str] = Field(default_factory=list)
    require_approval: bool = True
