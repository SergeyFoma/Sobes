# https://metanit.com/python/tutorial/3.9.php
'''Встроенная функция zip() в Python позволяет объединить элементы из нескольких коллекций 
(таких как списки, словари, кортежи или строки) в один набор кортежей. 
Объединяемые коллекции передаются в качестве параметра через запятую:'''
names = ["Tom", "Bob", "Sam"]
ages = [41, 46, 35]
for i in zip(names,ages):
    print(i)

for x,y in zip(names, ages):
    print(f'Name: {x}, Age: {y}')

# Объединение списков
na=list(zip(names, ages))
print("NA: ", na)

tup1=(1,2,3,4)
tup2=('a','x','g')
print(tuple(zip(tup1, tup2)))

d1={'q':23, 'we':45}
d2={'2':2,'3':3}
print(tuple(zip(d1,d2)))

#Подобным образом можно объединять и большее количество списков:
names = ["Tom", "Bob", "Sam"]
ages = [41, 46, 35]   
companies = ["Sber", "VK", "Yandex"]
print(list(zip(names, ages, companies)))