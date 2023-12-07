# Write a python program to access a function inside a function.


def outer_function():
    def inner_function():
        print("this is the inner function :\n")
    
    print("This is outer function :\n")
    inner_function()  # Calling the inner function inside the outer function 

    





# Calling the outer function 
outer_function()