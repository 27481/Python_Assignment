# Use iter and next method to access all the elements of a given set using while loop



my_set={2,1,0,0,5,4,1,5,3,0,0,5,1}
my_set_iterator=iter(my_set)


while True:
    try:
        element=next(my_set_iterator) 
        print(element)
    except StopIteration:
        break # exit the loop when all elements have been accessed 