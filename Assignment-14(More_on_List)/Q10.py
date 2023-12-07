# Write a python script to sort a list.


def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        swapped=False

        for j in range(0, n-i-1):
         # Swap if elements found is greater than the next element
         if(arr[j]>arr[j+1]):
            # arr[j], arr[j+1] = arr[j+1], arr[i]
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
            swapped=True


        if not swapped:
           break



# Driver code 
noOfelement=int(input("Enter the number of elements which you want to put :\n"))

Lst=[]

for i in range (0, noOfelement):
   print("Enter",i,"element")
   num=int(input())
   Lst.append(num)
   

bubble_sort(Lst)

print("Sorted list using buble sort :\n", Lst)
