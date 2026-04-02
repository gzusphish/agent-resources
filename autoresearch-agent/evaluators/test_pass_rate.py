#!/usr/bin/env python3
"""Measure test suite pass rate.
DO NOT MODIFY after experiment starts — this is the fixed evaluator.

SECURITY: TEST_CMD must be provided as a list (e.g., ["pytest", "tests/", "--tb=no", "-q"]),
not a string. This prevents shell injection vulnerabilities.
"""

import re
import subprocess
import sys

# --- CONFIGURE THESE ---
# MUST be a list, not a string (SECURITY: prevents shell injection)
TEST_CMD = ["pytest", "tests/", "--tb=no", "-q"]  # Test command as LIST
# --- END CONFIG ---

def run_tests(cmd_list, timeout=300):
    """Run test command as list with shell=False for security."""
    if not isinstance(cmd_list, list):
        print(f"ERROR: TEST_CMD must be a list, got: {type(cmd_list)}", file=sys.stderr)
        print("SECURITY: String commands with shell=True are not allowed.", file=sys.stderr)
        print('Use ["pytest", "tests/"] instead of "pytest tests/"', file=sys.stderr)
        sys.exit(1)
    return subprocess.run(cmd_list, shell=False, capture_output=True, text=True, timeout=timeout)

result = run_tests(TEST_CMD)
output = result.stdout + "\n" + result.stderr

# Try to parse pytest output: "X passed, Y failed, Z errors"
passed = failed = errors = 0

# pytest short format: "5 passed, 2 failed in 1.23s"
match = re.search(r"(\d+) passed", output)
if match:
    passed = int(match.group(1))
match = re.search(r"(\d+) failed", output)
if match:
    failed = int(match.group(1))
match = re.search(r"(\d+) error", output)
if match:
    errors = int(match.group(1))

total = passed + failed + errors
if total == 0:
    # Try unittest format: "Ran X tests"
    match = re.search(r"Ran (\d+) test", output)
    if match:
        total = int(match.group(1))
        if result.returncode == 0:
            passed = total
        else:
            # Count failures from output
            fail_match = re.search(r"FAILED \(failures=(\d+)", output)
            if fail_match:
                failed = int(fail_match.group(1))
                passed = total - failed

if total == 0:
    print("Could not parse test results", file=sys.stderr)
    print(f"Output: {output[:500]}", file=sys.stderr)
    sys.exit(1)

rate = passed / total

print(f"pass_rate: {rate:.4f}")
print(f"passed: {passed}")
print(f"failed: {failed}")
print(f"total: {total}")
