"""
An abstract class in Python is a class that cannot be instantiated on its own and is meant to serve as a blueprint for other classes.
Abstract classes are crucial in software development to enforce consistency, standardize behavior across multiple subclasses, 
and make your code more maintainable.

They are commonly used in: Authentication systems  , Payment processing systems , Database handling, File operations, Notification systems, Machine learning models


"""



from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @abstractmethod
    def get_salary(self):
        pass

class FulltimeEmployee(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def get_salary(self):
        return self.salary

class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, worked_hours, rate):
        super().__init__(first_name, last_name)
        self.worked_hours = worked_hours
        self.rate = rate

    def get_salary(self):
        return self.worked_hours * self.rate


class Payroll:
    def __init__(self):
        self.employee_list = []

    def add(self, employee):
        self.employee_list.append(employee)

    def print(self):
        for e in self.employee_list:
            print(f"{e.full_name} \t ${e.get_salary()}")
            # Polymorphism: Both FulltimeEmployee and HourlyEmployee implement the get_salary() method differently, but they are both treated as Employee objects in the Payroll class.




payroll = Payroll()

payroll.add(FulltimeEmployee('John', 'Doe', 6000))
payroll.add(FulltimeEmployee('Jane', 'Doe', 6500))
payroll.add(HourlyEmployee('Jenifer', 'Smith', 200, 50))
payroll.add(HourlyEmployee('David', 'Wilson', 150, 100))
payroll.add(HourlyEmployee('Kevin', 'Miller', 100, 150))

payroll.print()



# output:
# John Doe         $6000
# Jane Doe         $6500
# Jenifer Smith    $10000
# David Wilson     $15000
# Kevin Miller     $15000


"""
Why Use Abstract Classes Here?

Enforce Common Behavior:
The abstract class ensures that every subclass of Employee must implement the get_salary() method, thus enforcing a consistent interface.

Extensibility:
If you wanted to add new types of employees (e.g., ContractEmployee), you could simply subclass Employee and implement get_salary()
without modifying the existing code in the Payroll class.
"""
