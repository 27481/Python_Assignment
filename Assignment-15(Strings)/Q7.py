# Write a python script to determine whether a string contains a specific substring

DemoString="bhupenderJogibhupenderJogibhupenderJogi"



substringTocheck=input("Enter the substring which you want to search for :\n")
result=substringTocheck in DemoString


if(result):
    print(f"The given substring '{substringTocheck}' is present in Demostring")
else:
    print(f"the given substring {substringTocheck} is not present in Demostring")
