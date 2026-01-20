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
    print(res)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 3
print(split(lst, n))

#print(7//2)
#print(a.__dir__())
