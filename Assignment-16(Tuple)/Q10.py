# Write a python program to change the first item (22) of a list within the following tuple
# to 222.

tuple1=([22,33,44],55,66)

print("Original tuple ==>:",tuple1)

modified_list=list(tuple1[0])
modified_list[0]=222


new_tuple=(modified_list, *tuple1[1:])

print("New Tuple ===>:", new_tuple)