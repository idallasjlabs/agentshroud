# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Vendor policy profiles for the Inbound MCP Edge (SCRUM-209).

One YAML file per hosted agent under ``config/inbound-edge/vendors/``. Each file is
validated against ``config/inbound-edge/schema.json`` and then against rules a
schema cannot express (tool names and access classes must match the signed
descriptors, the DLP threshold may only rise above the global floor, monitor mode
needs an explicit acknowledgement). Any error stops startup — there is no
"load what parses" mode, because a half-loaded policy is a default-allow policy.

IEC 62443 alignment: FR2 (Use Control) — per-principal authorisation of tools.
"""

import ipaddress
import json
import logging
from dataclasses import dataclass, field
from datetime import time
from pathlib import Path
from typing import Dict, Optional, Tuple
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

import jsonschema
import yaml

from gateway.inbound_edge.descriptors import CONFIG_DIR, TOOL_DESCRIPTORS
from gateway.ingest_api.config import PIIConfig

logger = logging.getLogger("agentshroud.inbound_edge.profiles")

VENDORS_DIR = CONFIG_DIR / "vendors"
SCHEMA_PATH = CONFIG_DIR / "schema.json"
# The gateway-wide Presidio floor (CLAUDE.md §7.8). Profiles may raise it, never lower it.
GLOBAL_DLP_FLOOR = PIIConfig().min_confidence


class ProfileError(ValueError):
    """A vendor profile is invalid. The edge must not start."""


@dataclass(frozen=True)
class VendorProfile:
    vendor: str
    display_name: str
    enabled: bool
    mode: str
    oauth: bool
    dynamic_registration: bool
    redirect_uris: Tuple[str, ...]
    static_bearer: bool
    tools: Dict[str, str]
    per_client_per_minute: int
    per_vendor_per_minute: int
    max_concurrency: int
    daily_calls: int
    daily_delegations: int
    dlp_mode: str
    dlp_min_confidence: float
    max_response_bytes: int
    source_networks: Tuple[ipaddress._BaseNetwork, ...] = field(default=())
    allowed_hours: Optional[Tuple[time, time, ZoneInfo]] = None

    def tool_access(self, tool: str) -> Optional[str]:
        """``"read"``/``"write"`` when the vendor may call ``tool``, else ``None``."""
        return self.tools.get(tool)

    @property
    def enforcing(self) -> bool:
        return self.mode == "enforce"


def _schema_validator() -> jsonschema.Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text())
    jsonschema.Draft202012Validator.check_schema(schema)
    return jsonschema.Draft202012Validator(schema)


def _parse(path: Path, data: object, validator: jsonschema.Draft202012Validator) -> VendorProfile:
    errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
    if errors:
        first = errors[0]
        where = "/".join(str(p) for p in first.path) or "<root>"
        raise ProfileError(f"{path.name}: {where}: {first.message}")
    assert isinstance(data, dict)  # guaranteed by the schema's top-level type

    vendor = data["vendor"]
    if path.stem != vendor:
        raise ProfileError(f"{path.name}: file name must match vendor {vendor!r}")

    for tool, access in data["tools"].items():
        desc = TOOL_DESCRIPTORS.get(tool)
        if desc is None:
            raise ProfileError(f"{vendor}: unknown tool {tool!r}")
        if access != desc["access"]:
            raise ProfileError(
                f"{vendor}: tool {tool!r} listed as {access!r} but declared {desc['access']}"
            )

    dlp = data["dlp"]
    if dlp["min_confidence"] < GLOBAL_DLP_FLOOR:
        raise ProfileError(
            f"{vendor}: dlp.min_confidence {dlp['min_confidence']} is below the global "
            f"floor {GLOBAL_DLP_FLOOR}"
        )

    if data["mode"] == "monitor" and not data.get("monitor_ack", False):
        raise ProfileError(f"{vendor}: mode monitor requires monitor_ack: true")

    auth = data["auth"]
    if auth["static_bearer"]:
        # STUB: static bearer fallback (FR2) — NOT PRODUCTION READY. Refuse rather
        # than accept a profile whose setting would silently do nothing.
        raise ProfileError(f"{vendor}: static_bearer is not implemented in this release")
    for uri in auth["redirect_uris"]:
        if not uri.startswith("https://"):
            raise ProfileError(f"{vendor}: redirect URI must be https: {uri}")

    networks = []
    for cidr in data.get("source_cidrs", []):
        try:
            networks.append(ipaddress.ip_network(cidr, strict=True))
        except ValueError as exc:
            raise ProfileError(f"{vendor}: bad source_cidrs entry {cidr!r}: {exc}") from exc

    hours = None
    if "allowed_hours" in data:
        spec = data["allowed_hours"]
        try:
            hours = (
                time.fromisoformat(spec["start"]),
                time.fromisoformat(spec["end"]),
                ZoneInfo(spec["tz"]),
            )
        except (ValueError, ZoneInfoNotFoundError) as exc:
            raise ProfileError(f"{vendor}: bad allowed_hours: {exc}") from exc

    limits = data["limits"]
    profile = VendorProfile(
        vendor=vendor,
        display_name=data["display_name"],
        enabled=data["enabled"],
        mode=data["mode"],
        oauth=auth["oauth"],
        dynamic_registration=auth["dynamic_registration"],
        redirect_uris=tuple(auth["redirect_uris"]),
        static_bearer=auth["static_bearer"],
        tools=dict(data["tools"]),
        per_client_per_minute=limits["per_client_per_minute"],
        per_vendor_per_minute=limits["per_vendor_per_minute"],
        max_concurrency=limits["max_concurrency"],
        daily_calls=limits["daily_calls"],
        daily_delegations=limits["daily_delegations"],
        dlp_mode=dlp["mode"],
        dlp_min_confidence=float(dlp["min_confidence"]),
        max_response_bytes=data["max_response_bytes"],
        source_networks=tuple(networks),
        allowed_hours=hours,
    )
    if profile.mode == "monitor":
        logger.warning(
            "INBOUND EDGE VENDOR %s IS IN MONITOR MODE — violations are logged, NOT blocked",
            vendor,
        )
    return profile


def load_profiles(directory: Path = VENDORS_DIR) -> Dict[str, VendorProfile]:
    """Load and validate every ``*.yaml``/``*.yml`` profile in ``directory``.

    Raises :class:`ProfileError` on the first problem; never returns a partial set.
    """
    if not directory.is_dir():
        raise ProfileError(f"vendor profile directory missing: {directory}")
    validator = _schema_validator()
    profiles: Dict[str, VendorProfile] = {}
    paths = sorted([*directory.glob("*.yaml"), *directory.glob("*.yml")])
    for path in paths:
        try:
            data = yaml.safe_load(path.read_text())
        except yaml.YAMLError as exc:
            raise ProfileError(f"{path.name}: unparseable YAML: {exc}") from exc
        profile = _parse(path, data, validator)
        if profile.vendor in profiles:
            raise ProfileError(f"duplicate profile for vendor {profile.vendor!r}")
        profiles[profile.vendor] = profile
    return profiles
