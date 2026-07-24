#As we know tuple is immutable or unchangable but we can workaround by converting tuple to list

tuple = ("apple", "banana", "cherry")
list1 = list(tuple)

list1[1] = "orange"
print(list1)

list1.append("mango")
print(list1)

list1.pop(2)
print(list1)