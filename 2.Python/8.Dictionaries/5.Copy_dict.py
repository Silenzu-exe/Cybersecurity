#Copy a dictionarie 
#to copy a dict we use copy() or dict

thisdict = {
    "name" : "sandesh",
    "major": "Csit",
    "age" : 21
}

newdisct = thisdict.copy()

print(newdisct)

newdict = dict(thisdict)  #copy one dictionaries using dict() function.
print(newdict)

thisdict.update({"name":"Silenzux"})
print(thisdict)