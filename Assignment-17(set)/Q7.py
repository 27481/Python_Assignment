# Write a python program to remove last item of the given set
# thisset = {"Python", "Django", "JavaScript", “SQL”}


thisset = {"Python", "Django", "JavaScript", "SQL"}

value_to_remove = "SQL"

if value_to_remove in thisset:
    thisset.remove(value_to_remove)
    print("Set after removing:", thisset)
else:
    print("Value not found in the set.")
