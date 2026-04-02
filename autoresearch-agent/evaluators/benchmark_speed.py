#!/usr/bin/env python3
"""Measure execution speed of a target function or command.
DO NOT MODIFY after experiment starts — this is the fixed evaluator.

SECURITY: COMMAND must be provided as a list (e.g., ["python", "src/module.py"]),
not a string. This prevents shell injection vulnerabilities.
"""

import statistics
import subprocess
import sys
import time

# --- CONFIGURE THESE ---
# MUST be a list, not a string (SECURITY: prevents shell injection)
COMMAND = ["python", "src/module.py"]  # Command to benchmark as LIST
RUNS = 5                          # Number of runs
WARMUP = 1                        # Warmup runs (not counted)
# --- END CONFIG ---

def run_benchmark(cmd_list, timeout=120):
    """Run command as list with shell=False for security."""
    if not isinstance(cmd_list, list):
        print(f"ERROR: COMMAND must be a list, got: {type(cmd_list)}", file=sys.stderr)
        print("SECURITY: String commands with shell=True are not allowed.", file=sys.stderr)
        print('Use ["python", "script.py"] instead of "python script.py"', file=sys.stderr)
        sys.exit(1)
    return subprocess.run(cmd_list, shell=False, capture_output=True, timeout=timeout)

times = []

# Warmup
for _ in range(WARMUP):
    run_benchmark(COMMAND)

# Benchmark
for i in range(RUNS):
    t0 = time.perf_counter()
    result = run_benchmark(COMMAND)
    elapsed = (time.perf_counter() - t0) * 1000  # ms

    if result.returncode != 0:
        print(f"Run {i+1} failed (exit {result.returncode})", file=sys.stderr)
        print(f"stderr: {result.stderr.decode()[:200]}", file=sys.stderr)
        sys.exit(1)

    times.append(elapsed)

p50 = statistics.median(times)
p95 = sorted(times)[int(len(times) * 0.95)] if len(times) >= 5 else max(times)

print(f"p50_ms: {p50:.2f}")
print(f"p95_ms: {p95:.2f}")
print(f"runs: {RUNS}")
