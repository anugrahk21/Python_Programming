'''a=lambda x:x**1/2
#1st way
num=eval(input("number"))
print(list(map(a,num)))


#2nd way
l=[]
c=1
b=int(input("no"))
for i in range(b):
    p=int(input("number",c))
    l.append(p)
    c+=1
print(list(map(a,l)))'''


def max1(*num1):
    print(max(num1))#parameter given here must be same as given in defining statement
max1(1,2,3)

def min1(*num2):
    print(min(num2))
min1(1,2,3)
