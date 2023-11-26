#  Find factorial of given number 

def fact(num):
    fact=1
    for i in range(1, num+1):
        fact=fact*i

    return fact




num=int(input("Enter the number whose factorial you want to find out :\n"))

print(fact(num))



