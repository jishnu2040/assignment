class Circle:
    def __init__(self, radius):
        self._radius = radius

    # Getter method
    def get_radius(self):
        return self._radius

    # Setter method
    def set_radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    # Using property to treat radius like an attribute
    radius = property(get_radius, set_radius)

# Using the class
c = Circle(5)
print(c.radius)  # Calls get_radius() and prints 5
c.radius = 10    # Calls set_radius(10)
print(c.radius)  # Prints 10
