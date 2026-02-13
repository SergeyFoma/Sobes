HELP='''
help - напечатать справку по программе,
add - добавить задачу в список (название задачи запрашиваем у пользователя),
show - напечатать все добавленные задачи,
random - добавляет случайную задачу на дату "Сегодня".
'''
RANDOM_TASK = 'Записаться на курс в нетологию.'
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
        else:
            print("Такой даты нет.")
        #print(tasks)
    elif command == 'add':
        date = input('Введите дату: ')
        task = input("Введите задачу: ")
        if date in tasks:
            tasks[date].append(task)
        else:
            tasks[date]=[]
            tasks[date].append(task)
        print(f"Задача {task} добавлена в список задач.")
    elif command == "random":
        if "Сегодня" in tasks:
            tasks["Сегодня"].append(RANDOM_TASK)
        else:
            tasks["Сегодня"] = []
            tasks["Сегодня"].append(RANDOM_TASK)
    elif command == 'exit':
        print("Good By!!!")
        break
#print(tasks)