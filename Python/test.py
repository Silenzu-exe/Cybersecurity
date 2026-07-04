

x = "Hello"

def myfun():
    global y
    y = "name"
    print(x + " World " + y)
    
myfun()

print(x + " " + y)
