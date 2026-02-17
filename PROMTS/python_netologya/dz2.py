'''Задание 1
Закрепим знания по работе с циклом while и списками в Python. 
В первом задании вам предстоит проработать программу, созданную на лекции, добавив в неё новую команду — exit. 
При вводе этой команды программа должна завершить свою работу и вывести сообщение: «Спасибо за использование! До свидания!»

Пример ввода-вывода программы:
Введите команду: todo
Введите задачу: выучить Python
Задача выучить Python добавлена
Введите команду: show
['выучить Python']
Введите команду: exit
Спасибо за использование! До свидания!
'''

HELP='''
todo - Добавить задачу,

'''
# tasks=[]
# run=True
# while run:
#     command=input("Введите команду: ")
#     if command == 'todo':
#         command=input('Введите задачу: ')
#         tasks.append(command)
#         print(f'Задача {command} добавлена')
#     elif command == 'show':
#         print(tasks)
#     elif command == 'exit':
#         print('Спасибо за использование! До свидания!')
#         break

'''Задание 2
Продолжим развивать нашу программу. Во втором задании мы закрепим тему вложенных условий и 
создание нескольких списков.
Внесите следующие изменения: Создайте 3 пустых списка: a. today b. tomorrow c. other
Измените блок кода, который выполняет команду add:
После ввода команды нужно запросить у пользователя дату («Сегодня», «Завтра», «Другие») выполнения задачи.
В зависимости от введённой даты добавьте задачу в один из списков по следующим правилам: · 
Если пользователь ввёл «Сегодня», добавьте задачу в список today. · Если пользователь ввёл «Завтра», 
добавьте задачу в список tomorrow. · 
Если пользователь ввёл «Другие» другое значение, добавьте задачу в список other.

'''

tasks = []
today = []
tomorrow = []
other = []

run=True
while run:
    command = input('Введите команду: ')
    if command == 'add':
        command1 = input('Введите дату: ')
        if command1 == 'Сегодня':
            today.append(command1)
            command2 = input('Введите задачу: ')
            today.append(command2)
            print(f'Задача {command2} добавлена.')
        elif command1 == 'Завтра':
            tomorrow.append(command1)
            command2 = input('Введите задачу: ')
            tomorrow.append(command2)
            print(f'Задача {command2} добавлена.')
        else:
            other.append(command1)
            command2 = input('Введите задачу: ')
            other.append(command2)
            print(f'Задача {command2} добавлена.')
        
    elif command == 'show':
        print(today, tomorrow, other)
    elif command == 'exit':
        print('Спасибо за использование! До свидания!')
        break

# print(today)
# print(tomorrow)
# print(other)