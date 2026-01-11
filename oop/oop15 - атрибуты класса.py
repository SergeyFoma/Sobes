# Атрибуты класса
# Кроме атрибутов объектов в классе можно определять атрибуты классов. 
# Подобные атрибуты определяются в виде переменных уровня класса. Например:

# https://metanit.com/python/tutorial/7.6.php

class Person:
    default_name='Default'
    def __init__(self, name):
        if name:
            self.name=name
        else:
            self.name=Person.default_name

pers1=Person("Billi")
pers2=Person("")
pers1.name='Som'
print(pers1.name, pers2.name)

