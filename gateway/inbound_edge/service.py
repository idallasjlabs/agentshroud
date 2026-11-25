# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Assemble the gateway side of the Inbound MCP Edge from ``app_state`` (SCRUM-212).

Off unless ``AGENTSHROUD_INBOUND_EDGE=1``. When on, every prerequisite is checked
and a missing one stops the edge (logged CRITICAL) rather than degrading it: the
signing key and service token must be present, the shipped descriptors must match
their signed manifest, and every vendor profile must validate.

Environment:
    AGENTSHROUD_INBOUND_EDGE        "1" to enable
    AGENTSHROUD_EDGE_PUBLIC_URL     e.g. https://marvin.tail240ea8.ts.net:8443 (issuer)
    AGENTSHROUD_EDGE_SEARXNG_URL    default http://searxng-local:8080
    AGENTSHROUD_EDGE_EGRESS_PROXY   default http://127.0.0.1:8181 (internet egress; an
                                    internal SearXNG container is reached directly)
    AGENTSHROUD_EDGE_PKE_FEEDS      comma-separated https feed URLs (tool hidden if empty)
    AGENTSHROUD_EDGE_HERMES_URL     default http://${HERMES_API_HOST_UPSTREAM}:8642
    AGENTSHROUD_EDGE_HERMES_PROFILE default edge-delegate (tool hidden unless set to on)
    AGENTSHROUD_EDGE_DELEGATE       "1" once the edge-delegate Hermes profile is seeded
    AGENTSHROUD_EDGE_OBSIDIAN_URL   Obsidian Local REST API (HTTP), e.g.
                                    http://host.docker.internal:27123; local hosts only
    AGENTSHROUD_EDGE_OBSIDIAN_KEY   its API key, set per host in docker/.env (never in
                                    the repo); a mounted obsidian_api_key secret wins.
                                    The vault_* tools are hidden unless URL and key are set.
Secrets: edge_signing_key (EC P-256 PEM), edge_gateway_token, hermes_api_key,
optional obsidian_api_key.
"""

import base64
import hmac
import ipaddress
import logging
import os
import secrets
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional
from urllib.parse import urlparse
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

import httpx

from gateway.inbound_edge.approvals import EdgeApprovals
from gateway.inbound_edge.call_pipeline import EdgeCallPipeline, EdgeDeps
from gateway.inbound_edge.descriptors import verify_shipped_descriptors
from gateway.inbound_edge.edge_jwt import TokenService
from gateway.inbound_edge.facades import HermesDelegate, LabSearch, ObsidianVault, PkeStatus
from gateway.inbound_edge.oauth_service import EdgeOAuthService, derive_seal_key
from gateway.inbound_edge.profiles import VendorProfile, load_profiles
from gateway.inbound_edge.store import EdgeStore
from gateway.ingest_api.event_bus import make_event
from gateway.security.instruction_envelope import EnvelopeSigner
from gateway.utils.secrets import _SECRETS_DIR

logger = logging.getLogger("agentshroud.inbound_edge.service")

CANARY_COUNT = 3


@dataclass
class EdgeService:
    store: EdgeStore
    tokens: TokenService
    oauth: EdgeOAuthService
    approvals: EdgeApprovals
    pipeline: EdgeCallPipeline
    service_token: str
    issuer: str
    resource: str

    @property
    def profiles(self) -> Dict[str, VendorProfile]:
        """The validated vendor profiles the pipeline enforces (read by the Command Center)."""
        return self.pipeline.d.profiles

    def service_token_ok(self, presented: Optional[str]) -> bool:
        return bool(presented) and hmac.compare_digest(
            presented.encode(), self.service_token.encode()
        )

    async def close(self) -> None:
        await self.store.close()


def _searxng_proxy(url: str, egress_proxy: Optional[str]) -> Optional[str]:
    """Proxy for lab_search's call to SearXNG.

    The egress proxy controls internet egress and only handles CONNECT, so a plain
    http GET to the internal SearXNG container through it fails (405). A single-label
    host is a container name on the internal Docker network, so that hop goes direct.
    Anything else (a dotted name or an IP, i.e. possibly the internet) keeps the
    egress proxy, so pointing AGENTSHROUD_EDGE_SEARXNG_URL elsewhere cannot bypass it.
    """
    host = urlparse(url).hostname or ""
    if host and "." not in host and ":" not in host and host != "localhost":
        return None
    return egress_proxy


_OBSIDIAN_LOCAL_HOSTS = {"host.docker.internal", "localhost"}


def _obsidian_url(url: str) -> Optional[str]:
    """The Obsidian base URL if it names a local service, else ``None`` (tools hidden).

    The vault hop goes direct, not through the egress proxy: that proxy only does
    CONNECT, so a plain-HTTP request through it fails, as for SearXNG. Going direct
    is only safe because the target is pinned to local hosts here: plain http, no
    credentials in the URL, no path, and a host that is host.docker.internal,
    localhost, a single-label container name or a loopback/private IP literal. A
    public name or address is refused, so the Bearer key cannot be sent off-box by
    a mistyped setting.
    """
    try:
        parsed = urlparse(url.strip())
        port = parsed.port
    except ValueError:
        return None
    host = (parsed.hostname or "").lower()
    if parsed.scheme != "http" or not host or port is None:
        return None
    if parsed.username or parsed.password or parsed.path not in ("", "/"):
        return None
    if parsed.query or parsed.fragment:
        return None
    if host in _OBSIDIAN_LOCAL_HOSTS:
        return f"http://{host}:{port}"
    try:
        ip = ipaddress.ip_address(host)
    except ValueError:
        # Not an IP: only a single-label (container) name is local.
        return f"http://{host}:{port}" if "." not in host else None
    if ip.is_unspecified or not (ip.is_loopback or ip.is_private):
        return None
    return f"http://{ip.compressed if ip.version == 4 else f'[{ip.compressed}]'}:{port}"


def _obsidian_today(tz_name: str):
    """'Today' for vault_tasks in the owner's timezone (GATEWAY_TZ)."""
    try:
        tz = ZoneInfo(tz_name)
    except (ZoneInfoNotFoundError, ValueError):
        tz = ZoneInfo("UTC")
    return lambda: datetime.now(tz).date()


def _read_secret_blob(name: str) -> bytes:
    """Whole secret file (PEM is multi-line; gateway.utils.secrets keeps only the last line)."""
    try:
        return (Path(_SECRETS_DIR) / name).read_bytes().strip()
    except OSError:
        return b""


async def _telegram_send(bot_token: str, chat_id: str, text: str, markup=None) -> None:
    payload: Dict[str, Any] = {"chat_id": chat_id, "text": text}
    if markup:
        payload["reply_markup"] = markup
    async with httpx.AsyncClient(timeout=10.0) as client:
        resp = await client.post(
            f"https://api.telegram.org/bot{bot_token}/sendMessage", json=payload
        )
        resp.raise_for_status()


async def build_edge_service(app_state: Any) -> Optional[EdgeService]:
    if os.environ.get("AGENTSHROUD_INBOUND_EDGE", "0") != "1":
        logger.info("Inbound MCP Edge disabled (AGENTSHROUD_INBOUND_EDGE != 1)")
        return None

    signing_key = _read_secret_blob("edge_signing_key")
    service_token = _read_secret_blob("edge_gateway_token").decode().strip()
    issuer = os.environ.get("AGENTSHROUD_EDGE_PUBLIC_URL", "").rstrip("/")
    if not signing_key or len(service_token) < 32 or not issuer.startswith("https://"):
        logger.critical(
            "Inbound MCP Edge NOT started: edge_signing_key, edge_gateway_token (>=32 chars) "
            "and an https AGENTSHROUD_EDGE_PUBLIC_URL are all required"
        )
        return None
    verify_shipped_descriptors()  # raises DescriptorIntegrityError → caller refuses to start
    profiles = load_profiles()  # raises ProfileError → caller refuses to start
    resource = f"{issuer}/mcp"

    data_dir = os.environ.get("AGENTSHROUD_DATA_DIR", "/app/data")
    store = EdgeStore(Path(data_dir) / "inbound_edge.db", seal_key=derive_seal_key(signing_key))
    await store.init()
    tokens = TokenService(store, signing_key, issuer, resource)

    queue = app_state.approval_queue
    bot_token = getattr(queue, "bot_token", None)
    owner_chat = getattr(queue, "admin_chat_id", None)

    async def card(text: str, markup: Dict[str, Any]) -> None:
        if bot_token and owner_chat:
            await _telegram_send(bot_token, str(owner_chat), text, markup)

    async def notify(text: str) -> None:
        if bot_token and owner_chat:
            await _telegram_send(bot_token, str(owner_chat), text)

    approvals = EdgeApprovals(store, queue, notifier=card)
    oauth = EdgeOAuthService(store, tokens, profiles, issuer, resource, notify=notify)

    proxy = os.environ.get("AGENTSHROUD_EDGE_EGRESS_PROXY", "http://127.0.0.1:8181") or None
    searxng = os.environ.get("AGENTSHROUD_EDGE_SEARXNG_URL", "http://searxng-local:8080")
    facades: Dict[str, Any] = {"lab_search": LabSearch(searxng, _searxng_proxy(searxng, proxy))}
    feeds = [u.strip() for u in os.environ.get("AGENTSHROUD_EDGE_PKE_FEEDS", "").split(",")]
    if any(feeds):
        facades["pke_status"] = PkeStatus([u for u in feeds if u], proxy)
    local_agents = set()
    if os.environ.get("AGENTSHROUD_EDGE_DELEGATE", "0") == "1":
        hermes_host = os.environ.get("HERMES_API_HOST_UPSTREAM", "agentshroud-hermes-v2")
        hermes_key = _read_secret_blob("hermes_api_key").decode().strip()
        if hermes_key:
            facades["delegate_to_hermes"] = HermesDelegate(
                os.environ.get("AGENTSHROUD_EDGE_HERMES_URL", f"http://{hermes_host}:8642"),
                hermes_key,
                os.environ.get("AGENTSHROUD_EDGE_HERMES_PROFILE", "edge-delegate"),
                EnvelopeSigner(),
            )
            local_agents.add("hermes")
    obsidian_raw = os.environ.get("AGENTSHROUD_EDGE_OBSIDIAN_URL", "").strip()
    obsidian_key = (
        _read_secret_blob("obsidian_api_key").decode().strip()
        or os.environ.get("AGENTSHROUD_EDGE_OBSIDIAN_KEY", "").strip()
    )
    if obsidian_raw and obsidian_key:
        obsidian_url = _obsidian_url(obsidian_raw)
        if obsidian_url is None:
            logger.critical(
                "Obsidian vault tools NOT offered: AGENTSHROUD_EDGE_OBSIDIAN_URL must be "
                "http://<local host>:<port> (host.docker.internal, localhost, a container "
                "name or a private IP)"
            )
        else:
            vault = ObsidianVault(
                obsidian_url,
                obsidian_key,
                EnvelopeSigner(),
                today=_obsidian_today(os.environ.get("GATEWAY_TZ", "UTC")),
            )
            facades.update(vault.facades())

    pipeline_state = getattr(app_state, "pipeline", None)
    tripwire = getattr(pipeline_state, "canary_tripwire", None)
    if tripwire is None:
        from gateway.security.canary_tripwire import CanaryTripwire

        tripwire = CanaryTripwire()
    # Per-install canaries: planted in the edge-delegate persona (see
    # docker/bots/hermes/init-config.sh) and registered here so any echo trips.
    for value in await store_canaries(store):
        tripwire.register_canary(value, target="inbound_edge")

    from gateway.ingest_api.sanitizer import PIISanitizer
    from gateway.security.encoding_detector import EncodingDetector
    from gateway.security.heuristic_classifier import HeuristicClassifier
    from gateway.security.prompt_guard import PromptGuard

    if getattr(app_state, "audit_store", None) is None:
        logger.critical("Inbound MCP Edge NOT started: audit store unavailable")
        await store.close()
        return None
    deps = EdgeDeps(
        profiles=profiles,
        tokens=tokens,
        store=store,
        approvals=approvals,
        audit=app_state.audit_store,
        emit=app_state.event_bus.emit,
        # The edge uses enforce-mode PromptGuard regardless of the gateway's global
        # mode; vendor monitor mode is the only relaxation and is per profile.
        prompt_guard=PromptGuard(),
        encoding_detector=EncodingDetector(),
        heuristic=HeuristicClassifier(),
        lockdown=app_state.progressive_lockdown,
        tripwire=tripwire,
        sanitizer=getattr(app_state, "sanitizer", None) or PIISanitizer(app_state.config.pii),
        facades=facades,
        local_agents=local_agents,
    )
    service = EdgeService(
        store=store,
        tokens=tokens,
        oauth=oauth,
        approvals=approvals,
        pipeline=EdgeCallPipeline(deps),
        service_token=service_token,
        issuer=issuer,
        resource=resource,
    )
    await app_state.event_bus.emit(
        make_event(
            "edge_event",
            "Inbound MCP Edge started",
            {"vendors_enabled": sorted(v for v, p in profiles.items() if p.enabled)},
        )
    )
    logger.info(
        "Inbound MCP Edge ready: issuer=%s tools=%s vendors_enabled=%s",
        issuer,
        sorted(facades),
        sorted(v for v, p in profiles.items() if p.enabled),
    )
    return service


async def store_canaries(store: EdgeStore) -> list[str]:
    """Stable per-install canary values, created once and kept in the edge store."""
    await store.db.execute(
        "CREATE TABLE IF NOT EXISTS canaries (value TEXT PRIMARY KEY, created_at REAL)"
    )
    async with store.db.execute("SELECT value FROM canaries") as cur:
        values = [r[0] async for r in cur]
    while len(values) < CANARY_COUNT:
        value = "ASB-EDGE-" + base64.b32encode(secrets.token_bytes(10)).decode().rstrip("=")
        await store.db.execute("INSERT INTO canaries VALUES (?, strftime('%s','now'))", (value,))
        values.append(value)
    return values
