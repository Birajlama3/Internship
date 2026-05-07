class car :
    def __init__(self,make,model,year):
        self.model=model
        self.year=year
        self.make=make

    def get_descriptive_name(self):
        long_name=f"{self.year} {self.model}{self.make}"
        return long_name

new_car = car('audi','v2','2027') 
print(new_car.get_descriptive_name())