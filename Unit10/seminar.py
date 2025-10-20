import unittest


def add(x, y):
    """
    Add two numbers together.
    
    Args:
        x (float): The first number
        y (float): The second number
        
    Returns:
        float: The sum of x and y
    """
    return x + y


def subtract(x, y):
    """
    Subtract the second number from the first.
    
    Args:
        x (float): The number to subtract from
        y (float): The number to subtract
        
    Returns:
        float: The difference between x and y
    """
    return x - y


def multiply(x, y):
    """
    Multiply two numbers together.
    
    Args:
        x (float): The first number
        y (float): The second number
        
    Returns:
        float: The product of x and y
    """
    return x * y


def divide(x, y):
    """
    Divide the first number by the second.
    
    Args:
        x (float): The dividend (number to be divided)
        y (float): The divisor (number to divide by)
        
    Returns:
        float: The quotient of x divided by y
        
    Raises:
        ZeroDivisionError: If y is zero
    """
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y


# ============================================================================
# UNIT TESTS
# ============================================================================

class TestCalculatorOperations(unittest.TestCase):
    """
    Unit tests for calculator operations.
    
    This test suite covers all arithmetic operations including
    edge cases and error conditions.
    """
    
    def test_add_positive_numbers(self):
        """Test addition of two positive numbers."""
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(10.5, 2.5), 13.0)
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(5, -3), 2)
    
    def test_add_zero(self):
        """Test addition with zero."""
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, 5), 5)
    
    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(subtract(5.5, 2.5), 3.0)
    
    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(-5, 3), -8)
        self.assertEqual(subtract(5, -3), 8)
    
    def test_subtract_zero(self):
        """Test subtraction with zero."""
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(0, 5), -5)
    
    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        self.assertEqual(multiply(4, 3), 12)
        self.assertEqual(multiply(2.5, 4), 10.0)
    
    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(multiply(-4, 3), -12)
        self.assertEqual(multiply(-4, -3), 12)
        self.assertEqual(multiply(4, -3), -12)
    
    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(0, 0), 0)
    
    def test_multiply_by_one(self):
        """Test multiplication by one (identity property)."""
        self.assertEqual(multiply(5, 1), 5)
        self.assertEqual(multiply(1, 5), 5)
    
    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(7, 2), 3.5)
    
    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(10, -2), -5)
        self.assertEqual(divide(-10, -2), 5)
    
    def test_divide_by_one(self):
        """Test division by one (identity property)."""
        self.assertEqual(divide(5, 1), 5)
        self.assertEqual(divide(-5, 1), -5)
    
    def test_divide_zero_by_number(self):
        """Test zero divided by a number."""
        self.assertEqual(divide(0, 5), 0)
        self.assertEqual(divide(0, -5), 0)
    
    def test_divide_by_zero_raises_error(self):
        """Test that division by zero raises ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
        with self.assertRaises(ZeroDivisionError):
            divide(0, 0)
    
    def test_floating_point_precision(self):
        """Test operations with floating-point numbers."""
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)
        self.assertAlmostEqual(multiply(0.1, 0.2), 0.02, places=7)


# ============================================================================
# MAIN PROGRAM
# ============================================================================

def main():
    """
    Main calculator program loop.
    
    Displays a menu, accepts user input, and performs calculations
    until the user chooses to exit.
    """
    print("=" * 50)
    print("SIMPLE CALCULATOR")
    print("=" * 50)
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("=" * 50)
    
    while True:
        choice = input("\nEnter choice (1/2/3/4): ")
        
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    result = add(num1, num2)
                    print(f"{num1} + {num2} = {result}")
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"{num1} - {num2} = {result}")
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"{num1} * {num2} = {result}")
                elif choice == '4':
                    try:
                        result = divide(num1, num2)
                        print(f"{num1} / {num2} = {result}")
                    except ZeroDivisionError as e:
                        print(f"Error: {e}")
                
                next_calculation = input("\nDo another calculation? (yes/no): ")
                if next_calculation.lower() == "no":
                    print("Thank you for using the calculator!")
                    break
                    
            except ValueError:
                print("Error: Please enter valid numbers")
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    # Run unit tests if --test flag is used
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print("Running unit tests...\n")
        unittest.main(argv=[''], verbosity=2, exit=False)
    else:
        main()