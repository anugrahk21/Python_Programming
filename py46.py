#pattern
n=5
k=5
for i in range(n):
    for j in range(k):
        print("*",end=" ")
    print()
    k = k - 1

n=5
k=1
for i in range(n):
    for j in range(k):
        print("*",end=" ")
    print()
    k = k + 1

n=5
k=5
l=1
for i in range(n):
    for j in range(k):
        print(" ",end=" ")
    k=k-1
    for r in range(l):
        print("*",end=" ")
    l=l+1
    print()

n=5
k=5
l=1
for i in range(n):
    for j in range(k):
        print("*",end=" ")# in same line
    k=k-1
    for r in range(l):
        print(" ",end=" ")
    l=l+1
    print() #after doing whole code for one line we are going to the next line

n=5
k=5
l=1
h=0
for i in range(n):
    for j in range(k):
        print(" ",end=" ")
    k=k-1
    for r in range(l):
        print("*",end=" ")
    l=l+1
    for  f in range(h):
        print("*",end=" ")
    h=h+1
    print()

n=5
k=5
l=k-1
h=1
n=5
a=5
p=1
q=0
for i in range(n-1):
    for j in range(a-1):
        print(" ",end=" ")
    a=a-1
    for r in range(p):
        print("*",end=" ")
    p=p+1
    for  f in range(q):
        print("*",end=" ")
    q=q+1
    print()
for i in range(n):
    for  f in range(h-1):
        print(" ",end=" ")
    h=h+1
    for j in range(k):
        print("*",end=" ")
    k=k-1
    for r in range(l):
        print("*",end=" ")
    l=l-1

    print()
