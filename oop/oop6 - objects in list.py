class CarNumber:
    def __init__(self, number):
        self._number=number

    def get_number(self):
        return self._number
    
    def set_number(self, number):
        new_number=str(new_number)
        if len(new_number)!=6:
            raise ValueError("NO")
        self.number=new_number

num1=CarNumber("q222qq")
print(num1._number)
print(num1.get_number().upper()[1:4])

class Car:
    def __init__(self, brend, model, number):
        self._brend=brend
        self._model=model
        self.number=CarNumber(number)

car1=Car("BMW", "X5", "w123ee")
print(car1._brend, car1._model, car1.number.get_number().upper())
print()

class Dealer:
    def __init__(self):
        self.cars=[]

    def add_car(self, car):
        self.cars.append(car)

bmw=Car('BMW', "B1", 'w222ww')
dealer=Dealer()
dealer.add_car(bmw)
print(bmw._brend, bmw._model, dealer.cars[-1].number.get_number())

toyota=Car("Toyota", "Land Cruiser", 'p000pp')
dealer=Dealer()
dealer.add_car(toyota)
print(toyota._brend, toyota._model, dealer.cars[-1].number.get_number())