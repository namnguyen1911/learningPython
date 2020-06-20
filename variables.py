#variables do not need to be declared with any particular type
x = 4
y = "John"
print(x)
print(y)
#variables can be changed type after they have been set
z = 5
z = "Sally"
print(z)
#string variables cna be declared either by using single or double quotes
d = 'Lisa'
print(d)
#Variables names
"""
A variable name must start with a letter or underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores
Variable names are case-sensitive (age, Age, AGE are three different variables)
"""
#Python allows you to assign values to multiple variables in one line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#You can assign the same value to multiple variables in one lines
x = y = z = "Orange"
print(x)
print(y)
print(z)
#Use + to combine both text and variables
x = "awesome"
print("Python is " + x)
#You can also use the + character to add a variable to another variable
x = "Python is "
y = "awesome"
z = x + y
print(z)
#We can not combine a string and a number 
"""
x = 5
y = "John"
print(x + y) -> error
"""
#Global variables must be created outside of the functions
#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value
#You can create a global variable inside the function by using "global" keyword
#You can change a global variable by using "global" keyword inside a function
x = "awesome"
y =  'not bad'
def myfunc():
    global b
    b = "good"
    x = "fantastic"
    global y
    y = 'not very bad'
    
    print("Python is " + x)
    print("Python is also " + b)
    print("Python is " + y)

myfunc()

print("Python is " + x)
print("Python is also " + b)








