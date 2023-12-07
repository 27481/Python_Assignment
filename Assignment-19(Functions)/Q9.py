# Write a python program to create a function to check whether a number falls in a
# given range.



def check_in_range(num,lowerBound, UpperBound):
    return Lower_bound<=num<=Upper_bound




# Calling main function
num=int(input("Enter the number to check L :\n"))
Lower_bound=int(input("Enter the Lower_bound of the range :\n"))
Upper_bound=int(input("Enter the Upper_bound of the range :\n"))



res=check_in_range(num,Lower_bound,Upper_bound)


print(res)