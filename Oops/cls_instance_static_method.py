class Person:
    
    
    @staticmethod
    def add_numbers(x, y):
        return x + y
    
    # this is class attribute
    description = "this is the Person class for all object distribusion!!!"
    counter = 0
    
    # this is class method
    @classmethod
    def create_anonymous(cls):
        Person.description = "empty description!!!!!!!"
        return Person('Anonymous', 22)
    

    
    # this is instance atrribute
    def __init__(self, name, height):
        self.name = name
        self.height = height
        Person.counter += 1
    # this is instance method
    def great(self):
        return f"hai my name is {self.name} and my height is {self.height} !"
    

amal = Person('amal',167)
priya = Person('priya',152)


anonymous = Person.create_anonymous()
print(anonymous.height) 

print(Person.description)
print(amal.counter)
