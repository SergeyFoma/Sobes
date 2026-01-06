product = {'name':'Milk', 'price':200, 'quantity': 35}
print(product)


# динамическое формирование словаря через функцию
def init_product(name, price, quantity=0):
    return {'name':name, 'price':price, 'quantity':quantity}


milk = init_product(name = 'Milk', price=230, quantity = 55)
ris = init_product(name = 'Ris', price = 54)
brot = init_product('Brot', 52, 33)
print(milk['price'])
print(ris)
print(brot)