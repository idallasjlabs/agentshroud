---
source_file: "gateway/security/clamav_scanner.py"
type: "code"
community: "cli/main.py"
location: "L35"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/cli/mainpy
---

# clamd_available()

## Connections
- [[True if clamd accepts connections on its socket. Connects rather than testing…]] - `rationale_for` [EXTRACTED]
- [[clamav_scanner.py]] - `contains` [EXTRACTED]
- [[preferred_scan_binary()]] - `calls` [EXTRACTED]
- [[test_clamd_available_false_for_stale_socket_left_by_killed_daemon()]] - `calls` [EXTRACTED]
- [[test_clamd_available_false_when_socket_missing()]] - `calls` [EXTRACTED]
- [[test_clamd_available_true_when_daemon_listening()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/cli/mainpy
