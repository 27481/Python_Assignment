# Write a python script to calculate sum of first N odd natural numbers 




num=int(input("Enter the nth number :\n"))

def sumOfNoddnumbers(num):
     sum=0
     for i in range(num+1):
          if(i%2!=0):
           sum=sum+i
  
     return sum

print("Sum till nth number is :\n",sumOfNoddnumbers(num))