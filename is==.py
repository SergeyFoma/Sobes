# is - Проверяет идентичность объектов — указывают ли две переменные на один и тот же объект в памяти. 
# Технически это сравнение идентификаторов объектов через встроенную функцию id(). 
# == - Проверяет равенство значений объектов. Вызывает метод eq() объектов, сравнивая их содержимое, 
# а не их идентичность в памяти.

#  https://tproger.ru/articles/v-chem-raznica-mezhdu-is-i-v-python-241937

a=23
b=23
c=a
d=12

print(a is c)
print(a is b)
print(b is c)
print(a==b)
print(a==c)
print(b==c)
print(a is d)
print(b == d)

a=[1,2,3,4]
b=[1,2,3,4]
c=b
print()
print(a is b)
print(a == b)
print(c is b)
print(c == b)