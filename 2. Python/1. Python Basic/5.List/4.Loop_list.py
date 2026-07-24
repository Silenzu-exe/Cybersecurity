#loop through a list

list = ["apple", "banana", "manago"]

for a in list:      #print item of a list one by one..
    print(a)


#loop through index:

for i in range(len(list)):
    print(list[i])
    
# while loop:

list1 = ["science", "math", "nepali"]
i = 0

while i  < len(list1):
    print(list1[i])
    i = i + 1

# loop using loop compherension: offers short syntax for looping

[print (x) for x in list]
    