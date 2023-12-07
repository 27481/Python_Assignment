# Create an endless iterator using generator method to produce Prime numbers


def is_prime(num):
    if(num<2):
        return False
    
    for i in range(2, int(num**0.5)+1):
        if(num%i)==0:
            return False
        
    return True

def prime_numbers_generator(n):
    count=0
    num=2

    while(count<n):
        if(is_prime(num)):
            yield num
            count=count+1

        num=num+1


# Driver code 
num=int(input("Enter the Nth number upto which you want to generate prime number :\n"))

prime_gen=prime_numbers_generator(num)

for i in prime_gen:
    print(i)