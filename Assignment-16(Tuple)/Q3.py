# Write a python program to reverse the tuple.

elements=input("Enter the element which you want to reverse :\n").split()

given_tuple=tuple(elements)

reversed_tuple=given_tuple[::-1]

print("Before reversal :\n",given_tuple)
print("Reversed tuple :\n",reversed_tuple)

