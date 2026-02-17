# Codex (o4-mini) Peer Review — Phase 4 SSH Capability
Date: 2026-02-17

## Findings

[HIGH] gateway/ssh_proxy/proxy.py:11 — INJECTION_PATTERNS does not block newline characters, allowing "embedded newline" command chaining (e.g. `"ls\nrm -rf /"` bypasses the regex).
  Suggested fix: Include `\n` (and optionally `\r`) in the pattern or explicitly reject any command containing line breaks before sending to SSH.

[HIGH] gateway/ssh_proxy/proxy.py:66 — SSH is invoked with `-o StrictHostKeyChecking=no`, disabling host-key verification and opening the door to man-in-the-middle attacks.
  Suggested fix: Remove `-o StrictHostKeyChecking=no` or add support for a `known_hosts` file and enforce StrictHostKeyChecking.

[MEDIUM] gateway/ingest_api/main.py (around SSH initialization) — The `require_approval` flag in SSHConfig is never consulted. Valid, non-auto-approved commands always go to the queue, even when `require_approval: false` is set.
  Suggested fix: In the `ssh_exec` handler, check `if not proxy.config.require_approval` and treat all validated commands as auto-approved.

[MEDIUM] gateway/ssh_proxy/proxy.py:53 — Key paths from configuration (e.g. `"~/.ssh/id_ed25519"`) are passed verbatim to the SSH client without expanding `~` or environment variables.
  Suggested fix: Call `os.path.expanduser()` on `host.key_path` before building the SSH command.

[LOW] gateway/ingest_api/config.py:14 — Duplicate import of `SSHConfig` within `load_config`; the top-of-file import already brings it in.
  Suggested fix: Remove the inner import.

[LOW] gateway/ingest_api/config.py (~line 227) — The check `if ssh_section:` treats an empty dict as "no SSH config," silently falling back to defaults.
  Suggested fix: Change to `if "ssh" in raw_config:`.

[INFO] gateway/tests/test_ssh_endpoints.py — No test covers newline-based injection. Consider adding a test for commands containing `\n` or `\r`.

[INFO] gateway/ingest_api/models.py — The `SSHExecRequest.reason` field is never used in the handler or audit metadata.
