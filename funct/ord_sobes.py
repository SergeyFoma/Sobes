import time
import sys

start = time.time()
print(ord("A"))
finish = time.time()
result = finish-start
print("Result: ", start, finish, result)

start = time.time()
word = "DdUurianN"
word_list = []
for i in word:
    print(ord(i))
finish = time.time()
result = finish-start
print("Result FOR: ", start, finish, result)

start = time.time()
word_map = list(map(lambda i: ord(i), word))
print("WORD MAP: ", word_map)
finish = time.time()
result = finish-start
print("Result MAP: ", start, finish, result)

start = time.time()
word_generator = [ord(i) for i in word]
print("word_generator: ", word_generator)
finish = time.time()
result = finish-start
print("Result Word_generator: ", start, finish, result)

print('---------------------')

print(ord('C'))
print(id(ord('c')))