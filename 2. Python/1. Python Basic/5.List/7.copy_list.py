fruits = ["apple", "banana", "cherry"]
newlist = fruits.copy()  #use copy() to copy another list
print(newlist)

newlist1 = list(fruits) #use list to copy another list
print(newlist1)

newlist2 = fruits[:] #slice(:) operator
print(newlist2)

newlist3 = [1,2,3,4]

fruits.extend(newlist3)
print(fruits)