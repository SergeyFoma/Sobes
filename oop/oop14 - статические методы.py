# Статический метод в объектно-ориентированном программировании (ООП) на Python — это функция, 
# которая логически принадлежит классу, но не зависит от его состояния. В отличие от обычных методов, 
# статические не требуют создания экземпляра класса и не имеют доступа к его атрибутам.

# Особенности:
# Могут быть вызваны как через класс, так и через его экземпляры.
# Не могут непосредственно взаимодействовать с атрибутами экземпляра или класса.

'''Синтаксис
Статический метод объявляется с помощью декоратора @staticmethod. 
Этот декоратор указывает интерпретатору Python, что метод является статическим, 
и следует вызывать его через класс, а не через экземпляр класса. 
sky.pro
timeweb.cloud
blog.mikihands.com
Ключевые особенности:
Декоратор @staticmethod применяется непосредственно к функции внутри класса.
Метод не принимает параметры self или cls.
Статические методы не переопределяются автоматически при наследовании — 
каждый статический метод существует независимо в пространстве имён своего класса.'''

import counter

class Auto:
    count=counter.Counter()
    def __init__(self, brand, model, power):
        self.brand=brand 
        self.model=model 
        self.power=power 

    # def get_tax(self):
    #     return self._calc_tax(12, 25)
    
    # def _calc_tax(self, min_rate, max_rate):
    #     rate=min_rate
    #     if self.power > 100:
    #         rate=max_rate 
    #     return self.power * rate

    def get_tax(self):
        return Auto.calc_tax(self.power, 12, 25)

    @staticmethod
    def calc_tax(power, min_rate, max_rate):
        rate=min_rate
        if power > 100:
            rate=max_rate 
        return power * rate

class Bus(Auto):
    count=counter.Counter()
    def __init__(self, brand, model, power, sidaunt, standing):
        super().__init__(brand, model, power)
        self.sidaunt=sidaunt
        self.standing=standing

    # def get_tax(self):
    #     return super()._calc_tax(23,32)

    def get_tax(self):
        return super().calc_tax(self.power, 23,32)
    
aut1=Auto("AUT1", 'aut1', 123)
bus1=Bus('Bus1', 'bus1', 300, 40, 20)

print(aut1.brand, aut1.get_tax())
print(bus1.brand, bus1.get_tax())
        
tax=Auto.calc_tax(100, 10, 20) # мспользуем calc_tax самостоятельно вне объекта
print(tax)