"""Edge cases & error handling tests"""
from ..models import Item
from ..warehouse import Warehouse, InventoryManager, TaskManager
from ..subsystems import Gripper
from ..robot import HumanoidRobot
from ..config import ROBOT_BATTERY_CHARGING_THRESHOLD

def test_edge_cases():
    print("\n[TEST] Edge Cases and Error Handling")

    warehouse = Warehouse()
    assert warehouse.find_item("ANY") is None, "Empty warehouse should return None"
    print("  + Empty warehouse handled")

    try:
        Item("", "Invalid", 1.0, False)
        assert False, "Should raise ValueError for empty ID"
    except ValueError:
        print("  + Empty item_id validation works")

    try:
        Item("INVALID", "Negative", -5.0, False)
        assert False, "Should raise ValueError for negative weight"
    except ValueError:
        print("  + Negative weight validation works")

    gripper = Gripper(lambda *_: None)
    assert gripper.drop_item() is None, "Empty gripper should return None"
    print("  + Empty gripper handled")

    warehouse = Warehouse()
    inv_mgr = InventoryManager(warehouse)
    task_mgr = TaskManager(inv_mgr)
    assert task_mgr.get_next_task() is None, "Empty queue should return None"
    print("  + Empty task queue handled")

    robot = HumanoidRobot("TEST", sleeper=lambda *_: None)
    robot.battery_level = 5.0
    assert robot.battery_level <= ROBOT_BATTERY_CHARGING_THRESHOLD, "Low battery not detected"
    print("  + Low battery condition detected")
