# Объект в объекте

class CarNumber:
    def __init__(self, number):
        self._number=None
        self.set_number(number)

    def get_number(self):
        return self._number
    
    def set_number(self, new_number):
        new_number = str(new_number)
        if len(new_number) !=6:
            raise ValueError('NO')
        self._number=new_number.lower()

cn=CarNumber('111111')
cn.set_number('Q222qq')
#cn._number='M888MM'
print(cn.get_number())

class Car:
    def __init__(self, brend, model, number):
        self._brend=brend
        self._model=model
        self.number=CarNumber(number)

car1=Car("BMW", "X5", "b555BB")
car1.number.set_number("S777ss")
print(car1._brend, car1._model, car1.number.get_number().upper()[1:4])

