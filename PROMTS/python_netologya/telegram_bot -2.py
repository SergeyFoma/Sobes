# В telegram регистрируем бота @BotFather
# /newbot  -команда для создания бота
# NewPythonTODO  -название бота
# SFPythonTODObot  -username

'''Done! Congratulations on your new bot. You will find it at 

t.me/SFPythonTODObot. ----ссылка

You can now add a description, about section and profile picture for your bot, 
see /help for a list of commands. By the way, when you've finished creating your cool bot, 
ping our Bot Support if you want a better username for it. Just make sure the bot is fully 
operational before you do this.

Use this token to access the HTTP API:

8237776832:AAEFMZBwOOrHCJXUKHKV9JBOjDa08oi2STY

8237776832:AAEFMZBwOOrHCJXUKHKV9JBOjDa08oi2STY

Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api'''

# pythonanywhere
# pip install pyTelegramBotAPI


import telebot
import random

name = 'Сергей'
token = "8237776832:AAEFMZBwOOrHCJXUKHKV9JBOjDa08oi2STY" # нужен, что бы зарегистрировать бота на серверах telegram
bot = telebot.TeleBot(token) # переменная содержит все необходимые функции

HELP='''
/help - напечатать справку по программе,
/add - добавить задачу в список (название задачи запрашиваем у пользователя),
/show - напечатать добавленные задачи по дате, all - напечатать словарь всех задач,
/random - добавляет случайную задачу на дату "Сегодня".
'''
RANDOM_TASKS = ['Записаться на курс в нетологию.', 'Написать письмо Гвидо',
                'Покормить кошку', 'Помыть машину']

tasks={}

def add_todo(date, task):
    # date = input('Введите дату: ')
    # task = input("Введите задачу: ")
    date=date.lower()
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date]=[]
        tasks[date].append(task)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=['add'])
def add(message):
    #print(message.text)
    command = message.text.split(maxsplit=2) # получаем текст и разделяем его по пробелам
    date = command[1].lower() # получаем из текста дату
    task = command[2] # получаем задачу
    add_todo(date, task) # добавляем задачу на дату
    text = f'Задача {task} добавлена на дату {date}'
    #bot.send_message(message.chat.id, "Команда принята")
    bot.send_message(message.chat.id, text) # отправляем пользователю сообщение, что задача добавлена на дату

@bot.message_handler(command='random')
def random_add(message):
    date='Сегодя'
    task = random.choice(RANDOM_TASKS)
    add_todo(date, task) # добавляем задачу на дату
    text = f'Задача {task} добавлена на дату {date}'
    #bot.send_message(message.chat.id, "Команда принята")
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['show', "print"])
def show(message):
    command=message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ''
    if date in tasks:
        text = date.upper() + '\n'
        for task in tasks[date]:
            text + '[] ' + task + '\n'
    else:
        text = 'Задач на эту дату нет.'

    bot.send_message(message.chat.id, text)
print(tasks)

'''
@bot.message_handler(content_types=['text']) # регистрируем функцию в качестве обработчика сообщений типа text
def echo(message): # функция обработчик
    if name in message.text:
        mess='Ба! Знакомые все лица!'
        bot.send_message(message.chat.id,mess)
    else:
        bot.send_message(message.chat.id,message.text)
bot.polling(none_stop=True) # начинается отправка запросов на сервера tg и спрашивает нет ли для неё сообщений. Если сообщение есть, то начинается обработка
'''

bot.polling(none_stop=True) # начинается отправка запросов на сервера tg и спрашивает нет ли для неё сообщений. Если сообщение есть, то начинается обработка


'''
Финальная версия бота

Библиотека https://github.com/eternnoir/pyTelegramBotAPI (telebot) позволяет создавать 
более сложную логику для ботов.

Например, на этом занятии мы использовали команды. Кроме этого в библиотеке доступны 
следующие фильтры:
content_types - вид сообщения (текст, аудио и т.д.)
commands - список команд
regexp - регулярное выражение
func - произвольная функция, возвращающая True или False

Более подробно - https://github.com/eternnoir/pyTelegramBotAPI#message-handlers

Также с помощью этой библиотеки можно отправлять не только текст, но и аудио, 
видео и даже стикеры.
'''