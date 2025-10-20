"""Queue (FIFO) tests"""
from ..models import Item, Order
from ..warehouse import Warehouse, InventoryManager, TaskManager

def test_data_structure_queue():
    print("\n[TEST] Queue (FIFO) Data Structure")
    warehouse = Warehouse()
    for i in range(5):
        warehouse.add_item(Item(f"Q{i}", f"Item{i}", 1.0, False), "A1")

    inv_mgr = InventoryManager(warehouse)
    task_mgr = TaskManager(inv_mgr)

    order_ids = ["ORDER_FIRST", "ORDER_SECOND", "ORDER_THIRD"]
    for oid in order_ids:
        order = Order(oid, [f"Q{order_ids.index(oid)}"])
        task_mgr.process_order(order)

    dequeued_order_ids = []
    while True:
        task = task_mgr.get_next_task()
        if not task:
            break
        dequeued_order_ids.append(task.order_id)

    assert dequeued_order_ids == order_ids, \
        f"FIFO order violated: expected {order_ids}, got {dequeued_order_ids}"

    print("  + Queue maintains FIFO ordering")
    print("  + First-come-first-served processing verified")
    print("  + Fair order handling ensured")
