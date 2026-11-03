
# Define Circle class
import math

class Circle:

    def __init__(self, radius):
        self.radius = radius

    # Method to calculate area
    def get_area(self):
        return math.pi * self.radius ** 2

    # Method to calculate circumference
    def get_circumference(self):
        return 2 * math.pi * self.radius


# Create an object
radius = float(input("Enter the radius: "))

c = Circle(radius)

# Display results
print("Area of Circle:", round(c.get_area(), 2))
print("Circumference of Circle:", round(c.get_circumference(), 2))
