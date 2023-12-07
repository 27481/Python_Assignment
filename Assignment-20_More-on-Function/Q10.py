# 10. Write a python program to create a function to check whether a string is an anagram
# or not.

def check_anagram(str1, str2):
    str1=str1.lower().replace(" ","")
    str2=str2.lower().replace(" ","")
    return sorted(str1)==sorted(str2)





# Calling the above function 
sample_string_1=input("Enter the string to check if its anagram or not :\n")
sample_string_2=input("Enter the string to check if its anagram or not :\n")


if(check_anagram(sample_string_1, sample_string_2)):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")