from car import Car

my_car = Car('Ford', 'Focus', '2020', 'blue', mirror=3)
my_car.drive()
my_car.stop()

print('car num:' + str(my_car.car_of_num))

another_car = Car('Toyota', 'RAV4', '2018', 'silver', doors=5)
another_car.drive()
another_car.stop()

print('car num:' + str(another_car.car_of_num))
another_car.set_car_num(5)
print('car num:' + str(my_car.car_of_num))
print('car num:' + str(another_car.car_of_num))
Car.set_car_num(6)
print('car num:' + str(my_car.car_of_num))
print('car num:' + str(another_car.car_of_num))

print(my_car.wheels)
print(another_car.wheels)

another_car.wheels = 8

print(my_car.wheels)
print(another_car.wheels)


print(my_car)
