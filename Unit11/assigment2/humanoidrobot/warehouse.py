"""
Warehouse storage and inventory management systems.
"""

from typing import List, Optional, Dict
from collections import deque
from .models import Item, Order, Task


class Warehouse:
    """
    Manages physical inventory storage using LIST data structure.

    Demonstrates multiple search algorithms:
    - Linear search O(n): Educational demonstration
    - Hash-based search O(1): Production efficiency
    - Location filtering: Spatial queries
    """

    def __init__(self):
        """Initialize warehouse with empty inventory and indexes."""
        self.inventory: List[Dict] = []
        self.inventory_index: Dict[str, Dict] = {}
        self.location_index: Dict[str, List[Dict]] = {}

    def add_item(self, item: Item, location: str):
        """Add item to warehouse inventory with dual indexing."""

        if item.item_id in self.inventory_index:
            return False

        record = {'item': item, 'location': location}
        self.inventory.append(record)
        self.inventory_index[item.item_id] = record
        if location not in self.location_index:
            self.location_index[location] = []
        self.location_index[location].append(record)
        return True

    def find_item_linear(self, item_id: str) -> Optional[Dict]:
        """LINEAR SEARCH ALGORITHM - O(n) complexity."""
        for record in self.inventory:
            if record['item'].item_id == item_id:
                return record
        return None

    def find_item(self, item_id: str) -> Optional[Dict]:
        """HASH-BASED SEARCH ALGORITHM - O(1) complexity."""
        return self.inventory_index.get(item_id)

    def find_items_by_location(self, location: str) -> List[Dict]:
        """LOCATION-BASED FILTERING - Spatial search algorithm."""
        return self.location_index.get(location, [])


class InventoryManager:
    """Acts as authority on warehouse environmental data."""

    def __init__(self, warehouse: Warehouse):
        self.warehouse = warehouse

    def validate_order(self, order: Order) -> bool:
        """Validate that all required items exist in inventory."""
        return all(
            self.warehouse.find_item(item_id) for item_id in order.items_required
        )

    def get_item_record(self, item_id: str) -> Optional[Dict]:
        """Retrieve full warehouse record for an item."""
        return self.warehouse.find_item(item_id)


class TaskManager:
    """
    Manages task queue using FIFO (First-In-First-Out) data structure.

    The QUEUE ensures fair order processing in sequence received.
    Uses deque for O(1) enqueue and dequeue operations.
    """

    def __init__(self, inventory_manager: InventoryManager):
        self.inventory_manager = inventory_manager
        self.task_queue: deque = deque()
        self.completed_tasks: List[str] = []
        self.order_counter: int = 1

    def process_order(self, order: Order) -> bool:
        """Validate order and add task to FIFO queue."""
        if not self.inventory_manager.validate_order(order):
            return False
        task = Task(
            task_id=f"T_{order.order_id}",
            order_id=order.order_id,
            item_ids=order.items_required
        )
        self.task_queue.append(task)
        return True

    def get_next_order_id(self) -> str:
        """Generate next sequential order ID."""
        order_id = f"ORD{self.order_counter:04d}"
        self.order_counter += 1
        return order_id

    def get_next_task(self) -> Optional[Task]:
        """Retrieve next task from queue (FIFO ordering)."""
        return self.task_queue.popleft() if self.task_queue else None


class PackagingStation:
    """Physical workspace where robot stages and packs items."""

    def __init__(self, station_id: str):
        self.station_id = station_id
        self.staged_items: List[Item] = []
        self.packed_orders: List[str] = []

    def receive_staged_item(self, item: Item):
        """Accept item delivered by robot for staging."""
        self.staged_items.append(item)

    def get_staged_items_for_packing(self) -> List[Item]:
        """Retrieves all staged items and clear staging area."""
        items_to_pack = self.staged_items.copy()
        self.staged_items.clear()
        return items_to_pack

    def receive_order(self, order_id: str):
        """Records a completed order."""
        self.packed_orders.append(order_id)
