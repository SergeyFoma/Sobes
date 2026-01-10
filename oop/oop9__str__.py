class Product:
    def __init__(self, name, price, quantity=0):
        self._name=name
        self._price=price
        self._quantity=quantity

    def amount(self):
        return self._price * self._quantity
    
    def __str__(self):
        quantity=f'QUantity {self._quantity}'
        total=f'Полная стоимость {self.amount()} rub.'
        return f'{self._name} {quantity}\n{total}'
    
prod1=Product('Prod1', 120, 10)
print(prod1._name, prod1._price, prod1._quantity, prod1.amount())
print(prod1)