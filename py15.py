'''a=5>>1
print(a)

a1=10>>2
print(a1)

a2=10<<2
print(a2)

a3=~10
print(a3)

a4=10^8
print(a4)'''


a=int(input("enter no"))
s=0
for i in range(1,a):
    if a%i==0:
        s+=i
if s==a:
    print("perfect number")

