# Write a python program to create and print a dictionary which stores your information.
# (name, age, gender .....)


dict={
    'name':'utkarsh',
    'age':30,
    'gender':'male',
}


# Printing the dict 
print("Personal Info is =>")
for key,value in dict.items():
    print(f"{key.capitalize()}: {value}")




