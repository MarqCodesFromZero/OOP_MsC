# Humanoid Robot Warehouse System

## Table of Contents
1. [Overview](#overview)
2. [System Architecture](#system-architecture)
3. [Installation & Execution](#installation--execution)
4. [Data Structures & Algorithms](#data-structures--algorithms)
5. [Testing](#testing)
6. [Evaluation and reflection](#evaluation-and-reflection)
7. [References](#references)
8. [Project Structure](#project-structure)

---

## Overview

This system implements an autonomous humanoid robot for warehouse operations, capable of order fulfillment through intelligent navigation, item retrieval, and optimized packing. The implementation follows object-oriented principles and demonstrates core computer science data structures and algorithms.

**Key Features:**
- Autonomous navigation with obstacle avoidance
- Sensor-based item verification
- Battery management with automatic charging
- Two operational modes: Full Automatic and Semi-Automatic
- FIFO order queue processing
- LIFO-based packing optimization

---

## System Architecture

### Core Components

**1. Robot Subsystems:**
- `HumanoidRobot`: Main coordinator orchestrating warehouse operations
- `NavigationSystem`: Pathfinding and movement with obstacle detection
- `SensorArray`: Environmental sensing for item verification
- `Gripper`: Physical item manipulation (pick/drop operations)
- `PackingOptimizer`: Weight-based packing sequence optimization

**2. Warehouse Management:**
- `Warehouse`: Physical inventory storage with dual indexing
- `InventoryManager`: Inventory validation and record retrieval
- `TaskManager`: FIFO queue for order processing
- `PackagingStation`: Staging area for retrieved items

**3. Data Models:**
- `Item`: Product representation with validation
- `Order`: Customer order with multiple items
- `Task`: Robot work unit derived from orders
- `RobotStatus`: Operational state enumeration

---

## Installation & Execution

### Prerequisites
- Python 3.8 or higher
- No external dependencies required (uses standard library only)

### Setup
```bash
# Clone or extract the project
cd humanoid-robot

# Verify structure
ls humanoidrobot/
# Should show: app.py, cli.py, config.py, models.py, robot.py, subsystems.py, utils.py, warehouse.py, tests/
```

### Running the System
1.  Navigate to the project's root directory (`humanoid-robot/`).
2.  Run the main script from your terminal:
    ```bash
    python main.py
    ```
3.  You will be prompted to select an automation mode. After making a selection, the interactive `robot>>` prompt will appear.
4.  Type `help` to see a full list of available commands.

### Running Tests

The system includes a comprehensive, built-in test suite. To run it, simply use the `test` command at the application's prompt:

```bash
robot>> test
```

This will execute all unit, integration, and edge-case tests automatically and provide a summary of the results directly in your terminal.

Alternatively you can install pytest and run:

```bash
pytest -q
```

### CLI Commands Reference

| Command | Description |
|---------|-------------|
| `help` | Display all available commands |
| `items` | List current warehouse inventory |
| `additem` | Add new item interactively |
| `addorder` | Create customer order |
| `run [N]` | Execute N robot cycles (default: 1) |
| `mode [auto\|semi]` | Switch automation mode |
| `status` | Show system status |
| `history [N]` | View last N log entries |
| `env [N]` | Show environment readings |
| `demo` | Run automated demonstration |
| `test` | Execute test suite |
| `quit` | Exit system |

---

## Data Structures & Algorithms

This section demonstrates the implementation of core data structures and algorithms as required by the assignment.

### 1. List (Dynamic Array)
**Location:** `warehouse.py` - `Warehouse.inventory`

**Operations:**
- Append: O(1) amortized
- Iteration: O(n)
- Index access: O(1)

**Usage:** Stores all warehouse inventory records with item and location data.

### 2. Queue (FIFO)
**Location:** `warehouse.py` - `TaskManager.task_queue`

**Implementation:** `collections.deque`

**Operations:**
- Enqueue (append): O(1)
- Dequeue (popleft): O(1)

**Usage:** Ensures fair order processing - first order received is first processed.

### 3. Stack (LIFO)
**Location:** `subsystems.py` - `PackingOptimizer.packing_stack`

**Implementation:** `collections.deque`

**Operations:**
- Push (append): O(1)
- Pop: O(1)

**Usage:** Optimizes packing sequence. Items sorted by weight (ascending) then pushed onto stack. Pop operations retrieve heaviest first for stable packing.

**Algorithm:**
```
1. Sort items: lightest → heaviest
2. Push all to stack (lightest first)
3. Pop from stack (heaviest first due to LIFO)
4. Result: Heavy items packed at bottom
```

### 4. Hash Table (Dictionary)
**Location:** `warehouse.py` - `Warehouse.inventory_index`

**Operations:**
- Insert: O(1) average
- Lookup: O(1) average

**Usage:** Fast item retrieval by ID, avoiding O(n) linear searches.

### Search Algorithms

**Linear Search** - `find_item_linear()`
- Complexity: O(n)
- Use case: Educational demonstration

**Hash-Based Search** - `find_item()`
- Complexity: O(1) average
- Use case: Production efficiency

**Performance:** Tests show hash search is ~10-100x faster for typical warehouse sizes.

---

## Testing

### Test Suite Structure

All tests located in `humanoidrobot/tests/`:

1. **`test_list.py`**: List operations (append, iteration, indexing)
2. **`test_queue.py`**: FIFO ordering verification
3. **`test_stack.py`**: LIFO packing sequence
4. **`test_search.py`**: Algorithm performance comparison
5. **`test_edge.py`**: Edge cases and error handling
6. **`test_integration.py`**: End-to-end workflow

### Testing Approach

**All automated tests use Python's `assert` statements.** Test failures raise `AssertionError` with explanatory messages indicating what condition was violated. This provides immediate, automated verification of correctness without manual inspection.

### Running Tests

```bash
python main.py
# Type: test

# OR run non-interactively:
python -m humanoidrobot.tests.run (Should return empty in Terminal if tests pass)
```

### Test Coverage

- ✅ Data structure operations (List, Queue, Stack)
- ✅ Search algorithm correctness and performance
- ✅ Input validation (empty IDs, negative weights)
- ✅ Empty state handling (empty queue, empty gripper)
- ✅ Battery management logic
- ✅ End-to-end workflow integration

### Sample Test Output
```
============================================================
AUTOMATED TEST SUITE - WAREHOUSE ROBOT SYSTEM
============================================================

Testing data structures and algorithms per requirements...

[TEST] List Data Structure
  + List append O(1) verified
  + List iteration O(n) verified
  + List index access O(1) verified

[TEST] Queue (FIFO) Data Structure
  + Queue maintains FIFO ordering
  + First-come-first-served processing verified
  + Fair order handling ensured

[TEST] Stack (LIFO) Data Structure
  + Stack maintains LIFO ordering
  + Heaviest items retrieved first (optimal packing)
  + Empty stack handled correctly

[TEST] Search Algorithms
  + Linear search O(n): 0.0123ms
  + Hash search O(1): 0.0012ms
  + Hash search ~10.3x faster
  + Location-based filtering works
  + Missing items handled gracefully

[TEST] Edge Cases and Error Handling
  + Empty warehouse handled
  + Empty item_id validation works
  + Negative weight validation works
  + Empty gripper handled
  + Empty task queue handled
  + Low battery condition detected

[TEST] Integration - Full Workflow
  + Order created and queued (FIFO)
  + Battery consumed: 14.0%
  + Operations logged: 8 entries
  + End-to-end workflow executed

============================================================
TEST SUMMARY: 6 passed, 0 failed
============================================================

+ All tests passed! System meets requirements.
```

---

## System Design Updates

This implementation is representative of the activity diagram, class diagram, sequence diagrams, and state transition diagram defined in Assignment 1 (System Design). All diagrams are located in the `docs/` directory and embedded below for reference.

### Design Alignment

The code faithfully implements:
- **Class Diagram**: All classes, attributes, methods, and relationships (composition, association)
- **Sequence Diagrams**: Order creation flow and robot workflow interactions
- **Activity Diagram**: Complete workflow cycle including decision points and loops
- **State Machine**: Robot status transitions (IDLE → RETRIEVING → PACKING → CHARGING → ERROR)

**Note:** Minor enhancements were made during implementation (e.g., battery management sophistication, dual automation modes) that represent natural evolution of the design rather than deviation from it. These improvements maintain architectural consistency with the "Connected Specialist" philosophy.

### Diagrams

All diagrams from Assignment 1 (updated to reflect implementation) are included in `docs/`:

```
docs/
  ├── class-diagram.svg
  ├── sequence-diagram-1.svg  (Order Creation)
  ├── sequence-diagram-2.svg  (Robot Workflow)
  ├── activity-diagram.svg
  └── state-machine.svg
```

---

## Evaluation and Reflection

**This section evaluates the approach and reflects on the development process.**

### Approach & Design Decisions

**Design Philosophy and Architecture**

This implementation adheres to the "Connected Specialist" architecture from Assignment 1, where the HumanoidRobot coordinates operations rather than controlling everything. Following the Single Responsibility Principle (Ampatzoglou et al., 2019), each subsystem handles one concern: `NavigationSystem` manages movement, `SensorArray` handles perception, `Gripper` manipulates items, and `PackingOptimizer` determines packing sequences. This separation enabled isolated testing without affecting the broader system.

The warehouse systems follow similar patterns. The `Warehouse` class maintains inventory using a List with dual indexing, `InventoryManager` provides authoritative environmental data, `TaskManager` holds the FIFO queue of validated orders, and `PackagingStation` offers workspace for staging and packing. This architecture emerged directly from Assignment 1's UML class diagram (Bennett, 2010) and required no major structural changes during implementation.

**Implementation Challenges and Solutions**

Automation modes were initially challenging. From the outset I kept a composition-first design, and I did not want to introduce separate robot subclasses for automation modes. Instead, an automation_mode flag is passed into composed subsystems, which adjust behaviour locally. For example, `NavigationSystem.move_to()` prompts for operator input in semi-automatic mode but proceeds autonomously in full-automatic mode. This keeps the HumanoidRobot as an orchestrator and prevents duplicated logic or brittle inheritance hierarchies (Booch et al., 2005).

Battery management required more realistic consumption patterns. Each operation consumes different power levels, and the robot must intelligently decide when to charge. The `check_battery_and_charge()` method ensures operations never attempt with insufficient power while minimizing unnecessary charging.

State transitions proved complex. The Assignment 1 state machine (Bennett, 2010) showed five states, but determining exact transition moments required careful thought. I chose to transition at operation beginnings for clearer operator feedback.

**Data Structure Justifications**

Data structures directly support the three core operations. The FIFO queue ensures fairness—customers who order first are served first, critical for satisfaction. Python's `collections.deque` (Python Software Foundation, 2024) provides O(1) operations, ensuring the queue never bottlenecks even with hundreds of orders.

The LIFO stack solves physical constraints elegantly. Heavier items must sit at box bottoms, but robots retrieve items arbitrarily. Sorting by weight (ascending) and pushing onto a stack ensures pop operations automatically retrieve heaviest items first. The data structure itself enforces correct behavior without complex logic.

For inventory, dual-indexing balances education with efficiency. The primary list demonstrates operations at O(n), O(n), and O(1) complexity. The hash-based index provides O(1) lookups, with tests showing 10-100x speedup. Real systems often combine multiple structures for diverse requirements.

**Testing Strategy and Validation**

The automated test suite validates correctness and performance of core components using Python's `assert` statement (Python Software Foundation, 2024). Separate modules for List, Queue, Stack, and Search ensure each meets behavioral contracts. Edge case testing proved valuable—discovering empty queues, missing items, and invalid weights could cause silent failures. These tests drove defensive validation throughout.

Integration testing revealed subtle bugs unit tests missed. The workflow test initially failed because the gripper retained items across runs. This led to `clear_items()` cleanup in error paths. Performance testing provided concrete evidence that dual-indexing was justified, measuring actual speedup beyond theoretical analysis.

**Reflection on Development Process**

The most valuable lesson was the power of upfront design. Having detailed UML diagrams (Booch et al., 2005) meant implementation felt like translation rather than invention. I knew what classes were needed, how they should interact, and what data structures to use. When implementation deviated from design (such as adding the sleeper callable for testing), these were conscious improvements rather than desperate fixes.

If redoing this project, I would make the system more configurable. Currently, parameters live in `config.py` as constants, but production systems benefit from external configuration files allowing parameter tuning without code changes (Van Rossum et al., 2001). This would demonstrate the open/closed principle at system level.

The "Connected Specialist" architecture proved remarkably robust. As requirements evolved—adding battery management, implementing dual automation modes, supporting quantity-based orders—the modular design accommodated changes without restructuring. This validated the architectural decisions from the design phase and reinforced the value of SOLID principles (Ampatzoglou et al., 2019) in creating maintainable software.

---

## References

Ampatzoglou, A. et al. (2019) 'Applying the Single Responsibility Principle in Industry: Modularity Benefits and Trade-offs', *Proceedings of the 41st International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP'19)*, pp.281–290. Available at: https://doi.org/10.1145/3319008.3320125 (Accessed: 1 October 2025).

Bennett, S. (2010) *Object-Oriented Systems Analysis and Design Using UML*. London: McGraw-Hill UK Higher Ed. Available at: ProQuest Ebook Central https://ebookcentral.proquest.com/lib/ (Accessed: 2 October 2025).

Booch, G., Rumbaugh, J. and Jacobson, I. (2005) *The Unified Modeling Language User Guide*. 2nd edn. Boston: Addison-Wesley Professional.

### Python Documentation

Python Software Foundation (2024) *collections — Container datatypes*. Available at: https://docs.python.org/3/library/collections.html (Accessed: 30 September 2025).

Python Software Foundation (2024) *dataclasses — Data Classes*. Available at: https://docs.python.org/3/library/dataclasses.html (Accessed: 30 September 2025).

Python Software Foundation (2024) *enum — Support for enumerations*. Available at: https://docs.python.org/3/library/enum.html (Accessed: 30 September 2025).

### Style Guide

Van Rossum, G., Warsaw, B. and Coghlan, N. (2001) *PEP 8 – Style Guide for Python Code*. Available at: https://peps.python.org/pep-0008/ (Accessed: 30 September 2025).

### Testing Resources

Python Software Foundation (2024) *assert statement*. Available at: https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement (Accessed: 30 September 2025).

---

## Project Structure

```
humanoid-robot/
│
├── main.py                      # Entry point (run with: python main.py)
├── README.md                    
│
├── docs/                        
│   ├── class-diagram.svg
│   ├── sequence-diagram-1.svg
│   ├── sequence-diagram-2.svg
│   ├── activity-diagram.svg
│   └── state-machine.svg
│
└── humanoidrobot/
    ├── __init__.py
    ├── app.py                   # Main CLI coordinator
    ├── cli.py                   # User interface commands
    ├── config.py                # System constants
    ├── models.py                # Data models (Item, Order, Task)
    ├── robot.py                 # Main robot controller
    ├── subsystems.py            # Robot subsystems (Navigation, Sensors, Gripper, Packing)
    ├── utils.py                 # Helper functions
    ├── warehouse.py             # Warehouse management (Inventory, Tasks, Station)
    │
    └── tests/
        ├── __init__.py
        ├── run.py               # Test runner (can run: python -m humanoidrobot.tests.run)
        ├── test_list.py         # List data structure tests
        ├── test_queue.py        # Queue (FIFO) tests
        ├── test_stack.py        # Stack (LIFO) tests
        ├── test_search.py       # Search algorithm tests
        ├── test_edge.py         # Edge case tests
        └── test_integration.py  # Integration tests
```

---

**Author:** Ruben Marques
**Tutor:** Stelios Sotiriadis
**Module:** OOP
**Date:** October 2025
