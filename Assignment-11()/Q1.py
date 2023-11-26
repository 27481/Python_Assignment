# Write a python script to calculate sum of N natural numbers

num=int(input("Enter the nth number :\n"))

def sumOfNnumbers(num):
     sum=0
     for i in range(num+1):
          sum=sum+i;
  
     return sum

print("Sum till nth number is :\n",sumOfNnumbers(num))