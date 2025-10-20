"""Search algorithms tests"""
import time
from ..models import Item
from ..warehouse import Warehouse

def test_search_algorithms():
    print("\n[TEST] Search Algorithms")
    warehouse = Warehouse()

    test_items = [
        Item("SEARCH001", "Item1", 1.5, False),
        Item("SEARCH002", "Item2", 3.0, False),
        Item("SEARCH003", "Item3", 5.5, False),
        Item("SEARCH004", "Item4", 8.0, False),
    ]

    for idx, item in enumerate(test_items):
        warehouse.add_item(item, f"LOC{idx}")

    start = time.perf_counter()
    result_linear = warehouse.find_item_linear("SEARCH003")
    time_linear = time.perf_counter() - start

    assert result_linear is not None, "Linear search failed to find item"
    assert result_linear['item'].item_id == "SEARCH003"

    start = time.perf_counter()
    result_hash = warehouse.find_item("SEARCH003")
    time_hash = time.perf_counter() - start

    assert result_hash is not None, "Hash search failed to find item"
    assert result_hash['item'].item_id == "SEARCH003"

    loc_results = warehouse.find_items_by_location("LOC2")
    assert len(loc_results) == 1, "Location search failed"
    assert loc_results[0]['item'].item_id == "SEARCH003"

    assert warehouse.find_item("NONEXISTENT") is None
    assert warehouse.find_item_linear("NONEXISTENT") is None

    print(f"  + Linear search O(n): {time_linear * 1000:.4f}ms")
    print(f"  + Hash search O(1): {time_hash * 1000:.4f}ms")
    if time_linear > 0 and time_hash > 0:
        print(f"  + Hash search ~{time_linear / time_hash:.1f}x faster")
    print("  + Location-based filtering works")
    print("  + Missing items handled gracefully")
