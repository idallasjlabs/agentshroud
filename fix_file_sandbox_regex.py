#!/usr/bin/env python3

# Read the file
with open("gateway/security/file_sandbox.py", "r") as f:
    content = f.read()

# Fix the regex patterns
old_method = '''    def _detect_raw_traversal(self, path: str) -> str:
        """Detect path traversal attempts in raw input before normalization."""
        # Detect double-dot patterns (including double-encoded)
        if re.search(r'\.\.+[/\]', path) or re.search(r'[/\]\.\.+', path):
            return "path traversal sequence detected"
        
        # Detect Windows-style traversal with backslashes  
        if '\\\\' in path or (path.count('\\\\') >= 2 and ('system32' in path.lower() or 'windows' in path.lower())):
            return "Windows-style path traversal detected"
            
        # Detect encoded traversal patterns
        if '....//....' in path or '....//' in path:
            return "double-encoded traversal detected"
            
        return ""'''

new_method = '''    def _detect_raw_traversal(self, path: str) -> str:
        """Detect path traversal attempts in raw input before normalization."""
        # Detect double-dot patterns (including double-encoded)
        if re.search(r'\.\.+[/\\\\]', path) or re.search(r'[/\\\\]\.\.+', path):
            return "path traversal sequence detected"
        
        # Detect Windows-style traversal with backslashes  
        if '\\\\' in path and ('system32' in path.lower() or 'windows' in path.lower()):
            return "Windows-style path traversal detected"
            
        # Detect encoded traversal patterns
        if '....//....' in path or '....//' in path:
            return "double-encoded traversal detected"
            
        return ""'''

content = content.replace(old_method, new_method)

# Write back
with open("gateway/security/file_sandbox.py", "w") as f:
    f.write(content)

print("Fixed regex patterns in traversal detection")