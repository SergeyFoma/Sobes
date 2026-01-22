# % format() f

name="Alisa"
age=34
print("%s%d"%(name,age))

'''
message, name, age = map(str.strip, input().split(" | "))
# -- ваш код начинается тут
result="Меня зовут %s. Мне %d."%(name,int(age))
# -- ваш код заканчивается тут
print(result)

message, name, age = map(str.strip, input().split(" | "))
# -- ваш код начинается тут
result="Меня зовут {0}. Мне {1}.".format(name, age)
# -- ваш код заканчивается тут
print(result)
'''
# name="Lia"
# age=55
# print("My name is {0}. I {1} old.".format(name, age))

# num='100'
# print(f"{int(num)*2+100}")




# n = int(input())

# # -- ваш код начинается тут
# if n / 6 % 2 == 0 or n == 6:
#     result = 'True'
# else:
#     result = 'False'


# -- ваш код заканчивается тут

#print(result)

'''1 — ★
2 — ★★
3 — ★★★
4 — ★★★★
5 — ★★★★★'''
# sta=int(input('inT: '))
# res=['*', '**', '***', '****', '*****']
# result = res[(int(sta)-1)]
#print(result)

print(ord('★')) # -> 9733
print(chr(9733)) # -> ★

# right x=0-100
# left x = 100-0
# down y=0-100
# up y=100-0





# x, y, direction = map(str.strip, input().split(" "))
# x = int(x)
# y = int(y)
# print(x, y, direction)
# if direction == 'left':
#     result=f'x: {x-1}, y: {y}, direction: {direction}'
#     if x==0:
#         result=f'x: {x}, y: {y}, direction: {direction}'



# if direction == 'right':
#     result=f'x: {x+1}, y: {y}, direction: {direction}'
#     if x==100:
#         result=f'x: {x}, y: {y}, direction: {direction}'



# if direction == 'down':
#     result=f'x: {x}, y: {y+1}, direction: {direction}'
#     if y==100:
#         result=f'x: {x}, y: {y}, direction: {direction}'


# if direction == 'up':
#     result=f'x: {x}, y: {y-1}, direction: {direction}'
#     if y==0:
#         result=f'x: {x}, y: {y}, direction: {direction}'


# print(result)

# n=int(input('NNN: '))
# res=sum([i for i in range(0, n+1) if i%2!=0])
# print(res)

# import math
# num = int(input('Num: '))
# #n=[i for i in range(1, num+1, 2)]
# result = math.prod([i for i in range(1, num+1, 2)])
# print(result)

'''print(__import__('math').prod(range(1, int(input()) + 1, 2)))'''


# n, m, k = map(str.strip, input().split(" | "))
n, m, k = 2, 9, 1 # 1-5 2-3 3-0
n = int(n)
m = int(m)
k = int(k)



# -- ваш код начинается тут
result=int()
if n>=m:
    result = 1
elif n < m and k >= n:
    result = -1
#else:
    # res=m-n+k
    # print(res)
    # res2=res-n+k
    # print(res2)
    # res3=res2-n+k
    # print(res3)
    # res4=res3-n+k
    # print(res4)

    
# -- ваш код заканчивается тут
#print(result)
    # print(int(6/3+2))
    # print(int(10/4+1))

    
n, m, k = 3, 6, 2 # 1-5 2-3 3-0
n = int(n)
m = int(m)
k = int(k)

#for i in range(1, m+1):
#print((((m-n+k)-n+k)-n+k)-n)
if (m-n)!= 0:
    res=m-n+k
    #print(res)

x=m-n+k
y=x-n+k
print(x)
print(y)
while x < (m+1)-n+k:
    print('x= ', x)
    print('y= ', y)
    x += 1
    y += 1
