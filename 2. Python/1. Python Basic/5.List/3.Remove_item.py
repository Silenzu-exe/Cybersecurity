# 1. Remove() : it remove specific item from the list

list1 = ["apple", "banana", "orange"]
list1.remove("banana")

print(list1) 

# 2. Pop(): it removes specific index

list1.insert(2,"mango")
print(list1)

list1.pop(2)
print(list1)

# 3. del : it also remove specific index

list1.insert(2,"banana")
print(list1)

del list1[1]
print(list1)

#4. clear(): it remove every item from the list

list1.clear()
print(list1)