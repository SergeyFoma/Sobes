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

# ---------------------------------------------------------
# https://pyhub.ru/python-oop/lecture-17-50-92/

class Example:
    def __init__(self):
        self.attr1="Публичный аттрибут"
        self._attr2 = "Не публичный аттрибут"
        self.__attr3="Приватный аттрибут"

    # def display(self):
    #     print('Public = {self.attr1}')

example1 = Example()
print(example1.attr1)
print(example1._attr2)
# print((example1.__attr3))


# Защищённый (protected) доступ
# Защищённые атрибуты и методы принято обозначать одним подчеркиванием (_) в начале их имени. 
# Это является сигналом для разработчиков, что данные не предназначены для внешнего использования, 
# хотя Python технически не запрещает их доступ извне. 
# Это больше соглашение, чем реальная защита:
class Employee:
    def __init__(self, name, salary):
        self.name=name 
        self._salary=salary
        self.currency='Rub.'

    def display_salary(self):
        print(f"Salary employee {self.name} = {self._salary} {self.currency}")

    

empl1=Employee('Bob', 200000)
empl1._salary=50000
empl1.currency='$'
empl1.display_salary()

'''Приватный (private) доступ
Для строгого ограничения доступа используется приватный режим. 
Приватные атрибуты и методы начинаются с двух подчеркиваний (__). 
Такие атрибуты недоступны напрямую извне класса и могут быть использованы только внутри самого класса.'''
class BankAccount:
    def __init__(self, owner, balance):
        self.__owner=owner
        self.__balance=balance

    def show_balance(self):
        print(f"Owner {self.__owner} Balance {self.__balance}")

ba1=BankAccount('Biba', 322332)
#print(ba1.__owner, ba1.__balance)
ba1.show_balance()

# Работа с приватными атрибутами через методы
# Приватные атрибуты можно сделать доступными через специальные методы, например, для чтения данных:

class BancAccount:
    def __init__(self, owner, balance):
        self.__owner=owner
        self.__balance=balance

    def show_balance(self):
        print(f"Owner {self.__owner} balance {self.__balance}")

    def get_owner(self):  # В данном примере метод get_owner позволяет безопасно получить информацию о владельце счета, не раскрывая сам атрибут напрямую.
        return self.__owner

account1 = BancAccount('Boba', 500)
account1.show_balance()
#print(account1.__owner)
print(account1.get_owner())

print('-----'*20)

'''Доступ к приватным атрибутам извне через обход
Несмотря на приватность, в Python всё ещё можно получить доступ к приватным данным с помощью 
специального синтаксиса. Это называется "name mangling" (искажение имени). 
Имена приватных атрибутов и методов преобразуются Python во внутреннюю форму, к которой можно обратиться
Таким образом, используя внутреннее имя, мы всё-таки можем получить доступ к приватным атрибутам. 
Однако это считается плохой практикой и противоречит принципам инкапсуляции.'''

class BankAccount:
    def __init__(self, owner, balance):
        self.__owner=owner
        self.__balance=balance

account=BankAccount('Mia', 350)
print(account._BankAccount__owner, account._BankAccount__balance)
