"""Integration test"""
from ..models import Order
from ..utils import setup_system

def test_integration():
    print("\n[TEST] Integration - Full Workflow")

    result = setup_system(sleeper=lambda *_: None)
    _, inv_mgr, task_mgr, station, robot = result

    order = Order("INTEGRATION_TEST", ["SKU001", "SKU002"])
    assert task_mgr.process_order(order), "Order creation failed"
    print("  + Order created and queued (FIFO)")

    initial_battery = robot.battery_level
    robot.execute_workflow(task_mgr, inv_mgr, station)

    assert robot.battery_level < initial_battery, "Battery should decrease"
    print(f"  + Battery consumed: {initial_battery - robot.battery_level:.1f}%")

    assert len(robot.operation_log) > 0, "Operations should be logged"
    print(f"  + Operations logged: {len(robot.operation_log)} entries")

    print("  + End-to-end workflow executed")
