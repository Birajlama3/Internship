# Count occurence of a specific elements in a list and print the reversed list.
nums= [10,20,30,40,50,60,70,10,50,900,30,10]
target = 10
count = 0
for num in nums:
    if num == target:
        count+=1
print("The occurence of the number", target, "is", count)
for items in reversed(nums):
    print(items, "")