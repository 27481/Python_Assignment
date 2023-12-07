# Write a Python script to remove all non int values from a list.

original_list = [1, 'hello', 2.5, 3, 'world', 4.7, 5]
integer_list = []

for item in original_list:
    if type(item) == int:
        integer_list.append(item)

print("Original List:", original_list)
print("List with only integers:", integer_list)
