# https://pythonist.ru/kak-ispolzovat-funkczii-all-i-any-v-python/
'''Функция any()
Возвращает True, если хотя бы один элемент в итерируемом объекте (список, кортеж, словарь и т. д.) равен True. В противном случае —
Функция all()
Возвращает True, если все элементы в итерируемом объекте истинны. Если какой-либо элемент является ложным (включая False, 0, None, пустые строки или пустые коллекции), функция немедленно возвращает False. 
letpy.com
reintech.io'''

a=[1,2,'e']
print(all(a))
a=[1,2,'e',0]
print(all(a))
a=[1,2,'e',False]
print(all(a))

a=[1,2,'e',False,0]
print('ANY= ', any(a))

a=[0,0]
print('ANY= ', any(a))