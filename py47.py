#write a programme to print the fibonacci numbers

def fibonacci():
    p=10
    n=1
    j=0
    print(j)
    for i in range(p-1): # already printed the first number
        print(n)
        j,n=n,j+n # Update j and n simultaneously(j and n are updated based on their previous values)in 1st iteration j=1,n=0+1=1
fibonacci()