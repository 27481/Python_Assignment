# Write a python program to Sort a tuple of tuples by the second item.
# tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))



tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))

# Defining a lambda function to do custom sorting
lambdaa=lambda x: x[1]

# Using sort() function to do custom sorting 
sorted_Tuple=tuple(sorted(tuple1, key=lambdaa))



print("Sorted Tuple :\n", sorted_Tuple)