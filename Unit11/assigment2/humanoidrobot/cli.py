"""
Command-line interface for human operators.
"""

from typing import Optional

from .config import MAX_ITEMS_PER_ORDER
from .models import Item, Order
from .warehouse import TaskManager, Warehouse


class CLI:
    """Command-line interface for human operators to interact with system."""

    @staticmethod
    def add_item(warehouse: Warehouse) -> bool:
        """Interactive CLI to add a single item to warehouse inventory.

        Notes:
            - Validates item IDs early and checks for duplicates
        """
        print("\n" + "=" * 50)
        print("ADD NEW ITEM TO WAREHOUSE")
        print("=" * 50)

        try:
            item_id = input("Item ID: ").strip()
            if not item_id:
                print("- Item ID cannot be empty")
                return False

            lookup_id = item_id.upper()
            if lookup_id in warehouse.inventory_index:
                # Integrity: no silent overwrite of existing records.
                print(f"- Item with ID '{item_id}' already exists.")
                return False

            # gets user name for item
            name = input("Item Name: ").strip()
            if not name:
                print("- Item name cannot be empty")
                return False

            # 3) gets user weight for new item
            weight_str = input("Weight (kg): ").strip()
            try:
                weight = float(weight_str)
                if weight <= 0:
                    print("- Weight must be positive")
                    return False
            except ValueError:
                print("- Weight must be a number")
                return False

            # 4) user input for item fragility
            fragile_str = input("Fragile? (y/n): ").strip().lower()
            fragility = fragile_str in ("y", "yes")

            # 5) Location
            location = input("Storage Location (e.g., A1, B2): ").strip().upper()
            if not location:
                print("- Location cannot be empty")
                return False

            # 6) Build item and add once
            item = Item(item_id, name, weight, fragility)  # ID normalised inside Item
            if not warehouse.add_item(item, location):
                # Race/consistency guard: if another add slipped in between checks.
                print(f"- Item with ID '{item_id}' already exists.")
                return False

            print(f"\n+ Item {item.item_id} ({item.name}) added successfully at {location}")
            return True

        except ValueError as e:
            print(f"- Error: {e}")
            return False
        except Exception as e:  # user-facing CLI guard
            print(f"- Unexpected error: {e}")
            return False

    @staticmethod
    def create_order(
        warehouse: Warehouse, task_manager: TaskManager
    ) -> Optional[Order]:
        """Interactive CLI for creating orders with quantity support.

        Assumptions:
            - Only existing items can be ordered (validated per entry).
            - Item IDs in inventory are uppercase; we uppercase inputs for lookup
              but keep messaging friendly.
        """
        print("\n" + "=" * 50)
        print("CREATE NEW ORDER")
        print("=" * 50)

        # Auto-generate order ID (FIFO queue uses this later)
        order_id = task_manager.get_next_order_id()
        print(f"\nOrder ID: {order_id} (auto-generated)")

        items_list: list[str] = []

        print("\nAvailable items in warehouse:")
        print("-" * 50)

        if warehouse.inventory:
            print("ID       | NAME      | WEIGHT | LOCATION")
            print("---------+-----------+--------+---------")
            for record in warehouse.inventory:
                item = record["item"]
                print(
                    f"{item.item_id:<8} | {item.name:<9} | "
                    f"{item.weight:>6.1f} | {record['location']}"
                )
        else:
            print("(Warehouse is empty)")

        print("\n" + "=" * 50)
        print("Add items to order (press Enter or type '0' when done)")
        print("=" * 50)

        while True:
            item_id = input("\nItem ID (or Enter/0 to finish): ").strip()

            if not item_id or item_id == "0":
                break

            # Lookup is case-insensitive (inventory keys are uppercase)
            lookup_id = item_id.upper()
            if not warehouse.find_item(lookup_id):
                print(f"- Item {item_id} not found in warehouse")
                continue

            quantity_str = input(f"Quantity of {item_id}: ").strip()
            try:
                quantity = int(quantity_str)
                if quantity <= 0:
                    print("- Quantity must be positive")
                    continue
                if quantity > 50:
                    print("- Quantity too large (max 50 per item)")
                    continue
            except ValueError:
                print("- Quantity must be a number")
                continue

            # Append one entry per unit to keep downstream logic simple (FIFO/stack).
            for _ in range(quantity):
                items_list.append(lookup_id)

            print(f"+ Added {quantity}x {lookup_id} to order")

            if len(items_list) >= MAX_ITEMS_PER_ORDER:
                print(f"\n⚠ Order has reached maximum size ({MAX_ITEMS_PER_ORDER} items)")
                break

        if not items_list:
            print("- Order must contain at least one item")
            return None

        try:
            order = Order(order_id, items_list)
            print(f"\n+ Order {order.order_id} created with {len(items_list)} items")
            return order
        except ValueError as e:
            print(f"- Error creating order: {e}")
            return None
