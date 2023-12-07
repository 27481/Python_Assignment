# Write a python program to multiply all the numbers in a list.
# Write a python program to sum all the numbers in a list.

def multiply_all_the_numbers_of_lst(input_list):
    sum=1

    for i in input_list:
        sum=sum*i
    
    return sum



# Calling the above function 
temp_list=[1,2,5,4,5]
multiply=multiply_all_the_numbers_of_lst(temp_list)

print(multiply)
