'''To remove any item from a dictionary we use different functions:
    1. pop("key"): This will remove a specific item
    2. del dict_name("key"): does same as pop
    3.clear(): delete all the item in dictionary
'''

dict = {
    "name" : "Silenzu",
    "age" : 21
}  

#pop()
dict.pop("age")
print(dict)

#add item using update()
dict.update({"Home" : "Bayarghari"})
print(dict)

#del 
del dict["name"]
print(dict)
