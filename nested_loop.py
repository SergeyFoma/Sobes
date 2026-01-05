# https://skillbox.ru/media/code/funkciya-range-v-python/

for i in range(3):
    for j in range(5):
        print('*', end=' ')
    print()


# Теперь решим задачу посложнее. 
# Напишем код, который создаст приветственные сообщения для каждого человека в двух вариантах:

names = ['Boba', 'Biba', 'Buba']
greetings = ['Hello', 'Hi']
for i in names:
    for j in greetings:
        print(f'{j}, {i}')
    print()