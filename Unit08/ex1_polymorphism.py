""" Polymorphism Exercise 1"""

"""Polymorphism lets the same function or method name 
behave differently depending on the object that calls it."""

import random

# Parent class: Lottery
class Lottery:
    "Lottery numbers"

    def shuffle(self):
        # Initialize an empty list to store the results
        results = []
        # Generate 5 random integers between 1 and 20
        for i in range(5):
            results.append(random.randint(1, 20))
        # Return the list of results
        return results

# Child class: PowerBall (inherits from Lottery)
class PowerBall(Lottery):
    """Child class of Lottery"""

    def shuffle(self):
        # Override the shuffle method to generate 6 random integers between 1 and 99
        results = []
        for i in range(6):  # Generate 6 random numbers for PowerBall
            results.append(random.randint(1, 99))
        return results

# Testing the classes
if __name__ == "__main__":
    # Create an instance of PowerBall
    powerball = PowerBall()
    # Call the shuffle method of PowerBall
    powerball_numbers = powerball.shuffle()
    # Print the shuffled numbers
    print("PowerBall Numbers:", powerball_numbers)