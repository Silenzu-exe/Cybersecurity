'''in dictionaries: there are several ways to access a dict
1. get("keys"): it will display value of the specific key mention inside the box
2. values(): it will list all the value inside the dict
3. keys(): it will list all the keys inside the dict
4. item(): it will list both key: value pair

#to add a new key value pair or change the value of existing key we use 
update({"key": "value"}) function
'''
thisdict = {
    "name": "sandesh",
    "age" : 21,
    "home" : "syangja"
}

#do the same thing as get()
x = thisdict['name']
print(x)

#get()
y = thisdict.get('age') 
print(y)

#value()
z = thisdict.values()
print(z)

#get()
m = thisdict.keys()
print(m)

#items()
v = thisdict.items()
print(v)

#directly change the value of key

thisdict['home'] = "Bayarghari"
print(v)

#chaning the value of a key using update():

thisdict.update({"age" : 22})

print(thisdict)

dict1 = dict(name = "silenzu", age = 21 )
print(dict1)

dict1.update({"Study" : "CSIT"})
print(dict1)