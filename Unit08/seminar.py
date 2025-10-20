"""
Activity 1: Exception Handling
Activity 2: Data Structures (Set Operations & Linear Search)
"""

# ============================================================================
# ACTIVITY 1: EXCEPTION HANDLING
# ============================================================================

def divide_numbers(a, b):
    """
    Demonstrates exception handling with try-except blocks.
    Attempts to divide two numbers and handles various exceptions.
    """
    try:
        # Attempt to perform division
        result = int(a) / int(b)
        print(f"Division result: {a} / {b} = {result}")
        return result

    except ValueError:
        # Handle ValueError - occurs when conversion to int fails
        print("Error: Invalid input. Please enter valid integer values.")

    except ZeroDivisionError:
        # Handle ZeroDivisionError - occurs when dividing by zero
        print("Error: Cannot divide by zero.")

    except (TypeError, KeyError):
        # Handle multiple exceptions - TypeError and KeyError
        print("Error: Type or key error occurred. Check your input.")

    finally:
        # This block executes regardless of whether exception occurred
        print("Division operation attempt completed.\n")


def process_employee_data(employees, employee_id):
    """
    Demonstrates exception handling in accessing employee data.
    Used in context of employee management system 
    """
    try:
        # Attempt to access employee record
        employee = employees[employee_id]
        annual_leave = employee['annual_leave']

        # Calculate leave days remaining
        remaining_leave = 20 - annual_leave
        print(f"Employee: {employee['name']}")
        print(f"Annual leave taken: {annual_leave} days")
        print(f"Remaining leave: {remaining_leave} days\n")

    except KeyError:
        # Handle missing employee ID or missing dictionary keys
        print(f"Error: Employee ID {employee_id} not found in records.\n")

    except TypeError:
        # Handle type errors (e.g., wrong data type for calculation)
        print("Error: Invalid employee data format.\n")

    except ValueError:
        # Handle value errors in calculations
        print("Error: Invalid leave values.\n")


# ============================================================================
# ACTIVITY 2 DATA STRUCTURES - SET OPERATIONS
# ============================================================================

def explain_set_operations():
    """
    Explains set operations in context of employee management system.
    """
    print("="*70)
    print("SET OPERATIONS & THEIR USES IN EMPLOYEE MANAGEMENT")
    print("="*70)
    print()

    # Example sets
    engineers = {"Alice", "Bob", "Carol", "David"}
    managers = {"Bob", "Carol", "Eve", "Frank"}

    print("Engineers:", engineers)
    print("Managers:", managers)
    print()

    # 1. UNION
    print("1. UNION - Combine all unique members from both sets")
    print("   Use case: Find all employees in either Engineering OR Management")
    union_result = engineers | managers  # or engineers.union(managers)
    print(f"   Union Result: {union_result}")
    print(f"   All staff: {union_result}")
    print()

    # 2. INTERSECTION
    print("2. INTERSECTION - Find common members in both sets")
    print("   Use case: Find employees who are both Engineers AND Managers")
    intersection_result = engineers & managers  # or engineers.intersection(managers)
    print(f"   Intersection Result: {intersection_result}")
    print(f"   Dual-role employees: {intersection_result}")
    print()

    # 3. DIFFERENCE
    print("3. DIFFERENCE - Find members in first set but NOT in second")
    print("   Use case: Find Engineers who are NOT Managers")
    difference_result = engineers - managers  # or engineers.difference(managers)
    print(f"   Difference Result: {difference_result}")
    print(f"   Pure engineers: {difference_result}")
    print()

    # 4. SYMMETRIC DIFFERENCE
    print("4. SYMMETRIC DIFFERENCE - Find members in either set but NOT both")
    print("   Use case: Find employees in ONLY one department (not both)")
    sym_diff_result = engineers ^ managers  # or engineers.symmetric_difference(managers)
    print(f"   Symmetric Difference Result: {sym_diff_result}")
    print(f"   Single-role employees: {sym_diff_result}")
    print()


# ============================================================================
# ACTIVITY 2: DATA STRUCTURES - LINEAR SEARCH
# ============================================================================

def linear_search(data_list, target):
    """
    Performs a linear search on a list to find a target value.
    
    Linear Search:
    - Checks each element sequentially from start to end
    - Returns index if found, -1 if not found
    - Time Complexity: O(n)
    - Works on unsorted and sorted lists
    
    Args:
        data_list: List to search
        target: Value to find
        
    Returns:
        Index of target if found, -1 otherwise
    """
    try:
        for index in range(len(data_list)):
            if data_list[index] == target:
                print(f"Found '{target}' at index {index}")
                return index

        # If loop completes without finding target
        print(f"'{target}' not found in the list")
        return -1
  
    except TypeError:
        print("Error: Cannot search - list contains incompatible data types")
        return -1

def linear_search_employee_id(employees, target_id):
    """
    Linear search specifically for employee IDs in employee database.
    Demonstrates practical use of linear search.
    """
    try:
        for index, emp_id in enumerate(employees):
            if emp_id == target_id:
                print(f"Employee ID '{target_id}' found at position {index}")
                return index
        
        print(f" Employee ID '{target_id}' not found")
        return -1
        
    except TypeError:
        print("Error: Invalid employee ID format")
        return -1


# ============================================================================
# DEMONSTRATION
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("ACTIVITY 1: EXCEPTION HANDLING DEMONSTRATION")
    print("="*70 + "\n")
    
    # Test divide_numbers with various inputs
    print("Test 1: Normal division")
    divide_numbers(10, 2)
    
    print("Test 2: Division by zero")
    divide_numbers(10, 0)
    
    print("Test 3: Invalid input (non-numeric)")
    divide_numbers("abc", 5)
    
    # Test employee data processing
    print("Test 4: Process employee data")
    employees_db = {
        "EMP001": {"name": "Alice Johnson", "annual_leave": 5},
        "EMP002": {"name": "Bob Smith", "annual_leave": 12},
        "EMP003": {"name": "Carol Davis", "annual_leave": 8}
    }
    
    process_employee_data(employees_db, "EMP001")
    process_employee_data(employees_db, "EMP999")  # Non-existent ID
    
    # Set operations explanation and demonstration
    print("\n" + "="*70)
    print("ACTIVITY 2A: SET OPERATIONS")
    print("="*70 + "\n")
    explain_set_operations()
    
    # Linear search demonstration
    print("="*70)
    print("ACTIVITY 2B: LINEAR SEARCH")
    print("="*70 + "\n")
    
    # Test linear search on numbers
    numbers = [23, 45, 12, 56, 34, 78, 90, 11, 5, 67]
    print(f"Searching in list: {numbers}\n")
    
    linear_search(numbers, 56)
    linear_search(numbers, 99)
    linear_search(numbers, 23)
    
    print()
    
    # Test linear search on employee IDs
    employee_ids = ["EMP001", "EMP002", "EMP003", "EMP004", "EMP005"]
    print(f"Searching employee IDs: {employee_ids}\n")
    
    linear_search_employee_id(employee_ids, "EMP003")
    linear_search_employee_id(employee_ids, "EMP010")
    
    print("\n" + "="*70)