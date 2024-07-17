def fun1(*num):
   a=sum(num)
   return a
def fun2(*num):
    b=max(num)
    return b
def fun3(*num):
    c=min(num)
    return c
def fun4(*num):
    d=num*2
    return d
def fun5(*num):
    e=num**2
    return e
print(fun1(1,2,3,4,5,6,7,8,9))
print(fun2(1,2,3,4,5,6,7,8,9))
print(fun3(1,2,3,4,5,6,7,8,9))
print(fun4(1,2,3,4,5,6,7,8,9))
print(fun5(1,2,3,4,5,6,7,8,9))
