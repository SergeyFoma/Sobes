import array as ar 

ar1 = ar.array('d', [2.0, 3.2, 45.67])
print(ar1)
print(ar1[2])
print(ar1[-2])
for i in ar1[::-1]:
    print(i)

ar1[1]=5.55
print(ar1)

# Используя метод append, можно добавить один элемент в конец массива:
ar1.append(100.0)
print(ar1)

# Чтобы добавить сразу несколько элементов, можно использовать метод extend:
ar1.extend([87.9, 45.54, 7.1])
print(ar1)

# С помощью метода insert() можно вставить элемент в массив на любую нужную позицию:
ar1.insert(3, 777.7)
print(ar1)

ar2=ar.array('i', [1,2,3])
ar3=ar.array('i',[5,6,5])
ar4=ar2+ar3
print(ar4)
ar5=ar.array('d', [2.0, 3.0, 4.0])
ar6=ar.array('d', [5.0, 6.0])
#ar6.extend(ar5[0:2])
ar6.append(ar5[1])
print(ar6)

print(ar6.typecode)
print(ar6.itemsize)
print(ar6.buffer_info())
print(ar6.byteswap())
print(ar6.count(0))
ar7=ar.array('w', 'hello zxcv asdf')
print(ar7[0])

ar8=ar.array('u',['2','3'])
print(ar8)