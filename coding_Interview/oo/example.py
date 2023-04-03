# Transport can be anything. Horse, boat, airplane
"""
Note: It's different with Java programming.

1. subclass constructor __init__ will override super class constructor __init__
    which means instantiate a subclass that won't call super class __init__
    unless subclass have no constructor.
2. Ducking type is similar to interface of Java.

3. The private attributes using double underscore as the prefix

4. static variable is different with instance variable
    once you change class variable by instance, it turn into individual variable.
    Ex:
        Vehicle.vehicle_num = 123 # change Class variable and instance variable
        # If change value of instance
         car1 = Car('Tesla')
         car1.vehicle_num = 456  # this variable is not same with Class variable
    Conclusion:
        If you wanna using static variable.
        Just use class variable:
            Vehicle.vehicle_num = 123
"""
from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Vehicle(Transport):
    vehicle_num = 0
    __my_private_variable = 'vehicle private data'

    def __init__(self):
        print('Vehicle__init__')
        Vehicle.vehicle_num += 1

    def move(self):
        print('The Vehicle is moving...')

    def stop(self):
        print('The Vehicle stopped.')

    @classmethod
    def get_vehicle_num(cls):
        return cls.vehicle_num


class Car(Vehicle):
    def __init__(self, model, color='white'):
        super().__init__()
        self.model = model
        self.color = color
        pass

    def move(self):
        print('The ' + self.model + ' is moving...')

    def stop(self):
        print('The ' + self.color + ' car stopped.')

    @staticmethod
    def convert_kmh_to_mph(kmh):
        KMH_TO_MPH = 0.6214
        return kmh * KMH_TO_MPH

    def __str__(self):
        pass


class Airplane(Vehicle):
    def move(self):
        print('The airplane is taking off...')

    def stop(self):
        print('The airplane arrived')

    def fly(self):
        print('The plane is flying...')


class Duck():
    def fly(self):
        print('The Duck is flying...')

    def eat(self):
        print('The Duck is eating...')


class Horse(Transport):
    def move(self):
        print('The Horse is running...')

    def stop(self):
        print('The Horse stopped.')

    def eat(self):
        print('The Horse is eating...')


if __name__ == "__main__":

    # tr = Transport() # Can't instantiate abstract class

    # instantiate superclass
    veh = Vehicle()
    veh.move()
    veh.stop()
    print('Total vehicle:' + str(Vehicle.vehicle_num))

    # instantiate subclass
    car1 = Car('Tesla')
    car1.move()
    car1.stop()
    print('Total vehicle:' + str(Vehicle.vehicle_num))

    # instantiate subclass
    car2 = Car('Tesla', color='red')
    car2.move()
    car2.stop()
    print('Total vehicle:' + str(Vehicle.vehicle_num))

    # we denote private attributes using double underscore as the prefix
    # print('Get private value:' + str(car2.__my_private_variable)) # can not get private variable

    # using staticmethod
    print('100 km/h = ' + str(round(Car.convert_kmh_to_mph(100), 2)) + ' mph')

    plane = Airplane()
    plane.move()
    plane.stop()

    print('Total vehicle:' + str(Vehicle.vehicle_num))
    print('Total vehicle(instance):' + str(plane.vehicle_num))

    horse = Horse()
    horse.move()
    horse.stop()

    # Ducking type
    duck = Duck()
    fly_list = [plane, duck]
    for item in fly_list:
        item.fly()

    eat_list = [duck, horse]
    for item in eat_list:
        item.eat()
