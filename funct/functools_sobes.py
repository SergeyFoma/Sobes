a=[0,1,2,3,4,5,-2,-5,2,3,5,-2,-2]
res=filter(lambda x: x>1,a)
print(list(res))

res2=filter(lambda x: x>0, a)
#print('res2; ', list(res2))
print('res2: ', set(res2))