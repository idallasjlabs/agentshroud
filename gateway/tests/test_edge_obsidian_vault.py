# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Inbound MCP Edge — Obsidian vault facade (vault_* tools, threats T7/T8).

The Obsidian Local REST API is replaced by an in-memory fake behind an injected
httpx transport: no network. Every write path is pinned, the shared write guard
is exercised directly, and the guardrail table is checked end to end.
"""

import json
from datetime import date
from types import SimpleNamespace
from urllib.parse import unquote

import httpx
import jsonschema
import pytest

from gateway.inbound_edge import facades as f
from gateway.inbound_edge.descriptors import (
    PERSONAL_PROJECTS,
    TOOL_DESCRIPTORS,
    VAULT_TOOL_DESCRIPTORS,
    WORK_PROJECTS,
)
from gateway.security.instruction_envelope import (
    UNTRUSTED_OPEN,
    EnvelopeSigner,
    unwrap_untrusted,
)

BEARER = "fixture"
SIGNER = EnvelopeSigner(key=b"v" * 32)
CALL = SimpleNamespace(request_id="r-1", principal=SimpleNamespace(vendor="claude-duet"))
VALIDATORS = {
    n: jsonschema.Draft202012Validator(d["inputSchema"]) for n, d in VAULT_TOOL_DESCRIPTORS.items()
}
WRITE_TOOLS = sorted(n for n, d in VAULT_TOOL_DESCRIPTORS.items() if d["access"] == "write")
READ_TOOLS = sorted(n for n, d in VAULT_TOOL_DESCRIPTORS.items() if d["access"] == "read")
HUB = "10 Personal/agentshroud/agentshroud.md"
SYNC = "10 Personal/agentshroud/agentshroud.sync.md"


class FakeVault:
    """Minimal Obsidian Local REST API: GET/PUT/DELETE/MOVE /vault/*, POST /search/simple/."""

    def __init__(self, files=None):
        self.files = dict(files or {})
        self.requests = []
        self.writes = []  # (method, path) for every mutating call
        self.fail_move_after = None
        self.force_status = {}

    @staticmethod
    def _path(request):
        raw = request.url.raw_path.decode().split("?", 1)[0]
        assert raw.startswith("/vault/")
        return unquote(raw[len("/vault/") :])

    def _listing(self, folder):
        prefix = folder + "/" if folder else ""
        names = set()
        for path in self.files:
            if path.startswith(prefix):
                rest = path[len(prefix) :]
                names.add(rest.split("/", 1)[0] + "/" if "/" in rest else rest)
        return sorted(names)

    def __call__(self, request):
        self.requests.append(request)
        assert request.headers["authorization"] == f"Bearer {BEARER}"
        if request.url.path == "/search/simple/":
            q = request.url.params["query"].lower()
            hits = [
                {"filename": p, "score": 1, "matches": [{"context": c[:50], "match": {}}]}
                for p, c in sorted(self.files.items())
                if q in c.lower()
            ]
            hits.append({"filename": ".obsidian/workspace.json", "matches": [{"context": q}]})
            hits.append({"filename": 42})
            return httpx.Response(200, json=hits)
        path = self._path(request)
        forced = self.force_status.get((request.method, path))
        if forced:
            return httpx.Response(forced)
        if request.method == "GET":
            if path.endswith("/"):
                listing = self._listing(path.rstrip("/"))
                return (
                    httpx.Response(200, json={"files": listing}) if listing else httpx.Response(404)
                )
            if path not in self.files:
                return httpx.Response(404)
            return httpx.Response(
                200, text=self.files[path], headers={"ETag": f"v{len(self.files[path])}"}
            )
        self.writes.append((request.method, path))
        if request.method == "PUT":
            if request.headers.get("if-none-match") == "*" and path in self.files:
                return httpx.Response(412)
            match = request.headers.get("if-match")
            if match and path in self.files and match != f"v{len(self.files[path])}":
                return httpx.Response(412)
            self.files[path] = request.content.decode()
            return httpx.Response(204)
        if request.method == "DELETE":
            if path not in self.files:
                return httpx.Response(404)
            del self.files[path]
            return httpx.Response(204)
        if request.method == "MOVE":
            moves = sum(1 for m, _ in self.writes if m == "MOVE")
            if self.fail_move_after is not None and moves > self.fail_move_after:
                return httpx.Response(409)
            dest = unquote(request.headers["destination"])
            assert request.headers["allow-overwrite"] == "false"
            if dest in self.files:
                return httpx.Response(409)
            self.files[dest] = self.files.pop(path)
            return httpx.Response(204)
        return httpx.Response(405)


def _vault(fake, today=date(2026, 11, 25)):
    return f.ObsidianVault(
        "http://host.docker.internal:27123/",
        BEARER,
        SIGNER,
        transport=httpx.MockTransport(fake),
        today=lambda: today,
    )


async def _run(vault, tool, **args):
    errors = list(VALIDATORS[tool].iter_errors(args))
    assert not errors, errors[0].message
    return await vault.facades()[tool].run(args, CALL)


def _base_files():
    return {
        "00 Inbox/Inbox.md": "# Inbox\n\n- [ ] call bank\n",
        "01 GTD/Personal/Next.md": "- [ ] renew passport 📅 2026-11-20\n- [x] done thing\n",
        "01 GTD/Work/Next.md": "- [ ] ship report 📅 2026-11-25\n",
        HUB: "# agentshroud\n\n## Tasks\n\n- [ ] old task\n\n## Notes\n\nhello\n",
        SYNC: "- [ ] synced issue 📅 2026-12-01\n",
        "20 Work/azure-arc/azure-arc.md": "# azure-arc\n",
        "90 Templates/Daily.md": "template",
        "Home.md": "home",
        "30 Resources/Paper.md": "alpha beta",
    }


# ── descriptors: shape, enums, T7/T8 ──────────────────────────────────────


def test_eleven_vault_tools_four_read_seven_write():
    assert len(READ_TOOLS) == 4 and len(WRITE_TOOLS) == 7
    assert set(VAULT_TOOL_DESCRIPTORS) <= set(TOOL_DESCRIPTORS)
    for name in WRITE_TOOLS:
        assert TOOL_DESCRIPTORS[name]["write_budget"] == "vault_writes"
        assert "approval" in TOOL_DESCRIPTORS[name]["description"]


def test_project_enum_matches_owner_list():
    enum = VAULT_TOOL_DESCRIPTORS["vault_project"]["inputSchema"]["properties"]["project"]["enum"]
    assert enum == [*PERSONAL_PROJECTS, *WORK_PROJECTS]
    assert len(PERSONAL_PROJECTS) == 14 and len(WORK_PROJECTS) == 5


@pytest.mark.parametrize("tool", ["vault_project", "vault_project_archive"])
def test_slug_outside_enum_refused_by_schema(tool):
    for slug in ("../01 GTD", "agentshroud/../x", "AgentShroud", "secret-project", ""):
        assert not VALIDATORS[tool].is_valid({"project": slug})


@pytest.mark.parametrize(
    "title",
    [
        "../Home",
        "a/b",
        "..",
        "x..y",
        ".obsidian",
        "status.sync",
        "status.SYNC",
        "trailing ",
        "trailing.",
        "a\nb",
        "x" * 121,
        "back\\slash",
        "per%2fcent",
        "",
    ],
)
def test_title_traversal_refused_by_schema_and_facade(title):
    assert not VALIDATORS["vault_read"].is_valid({"folder": "root", "title": title})
    with pytest.raises(f.VaultPathError):
        f._vault_title(title)


def test_valid_titles_accepted():
    for title in ("Weekly review (Nov)", "2026-11-25", "plan_v2.final", "A"):
        assert VALIDATORS["vault_note_create"].is_valid(
            {"folder": "00 Inbox", "title": title, "body": "x"}
        )
        assert f._vault_title(title) == title


# ── the shared write guard ─────────────────────────────────────────────────


@pytest.mark.parametrize(
    "path",
    [
        "10 Personal/pke/pke.sync.md",
        "10 Personal/pke/PKE.SYNC.MD",
        "99 Archive/x/x.sync.md",
        "01 GTD/Personal/Next.md",
        "01 gtd/Work/Next.md",
        "90 Templates/Daily.md",
        ".obsidian/plugins/x/data.json",
        "10 Personal/.obsidian/app.json",
        "Home.md",
        "home.md",
        "Start here.md",
        "../outside.md",
        "/etc/passwd",
        "00 Inbox//x.md",
        "00 Inbox/./x.md",
        "00 Inbox\\x.md",
        "00 Inbox/x\x00.md",
        "",
        None,
        "x" * 600,
    ],
)
def test_shared_write_guard_refuses(path):
    with pytest.raises(f.VaultPathError):
        f.assert_vault_writable(path)


def test_shared_write_guard_allows_expected_targets():
    for path in (
        "00 Inbox/Inbox.md",
        HUB,
        "40 Journal/Daily/2026-11-25.md",
        "30 Resources/Paper.md",
        "99 Archive/pke/pke.md",
    ):
        assert f.assert_vault_writable(path) == path


def test_read_guard_refuses_hidden_and_traversal():
    for path in (".obsidian/app.json", "x/.trash/y.md", "../x.md", "a//b"):
        with pytest.raises(f.VaultPathError):
            f.assert_vault_readable(path)


def test_folder_pinning_helpers():
    assert f._vault_in("00 Inbox", "00 Inbox/a.md") == "00 Inbox/a.md"
    assert f._vault_in("", "Home.md") == "Home.md"
    for folder, path in (
        ("00 Inbox", "00 Inbox/sub/a.md"),
        ("00 Inbox", "30 Resources/a.md"),
        ("", "00 Inbox/a.md"),
        ("00 Inbox", "00 Inbox/"),
    ):
        with pytest.raises(f.VaultPathError):
            f._vault_in(folder, path)
    with pytest.raises(f.VaultPathError):
        f._vault_project("not-a-project")
    with pytest.raises(f.VaultPathError):
        f._vault_project(None)
    for bad in ("2026-02-31", "2026-1-1", None):
        with pytest.raises(f.VaultPathError):
            f._vault_date(bad)


def test_inert_neutralises_active_content():
    text = "```dataviewjs\nx\n``` `$= dv.x` <% tp.x %> %% ![img](https://e/x) <iframe>"
    out = f._vault_inert(text)
    assert "`" not in out and "<" not in out and "%%" not in out and "![" not in out


def test_insert_under_heading_variants():
    assert f._insert_under_heading("", "Tasks", "- [ ] a") == "## Tasks\n\n- [ ] a\n"
    out = f._insert_under_heading("# t\n\n## Tasks\n\n- [ ] x\n\n## Notes\n\nn\n", "Tasks", "B")
    assert out == "# t\n\n## Tasks\n\n- [ ] x\nB\n\n## Notes\n\nn\n"
    out = f._insert_under_heading("# t\n## Grooming\nold", "Grooming", "B")
    assert out == "# t\n## Grooming\noldB\n".replace("oldB", "old\nB")
    out = f._insert_under_heading("# t\n", "Notes", "B")
    assert out == "# t\n\n## Notes\n\nB\n"


def test_open_tasks_skips_comment_blocks():
    text = "- [ ] real\n%%\n- [ ] hidden in comment\n%%\n  - [ ] nested\n- [x] done\n"
    assert f._open_tasks(text) == ["- [ ] real", "- [ ] nested"]


# ── reads ──────────────────────────────────────────────────────────────────


async def test_search_drops_obsidian_hits_and_caps():
    fake = FakeVault({**_base_files(), "30 Resources/B.md": "alpha two"})
    out = await _run(_vault(fake), "vault_search", query="alpha", max_results=5)
    assert {r["title"] for r in out["results"]} == {"Paper", "B"}
    assert all(not r["folder"].startswith(".") for r in out["results"])
    assert fake.requests[0].url.params["maxResults"] == "10"
    out = await _run(_vault(fake), "vault_search", query="alpha", max_results=5)
    fake.files["Root note.md"] = "alpha"
    out = await _run(_vault(fake), "vault_search", query="alpha", max_results=5)
    assert {"title": "Root note", "folder": "root", "snippet": "alpha"} in out["results"]
    assert not fake.writes


async def test_search_respects_limit_and_odd_payloads():
    fake = FakeVault({f"30 Resources/n{i}.md": "zeta" for i in range(30)})
    out = await _run(_vault(fake), "vault_search", query="zeta", max_results=5)
    assert len(out["results"]) == 5

    def odd(request):
        return httpx.Response(200, json={"not": "a list"})

    vault = f.ObsidianVault("http://h:1", BEARER, SIGNER, transport=httpx.MockTransport(odd))
    assert (await vault.run_tool("vault_search", {"query": "x"}, CALL))["results"] == []

    def weird(request):
        return httpx.Response(200, json=[{"filename": "a.md", "matches": ["bad"]}])

    vault = f.ObsidianVault("http://h:1", BEARER, SIGNER, transport=httpx.MockTransport(weird))
    out = await vault.run_tool("vault_search", {"query": "x"}, CALL)
    assert out["results"] == [{"title": "a", "folder": "root", "snippet": ""}]


async def test_read_builds_path_from_enum_and_title():
    fake = FakeVault(_base_files())
    v = _vault(fake)
    out = await _run(v, "vault_read", folder="root", title="Home")
    assert out == {"path": "Home.md", "found": True, "content": "home", "truncated": False}
    out = await _run(v, "vault_read", folder="01 GTD/Work", title="Next")
    assert out["path"] == "01 GTD/Work/Next.md" and out["found"]
    out = await _run(v, "vault_read", folder="99 Archive", title="Missing")
    assert out == {"path": "99 Archive/Missing.md", "found": False}
    assert [unquote(r.url.raw_path.decode()) for r in fake.requests] == [
        "/vault/Home.md",
        "/vault/01 GTD/Work/Next.md",
        "/vault/99 Archive/Missing.md",
    ]
    with pytest.raises(f.VaultPathError):
        await v.run_tool("vault_read", {"folder": ".obsidian", "title": "x"}, CALL)
    with pytest.raises(f.VaultPathError):
        await v.run_tool("vault_read", {"folder": "root", "title": "../x"}, CALL)
    assert not fake.writes


async def test_read_truncates_large_notes():
    fake = FakeVault({"30 Resources/Big.md": "x" * (f.VAULT_NOTE_MAX_CHARS + 5)})
    out = await _run(_vault(fake), "vault_read", folder="30 Resources", title="Big")
    assert out["truncated"] and len(out["content"]) == f.VAULT_NOTE_MAX_CHARS


async def test_project_hub_sync_both():
    fake = FakeVault(_base_files())
    v = _vault(fake)
    out = await _run(v, "vault_project", project="agentshroud", part="both")
    assert out["hub"]["path"] == HUB and out["sync"]["path"] == SYNC
    assert out["sync"]["content"].startswith("- [ ] synced")
    out = await _run(v, "vault_project", project="azure-arc")
    assert out["hub"]["path"] == "20 Work/azure-arc/azure-arc.md" and "sync" not in out
    out = await _run(v, "vault_project", project="azure-arc", part="sync")
    assert out["sync"]["found"] is False and "hub" not in out
    with pytest.raises(f.VaultPathError):
        await v.run_tool("vault_project", {"project": "../../01 GTD"}, CALL)


async def test_tasks_scopes():
    fake = FakeVault(_base_files())
    v = _vault(fake)
    inbox = await _run(v, "vault_tasks", scope="inbox")
    assert [t["task"] for t in inbox["tasks"]] == ["- [ ] call bank"]
    personal = await _run(v, "vault_tasks", scope="personal")
    tasks = {t["task"] for t in personal["tasks"]}
    assert "- [ ] renew passport 📅 2026-11-20" in tasks and "- [ ] old task" in tasks
    assert "- [ ] synced issue 📅 2026-12-01" in tasks and "- [x] done thing" not in tasks
    work = await _run(v, "vault_tasks", scope="work")
    assert [t["task"] for t in work["tasks"]] == ["- [ ] ship report 📅 2026-11-25"]
    today = await _run(v, "vault_tasks", scope="today")
    assert [t["task"] for t in today["tasks"]] == ["- [ ] ship report 📅 2026-11-25"]
    assert today["today"] == "2026-11-25"
    overdue = await _run(v, "vault_tasks", scope="overdue")
    assert [t["task"] for t in overdue["tasks"]] == ["- [ ] renew passport 📅 2026-11-20"]
    assert overdue["tasks"][0] == {
        "task": "- [ ] renew passport 📅 2026-11-20",
        "title": "Next",
        "folder": "01 GTD/Personal",
    }
    assert not fake.writes


async def test_tasks_skip_bad_listing_names_and_truncate():
    files = {"00 Inbox/Big.md": "\n".join(f"- [ ] t{i}" for i in range(f.VAULT_TASKS_MAX + 9))}
    fake = FakeVault(files)
    out = await _run(_vault(fake), "vault_tasks", scope="inbox")
    assert out["truncated"] and len(out["tasks"]) == f.VAULT_TASKS_MAX

    def handler(request):
        if request.url.raw_path.endswith(b"/"):
            return httpx.Response(200, json={"files": [".hidden.md", "ok.md", "sub/", 7]})
        if b".hidden" in request.url.raw_path:
            raise AssertionError("hidden note must never be fetched")
        return httpx.Response(200, text="- [ ] fine\n")

    v = f.ObsidianVault("http://h:1", BEARER, SIGNER, transport=httpx.MockTransport(handler))
    out = await v.run_tool("vault_tasks", {"scope": "inbox"}, CALL)
    assert out["tasks"] == [{"task": "- [ ] fine", "title": "ok", "folder": "00 Inbox"}]


async def test_upstream_error_fails_closed():
    fake = FakeVault(_base_files())
    fake.force_status[("GET", HUB)] = 500
    with pytest.raises(f.VaultError):
        await _run(_vault(fake), "vault_project", project="agentshroud")


# ── writes: every path pinned, provenance, guardrails ──────────────────────


def _assert_wrapped(text, original):
    assert UNTRUSTED_OPEN in text
    start = text.index("[AgentShroud]")
    body, source = unwrap_untrusted(text[start:], SIGNER)
    assert source == "edge:claude-duet"
    assert body == f._vault_inert(original)


async def test_inbox_add_appends_wrapped_text():
    fake = FakeVault(_base_files())
    out = await _run(_vault(fake), "vault_inbox_add", text="buy milk\n`rm` <b>")
    assert out == {"ok": True, "path": "00 Inbox/Inbox.md", "result": "appended"}
    assert fake.writes == [("PUT", "00 Inbox/Inbox.md")]
    note = fake.files["00 Inbox/Inbox.md"]
    assert note.startswith("# Inbox\n\n- [ ] call bank\n\n")
    _assert_wrapped(note[note.index("[AgentShroud]") :].rstrip("\n"), "buy milk\n`rm` <b>")
    put = [r for r in fake.requests if r.method == "PUT"][0]
    assert put.headers["if-match"] == "v25"


async def test_inbox_add_creates_missing_inbox():
    fake = FakeVault({})
    out = await _run(_vault(fake), "vault_inbox_add", text="first")
    assert out["result"] == "created"
    assert fake.files["00 Inbox/Inbox.md"].startswith("# Inbox\n\n[AgentShroud]")
    put = [r for r in fake.requests if r.method == "PUT"][0]
    assert put.headers["if-none-match"] == "*"


async def test_append_conflict_fails_closed():
    fake = FakeVault(_base_files())
    fake.force_status[("PUT", "00 Inbox/Inbox.md")] = 412
    with pytest.raises(f.VaultError, match="changed"):
        await _run(_vault(fake), "vault_inbox_add", text="x")


@pytest.mark.parametrize(
    "folder", ["00 Inbox", "30 Resources", "40 Journal/Daily", "40 Journal/Weekly"]
)
async def test_note_create_pins_path_and_refuses_existing(folder):
    fake = FakeVault(_base_files())
    v = _vault(fake)
    out = await _run(v, "vault_note_create", folder=folder, title="New idea", body="body text")
    assert out == {"ok": True, "path": f"{folder}/New idea.md", "result": "created"}
    assert fake.writes == [("PUT", f"{folder}/New idea.md")]
    note = fake.files[f"{folder}/New idea.md"]
    assert note.startswith("# New idea\n\n")
    _assert_wrapped(note[len("# New idea\n\n") :].rstrip("\n"), "body text")
    again = await _run(v, "vault_note_create", folder=folder, title="New idea", body="other")
    assert again == {"ok": False, "path": f"{folder}/New idea.md", "error": "note already exists"}
    assert len(fake.writes) == 1


async def test_note_create_race_and_bad_folder():
    fake = FakeVault({})
    fake.force_status[("PUT", "00 Inbox/X.md")] = 412
    out = await _run(_vault(fake), "vault_note_create", folder="00 Inbox", title="X", body="b")
    assert out["error"] == "note already exists"
    for folder in ("01 GTD/Work", "90 Templates", "root", "99 Archive", "10 Personal"):
        assert not VALIDATORS["vault_note_create"].is_valid(
            {"folder": folder, "title": "X", "body": "b"}
        )
        with pytest.raises(f.VaultPathError):
            await _vault(fake).run_tool(
                "vault_note_create", {"folder": folder, "title": "X", "body": "b"}, CALL
            )


async def test_project_add_task_line_and_provenance():
    fake = FakeVault(_base_files())
    v = _vault(fake)
    out = await _run(
        v, "vault_project_add_task", project="agentshroud", task="Write  `tests`", due="2026-12-01"
    )
    line = "- [ ] Write ˋtestsˋ 📅 2026-12-01 #agentshroud"
    assert out == {
        "ok": True,
        "path": HUB,
        "result": "appended",
        "heading": "Tasks",
        "task": line,
    }
    assert fake.writes == [("PUT", HUB)]
    hub = fake.files[HUB]
    tasks_section = hub.split("## Tasks", 1)[1].split("## Notes", 1)[0]
    assert tasks_section.startswith(f"\n\n- [ ] old task\n{line}\n%%\n[AgentShroud]")
    assert hub.endswith("## Notes\n\nhello\n")
    comment = tasks_section.split("%%\n", 1)[1].rsplit("\n%%", 1)[0]
    _assert_wrapped(comment, "Write  `tests`")
    # The provenance copy in the comment is never reported as a second open task.
    assert f._open_tasks(hub) == ["- [ ] old task", line]


async def test_project_add_task_without_due_and_work_project():
    fake = FakeVault(_base_files())
    out = await _run(_vault(fake), "vault_project_add_task", project="azure-arc", task="Renew")
    assert out["task"] == "- [ ] Renew #azure-arc"
    assert fake.writes == [("PUT", "20 Work/azure-arc/azure-arc.md")]
    assert "## Tasks\n\n- [ ] Renew #azure-arc\n%%" in fake.files["20 Work/azure-arc/azure-arc.md"]


async def test_project_writes_need_existing_hub():
    fake = FakeVault({})
    out = await _run(_vault(fake), "vault_project_append", project="pke", heading="Notes", text="x")
    assert out == {
        "ok": False,
        "path": "10 Personal/pke/pke.md",
        "error": "project hub note not found",
    }
    assert not fake.writes


@pytest.mark.parametrize("heading", ["Tasks", "Grooming", "Notes"])
async def test_project_append_only_touches_hub(heading):
    fake = FakeVault(_base_files())
    out = await _run(
        _vault(fake), "vault_project_append", project="agentshroud", heading=heading, text="note"
    )
    assert out["ok"] and out["heading"] == heading
    assert fake.writes == [("PUT", HUB)]
    assert fake.files[SYNC] == _base_files()[SYNC]
    assert f"## {heading}" in fake.files[HUB]


async def test_project_append_bad_heading_and_conflict():
    fake = FakeVault(_base_files())
    with pytest.raises(f.VaultPathError):
        await _vault(fake).run_tool(
            "vault_project_append", {"project": "agentshroud", "heading": "x", "text": "t"}, CALL
        )
    fake.force_status[("PUT", HUB)] = 412
    with pytest.raises(f.VaultError):
        await _run(
            _vault(fake), "vault_project_append", project="agentshroud", heading="Notes", text="t"
        )


async def test_journal_append_creates_then_appends():
    fake = FakeVault({})
    v = _vault(fake)
    first = await _run(v, "vault_journal_append", date="2026-11-25", text="morning")
    second = await _run(v, "vault_journal_append", date="2026-11-25", text="evening")
    assert first["result"] == "created" and second["result"] == "appended"
    assert fake.writes == [("PUT", "40 Journal/Daily/2026-11-25.md")] * 2
    note = fake.files["40 Journal/Daily/2026-11-25.md"]
    assert note.startswith("# 2026-11-25\n\n[AgentShroud]") and note.count("[AgentShroud]") == 2
    with pytest.raises(f.VaultPathError):
        await v.run_tool("vault_journal_append", {"date": "2026-02-30", "text": "x"}, CALL)


async def test_archive_moves_every_file_but_sync():
    files = {
        HUB: "hub",
        SYNC: "sync",
        "10 Personal/agentshroud/notes/a b.md": "a",
        "10 Personal/agentshroud/img.png": "png",
        "10 Personal/pke/pke.md": "other project",
    }
    fake = FakeVault(files)
    out = await _run(_vault(fake), "vault_project_archive", project="agentshroud")
    assert out["ok"] and out["archived_to"] == "99 Archive/agentshroud"
    assert out["left_in_place"] == [SYNC]
    assert sorted(fake.files) == sorted(
        [
            "99 Archive/agentshroud/agentshroud.md",
            "99 Archive/agentshroud/img.png",
            "99 Archive/agentshroud/notes/a b.md",
            SYNC,
            "10 Personal/pke/pke.md",
        ]
    )
    assert all(m == "MOVE" for m, _ in fake.writes)
    assert SYNC not in [p for _, p in fake.writes]


async def test_archive_refusals_and_partial_failure():
    fake = FakeVault({HUB: "h", "99 Archive/agentshroud/old.md": "x"})
    out = await _run(_vault(fake), "vault_project_archive", project="agentshroud")
    assert out == {"ok": False, "error": "99 Archive/agentshroud/ already exists"}
    assert not fake.writes

    fake = FakeVault({})
    out = await _run(_vault(fake), "vault_project_archive", project="agentshroud")
    assert out == {"ok": False, "error": "project folder not found or empty"}

    fake = FakeVault(
        {HUB: "h", "10 Personal/agentshroud/b.md": "b", "10 Personal/agentshroud/c.md": "c"}
    )
    fake.fail_move_after = 1
    out = await _run(_vault(fake), "vault_project_archive", project="agentshroud")
    assert out["ok"] is False and "upstream 409" in out["error"]
    assert out["moved"] == [HUB]
    assert out["not_moved"] == ["10 Personal/agentshroud/b.md", "10 Personal/agentshroud/c.md"]


async def test_archive_limits():
    def deep(request):
        return httpx.Response(200, json={"files": ["d/"]})

    v = f.ObsidianVault("http://h:1", BEARER, SIGNER, transport=httpx.MockTransport(deep))

    async def no_dest(client, folder):
        return [] if folder.startswith("99 Archive") else ["d/"]

    v._list = no_dest
    with pytest.raises(f.VaultError, match="deeply"):
        await v.run_tool("vault_project_archive", {"project": "pke"}, CALL)

    many = {f"10 Personal/pke/n{i}.md": "x" for i in range(f.VAULT_ARCHIVE_MAX_FILES + 1)}
    with pytest.raises(f.VaultError, match="too large"):
        await _run(_vault(FakeVault(many)), "vault_project_archive", project="pke")


async def test_archive_refuses_listed_traversal_names():
    def handler(request):
        raw = unquote(request.url.raw_path.decode())
        if raw.startswith("/vault/99 Archive"):
            return httpx.Response(404)
        return httpx.Response(200, json={"files": ["../../escape.md"]})

    v = f.ObsidianVault("http://h:1", BEARER, SIGNER, transport=httpx.MockTransport(handler))
    with pytest.raises(f.VaultPathError):
        await v.run_tool("vault_project_archive", {"project": "pke"}, CALL)


@pytest.mark.parametrize(
    "folder", ["00 Inbox", "30 Resources", "40 Journal/Daily", "40 Journal/Weekly"]
)
async def test_note_delete_pins_path(folder):
    fake = FakeVault({f"{folder}/Old.md": "x"})
    out = await _run(_vault(fake), "vault_note_delete", folder=folder, title="Old")
    assert out == {"ok": True, "path": f"{folder}/Old.md", "result": "deleted (to trash)"}
    assert fake.writes == [("DELETE", f"{folder}/Old.md")]
    delete = [r for r in fake.requests if r.method == "DELETE"][0]
    assert "permanent" not in delete.url.params
    out = await _run(_vault(fake), "vault_note_delete", folder=folder, title="Old")
    assert out["error"] == "note not found"


async def test_note_delete_never_reaches_protected_notes():
    fake = FakeVault(_base_files())
    v = _vault(fake)
    for folder, title in (
        ("01 GTD/Work", "Next"),
        ("90 Templates", "Daily"),
        ("root", "Home"),
        ("10 Personal/agentshroud", "agentshroud"),
    ):
        assert not VALIDATORS["vault_note_delete"].is_valid({"folder": folder, "title": title})
        with pytest.raises(f.VaultPathError):
            await v.run_tool("vault_note_delete", {"folder": folder, "title": title}, CALL)
    with pytest.raises(f.VaultPathError):
        await v.run_tool("vault_note_delete", {"folder": "00 Inbox", "title": "x.sync"}, CALL)
    assert not fake.writes


async def test_write_guard_blocks_a_buggy_builder(monkeypatch):
    """Defence in depth: even if a path builder returned a protected path, no write is sent."""
    fake = FakeVault(_base_files())
    monkeypatch.setattr(f, "_vault_in", lambda folder, path: SYNC)
    v = _vault(fake)
    for tool, args in (
        ("vault_inbox_add", {"text": "x"}),
        ("vault_note_create", {"folder": "00 Inbox", "title": "T", "body": "b"}),
        ("vault_project_append", {"project": "agentshroud", "heading": "Notes", "text": "x"}),
        ("vault_project_add_task", {"project": "agentshroud", "task": "x"}),
        ("vault_journal_append", {"date": "2026-11-25", "text": "x"}),
        ("vault_note_delete", {"folder": "00 Inbox", "title": "T"}),
    ):
        with pytest.raises(f.VaultPathError):
            await v.run_tool(tool, args, CALL)
    monkeypatch.setattr(f, "_vault_in", lambda folder, path: "01 GTD/Work/Next.md")
    with pytest.raises(f.VaultPathError):
        await v.run_tool("vault_inbox_add", {"text": "x"}, CALL)
    with pytest.raises(f.VaultPathError):
        await v._put(None, "01 GTD/Personal/Next.md", "x", None, True)
    assert not fake.writes
    assert fake.files[SYNC] == _base_files()[SYNC]


async def test_unknown_tool_and_client_settings():
    v = _vault(FakeVault({}))
    with pytest.raises(f.VaultPathError):
        await v.run_tool("vault_shell", {}, CALL)
    client = v._client()
    try:
        assert client.trust_env is False and client.follow_redirects is False
    finally:
        await client.aclose()
    tool = v.facades()["vault_search"]
    assert tool.target == "obsidian:tasks-and-projects" and tool.requires_local_agent is None


async def test_reads_never_write_and_writes_send_bearer_only_to_base():
    fake = FakeVault(_base_files())
    v = _vault(fake)
    for tool, args in (
        ("vault_search", {"query": "a"}),
        ("vault_read", {"folder": "root", "title": "Home"}),
        ("vault_project", {"project": "pke", "part": "both"}),
        ("vault_tasks", {"scope": "today"}),
    ):
        await _run(v, tool, **args)
    assert not fake.writes
    assert {r.url.host for r in fake.requests} == {"host.docker.internal"}
    assert {r.url.port for r in fake.requests} == {27123}
    json.dumps([str(r.url) for r in fake.requests])  # all URLs serialisable, no surprises
