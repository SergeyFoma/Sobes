# Как разделить список Python

a=[1,2,3,4,5,6]
a1=a[0:3]
a2=a[3:]
print(a1, a2)

asd=[i for i in a if i%2 !=0]
print(asd)

n=3
for i in range(0, len(a), n):
    res=a[i:i+n]
    print('resultat: ',res)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 3
#print(split(lst, n))

#print(7//2)
#print(a.__dir__())

#Как удалить из списка дубликаты?
dubl=[3,4,5,3,2,1,5,2,5]
dubl_set=set(dubl)
print(list(dubl_set))

dub2=['a','d',34,'a','d','a',5,8,5,3,5]
dub2_2=[]
for i in dub2:
    if i not in dub2_2:
        dub2_2.append(i)
print("DUB2_2: ", dub2_2)

dubg=[4,4,4,5,5,5,2,3,2,3]
dubg2=[]
[dubg2.append(x) for x in dubg if x not in dubg2]
print(sorted(dubg2))

dubdict=[2,3,4,2,3,4,5,6,3,6,7,3,6,5]
dubdict=list(dict.fromkeys(dubdict))
print("dubdict: ", dubdict)


# Как проверить, существует ли значение в списке?
a=['q','we',4,6,8]
if 'we' in a:
    print("W: ", 'we')
else:
    print("NO")

val=4

f=False
for i in a:
    if i == val:
        f=True
        break
if f:
    print('YES: ', val)
else:
    print("NOOO")

anylist=[2,3,4,5,6]
flag=any(x==4 for x in anylist)
if flag:
    print('flag: ', flag)
else:
    print("flag none")

# В чем разница между append и extend?
a=[1,2,3,4]
a.append(8)
print(a)
b=[12,23]
a.extend(b)
print(a)

a.insert(2,55)
print(a)