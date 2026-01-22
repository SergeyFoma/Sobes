'''У вас есть переменные n, m, k, которые содержат входные пользовательские данные.
Волшебник продает волшебные мечи принцам, желающим убить дракона. У каждого меча есть основная характеристика – число драконьих голов, которые он срубает за один удар. Драконы имеют свои характеристики, включая число голов и скорость регенерации голов.
Число n, представляющее число голов, которые меч срубает одним ударом.
Число m, представляющее число голов дракона.
Число k, представляющее число голов, которые дракон может отрастить за раз.
Напишите код, который определяет, сможет ли принц убить дракона, используя определенный меч, и если да, то сколько ударов потребуется. При этом, бои принцев с драконами всегда протекают одинаково: принц атакует дракона, а затем прячется за щитом; дракон атакует огненным дыханием и может восстановить потерянные головы.
Если принц может убить дракона, ваше решение должно записать в переменную result количество ударов, необходимых для убийства дракона.
Если убить дракона таким мечом невозможно, ваше решение должно записать в переменную result значение -1.'''

#n, m, k = map(str.strip, input().split(" | "))
#n, m, k = 4, 10, 1
n, m, k = 3, 6, 2
n = int(n)
m = int(m)
k = int(k)

# -- ваш код начинается тут
# result=int()
# if n>=m:
#     result = 1
# elif n < m and k >= n:
#     result = -1
# else:
#     res=m-n+k
#     while int(res) > 0:
#         #print(result)
#         result = int(res)-n+k
#         if k ==1:
#             result = int(res)-n+k-1
#         break
        
# -- ваш код заканчивается тут
#print(result)

#--------------------------------------------------

# -- ваш код начинается тут

def battle(sword_heads,current_heads, new_heads):
    r = 1
    if sword_heads == current_heads:
        return 1
    elif sword_heads <= new_heads:
        return -1
    else:
        while current_heads > sword_heads:
            r += 1
            current_heads = current_heads - sword_heads + new_heads
    return r

result = battle(n,m,k)
# -- ваш код заканчивается тут

print('battle= ',result)

# ----------------------------------------------------

# -- ваш код начинается тут
count = 0 

if n >= m:
    count = m // n
    result = count
    if count == 0:
        result = 1
elif n < m and n > k:
    while m > 0:
        count += 1
        m -= n
        if m > 0:
            m += k
    result = count
elif n < m and n <= k:
    result = -1

# -- ваш код заканчивается тут

print ('Code-1= ', result)

# ------------------------------------------------------

n, m, k = 3, 6, 2
n = int(n)
m = int(m)
k = int(k)

# -- ваш код начинается тут
if n >= m:
    result = f'1={1}'               # one blow kill
elif n <= k:
    result = -1              # never killable
else:
    count = 0
    while m > 0:
        count += 1
        m = m - n            # blow
        if m > 0:
            m = m + k        # regen
        if m == 0:
            break
    result = count
    print(count)
# -- ваш код заканчивается тут

print(result)

# --------------------------------------------------------

n, m, k = 3, 6, 2
n = int(n)
m = int(m)
k = int(k)

# -- ваш код начинается тут
l, result = m, 0
while True:
    if l > m:
        result = -1
        break
    l -= n
    result += 1
    if l <= 0:
        break
    l += k
# -- ваш код заканчивается тут

print(result)

# -----------------------------------------------

from math import ceil

#n, m, k = map(int, input().split(" | "))
n, m, k = 3, 6, 2
n = int(n)
m = int(m)
k = int(k)

# -- ваш код начинается тут

result = 1 if n >= m else -1 if k >= n else 1 + ceil((m - n) / (n - k))

# -- ваш код заканчивается тут

print('ceil= ', result)

# -----------------------------------------

#n, m, k = map(str.strip, input().split(" | "))
n, m, k = 3, 6, 2

n = int(n)
m = int(m)
k = int(k)

# -- ваш код начинается тут
if n >= m:
    result = 1
else:
    if n <= k:
        result = -1
    else:
        result = (m - n) // (n - k) + 1


# -- ваш код заканчивается тут

print('hh=', result)

#-----------------------------------------------

n, m, k = 3, 6, 2

n = int(n)
m = int(m)
k = int(k)

# -- ваш код начинается тут

max_head = m
count = 0

while True:
    count += 1
    m -= n
    if m < 1:
        break

    m = min(m + k, max_head)
    if m == max_head:
        count = -1
        break

result = count

# -- ваш код заканчивается тут

print('while-2= ',result)

#---------------------------------------------

n, m, k = 3, 6, 2

n = int(n)
m = int(m)
k = int(k)
# -- ваш код начинается тут

result = (((1 + (m-n) // (n-k,1)[n==k]), -1)[n<=k], 1)[n>=m]

# -- ваш код заканчивается тут

print('One str= ', result)

#--------------------------------

n, m, k = 3, 6, 2

n = int(n)
m = int(m)
k = int(k)

result = 1 if n >= m else -1 if k >= n else 1 + (m - n) // (n - k)
print('One str-2= ', result)