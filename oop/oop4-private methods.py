#  непубличные методы
# Инкапсуляция - приватные аттрибуты и приватные методы
'''Приватные методы в объектно-ориентированном программировании (ООП) на Python — 
это методы, которые доступны только внутри класса, где они определены. 
К ним нельзя получить доступ из других объектов или другого места программы. 
thecode.media
ru.hexlet.io
diveintopython.org
Приватные методы используются для внутренних операций в классе, повышая инкапсуляцию и 
предотвращая случайное неправильное использование или переопределение.'''

# Пример с приватным методом
# Попробуем вызвать приватный метод через открытый метод внутри класса:

class BankAccount:
    def __init__(self, owner, balance):
        self.__owner=owner 
        self.__balance=balance

    def show_balance(self):
        print(f"Owner {self.__owner} balance - {self.__balance}")
        self.__private_method()

    def __private_method(self):
        print("Private method!!!")

ac1=BankAccount('Djon', 9000)
print(ac1.show_balance())

# Приватные методы можно использовать внутри класса, но они остаются недоступны напрямую извне.
'''Таким образом:
В Python существует три уровня доступа:
Публичные атрибуты и методы открыты для всех.
Защищённые атрибуты и методы рекомендуется не использовать вне класса, но технически они доступны.
Приватные атрибуты и методы защищены от внешнего доступа, однако их всё же можно обойти.'''

class Car:
    def __init__(self, brand, model, power):
        self._brand=brand 
        self._model=model 
        self._power=0
        self.set_power(power)

    def get_rate(self):
        return self.rate 
    
    def set_power(self,power):
        self._power=power

car1 = Car('Toyota', 'Lend Cruiser', 150)
car1.rate=0.23
print(car1._brand, car1._model, car1._power, car1.rate)
print(car1.get_rate())