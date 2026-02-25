#!/usr/bin/env python3
import re

# Read the file
with open("gateway/security/file_sandbox.py", "r") as f:
    content = f.read()

# Add a new method to detect traversal patterns before path resolution
traversal_detection_method = '''    def _detect_raw_traversal(self, path: str) -> str:
        """Detect path traversal attempts in raw input before normalization."""
        # Detect double-dot patterns (including double-encoded)
        if re.search(r'\.\.+[/\\]', path) or re.search(r'[/\\]\.\.+', path):
            return "path traversal sequence detected"
        
        # Detect Windows-style traversal with backslashes  
        if '\\\\' in path or (path.count('\\\\') >= 2 and ('system32' in path.lower() or 'windows' in path.lower())):
            return "Windows-style path traversal detected"
            
        # Detect encoded traversal patterns
        if '....//....' in path or '....//' in path:
            return "double-encoded traversal detected"
            
        return ""
'''

# Find where to insert the method (before _check method)
check_method_start = content.find("    def _check(")
if check_method_start != -1:
    # Insert the new method before _check
    content = content[:check_method_start] + traversal_detection_method + "\n" + content[check_method_start:]
    
    # Now modify the _check method to use the new detection
    old_flags_init = "        flags: list[str] = []"
    new_flags_init = '''        flags: list[str] = []

        # Pre-normalization traversal detection
        raw_traversal = self._detect_raw_traversal(path)
        if raw_traversal:
            flags.append(raw_traversal)'''
    
    content = content.replace(old_flags_init, new_flags_init)

# Write back
with open("gateway/security/file_sandbox.py", "w") as f:
    f.write(content)

print("Added pre-normalization traversal detection to FileSandbox")