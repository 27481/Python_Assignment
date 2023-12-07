# Write a python program to add elements of list to a set
# thisset = {"Python", "Django", "JavaScript"}
# mylist = ["Java", "C"]

thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]

for item in mylist:
    thisset.add(item)  # Add each item from mylist to thisset

print("Updated Set:", thisset)

