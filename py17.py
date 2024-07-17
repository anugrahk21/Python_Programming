x=int(input("enter number"))
for i in range(1,x+1):
    for j in range(1,i+1):
        print(j,end=" ")
    for k in range(i-1,0,-1):
        print(k,end=" ")
    print("\n")




y=int(input("enter number"))
for i in range(1,y+1):
    for j in range(1,i+1):
        print(j,end=" ")
    for k in range(1,i):
        print(k,end=" ")
    print("\n")


'''
a=int(input("enter year"))
if a%4==0 or a%400==0 and a%100==0:
    print("leap year")
else:
    print("not leap year")'''

'''

a=int(input("enter no"))
c=0
for i in range(1,a+1):
    if i%3==0 or i%5==0:
        c+=i       
print(c)
'''
