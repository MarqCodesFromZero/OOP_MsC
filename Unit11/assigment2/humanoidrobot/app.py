"""
Main entry point for the Humanoid Robot Warehouse System.
"""

import time

from .cli import CLI
from .config import MODE_FULL_AUTO, MODE_SEMI_AUTO
from .tests.run import run_all_tests
from .utils import (
    setup_system,
    print_help,
    print_inventory,
    print_status,
    run_demo,
)


def main() -> None:
    """CLI coordinator

    Responsibilities:
        - Collects user commands
        - Delegates operationns to subsystems 
    """
    print("=" * 60)
    print("HUMANOID ROBOT WAREHOUSE SYSTEM")
    print("=" * 60)
    print("\nSelect robot mode:")
    print("  1. Full Automatic (robot handles entire operation)")
    print("  2. Semi-Automatic (user assistance with obstacles, retries...)")

    while True:
        mode_choice = input("\nMode: ").strip()
        if mode_choice == "1":
            automation_mode = MODE_FULL_AUTO
            break
        if mode_choice == "2":
            automation_mode = MODE_SEMI_AUTO
            break
        print("Invalid choice. Please enter 1 or 2.")

    print(f"\n+ Automation mode set to: {automation_mode}")
    print("\nInitializing system...")

    #creates subsystems to be used throughout the system
    warehouse, inventory_manager, task_manager, station, robot = setup_system(
        automation_mode
    )

    print(f"+ System ready! {len(warehouse.inventory)} items in warehouse.")
    print(
        f"+ Robot {robot.robot_id} initialized at "
        f"{robot.navigation.current_location}"
    )
    print(f"+ Battery level: {robot.battery_level:.1f}%")
    print(
        "\nType 'help' for commands, 'demo' for demo, "
        "'test' for automated tests or 'quit'\n"
    )

    while True:
        try:
            command_line = input("robot>> ").strip().split()
        except (EOFError, KeyboardInterrupt):
            # allows Ctrl+D/Ctrl+C to exit without stack traces.
            print("\n\nShutting down system. Goodbye!")
            break

        if not command_line:
            continue

        cmd, *args = command_line
        cmd = cmd.lower()  # lowers the command token and preservesthe argument structure (SKUs).

        if cmd == "help":
            print_help()

        elif cmd == "items":
            print_inventory(warehouse)

        elif cmd == "additem":
            CLI.add_item(warehouse)

        elif cmd == "addorder":
            order = CLI.create_order(warehouse, task_manager)
            if order:
                if task_manager.process_order(order):
                    print(f"\n+ Order {order.order_id} queued successfully!")
                    print(f"  Total items in order: {len(order.items_required)}")
                    print(
                        f"  Position in queue: {len(task_manager.task_queue)}"
                    )
                else:
                    print("\n- Order validation failed")

        elif cmd == "run":
            # Defensive parsing: default to 1 cycle if arg is missing/non-numeric.
            cycles = int(args[0]) if args and args[0].isdigit() else 1

            if not task_manager.task_queue:
                # Guidance to the correct command name to reduce user friction.
                print("- No tasks in queue. Use 'addorder' to create orders.")
                continue

            for i in range(cycles):
                if not task_manager.task_queue:
                    print(f"\nCompleted {i} cycles - queue empty")
                    break

                print(f"\n{'=' * 60}")
                print(f"EXECUTING CYCLE {i + 1}/{cycles}")
                print(f"{'=' * 60}\n")
                robot.execute_workflow(task_manager, inventory_manager, station)

                if i < cycles - 1 and task_manager.task_queue:
                    print("\n--- Preparing for next cycle ---\n")
                    time.sleep(1)

        elif cmd == "mode":
            # Accept common aliases while keeping args case-preserved elsewhere.
            if args and args[0].lower() in ("auto", "full", "fullauto"):
                robot.automation_mode = MODE_FULL_AUTO
                print(f"+ Automation mode set to: {MODE_FULL_AUTO}")
            elif args and args[0].lower() in ("semi", "semiauto"):
                robot.automation_mode = MODE_SEMI_AUTO
                print(f"+ Automation mode set to: {MODE_SEMI_AUTO}")
            else:
                print(f"Current mode: {robot.automation_mode}")
                print("Usage: mode [auto|semi]")

        elif cmd == "status":
            print_status(robot, task_manager, warehouse, station)

        elif cmd == "history":
            n = int(args[0]) if args and args[0].isdigit() else 10
            print(f"\nLast {n} operations:")
            for log in robot.operation_log[-n:]:
                print(log)
            print()

        elif cmd == "env":
            n = int(args[0]) if args and args[0].isdigit() else 10
            print("\nEnvironment Status:")
            print(f"  Current Location: {robot.navigation.current_location}")
            print(f"\n  Obstacle Events (last {n}):")
            if robot.navigation.obstacle_events:
                for e in robot.navigation.obstacle_events[-n:]:
                    print(f"    - {e}")
            else:
                print("    (none)")
            print(f"\n  Sensor Readings (last {n}):")
            if robot.sensors.readings:
                for r in robot.sensors.readings[-n:]:
                    print(f"    - {r}")
            else:
                print("    (none)")
            print()

        elif cmd == "demo":
            run_demo(robot, task_manager, inventory_manager, station)

        elif cmd == "test":
            run_all_tests()

        elif cmd in ("quit", "exit"):
            print("\nShutting down system. Goodbye!")
            break

        else:
            print(
                f"- Unknown command: '{cmd}'. "
                "Type 'help' for available commands."
            )


if __name__ == "__main__":
    main()
