# write a python script to cprint binary equivalent of a given decimal number do not use bin() method 



def converIntoBianry(num): 
    s=''
    while num>0:
        s=str(num%2)+s
        num=num//2
    
    rev=s[::1]
    return rev




num=int(input("enter the decimal number which you want to convert into binary :\n"))


print(f'The decimal number {num} in binary form is :\n', converIntoBianry(num));

