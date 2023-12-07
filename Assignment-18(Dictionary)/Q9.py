# Write a python program to merge two python dictionaries into one dictionary.


small_dict1={'a':1,'b':2,'c':3}
small_dict2={'d':4,'e':5,'f':6}
small_dict3={'g':7,'h':8,'i':9}


# We can use dictionary unpacking by (**) operator / update() function

merged_dict={**small_dict1,**small_dict2,**small_dict3}

print(merged_dict)