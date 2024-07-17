a=int(input("num"))
'''p=0
q=1
r=0
while r<=a:
    print(r)
    p=q
    q=r
    r=p+q
'''

'''
print(p)
print(q)
for i in range(2,a+1):
    r=p+q
    print(r)
    p=q
    q=r'''

b=1
for i in range(1,a+1):
    b*=i
print(b)
j=str(b)
print(len(j))
