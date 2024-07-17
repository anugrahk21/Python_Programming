a=5
b=10
c=str(b)+"j"

d=complex(c)
print(a+d)
print(complex(a+d))
print(complex(a+b))

p=input("enter")

for i in p:
    s=p.count(i)
    if s==2:
        print("e")
print(p)


w=int(input("a"))
for i in range(1,w+1):
    for j in range(i):
        print("*",end=" ")
    print()
for k in range(w-1,0,-1):
    for m in range(k):
        print("*",end=" ")
    print()

