"""Recursively add numbers in a list"""

def list_sum(numbers):
    # Base case: If the list is empty, the sum is 0
    if not numbers:
        return 0
    else:
        # Recursive case: Add the first element to the sum of the rest of the list
        return numbers[0] + list_sum(numbers[1:])

# Test cases
print(list_sum([1, 2, 3, 4, 5]))  # Output: 15
print(list_sum([10, 12.5, 10, 7]))  # Output: 39.5