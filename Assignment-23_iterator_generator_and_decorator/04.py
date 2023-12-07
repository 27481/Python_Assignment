# Create a generator to produce squares of first N natural numbers


def generator_for_even_natural_number(n):
    count=0
    num=1

    while(count<n):
        yield num*num
        count=count+1
        num=num+1






num=int(input("Enter the Nth number :\n"))

res=generator_for_even_natural_number(num)

print(f"The first natural number are {num} :\n")

for i in res:
    print(i)