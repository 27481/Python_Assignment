# Write a python script to calculate sum of cubes of N natural number 
num=int(input("Enter the number :\n"))


def fun(num):
    cubeSum=0
    for i in range (num+1):
        cubeSum=cubeSum+(i*i*i)
    
    return cubeSum;



print("Enter the number upto which cubeSum you want to find out :\n", fun(num))

