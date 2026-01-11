class Auto2:

    count = 0  # создаём аттрибут класса

    def __init__(self, brand, model, power):
        self._brand = brand
        self._model = model
        self._power = power

        if type(self) is Auto2:
            Auto2.count += 1

    def get_tax(self):  # variant 2
        return self._calc_tax(10, 15)

    def _calc_tax(self, min_rate, max_rate):
        rate = min_rate
        if self._power > 100:
            rate = max_rate
        return rate * self._power

    def display_info(self): ...


class Bus2(Auto2):

    count = 0

    def __init__(self, brand, model, power, seating, stading):
        super().__init__(brand, model, power)
        self.seating = 0
        self.stading = 0
        self.set_places(seating, stading)
        Bus2.count += 1

    def get_tax(self):  # variant 2
        return super()._calc_tax(18, 27)  # здесь можно super() заменить на self

    def set_places(self, seating, stading):
        self.seating = seating
        self.stading = stading

    def place(self):
        return self.seating + self.stading


a1 = Auto2("A1", "a1", 99)
a2 = Auto2("A2", "a2", 110)

b1 = Bus2("B1", "b1", 300, 40, 25)


print(Auto2.count)
print(b1.place(), Bus2.count)


# объект как аттрибут класса - an object as an attribute of a class.


class Counter:
    def __init__(self):
        self._count = 0

    def inc(self):
        self._count += 1

    def __str__(self):
        return str(self._count)


class Auto3:

    # count=0 # создаём аттрибут класса
    count=Counter()

    def __init__(self, brand, model, power):
        self._brand = brand
        self._model = model
        self._power = power

        # if type(self) is Auto2:
        #     Auto2.count += 1
        if type(self) is Auto3:
            Auto3.count.inc()

    def get_tax(self):  # variant 2
        return self._calc_tax(10, 15)

    def _calc_tax(self, min_rate, max_rate):
        rate = min_rate
        if self._power > 100:
            rate = max_rate
        return rate * self._power

    def display_info(self): ...


class Bus3(Auto3):

    # count=0
    count=Counter()
    def __init__(self, brand, model, power, seating, stading):
        super().__init__(brand, model, power)
        self.seating = 0
        self.stading = 0
        self.set_places(seating, stading)
        # Bus2.count +=1
        Bus3.count.inc()

    def get_tax(self):  # variant 2
        return super()._calc_tax(18, 27)  # здесь можно super() заменить на self

    def set_places(self, seating, stading=0):
        self.seating = seating
        self.stading = stading

    def place(self):
        return self.seating + self.stading
aut1 = Auto3('Aut1', 'aut1', 90)
aut2=Auto3("Aut2", 'aut2', 120)
aut3=Auto3("Aut3", 'aut3', 120)
bu1=Bus3('Bu1', 'bu1', 150, 40, 20)
bu2=Bus3("bU2", "BU2", 200, 50, 10)
bu3=Bus3("bU3", "BU3", 200, 0, 0)

print(Auto3.count)
print(Bus3.count, bu3._brand)


#-----------------------------------------------------------------------------------
print('--------------------------------')

import counter

class Auto4:

    # count=0 # создаём аттрибут класса
    count=counter.Counter()

    def __init__(self, brand, model, power):
        self._brand = brand
        self._model = model
        self._power = power

        # if type(self) is Auto2:
        #     Auto2.count += 1
        if type(self) is Auto4:
            Auto4.count.inc()

    def get_tax(self):  # variant 2
        return self._calc_tax(10, 15)

    def _calc_tax(self, min_rate, max_rate):
        rate = min_rate
        if self._power > 100:
            rate = max_rate
        return rate * self._power

    def display_info(self): ...


class Bus4(Auto4):

    # count=0
    #count=counter.Counter()
    count=counter.Counter(10) # задаём начальное значение 10, с него начинаем отсчёт.
    def __init__(self, brand, model, power, seating, stading):
        super().__init__(brand, model, power)
        self.seating = 0
        self.stading = 0
        self.set_places(seating, stading)
        # Bus2.count +=1
        Bus4.count.inc()
        self.count=Bus4.count.get() # добавляем порядковый номер

    def get_tax(self):  # variant 2
        return super()._calc_tax(18, 27)  # здесь можно super() заменить на self

    def set_places(self, seating, stading=0):
        self.seating = seating
        self.stading = stading

    def place(self):
        return self.seating + self.stading
    
auto4_1=Auto4('Auto4_1', 'auto4_1', 230)
bus4_1=Bus4('BUS4_1', 'bus4_1', 200, 34, 20)

bus5=Bus4("Bus5", 'bus5', 130, 45, 20)
bus6=Bus4("Bus6", 'bus6', 130, 45, 20)

print('Auto4.count: ', Auto4.count)
print('Bus4.count: ', Bus4.count)

print(Bus4.count.get(), ' - Autobus')
print(Auto4.count.get(), ' - Car')

print(bus4_1.count, bus4_1._brand)
print(bus5.count, bus5._brand)
print(bus6.count, bus6._brand)