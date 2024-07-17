def square(l):
    c=[]
    for i in l:
        j=i**2
        c.append(j)
    return c
l1=eval(input("e"))
print(square(l1))

def square1(n):
    return n**2
n=[1,2,3,4]
print(list(map(square1,n)))
