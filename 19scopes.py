#Global keyword
# The global keyword allows you to modify a global variable inside a function.
x = 10  # Global variable

def modify_global():
    global x  # Declare x as global to modify the global variable
    x = 20  # Modify the global variable

modify_global()
print("Global x:", x)  # Output: Global x: 20


#nonlocal keyword
# The nonlocal keyword is used to modify a variable in the nearest enclosing (non-global) scope.

def outer_function():
    y = 5  # Enclosing variable

    def inner_function():
        nonlocal y  # Declare y as nonlocal to modify the enclosing y
        y = 15  # Modify the enclosing variable

    inner_function()
    print("Nonlocal y:", y)  # Output: Nonlocal y: 15

outer_function()



#key word arguments
# **kwargs allows a function to accept any number of keyword arguments (name=value pairs).
# Inside the function, kwargs is treated as a dictionary.

def greet_people(**kwargs):
    for name, message in kwargs.items():
        print(f"{name} says: {message}")

# Call the function with multiple keyword arguments
greet_people(Alice="Hello!", Bob="Good Morning!", Charlie="Hi!")

# Output:
# Alice says: Hello!
# Bob says: Good Morning!
# Charlie says: Hi!

