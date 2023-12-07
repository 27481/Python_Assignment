# Write a Python script to find the smallest number in a given list of numbers.

import sys

numberOfelements=int(input("Enter the number of elements which you want to put in list :\n"))

inputList=[]

for _ in range (numberOfelements):
    num=int(input("Enter a number :\n"))
    inputList.append(num)



# Initialize the maximum value in maxi
min_val= sys.maxsize

for i in inputList:
    if(i<min_val):
       min_val=i



print()
print("Smallest element in the list is :\n",min_val)
