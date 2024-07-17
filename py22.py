'''a=int(input("no"))
for i in (1,1+a):
    b=1
    for j in range(1,i+1):
        print(b,end=" ")
        b+=1
        print("\n")

'''


#1st way
a1=int(input("num:-"))
c=False
if a1>1:
    for i in range(2,a1):
        if a1%i==0:
            print("np")
            c=True
            break
    if c==False:
        print("p")
else:
    print("np")

#2nd way
a1=int(input("num:-"))
if a1>1:
    for i in range(2,a1):
        if a1%i==0:
            print("np")
            
            break
    else:
        print("p")
else:
    print("np")
    
#3rd way
while True:
    a1=int(input("num:-"))
    c=0
    if a1>1:
        for i in range(2,a1):
            if a1%i==0:
                c+=1
        if c>1:
            print("np")
        else:
            print("p")


'''
from primePy import primes
if primes.check(a1)==True:
    print("p")'''
