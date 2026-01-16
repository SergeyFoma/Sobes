'''Блок finally — компонент механизма обработки исключений в Python, который выполняется всегда, 
независимо от того, произошло исключение в блоке try или нет. 
Назначение: блок finally обеспечивает детерминированное завершение операций, 
особенно при работе с критическими ресурсами (закрытие файлов, соединений с базой данных, 
установление сетевого соединения)'''

class DB:
    connections=0
    def __init__(self, cid):
        self.cid=cid
        print("Открытие соединения {}".format(self.cid))
        DB.connections += 1

    def get_data(self):
        return "Данные из соединения {}".format(self.cid)
    
    def close(self):
        print("Закрытие соединения {}".format(self.cid))
        DB.connections -= 1

c1=DB(10)
c2=DB(20)
print("------Соединений:", DB.connections)

print(c1.get_data())
print(c2.get_data())

c1.close()
print("------Соединений:", DB.connections)

#--------------------------------------------------------
print("----------------------------")

class DB:
    connections=0
    def __init__(self, cid):
        self.cid=cid
        print("Открытие соединения {}".format(self.cid))
        DB.connections += 1

    def get_data(self):
        if self.cid > 10:
            raise ValueError("Слишком большой cid") # возбуждает исключение ValueError
        return "Данные из соединения {}".format(self.cid)
    
    def close(self):
        print("Закрытие соединения {}".format(self.cid))
        DB.connections -= 1

c1=DB(10)
c2=DB(20)
print("------Соединений:", DB.connections)

# print(c1.get_data())
# print(c2.get_data())
try:
    print(c1.get_data())
    print(c2.get_data())
except ValueError:
    pass

c1.close()
print("------Соединений:", DB.connections)

#--------------------------------------------------------
print("----------------------------")

class DB:
    """asdasdasd"""
    connections=0
    def __init__(self, cid):
        self.cid=cid
        self.cid += ""
        print("Открытие соединения {}".format(self.cid))
        DB.connections += 1

    def get_data(self):
        if self.cid > 10:
            raise ValueError("Слишком большой cid") # возбуждает исключение ValueError
        return "Данные из соединения {}".format(self.cid)
    
    def close(self):
        print("Закрытие соединения {}".format(self.cid))
        DB.connections -= 1

c1=DB(10)
c2=DB(20)
print("------Соединений:", DB.connections)

# print(c1.get_data())
# print(c2.get_data())
try:
    print(c1.get_data())
    print(c2.get_data())
except ValueError:
    pass
finally:
    c1.close()
    c2.close()
    print("------Соединений:", DB.connections)

'''Когда выполняется блок finally: 
sky.pro
После нормального завершения блока try — когда код в блоке try выполняется без ошибок, 
блок finally выполняется сразу после него.
После обработки исключения — если в блоке try возникло исключение и оно было обработано в соответствующем 
блоке except, блок finally выполняется после блока except.
После необработанного исключения — даже если исключение не было обработано (нет соответствующего блока except), 
блок finally всё равно выполнится, прежде чем исключение будет передано вверх по стеку вызовов.
При выходе из функции через return — если внутри блока try встречается оператор return, 
блок finally выполняется перед фактическим возвратом из функции.
При выходе из цикла или функции через break, continue — операторы управления потоком выполнения внутри 
блока try не препятствуют выполнению блока finally'''