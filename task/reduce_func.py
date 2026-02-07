# Склейте элементы списка whoami в строку с помощью функции reduce.
# from functools import reduce

# whoami = ['Я', ' ', 'п', 'р', 'о', 'г', 'р', 'а', 'м', 'м', 'и', 'с', 'т']

# def glue(x):
#     res=', '.join(x)
#     return res.replace(', ', '')
# #glue(whoami)

# whoami = reduce(glue, whoami)
# print("WHAOMI: ", whoami)

# ---------------------------------------

'''Используйте map и reduce, чтобы посчитать площадь квартиры, состоящей из комнат rooms.'''

from functools import reduce

rooms = [
    {"name": "кухня", "length": 6, "width": 4},
    {"name": "комната 1", "length": 5.5, "width": 4.5},
    {"name": "комната 2", "length": 5, "width": 4},
    {"name": "комната 3", "length": 7, "width": 6.3},
]
def scuare_rooms(x):
    return x['length']*x['width']
    
def scuare(x,y):
    return y+x
rooms = list(map(scuare_rooms,rooms))
print('ROOMS: ', rooms)

sq = reduce(scuare,rooms)
print("SQ: ", sq)