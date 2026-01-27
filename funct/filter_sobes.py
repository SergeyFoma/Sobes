'''Функция filter() в Python — это встроенная возможность отобрать нужные значения из какого-то 
однородного набора данных по созданной программистом формуле. Если говорить формально, 
то эта функция работает с итерируемыми объектами — наборами элементов, которые можно итерировать: 
перебирать по одному и выполнять какие-то действия в зависимости от того, что нам нужно.Функции в Python

Для такого перебора используется цикл: он проходит по всем элементам и с каждым выполняет одни и те же 
инструкции. Например, можно возвести все числа в квадрат или привести все буквы в строке к верхнему или 
нижнему регистру.'''

'''Как выглядит алгоритм этих действий:

Мы создаём функцию, которая будет проверять элементы в наборе.
Передаём в filter() эту функцию и коллекцию элементов для проверки.
На выходе получаем отфильтрованные значения, с которыми можно продолжать работать разными способами
 в зависимости от логики программы.

 Вместо первого аргумента-функции в filter() Python разрешает использовать None:

 https://thecode.media/funkciya-filter-v-python/
'''

a=123
print(a.__bool__)
print(a.__bool__())


def is_even(x):
    return x%2==0

elements=[1,2,3,4,5,6,7,8,9,10]

built=filter(is_even, elements)
print(built)

# выводы
# 1 for
# for b in built:
#     print(b)

# 2 преобразование итератора в список
# numbers=list(built)
# print(numbers)

# 3 получаем объекты по одному через метод next
# print("one elem: ",next(built))
# print("two element: ", next(built))
# print("three elem: ", next(built))

# 4 lambda
str_title=['a','Asd','xcv','Zxc']
elem = filter(lambda x: x==x.title(), str_title)
print(elem)
print(list(elem))
print(list(elem))

def st_upper(x):
    return x==x.upper()

upp=['ASD','qwe','Awq','MNB']

# upp_filter=filter(st_upper,upp)
# print(list(upp_filter))

upp_lam=filter(lambda x: x==x.upper(), upp)
print(list(upp_lam))


numb_nan=[12, 'qw', 45, '23']
# for i in numb_nan:
#     #print(type(i))
#     if type(i)==int:
#         print(i)
n_f=filter(lambda x: type(x)==int, numb_nan)
print(list(n_f))

# filter dict
dict_num={'a':9, 'b':'2', 'c':5}

print(dict_num.values())

#print(dir(dict_num))

