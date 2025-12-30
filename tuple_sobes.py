#1. В чем разница между списком и кортежем?
'''Список можно изменить после создания.
Кортеж нельзя изменить после создания.
Список упорядочен. Он представляет собой упорядоченные последовательности объектов, 
как правило, 
одного и того же типа. Например, все имена пользователей упорядочены по дате создания: ["Seth", "Ema", "Eli"].
У кортежа есть структура. В каждом индексе могут сосуществовать различные типы данных. 
Например, такая запись базы данных в памяти: (2, "Ema", "2020–04–16") # id, name, created_at'''

# Создание кортежа без скобок
a='qw', 'as', 'df'

# Распаковка кортежа
x,y,z=a
print(type(a),z,x)
print(a[0])

# Создание пустого кортежа
at=()
print(type(at))

at2=tuple()
print(type(at2))

# Преобразование списка в кортеж
al1=[1,2,3,4]
at3=tuple(al1)
print(type(at3))

# Преобразование строки в кортеж (каждый символ становится элементом)
ast='qwewqe'
at4=(ast,)
print(type(at4))

# Преобразование множества в кортеж
aset={4,5,6,7,8,6}
aset_tuple=tuple(aset)
print(type(aset_tuple))

adict={'as':123, 'sa':321}
adict_tuple=tuple(adict)
print(type(adict))
print(adict_tuple)
print(type(adict_tuple))

# Получение элементов по индексу
in_tup=('qwe', 34, 'gfd')
print(in_tup[-1])

# Разворот кортежа
print(in_tup[::-1])

#Поскольку кортежи неизменяемые, у них только два метода:
# Подсчет количества вхождений элемента
fruits = ("apple", "banana", "cherry", "banana", "date")
print(fruits.count("banana"))

# Поиск индекса первого вхождения элемента
banana_index=fruits.index("banana")
print(banana_index)

fruits = ("apple", "banana", "cherry", "banana", "date")
for i in range(len(fruits)):
    if fruits[i]=="banana":
        print(i)

#Операции с кортежами
# Узнать длину
print(len(fruits))

# Проверить наличие элемента
print("apple" in fruits)

# Конкатенация (объединение) кортежей
tuple_concat=("ddd", "fff", 66)
print(fruits+tuple_concat)

# Повторение
fru2=fruits*3
print(fru2)

# Распаковка
x,c,v = tuple_concat
print(x,c,v)

# Но можно создать новый кортеж на основе существующего
fff=(34,56,8)
new_tup=fff+tuple_concat[0:]
print(new_tup)

x=('sss',['w',3,2])
x[1][1]=555
print(x)

'''Сравнение списков и кортежей
Характеристика	Список (list)	Кортеж (tuple)
Синтаксис	[1, 2, 3]	(1, 2, 3)
Изменяемость	Да	Нет
Методы	Много: append, remove, sort...	Только count, index
Производительность	Медленнее	Быстрее
Использование памяти	Больше	Меньше
Может быть ключом словаря	Нет	Да
Подходит для	Коллекций, которые могут меняться	Неизменяемых данных'''

dict1={(1,2,3):'qwert', 'qw':555}
print(dict1)
# dict2={[1,2,3]:'qwert', 'qw':555}
# print(dict2)

#проверяем производительность
import time
start=time.time()
car=('Audy','BMV','Toyota','VAZ')
finish=time.time()
result=finish-start
print('result==',result*1000)

start=time.time()
car=['Audy','BMV','Toyota','VAZ']
finish=time.time()
result2=finish-start
print('result2==',result2*1000)

#Проверяем объем используемой памяти
import sys
my_list = [1, 2, 3]
print(f"Size list: {sys.getsizeof(my_list)} bit")

my_list = (1, 2, 3)
print(f"Size tuple: {sys.getsizeof(my_list)} bit")

my_dict = {'a': 1, 'b': 2}
print(f"Size dict: {sys.getsizeof(my_dict)} bit")