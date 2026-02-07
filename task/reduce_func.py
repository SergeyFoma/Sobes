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

<<<<<<< HEAD
sq = reduce(scuare,rooms)
print("SQ: ", sq)
=======
def glue(x,y):
#     res=', '.join(x)
#     return res.replace(', ', '')
# print(glue(whoami))
    return x+y
#print(glue(whoami))
whoami = reduce(glue, whoami)
print("WHAOMI: ", whoami)

#--------------------------------------------
print('---------------------------')

#Используйте map и reduce, чтобы посчитать площадь квартиры, состоящей из комнат rooms.
rooms = [
    {"name": "кухня", "length": 6, "width": 4},
    {"name": "комната 1", "length": 5.5, "width": 4.5},
    {"name": "комната 2", "length": 5, "width": 4},
    {"name": "комната 3", "length": 7, "width": 6.3},
]
def room_square(room):
    return room["length"] * room["width"]


def get_all_square(acc, room):
    return acc + room


rooms = map(room_square, rooms)
#print(list(rooms)) # вот тут джин и выходил, если оставлял строку активной

square = reduce(get_all_square, rooms, 0)
print(square)
>>>>>>> 662dcafe99f426606c66ef804bb33956fc1f3919
