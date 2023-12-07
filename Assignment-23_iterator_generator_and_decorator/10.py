# Define a function which calculates HCF of two numbers. Define and apply a
# decorator to check whether two given numbers are co-prime or not.




# Decorator function to check if two numbers are co-prime
def check_coprime(func):
    def wrapper(a, b):
        if hcf(a, b) == 1:
            print(f"{a} and {b} are co-prime numbers.")
        else:
            print(f"{a} and {b} are not co-prime numbers.")
        return func(a, b)
    return wrapper

# Function to calculate HCF (GCD) of two numbers
def hcf(a, b):
    while b:
        a, b = b, a % b
    return a

# Applying the decorator to check co-prime numbers
@check_coprime
def calculate_hcf(a, b):
    return hcf(a, b)

# Example usage:
num1 = 15
num2 = 28
calculate_hcf(num1, num2)
