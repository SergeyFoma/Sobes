# https://github.com/netology-code/pyfree-homeworks/blob/main/lections_code/3/todo.py

HELP='''
help - напечатать справку по программе,
add - добавить задачу в список (название задачи запрашиваем у пользователя),
show - напечатать все добавленные задачи.
'''
tasks = []

run=True

while run:
    command = input('Введите команду: ').strip()
    if command == 'help':
        print(HELP)
    elif command == 'show':
        print(tasks)
    elif command == 'add':
        task = input('Введите задачу: ')
        tasks.append(task)
        print("Задача добавлена.")
    else:
        print("Неизвестная команда.")
        print('Chao!')
        break
        # run = False

#print(tasks)

x = 1
while x <= 10:
    if x == 5:
        print(x)
        print("Мы достигли 5!")
        #x+=1
    elif x == 10:
        print(x)
        print("Мы достигли 10!")
        #x+=1
    else:
        print(x)

    x = x + 1

for i in range(1, 6):
    for j in range(1, 6):
        product = i * j
        print(f"{i} * {j} = {product}")
        if product > 10:
            print("Произведение больше 10")
        elif product == 10:
            print("Произведение равно 10")
        else:
            print("Произведение меньше 10")