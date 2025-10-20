"""Module to auto run tests interactively via CLI"""

from .test_list import test_data_structure_list
from .test_stack import test_data_structure_stack
from .test_queue import test_data_structure_queue
from .test_search import test_search_algorithms
from .test_edge import test_edge_cases
from .test_integration import test_integration

def run_all_tests():
    """Execute complete automated test suite."""
    print("\n" + "=" * 60)
    print("AUTOMATED TEST SUITE - WAREHOUSE ROBOT SYSTEM")
    print("=" * 60)
    print("\nTesting data structures and algorithms per requirements...")

    tests = [
        ("Data Structure: List", test_data_structure_list),
        ("Data Structure: Stack (LIFO)", test_data_structure_stack),
        ("Data Structure: Queue (FIFO)", test_data_structure_queue),
        ("Search Algorithms", test_search_algorithms),
        ("Edge Cases", test_edge_cases),
        ("Integration Test", test_integration),
    ]

    passed = 0
    failed = 0

    for _, test_func in tests:
        try:
            test_func()
            passed += 1
        except AssertionError as e:
            print(f"\n  - FAILED: {e}")
            failed += 1
        except Exception as e:  # pylint: disable=broad-exception-caught
            print(f"\n  - ERROR: {e}")
            failed += 1

    print("\n" + "=" * 60)
    print(f"TEST SUMMARY: {passed} passed, {failed} failed")
    print("=" * 60)

    if failed == 0:
        print("\n+ All tests passed! System meets requirements.\n")
    else:
        print(f"\n- {failed} test(s) failed. Review output above.\n")

    return failed == 0
