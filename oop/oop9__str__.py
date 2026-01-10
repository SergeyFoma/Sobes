class Product:
    def __init__(self, name, price, quantity=0):
        self._name=name
        self._price=price
        self._quantity=quantity

    def amount(self):
        return self._price * self._quantity
    
    def __str__(self):
        quantity=f'QUantity {self._quantity}'
        total=f'Полная стоимость {self.amount()} rub.'
        return f'{self._name} {quantity}\n{total}'
    
prod1=Product('Prod1', 120, 10)
print(prod1._name, prod1._price, prod1._quantity, prod1.amount())
print(prod1)

print('------------------------------------------')
class Car:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model

        # Начальное значение (создание атрибута)
        self.__power = 0
        # Реальная установка мощности.
        self.power = power

        self.__year = None

    @property
    def power(self):
        """
        Возвращаем мощность автомобиля.
        """
        return self.__power

    @power.setter
    def power(self, new_power):
        """
        Устанавливаем мощность автомобиля.
        """
        self.__power = int(new_power)

    def get_year(self):
        """
        Получаем год выпуска.
        """
        return self.__year

    def set_year(self, year):
        """
        Устанавливаем год выпуска.
        """
        self.__year = year
        
    def __str__(self):
        if self.__year != None:
            return f'{self.brand} {self.model}\nМощность: {self.power} лс.\nГод выпуска: {self.get_year()}'
        else:
            return f'{self.brand} {self.model}\nМощность: {self.power} лс.'
        
car = Car("Амберавто", "А5", 130)
print(car)
        

    