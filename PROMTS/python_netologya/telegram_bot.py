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

Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api'''

# pythonanywhere
# pip install pyTelegramBotAPI

import telebot

token = "8237776832:AAEFMZBwOOrHCJXUKHKV9JBOjDa08oi2STY" # нужен, что бы зарегистрировать бота на серверах telegram
bot = telebot.TeleBot(token) # переменная содержит все необходимые функции

@bot.message_handler(content_types=['text']) # регистрируем функцию в качестве обработчика сообщений типа text
def echo(message): # функция обработчик
    bot.send_message(message.chat.id,message.text)
bot.polling(none_stop=True) # начинается отправка запросов на сервера tg и спрашивает нет ли для неё сообщений. Если сообщение есть, то начинается обработка


