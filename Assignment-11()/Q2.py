# Write a python script to calculate sum of squares of first N natural numbers

num=int(input("Enter the number :\n"))


def fun(num):
    squareSum=0
    for i in range (num+1):
        squareSum=squareSum+i*i
    
    return squareSum;



print("Enter the number upto which  SquareSum you want to find out :\n", fun(num))

