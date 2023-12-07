# Write a Python script to calculate the sum of elements in a given list of numbers.

numberOfelements=int(input("Enter the number of elements you want to put in list :\n"))

inputList=[]

for i in range (numberOfelements):
    print("Enter the",i,"element:\n")
    num=int(input())
    inputList.append(num)



sum=0

for i in range (0,numberOfelements):
    sum=sum+inputList[i]


print("Sum of nth elements :\n",sum)