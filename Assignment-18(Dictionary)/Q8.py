# Write a python program to convert two lists into a dictionary in a way that item from
# list1 is the key and item from list2 is the value.


def list_to_dict(list1, list2):
    if(len(list1)!=len(list2)):
        raise ValueError("Lists must be of equal length")

    result_dict=dict(zip(list1, list2))
    return result_dict





# Driver code 
list1=['a','b','c']
list2=[1,2,3]

result=list_to_dict(list1, list2)
print(result)
       