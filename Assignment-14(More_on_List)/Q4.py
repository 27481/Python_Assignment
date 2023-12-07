# Write a Python script to find the greatest number in a given list of numbers.

import sys

numberOfelements=int(input("Enter the number of elements which you want to put in list :\n"))

inputList=[]

for _ in range (numberOfelements):
    num=int(input("Enter a number :\n"))
    inputList.append(num)



# Initialize the maximum value to negative infinity
maxi = float("-inf")

for i in inputList:
    if(i>maxi):
      maxi=i



print()
print("Greatest element in the list is :\n",maxi)
