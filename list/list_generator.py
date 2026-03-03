# https://skillbox.ru/media/code/funkciya-range-v-python/

a=[]
for i in range(10):
    a.append(i)
print(a)

b=[i for i in range(-15, 12,2)]
print(b)

# Вопрос 1. Как объединить списки?
print(a+b)
a.append(b)
print(a)

c=['asd','zxc']
for i in b:
    c.append(i)
print('A: ', c)

# Вопрос 2. Как умножать списки?
q=[1,2,3,4]
qq=q*5
print(qq)

# Вопрос 3. Как проверить, существует ли значение в списке?
print(21 in q)

# Вопрос 4. Как перевернуть список?
w=[2,3,4,5]
print(w[::-1])
w.reverse()
print(w)

# Вопрос 5. В чём разница между append и extend? extend -добавляет списками
l1=[2,3,4]
l2=['as', 'sd']
l1.extend(l2)
print(l1)

# Вопрос 6. Как удалить из списка дубликаты?
ls=[2,3,2,4,3,2,5,7,5,8,5,7,'a','s','a']
print(list(set(ls)))

ls2=[]
for i in ls:
    if i in ls2:
        continue
    else:
        ls2.append(i)
print('ls2: ', ls2)

print('-----------------------')

# Вопрос 7. Преобразуйте цикл for в генератор списков
a = [1, 2, 3, 4, 5]  # первый список, по которому бежим
a2 = []  # пустой список, который надо заполнить

for i in a:
    a2.append(i + 1)  # заполняем его в цикле for

print(a2)

al=[i+1 for i in a]
print(al)

print('-----------------')

#Вопрос 8. В чём разница между remove, pop и del?
ar=['qw', 'as', 2,3,4.5,2, 'as']
# Метод remove () удаляет из списка первое совпадающее значение.
ar.remove('as')
print(ar)
# print(ar.remove(2))

# Метод pop () удаляет элемент по индексу и возвращает этот элемент:
ar.pop(1)
print(ar)
print(ar.pop(1))

# Команда del тоже удаляет 
# элемент списка по его индексу, но имеет отличный от pop () синтаксис и ничего не возвращает:
del ar[1:3]
print(ar)
#Наконец, del может удалять целые переменные.
del ar
print(ar)

# https://skillbox.ru/media/code/spiski_v_python_11_voprosov_kotorye_mogut_zadat_na_sobesedovanii/
#Вопрос 9. Чем список отличается от других структур?
