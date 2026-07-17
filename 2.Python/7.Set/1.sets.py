''' sets is a method to store multiple items or value in a single variable just like list and tuple
    set is also immutable like tuple meaning we cannot change the item of sets once it is created
    set doesnot allow same value twice and it treates True and 1 as one value and same with False and 0. 
'''

thisset = {"apple", "banana", "cheery"}
print(thisset)

set1 = {True, 1, "apple", "apple"} #in this set apple and true is displayed only once 

print(set1)

#we can use set() constructor to convert item in to set

set2 = set(("apple", "banana", "cherry"))
print(set2)


#Access set:

#Item of a set cannot be accessed directly with index but we can access using loop or in operation to check if item is present or not

for x in thisset:
    print(x)

if "apple" in  thisset:
    print("yes there is apple")
else:
    print("nooo")
