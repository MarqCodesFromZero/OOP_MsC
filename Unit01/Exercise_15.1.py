"""
Exercise 15.1
"""

# Define a Point class to represent a point
class Point:
    # Initialize the coordinates
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Define a Circle class
class Circle:
    # Initialize the center and radius 
    def __init__(self, center, radius):
        # Set the center point and radius
        self.center = center
        self.radius = radius

# Function to check if a point is inside or on the boundary of a circle
def point_in_circle(circle, point):
    # Calculate the distance squared between the point and the center of the circle
    distance_squared = (point.x - circle.center.x) ** 2 + (point.y - circle.center.y) ** 2
    # Return True if the distance squared is less than or equal to the square of the circle's radius
    return distance_squared <= circle.radius ** 2

# Function to check if a rectangle is completely inside a circle
def rect_in_circle(circle, rect):
    # Check if all four corners of the rectangle are within or on the boundary of the circle
    for corner in rect.corners():
        if not point_in_circle(circle, corner):
            return False
    return True

# Function to check if a rectangle overlaps with a circle
def rect_circle_overlap(circle, rect):
    # Check if any of the corners of the rectangle fall inside the circle
    for corner in rect.corners():
        if point_in_circle(circle, corner):
            return True
    # Check if any part of the rectangle falls inside the circle
    for corner in rect.corners():
        # Calculate the distance between the corner and the center of the circle
        distance = ((corner.x - circle.center.x) ** 2 + (corner.y - circle.center.y) ** 2) ** 0.5
        # If the distance is less than the circle's radius, return True
        if distance < circle.radius:
            return True
    return False

# Define a Rectangle class to represent a rectangle
class Rectangle:
    # Initialize the width, height, and corner
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner

    # Method to get the corners of the rectangle
    def corners(self):
        return [
            Point(self.corner.x, self.corner.y),
            Point(self.corner.x + self.width, self.corner.y),
            Point(self.corner.x, self.corner.y + self.height),
            Point(self.corner.x + self.width, self.corner.y + self.height)
        ]

# Instantiate a Circle object with center at (150, 100) and radius 75
circ = Circle(Point(150, 100), 75)

# Usage
p = Point(160, 110)
print("Point in circle:", point_in_circle(circ, p))

rectangle = Rectangle(20, 30, Point(140, 90))
print("Rectangle in circle:", rect_in_circle(circ, rectangle))

overlap_rect = Rectangle(40, 40, Point(160, 110))
print("Rectangle-circle overlap:", rect_circle_overlap(circ, overlap_rect))
