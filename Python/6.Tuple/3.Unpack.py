#Unpacking : in Python, we are also allowed to extract the values back into variables. This is called "unpacking".

fruits = ("apple", "banana", "cheery")

(red, green, blue) = fruits

print(red)
print(green)
print(blue)
print("\n")

#if we have less no. of variable then the value in tuple then we use * that act as a list:

tuple = ("Silenzu", "black", "red", "blue")

(x, y, *z) = tuple

print(x)
print(y)
print(z)