"""
Main HumanoidRobot class coordinating warehouse operations.
"""

from typing import List, Callable
import time
from .models import RobotStatus, Task
from .warehouse import InventoryManager, TaskManager, PackagingStation
from .subsystems import NavigationSystem, SensorArray, Gripper, PackingOptimizer
from .config import (
    ROBOT_INITIAL_BATTERY, ROBOT_BATTERY_CHARGING_THRESHOLD,
    ROBOT_BATTERY_NAVIGATION_COST, ROBOT_BATTERY_RETRIEVAL_COST,
    ROBOT_BATTERY_PACKING_COST, ROBOT_CHARGING_TIME,
    NAVIGATION_CHARGING_STATION, PACKING_TIME_PER_ITEM,
    MODE_FULL_AUTO
)


class HumanoidRobot:
    """
    Autonomous humanoid robot coordinating warehouse operations.

    CORE OPERATIONS:
    1. GET NEXT TASK: Query TaskManager queue for validated orders
    2. RETRIEVE ITEM: Navigate -> Scan -> Pick → Transport -> Stage
    3. PACK ORDER: Analyze weights -> Stack items -> Pop and place (heaviest first)
    """

    def __init__(
        self, robot_id: str, automation_mode: str = MODE_FULL_AUTO,
        sleeper: Callable = time.sleep
    ):
        self.robot_id = robot_id
        self.battery_level = ROBOT_INITIAL_BATTERY
        self.status = RobotStatus.IDLE
        self.automation_mode = automation_mode
        self.sleeper = sleeper

        self.navigation = NavigationSystem(sleeper)
        self.sensors = SensorArray(sleeper)
        self.gripper = Gripper(sleeper)
        self.packing_optimizer = PackingOptimizer()

        self.operation_log: List[str] = []

    def log(self, message: str):
        """Log operation with timestamp to internal history and console."""
        timestamp = time.strftime("%H:%M:%S")
        entry = f"[{timestamp}] {message}"
        self.operation_log.append(entry)
        print()
        print(entry)

    def check_battery_and_charge(self) -> bool:
        """Check battery level and charge if needed."""
        if self.battery_level <= ROBOT_BATTERY_CHARGING_THRESHOLD:
            self.status = RobotStatus.CHARGING
            self.log(
                f"[BATTERY] Critical battery level ({self.battery_level:.1f}%)"
            )
            self.log("[BATTERY] Navigating to charging station...")

            if not self.navigation.move_to(
                NAVIGATION_CHARGING_STATION, self.automation_mode
            ):
                self.log("[BATTERY] Failed to reach charging station!")
                return False

            self.log(
                f"[BATTERY] Charging (Approx. {ROBOT_CHARGING_TIME:.0f} seconds)"
            )
            self.sleeper(ROBOT_CHARGING_TIME)

            self.battery_level = ROBOT_INITIAL_BATTERY
            self.log(
                f"[BATTERY] + Charging complete! ({self.battery_level:.1f}%)"
            )
            self.status = RobotStatus.IDLE

            return True

        return True

    def consume_battery(self, amount: float):
        """Consume battery and check if charging needed."""
        self.battery_level -= amount
        if self.battery_level < 0:
            self.battery_level = 0

    def retrieve_and_stage_one_item(
        self,
        item_id: str,
        inventory_manager: InventoryManager,
        station: PackagingStation
    ) -> bool:
        """Execute RETRIEVE ITEM operation for single item."""
        if not self.check_battery_and_charge():
            return False

        self.status = RobotStatus.RETRIEVING
        self.log(f"[ROBOT] Start retrieving {item_id}")

        record = inventory_manager.get_item_record(item_id)
        if not record:
            self.log(f"[ERROR] Item {item_id} not found in inventory")
            return False

        location = record['location']

        if not self.navigation.move_to(location, self.automation_mode):
            self.log(f"[ERROR] Navigation failed to {location}")
            return False
        self.consume_battery(ROBOT_BATTERY_NAVIGATION_COST)

        if not self.sensors.scan_location(location, self.automation_mode):
            self.log(
                f"[ERROR] Sensor verification failed for {item_id} at {location}"
            )
            return False

        self.gripper.pick_item(record['item'])

        if not self.navigation.move_to(station.station_id, self.automation_mode):
            self.log(f"[ERROR] Could not reach station {station.station_id}")
            return False
        self.consume_battery(ROBOT_BATTERY_NAVIGATION_COST)

        dropped = self.gripper.drop_item()
        if dropped:
            station.receive_staged_item(dropped)
            self.consume_battery(ROBOT_BATTERY_RETRIEVAL_COST)
            self.log(
                f"[ROBOT] Staged {item_id} at {station.station_id} "
                f"(Battery: {self.battery_level:.1f}%)"
            )
            return True

        self.log(f"[ERROR] Gripper empty when attempting to drop {item_id}")
        return False

    def pack_order(self, task: Task, station: PackagingStation) -> bool:
        """Execute PACK ORDER operation using STACK optimization."""
        if not self.check_battery_and_charge():
            return False

        self.status = RobotStatus.PACKING
        items_to_pack = station.get_staged_items_for_packing()
        self.log(
            f"[ROBOT] Packing {len(items_to_pack)} items for order {task.order_id}"
        )

        if not items_to_pack:
            self.log("[ROBOT] Nothing to pack")
            return True

        self.packing_optimizer.prepare_packing_sequence(items_to_pack)
        self.log("[PACK] Optimizing packing sequence (heaviest first)...")

        pack_count = 0
        while True:
            item = self.packing_optimizer.get_next_item_to_pack()
            if not item:
                break

            self.sleeper(PACKING_TIME_PER_ITEM)
            pack_count += 1
            self.log(
                f"[PACK] Packed item {pack_count}/{len(items_to_pack)}: "
                f"{item.item_id} ({item.name}, {item.weight:.1f}kg, "
                f"fragile={item.fragility})"
            )

        station.receive_order(task.order_id)
        self.consume_battery(ROBOT_BATTERY_PACKING_COST)
        self.log(
            f"[ROBOT] + Order {task.order_id} packaged "
            f"(Battery: {self.battery_level:.1f}%)"
        )
        return True

    def execute_workflow(
        self,
        task_manager: TaskManager,
        inventory_manager: InventoryManager,
        station: PackagingStation
    ):
        """Execute complete robot workflow for one order."""
        task = task_manager.get_next_task()
        if not task:
            self.log("[ROBOT] Checked for tasks: queue empty")
            return

        self.log(
            f"[ROBOT] Processing order {task.order_id} "
            f"with {len(task.item_ids)} items"
        )

        all_staged_successfully = True
        for idx, item_id in enumerate(task.item_ids, 1):
            self.log(f"[ROBOT] Retrieving item {idx}/{len(task.item_ids)}")
            if not self.retrieve_and_stage_one_item(
                item_id, inventory_manager, station
            ):
                all_staged_successfully = False
                break

        if all_staged_successfully:
            if self.pack_order(task, station):
                task_manager.completed_tasks.append(task.task_id)
                self.status = RobotStatus.IDLE
                self.log(f"[SUCCESS] +++ Order {task.order_id} complete! +++")
            else:
                self.status = RobotStatus.ERROR
                self.log(f"[FAIL] Order {task.order_id} failed during packing")
        else:
            self.status = RobotStatus.ERROR
            self.gripper.clear_items()
            self.log(
                f"[FAIL] Order {task.order_id} failed during retrieval/staging"
            )
