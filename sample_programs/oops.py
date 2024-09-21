
class Car:
    company ="maruti"
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def start(self):
        print("vroom vroom")


c1 = Car('ciaz', '78')
c2 = Car('innova', '89')
c1.start()
print(c1.year)
print(c1.name)
print(Car.company)