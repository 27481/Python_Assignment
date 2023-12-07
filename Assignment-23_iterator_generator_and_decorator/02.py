# Create a generator to produce first n odd natural numbers




def generate_odd_numbers(n):
    count=0
    num=1
    while(count<n):
        yield num
        num+=2 # Moving to the next odd number 
        count+=1





n=int(input("Enter the value of n:\n"))

# Calling the generator function 
res=generate_odd_numbers(n)
print(f"The first {n} odd natural numbers are :\n")


for i in res:
    print(i)

