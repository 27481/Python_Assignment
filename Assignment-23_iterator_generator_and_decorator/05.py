# Create a generator to produce first n terms of Fibonacci series


def fib_generator(num):
    a=0
    b=1
    count=0

    while(count<num):
        yield a
        temp=a+b
        a=b
        b=temp
        count+=1






num=int(input("Enter the Nth number :\n"))

fib_gen=fib_generator(num)
print("The Fibonaci series upto{num} are :\n")

for i in fib_gen:
    print(i)