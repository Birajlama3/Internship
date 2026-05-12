# Total no. of a digit in a number.
num = 12345
count = 0 
while(num!=0):
    x = num % 10
    
    count+=1
print("Total number of a digit in num is:", count)