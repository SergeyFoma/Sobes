# objects in dict

class CarNumber:
    def __init__(self, number):
        self._number=number

    def get_number(self):
        return self._number
    
    def set_number(self, number):
        new_number=self.new_number
        if  len(number)!=6:
            raise ValueError("NO")
        self._number=new_number

class Car:
    def __init__(self, brand, model, number):
        self._brand=brand
        self._model=model
        self._number=CarNumber(number)

class Dealer:
    def __init__(self):
        self.cars={}
    
    def add_car(self, car):
        self.cars[car._number.get_number()]=car

bmw=Car("BMW", "B5", 'a222aa')
print(bmw._brand, bmw._model, bmw._number.get_number())
dealer=Dealer()
dealer.add_car(bmw)

bmw2=Car("BMW2", "B3", "s333ss")
dealer.add_car(bmw2)

bmw3=Car("BMW3", "B5", "k333kk")
dealer.add_car(bmw3)
print(dealer.cars["s333ss"]._brand)