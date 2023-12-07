# Write down a python script to print the octal equivalent of a given decimal number 
  # do not use oct() function 



def convertIntoOctal(num):
    if(num==0):
         return "0"
    
    octal=""

    while(num>0):
       rem=num%8
       octal=str(rem)+octal
       num=num//8
    
    return octal 


num=int(input("enter the decimal number which you want to convert into octal :\n"))

print(f'The decimal number {num} in binary form is :\n', convertIntoOctal(num));

