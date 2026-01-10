#Как выполняется интерполяция строк?
'''Интерполяция строк в Python — это способ встраивать значения переменных, 
выражения или выходные данные функций непосредственно в строку. 
Это упрощает работу со строками, делает код более читаемым и устраняет необходимость 
в ручной конкатенации. 
pythonist.ru
В Python для интерполяции строк используются разные методы, например, 
f-строки, метод .format() и оператор %.'''

str1='Qwerty asdfg. Zxcv 345'
print(f'Hello!!! {str1}!')
print('My name is {}'.format(str1))
print('Hey %s %s'%(str1, str1))

#Create string
str2='Hello Vasya!'
str3="""Иногда нам нужно включить в строку особые символы, 
например, кавычки или перенос строки. 
Для этого используются последовательности с обратной косой чертой (\):"""
print(str3)

print(f'id={id(str1)}')
print(str1.__doc__)

print('----------------------')

print(dir(str1))
print()
print(str2.__dir__())
print('---'*20)
print(str2.__add__('PPPPPPP'))
print(str2.upper())

str4=12345
print(str4, str4.bit_count())
print('STR4= ',dir(str4))
str4=str(str4)
print(str4.zfill(15))