# Write a python program to check if all items in the tuple are the same.


t1=(5,5,5,5,5)

# t2=(10,20,30,40,50)


result=all(item==t1[0] for item in t1)


if(result):
    print("All items  in the tuple are the same ")
else:
    print("All items in the tuple are not same")