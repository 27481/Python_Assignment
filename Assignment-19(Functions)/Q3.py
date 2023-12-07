# Write a python program to create a function which expects an unknown number of
# arguments.

#! we can give unknown number of arguments to a function by using *args and **kwargs
""" 
*args allows a function to accept a variable number of positional arguments as a tuple.
**kwargs allows a function to accept a variable number of keyword arguments as a dictionary.
"""

def unknown_arguments(*args):
    print("Received",len(args),"arguments",args)
    for arg in args:
        print("Argument :", arg)




# Giving n number of arguments to the function above 
unknown_arguments(1,2,"hello","world","Python")
unknown_arguments(1,2,"hello","world","Python",'a','b','c')