# https://sky.pro/wiki/python/oop-v-python-inkapsulyaciya/

'''Инкапсуляция — принцип объектно-ориентированного программирования (ООП) в Python, 
который заключается в объединении данных и методов, которые с ними работают, 
в единый объект и ограничении доступа к внутреннему состоянию объекта из внешней среды.'''

'''Принцип
Инкапсуляция позволяет:
Скрыть детали реализации.
Защитить данные от неконтролируемого изменения.
Предоставить контролируемый интерфейс для работы с объектом.
 
python-academy.org
Некоторые функции инкапсуляции:
Контроль доступа — определяет, кто и как может взаимодействовать с данными класса.
Сокрытие деталей реализации — предотвращает зависимость клиентского кода от внутренней структуры.
Поддержка инвариантов — обеспечивает сохранение внутренней согласованности объекта.
Снижение связанности — минимизирует зависимости между компонентами системы.'''

'''Реализация
В Python инкапсуляция реализуется через соглашения о наименовании атрибутов и методов: 
synergy.ru
sky.pro
Public — атрибуты и методы, доступные извне, без подчёркиваний (например, attribute).
Protected — атрибуты и методы, доступные только в пределах класса и его подклассов, 
обозначаются одним подчёркиванием (например, _attribute).
Private — атрибуты и методы, доступные только в пределах класса, 
обозначаются двумя подчёркиваниями (например, __attribute).
 
synergy.ru
В отличие от некоторых строго типизированных языков (Java, C++), 
Python не имеет строгих механизмов для определения уровней доступа к атрибутам и методам.'''

'''Инкапсуляция – один из трёх китов объектно-ориентированного программирования наряду с наследованием и 
полиморфизмом. По сути, это механизм ограничения прямого доступа к компонентам объекта (данным и методам), 
определяющий, 
какая информация скрыта, а какая доступна извне.'''

# _price непубличный(приватный) атрибут
# price публичный
# API - публичный интерфейс


class Car:
    def __init__(self, name, power):
        self.name = name
        self.set_power(power)  # инициализация через сеттер

    def get_rate(self):
        return self.power * self.rate

    def set_power(self, new_power):
        new_power = float(new_power)
        if new_power <= 0:
            raise ValueError("Power must be >0")
        self.power = new_power


bmw = Car("BMW", 200)
print(bmw.name, bmw.power)
# print(bmw.get_rate())
bmw.rate = 10
bmw.power = "500"
print(bmw.get_rate())
bmw.set_power("500")
print(bmw.get_rate())
bmw.power = "300"
print(bmw.get_rate())

# reno = Car('Reno', 0)
# reno.set_power('-234')
# #reno.power=-120
# reno.rate=0.5
# print(reno.get_rate())

# lada = Car('Lada', -150)
# lada.rate=0.2
# print('Lada=',lada.get_rate())
print('-----------------------------------')
print()

class Product:
    def __init__(self, name, price, quantity=0):
        self.name = name  # публичный атрибут
        self._price = price  # приватный атрибут
        self._quantity = quantity
        self.set_price(price)
        self.currency = "Rub."

    def get_discount(self):
        return self.discount

    def get_price_discount(self):
        result = self.price - self.price * self.discount / 100
        return f"{result} {self.currency}"

    def set_discount(self, new_discount):
        new_discount = float(new_discount)
        if new_discount <= 0:
            raise ValueError("discount must be >0")
        self.discount = new_discount

    def set_price(self, new_price):
        new_price = float(new_price)
        if new_price <= 0:
            raise ValueError("Price must be  >0")
        self.price = new_price


table = Product("Table", 40, 10)
table.discount = 20
print(table.name, table.price, table._quantity, table.get_discount())
print(table.get_price_discount())

table.set_discount("10")
print("disc 100=", table.get_price_discount())

table.price = -205
print("Price - ", table.get_price_discount())

table.set_price(200)
print("Set_price=", table.get_price_discount())
