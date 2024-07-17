from math import factorial as fact
a=int(input("enter no"))
for i in range(a):
    for k in range(a-i+1):
        print(end=" ")
    for j in range(i+1):
        a1=fact(i)/(fact(j)*fact(i-j))
        
        print(int(a1),end=" ")
    print("\n")


'''for j in range(a+1):
    b1=[]
    if j==0:
        l=1
        b1.append(l)
    if j>0:
        a1=11**j
        b1.append(a1)
    for i in range(len(b1)):
        print(b1[i],end=" ")
        print("\n")'''
            
