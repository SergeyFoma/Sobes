a=0
while a <= 10:
    print(a)
    a += 1

print('-------------------------')

# Iterate through the loop.
c=0
cc=[10,20,30,40,50]
ccc=[]
while c < len(cc):
    print(cc[c], 'C: ',c)
    ccc.append(cc*2)
    c+=1
    #break
print("CCC: ", ccc)