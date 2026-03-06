a={'q':12, 'qw':'asd',55:[34,9]}
print(a.keys())
ak=[]
for key in a:
    ak.append(key)
print(ak)

bk=[k for k in a]
print(bk)
