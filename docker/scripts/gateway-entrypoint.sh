#!/bin/bash
# AgentShroud gateway root-phase entrypoint.
# Runs as root to fix bind-mount / named-volume ownership, then drops to
# the agentshroud user via gosu.  This is the standard Docker privilege-drop
# pattern (same as nginx, postgres, redis).
#
# Problem: Docker named volumes are created with the host GID (e.g. macOS
# _ssh GID 101) rather than the container GID (agentshroud GID 1000).
# freshclam and clamd cannot write to /var/lib/clamav if the GID doesn't match.
#
# This must be ENTRYPOINT (not CMD) so "$@" receives CMD arguments.
#
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
set -eo pipefail

# Fix ClamAV DB volume ownership so freshclam can write virus-definition updates.
chown -R agentshroud:agentshroud /var/lib/clamav 2>/dev/null || true

# Drop from root to agentshroud and exec the gateway start script.
exec gosu agentshroud "$@"
