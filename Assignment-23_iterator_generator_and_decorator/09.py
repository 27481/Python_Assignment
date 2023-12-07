""" 

Define a function which takes lengths of three sides of a triangle as arguments and
display the perimeter or triangle. Define and apply a decorator which checks for the
validity of the triangle on the basis of lengths of the side. This makes the perimeter to
be displayed when the triangle can exist with the given lengths of the sides.

"""



# Decorator function to check the validity of the triangle
def check_valid_triangle(func):
    def wrapper(a, b, c):
        if a + b > c and b + c > a and c + a > b:
            print("Valid triangle!")
            return func(a, b, c)
        else:
            print("Invalid triangle! Cannot form a triangle with given side lengths.")
    return wrapper


# Function to calculate the perimeter of a triangle
@check_valid_triangle
def calculate_perimeter(a, b, c):
    perimeter = a + b + c
    print(f"Perimeter of the triangle: {perimeter}")

# Example usage:
side1 = 3
side2 = 4
side3 = 5

calculate_perimeter(side1, side2, side3)
