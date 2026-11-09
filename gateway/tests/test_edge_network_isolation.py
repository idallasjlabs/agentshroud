# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Static network-isolation contract for the Inbound MCP Edge (SCRUM-217).

The edge container is the only internet-reachable AgentShroud process. Its blast
radius is bounded by compose topology alone, so that topology is pinned here for
prod (base file) and dev (base + marvin override, with the override's ``!override``
semantics applied):

* the edge is on ``agentshroud-dmz`` only, and the DMZ is ``internal: true``;
* the DMZ's only other member is the gateway, so the edge cannot reach Hermes,
  OpenClaw, docker-socket-proxy or anything on the isolated/internal tiers;
* the edge has no volumes (so no docker.sock), no published ports, a read-only
  root, ``cap_drop: [ALL]``, a non-root numeric user, ``no-new-privileges``,
  Docker's default seccomp, and only the ``edge_gateway_token`` secret (never
  the signing key);
* the DMZ subnet is outside the gateway's ``PROXY_ALLOWED_NETWORKS``, so the edge
  cannot use ``/v1``, ``/forward`` or the CONNECT proxy;
* the gateway publishes the edge port on 127.0.0.1 only.

Every check is also run against a deliberately broken copy of the compose model
(``MUTATIONS``) to prove it fails when its control is removed.

IEC 62443: FR5 (Restricted Data Flow) SR 5.1/5.2, SL2.
"""

from __future__ import annotations

import copy
import ipaddress
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
BASE = REPO_ROOT / "docker" / "docker-compose.yml"
DEV_OVERRIDE = REPO_ROOT / "docker" / "docker-compose.agentshroud-bot.marvin.yml"

EDGE = "agentshroud-mcp-edge"
GATEWAY = "gateway"
DMZ = "agentshroud-dmz"
EDGE_PORT = 8443


class _Override(list):
    """A sequence tagged ``!override`` — replaces instead of merging."""


class _ComposeLoader(yaml.SafeLoader):
    pass


def _override(loader: yaml.SafeLoader, node: yaml.Node) -> Any:
    if isinstance(node, yaml.SequenceNode):
        return _Override(loader.construct_sequence(node, deep=True))
    if isinstance(node, yaml.MappingNode):
        mapping = loader.construct_mapping(node, deep=True)
        mapping["__override__"] = True
        return mapping
    return loader.construct_scalar(node)


_ComposeLoader.add_constructor("!override", _override)
_ComposeLoader.add_constructor("!reset", lambda loader, node: None)


def _load(path: Path) -> Dict[str, Any]:
    # Fixed repo paths only (BASE / DEV_OVERRIDE).
    return yaml.load(path.read_text(), Loader=_ComposeLoader)  # nosec B506 - SafeLoader subclass


def _env_key(entry: str) -> str:
    return entry.split("=", 1)[0]


def _merge(base: Any, over: Any, key: str = "") -> Any:
    """Minimal compose merge: mappings deep-merge, ``!override`` replaces,
    ``environment`` lists merge by variable name, other sequences append-unique."""
    if isinstance(over, _Override):
        return list(over)
    if isinstance(over, dict) and over.pop("__override__", False):
        return over
    if isinstance(base, dict) and isinstance(over, dict):
        out = dict(base)
        for k, v in over.items():
            out[k] = _merge(base[k], v, k) if k in base else _strip(v)
        return out
    if isinstance(base, list) and isinstance(over, list):
        if key == "environment":
            merged = {_env_key(e): e for e in base}
            merged.update({_env_key(e): e for e in over})
            return list(merged.values())
        return base + [v for v in over if v not in base]
    return _strip(over)


def _strip(value: Any) -> Any:
    if isinstance(value, _Override):
        return list(value)
    if isinstance(value, dict):
        return {k: _strip(v) for k, v in value.items() if k != "__override__"}
    return value


def _compose(env: str) -> Dict[str, Any]:
    model = _strip(_load(BASE))
    if env == "dev":
        model = _merge(model, _load(DEV_OVERRIDE))
    return model


# ── model accessors ─────────────────────────────────────────────────────────────


def _networks(svc: Dict[str, Any]) -> List[str]:
    nets = svc.get("networks") or []
    return list(nets) if isinstance(nets, (list, dict)) else []


def _environment(svc: Dict[str, Any]) -> Dict[str, str]:
    env = svc.get("environment") or {}
    if isinstance(env, dict):
        return {k: str(v) for k, v in env.items()}
    return {_env_key(e): (e.split("=", 1)[1] if "=" in e else "") for e in env}


def _subnets(compose: Dict[str, Any], network: str) -> List[ipaddress.IPv4Network]:
    cfg = (compose["networks"].get(network) or {}).get("ipam", {}).get("config", [])
    return [ipaddress.ip_network(c["subnet"]) for c in cfg if "subnet" in c]


def _published(port: Any) -> Optional[Dict[str, str]]:
    """Normalise a compose port (short or long syntax) to host_ip/published/target."""
    if isinstance(port, dict):
        return {
            "host_ip": str(port.get("host_ip", "")),
            "published": str(port.get("published", "")),
            "target": str(port.get("target", "")),
        }
    parts = str(port).split("/")[0].split(":")
    if len(parts) == 3:
        return {"host_ip": parts[0], "published": parts[1], "target": parts[2]}
    if len(parts) == 2:
        return {"host_ip": "", "published": parts[0], "target": parts[1]}
    return {"host_ip": "", "published": "", "target": parts[0]}


# ── checks: each returns None when the control holds, else the violation ────────


def check_edge_on_dmz_only(c):
    nets = _networks(c["services"][EDGE])
    return None if nets == [DMZ] else f"edge networks are {nets}, expected only {DMZ}"


def check_dmz_internal(c):
    return None if c["networks"][DMZ].get("internal") is True else f"{DMZ} is not internal: true"


def check_dmz_members(c):
    members = sorted(n for n, s in c["services"].items() if DMZ in _networks(s))
    expected = sorted([EDGE, GATEWAY])
    return None if members == expected else f"{DMZ} members are {members}, expected {expected}"


def check_edge_no_volumes(c):
    svc = c["services"][EDGE]
    if svc.get("volumes") or svc.get("volumes_from"):
        return f"edge mounts volumes: {svc.get('volumes') or svc.get('volumes_from')}"
    if "docker.sock" in yaml.safe_dump(svc):
        return "edge references docker.sock"
    return None


def check_edge_read_only(c):
    return None if c["services"][EDGE].get("read_only") is True else "edge root is not read_only"


def check_edge_cap_drop_all(c):
    svc = c["services"][EDGE]
    if svc.get("cap_drop") != ["ALL"]:
        return f"edge cap_drop is {svc.get('cap_drop')}, expected [ALL]"
    if svc.get("cap_add"):
        return f"edge adds capabilities {svc['cap_add']}"
    if svc.get("privileged"):
        return "edge is privileged"
    return None


def check_edge_non_root(c):
    user = str(c["services"][EDGE].get("user", ""))
    uid = user.split(":", 1)[0]
    if not uid.isdigit() or int(uid) == 0:
        return f"edge user {user!r} is not a numeric non-root UID"
    return None


def check_edge_no_new_privileges_default_seccomp(c):
    opts = [str(o) for o in c["services"][EDGE].get("security_opt") or []]
    if "no-new-privileges:true" not in opts:
        return "edge lacks no-new-privileges:true"
    if any(o.startswith("seccomp") for o in opts):
        return f"edge overrides the default seccomp profile: {opts}"
    return None


def check_edge_no_published_ports(c):
    svc = c["services"][EDGE]
    if svc.get("ports") or svc.get("network_mode"):
        return f"edge publishes ports/network_mode: {svc.get('ports') or svc.get('network_mode')}"
    return None


def check_edge_secrets(c):
    secrets = [
        s if isinstance(s, str) else s.get("source")
        for s in c["services"][EDGE].get("secrets") or []
    ]
    return None if secrets == ["edge_gateway_token"] else f"edge secrets are {secrets}"


def check_proxy_allowlist_excludes_dmz(c):
    allowed = _environment(c["services"][GATEWAY]).get("PROXY_ALLOWED_NETWORKS", "")
    dmz = _subnets(c, DMZ)
    if not dmz:
        return f"{DMZ} has no subnet"
    for cidr in filter(None, (x.strip() for x in allowed.split(","))):
        net = ipaddress.ip_network(cidr, strict=False)
        if any(net.overlaps(d) for d in dmz):
            return f"PROXY_ALLOWED_NETWORKS entry {cidr} overlaps the DMZ {dmz}"
    return None


def check_gateway_edge_port_loopback_only(c):
    ports = [_published(p) for p in c["services"][GATEWAY].get("ports") or []]
    edge = [p for p in ports if p["target"] == str(EDGE_PORT)]
    if not edge:
        return f"gateway does not publish the edge forwarder port {EDGE_PORT}"
    bad = [p for p in edge if p["host_ip"] != "127.0.0.1"]
    return None if not bad else f"edge port published beyond loopback: {bad}"


def check_gateway_keeps_dual_membership(c):
    nets = _networks(c["services"][GATEWAY])
    need = {"agentshroud-internal", "agentshroud-isolated", DMZ}
    return None if need <= set(nets) else f"gateway networks {nets} missing {need - set(nets)}"


def check_dmz_subnet_unique(c):
    dmz = _subnets(c, DMZ)
    for name in c["networks"]:
        if name == DMZ:
            continue
        for other in _subnets(c, name):
            if any(other.overlaps(d) for d in dmz):
                return f"{DMZ} {dmz} overlaps {name} {other}"
    return None


def check_issuer_matches(c):
    edge = _environment(c["services"][EDGE]).get("EDGE_PUBLIC_URL")
    gw = _environment(c["services"][GATEWAY]).get("AGENTSHROUD_EDGE_PUBLIC_URL")
    return None if edge and edge == gw else f"edge issuer {edge!r} != gateway issuer {gw!r}"


def check_forwarder_targets_edge(c):
    edge = c["services"][EDGE]
    upstream = _environment(c["services"][GATEWAY]).get("AGENTSHROUD_EDGE_UPSTREAM_HOST")
    names = {EDGE, edge.get("container_name"), edge.get("hostname")}
    return (
        None
        if upstream in names
        else f"gateway forwarder upstream {upstream!r} is not the edge {names}"
    )


CHECKS: Dict[str, Callable[[Dict[str, Any]], Optional[str]]] = {
    f.__name__: f
    for f in (
        check_edge_on_dmz_only,
        check_dmz_internal,
        check_dmz_members,
        check_edge_no_volumes,
        check_edge_read_only,
        check_edge_cap_drop_all,
        check_edge_non_root,
        check_edge_no_new_privileges_default_seccomp,
        check_edge_no_published_ports,
        check_edge_secrets,
        check_proxy_allowlist_excludes_dmz,
        check_gateway_edge_port_loopback_only,
        check_gateway_keeps_dual_membership,
        check_dmz_subnet_unique,
        check_issuer_matches,
        check_forwarder_targets_edge,
    )
}


@pytest.fixture(scope="module", params=["prod", "dev"])
def compose(request):
    return _compose(request.param)


@pytest.mark.parametrize("name", sorted(CHECKS))
def test_isolation_control_holds(compose, name):
    assert CHECKS[name](compose) is None, CHECKS[name](compose)


def test_dev_and_prod_dmz_subnets_differ():
    prod, dev = _subnets(_compose("prod"), DMZ), _subnets(_compose("dev"), DMZ)
    assert prod and dev and not any(p.overlaps(d) for p in prod for d in dev)


def test_dev_override_renames_edge_and_retargets_forwarder():
    dev = _compose("dev")
    assert dev["services"][EDGE]["container_name"] == "agentshroud-dev-mcp-edge"
    assert _environment(dev["services"][GATEWAY])["AGENTSHROUD_EDGE_UPSTREAM_HOST"] == (
        "agentshroud-dev-mcp-edge"
    )


# ── mutation proof: every check fails when its control is removed ───────────────


def _svc(c, name):
    return c["services"][name]


def _add_env(c, svc, entry):
    env = _svc(c, svc).setdefault("environment", [])
    key = _env_key(entry)
    _svc(c, svc)["environment"] = [e for e in env if _env_key(e) != key] + [entry]


MUTATIONS: List[tuple] = [
    ("check_edge_on_dmz_only", lambda c: _svc(c, EDGE)["networks"].append("agentshroud-isolated")),
    ("check_edge_on_dmz_only", lambda c: _svc(c, EDGE).update(networks=["agentshroud-internal"])),
    ("check_dmz_internal", lambda c: c["networks"][DMZ].update(internal=False)),
    ("check_dmz_members", lambda c: _svc(c, "hermes")["networks"].append(DMZ)),
    ("check_dmz_members", lambda c: _svc(c, "docker-socket-proxy").update(networks=[DMZ])),
    (
        "check_edge_no_volumes",
        lambda c: _svc(c, EDGE).update(volumes=["/var/run/docker.sock:/var/run/docker.sock:ro"]),
    ),
    ("check_edge_read_only", lambda c: _svc(c, EDGE).pop("read_only")),
    ("check_edge_cap_drop_all", lambda c: _svc(c, EDGE).update(cap_add=["NET_RAW"])),
    ("check_edge_cap_drop_all", lambda c: _svc(c, EDGE).pop("cap_drop")),
    ("check_edge_non_root", lambda c: _svc(c, EDGE).update(user="0:0")),
    ("check_edge_non_root", lambda c: _svc(c, EDGE).pop("user")),
    (
        "check_edge_no_new_privileges_default_seccomp",
        lambda c: _svc(c, EDGE)["security_opt"].append("seccomp=unconfined"),
    ),
    ("check_edge_no_new_privileges_default_seccomp", lambda c: _svc(c, EDGE).pop("security_opt")),
    ("check_edge_no_published_ports", lambda c: _svc(c, EDGE).update(ports=["8443:8443"])),
    ("check_edge_secrets", lambda c: _svc(c, EDGE)["secrets"].append("edge_signing_key")),
    (
        "check_proxy_allowlist_excludes_dmz",
        lambda c: _add_env(
            c,
            GATEWAY,
            "PROXY_ALLOWED_NETWORKS="
            + ",".join(str(n) for n in _subnets(c, DMZ))
            + ",10.254.111.0/24",
        ),
    ),
    (
        "check_proxy_allowlist_excludes_dmz",
        lambda c: _add_env(c, GATEWAY, "PROXY_ALLOWED_NETWORKS=0.0.0.0/0"),
    ),
    (
        "check_gateway_edge_port_loopback_only",
        lambda c: _svc(c, GATEWAY)["ports"].append("0.0.0.0:8443:8443"),
    ),
    (
        "check_gateway_edge_port_loopback_only",
        lambda c: _svc(c, GATEWAY).update(
            ports=[p for p in _svc(c, GATEWAY)["ports"] if not str(p).endswith(":8443")]
        ),
    ),
    (
        "check_gateway_keeps_dual_membership",
        lambda c: _svc(c, GATEWAY)["networks"].remove("agentshroud-isolated"),
    ),
    (
        "check_dmz_subnet_unique",
        lambda c: c["networks"][DMZ]["ipam"].update(
            config=copy.deepcopy(c["networks"]["agentshroud-isolated"]["ipam"]["config"])
        ),
    ),
    (
        "check_issuer_matches",
        lambda c: _add_env(c, EDGE, "EDGE_PUBLIC_URL=https://attacker.example:8443"),
    ),
    (
        "check_forwarder_targets_edge",
        lambda c: _add_env(c, GATEWAY, "AGENTSHROUD_EDGE_UPSTREAM_HOST=agentshroud-hermes-v2"),
    ),
]


def test_every_check_has_a_mutation():
    assert {name for name, _ in MUTATIONS} == set(CHECKS)


@pytest.mark.parametrize(
    "name,mutate", MUTATIONS, ids=[f"{n}-{i}" for i, (n, _) in enumerate(MUTATIONS)]
)
def test_check_fails_when_control_removed(compose, name, mutate):
    broken = copy.deepcopy(compose)
    mutate(broken)
    assert CHECKS[name](broken) is not None, f"{name} still passes after mutation"
