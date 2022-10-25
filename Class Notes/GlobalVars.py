"""
Global variables can be used by everyone, both inside of functions and outside.
If you create a variable with the same name inside a function, this variable will be local,
and can only be used inside the function.
The global variable with the same name will remain as it was, global and with the original value.
"""

"""
The global Keyword
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
To create a global variable inside a function, you can use the global keyword.
If you use the global keyword, the variable belongs to the global scope.
Also, use the global keyword if you want to change a global variable inside a function.
To change the value of a global variable inside a function, refer to the variable by using the global keyword.
"""

# Example 1
x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()

# Example 2
x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()
print("Python is " + x)


# Example 3
def myfunc():
    global x
    x = "fantastic"


myfunc()
print("Python is " + x)

# Example 4
x = "awesome"


def myfunc():
    global x
    x = "fantastic"


myfunc()
print("Python is " + x)
