'''Нужно ли вообще сортировать словари Python?
Когда сортируете словарь, то сначала спросите себя: “нужно ли мне это?”. 
Или даже конкретнее: “нужен ли мне словарь?”. Словарь “под капотом” содержит обычный массив 
большого размера, который при необходимости может еще расшириться. Поэтому словари занимает 
приличное место в памяти. Иногда можно обойтись обычным списком из кортежей, 
над ним гораздо легче итерироваться и не нужно преобразовывать во что-то другое.'''

import sys
import time

start=time.time()
rooms = {"Pink": "Rm 403", "Space": "Rm 201", "Quail": "Rm 500", "Lime": "Rm 503", "Ant":'555'}
print(sorted(rooms.items()))
stop=time.time()
res=stop-start
print(res)
print(f'Memory: {sys.getsizeof(rooms)} bit.')

start=time.time()
r1=["Pink","Space","Quail","Lime","Ant"]
r2=["Rm 403","Rm 201","Rm 500","Rm 503",'555']
r3=list(zip(r1,r2))
print(f'R3: {r3}')
stop=time.time()
res=stop-start
print(res)
print(f'Memory r3: {sys.getsizeof(r3)} bit.')



