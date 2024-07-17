'''
a=input("enter value")
a1=a[::-1]
a2=[a]
if a in a1 and a2:
    print("paliandrome")
else:
    print("not paliandrome")



list1=[1,2,3]
list2=["a","b","c"]
a3=dict(zip(list1,list2))
print(a3)



x="hello"
print(x[1:2:4])


'''
b1=int(input("enter no"))
b=len(str(b1))
c=0
for i in str(b1):
    c+=int(i)**b
if c==b1:
    print("amstrong")
else:
    print("not amstrong")

'''

x=int(input("enter number"))
for i in range(1,x+1):
    for j in range(1,i):
        print(j,end=" ")
    print("\n")
'''


