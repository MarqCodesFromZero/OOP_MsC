"""Double amount"""

def double(amount):
    # Base case: If there is no amount to double, return 0
    if amount == 0:
        return 0
    else:
        # Recursive case: Return 2 for each 
        # and add the rest for (amount - 1)
        return 2 + double(amount - 1)

# Test cases
print(double(8))  # Output: 16
print(double(0))  # Output: 0
print(double(200))