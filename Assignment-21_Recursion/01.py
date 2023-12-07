# Write a recursive python function to print first N natural numbers.



def recursive_func(given_number):
    if(given_number>0):
        recursive_func(given_number-1) # recursive call with n-1
        print(given_number)



# Calling the recursive function 
input_Nth_number=int(input("Enter the Nth number :\n"))

recursive_func(input_Nth_number)