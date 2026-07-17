list = ["apple", "banana", "orange"]

list[0] = "manago"

print(list[0])

list[1:3]= ["Grapes", "kiwi"]

print(list)

#insert(position,"value")insert value in list at desire position
list.insert(2,"watermelon")
print(list)

#append("value"): To add an item in the list at the end of the list
list.append("strawberry")
print(list)

#extend(name of list): combine two or more list, it can be used with list,tuple,set,dict
list1 = ["science", "computer"]
list2 = ["physic", "nepali"]
list3 = ("apple","banana")
list1.extend(list2)
list1.extend(list3)
print(list1)