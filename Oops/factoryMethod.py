class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @classmethod
    def create_anonymous(cls):
        return cls('Jishnu', 25) 

# Create an anonymous person
anonymous = Person.create_anonymous()
print(anonymous.name, anonymous.age)  
