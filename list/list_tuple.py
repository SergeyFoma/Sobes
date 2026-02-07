# Как объединить два списка в список кортежей?

a=[12,23,34]
b=[8,9,6]
c=[tuple(a),tuple(b)]
print(c)

d=map(lambda x,y:(x,y),a,b)
print(list(d))
