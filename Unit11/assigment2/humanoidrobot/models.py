"""
Data models and enums for the Humanoid Robot Warehouse System.
"""

from dataclasses import dataclass
from enum import Enum
from typing import List
from .config import MAX_ITEM_WEIGHT, MIN_ITEM_WEIGHT, MAX_ITEMS_PER_ORDER



class RobotStatus(Enum):
    """Robot operational states."""
    IDLE = "IDLE"
    RETRIEVING = "RETRIEVING"
    PACKING = "PACKING"
    CHARGING = "CHARGING"
    ERROR = "ERROR"


@dataclass
class Item:
    """Represents an item with validation."""
    item_id: str
    name: str
    weight: float
    fragility: bool

    def __post_init__(self):
        """Validate item data after initialisation."""
        if not self.item_id or not self.item_id.strip():
            raise ValueError("item_id cannot be empty")
        if not self.name or not self.name.strip():
            raise ValueError("name cannot be empty")
        if self.weight <= MIN_ITEM_WEIGHT:
            raise ValueError(
                f"weight must be > {MIN_ITEM_WEIGHT}kg, got {self.weight}"
            )
        if self.weight > MAX_ITEM_WEIGHT:
            raise ValueError(
                f"weight exceeds maximum ({MAX_ITEM_WEIGHT}kg), got {self.weight}"
            )
        if not isinstance(self.fragility, bool):
            raise TypeError(
                f"fragility must be boolean, got {type(self.fragility)}"
            )
        self.item_id = self.item_id.strip().upper()
        self.name = self.name.strip()


@dataclass
class Order:
    """Represents a customer order requiring item retrieval."""
    order_id: str
    items_required: List[str]

    def __post_init__(self):
        """Validate order data."""
        if not self.order_id or not self.order_id.strip():
            raise ValueError("order_id cannot be empty")
        if not self.items_required:
            raise ValueError("Order must contain at least one item")
        if len(self.items_required) > MAX_ITEMS_PER_ORDER:
            raise ValueError(
                f"Order exceeds maximum items ({MAX_ITEMS_PER_ORDER})"
            )
        self.order_id = self.order_id.strip().upper()


@dataclass
class Task:
    """Represents a work task for the robot derived from an order."""
    task_id: str
    order_id: str
    item_ids: List[str]