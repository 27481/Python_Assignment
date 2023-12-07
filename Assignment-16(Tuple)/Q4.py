# Write a python program to Swap two tuples in Python.

t1=(1,2,3,4,5)
t2=(10,20,30,40,50)


print("Before swap :",t1,t2, sep='\n')

# Swapping both the tuple 
temp_tuple=t1
t1=t2
t2=temp_tuple



print("After swap :",t1,t2, sep='\n');