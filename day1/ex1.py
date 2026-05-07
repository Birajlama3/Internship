# This is comment.

x  = 10 # variable
y = 20

if(x>y): #if-else statement 
    print("X is greater than y")
else:
    print("Y is greater than X")

# Multipe output variable using comma.
x = 3
y = "Nabin"
z = "Kamalesh"
print(x,y,z)

#Global Variable
a = "Biraj"
def display(): #Function
    b= "bijay" #local variable
    print("The Name is :", a)

display()

#DataTypes
x = "John" #Strings
x = 10 #int 
y = 10.3 #float
fruits = ['banana','apple','orange'] #List
fruits = ('apple','guava','grapes') #tuple
fruits = {'apple', 'guava', 'pomegranate'} #dictionary
x = True # Bool

# Casting used to specify type of a variable.
x =float(1.3)
name  = str("Biraj")

#Python Match
day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 3:
        print("Thursday")
    case 3:
        print("Friday")
    case 3:
        print("Saturday")
    case 3:
        print("Sunday")
    
# for loops
fruits = ['apple', 'banana', 'guava']
for x in fruits:
    print(x) 

#Break statements in loop
fruits = ['apple', 'banana', 'guava']
for x in fruits:
    print(x)  
    if(x =="banana"):
        break

#Nested loops
adj = ['big', 'juicy','sweet']
fruits = ['apple', 'banana', 'guava']
for x in adj:
    for y in fruits:
        print(x,y)  

# Python functions
temp = 77
def calculate():
  cel = (temp - 32) * 5/9
  print("Temperature in celsius is:", cel)
calculate()

#Function with argument 
def areaofcircle(r):
    area = 3.142 * r * r
    print("Area of circle is:", area,"sq.units")
areaofcircle(7)

# Arbitary Arguments --> used if the no. of total argument is unknown.
def my_function(*name):
    print("The student are:", name)
my_function("Biraj","Nabin","Bijaya")

# Python array
cars = ['bmw','audi','ferrari']
print(cars[0])
cars.append("Honda")
print(cars)

#Lambda Functions
x = lambda a:a+10
print(x(5))

import day1.module1 as m1 # Renaming the module.
m1.greeting("Biraj")

import platform as plt # Built-in module 
x = plt.system()
y = dir(plt)
print(x)

import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))