# Write a python program to create three dictionaries, then create one dictionary that
# will contain the other three dictionaries.



#Creating 3 dictionaries 
dict1={'Name':'utkarsh','Year':'3rd', 'hobby':'coding'}
dict2={'Name':'Pandey','Year':'4rd', 'hobby':'nothing'}
dict3={'Name':'utkarsh Pandey','Year':'3rd', 'hobby':'coding'}


# Creating a dictionary containing the three dictionaries 

merged_dict={
    'First':dict1,
    'Second':dict2,
    'Third':dict3
}

# Accessing the merged dict 
for key,val in merged_dict.items():
    print(f"{key}: {val}")