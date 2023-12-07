# Write a python program to create a function which expects kwargs arguments.


def kwargs_arguments(**kwargs):
    for key,value in kwargs.items():
        print(f"key:{key}, Value :{value}")






# giving n number of arugment in the above declared function 
kwargs_arguments(name="Alice", age=30, city="New York")