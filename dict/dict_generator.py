adict={key: key**2 for key in range(1,5)}
print(adict)

ad1=[1,2,3,4]
ad2=['q','w','e','r']
ad3=dict(zip(ad1,ad2))
print(ad3)

ad4=[1,2,3,4]
ad5=['q','w','e','r']
ad6={k: v for (k,v) in zip(ad4,ad5)}
print('AD6: ',ad6)

print(ad6.items())
print(ad6.keys())
print(ad6.values())