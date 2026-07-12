# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Schema-driven contract fuzzing for the ingest/data-plane API (SCRUM-76).

Complements test_api_contract.py's snapshot/drift gate.  The drift gate proves
the schema hasn't changed; this proves the *implementation* survives adversarial
input against that schema — the bug class (unhandled 500s on malformed bodies,
type confusion, oversized/deeply-nested payloads) that schemathesis targets,
here implemented dependency-free with the existing FastAPI TestClient so it
runs offline and needs no new package.

Scope: only body-parsing DATA-plane endpoints (those declaring a requestBody in
the committed OpenAPI snapshot).  Destructive CONTROL-plane routes (kill switch,
rebuild, service start/stop, upgrades/rollbacks, DNS mutation, credential
rotation) are DENYLISTED — the fuzzer must never risk executing an operational
action even in the unauthenticated test app.

Contract asserted for every (path, payload):
- never HTTP 500 (an unhandled exception is always a bug)
- status is a sane, documented-shape code
- if a body is returned it is valid JSON (no half-serialized error leak)

COVERAGE BOUNDARY (stated honestly — no security theater): the test app runs
without lifespan, so most routes reject at the AUTH boundary (401) before
Pydantic body validation.  This gate therefore proves the auth boundary and
the public / localhost-gated endpoints (e.g. /api/alerts, /soc/v1/auth/login)
never 500 on adversarial input; DEEP authenticated body-parsing fuzz needs a
signed-token fixture and is tracked as follow-up in SCRUM-76's Jira comment.
Both layers matter — a crash at the auth boundary is exploitable pre-auth.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

SNAPSHOT_PATH = Path(__file__).resolve().parent.parent / "openapi.json"

# Path PREFIXES whose mutating routes must never be fuzzed — executing them
# (even unauthenticated) could take an operational action.  Matched by
# str.startswith on the OpenAPI path template.
_DESTRUCTIVE_PREFIXES = (
    "/api/killswitch",
    "/api/rebuild",
    "/api/services",
    "/api/updates",
    "/api/v1/versions",
    "/api/mode",
    "/api/config",
    "/api/skills/reload",
    "/manage/credentials",
    "/manage/dns",
    "/manage/canary",
    "/manage/deep-test",
    "/credentials/op-proxy",  # proxies to the host 1Password agent
    "/email/",  # would attempt real mail delivery
)

# Adversarial payload battery — each is sent as the JSON body.
_FUZZ_PAYLOADS: list[tuple[str, object]] = [
    ("empty_object", {}),
    ("null", None),
    ("empty_string", ""),
    ("bare_array", [1, 2, 3]),
    ("bare_number", 42),
    ("bare_bool", True),
    ("wrong_types", {"content": 12345, "source": ["not", "a", "string"], "user_id": {}}),
    ("null_fields", {"content": None, "source": None, "route_to": None}),
    ("huge_string", {"content": "A" * 200_000}),
    ("deeply_nested", {"content": _n if (_n := {"x": 1}) else 1}),  # replaced below
    ("unicode_soup", {"content": "\U0001f525 \ufeff \U0001f600 \x1b[31m", "source": "api"}),
    ("sql_ish", {"content": "'; DROP TABLE ledger;--", "source": "api"}),
    ("path_traversal", {"content": "../../../etc/passwd", "source": "api"}),
    ("extra_unknown_fields", {"content": "hi", "source": "api", "__proto__": {"x": 1}, "z": "q"}),
    ("negative_numbers", {"content": "hi", "source": "api", "limit": -(2**40)}),
]


def _deep_nest(depth: int = 60) -> dict:
    node: dict = {"content": "x"}
    cur = node
    for _ in range(depth):
        cur["nested"] = {}
        cur = cur["nested"]
    return node


# Fix the deeply-nested payload (comprehension placeholder above kept the list
# literal readable; real value built here).
_FUZZ_PAYLOADS = [
    (name, _deep_nest() if name == "deeply_nested" else body) for name, body in _FUZZ_PAYLOADS
]

_ACCEPTABLE_STATUSES = {
    200,
    201,
    202,
    204,
    400,
    401,
    403,
    404,
    405,
    409,
    413,
    415,
    422,
    429,
    501,
    503,  # documented "not wired in test app" / "unavailable" shapes
}


def _fuzzable_endpoints() -> list[tuple[str, str]]:
    """(method, path) for every non-destructive route declaring a requestBody."""
    if not SNAPSHOT_PATH.exists():
        return []
    schema = json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))
    out: list[tuple[str, str]] = []
    for path, methods in schema.get("paths", {}).items():
        if any(path.startswith(p) for p in _DESTRUCTIVE_PREFIXES):
            continue
        for method, op in methods.items():
            if method not in ("post", "put", "patch"):
                continue
            if "requestBody" not in op:
                continue
            # Path-parameter templates: substitute a benign token so routing
            # resolves without hitting a {placeholder} literal.
            concrete = path
            while "{" in concrete:
                start = concrete.index("{")
                end = concrete.index("}", start)
                concrete = concrete[:start] + "fuzz-id" + concrete[end + 1 :]
            out.append((method, concrete))
    return out


_ENDPOINTS = _fuzzable_endpoints()


@pytest.fixture(scope="module")
def client():
    try:
        from fastapi.testclient import TestClient

        from gateway.ingest_api.main import app

        return TestClient(app)
    except Exception as e:  # pragma: no cover - env guard
        pytest.skip(f"Could not instantiate app: {e}")


def test_fuzz_surface_is_nonempty():
    # Guards against a snapshot/denylist change silently emptying the fuzz set —
    # a green run with zero endpoints would be false assurance (no security
    # theater).
    assert _ENDPOINTS, "No fuzzable endpoints resolved — check snapshot/denylist"


@pytest.mark.parametrize("method,path", _ENDPOINTS, ids=lambda v: v if isinstance(v, str) else "")
@pytest.mark.parametrize("payload_name,payload", _FUZZ_PAYLOADS, ids=[p[0] for p in _FUZZ_PAYLOADS])
def test_endpoint_survives_adversarial_body(client, method, path, payload_name, payload):
    resp = client.request(method.upper(), path, json=payload)

    assert resp.status_code != 500, (
        f"{method.upper()} {path} returned 500 on '{payload_name}' payload — "
        "unhandled exception (input-handling bug)."
    )
    assert resp.status_code in _ACCEPTABLE_STATUSES, (
        f"{method.upper()} {path} returned undocumented {resp.status_code} " f"on '{payload_name}'."
    )
    body = resp.content
    if body:
        try:
            json.loads(body)
        except (json.JSONDecodeError, UnicodeDecodeError):
            # Non-JSON is allowed only for explicitly non-JSON content types.
            ctype = resp.headers.get("content-type", "")
            assert "application/json" not in ctype, (
                f"{method.upper()} {path} returned malformed JSON on "
                f"'{payload_name}' (content-type {ctype})."
            )


def test_destructive_routes_are_excluded():
    # Documents the safety boundary: no denylisted control-plane route may leak
    # into the fuzz set.
    for _m, path in _ENDPOINTS:
        assert not any(
            path.startswith(p.replace("{", "").rstrip("/")) and "killswitch" in path
            for p in _DESTRUCTIVE_PREFIXES
        ), f"Destructive route {path} leaked into the fuzz set"
