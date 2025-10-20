"""Biggest number in a list recursively"""


def get_max(numbers):
    # Base case: If the list has only one element, return that element as the maximum number
    if len(numbers) == 1:
        return numbers[0]
    else:
        # Recursive case: Compare the first element with the maximum of the rest of the list
        # If the first element is greater, return it; otherwise, recursively find the maximum in the rest of the list
        return numbers[0] if numbers[0] > get_max(numbers[1:]) else get_max(numbers[1:])

# Test cases
print(get_max([1, 2, 3, 4, 5]))   # Output: 5
print(get_max([11, 22, 3, 41, 15])) # Output: 41
