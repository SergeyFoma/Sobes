class Car:
    def __init__(self, color, speed):
        self.color=color
        self.speed = speed

my_car = Car
my_car.color='red'
my_car.speed = 250
print(my_car.color, my_car.speed)

my_car2=Car('Blue', '300 km/h')
print(my_car2.color, my_car2.speed)

