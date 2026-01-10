class Auto:
    def __init__(self, brand, model, power):
        self.brand=brand 
        self.model = model 
        self.power = power 

    def get_tax(self):
        rate=10
        if self.power >100:
            rate=12
        return self.power * rate

auto1=Auto('Audi', 'A3', 100)
print(auto1.get_tax())
class Bus(Auto):
    def set_places(self, seating, standing=0):
        self.seating=seating
        self.standing=standing

    def total_places(self):
        return self.standing + self.seating
    
    def get_tax(self):
        rate=35
        return self.power * rate
auto2=Auto('A2', "a20", 200)
print("auto2 get_tax= ", auto2.get_tax())  

bus1=Bus('Paz', 'P1', 200)
bus1.set_places(50, 10)
# print(bus1.brand, bus1.model, 'get_tax- ',bus1.get_tax())
print(bus1.total_places(), 'get_tax переопределён= ',bus1.get_tax())