
class Duck:

    def __init__(self, name):
        self.name = name

    def quack(self):
        print('Quack!')


class Car:

    def __init__(self, model):
        self.model = model

    def quack(self):
        print('I can quack, too!')


def quacks(obj):
    obj.quack()


donald = Duck('Donald Duck')
car = Car('A car')
car2 = Car('A car2')
list = [donald, car, car2]

for item in list:
    quacks(item)
