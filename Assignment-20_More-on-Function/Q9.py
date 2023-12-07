# Write a python program to create a function to check whether a string is a pangram
# or not.


def is_pangram(input_string):
    alphabet=set('abcdefghijklmnopqrstuvwxyz')

    # converting input string to lowercase and removing non-alphabetic characters

    input_string=input_string.lower()
    stt=set(input_string)

    return len(stt)>=26







# Calling the function
sample_string="The quick brown fox jumps over the lazy dog"

if(is_pangram(sample_string)):
    print(f'"{sample_string}" is a pangram')
else:
    print(f'"{sample_string}" is not a pangram')
