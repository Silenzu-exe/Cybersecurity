#List is used to store multiple value inside a single variable

funlist = ["apple", "banana","orange"]
list1 = [1,2,"mango",True]
print(list1[1])

print(funlist)

#list are changable, allow duplicates,ordered first item is denoted by [0], 2nd item[1]

print(funlist[0])   
print(funlist[-1])  #-1 access last item, -2 2nd last item and so on

print(list1[0:3])   #print list in range last range is not included

funlist[0] = "mango" #change the value of list[0] from apple to mango
print(funlist[0])

print(len(funlist))   #display no of item in a list

print(type(funlist)) 

mylist = list(("apple", "mango"))
print(mylist)