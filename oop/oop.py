# https://habr.com/ru/articles/969088/
# https://python-academy.org/ru/guide/oop

# Объектно-ориентированное программирование — это подход к разработке программ, 
# при котором программа строится как набор объектов, каждый из которых является экземпляром 
# определенного класса, 
# а классы образуют иерархию наследования.
# Класс (Class) — это чертеж робота. В нем написано: «У робота должны быть имя, уровень заряда и серийный номер». 
# Чертеж сам по себе ничего не делает. Он просто висит на стене.
# Объект (Object) — это конкретный робот, собранный по этому чертежу. Его можно потрогать, включить, отправить на работу.
# одному чертежу (Классу) можно собрать тысячи разных роботов (Объектов). У одного будет имя «Бендер», у другого «R2D2», но структура у них одинаковая.

# __init__ -конструктор класса. Зарезервированно python.
# self - 
# self.name - атрибуты объекта или переменные объекта
class Product:
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.currency = 'Rub.'

    # Создаём метод класса для обработки цены
    #def get_full_price(self, currency='rub'):
    def get_full_price(self):
        full_price = self.price * self.quantity # переменные метода
        result = f'{full_price}{self.currency}'      #  переменные метода
        return result
    
    def update_price(self, new_price):
        self.price = int(new_price)

    def set_currency(self, currency):
        self.currency = currency.lower()


# создаём объект(экземпляр класса)
prod1 = Product("Рис", 123, 34)
print(prod1.name)
print(prod1.price * prod1.quantity)

milk = Product('Milk', 120, 20)
print(milk.name, milk.price, milk.quantity)

print('get full price', milk.get_full_price())
print('prod1', prod1.get_full_price())

prod1.update_price(new_price=100)
print('update_price=', prod1.get_full_price())

# print(milk.get_full_price(currency=' USD'))
# print(prod1.get_full_price(currency=' Krona'))
milk.set_currency(currency='R.')
print(milk.name, milk.currency)