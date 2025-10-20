"""
Robot subsystems for navigation, sensing, manipulation, and packing.
"""

from typing import List, Optional, Callable
from collections import deque
import random
import time
from .models import Item
from .config import (
    NAVIGATION_HOME_LOCATION, NAVIGATION_OBSTACLE_CHANCE, NAVIGATION_REROUTE_FAILURE_CHANCE,
    NAVIGATION_TIME_PER_MOVE, SENSOR_FAILURE_RATE, SENSOR_SCAN_TIME,
    GRIPPER_PICK_TIME, GRIPPER_DROP_TIME, MODE_FULL_AUTO, MODE_SEMI_AUTO
)


class NavigationSystem:
    """Handles robot movement and pathfinding with obstacle detection."""

    def __init__(self, sleeper: Callable = time.sleep):
        self.current_location = NAVIGATION_HOME_LOCATION
        self.obstacle_events: List[str] = []
        self.sleeper = sleeper

    def move_to(self, location: str, automation_mode: str = MODE_FULL_AUTO) -> bool:
        """Navigate to target location with obstacle simulation."""
        print(f"[NAV] Navigating from {self.current_location} to {location}...")
        self.sleeper(NAVIGATION_TIME_PER_MOVE)

        if random.random() < NAVIGATION_OBSTACLE_CHANCE:
            self.obstacle_events.append(f"Obstacle en route to {location}")
            print(f"[NAV] ⚠ Obstacle detected en route to {location}!")

            if automation_mode == MODE_SEMI_AUTO:
                response = input(
                    "[NAV] Attempt automatic reroute? (y/n): "
                ).strip().lower()
                if response != 'y':
                    print("[NAV] Navigation cancelled by user")
                    return False

            print("[NAV] Attempting automatic reroute...")
            self.sleeper(1.0)

            if random.random() < NAVIGATION_REROUTE_FAILURE_CHANCE:
                self.obstacle_events.append(f"Reroute failed to {location}")
                print("[NAV] - Reroute failed!")

                if automation_mode == MODE_SEMI_AUTO:
                    retry = input(
                        "[NAV] Retry navigation? (y/n): "
                    ).strip().lower()
                    if retry == 'y':
                        print("[NAV] Retrying navigation...")
                        self.sleeper(NAVIGATION_TIME_PER_MOVE)
                        self.current_location = location
                        print(f"[NAV] + Reached {location} (manual retry)")
                        return True
                return False

            print("[NAV] + Reroute successful")

        self.current_location = location
        print(f"[NAV] + Arrived at {location}")
        return True


class SensorArray:
    """Environmental sensing subsystem for item verification."""

    def __init__(self, sleeper: Callable = time.sleep):
        self.readings: List[str] = []
        self.sleeper = sleeper

    def scan_location(
        self, location: str, automation_mode: str = MODE_FULL_AUTO
    ) -> bool:
        """Scan location to verify item presence and correctness."""
        print(f"[SENSOR] Scanning location {location}...")
        self.sleeper(SENSOR_SCAN_TIME)

        success = random.random() > SENSOR_FAILURE_RATE
        self.readings.append(f"Scan {location}: {'OK' if success else 'FAIL'}")

        if not success:
            print(f"[SENSOR] - Scan failed at {location}")
            if automation_mode == MODE_SEMI_AUTO:
                retry = input("[SENSOR] Retry scan? (y/n): ").strip().lower()
                if retry == 'y':
                    print("[SENSOR] Retrying scan...")
                    self.sleeper(SENSOR_SCAN_TIME)
                    print("[SENSOR] + Scan successful (retry)")
                    return True
            return False

        print("[SENSOR] + Scan successful")
        return True


class Gripper:
    """Item manipulation subsystem for pick and drop operations."""

    def __init__(self, sleeper: Callable = time.sleep):
        self.status = "OPEN"
        self.carried_items: List[Item] = []
        self.sleeper = sleeper

    def pick_item(self, item: Item):
        """Execute pick operation on item."""
        print(f"[GRIPPER] Picking up {item.name}...")
        self.sleeper(GRIPPER_PICK_TIME)
        self.carried_items.append(item)
        self.status = "CLOSED"
        print(f"[GRIPPER] + Picked up {item.name} ({item.weight:.1f}kg)")

    def drop_item(self) -> Optional[Item]:
        """Execute drop operation, releasing carried item."""
        if self.carried_items:
            print("[GRIPPER] Dropping item...")
            self.sleeper(GRIPPER_DROP_TIME)
            item = self.carried_items.pop()
            self.status = "OPEN"
            print(f"[GRIPPER] + Dropped {item.name}")
            return item
        return None

    def clear_items(self):
        """Clear all carried items (error recovery)."""
        self.carried_items.clear()
        self.status = "OPEN"


class PackingOptimizer:
    """
    Optimizes packing sequence using STACK (LIFO) data structure.

    Heavy items are always packed first (bottom of box).

    ALGORITHM:
    1. Sort items by weight (ascending: lightest to heaviest)
    2. Push sorted items onto STACK (lightest first, heaviest last)
    3. Due to LIFO nature, pop operations retrieve heaviest first
    4. This ensures proper packing order without complex logic
    """

    def __init__(self):
        self.packing_stack: deque = deque()

    def prepare_packing_sequence(self, items: List[Item]):
        """Prepare optimal packing sequence using STACK properties."""
        self.packing_stack.clear()
        sorted_items = sorted(items, key=lambda x: x.weight)
        for item in sorted_items:
            self.packing_stack.append(item)

    def get_next_item_to_pack(self) -> Optional[Item]:
        """Pop next item from stack (LIFO: heaviest first)."""
        return self.packing_stack.pop() if self.packing_stack else None
