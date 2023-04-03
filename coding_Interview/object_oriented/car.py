
class Car:
    car_of_num = 0
    wheels = 4  # Class Variable

    def __init__(self, make, model, year, color, doors=4, mirror=2):
        self.make = make    # Instance Variable
        self.model = model
        self.year = year
        self.color = color
        self.doors = doors
        self.mirror = mirror
        Car.car_of_num += 1

    def drive(self):
        print('This '+self.color+' car is driving')

    def stop(self):
        print('This '+self.color+' car is stopped')

    @classmethod
    def set_car_num(cls, num):
        cls.car_of_num = num

    @staticmethod
    def get_mph_speed(kmh):
        KMH_TO_MPH = 0.6214
        return kmh * KMH_TO_MPH

    def __str__(self):
        return "Car Model:" + self.model


if __name__ == "__main__":
    print('This is a Car class.')

    my_car = Car('A', 'B', 'C', 'D')

    print(my_car)

    print('100 km/h = ' + str(Car.get_mph_speed(100)) + ' mph')
