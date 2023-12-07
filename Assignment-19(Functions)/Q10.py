# Write a python program to create a function to check whether a given number is even
# or odd.


def check(num):
    res= "even" if num%2==0 else "odd"
    return res



# Calling the above function 
num=int(input("Enter the number which you want to check :\n"))
res=check(num)
print(res)