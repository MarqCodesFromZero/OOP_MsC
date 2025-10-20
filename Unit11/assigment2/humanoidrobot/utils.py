"""
Utility functions for system setup and display.
"""

import time
from typing import Callable
from .models import Item, Order
from .warehouse import Warehouse, InventoryManager, TaskManager, PackagingStation
from .robot import HumanoidRobot
from .config import (
    MODE_FULL_AUTO, ROBOT_BATTERY_CHARGING_THRESHOLD, ROBOT_BATTERY_CRITICAL
)


def setup_system(
    automation_mode: str = MODE_FULL_AUTO, sleeper: Callable = time.sleep
):
    """Initialize complete warehouse system with demo data."""
    warehouse = Warehouse()
    inventory_manager = InventoryManager(warehouse)
    task_manager = TaskManager(inventory_manager)
    station = PackagingStation("PACK_STATION_1")
    robot = HumanoidRobot("ROBOT_001", automation_mode, sleeper)

    demo_items = [
        (Item("SKU001", "Laptop", 2.5, True), "A1"),
        (Item("SKU002", "Cable", 0.1, False), "A2"),
        (Item("SKU003", "Monitor", 5.0, True), "B1"),
        (Item("SKU004", "Keyboard", 0.8, False), "B2"),
        (Item("SKU005", "Adapter", 0.5, False), "A3"),
    ]
    for item, location in demo_items:
        warehouse.add_item(item, location)

    return warehouse, inventory_manager, task_manager, station, robot


def print_help():
    """Display available CLI commands."""
    print("""
COMMANDS:
  help                - Shows commands
  items               - List warehouse inventory
  additem             - Add new item to warehouse inventory
  addorder            - Create order interactively (item and quantities)
  run [N]             - Execute N robot order cycles (default: 1)
  mode [auto|semi]    - Set automation mode
  status              - Show system status
  history [N]         - Show last N robot log entries (default: 10)
  env [N]             - Show last N environment readings/events (default: 10)
  demo                - Run automated demo
  test                - Run automated tests
  quit                - Exit system
    """)


def print_inventory(warehouse: Warehouse):
    """Display warehouse inventory in tabular format."""
    if not warehouse.inventory:
        print("Warehouse is empty")
        return

    print("\nINVENTORY:")
    print("ID       | NAME      | WEIGHT | FRAGILE | LOCATION")
    print("---------+-----------+--------+---------+---------")
    for record in warehouse.inventory:
        item = record['item']
        print(
            f"{item.item_id:<8} | {item.name:<9} | {item.weight:>6.1f} | "
            f"{str(item.fragility):<7} | {record['location']}"
        )
    print(f"\nTotal items: {len(warehouse.inventory)}\n")


def print_status(
    robot: HumanoidRobot, task_manager: TaskManager,
    warehouse: Warehouse, station: PackagingStation
):
    """Display comprehensive system status."""
    print("\nROBOT STATUS:")
    print(f"  ID: {robot.robot_id}")
    print(f"  Status: {robot.status.value}")
    print(f"  Automation Mode: {robot.automation_mode}")
    print(f"  Location: {robot.navigation.current_location}")
    print(f"  Battery: {robot.battery_level:.1f}%", end="")

    if robot.battery_level <= ROBOT_BATTERY_CRITICAL:
        print(" ⚠⚠⚠ CRITICAL!")
    elif robot.battery_level < ROBOT_BATTERY_CHARGING_THRESHOLD:
        print(" ⚠ LOW")
    else:
        print()

    print(f"  Items Carried: {len(robot.gripper.carried_items)}")

    print("\nSYSTEM STATUS:")
    print(f"  Tasks in Queue: {len(task_manager.task_queue)}")
    print(f"  Completed Tasks: {len(task_manager.completed_tasks)}")
    print(f"  Inventory Items: {len(warehouse.inventory)}")
    print(f"  Packed Orders: {len(station.packed_orders)}")
    print()


def run_demo(robot, task_manager, inventory_manager, station):
    """Execute automated demonstration workflow."""
    print("\n" + "=" * 60)
    print("RUNNING AUTOMATED DEMO")
    print("=" * 60)
    print("\nThis demo demonstrates the three core operations:")
    print("1. GET NEXT TASK - Order queued in FIFO queue")
    print("2. RETRIEVE ITEM - Navigate, scan, pick, transport, stage")
    print("3. PACK ORDER - Optimize with STACK, pack heaviest first")
    print(f"\nAutomation Mode: {robot.automation_mode}\n")

    items_list = ["SKU001", "SKU001", "SKU003"]
    order_id = task_manager.get_next_order_id()
    demo_order = Order(order_id, items_list)

    if task_manager.process_order(demo_order):
        print(f"+ Demo order {demo_order.order_id} created successfully")
        print(f"  Items: {', '.join(demo_order.items_required)}")
        print("  Queued in FIFO task queue\n")

        print("Executing workflow...\n")
        print("=" * 60)
        robot.execute_workflow(task_manager, inventory_manager, station)

        print("\n" + "=" * 60)
        print("DEMO COMPLETED")
        print("=" * 60)
        print("\nUse 'status' to see results or 'history' for detailed log\n")
    else:
        print("- Demo failed - items not available in inventory\n")
