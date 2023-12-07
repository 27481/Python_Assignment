# Write a python program to create a function that checks whether a passed string is
# palindrome or not.



def check_palindrom(input_string):
    length=len(input_string)

    for i in range(0, length//2):
        if(input_string[i]!=input_string[length-i-1]):
            return False
    
    return True


# Calling the function 
input_string=input("Enter the string to check if its palindrome or not :\n")

res=check_palindrom(input_string)
print(res)

