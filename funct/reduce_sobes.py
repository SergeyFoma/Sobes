"""Функция reduce() (из модуля functools) последовательно применяет функцию к итерируемому объекту,
сводя его к одному значению. Она удобна для решения таких задач, как суммирование, умножение (факториал),
поиск максимального/минимального значения, объединение строк или выравнивание списков.
Используйте её для простых однострочных вычислений,
избегайте её в сложных логических задачах (циклы понятнее) или когда нужны промежуточные результаты.
"""

"""Параметры:

function: Функция, которая принимает два аргумента и возвращает одно значение.
iterable: Последовательность, которую нужно сократить (список, кортеж и т. д.).
инициализатор (необязательно): Начальное значение, которое помещается перед первым элементом.
Возвращаемое значение: Одно итоговое значение после обработки всех элементов.

Функция reduce() особенно полезна в сценариях, требующих преобразования итерируемых данных в одно 
накопленное значение. Это включает операции, такие как нахождение суммы, произведения, наибольшего числа, 
конкатенация строк или даже реализация более сложных алгоритмов, 
которые требуют итеративного сведения.
"""
# https://www.geeksforgeeks.org/python/reduce-in-python/

from functools import reduce

a = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x + y, a))

b = ["Asd", "Zxc", "qwe"]
print(reduce(lambda x, y: x + " " + y, b, "DDD"))


def add_s(x, y):
    """kjhg"""
    return x + " " + y


c = ("xc", "asd", "EwQ")
print(reduce(add_s, c, "BBB"))

d = [23, 1, 5, 43, 456, 78, 9, 6]
res = reduce(lambda x, y: x * y, d)
print(res)

e = d
res = reduce(lambda x, y: x / y, e)
print("Division: ", round(res, 4), res)

# ----------------------------------

# Найдем факториал числа 5
l = range(1, 6)
print(l)


def mult(x, y):
    return x * y


factorial = reduce(mult, l)
print("factorial: ", factorial)

# ----------------------------------------------
print("----------------------------------")
# reduce() + map()

gamers = [
    {"name": "Mik", "goals": 6, "pass": 8},
    {"name": "Bob", "goals": 12, "pass": 15},
    {"name": "Dron", "goals": 9, "pass": 13},
]


def goal_pass(gamer):
    return {"name": gamer["name"], "gp": gamer["goals"] + gamer["pass"]}


# gamers2=list(map(goal_pass, gamers))
# print(gamers2)


def best_gamer(gamer1, gamer2):
    if gamer1["gp"] > gamer2["gp"]:
        return gamer1
    return gamer2


print(reduce(best_gamer, map(goal_pass, gamers)))
