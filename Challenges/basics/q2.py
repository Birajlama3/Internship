# Write a Python program to create a calculator class. Include methods for basic arithmetic operations. 
class Calculator:
    def __init(self,x,y):
        self.x = x
        self.y = y
    def add(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y
    def mul(self,x,y):
        return x*y
    def div(self,x,y):
        if(y!= 0):
            return x/y
        else:
            return("Cannot divide by zero.")

c1 = Calculator()
print(c1.add(10,5))
print(c1.sub(5,3))
print(c1.mul(3,4))
print(c1.div(10,5))


