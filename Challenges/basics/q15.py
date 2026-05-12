# list using two other lists.
#write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.

l1 = [1,2,3,4,5,6,7,8]
l2 = [9,10,11,12,13,14]
res = list()
odd_element = l1[0::2]
print("The odd index element from the list1 is:", odd_element)

even_element = l2[1::2]
print("The even index element from the list2 is:", even_element)

print("The final list from both lists are:")
res.extend(odd_element)
res.extend(even_element)
print(res)
