# Create an endless iterator using generator method to produce terms of Fibonacci
# series


def fibonacci_generator():
    a=0
    b=1
    
    while True:
        yield a
        temp=a
        a=b
        b=temp+b

# Example usage:
fib_gen = fibonacci_generator()

# Producing and printing the terms of the Fibonacci series indefinitely
for _ in range(10):  # Change 10 to the number of terms you want to print
    print(next(fib_gen))
