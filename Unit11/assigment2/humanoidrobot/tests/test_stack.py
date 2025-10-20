"""Stack (LIFO) test """
from ..models import Item
from ..subsystems import PackingOptimizer

def test_data_structure_stack():
    print("\n[TEST] Stack (LIFO) Data Structure")
    optimizer = PackingOptimizer()

    items = [
        Item("STACK1", "Light", 1.0, False),
        Item("STACK2", "Medium", 5.0, False),
        Item("STACK3", "Heavy", 10.0, False),
    ]

    optimizer.prepare_packing_sequence(items)

    popped_weights = []
    while True:
        item = optimizer.get_next_item_to_pack()
        if not item:
            break
        popped_weights.append(item.weight)

    assert popped_weights == [10.0, 5.0, 1.0], \
        f"LIFO order violated: expected [10.0, 5.0, 1.0], got {popped_weights}"

    assert optimizer.get_next_item_to_pack() is None, "Empty stack should return None"

    print("  + Stack maintains LIFO ordering")
    print("  + Heaviest items retrieved first (optimal packing)")
    print("  + Empty stack handled correctly")