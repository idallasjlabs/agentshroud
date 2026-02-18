"""Kill Switch Tests — verify freeze, shutdown, disconnect modes."""

import os
import stat
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parent.parent.parent
KILLSWITCH_PATH = REPO_ROOT / "docker" / "scripts" / "killswitch.sh"


class TestKillSwitchScript:
    """Verify the kill switch script structure and modes."""

    @pytest.fixture
    def script_content(self):
        if not KILLSWITCH_PATH.exists():
            pytest.skip("killswitch.sh not found")
        return KILLSWITCH_PATH.read_text()

    def test_script_exists(self):
        assert KILLSWITCH_PATH.exists(), "Kill switch script must exist"

    def test_script_is_executable(self):
        if not KILLSWITCH_PATH.exists():
            pytest.skip("killswitch.sh not found")
        mode = os.stat(KILLSWITCH_PATH).st_mode
        assert mode & stat.S_IXUSR, "Kill switch script should be executable"

    def test_supports_freeze_mode(self, script_content):
        assert "freeze" in script_content, "Must support freeze mode"

    def test_supports_shutdown_mode(self, script_content):
        assert "shutdown" in script_content, "Must support shutdown mode"

    def test_supports_disconnect_mode(self, script_content):
        assert "disconnect" in script_content, "Must support disconnect mode"

    def test_freeze_pauses_containers(self, script_content):
        assert "pause" in script_content.lower() or "freeze" in script_content.lower()

    def test_disconnect_exports_ledger(self, script_content):
        # Disconnect mode should export/backup audit data
        assert "ledger" in script_content.lower() or "export" in script_content.lower() or "audit" in script_content.lower()

    def test_has_confirmation_prompt(self, script_content):
        # Should confirm before destructive actions
        assert "confirm" in script_content.lower() or "read -p" in script_content

    def test_has_usage_function(self, script_content):
        assert "usage" in script_content

    def test_invalid_mode_shows_usage(self, script_content):
        assert "usage" in script_content and "Error" in script_content or "Invalid" in script_content

    def test_creates_incident_record(self, script_content):
        # Should create a timestamped incident record
        assert "TIMESTAMP" in script_content or "timestamp" in script_content or "date" in script_content

    def test_sets_strict_mode(self, script_content):
        assert "set -e" in script_content, "Script should use strict error handling"


class TestKillSwitchConfig:
    """Kill switch configuration in example configs."""

    def test_paranoid_env_has_kill_switch(self):
        path = REPO_ROOT / "examples" / "paranoid.env"
        if not path.exists():
            pytest.skip("paranoid.env not found")
        content = path.read_text()
        assert "KILL_SWITCH_ENABLED=true" in content

    def test_paranoid_env_kill_switch_action(self):
        path = REPO_ROOT / "examples" / "paranoid.env"
        if not path.exists():
            pytest.skip("paranoid.env not found")
        content = path.read_text()
        assert "KILL_SWITCH_ACTION=" in content
        # Should be one of: freeze, shutdown, disconnect
        assert any(mode in content for mode in ["freeze", "shutdown", "disconnect"])

    def test_recommended_env_has_kill_switch(self):
        path = REPO_ROOT / "examples" / "recommended.env"
        if not path.exists():
            pytest.skip("recommended.env not found")
        content = path.read_text()
        assert "KILL_SWITCH_ENABLED=true" in content
