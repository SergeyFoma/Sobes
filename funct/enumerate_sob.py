# Функция enumerate() в Python используется при итерации последовательности, 
# чтобы одновременно перебирать элементы и их индексы в цикле. Это упрощает код, 
# делает его более читаемым и эффективным. 
# timeweb.cloud
# olegtalks.ru
# realpython.com
# Функция принимает итерируемый объект (список, строку, кортеж и т. д.) и 
# возвращает итератор, который на каждом шаге отдаёт кортеж из двух элементов: (индекс, значение).
'''Принцип работы
Функция добавляет счётчик к каждому элементу итерируемого объекта и возвращает его.
 Это позволяет: 
ru.hexlet.io
realpython.com
Не вручную управлять индексами — функция возвращает кортеж с индексом и значением, 
поэтому не нужно увеличивать счётчик самостоятельно. 
proglib.io
realpython.com
Указать начальное значение индекса — через параметр start можно задать стартовую нумерацию, 
например, с 1. 
blog.skillfactory.ru
timeweb.cloud
Преимущества использования enumerate():
Читаемость — код становится чище и понятнее.
Меньше ошибок — нет необходимости вручную управлять индексами.
Универсальность — функция работает с любыми итерируемыми объектами.'''

'''Функция enumerate() — это встроенный инструмент Python, который превращает 
итерируемый объект (например, список) в последовательность пар (индекс, значение). 
Другими словами, она автоматически нумерует элементы коллекции, избавляя вас от необходимости 
делать это вручную.'''

# https://sky.pro/wiki/python/kak-ispolzovat-enumerate-v-python-dlya-perebora-spiskov/

# Без enumerate()
fruits=['apple','tomate','banan','orange']
count=0
for f in fruits:
    count+=1
    print(count,f)

#  enumerate()
fruits=['Apple','Tomate','Banan','Orange']
fruits2=[]
#fruits3=[]
for num, f in enumerate(fruits):
    fruits2.append((num+1, f.upper()))
    # fruits2.append(num+1)
    # fruits3.append(f)
print(sorted(fruits2))
#print(list(zip(fruits2,fruits3)))

colors = ['red', 'green', 'blue']
col=[]
for num, c in enumerate(colors,start=1):
    col.append([num,c])
    print(num,c)
print(col)

# Если нужны только индексы
a=('qw','as','zx')
for i,_ in enumerate(a,start=1):
    print(i)

# Если нужны только значения (хотя проще использовать просто for value in colors)
for _,i in enumerate(a, start=1):
    print(i)

# 1. Создание словаря из списка с индексами в качестве ключей
alist=['cv', 'df', 'er']
adict={key:value for key, value in enumerate(alist, start=5)}
print(adict)

# 2. Поиск всех вхождений элемента в список
b=[1,3,5,2,4,6,1,2,4,2,5]
for n,i in enumerate(b):
    if i==2:
        print(n,i)

bg=[n for n, i in enumerate(b)if i==2]
print(bg)

# 3. Фильтрация элементов с учётом их позиции
a=[10,21,30,40,53,60]
aa=[(n,i) for n,i in enumerate(a,start=1)if i%2==0]
print(aa)

# 4. Изменение списка на месте с учётом индексов

for n, i in enumerate(aa,start=1):
    a[n]=n*i
print('a',a)

# 5. Работа с несколькими списками одновременно
rr=[1,2,3]
tt=[4,5,6]
yy=[7,8,9]
res=[]
for n,(r,t,y) in enumerate(zip(rr,tt,yy),start=1):
    res.append([n,rr,tt,yy])
print((res))

# 7. Изменение начального индекса для улучшения читаемости
tasks = ['Написать код', 'Протестировать', 'Задеплоить']
for num, task in enumerate(tasks, start=1):
    print(f"Задача #{num}: {task}")