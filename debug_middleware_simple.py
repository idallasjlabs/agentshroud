#!/usr/bin/env python3
import tempfile
from pathlib import Path

# Set up test environment similar to the failing test  
temp_dir = Path(tempfile.mkdtemp())
print(f"Temp dir: {temp_dir}")

# Create other user's workspace (simulates the test)
other_user_workspace = temp_dir / "users" / "other_user" / "workspace"
other_user_workspace.mkdir(parents=True)  
other_user_file = other_user_workspace / "secret.txt"
other_user_file.write_text("Other user's secret data")

# Create user_123's workspace
user_workspace = temp_dir / "users" / "user_123" / "workspace"
user_workspace.mkdir(parents=True)

print(f"User 123 workspace: {user_workspace}")
print(f"Other user file: {other_user_file}")

# Test the path checking logic (simulate the _is_path_allowed_for_user method)
def check_path_allowed(file_path, user_workspace_path):
    try:
        # Convert to absolute paths for comparison
        file_path_abs = str(Path(file_path).resolve())
        user_workspace_abs = str(Path(user_workspace_path).resolve())
        
        print(f"File path absolute: {file_path_abs}")
        print(f"User workspace absolute: {user_workspace_abs}")
        
        # Allow access to user's own workspace
        if file_path_abs.startswith(user_workspace_abs):
            print("  → File is in user's own workspace: ALLOWED")
            return True
        
        # Allow access to shared resources (read-only)
        shared_path = str(Path("/home/node/.openclaw/workspace/shared").resolve())
        if file_path_abs.startswith(shared_path):
            print(f"  → File is in shared path ({shared_path}): ALLOWED") 
            return True
        
        # Allow access to common system paths (read-only)
        allowed_system_paths = ["/tmp", "/proc/meminfo", "/proc/cpuinfo", "/etc/os-release"]
        for sys_path in allowed_system_paths:
            if file_path_abs.startswith(sys_path):
                print(f"  → File matches system path {sys_path}: ALLOWED")
                return True
                
        print("  → File not in any allowed path: DENIED")
        return False
        
    except Exception as e:
        print(f"  → Error: {e}")
        return False

result = check_path_allowed(str(other_user_file), str(user_workspace))
print(f"\nFinal result: {result}")