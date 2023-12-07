# Write a python program to create a function that prints the even numbers from a
# given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]



def print_even_numbers(given_list):
    for int in given_list:
        if(int%2==0):
            print(int)




# Calling function
sample_lst=[1,2,3,4,5,6,7,8,9,10]

print_even_numbers(sample_lst)
