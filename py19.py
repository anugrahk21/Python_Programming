a=int(input("no"))
b=int(input("no 2"))
'''if b>a:
    a,b=b,a
while b!=0:
    a,b=b,a%b
print(a)'''


x=1
y=2
while y<=min(a,b):
    if a%y==0 and b%y==0:
        x=y
    y+=1
print(x)
