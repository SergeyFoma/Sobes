# Склейте элементы списка whoami в строку с помощью функции reduce.
from functools import reduce

whoami = ['Я', ' ', 'п', 'р', 'о', 'г', 'р', 'а', 'м', 'м', 'и', 'с', 'т']

def glue(x):
    res=', '.join(x)
    return res.replace(', ', '')
#glue(whoami)

whoami = reduce(glue, whoami)
print("WHAOMI: ", whoami)