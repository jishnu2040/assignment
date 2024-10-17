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



# propert() using validation

class Employee:
    def __init__(self, salary):
        self._salary = salary

    def get_salary(self):
        return self._salary

    def set_salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

    salary = property(get_salary, set_salary)

e = Employee(5000)
e.salary = 6000   # Valid
# e.salary = -1000  # Raises ValueError: Salary cannot be negative



