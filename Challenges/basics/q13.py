# Return Multiple value from a single function
a = 10
b = 5
def calculation():
    sum = a+b
    dif = a-b
    mul = a*b
    div = a/b
    return sum, dif, mul, div
print("The sum and the difference is:", calculation())