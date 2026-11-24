# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""docker/setup-secrets.sh store-one: store exactly one named secret.

`store` regenerates gateway_password and prompts for every secret, so adding one
new credential (edge_funnel_authkey) through it would rotate the gateway password
as a side effect. `store-one` must touch only the secret it is given.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SETUP = REPO / "docker" / "setup-secrets.sh"


def _run(
    tmp_path: Path, snippet: str, typed: str = "tskey-auth-TEST"
) -> subprocess.CompletedProcess:
    home = tmp_path / "home-secrets"
    script = (
        f'. "{SETUP}"; BACKEND=homedir; SECRETS_HOME_DIR="{home}"; '
        # The masked prompt reads /dev/tty; the double returns what the owner typed.
        f"read_secret_masked() {{ printf '%s' '{typed}'; }}; "
        f"{snippet}"
    )
    return subprocess.run(
        ["bash", "-c", script],
        capture_output=True,
        text=True,
        env={"PATH": "/usr/bin:/bin:/opt/homebrew/bin", "HOME": str(tmp_path)},
        check=False,
    )


def test_stores_only_the_named_secret(tmp_path):
    out = _run(tmp_path, "cmd_store_one edge_funnel_authkey")
    assert out.returncode == 0, out.stderr
    stored = sorted(p.name for p in (tmp_path / "home-secrets").iterdir())
    assert stored == ["edge_funnel_authkey.txt"]
    assert (tmp_path / "home-secrets" / "edge_funnel_authkey.txt").read_text() == "tskey-auth-TEST"


def test_never_prints_the_value(tmp_path):
    out = _run(tmp_path, "cmd_store_one edge_funnel_authkey")
    assert "tskey-auth-TEST" not in out.stdout + out.stderr


def test_unknown_name_refuses_and_stores_nothing(tmp_path):
    out = _run(tmp_path, "cmd_store_one edge_funnel_authky")
    assert out.returncode == 2
    assert not (tmp_path / "home-secrets").exists()


def test_empty_value_refuses_and_stores_nothing(tmp_path):
    out = _run(tmp_path, "cmd_store_one edge_funnel_authkey", typed="")
    assert out.returncode == 1
    assert not (tmp_path / "home-secrets").exists()


def test_missing_name_is_a_usage_error(tmp_path):
    out = _run(tmp_path, "cmd_store_one")
    assert out.returncode == 2


def test_dispatch_accepts_the_name_argument(tmp_path):
    """The CLI's flag parser rejects unknown arguments, so the name must be taken
    before it runs; an unknown name still fails with the store-one usage error."""
    out = subprocess.run(
        ["bash", str(SETUP), "store-one", "no_such_secret"],
        capture_output=True,
        text=True,
        env={
            "PATH": "/usr/bin:/bin",
            "HOME": str(tmp_path),
            "AGENTSHROUD_SECRET_BACKEND": "homedir",  # pragma: allowlist secret
        },
        check=False,
    )
    assert out.returncode == 2
    assert "Unknown argument" not in out.stderr
    assert "no_such_secret" in out.stderr
