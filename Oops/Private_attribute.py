class Counter:
    def __init__(self):
        self.__current = 0

    def increment(self):
        self.__current += 1

    def value(self):
        return self.__current

    def reset(self):
        self.__current = 0


# input 
counter = Counter()
print(counter._Counter__current)

using class name as prifix, then only attribute can access


