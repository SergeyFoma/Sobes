'''Сайт предназначен для мужчин от 20 до 30 лет включительно. 
Отфильтруйте список people, чтобы в нем осталась только целевая аудитория сайта.
Результат должен быть помещен в переменную my_people.'''

people = [
    {"sex": "m", "age": 12},
    {"sex": "w", "age": 12},
    {"sex": "m", "age": 15},
    {"sex": "m", "age": 20},
    {"sex": "m", "age": 13},
    {"sex": "m", "age": 27},
    {"sex": "w", "age": 31},
    {"sex": "m", "age": 17},
    {"sex": "w", "age": 17},
    {"sex": "m", "age": 12},
    {"sex": "m", "age": 42},
    {"sex": "w", "age": 25}
]


def peop(x):
    if x["sex"]=="m" and 30>=x["age"]>=20:
        return(x)
    
#print(peop(people))

my_people=filter(peop, people)
print("my_people: ", list(my_people))

# my_people=filter(lambda x:x["sex"]=="m" and 30>=x["age"]>=20, people)
# print(list(my_people))

# for i in people:
#     print(i["sex"],i["age"])