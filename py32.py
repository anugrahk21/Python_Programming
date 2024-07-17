s=input("a :")
print(s[-1]+s[1:len(s)-1]+s[0])#first and last swap
print(s[0:len(s)])
print(s[0:2])#first 2
print(s[-2:])#last 2
print(s[-1:-4:-1])

b=int(input("index :"))#remove the element of given index
if b>=len(s) or b<0:
    print("error")
else:
    print(s[0:b]+s[b+1:])
    
p=input("1")#first element of given 2 string
q=input("2")
if len(p)<=1 or len(q)<=1:
    print("null")
else:
    print(p[1:]+q[1:])


