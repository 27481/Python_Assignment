# Create a generator to produce first n even natural numbers


def generate_eve_natural_number(n):
    count=0
    num=0

    while(count<n):
        yield num
        num=num+2
        count=count+1




num=int(input("Enter the Nth number :\n"))
res=generate_eve_natural_number(num)

print(f"The first natural {num} are :\n")
for i in res:
    print(i)