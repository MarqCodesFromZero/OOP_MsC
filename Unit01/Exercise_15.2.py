#######################################################################
#Exercise 15.2
#######################################################################

import turtle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Define a Circle
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

# Define a Rectangle
class Rectangle:
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner

# Define a function to draw a rectangle
def draw_rect(t, rect):
    # Lift the pen to avoid drawing while positioning
    t.penup()
    # Move to the starting corner of the rectangle
    t.goto(rect.corner.x, rect.corner.y)
    # Lower the pen to start drawing
    t.pendown()
    # Draw the rectangle
    for _ in range(2):
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
        t.left(90)

# Define a function to draw a circle
def draw_circle(t, circle):
    # Lift the pen to avoid drawing while positioning
    t.penup()
    # Move to the center of the circle
    t.goto(circle.center.x, circle.center.y - circle.radius)
    # Lower the pen to start drawing
    t.pendown()
    # Draw the circle
    t.circle(circle.radius)

# Create a Turtle object
SCREEN = turtle.Screen()
turt = turtle.Turtle()

# Instantiate a Rectangle object
rectangle = Rectangle(100, 50, Point(-50, -50))

# Instantiate a Circle object
circ = Circle(Point(0, 0), 75)

# Draw the rectangle
draw_rect(turt, rectangle)

# Draw the circle
draw_circle(turt, circ)

# Keep the window open until it is closed by the user
SCREEN.mainloop()
