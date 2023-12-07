# Write a python program to create a function that accepts a string and calculate the
# number of upper case letters and lower case letters.



def check_lowercase_n_uppercase(input_string):
    lower_char_count=0
    upper_char_count=0

    for char in input_string:
        if char.isupper():
            upper_char_count+=1
        elif char.islower():
            lower_char_count+=1
        
    return print(upper_char_count,lower_char_count)




# Calling the function
input_string=input("Enter the sample string :\n")

check_lowercase_n_uppercase(input_string)


