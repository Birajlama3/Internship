# Product class with stock value calculator.
class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_value(self):
        total_val = self.price * self.quantity
        return total_val
p1 = Product("Headphones",1000,3) 
print(f"The total value of {p1.name} is {p1.total_value()}")
        