# Полиморфизм — принцип объектно-ориентированного программирования (ООП),
# позволяющий использовать объекты разных классов через единый интерфейс.
# https://habr.com/ru/articles/552922/


class Car:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power

    def tax(self):
        rate = 10
        return self.power * rate


class Bus:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power

    def tax(self):
        rate = 50
        return self.power * rate


car1 = Car("BMW", "B1", 100)
bus1 = Bus("Bus1", "Bus111", 100)

for i in (car1, bus1):
    print(f"{i.brand},\n{i.model},\n{i.tax()}")

print("------------------------------")


class Dealer:
    def __init__(self):
        self.cars = []

    def set_add_car(self, car):
        self.cars.append(car)

    def total_tax(self):  # метод вычисления налогов
        tax = 0
        for car in self.cars:
            tax += car.tax()
        return tax


bmw = Car("BMW", "bmw", 120)
audi = Car("Audi", "audi", 100)
bus1 = Bus("BUS1", "bus1", 300)

dealer = Dealer()
dealer.set_add_car(bmw)
dealer.set_add_car(audi)
dealer.set_add_car(bus1)

print(dealer.total_tax())


# расширение конструктора
class Auto:
    def __init__(self, brand, model, power):
        self.brand = brand.lower()
        self.model = model
        self.power = power

    def get_tax(self):
        rate = 10
        return self.power * rate


class Buss(Auto):
    # def __init__(self, brand, model, power): # variant 1,2
    def __init__(self, brand, model, power, seating, standing=0):  # вариант 3
        # brand=f'Autobus: {brand}' # расширяем конструктор вариант 1
        super().__init__(brand, model, power)
        # self.brand=f'Autobusik: {self.brand.upper()}' # расширяем конструктор вариант 2
        self.seating = 0
        self.standing = 0
        self.set_places(seating, standing)  # variant 3

    def set_places(self, seating, standing=0):
        self.seating = seating
        self.standing = standing

    def total_places(self):
        return self.standing + self.seating

    def get_tax(self):
        rate = 10
        return self.power * rate + 10


bmw = Auto("BMW", "bmw1", 100)

# bus=Buss('Bus', 'bus', 100)
bus = Buss("Bus", "bus", 100, 30, 10)  # variant 3

print(
    bmw.brand,
    bmw.get_tax(),
    " ",
    bus.brand,
    bus.get_tax(),
    f"Places bus- {bus.total_places()}, {bus.seating}",
)

print("-----------------------------------")


# Расширение методов
class Auto2:
    def __init__(self, brand, model, power):
        self._brand=brand 
        self._model=model 
        self._power=power 

    # def get_tax(self):
    #     rate = 10
    #     if self._power > 100:
    #         rate = 15
    #     return rate * self._power

    def get_tax(self): # variant 2
        return self._calc_tax(10, 15)

    def _calc_tax(self, min_rate, max_rate): 
        rate = min_rate 
        if self._power > 100:
            rate = max_rate 
        return rate * self._power
    
class Bus2(Auto2):
    def __init__(self, brand, model, power, seating, stading):
        super().__init__(brand, model, power)
        self.seating=seating
        self.stading=stading
    # def get_tax(self):
    #     rate=20
    #     if self._power>300:
    #         rate=30
    #     return rate * self._power

    # def get_tax(self): # расширяем метод get_tax методом из родительского класса
    #     tax=super().get_tax()
    #     return tax * 1.5

    def get_tax(self): # variant 2
        return super()._calc_tax(18,27) # здесь можно super() заменить на self

    def place(self):
        return self.seating + self.stading

a2=Auto2('Honda', 'H2', 100)
print(f'{a2._brand} {a2._model} {a2._power} {a2.get_tax()}')

#b2=Auto2('Bus-Honda', 'B-H2', 320, 50, 10)
#b2=Bus2('Bus-Honda', 'B-H2', 320, 50, 10)
#print(f'{b2._brand} {b2._model} {b2._power} {b2.get_tax()} {b2.seating} {b2.stading}')

b3=Bus2('B3','b3',200,50,10)
print(b3._brand, b3._model, b3._power, b3.seating, b3.stading, b3.get_tax(), b3.place())
    
