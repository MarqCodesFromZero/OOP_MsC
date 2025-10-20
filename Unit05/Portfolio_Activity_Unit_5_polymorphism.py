"""
This module demonstrates polymorphism through different types of warehouse robots.
"""

# Base class for all warehouse robots
class WarehouseRobot:
    def __init__(self, robot_id, battery_capacity):
        """
        Initialize a warehouse robot with ID and battery capacity.
        
        Parameters:
        robot_id (str): Unique identifier for the robot.
        battery_capacity (float): Maximum battery capacity in percentage.
        """
        self.robot_id = robot_id
        self.battery_capacity = battery_capacity
        self.battery_level = battery_capacity
        self.is_active = False
    
    def activate(self):
        """
        Activate the robot if it has sufficient battery.
        
        This method sets the is_active flag to True and prints an activation message.
        """
        if self.battery_level > 10:
            self.is_active = True
            print(f"Robot {self.robot_id} activated.")
        else:
            print(f"Robot {self.robot_id} cannot activate - low battery.")
    
    def deactivate(self):
        """
        Deactivate the robot.
        
        This method sets the is_active flag to False and prints a deactivation message.
        """
        if self.is_active:
            self.is_active = False
            print(f"Robot {self.robot_id} deactivated.")
        else:
            print(f"Robot {self.robot_id} is already inactive.")
    
    def perform_task(self):
        """
        Overriden by other classes 
        """
        print(f"Robot {self.robot_id} performing generic task...")


# Picks and packs items
class HumanoidRobot(WarehouseRobot):
    def __init__(self, robot_id, battery_capacity, gripper_type):
        """
        Initialize a humanoid robot with gripper capabilities.
        
        Parameters:
        robot_id (str): Unique identifier for the robot.
        battery_capacity (float): Maximum battery capacity in percentage.
        gripper_type (str): Type of gripper (e.g., "standard", "precision").
        """
        super().__init__(robot_id, battery_capacity)
        self.gripper_type = gripper_type
        self.items_carried = []
    
    def perform_task(self):
        """
        Override perform_task to pick and pack items.
        
        Humanoid robots specialize in handling items with grippers.
        """
        if self.is_active:
            print(f"Humanoid Robot {self.robot_id} using {self.gripper_type} gripper...")
            print("Picking items from shelves")
            print("Packing items into boxes")
            self.battery_level -= 5
        else:
            print(f"Robot {self.robot_id} is not active.")
    
    def pick_item(self, item_name):
        """
        Pick an item using the gripper.
        
        Parameters:
        item_name (str): Name of the item to pick.
        """
        if self.is_active:
            self.items_carried.append(item_name)
            print(f"Robot {self.robot_id} picked up: {item_name}")
        else:
            print(f"Robot {self.robot_id} cannot pick items - not active.")


# For moving pallets
class TransportRobot(WarehouseRobot):
    def __init__(self, robot_id, battery_capacity, load_capacity):
        """
        Initialize a transport robot with load capacity.
        
        Parameters:
        robot_id (str): Unique identifier for the robot.
        battery_capacity (float): Maximum battery capacity in percentage.
        load_capacity (float): Maximum weight capacity in kg.
        """
        super().__init__(robot_id, battery_capacity)
        self.load_capacity = load_capacity
        self.current_load = 0
    
    def perform_task(self):
        """
        Override perform_task to transport heavy loads.
        
        Transport robots specialize in moving pallets and heavy items.
        """
        if self.is_active:
            print(f"Transport Robot {self.robot_id} moving loads...")
            print(f"Current load: {self.current_load}/{self.load_capacity} kg")
            print("Transporting pallets across warehouse")
            self.battery_level -= 8
        else:
            print(f"Robot {self.robot_id} is not active.")
    
    def load_pallet(self, weight):
        """
        Load a pallet onto the robot.
        
        Parameters:
        weight (float): Weight of the pallet in kg.
        """
        if self.is_active and (self.current_load + weight <= self.load_capacity):
            self.current_load += weight
            print(f"Robot {self.robot_id} loaded {weight}kg (Total: {self.current_load}kg)")
        else:
            print(f"Robot {self.robot_id} cannot load - exceeds capacity or inactive.")


# Specialized for scanning and counting
class InventoryRobot(WarehouseRobot):
    def __init__(self, robot_id, battery_capacity, scanner_type):
        """
        Initialize an inventory robot with scanning capabilities.
        
        Parameters:
        robot_id (str): Unique identifier for the robot.
        battery_capacity (float): Maximum battery capacity in percentage.
        scanner_type (str): Type of scanner (e.g., "barcode", "RFID").
        """
        super().__init__(robot_id, battery_capacity)
        self.scanner_type = scanner_type
        self.items_scanned = 0
    
    def perform_task(self):
        """
        Override perform_task to scan and audit inventory.
        
        Inventory robots specialises in tracking and verifying stock.
        """
        if self.is_active:
            print(f"Inventory Robot {self.robot_id} scanning with {self.scanner_type}...")
            print("Scanning shelves for inventory audit")
            print(f"Items scanned so far: {self.items_scanned}")
            self.battery_level -= 3
        else:
            print(f"Robot {self.robot_id} is not active.")
    
    def scan_item(self, item_id):
        """
        Scan an item for inventory tracking.
        
        Parameters:
        item_id (str): ID of the item to scan.
        """
        if self.is_active:
            self.items_scanned += 1
            print(f"Robot {self.robot_id} scanned item: {item_id}")
        else:
            print(f"Robot {self.robot_id} cannot scan - not active.")


# Demonstration of polymorphism
if __name__ == "__main__":
    print("=" * 60)
    print("POLYMORPHISM DEMONSTRATION - WAREHOUSE ROBOT FLEET")
    print("=" * 60)

    # Create instances of different robot types
    humanoid = HumanoidRobot("H-001", 100, "precision")
    transport = TransportRobot("T-001", 100, 500)
    inventory = InventoryRobot("I-001", 100, "RFID")

    robot_fleet = [humanoid, transport, inventory]

    print("\n--- ACTIVATING ALL ROBOTS ---\n")
    for robot in robot_fleet:
        robot.activate() 

    print("\n--- PERFORMING TASKS ---\n")
    for robot in robot_fleet:
        robot.perform_task()  # Each robot type performs its specialized task
        print()

    print("--- SPECIALIZED OPERATIONS ---\n")
    # Perform type-specific operations
    if isinstance(humanoid, HumanoidRobot):
        humanoid.pick_item("Laptop")
        humanoid.pick_item("Keyboard")

    if isinstance(transport, TransportRobot):
        transport.load_pallet(200)
        transport.load_pallet(150)

    if isinstance(inventory, InventoryRobot):
        inventory.scan_item("SKU001")
        inventory.scan_item("SKU002")
        inventory.scan_item("SKU003")

    print("\n--- DEACTIVATING ALL ROBOTS ---\n")

    for robot in robot_fleet:
        robot.deactivate()
        print(f"  Battery remaining: {robot.battery_level:.1f}%")
        print()

    print("=" * 60)
    print("  Single interface (WarehouseRobot) for multiple robot types")
    print("  perform_task() behaves differently for each robot type")
    print("  Easy to add new robot types without changing existing code")
    print("  Flexibility in managing heterogeneous robot collections")
    print("=" * 60)
