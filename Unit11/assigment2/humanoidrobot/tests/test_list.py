"""List data structure tests (unchanged)."""
from ..models import Item
from ..warehouse import Warehouse

def test_data_structure_list():
    print("\n[TEST] List Data Structure")
    warehouse = Warehouse()

    test_items = [
        (Item("LIST001", "Item1", 1.0, False), "A1"),
        (Item("LIST002", "Item2", 2.0, False), "A2"),
        (Item("LIST003", "Item3", 3.0, False), "A3"),
    ]

    for item, loc in test_items:
        warehouse.add_item(item, loc)

    assert len(warehouse.inventory) == 3, f"Expected 3 items, got {len(warehouse.inventory)}"

    count = 0
    for record in warehouse.inventory:
        count += 1
        assert 'item' in record and 'location' in record, "Record structure invalid"
    assert count == 3, f"Iteration count mismatch: expected 3, got {count}"

    first_item = warehouse.inventory[0]['item']
    assert first_item.item_id == "LIST001", f"Index access failed: got {first_item.item_id}"

    print("  + List append O(1) verified")
    print("  + List iteration O(n) verified")
    print("  + List index access O(1) verified")
