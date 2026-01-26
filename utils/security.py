# utils/security.py
import re

def validate_code_safety(code):
    # Blacklist dangerous modules and functions
    forbidden = [
        'import os', 'import sys', 'import subprocess', 'import shutil',
        'open(', 'eval(', 'exec(', 'getattr', 'setattr', '__import__',
        '__subclasses__', 'write(', '.system(', 'pickle'
    ]
    
    for word in forbidden:
        if word in code.lower():
            return False, f"Security Block: Use of '{word}' is restricted."
    
    # Check for excessive length to prevent memory attacks
    if len(code) > 2000:
        return False, "Security Block: Code is too long."
        
    return True, ""