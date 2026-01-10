# Полиморфизм — принцип объектно-ориентированного программирования (ООП), 
# позволяющий использовать объекты разных классов через единый интерфейс.
# https://habr.com/ru/articles/552922/

class Car:
    def __init__(self, brand, model, power):
        self.brand=brand
        self.model=model 
        self.power=power 

    def tax(self):
        rate = 10
        return self.power * rate

class Bus:
    def __init__(self, brand, model, power):
        self.brand=brand
        self.model=model 
        self.power=power 

    def tax(self):
        rate = 50
        return self.power * rate
    
car1=Car('BMW', 'B1', 100)
bus1=Bus('Bus1', 'Bus111', 100)
    
for i in (car1, bus1):
    print(f'{i.brand},\n{i.model},\n{i.tax()}')

print('------------------------------')

