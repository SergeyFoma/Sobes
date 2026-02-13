import sys


#https://tproger.ru/articles/raspredelenie-pamjati-v-python-skolko-i-v-kakih-sluchajah-zanimajut-tipy-dannyh

'''sys.getrefcount — функция в модуле sys Python, которая возвращает количество ссылок на объект. 
Это значение используется Python для управления памятью: когда счётчик ссылок становится 0, 
память, занятая объектом, удаляется.'''

# https://habr.com/ru/articles/951742/

a = 1000
b = a
print(sys.getrefcount(1000))
# 5
del b
print(sys.getrefcount(a))
# 4

print(sys.version) #возвращает строку с версией установленного интерпретатора Python

print(sys.platform) # возвращает название платформы, на которой работает интерпретатор (например, win32, linux, darwin).
print(sys.version_info) #  Возвращает кортеж с компонентами версии (major, minor, micro, releaselevel, serial). Это предпочтительный способ для программных проверок, так как он исключает необходимость парсинга строки.
# if sys.version_info >= (3, 8):
#     print("Эта функция требует Python 3.8 или новее.")
# else:
#     print("Ваша версия Python устарела.")

print(f"Скрипт запущен интерпретатором: {sys.executable}")

# print(dir(a))
# print(id(a))
# print(a.__dir__())

# cv='234'
# print('DIR CV: ', dir(cv))
# print('cv.__dir__ = ', cv.__dir__())
# c=cv.__add__('45')
# print(c)