
"""Polymorphism Exercise 2"""

class Airplane:
    def __init__(self, first_class:int, business_class:int, coach:int):
        # Initialize Airplane with the number of passengers in first class, business class, and coach
        self.first_class = first_class
        self.business_class = business_class
        self.coach = coach

    def total(self):
        # Calculate and return the total number of passengers on board the airplane
        return self.first_class + self.business_class + self.coach

class Train:
    def __init__(self, car1, car2, car3, car4, car5):
        # Initialize Train with the number of passengers in each of the 5 cars
        self.car1 = car1
        self.car2 = car2
        self.car3 = car3
        self.car4 = car4
        self.car5 = car5

    def total(self):
        # Calculate and return the total number of passengers on board the train
        return self.car1 + self.car2 + self.car3 + self.car4 + self.car5

def passengers(obj):
    # Call the total method of the passed object to get the total number of passengers
    print(f'There are {obj.total()} passengers on board.')

# Testing the function with instances of Airplane and Train
if __name__ == "__main__":

    # Create an instance of Airplane with passenger counts for each class
    airplane = Airplane(first_class=10, business_class=20, coach=50)

    # Call the passengers function with the Airplane instance
    passengers(airplane)  # Output: There are 80 passengers on board.

    # Create an instance of Train with passenger counts for each car
    train = Train(car1=30, car2=40, car3=50, car4=60, car5=70)
    
    # Call the passengers function with the Train instance
    passengers(train)  # Output: There are 250 passengers on board.