#!/usr/bin/env python3
"""
mcp_oauth_preflight.py

Enterprise-safe OAuth + MCP connectivity preflight.

Fixes included
- Starts a loopback callback listener BEFORE opening Atlassian auth URL.
- Reads FULL JSON bodies for token endpoints (prevents "Unterminated string" from truncation).

Supported commands
- reachability : DNS + TLS + HTTP check for one or more URLs
- oauth        : interactive OAuth checks (GitHub device flow, Atlassian 3LO PKCE)
- all          : run reachability then oauth

Usage
  set -a; source .env; set +a
  python3 mcp_oauth_preflight.py reachability --url https://mcp.atlassian.com/v1/mcp
  python3 mcp_oauth_preflight.py oauth --only atlassian
  python3 mcp_oauth_preflight.py oauth --only github
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import secrets
import socket
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request
import webbrowser
from dataclasses import dataclass
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Callable, Dict, List, Optional, Tuple


# -----------------------------
# Utility
# -----------------------------

def getenv_required(key: str) -> str:
    v = os.getenv(key, "").strip()
    if not v:
        raise SystemExit(f"Missing required env var: {key}")
    return v


def _read_body(resp, max_bytes: Optional[int]) -> bytes:
    """
    Read response body.
    - max_bytes=None -> read all bytes
    - max_bytes=int  -> read up to that many bytes
    """
    if max_bytes is None:
        return resp.read()
    return resp.read(max_bytes)


def _http_request(
    url: str,
    method: str = "GET",
    headers: Optional[Dict[str, str]] = None,
    data: Optional[bytes] = None,
    timeout: float = 10.0,
    max_bytes: Optional[int] = 2000,   # default: small, safe for reachability
) -> Tuple[int, str, Dict[str, str]]:
    req = urllib.request.Request(url=url, method=method, headers=headers or {}, data=data)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = _read_body(resp, max_bytes)
            return resp.status, body.decode("utf-8", errors="replace"), dict(resp.headers)
    except urllib.error.HTTPError as he:
        # HTTPError is also a response; include status + body
        body = _read_body(he, max_bytes)
        return he.code, body.decode("utf-8", errors="replace"), dict(he.headers)


def _dns_lookup(host: str) -> List[str]:
    out = []
    for fam, _, _, _, sockaddr in socket.getaddrinfo(host, None):
        if fam in (socket.AF_INET, socket.AF_INET6):
            out.append(sockaddr[0])
    # de-dupe while preserving order
    seen = set()
    uniq = []
    for ip in out:
        if ip not in seen:
            seen.add(ip)
            uniq.append(ip)
    return uniq


def _tls_probe(host: str, port: int = 443, timeout: float = 10.0) -> Tuple[str, str]:
    ctx = ssl.create_default_context()
    ctx.minimum_version = ssl.TLSVersion.TLSv1_2
    with socket.create_connection((host, port), timeout=timeout) as sock:
        with ctx.wrap_socket(sock, server_hostname=host) as ssock:
            tlsver = ssock.version() or "unknown"
            cert = ssock.getpeercert()
            cn = "unknown"
            for tup in cert.get("subject", ()):
                for k, v in tup:
                    if k == "commonName":
                        cn = v
                        break
            return tlsver, cn


def _normalize_url(url: str) -> str:
    if not url.startswith("http://") and not url.startswith("https://"):
        return "https://" + url
    return url


# -----------------------------
# Reachability
# -----------------------------

def cmd_reachability(urls: List[str], timeout: float = 10.0) -> int:
    print("=" * 78)
    print("MCP/OAuth Reachability Preflight (DNS + TLS + HTTP)")
    print("=" * 78)

    rc = 0
    for raw in urls:
        url = _normalize_url(raw)
        u = urllib.parse.urlparse(url)
        host = u.hostname or ""
        port = u.port or (443 if u.scheme == "https" else 80)

        print(f"\nURL: {url}")

        try:
            ips = _dns_lookup(host)
            print(f"DNS: OK  {', '.join(ips[:5])}{' ...' if len(ips) > 5 else ''}")
        except Exception as ex:
            print(f"DNS: FAIL  {ex}")
            rc = 1
            continue

        if u.scheme == "https":
            try:
                tlsver, cn = _tls_probe(host, port=port, timeout=timeout)
                print(f"TLS: OK  TLS={tlsver}, CN={cn}")
            except Exception as ex:
                print(f"TLS: FAIL  {ex}")
                rc = 1
                continue
        else:
            print("TLS: (skipped, http)")

        start = time.time()
        try:
            status, _, headers = _http_request(
                url,
                timeout=timeout,
                headers={"User-Agent": "mcp-oauth-preflight/2.1"},
                max_bytes=2000,  # reachability only
            )
            ms = int((time.time() - start) * 1000)
            loc = headers.get("Location")
            msg = f"HTTP: {status:<3}  {ms:>4}ms"
            if loc:
                msg += f"  -> {loc}"
            print(msg)

            if status in (200, 204, 301, 302, 303, 307, 308, 401, 403):
                print("HINT: Reachable. Auth may be required (401/403 is common).")
            else:
                print("HINT: Reachable but unexpected status; investigate.")
        except Exception as ex:
            ms = int((time.time() - start) * 1000)
            print(f"HTTP: FAIL {ms}ms  {ex}")
            rc = 1

    return rc


# -----------------------------
# Loopback callback listener (PKCE / auth code flows)
# -----------------------------

class _CallbackHandler(BaseHTTPRequestHandler):
    received: Dict[str, List[str]] = {}

    def do_GET(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        qs = urllib.parse.parse_qs(parsed.query)
        _CallbackHandler.received = qs

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"OAuth callback received. You can close this tab.\n")

    def log_message(self, fmt: str, *args: object) -> None:
        return  # quiet


def _start_callback_server(redirect_uri: str) -> Tuple[HTTPServer, str, int]:
    u = urllib.parse.urlparse(redirect_uri)
    host = u.hostname or "127.0.0.1"
    port = u.port or 8000
    _CallbackHandler.received = {}
    httpd = HTTPServer((host, port), _CallbackHandler)
    return httpd, host, port


def _wait_for_callback(httpd: HTTPServer, timeout: float) -> Dict[str, List[str]]:
    deadline = time.time() + timeout
    while time.time() < deadline:
        httpd.timeout = 0.2
        httpd.handle_request()
        if _CallbackHandler.received:
            break
    return _CallbackHandler.received


# -----------------------------
# OAuth: GitHub device flow
# -----------------------------

def oauth_github(timeout: float = 180.0) -> Tuple[bool, str]:
    client_id = getenv_required("GITHUB_CLIENT_ID")
    scopes = os.getenv("GITHUB_SCOPES", "read:user repo").strip() or "read:user repo"

    data = urllib.parse.urlencode({
        "client_id": client_id,
        "scope": scopes
    }).encode("utf-8")

    status, body, _ = _http_request(
        "https://github.com/login/device/code",
        method="POST",
        headers={
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "mcp-oauth-preflight/2.1",
        },
        data=data,
        timeout=15.0,
        max_bytes=None,  # read full JSON
    )
    if status != 200:
        return False, f"Device code request failed: HTTP {status} {body[:300]}"

    payload = json.loads(body)
    device_code = payload.get("device_code")
    user_code = payload.get("user_code")
    verify_uri = payload.get("verification_uri") or "https://github.com/login/device"
    interval = int(payload.get("interval", 5))

    if not device_code or not user_code:
        return False, f"Unexpected GitHub device payload: {payload}"

    print("GitHub device flow:")
    print(f"  Visit: {verify_uri}")
    print(f"  Code : {user_code}")
    try:
        webbrowser.open(verify_uri, new=2)
    except Exception:
        pass

    token_deadline = time.time() + timeout
    while time.time() < token_deadline:
        time.sleep(interval)
        data2 = urllib.parse.urlencode({
            "client_id": client_id,
            "device_code": device_code,
            "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
        }).encode("utf-8")

        status2, body2, _ = _http_request(
            "https://github.com/login/oauth/access_token",
            method="POST",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "mcp-oauth-preflight/2.1",
            },
            data=data2,
            timeout=15.0,
            max_bytes=None,  # read full JSON
        )
        if status2 != 200:
            return False, f"Token poll failed: HTTP {status2} {body2[:300]}"

        tok = json.loads(body2)
        if "access_token" in tok:
            return True, "OAuth SUCCESS (token acquired)."

        err = tok.get("error")
        if err in ("authorization_pending", "slow_down"):
            if err == "slow_down":
                interval = min(interval + 2, 15)
            continue

        return False, f"OAuth FAILED: {tok}"

    return False, "Timed out waiting for device authorization."


# -----------------------------
# OAuth: Atlassian 3LO with PKCE (loopback callback)
# -----------------------------

def _pkce_pair() -> Tuple[str, str]:
    verifier = base64.urlsafe_b64encode(secrets.token_bytes(32)).decode("utf-8").rstrip("=")
    digest = hashlib.sha256(verifier.encode("utf-8")).digest()
    challenge = base64.urlsafe_b64encode(digest).decode("utf-8").rstrip("=")
    return verifier, challenge


def oauth_atlassian(timeout: float = 180.0) -> Tuple[bool, str]:
    client_id = getenv_required("ATLASSIAN_CLIENT_ID")
    client_secret = getenv_required("ATLASSIAN_CLIENT_SECRET")
    scopes = os.getenv("ATLASSIAN_SCOPES", "").strip() or "read:jira-user read:jira-work write:jira-work read:confluence-content.summary write:confluence-content"
    redirect_uri = os.getenv("ATLASSIAN_REDIRECT_URI", "http://127.0.0.1:8000/callback").strip()

    verifier, challenge = _pkce_pair()
    state = secrets.token_urlsafe(16)

    params = {
        "audience": "api.atlassian.com",
        "client_id": client_id,
        "scope": scopes,
        "redirect_uri": redirect_uri,
        "state": state,
        "response_type": "code",
        "prompt": "consent",
        "code_challenge": challenge,
        "code_challenge_method": "S256",
    }
    auth_url = "https://auth.atlassian.com/authorize?" + urllib.parse.urlencode(
        params, quote_via=urllib.parse.quote
    )

    print("Atlassian OAuth (browser):")
    print(f"  Redirect URI: {redirect_uri}")
    print(f"  Scopes      : {scopes}")
    print(f"  {auth_url}\n")

    # Start listener BEFORE opening browser (prevents 127.0.0.1 refused)
    httpd, host, port = _start_callback_server(redirect_uri)
    print(f"Listening for OAuth callback on {host}:{port} ... (keep this terminal open)")

    try:
        webbrowser.open(auth_url, new=2)
    except Exception:
        pass

    qs = _wait_for_callback(httpd, timeout=timeout)
    httpd.server_close()

    if not qs:
        return False, "Timed out waiting for OAuth callback (loopback may be blocked)."

    err = (qs.get("error") or [None])[0]
    if err:
        return False, f"OAuth FAILED (callback error): {err}"

    code = (qs.get("code") or [None])[0]
    got_state = (qs.get("state") or [None])[0]

    if got_state != state:
        return False, "OAuth FAILED: state mismatch (possible browser/session mix-up)."
    if not code:
        return False, f"OAuth FAILED: no code in callback (params={list(qs.keys())})"

    token_payload = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code,
        "redirect_uri": redirect_uri,
        "code_verifier": verifier,
    }

    status, body, _ = _http_request(
        "https://auth.atlassian.com/oauth/token",
        method="POST",
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "mcp-oauth-preflight/2.1",
        },
        data=json.dumps(token_payload).encode("utf-8"),
        timeout=20.0,
        max_bytes=None,  # IMPORTANT: full JSON (fixes truncation / unterminated string)
    )
    if status != 200:
        return False, f"Token exchange failed: HTTP {status} {body[:500]}"

    tok = json.loads(body)
    access_token = tok.get("access_token")
    if not access_token:
        return False, f"Token exchange succeeded but no access_token present: {tok}"

    # Confirm accessible resources (proves site access)
    status2, body2, _ = _http_request(
        "https://api.atlassian.com/oauth/token/accessible-resources",
        method="GET",
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {access_token}",
            "User-Agent": "mcp-oauth-preflight/2.1",
        },
        timeout=20.0,
        max_bytes=None,  # full JSON
    )
    if status2 != 200:
        return False, f"Accessible-resources check failed: HTTP {status2} {body2[:500]}"

    resources = json.loads(body2)
    if isinstance(resources, list) and resources:
        names = ", ".join([r.get("name", "?") for r in resources[:3]])
        return True, f"OAuth SUCCESS (token acquired). Accessible resources: {names}"

    return True, "OAuth SUCCESS (token acquired). (No accessible resources returned.)"


# -----------------------------
# CLI
# -----------------------------

@dataclass
class OAuthResult:
    name: str
    ok: bool
    msg: str


def cmd_oauth(only: Optional[str], timeout: float) -> int:
    tests: List[Tuple[str, Callable[[], Tuple[bool, str]]]] = [
        ("github", lambda: oauth_github(timeout=timeout)),
        ("atlassian", lambda: oauth_atlassian(timeout=timeout)),
    ]

    if only:
        tests = [t for t in tests if t[0] == only]
        if not tests:
            raise SystemExit("--only must be one of: github, atlassian")

    results: List[OAuthResult] = []
    for name, fn in tests:
        print("=" * 78)
        print(f"OAuth Test: {name}")
        print("=" * 78)
        try:
            ok, msg = fn()
        except Exception as ex:
            ok, msg = False, f"Exception: {ex}"
        results.append(OAuthResult(name=name, ok=ok, msg=msg))
        print(("PASS: " if ok else "FAIL: ") + msg)
        print("")

    print("=" * 78)
    print("SUMMARY")
    print("=" * 78)
    rc = 0
    for r in results:
        icon = "✅" if r.ok else "❌"
        print(f"- {r.name:<9} {icon} {'PASS' if r.ok else 'FAIL'}  {r.msg}")
        if not r.ok:
            rc = 1

    print("=" * 78)
    print("MCP CONFIG (only for PASS)")
    print("=" * 78)

    any_ok = False
    for r in results:
        if not r.ok:
            continue
        any_ok = True
        if r.name == "github":
            print("GitHub OAuth PASS (device flow).")
            print("NOTE: GitHub MCP endpoint is currently incompatible with Claude MCP auth")
            print("      (no Dynamic Client Registration). Track as 'blocked by protocol'.\n")
        if r.name == "atlassian":
            print("Atlassian MCP (remote HTTP)")
            print("  claude mcp add --transport http atlassian https://mcp.atlassian.com/v1/mcp --scope project")
            print("  Then in Claude Code: /mcp -> Authenticate\n")

    if not any_ok:
        print("No OAuth tests passed, so no MCP configs are recommended yet.")

    return rc


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    ap_r = sub.add_parser("reachability", help="DNS + TLS + HTTP reachability checks")
    ap_r.add_argument("--url", action="append", required=True, help="URL to probe (repeatable)")
    ap_r.add_argument("--timeout", type=float, default=10.0)

    ap_o = sub.add_parser("oauth", help="Interactive OAuth checks")
    ap_o.add_argument("--only", choices=["github", "atlassian"], help="Run only one OAuth test")
    ap_o.add_argument("--timeout", type=float, default=180.0)

    ap_a = sub.add_parser("all", help="Run reachability then oauth")
    ap_a.add_argument("--url", action="append", required=True, help="URL to probe (repeatable)")
    ap_a.add_argument("--only", choices=["github", "atlassian"], help="Run only one OAuth test")
    ap_a.add_argument("--timeout", type=float, default=180.0)

    args = ap.parse_args()

    if args.cmd == "reachability":
        return cmd_reachability(args.url, timeout=args.timeout)
    if args.cmd == "oauth":
        return cmd_oauth(args.only, timeout=args.timeout)
    if args.cmd == "all":
        rc1 = cmd_reachability(args.url, timeout=10.0)
        rc2 = cmd_oauth(args.only, timeout=args.timeout)
        return 1 if (rc1 or rc2) else 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
