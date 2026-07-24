# List comphersion: Offers a short syntax


#Normal:
fruits = ["apple", "banana", "cherry"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)


#comphersion:
newlist1 =[x for x in fruits if "a" in x]
print(newlist1)

newlist1 =[x.upper() for x in fruits if x != "apple"]
print(newlist1)

newlist1 =[x if x != "banana" else "orange" for x in fruits]
print(newlist1)