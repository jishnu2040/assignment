class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

  def __str__(self):
    return f'Person({self.first_name} {self.last_name},{self.age}old)'

# Internally, Python will call the __str__ method automatically when an instance calls the str() method.

person = Person('John', 'Doe', 25)
print(person)

# o/p:
# Person(John Doe,25 old)

# __repr__(self) : he __str__ method returns a string representation of an object that is human-readable while the __repr__ method 
# returns a string representation of an object that is machine-readable.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    person = Person('John', 25)


# __del__ (self): methos python has garbeg collector that remove data from memoriy once there no any more , but __but__ do this job manually..........

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print('__del__ was called')


if __name__ == '__main__':
    person = Person('John Doe', 23)
    person = None



