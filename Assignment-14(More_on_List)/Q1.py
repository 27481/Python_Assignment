# Write a Python script to create a list of first N natural numbers.


num=int(input("Enter the List elements :\n"))

list=[];

for i in range (1, num+1):
    list.append(i)


print(list);


# By doing list comphrension 
num =int(input("Enter the number of elements :\n"))
list_of_Natural_numbers=[i for i in range(1, num+1)]

print(list_of_Natural_numbers)