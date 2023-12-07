# Write a python program to create a function that takes a number as a parameter and
# checks if the number is prime or not.

def Prime_or_not(num):
    count=0
    for i in range (0,num-1):
        if(i%num==0):
           count+=1
    
    if(count==1):




# Calling the function 
num=int(input("Enter the number to check whether prime or not :\n"))

res=Prime_or_not(num)
print(res)