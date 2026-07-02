#global variable: variable created outside of the function and can be use by everyone.

x = "Sandesh"

def myfunc():  #create a function.
    print("My name is " + x)    #X is created outside of this function
    
myfunc()



# local vairable
''' If i created two variable using same name one outside the function and another inside the function'''

x = "fun"

def myfun():
    x = "awesome"  #local vairable
    print("python is " + x) # always give priority to the local variable if available, if not thne global variable

myfun()

print("python is " + x)


# GLobal variable inside a function

def function():
    global x           #If i want to create a global funtion inside a function then i use a keyword 'global' 
    x = "test"

function()

print("this is " + x)



#
# Two GLobal variable inside and outside a function


x = "fun"
def function():    #if two global variable then, give priority to the variable inside function...
    global x         
    x = "test"

function()

print("this is " + x)


    