# Tuples are used to store multiple items in a single variable like a list but tuple cannot be change(immutable)
# Tuples are stored in side small bracket

tuple = ("apple", "banana", "cherry")
print(tuple)

#lenth of tuple:
print(len(tuple))

#for single element in tuple we use comma
tuple1 = ("computer", )
print(type(tuple1))

tuple2 =("apple") #not a tuple 
print(type(tuple2))

#Access tuple
print(tuple[:2])