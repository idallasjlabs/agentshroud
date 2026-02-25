#!/usr/bin/env python3
import re

# Read the file
with open("gateway/security/path_isolation.py", "r") as f:
    content = f.read()

# Find and replace the problematic section
old_pattern = r"""                    # Don't rewrite if it's already in an agentshroud subdirectory
                    if relative_path\.startswith\('agentshroud' \+ os\.sep\):
                        return path"""

new_code = """                    # Check if path is already in the user's namespace
                    user_temp_dir = self._get_user_temp_dir(user_id)
                    if abs_path.startswith(user_temp_dir + os.sep) or abs_path == user_temp_dir:
                        return abs_path"""

# Replace using regex
content = re.sub(old_pattern, new_code, content, flags=re.MULTILINE)

# Write back
with open("gateway/security/path_isolation.py", "w") as f:
    f.write(content)

print("Fixed path isolation double-rewrite issue")