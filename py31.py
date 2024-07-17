def square(a):
    return a**2
def cube(a):
    return a**3
def double(a):
    return a*2
def mul(a,b):
    return a*b
a=int(input("1st"))
b=int(input("2nd"))
print(square(double(cube(mul(a,b)))))


x=lambda y:y**2
y=2
print(x(y))

a=25
def abc():
    global a
    a=90
def cvv():
    a=6
    print(a)
print("before functions",a)
cvv()
print("after 2nd",a)
abc()
print("after 2st",a)
