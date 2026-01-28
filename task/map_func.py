# Создайте функцию для использования внутри map. 
# Функция должна добавлять к каждой комнате в списке rooms элемент с именем square содержащий её площадь.

rooms = [
    {"name": "кухня", "length": 6, "width": 4},
    {"name": "комната 1", "length": 5.5, "width": 4.5},
    {"name": "комната 2", "length": 5, "width": 4},
    {"name": "комната 3", "length": 7, "width": 6.3},
]

def add_elem(x):
    square=int(x['length'])*int(x['width'])
    x['scuare']=square
    return x

rooms = map(add_elem, rooms)
print(list(rooms))

# В списке digits содержатся строки с числами. Эти строки содержат ошибки: лишние пробелы, 
# а также неправильные разделители целой и десятичной части.
# Создайте функцию, которая сначала исправит ошибки в строках, а затем преобразует каждую строку в 
# вещественное число. 
# Примените эту функцию ко всем элементам digits с помощью map.

digits = ["12", "145", "  45", "12.4", "45,14", "15 645"]

def fix_it(x):
    return float(x.replace(',','').replace(' ',''))

right_digits = map(fix_it,digits)
print('right_digits: ', list(right_digits))