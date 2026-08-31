#In dict we use for loop for looping:

dict = {
    "name" : "sandesh",
    "major": "Csit",
    "age" : 21
}

for x in dict:    #this diplay keys one by one
    print(x)

print("-------------")

for x in dict:    #this will print values one by one
    print(dict[x])

print("-------------")
  
for x in dict.values():  #we can use for loop with values() to print value.
    print(x)
    
print("-------------") 
  
for x in dict.keys():      #we can use for loop with keys to print keys
    print(x)

print("--------------")

for x in dict.items():   #we can use for loop with items() to print both keys and values
    print(x)