# in set once we created a set we cannot change its item nbut we can add new item

thisset = {"apple", "banana", "cherry"}

#1. add(): to add item in a set
thisset.add("orange")
print(thisset)

#2. update: to add 2 sets or set with other data type(list or tuple)

set1 = {"red", "blue", "green"}
set2 = {"apple", "banana", "orange"}
list= ["black", "pruple"]
set1.update(set2)
print(set1)

set1.update(list)
print(set1)