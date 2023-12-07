# Write a Python script to print distinct elements along with their frequencies of
# occurrence in the list.





# we will use hash table i.e dictionary 
def fun(lst):
    freq=dict()

    for ele in lst:
        freq[ele]=lst.count(ele)

    return freq





list=[1,1,1,4,5,6,7,8,9,0.1,1,1]

print("The occurence of each element in the list is :\n",fun(list))