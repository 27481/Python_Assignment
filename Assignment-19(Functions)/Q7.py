# Write a python program to sum all the numbers in a list.

def sum_all_the_numbers_of_lst(input_list):
    sum=0

    for i in input_list:
        sum=sum+i
    
    return sum



# Calling the above function 
temp_list=[1,2,3,4,5]
summ=sum_all_the_numbers_of_lst(temp_list)

print(summ)
