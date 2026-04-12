#!/usr/bin/env python3
"""Measure build/compile time.
DO NOT MODIFY after experiment starts — this is the fixed evaluator.

SECURITY: Commands must be provided as lists (e.g., ["npm", "run", "build"]),
not strings. This prevents shell injection vulnerabilities.
"""

import subprocess
import sys
import time
import statistics

# --- CONFIGURE THESE ---
# MUST be lists, not strings (SECURITY: prevents shell injection)
BUILD_CMD = ["npm", "run", "build"]    # or: ["docker", "build", "-t", "test", "."]
CLEAN_CMD = []                         # optional: ["npm", "run", "clean"]
RUNS = 3                               # Number of builds to average
# --- END CONFIG ---

def run_cmd(cmd_list, timeout=600):
    """Run command as list with shell=False for security."""
    if not cmd_list:
        return None
    if not isinstance(cmd_list, list):
        print(f"ERROR: Command must be a list, got: {type(cmd_list)}", file=sys.stderr)
        print("SECURITY: String commands with shell=True are not allowed.", file=sys.stderr)
        print('Use ["npm", "run", "build"] instead of "npm run build"', file=sys.stderr)
        sys.exit(1)
    return subprocess.run(cmd_list, shell=False, capture_output=True, timeout=timeout)

times = []

for i in range(RUNS):
    # Clean if configured
    if CLEAN_CMD:
        run_cmd(CLEAN_CMD, timeout=60)

    t0 = time.perf_counter()
    result = run_cmd(BUILD_CMD, timeout=600)
    elapsed = time.perf_counter() - t0

    if result is None or result.returncode != 0:
        print(f"Build {i+1} failed", file=sys.stderr)
        if result:
            print(f"stderr: {result.stderr.decode()[:200]}", file=sys.stderr)
        sys.exit(1)

    times.append(elapsed)

avg = statistics.mean(times)
median = statistics.median(times)

print(f"build_seconds: {median:.2f}")
print(f"build_avg: {avg:.2f}")
print(f"runs: {RUNS}")
