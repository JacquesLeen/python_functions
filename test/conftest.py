"""Pytest configuration."""

import sys
from pathlib import Path

# Get the absolute path to src directory
src_path = Path(__file__).parent.parent / "src"
print(f"DEBUG: src_path = {src_path}")
print(f"DEBUG: src_path exists = {src_path.exists()}")

if src_path.exists():
    sys.path.insert(0, str(src_path))
    print(f"DEBUG: Added {src_path} to sys.path")
else:
    print(f"ERROR: src directory not found at {src_path}")
    raise FileNotFoundError(f"src directory not found at {src_path}")
