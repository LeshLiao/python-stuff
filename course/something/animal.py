
class Animal:
    name = ''
    def __init__(self, name):
        self.name = name
    def walk(self):
        print('Animal walk!')

class Cat(Animal):
    age = 3
    def __init__(self):
        pass
    def walk(self):
        print('Cat walk!')

animal = Cat()
animal.walk()