# Write a python program to create a function that takes a list and returns a new list
# with the original list's unique elements.


def Unique_element_list(givenList):
    stt=list(set(givenList))
    return stt





# Calling the function 
Lst=[1,2,3,4,5,6,6,6,6,6]

res=Unique_element_list(Lst)
print(res)
