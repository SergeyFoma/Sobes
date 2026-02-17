import random

HELP='''
help - напечатать справку по программе,
add - добавить задачу в список (название задачи запрашиваем у пользователя),
show - напечатать добавленные задачи по дате, all - напечатать словарь всех задач,
random - добавляет случайную задачу на дату "Сегодня".
'''

def add_todo(date, task):
    # date = input('Введите дату: ')
    # task = input("Введите задачу: ")
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date]=[]
        tasks[date].append(task)
    print(f"Задача {task} добавлена в список задач.")

RANDOM_TASK = 'Записаться на курс в нетологию.'
RANDOM_TASKS = ['Записаться на курс в нетологию.', 'Написать письмо Гвидо',
                'Покормить кошку', 'Помыть машину']
tasks={}

run = True 
while run:
    command = input("Введите команду: ")
    if command == 'help':
        print(HELP)
    elif command == 'show':
        date = input('Введите дату для отображения списка задач: ')
        if date in tasks:
            # for k in tasks:
            #     if k == date:
            #         print(f'Date: {k}: {tasks[k]}')
            for v in tasks[date]:
                print(f"Дата: {date} - {v}")
        elif date == 'all':
            print(tasks)
        else:
            print("Такой даты нет.")
        #print(tasks)
    elif command == 'add':
        date = input('Введите дату: ')
        task = input("Введите задачу: ")
        # if date in tasks:
        #     tasks[date].append(task)
        # else:
        #     tasks[date]=[]
        #     tasks[date].append(task)
        # print(f"Задача {task} добавлена в список задач.")
        add_todo(date, task)
    elif command == "random":
        # print("Random: ", command)
        # if "Сегодня" in tasks:
        #     tasks["Сегодня"].append(RANDOM_TASK)
        # else:
        #     tasks["Сегодня"] = []
        #     tasks["Сегодня"].append(RANDOM_TASK)
        ## add_todo("Сегодня", RANDOM_TASK)
        task = random.choice(RANDOM_TASKS)
        add_todo("Сегодня", task)
    elif command == 'exit':
        print("Good By!!!")
        break
#print(tasks)