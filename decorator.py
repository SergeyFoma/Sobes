# Что такое декоратор?

# Декоратор позволяет добавить новую функциональность к существующей функции. 
# Это делается следующим образом. Функция передается декоратору, 
# а он выполняет и существующий, и дополнительный код.

'''Декоратор — это особый вид функции, которая принимает другую функцию в качестве входных данных, 
расширяет или изменяет ее поведение и возвращает измененную функцию без изменения ее исходного кода.
Декораторы следуют ключевому принципу в программировании — Принципу открытости/закрытости, 
который гласит, что код должен быть открыт для расширения, но закрыт для модификации. 
С помощью декораторов вы можете добавлять новое поведение функциям без изменения их оригинального кода.'''

import time

def time_decor(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        finish = time.time()
        result = finish - start
        print(f"Функция {func.__name__} выполнялась {result:.4f} секунд")
        return res
    return wrapper

@time_decor
def calc_sum(n):
    return sum(range(n))
calc_sum(1000000)





def func_decorator(func):
    def wrapper(*args, **kwargs):
        print('------------Что-то до------------')
        res = func(*args, **kwargs)
        print('------------Что-то после---------------------')

        return res
    return wrapper

def some_func(title, tag):
    print(f'title={title}, tag={tag}')
    return f'<{tag}>title</{tag}>'

some_func = func_decorator(some_func)
res=some_func('Python', 'h1')
print(res)



import sys

def mem(func):
    def wrapper(*args, **kwargs):
        res=func(*args, **kwargs)
        print(f'Функция {func.__name__} занимает {sys.getsizeof(func)} bit')
        return res
    return wrapper

@mem
#@time_decor
def tim_tup(n):
    ali=[]
    for i in range(n, 1000000):
        ali.append(i*9999)
    atup=tuple(ali)
    #print(atup)
    return atup 
tim_tup(3)

@mem
#@time_decor
def tim_list(n):
    ali=[]
    for i in range(n, 1000000):
        ali.append(i*9999)
    return ali

tim_list(3)



def upper_st(func):
    def wrapper(*args, **kwargs):
        print('Hello')
        result = func(*args, **kwargs)
        print('Good by!')
        return result
    return wrapper

def st_upper(stroka):
    return stroka.upper()

print(st_upper('asdf xcvb.'))