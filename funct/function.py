# В чем разница между func и func()?
'''func — это представляющий функцию объект, который можно назначить переменной или передать другой функции. 
Функция func() с круглыми скобками вызывает функцию и возвращает результат.'''

def qwert(n):
    return n
#func()
a=qwert("Asdf zxcv")
print(a)
b=qwert
print(b("Cccccc"))
print(qwert)

# Как узнать сласс
a='asd asd'
print(type(a).__name__)
print(a.__class__.__name__)

# min() max()
