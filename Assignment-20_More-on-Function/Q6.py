# Write a python program to create a function and print a list where the values are
# square of numbers between 1 and 30.


def squareed_list(num):
    list=[]
    for i in range(1,num):
        if i%2==0:
            list.append(i)
    
    return list


# Calling function 
result=squareed_list(30)

print(result)