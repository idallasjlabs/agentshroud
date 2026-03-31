# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""HTTP client for the AgentShroud SCL REST API (/soc/v1/)."""
from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.error import HTTPError
from urllib.parse import urljoin, urlencode
from urllib.request import Request, urlopen


class SCLClient:
    """Minimal synchronous httpx-free client for the SCL API."""

    def __init__(self, base_url: str, token: str, timeout: int = 30):
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.timeout = timeout
        self._soc_base = f"{self.base_url}/soc/v1"

    def _request(
        self,
        method: str,
        path: str,
        body: Optional[Dict] = None,
        params: Optional[Dict] = None,
    ) -> Any:
        url = f"{self._soc_base}/{path.lstrip('/')}"
        if params:
            url = f"{url}?{urlencode(params)}"
        data = json.dumps(body).encode() if body is not None else None
        req = Request(
            url,
            data=data,
            method=method,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
        )
        try:
            with urlopen(req, timeout=self.timeout) as resp:
                raw = resp.read()
                return json.loads(raw) if raw else {}
        except HTTPError as exc:
            raw = exc.read()
            try:
                return json.loads(raw)
            except Exception:
                return {"error": True, "code": str(exc.code), "message": exc.reason}

    def get(self, path: str, params: Optional[Dict] = None) -> Any:
        return self._request("GET", path, params=params)

    def post(self, path: str, body: Optional[Dict] = None) -> Any:
        return self._request("POST", path, body=body)

    def put(self, path: str, body: Optional[Dict] = None) -> Any:
        return self._request("PUT", path, body=body)

    def delete(self, path: str) -> Any:
        return self._request("DELETE", path)

    # ------------------------------------------------------------------
    # Convenience methods
    # ------------------------------------------------------------------

    def get_services(self) -> List[Dict]:
        return self.get("/services")

    def restart_service(self, name: str, confirm: bool = False) -> Dict:
        return self.post(f"/services/{name}/restart", {"confirm": confirm})

    def stop_service(self, name: str, confirm: bool = False) -> Dict:
        return self.post(f"/services/{name}/stop", {"confirm": confirm})

    def get_logs(self, name: str, tail: int = 50) -> Dict:
        return self.get(f"/services/{name}/logs", {"tail": tail})

    def get_events(self, severity: Optional[str] = None, limit: int = 50) -> List[Dict]:
        params = {"limit": limit}
        if severity:
            params["severity"] = severity
        return self.get("/security/events", params)

    def get_risk(self) -> Dict:
        return self.get("/security/risk")

    def get_correlation(self) -> Dict:
        return self.get("/security/correlation")

    def get_users(self) -> List[Dict]:
        return self.get("/users")

    def add_collaborator(self, user_id: str) -> Dict:
        return self.post("/users/collaborator", {"user_id": user_id})

    def get_egress_pending(self) -> List[Dict]:
        return self.get("/egress/pending")

    def approve_egress(self, request_id: str) -> Dict:
        return self.post(f"/egress/{request_id}/approve")

    def deny_egress(self, request_id: str) -> Dict:
        return self.post(f"/egress/{request_id}/deny")

    def block_egress(self, reason: str = "CLI emergency block", confirm: bool = False) -> Dict:
        return self.post("/egress/emergency-block", {"reason": reason, "confirm": confirm})

    def freeze(self, confirm: bool = False) -> Dict:
        return self.post("/killswitch/freeze", {"confirm": confirm})

    def get_health(self) -> Dict:
        return self.get("/health")

    def get_groups(self) -> List[Dict]:
        return self.get("/groups")

    def add_group_member(self, group_id: str, user_id: str) -> Dict:
        return self.post(f"/groups/{group_id}/members", {"user_id": user_id})

    def set_group_mode(self, group_id: str, mode: str) -> Dict:
        return self.put(f"/groups/{group_id}/mode", {"collab_mode": mode})

    def run_scan(self, scanner: str) -> Dict:
        return self.post(f"/scan/{scanner}", {"confirm": True})


def client_from_env(base_url: Optional[str] = None, token: Optional[str] = None) -> SCLClient:
    """Build SCLClient from args or environment variables."""
    url = base_url or os.environ.get("AGENTSHROUD_URL", "http://localhost:8080")
    tok = token or os.environ.get("AGENTSHROUD_TOKEN", "") or os.environ.get("AGENTSHROUD_GATEWAY_PASSWORD", "")
    if not tok:
        raise ValueError(
            "No token provided. Set AGENTSHROUD_TOKEN or pass --token."
        )
    return SCLClient(url, tok)
