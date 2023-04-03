# Transport can be anything. Horse, boat, airplane

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

    def __init__(self):
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

    veh = Vehicle()
    veh.move()
    veh.stop()

    car1 = Car('Tesla')
    car1.move()
    car1.stop()

    car2 = Car('Tesla', color='red')
    car2.move()
    car2.stop()
    print('Total vehicle:' + str(Vehicle.get_vehicle_num()))
    print('100 km/h = ' + str(Car.convert_kmh_to_mph(100)) + ' mph')

    plane = Airplane()
    plane.move()
    plane.stop()
    print('Total vehicle:' + str(Vehicle.get_vehicle_num()))

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
