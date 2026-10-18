"""
tests/run_tests.py
==================
Academic Mathematical Verification and Numerical Stability Test Suite.
Verifies analytical finite-difference gradients and numerical bounds for all NumPy models.
"""

import sys
import os
import time
import pytest

if __name__ == "__main__":
    test_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(test_dir)
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    print("=" * 80)
    print("  MATHEMATICAL GRADIENT VERIFICATION & NUMERICAL STABILITY TEST SUITE")
    print("=" * 80)
    print(f"Executing test files from: {test_dir}\n")

    start_time = time.time()
    exit_code = pytest.main([
        "-v",
        "-s",
        test_dir,
        "--tb=short"
    ])
    elapsed = time.time() - start_time

    print("\n" + "=" * 80)
    if exit_code == 0:
        print(f"  [SUCCESS] ALL 11 MATHEMATICAL GRADIENT & STABILITY TESTS PASSED ({elapsed:.2f}s)")
    else:
        print(f"  [FAILURE] TEST SUITE FAILED with exit code {exit_code}")
    print("=" * 80)

    sys.exit(exit_code)
