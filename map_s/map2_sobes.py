a=['Vasya ', 'Bob ', 'Max ']
b=['Pupkin', 'Bobik', 'Mix']

ab=map(lambda x,y: x+y, a,b)
print(list(ab))

def f_nam(f,n):
    '''qwerqwe'''
    return f+' + '+ n

ab2=map(f_nam, a, b)
print(list(ab2))

word = ['Asdf', 'qweqweqwe', 'vmcj fgh']
w=map(lambda x: len(x), word)
print(list(w))

fruits = ['Apple', "orange", "Banan"]
for i in fruits:
    print(f"I like {i}")
    print(i)

fr = map(lambda x: f"I like {x}", fruits)
print(list(fr)[0])
#print(f'{list(fr)[1].upper()}!')

'''Когда использовать map(): для готовых функций или больших данных (итератор экономит память), 
когда функция для преобразования одна. 
Для большего количества преобразований и сложной логики лучше подойдёт цикл for.'''

#import traceback


