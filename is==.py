# is - Проверяет идентичность объектов — указывают ли две переменные на один и тот же объект в памяти. 
# Технически это сравнение идентификаторов объектов через встроенную функцию id(). 
# == - Проверяет равенство значений объектов. Вызывает метод eq() объектов, сравнивая их содержимое, 
# а не их идентичность в памяти.

#  https://tproger.ru/articles/v-chem-raznica-mezhdu-is-i-v-python-241937

a=123
b=123
print("ID= ", id(a), id(b))
print('A is B= ', a is b)
print('A == B= ', a == b) 

al=[1,2,3]
bl=[1,2,3]
cl=al
print(al is bl)
print(al == bl)
print(cl is al, cl == al, cl is bl, al is bl, cl == bl)
print(id(al), id(bl), id(cl))

# x=256
# y=256
# z=x
# print(x is y, x is z, x == y, x == z, y ==z, y is z)

x=25705
y=25705
z=x
print(x is y, x is z, x == y, x == z, y ==z, y is z)

xs='asd'
zx='asd'
xz=zx
print(xs is zx, xs == zx, id(xs), id(zx), id(xz))

at=(1,2,3)
st=(1,2,3)
za=at
print(id(at), id(st), id(za), at is st, at == st, st is za, st == za)

seta={'1':1,'2':2,'3':3}
setb={'1':1,'2':2,'3':3}
print(seta is setb, seta == setb, id(seta), id(setb))