class Person:
    """Represents a generic Person."""
    def __init__(self, first, last, weight, height):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height

# Create five Person objects with appropriate values
p1 = Person('Tom', 'Thumb', 150, 68)
p2 = Person('Fred', 'Flintstone', 200, 72)
p3 = Person('George', 'Washington', 180, 70)
p4 = Person('Tanya', 'Adams', 140, 65)
p5 = Person('Mary', 'Smith', 130, 63)

# Create a list and store the Person objects in the list
person_list = [p1, p2, p3, p4, p5]

# Iterate over the list and print out the first names of each Person object
for person in person_list:
    print(person.first_name)
