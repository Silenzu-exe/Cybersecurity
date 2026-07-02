color = ("red", "black", "blue", "green")

(x, y, *z) = color
print(x)

list1 = list(color)

list1.append("orange")
print(list1)

list1.remove("red")
print(list1)

for x in color:
    print(x)

print("\n")

for i in range(len(color)):
    print(color[i])

print("\n")

i = 0   
while i < len(color):
    print(color[i])
    i =i + 1
    
