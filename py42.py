a=int(input("enter no.: "))
if a%2!=0:
    print("weird")
else:
    if a>=2 and a<=5:
        print("not weird")
    elif a>=6 and a<=20:
        print("weird")
    elif a>20:
        print("not weird")
