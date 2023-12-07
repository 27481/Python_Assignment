# Write down a python script to count digits in a given number 
def cnt(num):
     ct=0
     while(num>0):
        num=num//10
        ct+=1
     
     return ct


num=int(input("Enter the number whose digit you want to count :\n"))
print("Count of the digit is :\n", cnt(num))