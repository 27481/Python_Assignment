# Write a python program to add items from another set to the current set. thisset =
# {"Java", "Python", "SQL"}




thisset={"java","Python","SQL"}
another_set={"CPP","Rust","Golang"}


thisset.update(another_set)

print("Updated set is :\n", thisset)