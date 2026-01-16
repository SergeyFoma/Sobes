# while True:
#     x=input("Enter a number: ")
#     try:
#         x=float(x)
#         y=100/x
#         break
#     except ValueError:
#         print("Error, enter a number: ")
#     except ZeroDivisionError:
#         print("You cannot divide by zero.") # на ноль делить нельзя
# print(y)

import traceback 
'''Этот модуль предоставляет стандартный интерфейс для извлечения, 
форматирования и вывода трассировок стека программ на Python. 
Он более гибкий, чем стандартное отображение трассировки стека в интерпретаторе, 
и поэтому позволяет настраивать некоторые аспекты вывода. 
Наконец, он содержит утилиту для сбора достаточной информации об исключении, 
чтобы вывести её позже, без необходимости сохранять ссылку на само исключение. 
Поскольку исключения могут быть основой для больших графов объектов, 
эта утилита может значительно улучшить управление памятью.'''

# while True:
#     x=input("Enter a number: ")
#     try:
#         x=float(x)
#         y=100/x
#         break 
#     except (ValueError, NameError):
#         print("Error, enter a number: ")
#     except ZeroDivisionError:
#         print("Error, you cannot divide by zero!")
#     except Exception:
#         print(traceback.format_exc())# узнаем название исключения ZeroDivisionError и включим её в код выше
# print(y)

while True:
    x=input("Enter a number: ")
    
    try:
        x=float(x)
        if x==1:
            x=None
        y=100/x
        break
    # except ValueError:
    #     print("Error, enter a number: ")
    except ZeroDivisionError:
        print("Error, you cannot divide by zero!")
    # except TypeError:
    #     print("Error, unsupported operand None.")
    except Exception:
        #print(traceback.format_exc())
        f=open("log.txt", "a+")
        traceback.print_exc(file=f)
        f.close()
        print("Invalid value.")
print(y)
