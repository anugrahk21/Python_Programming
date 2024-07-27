#exception

a=int(input())
for _ in range(a):
    try:
        b,c=map(int,input().split())
        d=b//c
        print(d)
    except Exception as e: # if error in try block it will go here
        print("Error Code:",e)   #the exception will we print here

    #there are many exceptions
    #like ZeroDivisionError, TypeError, ValueError, etc.
    #you can catch these exceptions and handle them accordingly