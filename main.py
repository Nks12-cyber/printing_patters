i = int(input("enter a number "))
boolean = int(input("enter 0 for fale and 1 for true "))
n=1
while(i!=0):
    if boolean==1:
        print("*"*n)
        n=n+1
    else:
        print("*"*i)
    i = i-1
