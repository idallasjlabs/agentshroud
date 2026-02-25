import tempfile
import os
from gateway.security.path_isolation import PathIsolationManager, PathIsolationConfig

# Create a temporary directory for testing  
with tempfile.TemporaryDirectory() as temp_dir:
    config = PathIsolationConfig(
        base_temp_dir=os.path.join(temp_dir, "agentshroud"),
        isolated_paths=["/tmp", "/var/tmp"]
    )
    
    manager = PathIsolationManager(config)
    user_id = "test_user"
    manager.register_user_session(user_id)
    
    print(f"Temp dir: {temp_dir}")
    print(f"Base temp dir: {manager.config.base_temp_dir}")
    
    # Get user temp path
    own_path = manager.get_user_temp_path(user_id, "file.txt")
    print(f"Own path: {own_path}")
    print(f"Own path absolute: {os.path.abspath(own_path)}")
    
    # Test rewrite path
    result = manager.rewrite_path(own_path, user_id)
    print(f"Original path: {result.original_path}")
    print(f"Rewritten path: {result.rewritten_path}")
    print(f"Was rewritten: {result.was_rewritten}")
    print(f"Blocked: {result.blocked}")
    print(f"Reason: {result.reason}")
    
    # Debug the path checking logic
    abs_path = os.path.abspath(own_path)
    print(f"\nDebugging path logic:")
    print(f"abs_path: {abs_path}")
    
    for isolated_path in manager.config.isolated_paths:
        isolated_abs = os.path.abspath(isolated_path)
        print(f"Checking against isolated_path: {isolated_path} -> {isolated_abs}")
        
        if abs_path.startswith(isolated_abs):
            print(f"  Path starts with isolated path")
            try:
                relative_path = os.path.relpath(abs_path, isolated_abs)
                print(f"  Relative path: {relative_path}")
                print(f"  Starts with 'agentshroud/'?: {relative_path.startswith('agentshroud' + os.sep)}")
                if relative_path.startswith('agentshroud' + os.sep):
                    print(f"  Would return original path: {own_path}")
                else:
                    user_temp_dir = manager._get_user_temp_dir(user_id)
                    rewritten_path = os.path.join(user_temp_dir, relative_path)
                    print(f"  Would rewrite to: {rewritten_path}")
            except ValueError as e:
                print(f"  ValueError: {e}")
        else:
            print(f"  Path does NOT start with isolated path")