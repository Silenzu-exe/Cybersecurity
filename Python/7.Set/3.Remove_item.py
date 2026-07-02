''' to remove item from a set we can use multiple function:
1. remove(): it item is not in list it raise error
2. discard(): if item is not in list doesn't raise error
3. del: remove complete set
4. pop(): delete random item form set
5.clear():to clear all item in a list
'''

thisset = {"red", "black", "blue", "green","apple","banana"}

thisset.remove("green")
print(thisset)

thisset.discard("red")
print(thisset)

thisset.pop() #remove random item
print(thisset)

del thisset  #delete the set


