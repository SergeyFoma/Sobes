class Product:
    def __init__(self, name, price):
        self.name=name
        self.price=price

    def __str__(self):
        return self.name

prod1=Product('Prod1', 100)
print(str(prod1) +' '+ str(prod1.price))
print('Product: '+prod1.__str__())