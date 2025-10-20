"""Recursion EX 1"""

def recursive_sum(n):
    # Base case: If n is 0, return 0 as the sum is zero
    if n == 0:
        return 0
    else:
        # Recursive case: Return the current number (n) added to the sum of numbers from 0 to n-1
        return n + recursive_sum(n - 1)

# Test cases
print(recursive_sum(5))  # Output: 15
print(recursive_sum(10))  # Output: 55