#print((1*(1/7))*(3*(1/13)))
d='(1*(1/7))*(3*(1/16))' # (1*7+1)/7 * (3*16+1)/16 = 8/7 * 49/16 = 7/2=3(1/2)

# выделяем целые числа
d1='1*(5/7)'
d1_split=  d1.split('*')[0] # первое целое
print('d1_split: ', d1_split)
#print('/: ', d1_split[1].index('/')+1)
d2='3*(1/16)'
d2_split=d2.split('*')[0] # второе целое
print(f'd2_split: {d2_split}')

# разбиваем дроби на знаменатели и числители
# знаменатели
#print('d1_split[-1]: ', d1.split('*')[-1][-2])
z1_index_start = d1.split('*')[1].index('/')
print('z1_index_start', z1_index_start)
z1_index_finish = d1.split('*')[1].index(')')
print('z1_index_finish', z1_index_finish)

z2_index_start = d2.split('*')[1].index('/')
print('z2_index_start', z2_index_start)
z2_index_finish = d2.split('*')[1].index(')')
print('z2_index_finish', z2_index_finish)

# print('AAA', d1.split('*')[1][z1_index_start+1:z1_index_finish])

z1=d1.split('*')[1][z1_index_start+1:z1_index_finish]
print('z1: ', z1)
z2=d2.split('*')[1][z2_index_start+1:z2_index_finish]
print('z2: ', z2)

# числители
h_1=(int(d1_split)*int(z1)+1)
h_2=(int(d2_split)*int(z2)+1)
print('h1: ', h_1, 'h2: ', h_2)

# преобразованные дроби
d1_1=[h_1, int(z1)]
d1_2=[h_2, int(z2)]
print('d1_1, d1_2: ', d1_1, d1_2) # (8/7) * (49/16)

# сокращаем дробь находим общий делитель
sokr1=int(d1_2[0])/int(d1_1[1])
print('sokr1: ', int(sokr1))
sokr2=int(d1_2[1])/int(d1_1[0])
print('sokr2: ', int(sokr2))

#print(7/2)

def common_divisor(a,b):
    if a[0]<b[1]:
        if b[1]%a[0]==0:
            res=b[1]/a[0]
    else:
        if a[0]%b[1]==0:
            res=a[0]/b[1]
    if a[1]<b[0]:
        if b[0]%a[1]==0:
            res2=b[0]/a[1]
    else:
        if a[1]%b[0]==0:
            res2=a[1]/b[0]
    print('RES: ', res2,'/',res)
#common_divisor([8, 7], [49, 16])
common_divisor(d1_1, d1_2)
print(17%8)
# d1_h=h_1*h_2
# d1_z=int(z1)*int(z2)
# print('his: ', d1_h,'znam: ', d1_z)


# def divider(a, b):
#     """function divider"""
#     al = []
#     bl = []
#     for i in range(2, b + 1):
#         res = a % i
#         res2 = b % i
#         if res == 0:
#             al.append(i)
#         if res2 == 0:
#             bl.append(i)

#     result = al + bl
#     print(al, bl)
#     print('RESULT: ', result)
#     sx = set()
#     # sx.add(12)
#     # print('SX==',sx)
#     for x in result:
#         #print(x)
#         if result.count(x) == 2:
#             #print(x)
#             sx.add(x)
#             #print('X',x)
#     print(sx, type(sx))
# divider(d1_h, d1_z)
# result=divider(d1_h, d1_z)
# print("divider: ", result)

# # сокращаем дробь
# short_h=d1_h/result
# short_z=d1_z/result
# #print(short_h, short_z)
# result2=f'{int(short_h)}/{int(short_z)}'
# print('result2: ', result2)
# print(int(short_h)/int(short_z))