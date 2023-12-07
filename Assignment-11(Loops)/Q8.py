# Write a python scrip to calculate sum of digits of a given number


def cnt(num):
     sum=0
     while(num>0):
        lastdigit=num%10
        sum=sum+lastdigit
        num=num//10
     
     return sum


num=int(input("Enter the number whose Sum of digit you want to print:\n"))
print("The sum of digit that number is :\n", cnt(num))



# 2nd method by using List compherension