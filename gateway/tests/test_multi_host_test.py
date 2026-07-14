# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for multi_host_test — host parsing + result aggregation (no real SSH)."""

from __future__ import annotations

import os
import stat
import subprocess
import sys
from pathlib import Path
from unittest.mock import MagicMock

from gateway.tools.multi_host_test import (
    DEFAULT_COMMAND,
    DEFAULT_HOSTS,
    DEFAULT_USER,
    UNREACHABLE_EXIT,
    HostResult,
    HostStatus,
    MultiHostResult,
    build_parser,
    build_ssh_argv,
    classify,
    main,
    parse_hosts,
    run_multi_host,
    ssh_runner,
    tail,
)


class TestParseHosts:
    def test_none_returns_defaults(self):
        assert parse_hosts(None) == list(DEFAULT_HOSTS)

    def test_empty_string_returns_defaults(self):
        assert parse_hosts("   ") == list(DEFAULT_HOSTS)

    def test_comma_separated(self):
        assert parse_hosts("marvin,trillian") == ["marvin", "trillian"]

    def test_whitespace_separated(self):
        assert parse_hosts("marvin trillian  pi") == ["marvin", "trillian", "pi"]

    def test_mixed_separators_and_stripping(self):
        assert parse_hosts(" marvin , trillian ,pi ") == ["marvin", "trillian", "pi"]

    def test_dedup_preserves_first_order(self):
        assert parse_hosts("a,b,a,c,b") == ["a", "b", "c"]

    def test_custom_default(self):
        assert parse_hosts(None, default=["x"]) == ["x"]

    def test_only_separators_falls_back_to_default(self):
        # A string of only commas produces no tokens -> default.
        assert parse_hosts(",,,", default=["z"]) == ["z"]


class TestTail:
    def test_empty(self):
        assert tail("") == ""

    def test_only_newlines(self):
        assert tail("\n\n\n") == ""

    def test_keeps_last_n_lines(self):
        text = "a\nb\nc\nd\ne\nf"
        assert tail(text, lines=3) == "d\ne\nf"

    def test_shorter_than_n(self):
        assert tail("one\ntwo", lines=5) == "one\ntwo"

    def test_strips_trailing_newline(self):
        assert tail("only\n", lines=5) == "only"


class TestClassify:
    def test_zero_is_pass(self):
        assert classify(0) is HostStatus.PASS

    def test_nonzero_is_fail(self):
        assert classify(1) is HostStatus.FAIL
        assert classify(2) is HostStatus.FAIL

    def test_255_is_unreachable(self):
        assert classify(UNREACHABLE_EXIT) is HostStatus.UNREACHABLE


class TestHostResult:
    def test_ok_only_when_pass(self):
        assert HostResult("h", HostStatus.PASS, 0).ok is True
        assert HostResult("h", HostStatus.FAIL, 1).ok is False
        assert HostResult("h", HostStatus.UNREACHABLE, 255).ok is False


def _fake_runner(mapping):
    """Return a runner that looks up (exit_code, output) by host name."""

    def _run(host, command):
        return mapping[host]

    return _run


class TestRunMultiHost:
    def test_all_pass(self):
        runner = _fake_runner({"a": (0, "ok\n"), "b": (0, "ok\n")})
        res = run_multi_host(["a", "b"], "cmd", runner)
        assert res.all_ok is True
        assert res.exit_code == 0
        assert [r.status for r in res.results] == [HostStatus.PASS, HostStatus.PASS]

    def test_mixed_pass_fail_unreachable(self):
        runner = _fake_runner(
            {
                "a": (0, "green"),
                "b": (1, "boom\ntraceback"),
                "c": (UNREACHABLE_EXIT, "ssh: connect refused"),
            }
        )
        res = run_multi_host(["a", "b", "c"], "cmd", runner)
        assert res.exit_code == 1
        assert res.all_ok is False
        assert [r.host for r in res.passed] == ["a"]
        assert [r.host for r in res.failed] == ["b"]
        assert [r.host for r in res.unreachable] == ["c"]

    def test_runner_exception_marks_unreachable(self):
        def _boom(host, command):
            raise OSError("network down")

        res = run_multi_host(["a"], "cmd", _boom)
        assert res.results[0].status is HostStatus.UNREACHABLE
        assert res.results[0].exit_code == UNREACHABLE_EXIT
        assert "network down" in res.results[0].output_tail
        assert res.exit_code == 1

    def test_output_tail_is_truncated(self):
        long_out = "\n".join(str(i) for i in range(20))
        runner = _fake_runner({"a": (0, long_out)})
        res = run_multi_host(["a"], "cmd", runner, tail_lines=2)
        assert res.results[0].output_tail == "18\n19"

    def test_on_host_callback_invoked_per_host(self):
        cb = MagicMock()
        runner = _fake_runner({"a": (0, ""), "b": (1, "")})
        run_multi_host(["a", "b"], "cmd", runner, on_host=cb)
        assert cb.call_count == 2

    def test_empty_host_list_is_not_ok(self):
        res = run_multi_host([], "cmd", _fake_runner({}))
        assert res.all_ok is False
        assert res.exit_code == 1


class TestMultiHostResultProperties:
    def test_render_summary_contains_hosts_and_overall(self):
        res = MultiHostResult(
            results=[
                HostResult("marvin", HostStatus.PASS, 0),
                HostResult("trillian", HostStatus.FAIL, 1),
                HostResult("raspberrypi", HostStatus.UNREACHABLE, 255),
            ]
        )
        summary = res.render_summary()
        assert "marvin" in summary
        assert "trillian" in summary
        assert "raspberrypi" in summary
        assert "OVERALL: FAIL" in summary
        assert "Passed: 1" in summary
        assert "Failed: 1" in summary
        assert "Unreachable: 1" in summary

    def test_render_summary_all_pass_overall(self):
        res = MultiHostResult(results=[HostResult("a", HostStatus.PASS, 0)])
        assert "OVERALL: PASS" in res.render_summary()

    def test_render_summary_empty(self):
        # No results -> still renders header + OVERALL FAIL without crashing.
        res = MultiHostResult()
        summary = res.render_summary()
        assert "OVERALL: FAIL" in summary
        assert "Hosts: 0" in summary


class TestBuildSshArgv:
    def test_argv_shape(self):
        argv = build_ssh_argv("marvin", "bash scripts/smoke.sh")
        assert argv[0] == "ssh"
        assert "BatchMode=yes" in argv
        assert "ConnectTimeout=10" in argv
        assert f"{DEFAULT_USER}@marvin" in argv
        assert argv[-1] == "bash scripts/smoke.sh"

    def test_custom_user(self):
        argv = build_ssh_argv("pi", "true", user="root")
        assert "root@pi" in argv


class TestSshRunner:
    def test_ssh_runner_uses_subprocess(self, monkeypatch):
        calls = {}

        class FakeProc:
            returncode = 0
            stdout = "out"
            stderr = "err"

        def fake_run(argv, **kwargs):
            calls["argv"] = argv
            calls["kwargs"] = kwargs
            return FakeProc()

        monkeypatch.setattr("gateway.tools.multi_host_test.subprocess.run", fake_run)
        run = ssh_runner()
        code, output = run("marvin", "echo hi")
        assert code == 0
        assert output == "outerr"
        assert calls["argv"][0] == "ssh"
        assert calls["kwargs"]["check"] is False

    def test_ssh_runner_none_streams(self, monkeypatch):
        class FakeProc:
            returncode = 3
            stdout = None
            stderr = None

        monkeypatch.setattr(
            "gateway.tools.multi_host_test.subprocess.run",
            lambda argv, **kw: FakeProc(),
        )
        code, output = ssh_runner()("h", "cmd")
        assert code == 3
        assert output == ""


class TestParserAndCommandResolution:
    def test_parser_defaults(self):
        args = build_parser().parse_args([])
        assert args.hosts is None
        assert args.user == DEFAULT_USER
        assert args.dry_run is False

    def test_parser_hosts_and_command(self):
        args = build_parser().parse_args(["--hosts", "a,b", "--", "echo", "x"])
        assert args.hosts == "a,b"
        assert args.command[-2:] == ["echo", "x"]


class TestMain:
    def test_dry_run_touches_nothing(self, capsys):
        # A runner that would explode if called — proves dry-run calls nothing.
        def _explode(host, command):  # pragma: no cover - must never run
            raise AssertionError("runner must not be called during --dry-run")

        rc = main(["--dry-run", "--hosts", "marvin,trillian", "--", "true"], runner=_explode)
        out = capsys.readouterr().out
        assert rc == 0
        assert "[DRY RUN]" in out
        assert "marvin" in out
        assert "trillian" in out
        assert "true" in out

    def test_dry_run_default_command(self, capsys):
        rc = main(["--dry-run", "--hosts", "marvin"])
        out = capsys.readouterr().out
        assert rc == 0
        assert DEFAULT_COMMAND in out

    def test_main_all_pass_with_injected_runner(self, capsys):
        rc = main(
            ["--hosts", "a,b", "--", "true"],
            runner=_fake_runner({"a": (0, "ok"), "b": (0, "ok")}),
        )
        out = capsys.readouterr().out
        assert rc == 0
        assert "OVERALL: PASS" in out

    def test_main_failure_nonzero_exit(self, capsys):
        rc = main(
            ["--hosts", "a,b", "--", "false"],
            runner=_fake_runner({"a": (0, "ok"), "b": (1, "fail-tail")}),
        )
        out = capsys.readouterr().out
        assert rc == 1
        assert "OVERALL: FAIL" in out
        assert "fail-tail" in out  # tail streamed via progress callback

    def test_main_unreachable_nonzero_exit(self, capsys):
        rc = main(
            ["--hosts", "a", "--", "true"],
            runner=_fake_runner({"a": (UNREACHABLE_EXIT, "no route")}),
        )
        assert rc == 1
        assert "UNREACHABLE" in capsys.readouterr().out

    def test_main_default_hosts(self, capsys):
        seen = []

        def _runner(host, command):
            seen.append(host)
            return (0, "ok")

        rc = main(["--", "true"], runner=_runner)
        assert rc == 0
        assert seen == list(DEFAULT_HOSTS)


# ── Subprocess tests exercising the bash wrapper end-to-end (no real SSH) ──────
#
# These run `scripts/multi-host-test.sh` as a real process. A fake `ssh` is
# placed first on PATH so nothing ever leaves the machine:
#   * --dry-run must NOT invoke ssh at all (a poison ssh that would fail if run).
#   * a non-dry run drives the fake ssh to return controlled exit codes and
#     asserts the aggregated overall exit code through the wrapper.

REPO_ROOT = Path(__file__).resolve().parents[2]
WRAPPER = REPO_ROOT / "scripts" / "multi-host-test.sh"


def _write_exec(path: Path, body: str) -> None:
    path.write_text(body)
    path.chmod(path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


def _run_wrapper(args, fake_bin: Path, extra_env=None):
    env = os.environ.copy()
    env["PATH"] = f"{fake_bin}{os.pathsep}{env['PATH']}"
    env["PYTHON"] = sys.executable
    if extra_env:
        env.update(extra_env)
    return subprocess.run(
        ["bash", str(WRAPPER), *args],
        capture_output=True,
        text=True,
        env=env,
        cwd=str(REPO_ROOT),
        check=False,
    )


class TestWrapperSubprocess:
    def test_wrapper_dry_run_never_calls_ssh(self, tmp_path):
        # Poison ssh: exits non-zero and leaves a marker file if ever invoked.
        marker = tmp_path / "ssh-was-called"
        poison = tmp_path / "ssh"
        _write_exec(poison, f'#!/usr/bin/env bash\ntouch "{marker}"\nexit 1\n')

        proc = _run_wrapper(["--hosts", "marvin,trillian", "--dry-run", "--", "uptime"], tmp_path)
        assert proc.returncode == 0, proc.stderr
        assert "[DRY RUN]" in proc.stdout
        assert "marvin" in proc.stdout and "trillian" in proc.stdout
        assert not marker.exists(), "ssh must NOT be invoked during --dry-run"

    def test_wrapper_all_pass(self, tmp_path):
        # Fake ssh always succeeds.
        fake = tmp_path / "ssh"
        _write_exec(fake, '#!/usr/bin/env bash\necho "remote ok"\nexit 0\n')
        proc = _run_wrapper(["--hosts", "marvin,trillian", "--", "true"], tmp_path)
        assert proc.returncode == 0, proc.stderr
        assert "OVERALL: PASS" in proc.stdout

    def test_wrapper_mixed_exit_codes_fail(self, tmp_path):
        # Fake ssh: fail for 'trillian', unreachable (255) for 'raspberrypi'.
        fake = tmp_path / "ssh"
        _write_exec(
            fake,
            "#!/usr/bin/env bash\n"
            'target="${@: -2:1}"\n'  # second-to-last arg is user@host
            'case "$target" in\n'
            "  *trillian) echo boom; exit 1 ;;\n"
            "  *raspberrypi) echo unreachable; exit 255 ;;\n"
            "  *) echo ok; exit 0 ;;\n"
            "esac\n",
        )
        proc = _run_wrapper(["--hosts", "marvin,trillian,raspberrypi", "--", "true"], tmp_path)
        assert proc.returncode == 1, proc.stdout + proc.stderr
        assert "OVERALL: FAIL" in proc.stdout
        assert "Passed: 1" in proc.stdout
        assert "Failed: 1" in proc.stdout
        assert "Unreachable: 1" in proc.stdout

    def test_wrapper_env_host_override(self, tmp_path):
        fake = tmp_path / "ssh"
        _write_exec(fake, "#!/usr/bin/env bash\nexit 0\n")
        proc = _run_wrapper(["--dry-run"], tmp_path, extra_env={"MULTI_HOST_HOSTS": "onlyhost"})
        assert proc.returncode == 0, proc.stderr
        assert "onlyhost" in proc.stdout
