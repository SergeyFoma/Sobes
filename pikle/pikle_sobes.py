# https://kurshub.ru/journal/blog/chto-takoe-modul-pickle-v-python/

import pickle
data = {'name': 'Alice', 'age': 30}
# dump() -- сразу в файл
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)
# dumps() -- в байтовую строку
serialized = pickle.dumps(data)
print(type(serialized))  # <class 'bytes'>
print(serialized)

# load() -- из файла
with open('data.pkl', 'rb') as f:
    restored_data = pickle.load(f)
# loads() -- из байтов
restored_data = pickle.loads(serialized)
print(restored_data)