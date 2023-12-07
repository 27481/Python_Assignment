# Write a python script to check if a string contains only characters of the alphabet.

strr=input("Enter the input string to check :\n")

if(strr.isalpha()):
    print("String contains only alphanumberic characters:\n")
else:
    print("String does not contain only alphanumeric characters it contains a mixture")