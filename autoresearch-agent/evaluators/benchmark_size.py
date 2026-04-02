#!/usr/bin/env python3
"""Measure file, bundle, or Docker image size.
DO NOT MODIFY after experiment starts — this is the fixed evaluator.

SECURITY: Commands must be provided as lists (e.g., ["npm", "run", "build"]),
not strings. This prevents shell injection vulnerabilities.
"""

import os
import subprocess
import sys

# --- CONFIGURE ONE OF THESE ---
# Option 1: File size
TARGET_FILE = "dist/main.js"

# Option 2: Directory size (uncomment to use)
# TARGET_DIR = "dist/"

# Option 3: Docker image (uncomment to use)
# DOCKER_IMAGE = "myapp:latest"
# DOCKER_BUILD_CMD = ["docker", "build", "-t", "myapp:latest", "."]

# Option 4: Build first, then measure (uncomment to use)
# BUILD_CMD = ["npm", "run", "build"]  # MUST be a list, not string
# --- END CONFIG ---

def run_cmd(cmd_list, timeout=60):
    """Run command as list with shell=False for security."""
    if not isinstance(cmd_list, list):
        print(f"ERROR: Command must be a list, got: {type(cmd_list)}", file=sys.stderr)
        print("SECURITY: String commands with shell=True are not allowed.", file=sys.stderr)
        sys.exit(1)
    return subprocess.run(cmd_list, shell=False, capture_output=True, timeout=timeout)

# Build if needed
if "BUILD_CMD" in dir() or "BUILD_CMD" in globals():
    result = run_cmd(BUILD_CMD, timeout=300)
    if result.returncode != 0:
        print(f"Build failed: {result.stderr.decode()[:200]}", file=sys.stderr)
        sys.exit(1)

# Measure
if "DOCKER_IMAGE" in dir() or "DOCKER_IMAGE" in globals():
    if "DOCKER_BUILD_CMD" in dir():
        run_cmd(DOCKER_BUILD_CMD, timeout=300)
    result = subprocess.run(
        ["docker", "image", "inspect", DOCKER_IMAGE, "--format", "{{.Size}}"],
        shell=False,
        capture_output=True,
        text=True
    )
    try:
        size_bytes = int(result.stdout.strip())
    except ValueError:
        print(f"Could not parse size from: {result.stdout[:100]}", file=sys.stderr)
        sys.exit(1)
elif "TARGET_DIR" in dir() or "TARGET_DIR" in globals():
    size_bytes = sum(
        os.path.getsize(os.path.join(dp, f))
        for dp, _, fns in os.walk(TARGET_DIR) for f in fns
    )
elif os.path.exists(TARGET_FILE):
    size_bytes = os.path.getsize(TARGET_FILE)
else:
    print(f"Target not found: {TARGET_FILE}", file=sys.stderr)
    sys.exit(1)

size_kb = size_bytes / 1024
size_mb = size_bytes / (1024 * 1024)

print(f"size_bytes: {size_bytes}")
print(f"size_kb: {size_kb:.1f}")
print(f"size_mb: {size_mb:.2f}")
