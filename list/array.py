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