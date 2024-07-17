a=input("a")
c=ord(a)+1
print(c)

a=input("enter")
b=[]
c=[]
l=[]
for i in a:
    b.append(i)
for j in a[::-1]:
    c.append(j)
for k in a:
    l.append(k)
print(l[::-1])
if c[::-1]==b:
    print("p")
print(b)
print(c)
print(a[::-1])

#max and min in a list
b1=eval(input("a"))
print(b1)
b1.sort()
print(b1[-1])
print(max(b1))
